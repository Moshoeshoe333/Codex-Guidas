#!/usr/bin/env python3
"""Validate and queue Codex-Guidas assurance-universe and invariant registers."""
from __future__ import annotations
import argparse, json, re, sys
from datetime import date, timedelta
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
RISK_TIERS = {'critical','high','moderate','low','unassessed'}
RISK_STATES = {'provisional','approved','not_assessed'}
AUDIT_STATES = {'identified','scheduled','in_progress','audited','blocked','retired'}
AUDIT_OPINIONS = {'pass','conditional','fail','abstain-insufficient-evidence'}
OPERATING_STATES = {'not_assessed','planned','implemented','verified','blocked','accepted_risk','not_applicable'}
OWNERSHIP_STATES = {'unassigned','proposed','assigned'}
DESIGN_STATES = {'documented','partially_documented','absent','not_applicable'}

def nonempty(value): return isinstance(value, str) and bool(value.strip())
def parse_date(value, label, errors):
    if value is None: return None
    if not isinstance(value,str): errors.append(f'{label} must be an ISO date or null'); return None
    try: parsed=date.fromisoformat(value)
    except ValueError: errors.append(f'{label} has invalid ISO date {value!r}'); return None
    if parsed.isoformat()!=value: errors.append(f'{label} must use YYYY-MM-DD'); return None
    return parsed

def known_invariant_ids(root=ROOT):
    text=(root/'03-architecture'/'invariants-catalogue.md').read_text(encoding='utf-8')
    return set(re.findall(r'^\|\s*(INV-\d{3})\s*\|',text,flags=re.MULTILINE))

def validate_data(data, invariant_ids):
    errors=[]
    if not isinstance(data,dict): return ['register root must be a JSON object']
    if data.get('schema_version')!='1.0': errors.append('schema_version must be 1.0')
    if data.get('register_status') not in {'proposed-unratified','ratified','superseded'}: errors.append('invalid register_status')
    if not nonempty(data.get('authority_boundary')): errors.append('authority_boundary must be non-empty')
    evidence,assets,controls=(data.get(k) for k in ('evidence','audit_assets','invariant_controls'))
    for name,value in (('evidence',evidence),('audit_assets',assets),('invariant_controls',controls)):
        if not isinstance(value,list): errors.append(f'{name} must be an array')
    if errors: return errors
    evmap={}
    for item in evidence:
        if not isinstance(item,dict): errors.append('evidence item must be an object'); continue
        eid=item.get('id')
        if not nonempty(eid): errors.append('evidence item requires id'); continue
        if eid in evmap: errors.append(f'duplicate evidence id: {eid}')
        evmap[eid]=item
        for f in ('type','uri','scope','limitation'):
            if not nonempty(item.get(f)): errors.append(f'evidence {eid}: {f} must be non-empty')
        parse_date(item.get('observed_on'),f'evidence {eid} observed_on',errors)
    asset_ids=set()
    for item in assets:
        if not isinstance(item,dict): errors.append('audit asset must be an object'); continue
        aid=item.get('id')
        if not nonempty(aid): errors.append('audit asset requires id'); continue
        if aid in asset_ids: errors.append(f'duplicate audit asset id: {aid}')
        asset_ids.add(aid)
        for f in ('name','asset_type','owner_role','decision_authority_role','risk_rationale'):
            if not nonempty(item.get(f)): errors.append(f'audit asset {aid}: {f} must be non-empty')
        paths=item.get('path_scope')
        if not isinstance(paths,list) or not paths or not all(nonempty(p) for p in paths): errors.append(f'audit asset {aid}: path_scope must be a non-empty path array')
        if item.get('risk_tier') not in RISK_TIERS: errors.append(f'audit asset {aid}: invalid risk_tier')
        if item.get('risk_rating_status') not in RISK_STATES: errors.append(f'audit asset {aid}: invalid risk_rating_status')
        if item.get('risk_rating_status')=='approved' and not isinstance(item.get('risk_approval'),dict): errors.append(f'audit asset {aid}: approved risk tier requires risk_approval')
        interval=item.get('review_interval_days')
        if not isinstance(interval,int) or isinstance(interval,bool) or not 1<=interval<=365: errors.append(f'audit asset {aid}: review_interval_days must be 1..365')
        last=parse_date(item.get('last_inventory_review_on'),f'audit asset {aid} last_inventory_review_on',errors)
        due=parse_date(item.get('next_review_due'),f'audit asset {aid} next_review_due',errors)
        if last and isinstance(interval,int) and not isinstance(interval,bool) and interval>0 and due and due!=last+timedelta(days=interval): errors.append(f'audit asset {aid}: next_review_due must equal last inventory review plus cadence')
        last_audit=parse_date(item.get('last_audit_on'),f'audit asset {aid} last_audit_on',errors)
        state,opinion=item.get('review_status'),item.get('audit_opinion')
        if state not in AUDIT_STATES: errors.append(f'audit asset {aid}: invalid review_status')
        if opinion is not None and opinion not in AUDIT_OPINIONS: errors.append(f'audit asset {aid}: invalid audit_opinion')
        if state=='audited':
            if last_audit is None or opinion is None: errors.append(f'audit asset {aid}: audited state requires date and opinion')
            if not item.get('audit_evidence_refs'): errors.append(f'audit asset {aid}: audited state requires audit_evidence_refs')
        elif last_audit is not None or opinion is not None or item.get('audit_evidence_refs'): errors.append(f'audit asset {aid}: audit date/opinion/evidence require audited state')
        for f in ('inventory_evidence_refs','audit_evidence_refs'):
            refs=item.get(f,[])
            if not isinstance(refs,list) or not all(isinstance(r,str) and r in evmap for r in refs): errors.append(f'audit asset {aid}: {f} must resolve to evidence ids')
        triggers=item.get('change_triggers')
        if not isinstance(triggers,list) or not triggers: errors.append(f'audit asset {aid}: change_triggers must be non-empty')
        else:
            for n,t in enumerate(triggers,1):
                if not isinstance(t,dict) or not isinstance(t.get('paths'),list) or not t.get('paths') or not nonempty(t.get('action')): errors.append(f'audit asset {aid}: invalid change trigger {n}')
        if not isinstance(item.get('limitations'),list) or not all(nonempty(x) for x in item['limitations']): errors.append(f'audit asset {aid}: limitations must be non-empty statements')
    control_ids=set()
    for item in controls:
        if not isinstance(item,dict): errors.append('invariant control must be an object'); continue
        cid=item.get('id')
        if not nonempty(cid): errors.append('invariant control requires id'); continue
        if cid in control_ids: errors.append(f'duplicate invariant control id: {cid}')
        control_ids.add(cid)
        iid=item.get('invariant_id')
        if iid not in invariant_ids: errors.append(f'invariant control {cid}: unknown invariant_id {iid!r}')
        for f in ('invariant_name','scope','owner_role','verification_method','notes'):
            if not nonempty(item.get(f)): errors.append(f'invariant control {cid}: {f} must be non-empty')
        if item.get('design_state') not in DESIGN_STATES: errors.append(f'invariant control {cid}: invalid design_state')
        state,ownership,owner=item.get('operating_status'),item.get('ownership_status'),item.get('control_owner')
        if state not in OPERATING_STATES: errors.append(f'invariant control {cid}: invalid operating_status')
        if ownership not in OWNERSHIP_STATES: errors.append(f'invariant control {cid}: invalid ownership_status')
        if ownership=='assigned' and not nonempty(owner): errors.append(f'invariant control {cid}: assigned ownership requires control_owner')
        if ownership=='unassigned' and owner is not None: errors.append(f'invariant control {cid}: unassigned ownership must have null control_owner')
        last=parse_date(item.get('last_verified_on'),f'invariant control {cid} last_verified_on',errors)
        due=parse_date(item.get('next_review_due'),f'invariant control {cid} next_review_due',errors)
        refs=item.get('evidence_refs',[])
        if not isinstance(refs,list) or not all(isinstance(r,str) and r in evmap for r in refs): errors.append(f'invariant control {cid}: evidence_refs must resolve to evidence ids')
        if state=='verified':
            if ownership!='assigned' or not nonempty(owner): errors.append(f'invariant control {cid}: verified operation requires an assigned control owner')
            if last is None or due is None: errors.append(f'invariant control {cid}: verified operation requires last_verified_on and next_review_due')
            if not refs: errors.append(f'invariant control {cid}: verified operation requires evidence_refs')
        elif state=='not_assessed' and (last is not None or refs): errors.append(f'invariant control {cid}: not_assessed cannot carry verification date or evidence refs')
        if state=='accepted_risk' and (not nonempty(item.get('accepted_by')) or not nonempty(item.get('residual_risk')) or due is None): errors.append(f'invariant control {cid}: accepted_risk requires acceptor, residual risk and review date')
    return errors

def load_repository(root=ROOT):
    try: data=json.loads((root/'12-assurance'/'registers.json').read_text(encoding='utf-8'))
    except (OSError,json.JSONDecodeError) as exc: return None,[f'cannot load assurance register: {exc}']
    try: ids=set(re.findall(r'^\|\s*(INV-\d{3})\s*\|',(root/'03-architecture'/'invariants-catalogue.md').read_text(encoding='utf-8'),flags=re.MULTILINE))
    except OSError as exc: return None,[f'cannot load invariant catalogue: {exc}']
    errors=validate_data(data,ids)
    for asset in data.get('audit_assets',[]) if isinstance(data,dict) else []:
        if isinstance(asset,dict):
            for p in asset.get('path_scope',[]) if isinstance(asset.get('path_scope'),list) else []:
                if isinstance(p,str) and not (root/p).exists(): errors.append(f'audit asset {asset.get("id","?")}: missing path_scope target {p}')
    return data,errors

def review_queue(data,as_of):
    rows=[]
    for asset in data.get('audit_assets',[]):
        if asset.get('review_status')=='retired': continue
        due=date.fromisoformat(asset['next_review_due'])
        label='OVERDUE' if due<as_of else ('DUE today' if due==as_of else 'DUE')
        rows.append((due,asset['id'],'AUDIT',asset['review_status'],label))
    for control in data.get('invariant_controls',[]):
        if control.get('operating_status')=='not_applicable': continue
        due=date.fromisoformat(control['next_review_due'])
        label='OVERDUE' if due<as_of else ('DUE today' if due==as_of else 'DUE')
        rows.append((due,control['id'],'CONTROL',control['operating_status'],label))
    return sorted(rows)

def main():
    parser=argparse.ArgumentParser(description='Validate assurance registers and list review triggers.')
    sub=parser.add_subparsers(dest='command',required=True)
    sub.add_parser('validate',help='Validate asset/control structure and references.')
    q=sub.add_parser('queue',help='List upcoming and overdue reviews.')
    q.add_argument('--as-of',help='ISO date for deterministic output; defaults to today.')
    args=parser.parse_args()
    data,errors=load_repository()
    if errors:
        print('Assurance register validation FAILED:')
        for error in errors: print(' - '+error)
        return 1
    if args.command=='validate':
        print(f"Assurance register validation PASS: {len(data['audit_assets'])} assets, {len(data['invariant_controls'])} controls, {len(data['evidence'])} inventory evidence items.")
        print('Register integrity only; no audit or operating-effectiveness conclusion is implied.')
        return 0
    try: as_of=date.fromisoformat(args.as_of) if args.as_of else date.today()
    except ValueError: print('--as-of must be YYYY-MM-DD',file=sys.stderr); return 2
    rows=review_queue(data,as_of)
    for due,rid,kind,state,label in rows: print(f'{rid} | {kind} | {state} | {label} {due.isoformat()}')
    print(f'\\n{len(rows)} review trigger(s) as of {as_of.isoformat()}. A due date is a reminder, not audit evidence.')
    return 0

if __name__=='__main__': raise SystemExit(main())
