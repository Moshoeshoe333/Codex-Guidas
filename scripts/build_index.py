#!/usr/bin/env python3
"""Build a deterministic JSON retrieval index from Codex-Guidas Markdown records."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from codex import ROOT, read_frontmatter


def build_index_data(root: Path = ROOT) -> dict:
    lesson_dir = root / "01-lessons-learned" / "lessons"
    defect_dir = root / "11-defect-intelligence"
    paths = sorted(lesson_dir.glob("CG-*.md")) + sorted(defect_dir.glob("DEF-*.md"))
    records = []
    for path in paths:
        metadata, body = read_frontmatter(path)
        title_line = next((line.strip() for line in body.splitlines() if line.startswith("# ")), "")
        title = title_line[2:].split(" — ", 1)[-1] if " — " in title_line else title_line.removeprefix("# ").strip()
        records.append({
            "id": metadata.get("id"),
            "record_type": metadata.get("record_type"),
            "title": title,
            "status": metadata.get("status"),
            "projects": metadata.get("projects", []),
            "tags": metadata.get("tags", []),
            "layer": metadata.get("layer"),
            "component": metadata.get("component"),
            "failure_mode": metadata.get("failure_mode"),
            "severity": metadata.get("severity"),
            "evidence_class": metadata.get("evidence_class"),
            "verification_status": metadata.get("verification_status"),
            "origin_date": metadata.get("origin_date"),
            "last_reviewed": metadata.get("last_reviewed"),
            "verification_due": metadata.get("verification_due"),
            "source_path": metadata.get("source_path"),
            "record_path": path.relative_to(root).as_posix(),
        })
    records.sort(key=lambda record: (record.get("id") or "", record.get("record_path") or ""))
    return {
        "schema_version": 1,
        "source_of_truth": "Markdown lesson and defect records",
        "record_count": len(records),
        "counts": {
            "lessons": sum(1 for item in records if item["record_type"] == "lesson"),
            "defects": sum(1 for item in records if item["record_type"] == "defect"),
        },
        "records": records,
    }


def render_index(root: Path = ROOT) -> str:
    return json.dumps(build_index_data(root), ensure_ascii=False, indent=2) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Build or check the Codex-Guidas JSON knowledge index.")
    parser.add_argument("--output", default="index/knowledge-index.json", help="Output path; relative paths are resolved from the repository root.")
    parser.add_argument("--check", action="store_true", help="Fail if the selected index differs from the Markdown records.")
    args = parser.parse_args()
    output = Path(args.output)
    if not output.is_absolute():
        output = ROOT / output
    output = output.resolve()
    expected = render_index()
    if args.check:
        if not output.exists():
            print(f"Index missing: {output}")
            return 1
        actual = output.read_text(encoding="utf-8")
        if actual != expected:
            print("Knowledge index is stale. Run: python scripts/build_index.py")
            return 1
        print(f"Knowledge index PASS: {output} is current.")
        return 0
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(expected, encoding="utf-8")
    print(f"Knowledge index written: {output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
