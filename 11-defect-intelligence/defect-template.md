---
id: "DEF-YYYY-NNN"
record_type: "defect"
status: "New"
projects: []
layer: "unknown"
component: null
failure_mode: null
severity: null
origin_date: null
last_reviewed: null
verification_due: null
evidence_class: "Reported"
verification_status: "not-claimed"
source_path: "path/to/source"
review_scope: "state what was actually reviewed"
---

# DEF-2026-NNN — [Short factual title]

- **State:** See frontmatter and the canonical record taxonomy.
- **Severity:** S0 / S1 / S2 / S3 / S4 (impact-based; see canonical taxonomy).
- **Date detected:**
- **Last updated:**
- **Owning project/repository:**
- **Affected branch/ref:**
- **Affected full commit SHA:** Unknown / [SHA]
- **Owner:**
- **Related issue/PR/CI run/log:**
- **Related lessons:** CG-XXX / none found
- **Reporter/source:** [Avoid personal or sensitive data]

## 1. Summary
One or two factual sentences describing the failure or near miss.

## 2. Expected behaviour
What should have happened? Link the requirement, invariant or decision.

## 3. Observed behaviour
What actually happened? Include reproducible steps and exact error/signature where safe.

## 4. Impact and scope
- Actual impact:
- Potential impact (clearly labelled):
- Affected users/data/components:
- Scope known or unknown:
- Workaround / containment:

## 5. Evidence ledger
| Evidence ID | Type | Exact ref (commit/run/log) | Observation | Limitation |
|---|---|---|---|---|
| E-001 | Source / test / CI / runtime / report | | | |

## 6. Root-cause analysis
- **Status:** Unknown / suspected / confirmed
- **Hypothesis:**
- **Evidence supporting:**
- **Evidence contradicting:**
- **Discriminating test still needed:**

Do not label a hypothesis confirmed without evidence that distinguishes it from plausible alternatives.

## 7. Similarity search
- Search terms:
- Lesson IDs searched:
- Prior defect IDs:
- Similarity result and why it is/isn't the same cause:

## 8. Corrective action
Smallest authorized change, owner and exact change/PR/commit link.

## 9. Preventive and detective controls
What will prevent recurrence or detect it earlier? State whether proposed, implemented or verified.

## 10. Regression and acceptance evidence
| Check | Command / procedure | Environment | Exact commit | Expected | Actual | Evidence link |
|---|---|---|---|---|---|---|
| | | | | | | |

## 11. Residual risk and follow-up
Unknowns, accepted risk, deferred work, owner and due/review date.

## 12. Closure decision
- **Decision:** Keep open / contained / close / won't fix / reopen
- **Approver/authority:**
- **Acceptance criteria met:**
- **Reason:**
- **Closure evidence:**

## 13. Reusable lesson
Existing CG-XXX updated / new CG-XXX proposed / no cross-project lesson (explain).

Use null for unknown metadata. A pending verification must have a review date. Run the knowledge integrity validator before submitting.
