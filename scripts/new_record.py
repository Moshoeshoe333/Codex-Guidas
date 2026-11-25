#!/usr/bin/env python3
"""Allocate Codex-Guidas record IDs and create lesson or defect records."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
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
        record_id = match.group(1)
        if record_id in ids:
            raise ValueError(f"Duplicate lesson record ID {record_id} in {directory}")
        ids.add(record_id)
    return ids


def next_id(record_type: str, root: Path = ROOT, year: int | None = None) -> str:
    if record_type == "lesson":
        ledger = root / "01-lessons-learned" / "ledger.md"
        lessons = root / "01-lessons-learned" / "lessons"
        # During migration, the ledger and file projection overlap by design.
        # Allocate above the maximum in either source; never assume a missing
        # file projection means that a legacy ID is free.
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


def frontmatter(record_id: str, record_type: str, project: str | None, severity: str, tags: list[str], source_path: str, observed_on: str | None) -> str:
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
    lines = []
    for key, value in metadata:
        lines.append(f"{key}: " + ("null" if value is None else json.dumps(value, ensure_ascii=False)))
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


def insert_table_row(path: Path, header_prefix: str, row: str) -> None:
    lines = path.read_text(encoding="utf-8").splitlines()
    header_index = next((i for i, line in enumerate(lines) if line.startswith(header_prefix)), None)
    if header_index is None:
        raise ValueError(f"Could not find register table in {path}")
    end = header_index + 1
    while end < len(lines) and lines[end].startswith("|"):
        end += 1
    lines.insert(end, row)
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def create_record(record_type: str, title: str, project: str | None = None, quick: bool = False,
                 severity: str = "S4", tags: list[str] | None = None, source_path: str = "Unknown",
                 observed_on: str | None = None, root: Path = ROOT) -> Path:
    if record_type not in {"lesson", "defect"}:
        raise ValueError("record_type must be lesson or defect")
    if not title.strip():
        raise ValueError("title must not be empty")
    if observed_on:
        date.fromisoformat(observed_on)
    record_id = next_id(record_type, root=root)
    if record_type == "lesson":
        target_dir = root / "01-lessons-learned" / "lessons"
        template_path = root / "09-templates" / "lesson-template.md"
        target = target_dir / f"{record_id}.md"
    else:
        target_dir = root / "11-defect-intelligence"
        template_path = root / "11-defect-intelligence" / "defect-template.md"
        target = target_dir / f"{record_id}-{slugify(title)}.md"
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
    target.write_text(metadata + body, encoding="utf-8")
    if record_type == "lesson":
        ledger = root / "01-lessons-learned" / "ledger.md"
        row = f"| [{record_id}](lessons/{record_id}.md) | {title.strip().replace('|', '/')} | {project or 'Unknown'} | Proposed | To be completed during review. |"
        insert_table_row(ledger, "| ID |", row)
    else:
        register = root / "11-defect-intelligence" / "README.md"
        row = f"| [{record_id}]({target.name}) | {project or 'Unknown'} | {severity} (provisional) | New | {title.strip().replace('|', '/')} | Intake captured; evidence review pending |"
        insert_table_row(register, "| Defect ID |", row)
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
    except (ValueError, FileExistsError, OSError) as exc:
        print(f"Record creation failed: {exc}", file=sys.stderr)
        return 1
    print(f"Created {path.relative_to(ROOT)}")
    print("Review the record, evidence, residual risk and register entry before committing.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
