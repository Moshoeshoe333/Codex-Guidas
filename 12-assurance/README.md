# Assurance Registers

**Status:** Proposed, unratified operating register.  
**Initialised:** 2026-11-20.  
**Scope:** Codex-Guidas repository assurance only; this is not a portfolio command layer.

## Purpose

Maintain an explicit list of repository surfaces that deserve review, why they matter, when they should be revisited and what changes should trigger a focused review. Track whether important engineering invariants are merely documented, designed, implemented or actually operating.

Machine-readable source: [`registers.json`](registers.json). Validate and list review triggers with:

```bash
python scripts/assurance_register.py validate
python scripts/assurance_register.py queue --as-of 2026-11-20
```

CI validates structure, cross-references, dates and the review queue. It does **not** perform the audit, inspect GitHub settings, prove evidence truth or automatically launch a review.

## Audit universe

The four assets cover automation/CI, evidence and defect lifecycle, methodologies/invariants/framework lineage, and reusable packs. Each has a provisional risk tier, rationale, review interval and path-based change triggers.

Initial tiers are provisional judgements, not approved risk acceptance or certification. The inventory review records only which surfaces exist and selected documentation inspected. `last_audit_on` and `audit_opinion` remain null because no formal asset audit has been completed.

| Tier | Working interpretation |
|---|---|
| Critical | Credible severe safety, security, privacy or data-integrity exposure, active exploitation, or highly irreversible consequence. |
| High | Material user, service, security or integrity consequence with significant exposure or limited mitigation. |
| Moderate | Meaningful governance, integrity or operational consequence, but bounded scope and plausible recovery/containment. |
| Low | Limited consequence and exposure with straightforward recovery. |
| Unassessed | Insufficient evidence to assign a defensible tier. |

Review intervals are planning defaults. A material change trigger should prompt the affected scope to be reconsidered; the trigger matrix is currently a manual routing aid, not an automated scheduler.

## Operational invariant register

The initial register tracks the invariants most directly relevant to this repository's evidence, record, CI and retrieval processes: INV-001, INV-002, INV-009, INV-010, INV-011, INV-014 and INV-018.

All seven begin as `not_assessed`. Their design state records only that a rule and intended verification method are documented. No operating effectiveness is claimed. Operational owners are unassigned; 4 December 2026 is a proposed trigger to assign accountable owners and plan the first bounded verification, not proof that it has happened.

An invariant used by another project requires a separate local owner, scope, evidence and decision authority. A Codex-Guidas entry does not transfer authority.

| State | Meaning |
|---|---|
| not_assessed | No operation test has been completed in the stated scope. |
| planned | An owner and concrete verification plan exist; operation is not yet verified. |
| implemented | A control exists, but operation has not been demonstrated against acceptance criteria. |
| verified | Direct evidence demonstrates operation for the stated scope, owner, version and date. |
| blocked | Verification cannot proceed; blocker and owner must be recorded. |
| accepted_risk | A named authorized person accepts a described residual risk with a review/expiry date. |
| not_applicable | Reason and authorized decision owner are recorded. |

`verified` requires an assigned owner, dated verification, a method and evidence references that resolve to the evidence register. `accepted_risk` requires an acceptor, residual-risk statement and review date. A metadata validator cannot authenticate identities, competence or authority.

## Audit opinions

Use `pass`, `conditional`, `fail` or `abstain-insufficient-evidence` only after a defined audit scope has been performed. `pass` applies only to the stated criteria and scope, not a claim of zero risk. `conditional` names required actions and deadlines. `fail` records a material unmet criterion. `abstain-insufficient-evidence` means the reviewer cannot support an opinion. Critical safeguards cannot be averaged away by unrelated passing controls.

## Review process

1. Identify the asset and exact change/trigger.
2. Select only the relevant review scope; do not re-audit unrelated surfaces.
3. Record branch, full commit SHA, dates, environment, reviewer, evidence references, contradictions and exclusions.
4. Separate design adequacy from operating effectiveness.
5. Record an opinion only after checks are completed; otherwise leave the audit unperformed or abstain.
6. Assign corrective/preventive actions to the authority that owns the affected repository or project.
7. Revisit after material change and at the next review trigger.

## Current limitations

- Risk tiers and intervals are provisional and await repository-owner ratification.
- GitHub branch protection, secret scanning, dependency alerts, private vulnerability reporting and other settings have not been verified.
- Change triggers do not launch automated tier-specific checks.
- No operational invariant is marked verified and no audit opinion has been issued.
- The evidence register contains an immutable repository snapshot for inventory provenance only; it is not a control-effectiveness witness.

## Authority and licensing

Codex-Guidas curates its own knowledge and assurance records. Each project retains authority over implementation, release, risk acceptance and closure. The external reuse licence remains undeclared; this register grants no permission to redistribute or apply controls elsewhere.
