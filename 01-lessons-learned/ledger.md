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

## Additional lessons from source archaeology (2026-11-18)

| ID | Lesson | Source evidence | Evidence class | Reusable control |
|---|---|---|---|---|
| CG-017 | A repository write is not complete until the intended branch is read back and the diff inspected. | ScoutSA `docs/engineering-integrity.md`, DOC-002 | Observed / verified in source record | Always specify branch; fetch the written path from that branch; inspect commit and diff. |
| CG-018 | Documentation integrity can be tested as code, but the guard itself needs testing. | ScoutSA DOC-001–DOC-004 | Observed | Test the consistency check locally and in hosted CI; preserve failed runs and exact successful runs. |
| CG-019 | Zero-byte or invalid workflow files can create misleading CI noise. | ScoutSA CI-001 | Observed | Validate workflow files are non-empty and contain valid triggers/jobs; identify run and job before attributing failure. |
| CG-020 | Mainline and prototype branches are separate evidence/authority boundaries. | ScoutSA engineering-integrity policy | Observed / derived | Maintain separate branch-specific controls; never infer one branch's status from another. |
| CG-021 | Deep immutability requires nested mutation rejection and detachment from mutable source inputs. | SoulSync 3 `tests/test_coordinate99.py`, commit `ddcd79046248c8ee4b04238b0489b92199de21fd` | Observed in source; execution not re-run here | Add nested mapping/list mutation tests and source-mutation detachment tests. |
| CG-022 | Typed absence must not be collapsed into zero, false or a guessed default. | SoulSync 3 33-Tier / coordinate tests | Observed in source | Represent absence explicitly and test non-coercion. |
| CG-023 | Provenance is lineage, not authorization. | SoulSync 3 coordinate tests | Observed in source | Keep evidence lineage and execution/permission authority separate. |
| CG-024 | Discovery can be automated; authority cannot be delegated to an agent by implication. | SoulSyncMobile ledger `methodology-delta.md`, MD-SWARM-001 | Adopted methodology in source | Agents may discover/normalize candidate evidence; deterministic/human policy review controls fixture admission and production changes. |
| CG-025 | A CI harness is not a substitute for physical mobile runtime evidence. | SoulSyncMobile ledger README and MD-GBOOT-001 | Observed / adopted rule | Keep CI, APK build, install, device execution and G-BOOT witness as separate gates. |
| CG-026 | Keep app source, forensic ledger and runtime evidence in separate repositories with exact cross-references. | SoulSyncMobile ledger README | Observed architecture | Link exact app SHA, workflow/run, branch/ref and artifact identity; ledger changes are not app changes. |
| CG-027 | Stored observation confidence and freshness may represent different domain facts. | NAVIGRE Pass 5 policy simulation | Derived / proposed policy | Preserve stored confidence; evaluate freshness separately; only accepted contract defines stale authorization. |
| CG-028 | Authorization does not imply route existence or route verification. | NAVIGRE Spatial Seam 4 artifacts | Observed design invariant | Use narrow authorization result types and test downstream claims independently. |
| CG-029 | PR-head evidence does not automatically certify the squash-merge commit. | NAVIGRE Master Evidence Ledger and Seam 4 evidence gate | Adopted rule | Recheck exact merge SHA; do not inherit green across code boundaries. |
| CG-030 | A methodology must disclose what remains unspecified and unvalidated. | SoulSync 3 `docs/33-tier-framework.md` | Observed | State maturity, open definitions, validation gaps and non-claims explicitly. |

These entries are source-backed observations or derived controls. They are not all independently re-executed in this Codex-Guidas import. See [the 2026-11-18 repository archaeology report](../10-source-audits/2026-11-18-repository-archaeology.md) for source paths, blob SHAs and limitations.
