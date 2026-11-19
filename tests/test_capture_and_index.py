"""Regression tests for Codex-Guidas record capture and index generation."""

from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR / "scripts"))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


new_record = load_module("new_record", ROOT_DIR / "scripts" / "new_record.py")
build_index = load_module("build_index", ROOT_DIR / "scripts" / "build_index.py")


class NewRecordTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "01-lessons-learned" / "lessons").mkdir(parents=True)
        (self.root / "11-defect-intelligence").mkdir(parents=True)
        (self.root / "09-templates").mkdir(parents=True)
        (self.root / "01-lessons-learned" / "ledger.md").write_text(
            "| ID | Lesson | Origin | Evidence class | Reusable control |\n|---|---|---|---|---|\n", encoding="utf-8")
        (self.root / "11-defect-intelligence" / "README.md").write_text(
            "| Defect ID | Project | Severity | State | Summary | Source / evidence |\n|---|---|---|---|---|---|\n", encoding="utf-8")
        (self.root / "09-templates" / "lesson-template.md").write_text(
            "---\nid: \"CG-XXX\"\n---\n# CG-XXX — [Concise lesson title]\n", encoding="utf-8")
        (self.root / "11-defect-intelligence" / "defect-template.md").write_text(
            "---\nid: \"DEF-YYYY-NNN\"\n---\n# DEF-YYYY-NNN — [Short factual title]\n", encoding="utf-8")
        self.addCleanup(self.temp.cleanup)

    def test_quick_lesson_allocates_id_and_updates_index(self):
        path = new_record.create_record("lesson", "Evidence before assumption", "ScoutSA", True, root=self.root)
        self.assertEqual(path.name, "CG-001.md")
        content = path.read_text(encoding="utf-8")
        self.assertIn('status: "Proposed"', content)
        self.assertIn('source_path: "Unknown"', content)
        self.assertIn("# CG-001 — Evidence before assumption", content)
        self.assertIn("[CG-001](lessons/CG-001.md)", (self.root / "01-lessons-learned" / "ledger.md").read_text(encoding="utf-8"))

    def test_defect_defaults_to_provisional_s4_and_registers(self):
        path = new_record.create_record("defect", "Partial write", "SoulSyncMobile", True, root=self.root)
        content = path.read_text(encoding="utf-8")
        self.assertIn('severity: "S4"', content)
        self.assertIn("Provisional severity: S4", content)
        self.assertIn("[DEF-", (self.root / "11-defect-intelligence" / "README.md").read_text(encoding="utf-8"))

    def test_existing_id_is_not_overwritten(self):
        lessons = self.root / "01-lessons-learned" / "lessons"
        (lessons / "CG-001.md").write_text("existing", encoding="utf-8")
        path = new_record.create_record("lesson", "Next lesson", quick=True, root=self.root)
        self.assertEqual(path.name, "CG-002.md")


class BuildIndexTests(unittest.TestCase):
    def test_index_is_deterministic_and_preserves_explicit_tags(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            lessons = root / "01-lessons-learned" / "lessons"
            defects = root / "11-defect-intelligence"
            lessons.mkdir(parents=True)
            defects.mkdir(parents=True)
            (lessons / "CG-001.md").write_text(
                '---\nid: "CG-001"\nrecord_type: "lesson"\nstatus: "Proposed"\nprojects: ["ScoutSA"]\ntags: ["persistence", "atomicity"]\nlayer: "body"\ncomponent: "storage"\nfailure_mode: null\nseverity: null\nevidence_class: "Proposed"\nverification_status: "not-claimed"\norigin_date: null\nlast_reviewed: null\nverification_due: null\nsource_path: "Unknown"\nreview_scope: "test"\n---\n# CG-001 — Atomic storage writes\n',
                encoding="utf-8")
            result = build_index.build_index_data(root)
            self.assertEqual(result["record_count"], 1)
            self.assertEqual(result["records"][0]["tags"], ["persistence", "atomicity"])
            self.assertEqual(result["records"][0]["title"], "Atomic storage writes")


if __name__ == "__main__":
    unittest.main()
