# DEF-2026-002 — A logical scan record spans two non-atomic persistence writes

- **State:** Investigating
- **Severity:** S4 (source-level observation; partial-write impact not reproduced)
- **Date detected:** 2026-11-18
- **Last updated:** 2026-11-18
- **Owning project/repository:** SoulSyncMobile — `Moshoeshoe333/SOULSYNCMOBILE`
- **Affected branch/ref:** `main`
- **Affected full commit SHA:** `b85a83c9f672a11c71b94090826710475d8b6f86` (repository head observed during read-only inspection; source blobs below)
- **Owner:** SoulSyncMobile project maintainer (to be assigned)
- **Related issue/PR/CI run/log:** None inspected; no runtime reproduction or CI run claimed
- **Related lessons:** CG-002, CG-026
- **Reporter/source:** Codex-Guidas Tri-Tier 33 read-only pilot 01

## 1. Summary
Source inspection found that a scan updates the incident list and Harmony state through two sequential storage writes, without a transaction spanning both keys. A partial-write inconsistency is possible if the first write succeeds and the second fails; this outcome has not been dynamically reproduced.

## 2. Expected behaviour
The system must define one logical commit contract for a scan. After interruption or partial failure, durable state must be consistent or explicitly recoverable, and the UI must not imply that the scan was fully committed when it was not.

## 3. Observed behaviour
The hook writes the updated incident list first and the updated Harmony state second. It publishes the new in-memory snapshot only after both calls. There is no transaction/rollback spanning the two storage keys. The dashboard awaits the operation without a local catch or visible save-failure state.

The source sequence is confirmed by inspection; partial-write behaviour and restart recovery were not tested.

## 4. Impact and scope
- **Actual impact:** Not established; no injected write failure or observed data loss/corruption.
- **Potential impact:** Incident history and Harmony state may diverge after interruption or second-write failure; UI feedback may not clearly communicate persistence failure.
- **Affected users/data/components:** Potentially scan history and derived Harmony state in the affected storage flow; exact scope unknown.
- **Scope known or unknown:** Source path identified; runtime, platform and recovery scope unknown.
- **Workaround / containment:** No workaround validated. Do not describe the logical scan as atomically persisted until its consistency contract is tested.

## 5. Evidence ledger
| Evidence ID | Type | Exact ref (commit/run/log) | Observation | Limitation |
|---|---|---|---|---|
| E-001 | Source | `SOULSYNCMOBILE` `src/storage/storageManager.ts`, blob `17859deeb96a9fb87353151014ca3982e5668c62` | Separate storage operations for incident and Harmony state | Source inspection only |
| E-002 | Source | `SOULSYNCMOBILE` `src/hooks/useGuardianState.ts`, blob `db52b38fd4c9f8909f33df78c8e2752e18993fe2` | Sequential writes and snapshot publication after both | No injected failure |
| E-003 | Source | `SOULSYNCMOBILE` `App.tsx`, blob `17b1b37df4f93547c099129cff883571c5e9b1d5` | Dashboard awaits scan operation without local catch/visible save-failure state | No UI runtime witness |
| E-004 | Assessment | Codex-Guidas `doctrines/tri-tier-33/pilots/2026-11-18-soulsyncmobile-readonly-pilot-01.md`, blob `fd2b543792afd9dbcd05808f29eab170a96ad043`, finding F-08 | Consolidated finding and limitations | Assessment is not an independent runtime test |

## 6. Root-cause analysis
- **Status:** Suspected design/consistency-contract gap; not runtime-confirmed
- **Hypothesis:** The logical scan operation is implemented as two independent key writes without an atomic commit or explicit recoverable partial-commit protocol.
- **Evidence supporting:** E-001 and E-002.
- **Evidence contradicting:** No contrary evidence inspected; storage adapter guarantees and restart behaviour remain untested.
- **Discriminating test still needed:** P-04 — synthetic adapter allows incident write and rejects Harmony write; inspect both durable keys, UI outcome, retry behaviour and restart recovery.

## 7. Similarity search
- **Search terms:** partial write; multi-key persistence; atomic logical action; idempotency; recoverable commit
- **Lesson IDs searched:** CG-002, CG-026
- **Prior defect IDs:** No individual DEF record found at intake.
- **Similarity result:** Related to evidence-boundary and repository separation lessons; no identical prior root cause established.

## 8. Corrective action
None authorized or implemented. First ratify whether Harmony is derived/rebuildable from the incident ledger, whether one atomic record is required, or whether an outbox/commit protocol is justified. Do not select an architecture before the owning project approves the consistency contract.

## 9. Preventive and detective controls
- **Proposed:** Define the durable source of truth and logical commit/acknowledgement point.
- **Proposed:** Add partial-write, retry, idempotency and restart-recovery fault-injection tests using synthetic data.
- **Proposed:** Expose pending, committed and failed persistence states in the UI.
- **Verified:** None.

## 10. Regression and acceptance evidence
| Check | Command / procedure | Environment | Exact commit | Expected | Actual | Evidence link |
|---|---|---|---|---|---|---|
| P-04 | Synthetic adapter succeeds on incident write and rejects Harmony write | Not run | Target SHA above | Consistent state or explicit recoverable partial commit; no false success | Not run | Pilot report F-08 / P-04 |

## 11. Residual risk and follow-up
No dynamic proof of partial inconsistency, lost update, duplication or failed recovery exists. Next action: run P-04 in an isolated synthetic harness after the persistence contract and test scope are authorized. No application modification is included in this record.

## 12. Closure decision
- **Decision:** Keep open / Investigating
- **Approver/authority:** SoulSyncMobile project owner
- **Acceptance criteria met:** No
- **Reason:** No fault injection, approved remediation or regression evidence.
- **Closure evidence:** None

## 13. Reusable lesson
Existing CG-026 is relevant to evidence and repository boundaries. A new cross-project atomicity lesson may be proposed after the failure mode and preventive control are demonstrated; do not promote this source-level observation to Verified.
