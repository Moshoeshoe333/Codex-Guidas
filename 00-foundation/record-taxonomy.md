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

## Evidence promotion and assurance

A status transition is a claim about the maturity of knowledge, not a reward for completing paperwork.

| Transition | Minimum basis | Ratification |
|---|---|---|
| Observed | A dated, attributable source observation or report. Label source-only observations honestly; do not imply runtime reproduction. | The record author may capture the observation. |
| Observed to Derived | Identify the observation(s), explain the inference, record plausible alternatives and applicability limits. | A maintainer may classify a bounded inference as Derived; this is not independent verification of a control. |
| Proposed or Derived to Verified | Define acceptance criteria before testing; attach immutable evidence references; record exact revision, procedure/command, environment, actual result and limitations in the Evidence ledger. The evidence must exercise the stated control, not merely show that documentation or code exists. | Name the author, auditor and ratifier. Normally the auditor is distinct from the author. A transparent self-review may be recorded as limited-self-review, but it is lower assurance and must not be represented as independent. |

There is no universal fixed count of independent sources that fits every claim. A narrow deterministic software claim may be supported by a reproducible test on an exact commit; high-consequence claims need stronger, independent and domain-appropriate evidence. Critical security, privacy, safeguarding and data-integrity controls cannot be promoted on self-review alone. Project-specific controls also require the owning project’s authorized decision-maker; Codex-Guidas cannot ratify another project’s production or release authority.

The CI validator enforces the presence and internal consistency of evidence IDs and review declarations for Verified claims. It does not adjudicate evidence quality, reviewer identity, domain competence or delegated authority. A green CI run therefore proves metadata integrity—not that the claim is substantively true.
