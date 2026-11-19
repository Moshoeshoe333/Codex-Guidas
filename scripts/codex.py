#!/usr/bin/env python3
"""Search and validate Codex-Guidas records using only the Python standard library."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
LESSONS = ROOT / "01-lessons-learned" / "lessons"
LESSON_INDEX = ROOT / "01-lessons-learned" / "ledger.md"
DEFECTS = ROOT / "11-defect-intelligence"
DEFECT_LEDGER = DEFECTS / "ledger.md"

LESSON_STATUSES = {"Observed", "Derived", "Proposed", "Verified", "Superseded"}
DEFECT_STATUSES = {
    "New", "Triaged", "Investigating", "Contained", "Fix proposed",
    "In verification", "Closed", "Blocked", "Won't fix", "Reopened",
}
LAYERS = {"mind", "body", "spirit", "infra", "process", "cross-cutting", "unknown"}
VERIFICATION = {"pending", "source-only", "not-claimed", "verified", "blocked"}
SEVERITIES = {"S0", "S1", "S2", "S3", "S4"}
REQUIRED = {
    "id", "record_type", "status", "projects", "layer", "component",
    "failure_mode", "severity", "origin_date", "last_reviewed",
    "verification_due", "evidence_class", "verification_status",
    "source_path", "review_scope",
}
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
ID_RE = re.compile(r"^(?:CG-\d{3}|DEF-\d{4}-\d{3})$")


def parse_scalar(raw: str):
    raw = raw.strip()
    if raw == "null":
        return None
    if raw.startswith('"') or raw.startswith("["):
        return json.loads(raw)
    return raw


def read_frontmatter(path: Path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    marker = text.find("\n---\n", 4)
    if marker < 0:
        raise ValueError("frontmatter closing delimiter not found")
    metadata = {}
    for line_number, line in enumerate(text[4:marker].splitlines(), start=2):
        if not line.strip():
            continue
        if ":" not in line:
            raise ValueError(f"invalid frontmatter line {line_number}")
        key, raw = line.split(":", 1)
        key = key.strip()
        if key in metadata:
            raise ValueError(f"duplicate metadata key: {key}")
        metadata[key] = parse_scalar(raw)
    body = text[marker + 5 :]
    return metadata, body


def record_paths():
    return sorted(LESSONS.glob("CG-*.md")) + sorted(DEFECTS.glob("DEF-*.md"))


def validate_date(value, field, path, errors):
    if value is None:
        return
    if not isinstance(value, str):
        errors.append(f"{path}: {field} must be an ISO date string or null")
        return
    try:
        date.fromisoformat(value)
    except ValueError:
        errors.append(f"{path}: invalid {field}: {value!r}")


def validate_local_links():
    errors = []
    for path in ROOT.rglob("*.md"):
        if any(part.startswith(".") for part in path.relative_to(ROOT).parts):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as exc:
            errors.append(f"{path.relative_to(ROOT)}: cannot read: {exc}")
            continue
        for target in LINK_RE.findall(text):
            target = target.strip().strip("<>")
            parsed = urlparse(target)
            if parsed.scheme or target.startswith("#") or not parsed.path:
                continue
            candidate = (path.parent / unquote(parsed.path)).resolve()
            if not candidate.exists():
                errors.append(f"{path.relative_to(ROOT)}: broken local link target {target!r}")
    return errors


def validate_records():
    errors = []
    seen = {}
    lessons = sorted(LESSONS.glob("CG-*.md"))
    defects = sorted(DEFECTS.glob("DEF-*.md"))
    if not lessons:
        errors.append("no individual lesson records found")

    for path in lessons + defects:
        rel = path.relative_to(ROOT).as_posix()
        try:
            meta, body = read_frontmatter(path)
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            errors.append(f"{rel}: {exc}")
            continue
        missing = sorted(REQUIRED - set(meta))
        if missing:
            errors.append(f"{rel}: missing required fields: {', '.join(missing)}")
            continue
        rid = meta.get("id")
        if not isinstance(rid, str) or not ID_RE.fullmatch(rid):
            errors.append(f"{rel}: invalid record ID {rid!r}")
        else:
            if rid in seen:
                errors.append(f"duplicate ID {rid}: {seen[rid]} and {rel}")
            seen[rid] = rel
            if path.parent == LESSONS and path.stem != rid:
                errors.append(f"{rel}: lesson filename stem must exactly match id {rid}")
            if path.parent == DEFECTS and path.stem != rid and not path.stem.startswith(rid + "-"):
                errors.append(f"{rel}: defect filename must be the ID or begin with ID plus a descriptive suffix: {rid}")
            heading = next((ln.strip() for ln in body.splitlines() if ln.startswith("# ")), "")
            if not heading.startswith("# " + rid + " —"):
                errors.append(f"{rel}: first heading must begin with '# {rid} —'")

        kind = "lesson" if path.parent == LESSONS else "defect"
        if meta.get("record_type") != kind:
            errors.append(f"{rel}: record_type must be {kind!r}")
        valid_status = LESSON_STATUSES if kind == "lesson" else DEFECT_STATUSES
        if meta.get("status") not in valid_status:
            errors.append(f"{rel}: invalid {kind} status {meta.get('status')!r}")
        if not isinstance(meta.get("projects"), list) or not all(isinstance(x, str) for x in meta["projects"]):
            errors.append(f"{rel}: projects must be an array of strings")
        if meta.get("layer") not in LAYERS:
            errors.append(f"{rel}: invalid layer {meta.get('layer')!r}")
        for field in ("component", "failure_mode"):
            if meta.get(field) is not None and not isinstance(meta.get(field), str):
                errors.append(f"{rel}: {field} must be a string or null")
        severity = meta.get("severity")
        if kind == "defect" and severity not in SEVERITIES:
            errors.append(f"{rel}: defect severity must be one of {sorted(SEVERITIES)}")
        if kind == "lesson" and severity is not None:
            errors.append(f"{rel}: lesson severity must be null unless formally assessed")
        for field in ("origin_date", "last_reviewed", "verification_due"):
            validate_date(meta.get(field), field, rel, errors)
        if meta.get("verification_status") not in VERIFICATION:
            errors.append(f"{rel}: invalid verification_status {meta.get('verification_status')!r}")
        if meta.get("verification_status") == "pending" and meta.get("verification_due") is None:
            errors.append(f"{rel}: pending verification requires verification_due")
        for field in ("evidence_class", "source_path", "review_scope"):
            if not isinstance(meta.get(field), str) or not meta[field].strip():
                errors.append(f"{rel}: {field} must be a non-empty string")

    index_text = LESSON_INDEX.read_text(encoding="utf-8") if LESSON_INDEX.exists() else ""
    indexed = re.findall(r"\[(CG-\d{3})\]\(lessons/(CG-\d{3})\.md\)", index_text)
    indexed_ids = [left for left, right in indexed if left == right]
    if len(indexed_ids) != len(set(indexed_ids)):
        errors.append("lesson index contains duplicate ID links")
    expected_ids = {p.stem for p in lessons}
    if set(indexed_ids) != expected_ids:
        errors.append(f"lesson index mismatch; missing={sorted(expected_ids-set(indexed_ids))}, extra={sorted(set(indexed_ids)-expected_ids)}")

    errors.extend(validate_local_links())
    if errors:
        print("Knowledge integrity validation FAILED:")
        for item in errors:
            print(" - " + item)
        return 1
    print(f"Knowledge integrity validation PASS: {len(lessons)} lessons, {len(defects)} defect files, unique IDs, required metadata, index coverage and local Markdown links.")
    return 0


def search_documents():
    paths = record_paths()
    if DEFECT_LEDGER.exists():
        paths.append(DEFECT_LEDGER)
    for path in paths:
        try:
            text = path.read_text(encoding="utf-8")
            if text.startswith("---\n"):
                meta, body = read_frontmatter(path)
            else:
                meta, body = {}, text
            if path == DEFECT_LEDGER:
                meta = {"id": "DEFECT-REGISTER", "record_type": "register", "status": "Active"}
            yield path, meta, body
        except (OSError, ValueError, json.JSONDecodeError):
            continue


def search(args):
    terms = [part.casefold() for part in args.query.split() if part]
    matches = []
    for path, meta, body in search_documents():
        if args.type and meta.get("record_type") != args.type:
            continue
        if args.project:
            projects = " ".join(meta.get("projects", [])) if isinstance(meta.get("projects"), list) else ""
            if args.project.casefold() not in (projects + " " + body).casefold():
                continue
        if args.layer and meta.get("layer") != args.layer:
            continue
        if args.component and args.component.casefold() not in str(meta.get("component") or "").casefold():
            continue
        if args.failure_mode and args.failure_mode.casefold() not in str(meta.get("failure_mode") or "").casefold():
            continue
        haystack = json.dumps(meta, ensure_ascii=False).casefold() + "\n" + body.casefold()
        if all(term in haystack for term in terms):
            matches.append((path, meta))
    if not matches:
        print("No matching records found. This is a retrieval result, not proof that no similar defect exists.")
        return 0
    for path, meta in matches:
        projects = ", ".join(meta.get("projects", [])) if isinstance(meta.get("projects"), list) else ""
        print(f"{meta.get('id', 'REGISTER')} | {meta.get('status', 'unclassified')} | {projects or 'project not tagged'} | {path.relative_to(ROOT)}")
    print(f"\n{len(matches)} matching document(s). Inspect evidence before treating a match as the same cause.")
    return 0


def review_queue(args):
    as_of = date.fromisoformat(args.as_of) if args.as_of else date.today()
    pending = []
    for path in record_paths():
        try:
            meta, _ = read_frontmatter(path)
        except (OSError, ValueError, json.JSONDecodeError):
            continue
        if meta.get("verification_status") != "pending":
            continue
        due_text = meta.get("verification_due")
        due = date.fromisoformat(due_text) if due_text else None
        if due is None:
            label = "NO DUE DATE"
        elif due < as_of:
            label = f"OVERDUE since {due.isoformat()}"
        elif due == as_of:
            label = f"DUE today ({due.isoformat()})"
        else:
            label = f"DUE {due.isoformat()}"
        pending.append((due or date.max, meta.get("id", path.stem), label, path))
    if not pending:
        print(f"No records are currently marked pending verification as of {as_of.isoformat()}.")
        return 0
    for _, rid, label, path in sorted(pending):
        print(f"{rid} | {label} | {path.relative_to(ROOT)}")
    print(f"\n{len(pending)} pending record(s). A due date is a review trigger, not proof of completion.")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Search and validate the Codex-Guidas knowledge base.")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("validate", help="Validate metadata, unique IDs, index and local links.")
    search_parser = sub.add_parser("search", help="Search lesson and defect records.")
    search_parser.add_argument("query", help="Space-separated terms; all terms must match.")
    search_parser.add_argument("--type", choices=("lesson", "defect", "register"))
    search_parser.add_argument("--project")
    search_parser.add_argument("--layer", choices=sorted(LAYERS))
    search_parser.add_argument("--component")
    search_parser.add_argument("--failure-mode")
    queue_parser = sub.add_parser("review-queue", help="List pending verifications and overdue follow-ups.")
    queue_parser.add_argument("--as-of", help="ISO date for deterministic review; defaults to today.")
    args = parser.parse_args()
    if args.command == "validate":
        return validate_records()
    if args.command == "search":
        return search(args)
    if args.command == "review-queue":
        return review_queue(args)
    return 2


if __name__ == "__main__":
    sys.exit(main())
