# Pack: Defect Intelligence

**Pack ID:** CG-PACK-004  
**Version:** 1.0.0  
**Maturity:** Operating structure; historical defect migration and recurrence outcomes remain incomplete.  
**Canonical central register:** [11-defect-intelligence/ledger.md](../../11-defect-intelligence/ledger.md)  
**Supporting source:** 01-lessons-learned/ledger.md (where present)

## Purpose
Turn defects into traceable learning and recurrence prevention, not merely closed tickets.

## Defect lifecycle
1. **Detect:** preserve the failing command, environment, commit, logs and observed behaviour.
2. **Contain:** assess user impact, data integrity, security/safety exposure and blast radius.
3. **Reproduce:** isolate a minimal case; distinguish deterministic failure from intermittent symptoms.
4. **Diagnose:** separate confirmed facts from root-cause hypotheses.
5. **Correct:** make the smallest authorized fix.
6. **Prevent:** add a control at the right layer (contract, code, test, CI, monitoring, procedure or training).
7. **Verify:** rerun the reproduction and relevant regressions; test the prevention mechanism itself.
8. **Close:** record exact commit/run, evidence, residual risk and owner.
9. **Transfer:** search for analogous project exposure and add a reusable lesson with applicability boundaries.

## Required defect record
- Defect ID / project / date:
- Severity and affected users:
- Exact branch, commit, environment:
- Expected vs actual:
- Reproduction steps and logs:
- Confirmed facts:
- Root-cause hypothesis / confidence:
- Containment:
- Corrective change:
- Preventive control:
- Regression test:
- Verification run and result:
- Residual risk:
- Cross-project analogues:
- Closure owner/date:

## Rules
- Do not weaken a meaningful test simply to obtain a green result.
- Preserve failed evidence.
- A green test suite does not prove all failure modes are covered.
- Test the guardrail itself.
- Search the existing defect and lesson registers before creating duplicates.
- Never put secrets or personal data in defect records.

## Adaptation
Start with a Markdown template and a small register. Add automation only when volume and repeated retrieval justify it. A defect ledger is not a substitute for issue tracking or incident response.
