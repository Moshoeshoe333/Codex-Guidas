# Cross-Project Engineering Lessons Ledger

**Status:** Initial curated register. Entries are distilled from prior project work and discussions; not all have been independently re-audited against current repositories.

## Status vocabulary
- **Observed:** A specific event or condition was recorded.
- **Derived:** A transferable lesson inferred from observations.
- **Proposed:** A recommended control not yet demonstrated.
- **Verified:** Reproduced and checked against defined criteria.
- **Superseded:** Replaced by a later evidenced practice.

| ID | Lesson | Origin | Evidence class | Reusable control |
|---|---|---|---|---|
| CG-001 | Documentation is not implementation. | ScoutSA / portfolio | Derived | Label requirements, design, code, runtime and user evidence separately. |
| CG-002 | Passing tests prove only the cases and environment exercised. | SoulSync | Derived | Record command, environment, test count, commit and uncovered paths. |
| CG-003 | Do not weaken meaningful tests merely to make CI green. | Cross-project | Proposed rule | Review test changes as carefully as production changes; explain removed coverage. |
| CG-004 | Preserve failed execution evidence; a build stage passing is not runtime verification. | SoulSyncMobile | Observed / derived | Record failure stage, logs, environment and unresolved gate. |
| CG-005 | Immutability and explicit contracts need direct mutation and boundary tests. | SoulSync | Derived | Test attempted mutation and contract boundaries; do not infer total coverage. |
| CG-006 | Synthetic data validates technical behaviour, not market demand. | ScoutSA | Derived | Separate technical validation from user and commercial validation. |
| CG-007 | Verification is not a guarantee of opportunity, quality or outcome. | ScoutSA | Derived | State exactly what was checked and what remains unknown. |
| CG-008 | Visibility, discoverability, access, contact and placement are distinct states. | ScoutSA | Derived | Model and measure transitions separately. |
| CG-009 | Under-18 interactions require guardian, safeguarding and access-control boundaries. | ScoutSA | Risk requirement | Block unsafe contact paths by default and test abuse cases. |
| CG-010 | Architecture must earn complexity through demonstrated need. | ScoutSA / portfolio | Adopted principle | Build the smallest complete vertical slice; defer speculative abstractions. |
| CG-011 | Fail-closed decisions need explicit semantics and recovery paths. | SoulSync / Mobile | Derived | Test allowed, warning, denied, unknown and malformed-input paths. |
| CG-012 | GPS and other uncertain signals must be represented as estimates with freshness/confidence. | NAVIGRE | Derived | Store observation time, accuracy, confidence, decay and expiry. |
| CG-013 | A score without inputs, weights, thresholds and limitations is not auditable. | NAVIGRE | Derived | Version scoring rules and expose factor-level rationale. |
| CG-014 | Threat observations are leads, not confirmed incidents until corroborated. | UCI concept | Proposed | Record source, time, confidence, corroboration and analyst assessment separately. |
| CG-015 | Stakeholder silence is not user-validation evidence. | ScoutSA | Derived | Recruit independent adult testers; separate partnership, usability and commercial validation. |
| CG-016 | Every session should end with verified status, open risks and next smallest action. | Portfolio | Adopted rule | Write a concise evidence-linked closeout. |

## Required fields for future entries
Unique ID; discovery/review dates; source project and exact artifact; commit/run identifier; expected and actual behaviour; impact/severity; root-cause status; corrective and preventive controls; regression test; evidence class; reproducibility; residual risk; applicability boundaries.

## Promotion rule
Do not mark a lesson Verified because the recommendation sounds sensible or code was written. State what was tested, where, when, against which commit and with what result. Without source evidence, retain Derived or Proposed status.