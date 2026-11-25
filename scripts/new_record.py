#!/usr/bin/env python3
"""Allocate Codex-Guidas record IDs and create recoverable lesson or defect records."""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
import tempfile
from contextlib import contextmanager
from datetime import date
from pathlib import Path
from typing import Iterator

ROOT = Path(__file__).resolve().parents[1]
TRANSACTION_JOURNAL = ".codex-record-transaction.json"
TRANSACTION_LOCK = ".codex-record-transaction.lock"
LESSON_ID_RE = re.compile(r"CG-(\d{3})")
LESSON_LINK_RE = re.compile(r"\[(CG-\d{3})\]\(lessons/(CG-\d{3})\.md\)")


def _lesson_ids_from_ledger(path: Path) -> set[str]:
    """Read legacy bare IDs and migrated Markdown links from the lesson index."""
    if not path.is_file():
        raise ValueError(f"Cannot allocate a lesson ID: canonical lesson ledger is missing: {path}")
    lines = path.read_text(encoding="utf-8").splitlines()
    headers = [i for i, line in enumerate(lines) if line.strip().startswith("| ID |")]
    if len(headers) != 1:
        raise ValueError(
            f"Cannot allocate a lesson ID: expected exactly one '| ID |' table header in {path}; "
            f"found {len(headers)}"
        )
    ids: set[str] = set()
    for line_number, line in enumerate(lines[headers[0] + 1 :], start=headers[0] + 2):
        stripped = line.strip()
        if not stripped.startswith("|"):
            break
        if re.fullmatch(r"\|[\s|:-]+\|", stripped):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if not cells or not cells[0]:
            raise ValueError(f"Malformed lesson ID cell at {path}:{line_number}")
        first = cells[0]
        link = LESSON_LINK_RE.fullmatch(first)
        if link:
            if link.group(1) != link.group(2):
                raise ValueError(
                    f"Inconsistent lesson link ID and filename at {path}:{line_number}: {first}"
                )
            record_id = link.group(1)
        elif LESSON_ID_RE.fullmatch(first):
            record_id = first
        else:
            raise ValueError(
                f"Malformed lesson ID at {path}:{line_number}: {first!r}; "
                "expected CG-NNN or [CG-NNN](lessons/CG-NNN.md)"
            )
        if record_id in ids:
            raise ValueError(f"Duplicate lesson ID {record_id} in {path}:{line_number}")
        ids.add(record_id)
    return ids


def _lesson_ids_from_files(directory: Path) -> set[str]:
    """Read IDs from individual lesson filenames; reject malformed CG-prefixed files."""
    if not directory.exists():
        return set()
    ids: set[str] = set()
    for path in directory.glob("CG-*.md"):
        match = re.fullmatch(r"(CG-\d{3})\.md", path.name)
        if not match:
            raise ValueError(f"Malformed lesson record filename; expected CG-NNN.md: {path}")
        ids.add(match.group(1))
    return ids


def next_id(record_type: str, root: Path = ROOT, year: int | None = None) -> str:
    if record_type == "lesson":
        ledger = root / "01-lessons-learned" / "ledger.md"
        lessons = root / "01-lessons-learned" / "lessons"
        existing = _lesson_ids_from_ledger(ledger) | _lesson_ids_from_files(lessons)
        numbers = [int(record_id[-3:]) for record_id in existing]
        return f"CG-{max(numbers, default=0) + 1:03d}"
    if record_type != "defect":
        raise ValueError("record_type must be lesson or defect")
    current_year = year or date.today().year
    paths = (root / "11-defect-intelligence").glob(f"DEF-{current_year}-*.md")
    numbers = [
        int(match.group(1))
        for path in paths
        if (match := re.fullmatch(rf"DEF-{current_year}-(\d{{3}})(?:-.+)?", path.name))
    ]
    return f"DEF-{current_year}-{max(numbers, default=0) + 1:03d}"


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")
    return slug[:64].rstrip("-") or "untitled"


def frontmatter(record_id: str, record_type: str, project: str | None, severity: str,
                tags: list[str], source_path: str, observed_on: str | None) -> str:
    is_lesson = record_type == "lesson"
    metadata = [
        ("id", record_id),
        ("record_type", record_type),
        ("status", "Proposed" if is_lesson else "New"),
        ("projects", [project] if project else []),
        ("layer", "unknown"),
        ("component", None),
        ("failure_mode", None),
        ("severity", None if is_lesson else severity),
        ("origin_date", observed_on),
        ("last_reviewed", None),
        ("verification_due", None),
        ("evidence_class", "Proposed intake; source review pending" if is_lesson else "Reported; reproduction pending"),
        ("verification_status", "not-claimed"),
        ("evidence_refs", []),
        ("author", None),
        ("auditor", None),
        ("ratified_by", None),
        ("assurance_level", "unassessed"),
        ("source_path", source_path or "Unknown"),
        ("review_scope", "quick capture; source evidence, applicability and current status not yet independently reviewed"),
        ("tags", tags),
    ]
    lines = [
        f"{key}: " + ("null" if value is None else json.dumps(value, ensure_ascii=False))
        for key, value in metadata
    ]
    return "---\n" + "\n".join(lines) + "\n---\n"


def quick_body(record_id: str, record_type: str, title: str, severity: str) -> str:
    if record_type == "lesson":
        return f"""\n# {record_id} — {title}

**Status:** Proposed intake; evidence and applicability review pending.  
**Captured on:** {date.today().isoformat()}

## Observation / proposed principle
[What happened or what principle is being proposed? Keep fact and interpretation separate.]

## Evidence and provenance
- Source artifact / commit / report: Unknown
- Evidence class and limitation: Not yet reviewed

## Applicability
- Relevant project/context:
- Where this may not apply:

## Residual risk and next review
[What remains uncertain, and what is the smallest next verification?]
"""
    return f"""\n# {record_id} — {title}

**State:** New  
**Provisional severity:** {severity} — re-triage when impact evidence is available.  
**Captured on:** {date.today().isoformat()}

## Observed signal
[Record the original signal without converting a hypothesis into a fact.]

## Evidence
- Exact source / commit / command / environment: Unknown
- Evidence entry or explicit gap: No artifact linked yet

## Impact and residual risk
[Separate demonstrated impact from potential impact. State what remains exposed or unknown.]

## Next discriminating check
[What is the smallest check that could distinguish plausible explanations?]
"""


def _insert_table_row_text(original: str, header_prefix: str, row: str, source: str) -> str:
    lines = original.splitlines()
    header_index = next((i for i, line in enumerate(lines) if line.startswith(header_prefix)), None)
    if header_index is None:
        raise ValueError(f"Could not find register table in {source}")
    end = header_index + 1
    while end < len(lines) and lines[end].startswith("|"):
        end += 1
    lines.insert(end, row)
    return "\n".join(lines).rstrip() + "\n"


def _fsync_directory(directory: Path) -> None:
    descriptor = os.open(directory, os.O_RDONLY)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def _atomic_write(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary_name = None
    try:
        with tempfile.NamedTemporaryFile(mode="wb", dir=path.parent,
                                         prefix=f".{path.name}.", suffix=".tmp",
                                         delete=False) as temporary:
            temporary_name = temporary.name
            temporary.write(content)
            temporary.flush()
            os.fsync(temporary.fileno())
        os.replace(temporary_name, path)
        _fsync_directory(path.parent)
    finally:
        if temporary_name and os.path.exists(temporary_name):
            os.unlink(temporary_name)


def _write_transaction_journal(root: Path, journal: dict) -> None:
    payload = json.dumps(journal, sort_keys=True, separators=(",", ":")).encode("utf-8")
    _atomic_write(root / TRANSACTION_JOURNAL, payload)


def _remove_transaction_journal(root: Path) -> None:
    journal = root / TRANSACTION_JOURNAL
    if journal.exists():
        journal.unlink()
        _fsync_directory(root)


def _replace_transaction_file(path: Path, content: bytes) -> None:
    _atomic_write(path, content)


def _safe_journal_path(root: Path, relative: str) -> Path:
    candidate = Path(relative)
    if candidate.is_absolute() or not relative or ".." in candidate.parts:
        raise ValueError(f"Unsafe path in transaction journal: {relative!r}")
    root_resolved = root.resolve()
    resolved = (root / candidate).resolve()
    if not resolved.is_relative_to(root_resolved):
        raise ValueError(f"Transaction journal path escapes repository root: {relative!r}")
    return resolved


def _validated_journal(root: Path) -> dict:
    journal_path = root / TRANSACTION_JOURNAL
    try:
        journal = json.loads(journal_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"Cannot read transaction journal: {exc}") from exc
    if not isinstance(journal, dict) or journal.get("version") != 1:
        raise ValueError("Unsupported or malformed transaction journal version")
    if journal.get("state") not in {"prepared", "committed"}:
        raise ValueError("Unknown transaction journal state")
    entries = journal.get("entries")
    if not isinstance(entries, list) or not entries:
        raise ValueError("Transaction journal entries must be a non-empty list")
    seen: set[str] = set()
    for entry in entries:
        if not isinstance(entry, dict) or set(entry) != {"path", "existed", "original_b64"}:
            raise ValueError("Malformed transaction journal entry")
        relative = entry["path"]
        if not isinstance(relative, str) or relative in seen:
            raise ValueError("Malformed or duplicate transaction journal path")
        seen.add(relative)
        _safe_journal_path(root, relative)
        if not isinstance(entry["existed"], bool):
            raise ValueError("Malformed transaction journal existence marker")
        if entry["existed"]:
            if not isinstance(entry["original_b64"], str):
                raise ValueError("Missing original bytes in transaction journal")
            try:
                base64.b64decode(entry["original_b64"], validate=True)
            except (ValueError, base64.binascii.Error) as exc:
                raise ValueError("Invalid original bytes in transaction journal") from exc
        elif entry["original_b64"] is not None:
            raise ValueError("Unexpected original bytes for a previously absent file")

    lesson_pair = (
        "01-lessons-learned/ledger.md" in seen
        and any(re.fullmatch(r"01-lessons-learned/lessons/CG-\\d{3}\\.md", item) for item in seen)
    )
    defect_pair = (
        "11-defect-intelligence/README.md" in seen
        and any(re.fullmatch(r"11-defect-intelligence/DEF-\\d{4}-\\d{3}(?:-[a-z0-9-]+)?\\.md", item) for item in seen)
    )
    if len(seen) != 2 or not (lesson_pair or defect_pair):
        raise ValueError("Transaction journal paths are not an approved record/index pair")
    return journal


def _rollback_transaction(root: Path, journal: dict) -> None:
    for entry in reversed(journal["entries"]):
        path = _safe_journal_path(root, entry["path"])
        if entry["existed"]:
            original = base64.b64decode(entry["original_b64"], validate=True)
            _atomic_write(path, original)
        elif path.exists():
            path.unlink()
            _fsync_directory(path.parent)


def _recover_pending_transaction_unlocked(root: Path) -> None:
    journal_path = root / TRANSACTION_JOURNAL
    if not journal_path.exists():
        return
    journal = _validated_journal(root)
    if journal["state"] == "prepared":
        _rollback_transaction(root, journal)
    _remove_transaction_journal(root)


@contextmanager
def _transaction_lock(root: Path) -> Iterator[None]:
    root.mkdir(parents=True, exist_ok=True)
    lock_path = root / TRANSACTION_LOCK
    try:
        descriptor = os.open(lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError as exc:
        raise RuntimeError(
            f"Record transaction lock already exists at {lock_path}; verify no writer is active "
            "before manually removing a stale lock"
        ) from exc
    try:
        os.write(descriptor, f"pid={os.getpid()}\n".encode("ascii"))
        os.fsync(descriptor)
        yield
    finally:
        os.close(descriptor)
        try:
            lock_path.unlink()
            _fsync_directory(root)
        except FileNotFoundError:
            pass


def recover_pending_transaction(root: Path = ROOT) -> None:
    """Recover or clean a prior transaction while holding the repository lock."""
    with _transaction_lock(root):
        _recover_pending_transaction_unlocked(root)


def _apply_transaction_unlocked(root: Path, updates: dict[Path, bytes]) -> None:
    entries = []
    for path, _content in updates.items():
        resolved = path.resolve()
        if not resolved.is_relative_to(root.resolve()):
            raise ValueError(f"Transaction destination is outside repository root: {path}")
        existed = resolved.exists()
        original = resolved.read_bytes() if existed else None
        entries.append({
            "path": resolved.relative_to(root.resolve()).as_posix(),
            "existed": existed,
            "original_b64": base64.b64encode(original).decode("ascii") if existed else None,
        })
    journal = {"version": 1, "state": "prepared", "entries": entries}
    try:
        _write_transaction_journal(root, journal)
        for path, content in updates.items():
            _replace_transaction_file(path.resolve(), content)
        journal["state"] = "committed"
        _write_transaction_journal(root, journal)
    except Exception as transaction_error:
        if (root / TRANSACTION_JOURNAL).exists():
            try:
                pending = _validated_journal(root)
                if pending["state"] == "committed":
                    raise RuntimeError(
                        "The committed marker is visible but a filesystem durability error occurred; "
                        "the journal is preserved and the transaction outcome requires inspection"
                    ) from transaction_error
                _recover_pending_transaction_unlocked(root)
            except RuntimeError:
                raise
            except Exception as recovery_error:
                raise RuntimeError(
                    "Record transaction failed and automatic rollback also failed; "
                    "preserve the journal and inspect repository state before retrying"
                ) from recovery_error
        raise
    try:
        _remove_transaction_journal(root)
    except OSError:
        # The committed marker is durable. Keep the journal for safe cleanup next time.
        pass


def insert_table_row(path: Path, header_prefix: str, row: str) -> None:
    """Compatibility helper; transaction-aware creation uses in-memory text updates."""
    original = path.read_text(encoding="utf-8")
    updated = _insert_table_row_text(original, header_prefix, row, str(path))
    _atomic_write(path, updated.encode("utf-8"))


def create_record(record_type: str, title: str, project: str | None = None, quick: bool = False,
                  severity: str = "S4", tags: list[str] | None = None, source_path: str = "Unknown",
                  observed_on: str | None = None, root: Path = ROOT) -> Path:
    if record_type not in {"lesson", "defect"}:
        raise ValueError("record_type must be lesson or defect")
    if not title.strip():
        raise ValueError("title must not be empty")
    if observed_on:
        date.fromisoformat(observed_on)

    with _transaction_lock(root):
        _recover_pending_transaction_unlocked(root)
        record_id = next_id(record_type, root=root)
        if record_type == "lesson":
            target_dir = root / "01-lessons-learned" / "lessons"
            template_path = root / "09-templates" / "lesson-template.md"
            target = target_dir / f"{record_id}.md"
            index_path = root / "01-lessons-learned" / "ledger.md"
            header_prefix = "| ID |"
            row = f"| [{record_id}](lessons/{record_id}.md) | {title.strip().replace('|', '/')} | {project or 'Unknown'} | Proposed | To be completed during review. |"
        else:
            target_dir = root / "11-defect-intelligence"
            template_path = root / "11-defect-intelligence" / "defect-template.md"
            target = target_dir / f"{record_id}-{slugify(title)}.md"
            index_path = root / "11-defect-intelligence" / "README.md"
            header_prefix = "| Defect ID |"
            row = f"| [{record_id}]({target.name}) | {project or 'Unknown'} | {severity} (provisional) | New | {title.strip().replace('|', '/')} | Intake captured; evidence review pending |"
        if target.exists():
            raise FileExistsError(f"Refusing to overwrite existing record: {target}")

        metadata = frontmatter(record_id, record_type, project, severity, tags or [], source_path, observed_on)
        if quick:
            body = quick_body(record_id, record_type, title.strip(), severity)
        else:
            template = template_path.read_text(encoding="utf-8")
            if not template.startswith("---\n") or "\n---\n" not in template[4:]:
                raise ValueError(f"Template frontmatter is malformed: {template_path}")
            body = template.split("\n---\n", 1)[1].lstrip()
            body = body.replace("CG-XXX", record_id).replace("DEF-YYYY-NNN", record_id)
            body = body.replace("[Concise lesson title]", title.strip()).replace("[Short factual title]", title.strip())
            body = "\n" + body

        target_dir.mkdir(parents=True, exist_ok=True)
        original_index = index_path.read_text(encoding="utf-8")
        updated_index = _insert_table_row_text(original_index, header_prefix, row, str(index_path))
        updates = {
            target: (metadata + body).encode("utf-8"),
            index_path: updated_index.encode("utf-8"),
        }
        _apply_transaction_unlocked(root, updates)
        return target


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a Codex-Guidas lesson or defect record.")
    parser.add_argument("record_type", choices=("lesson", "defect"))
    parser.add_argument("--title", required=True)
    parser.add_argument("--project")
    parser.add_argument("--quick", action="store_true", help="Create a minimal intake record for later expansion.")
    parser.add_argument("--severity", choices=("S0", "S1", "S2", "S3", "S4"), default="S4")
    parser.add_argument("--tag", action="append", default=[], help="Curated retrieval tag; may be repeated.")
    parser.add_argument("--source-path", default="Unknown")
    parser.add_argument("--observed-on", help="Known date first observed, YYYY-MM-DD; omitted remains Unknown/null.")
    args = parser.parse_args()
    try:
        path = create_record(args.record_type, args.title, args.project, args.quick, args.severity,
                             args.tag, args.source_path, args.observed_on)
    except (ValueError, FileExistsError, OSError, RuntimeError) as exc:
        print(f"Record creation failed: {exc}", file=sys.stderr)
        return 1
    print(f"Created {path.relative_to(ROOT)}")
    print("Review the record, evidence, residual risk and register entry before committing.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
