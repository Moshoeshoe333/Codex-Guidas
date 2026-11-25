"""Regression tests for legacy and migrated lesson ID allocation."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import importlib.util

ROOT_DIR = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("new_record", ROOT_DIR / "scripts" / "new_record.py")
assert SPEC and SPEC.loader
new_record = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(new_record)


class LessonAllocatorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.lessons = self.root / "01-lessons-learned" / "lessons"
        self.lessons.mkdir(parents=True)
        self.ledger = self.root / "01-lessons-learned" / "ledger.md"
        self.addCleanup(self.temp.cleanup)

    def write_ledger(self, ids: list[str], linked: bool = False) -> None:
        rows = ["| ID | Lesson | Origin | Evidence class | Reusable control |", "|---|---|---|---|---|"]
        for record_id in ids:
            first = f"[{record_id}](lessons/{record_id}.md)" if linked else record_id
            rows.append(f"| {first} | title | source | Derived | control |")
        self.ledger.write_text("\n".join(rows) + "\n", encoding="utf-8")

    def add_files(self, ids: list[str]) -> None:
        for record_id in ids:
            (self.lessons / f"{record_id}.md").write_text("record", encoding="utf-8")

    def test_a1_legacy_ledger_only_allocates_after_ledger(self):
        self.write_ledger([f"CG-{i:03d}" for i in range(1, 43)])
        self.assertEqual(new_record.next_id("lesson", root=self.root), "CG-043")

    def test_a2_migrated_records_and_linked_ledger_allocate_after_max(self):
        ids = [f"CG-{i:03d}" for i in range(1, 43)]
        self.write_ledger(ids, linked=True)
        self.add_files(ids)
        self.assertEqual(new_record.next_id("lesson", root=self.root), "CG-043")

    def test_a3_mixed_migration_uses_maximum_from_both_sources(self):
        self.write_ledger([f"CG-{i:03d}" for i in range(1, 43)])
        self.add_files([f"CG-{i:03d}" for i in range(1, 41)])
        self.assertEqual(new_record.next_id("lesson", root=self.root), "CG-043")

    def test_a4_file_ahead_of_ledger_never_reuses_id(self):
        self.write_ledger([f"CG-{i:03d}" for i in range(1, 43)])
        self.add_files([f"CG-{i:03d}" for i in range(1, 44)])
        self.assertEqual(new_record.next_id("lesson", root=self.root), "CG-044")

    def test_a5_duplicate_ledger_ids_fail_closed(self):
        self.write_ledger(["CG-001", "CG-001"])
        with self.assertRaisesRegex(ValueError, "Duplicate lesson ID"):
            new_record.next_id("lesson", root=self.root)

    def test_a5_malformed_ledger_id_fails_closed(self):
        self.write_ledger(["CG-001", "CG-ABC"])
        with self.assertRaisesRegex(ValueError, "Malformed lesson ID"):
            new_record.next_id("lesson", root=self.root)

    def test_a5_mismatched_link_id_and_filename_fails_closed(self):
        self.ledger.write_text(
            "| ID | Lesson | Origin | Evidence class | Reusable control |\n"
            "|---|---|---|---|---|\n"
            "| [CG-001](lessons/CG-002.md) | title | source | Derived | control |\n",
            encoding="utf-8",
        )
        with self.assertRaisesRegex(ValueError, "Inconsistent lesson link"):
            new_record.next_id("lesson", root=self.root)

    def test_a6_gap_allocates_max_plus_one_not_first_gap(self):
        self.write_ledger(["CG-001", "CG-003"])
        self.assertEqual(new_record.next_id("lesson", root=self.root), "CG-004")


if __name__ == "__main__":
    unittest.main()
