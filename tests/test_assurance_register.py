"""Tests for the audit-universe and invariant-operation registers."""
from __future__ import annotations
import copy, importlib.util, unittest
from datetime import date
from pathlib import Path
SCRIPT=Path(__file__).resolve().parents[1]/'scripts'/'assurance_register.py'
SPEC=importlib.util.spec_from_file_location('assurance_register',SCRIPT)
if SPEC is None or SPEC.loader is None: raise RuntimeError(f'Cannot load {SCRIPT}')
assurance=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(assurance)
class AssuranceRegisterTests(unittest.TestCase):
    def setUp(self):
        self.data,errors=assurance.load_repository()
        if errors: raise AssertionError('; '.join(errors))
        self.data=copy.deepcopy(self.data)
        self.ids=assurance.known_invariant_ids()
    def test_current_register_is_valid(self):
        self.assertEqual(assurance.validate_data(self.data,self.ids),[])
    def test_duplicate_asset_id_is_rejected(self):
        self.data['audit_assets'][1]['id']=self.data['audit_assets'][0]['id']
        self.assertTrue(any('duplicate audit asset id' in e for e in assurance.validate_data(self.data,self.ids)))
    def test_unknown_invariant_reference_is_rejected(self):
        self.data['invariant_controls'][0]['invariant_id']='INV-999'
        self.assertTrue(any('unknown invariant_id' in e for e in assurance.validate_data(self.data,self.ids)))
    def test_verified_control_requires_owner_and_evidence(self):
        self.data['invariant_controls'][0]['operating_status']='verified'
        errors=assurance.validate_data(self.data,self.ids)
        self.assertTrue(any('verified operation requires an assigned control owner' in e for e in errors))
        self.assertTrue(any('verified operation requires evidence_refs' in e for e in errors))
    def test_unresolved_evidence_reference_is_rejected(self):
        self.data['audit_assets'][0]['inventory_evidence_refs']=['CG-AU-EV-999']
        self.assertTrue(any('inventory_evidence_refs must resolve' in e for e in assurance.validate_data(self.data,self.ids)))
    def test_review_queue_is_date_ordered(self):
        rows=assurance.review_queue(self.data,date(2026,11,20))
        self.assertEqual(rows[0][1],'CG-IC-001')
        self.assertEqual(len(rows),11)
if __name__=='__main__': unittest.main()
