# Canonical record taxonomy

This file owns the vocabulary used by structured records. Lesson and defect states intentionally differ because they describe different lifecycle concepts.

## Cross-project lesson status

| Status | Meaning |
|---|---|
| Observed | A specific source-backed event or condition was recorded. This does not by itself imply runtime reproduction. |
| Derived | A transferable lesson was inferred from one or more observations. |
| Proposed | A recommended control or hypothesis has not yet been demonstrated. |
| Verified | The stated control was reproduced against explicit criteria on an exact source revision and environment, with evidence recorded. |
| Superseded | A later evidenced practice replaces this record; preserve the historical link and reason. |

## Defect workflow state

| State | Meaning |
|---|---|
| New | Recorded, not yet triaged. |
| Triaged | Impact, scope and owner assessed. |
| Investigating | Evidence collection and hypotheses are in progress. |
| Contained | Immediate risk reduced; root cause may remain open. |
| Fix proposed | A corrective change is identified but not yet verified. |
| In verification | A change exists and its evidence is being evaluated. |
| Closed | Acceptance criteria passed and residual risk accepted by the proper owner. |
| Blocked | Progress depends on an external decision, access or prerequisite. |
| Won't fix | The proper authority explicitly accepts residual risk with rationale. |
| Reopened | Recurrence or failed acceptance criteria invalidate prior closure. |

## Defect severity

| Severity | Meaning |
|---|---|
| S0 | Critical: active exploitation, material data loss/corruption, severe safety risk or broad compromise. |
| S1 | High: major workflow loss, significant security/privacy exposure, unsafe access path or integrity failure. |
| S2 | Moderate: important function impaired with a workaround, limited scope or recoverable issue. |
| S3 | Low: minor issue with low impact and safe workaround. |
| S4 | Observation: near miss, quality concern or improvement opportunity without demonstrated user impact. |

Severity is an impact classification, not urgency by itself. Security and safeguarding concerns may require escalation before impact is fully known.

## Evidence class and verification status are not lifecycle status

- **evidence_class** preserves original evidence wording, such as source-observed, derived from static review or pending runtime reproduction. It is not a second status register.
- **verification_status** is a retrieval field: pending, source-only, not-claimed, verified or blocked.
- A record may be **Derived** while verification is **pending**. Do not promote it merely because a fix was written or a test was added.
- Lesson status and defect state are separate enums. Do not force a defect state into the lesson vocabulary or vice versa.

## Change rule

Update vocabulary here first, then update the schema validator and templates in the same change. Do not silently rename historical values. An allowed status is not evidence that a record's claims are correct.
