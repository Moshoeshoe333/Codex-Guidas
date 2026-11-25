"""Fault-injection tests for recoverable record/index transactions."""

from __future__ import annotations

import base64
import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT_DIR = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("new_record", ROOT_DIR / "scripts" / "new_record.py")
assert SPEC and SPEC.loader
new_record = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(new_record)


class RecordTransactionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        lessons = self.root / "01-lessons-learned" / "lessons"
        lessons.mkdir(parents=True)
        (self.root / "09-templates").mkdir()
        self.ledger = self.root / "01-lessons-learned" / "ledger.md"
        self.ledger.write_text(
            "| ID | Lesson | Origin | Evidence class | Reusable control |\n"
            "|---|---|---|---|---|\n"
            "| CG-001 | Existing | Test | Derived | Keep |\n",
            encoding="utf-8",
        )
        (self.root / "09-templates" / "lesson-template.md").write_text(
            "---\ntemplate: lesson\n---\n# CG-XXX — [Concise lesson title]\n",
            encoding="utf-8",
        )
        self.addCleanup(self.temp.cleanup)

    def create(self):
        return new_record.create_record(
            "lesson", "Transaction test", root=self.root, source_path="tests"
        )

    def snapshot(self):
        record_dir = self.root / "01-lessons-learned" / "lessons"
        return {
            "ledger": self.ledger.read_bytes(),
            "records": {
                path.name: path.read_bytes()
                for path in record_dir.glob("*.md")
            },
        }

    def test_w1_prepare_failure_leaves_destinations_unchanged(self):
        before = self.snapshot()
        with mock.patch.object(new_record, "_write_transaction_journal", side_effect=OSError("injected prepare failure")):
            with self.assertRaises(OSError):
                self.create()
        self.assertEqual(self.snapshot(), before)
        self.assertFalse((self.root / new_record.TRANSACTION_JOURNAL).exists())

    def test_w2_journal_is_prepared_before_first_replace(self):
        before = self.snapshot()

        def assert_prepared_then_fail(path, content):
            journal_path = self.root / new_record.TRANSACTION_JOURNAL
            self.assertTrue(journal_path.exists())
            import json
            self.assertEqual(json.loads(journal_path.read_text(encoding="utf-8"))["state"], "prepared")
            self.assertEqual(self.snapshot(), before)
            raise OSError("injected first replace failure")

        with mock.patch.object(new_record, "_replace_transaction_file", side_effect=assert_prepared_then_fail):
            with self.assertRaises(OSError):
                self.create()
        self.assertEqual(self.snapshot(), before)
        self.assertFalse((self.root / new_record.TRANSACTION_JOURNAL).exists())

    def test_w3_failure_after_record_replace_rolls_back_orphan(self):
        before = self.snapshot()
        original = new_record._replace_transaction_file
        calls = 0

        def fail_second(path, content):
            nonlocal calls
            calls += 1
            if calls == 2:
                raise OSError("injected index replace failure")
            return original(path, content)

        with mock.patch.object(new_record, "_replace_transaction_file", side_effect=fail_second):
            with self.assertRaises(OSError):
                self.create()
        self.assertEqual(self.snapshot(), before)
        self.assertFalse((self.root / new_record.TRANSACTION_JOURNAL).exists())

    def test_w4_failure_before_commit_marker_rolls_back_both_files(self):
        before = self.snapshot()
        original = new_record._write_transaction_journal
        calls = 0

        def fail_commit(root, journal):
            nonlocal calls
            calls += 1
            if calls == 2:
                raise OSError("injected commit marker failure")
            return original(root, journal)

        with mock.patch.object(new_record, "_write_transaction_journal", side_effect=fail_commit):
            with self.assertRaises(OSError):
                self.create()
        self.assertEqual(self.snapshot(), before)
        self.assertFalse((self.root / new_record.TRANSACTION_JOURNAL).exists())

    def test_w5_cleanup_failure_preserves_committed_state_and_recovers(self):
        with mock.patch.object(new_record, "_remove_transaction_journal", side_effect=OSError("injected cleanup failure")):
            created = self.create()
        self.assertTrue(created.exists())
        self.assertIn("CG-002", self.ledger.read_text(encoding="utf-8"))
        journal_path = self.root / new_record.TRANSACTION_JOURNAL
        self.assertTrue(journal_path.exists())
        new_record.recover_pending_transaction(self.root)
        self.assertFalse(journal_path.exists())
        self.assertTrue(created.exists())
        self.assertIn("CG-002", self.ledger.read_text(encoding="utf-8"))

    def test_w6_prepared_recovery_is_idempotent(self):
        record = self.root / "01-lessons-learned" / "lessons" / "CG-002.md"
        original_ledger = self.ledger.read_bytes()
        journal = {
            "version": 1,
            "state": "prepared",
            "entries": [
                {"path": "01-lessons-learned/lessons/CG-002.md", "existed": False, "original_b64": None},
                {"path": "01-lessons-learned/ledger.md", "existed": True, "original_b64": base64.b64encode(original_ledger).decode("ascii")},
            ],
        }
        new_record._write_transaction_journal(self.root, journal)
        record.write_text("partial record", encoding="utf-8")
        self.ledger.write_text("partial ledger", encoding="utf-8")
        new_record.recover_pending_transaction(self.root)
        first = self.snapshot()
        new_record.recover_pending_transaction(self.root)
        self.assertEqual(self.snapshot(), first)
        self.assertEqual(self.ledger.read_bytes(), original_ledger)
        self.assertFalse(record.exists())

    def test_w7_existing_lock_fails_closed_without_mutation(self):
        before = self.snapshot()
        lock = self.root / new_record.TRANSACTION_LOCK
        lock.write_text("another writer", encoding="utf-8")
        with self.assertRaisesRegex(RuntimeError, "lock"):
            self.create()
        self.assertEqual(self.snapshot(), before)

    def test_w8_malformed_or_traversal_journal_fails_closed(self):
        journal_path = self.root / new_record.TRANSACTION_JOURNAL
        journal_path.write_text(
            '{"version":1,"state":"prepared","entries":[{"path":"../outside","existed":false,"original_b64":null}]}',
            encoding="utf-8",
        )
        before = self.snapshot()
        with self.assertRaisesRegex(ValueError, "journal|path|transaction"):
            new_record.recover_pending_transaction(self.root)
        self.assertEqual(self.snapshot(), before)
        self.assertTrue(journal_path.exists())

        # A path inside the repository is still forbidden unless it is the
        # expected record/index pair; recovery must not be a generic file writer.
        journal_path.write_text(
            '{"version":1,"state":"prepared","entries":['
            '{"path":"README.md","existed":false,"original_b64":null},'
            '{"path":"01-lessons-learned/ledger.md","existed":true,"original_b64":"eA=="}]}',
            encoding="utf-8",
        )
        with self.assertRaisesRegex(ValueError, "approved record/index pair"):
            new_record.recover_pending_transaction(self.root)
        self.assertTrue(journal_path.exists())

        # An approved-looking record path must not resolve through a symlink
        # to a different file inside the repository.
        link = self.root / "01-lessons-learned" / "lessons" / "CG-999.md"
        link.symlink_to(self.root / "README.md")
        journal_path.write_text(
            '{"version":1,"state":"prepared","entries":['
            '{"path":"01-lessons-learned/lessons/CG-999.md","existed":false,"original_b64":null},'
            '{"path":"01-lessons-learned/ledger.md","existed":true,"original_b64":"eA=="}]}',
            encoding="utf-8",
        )
        with self.assertRaisesRegex(ValueError, "Symlinked"):
            new_record.recover_pending_transaction(self.root)
        self.assertTrue(journal_path.exists())
        self.assertTrue(link.is_symlink())


if __name__ == "__main__":
    unittest.main()
