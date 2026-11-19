"""Regression tests for the Codex-Guidas search and integrity CLI."""

from __future__ import annotations

import importlib.util
import io
import json
import tempfile
import unittest
from argparse import Namespace
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "codex.py"
SPEC = importlib.util.spec_from_file_location("codex_cli", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Unable to load CLI module from {SCRIPT}")
codex = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(codex)


def frontmatter(metadata: dict) -> str:
    lines = []
    for key, value in metadata.items():
        if value is None:
            raw = "null"
        elif isinstance(value, (str, list, dict, bool, int, float)):
            raw = json.dumps(value)
        else:
            raise TypeError(f"Unsupported test metadata value for {key}: {value!r}")
        lines.append(f"{key}: {raw}")
    return "---\n" + "\n".join(lines) + "\n---\n"


def lesson_metadata(record_id: str = "CG-001") -> dict:
    return {
        "id": record_id,
        "record_type": "lesson",
        "status": "Derived",
        "projects": ["SampleProject"],
        "layer": "mind",
        "component": "domain-model",
        "failure_mode": None,
        "severity": None,
        "origin_date": None,
        "last_reviewed": "2026-11-19",
        "verification_due": None,
        "evidence_class": "Derived",
        "verification_status": "not-claimed",
        "source_path": "source.md",
        "review_scope": "CLI regression test fixture",
    }


def defect_metadata(record_id: str = "DEF-2026-001") -> dict:
    return {
        "id": record_id,
        "record_type": "defect",
        "status": "Investigating",
        "projects": ["SOULSYNCMOBILE"],
        "layer": "body",
        "component": "persistence",
        "failure_mode": "storage read failure",
        "severity": "S4",
        "origin_date": "2026-11-18",
        "last_reviewed": "2026-11-19",
        "verification_due": "2026-12-19",
        "evidence_class": "Source-observed",
        "verification_status": "pending",
        "source_path": "source.md",
        "review_scope": "CLI regression test fixture",
    }


class CodexCliTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.lessons = self.root / "01-lessons-learned" / "lessons"
        self.defects = self.root / "11-defect-intelligence"
        self.lessons.mkdir(parents=True)
        self.defects.mkdir(parents=True)
        self.lesson_index = self.root / "01-lessons-learned" / "ledger.md"
        self.lesson_index.parent.mkdir(parents=True, exist_ok=True)
        self.defect_ledger = self.defects / "ledger.md"
        self.patchers = [
            patch.object(codex, "ROOT", self.root),
            patch.object(codex, "LESSONS", self.lessons),
            patch.object(codex, "LESSON_INDEX", self.lesson_index),
            patch.object(codex, "DEFECTS", self.defects),
            patch.object(codex, "DEFECT_LEDGER", self.defect_ledger),
        ]
        for patcher in self.patchers:
            patcher.start()
            self.addCleanup(patcher.stop)
        self.addCleanup(self.temp.cleanup)

    def write_record(self, path: Path, metadata: dict, body: str = "A test record."):
        path.parent.mkdir(parents=True, exist_ok=True)
        record_id = metadata["id"]
        path.write_text(
            frontmatter(metadata) + f"\n# {record_id} — Test record\n\n{body}\n",
            encoding="utf-8",
        )

    def test_frontmatter_parses_json_quoted_values_and_null(self):
        metadata = lesson_metadata()
        parsed, body = codex.read_frontmatter(
            self.write_text("sample.md", frontmatter(metadata) + "# Body\n")
        )
        self.assertEqual(parsed["id"], "CG-001")
        self.assertIsNone(parsed["failure_mode"])
        self.assertEqual(parsed["projects"], ["SampleProject"])
        self.assertIn("# Body", body)

    def test_frontmatter_rejects_duplicate_keys(self):
        path = self.root / "duplicate.md"
        path.write_text("---\nid: \"CG-001\"\nid: \"CG-002\"\n---\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "duplicate metadata key"):
            codex.read_frontmatter(path)

    def test_validator_accepts_valid_lesson_and_index(self):
        self.write_record(self.lessons / "CG-001.md", lesson_metadata(), "storage hydration ledger")
        self.lesson_index.write_text("[CG-001](lessons/CG-001.md)\n", encoding="utf-8")
        output = io.StringIO()
        with redirect_stdout(output):
            result = codex.validate_records()
        self.assertEqual(result, 0)
        self.assertIn("1 lessons, 0 defect files", output.getvalue())

    def test_validator_rejects_duplicate_record_ids(self):
        self.write_record(self.lessons / "CG-001.md", lesson_metadata())
        duplicate = lesson_metadata()
        duplicate["id"] = "CG-001"
        self.write_record(self.lessons / "CG-002.md", duplicate)
        self.lesson_index.write_text(
            "[CG-001](lessons/CG-001.md)\n[CG-002](lessons/CG-002.md)\n",
            encoding="utf-8",
        )
        output = io.StringIO()
        with redirect_stdout(output):
            result = codex.validate_records()
        self.assertEqual(result, 1)
        self.assertIn("duplicate ID CG-001", output.getvalue())

    def test_search_finds_defect_by_terms_and_project(self):
        record = self.defects / "DEF-2026-001-storage-hydration.md"
        self.write_record(record, defect_metadata(), "storage hydration failure masked as an empty ledger")
        args = Namespace(
            query="hydration ledger",
            type="defect",
            project="SOULSYNCMOBILE",
            layer=None,
            component=None,
            failure_mode=None,
            tag=None,
        )
        output = io.StringIO()
        with redirect_stdout(output):
            result = codex.search(args)
        self.assertEqual(result, 0)
        self.assertIn("DEF-2026-001", output.getvalue())


    def test_search_filters_by_explicit_tag(self):
        metadata = lesson_metadata()
        metadata["tags"] = ["persistence", "atomicity"]
        self.write_record(self.lessons / "CG-001.md", metadata, "partial write storage")
        args = Namespace(
            query="partial write",
            type="lesson",
            project=None,
            layer=None,
            component=None,
            failure_mode=None,
            tag="atomicity",
        )
        output = io.StringIO()
        with redirect_stdout(output):
            result = codex.search(args)
        self.assertEqual(result, 0)
        self.assertIn("CG-001", output.getvalue())

    def test_review_queue_marks_past_due_record_overdue(self):
        record = self.defects / "DEF-2026-001-storage-hydration.md"
        self.write_record(record, defect_metadata())
        output = io.StringIO()
        with redirect_stdout(output):
            result = codex.review_queue(Namespace(as_of="2026-12-20"))
        self.assertEqual(result, 0)
        self.assertIn("OVERDUE since 2026-12-19", output.getvalue())

    def test_local_link_validator_finds_missing_target(self):
        source = self.root / "guide.md"
        source.write_text("[Missing](not-created.md)\n", encoding="utf-8")
        errors = codex.validate_local_links()
        self.assertTrue(any("not-created.md" in error for error in errors))

    def write_text(self, name: str, content: str) -> Path:
        path = self.root / name
        path.write_text(content, encoding="utf-8")
        return path


if __name__ == "__main__":
    unittest.main()
