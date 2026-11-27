# DEF-2026-002 — A logical scan record spans two non-atomic persistence writes

- **State:** Investigating
- **Severity:** S4 (partial-write outcome reproduced in a mock-backed hook harness; native-device/user impact not established)
- **Date detected:** 2026-11-18
- **Last updated:** 2026-11-27
- **Owning project/repository:** SoulSyncMobile — `Moshoeshoe333/SOULSYNCMOBILE`
- **Affected branch/ref:** `main`
- **Original detection baseline:** `b85a83c9f672a11c71b94090826710475d8b6f86` (repository head observed during initial read-only inspection; source blobs below)
- **Latest revalidated application baseline (2026-11-27):** `1f50bd3387c61d51868140ec3776b94150a2d4c6` (`main`; the two affected source blobs remain unchanged)
- **Owner:** SoulSyncMobile project maintainer (to be assigned)
- **Related CI run:** [44297424933](https://github.com/Moshoeshoe333/SOULSYNCMOBILE/actions/runs/44297424933) — successful on exact test commit `1b989d1145587cf223fc9bbeecf8d1856536152c`
- **Related lessons:** CG-002, CG-026
- **Reporter/source:** Codex-Guidas Tri-Tier 33 read-only pilot 01

## 1. Summary
Source inspection found that a scan updates the incident list and Harmony state through two sequential storage writes, without a transaction spanning both keys. A partial-write inconsistency is possible if the first write succeeds and the second fails. This outcome was subsequently reproduced in a controlled mock-backed hook test in CI run `44297424933`; no native-device failure or actual user data loss is established.

## 2. Expected behaviour
The system must define one logical commit contract for a scan. After interruption or partial failure, durable state must be consistent or explicitly recoverable, and the UI must not imply that the scan was fully committed when it was not.

## 3. Observed behaviour
The hook writes the updated incident list first and the updated Harmony state second. It publishes the new in-memory snapshot only after both calls. There is no transaction/rollback spanning the two storage keys. The dashboard awaits the operation without a local catch or visible save-failure state.

The source sequence is confirmed by inspection. The synthetic test source at E-005 was subsequently executed in GitHub Actions run `44297424933`, on exact test commit `1b989d1145587cf223fc9bbeecf8d1856536152c`; the Guardian hook fault suite passed 2/2. The second-write case reproduced the asserted split in the mock harness: the incident entry was persisted, the Harmony key remained absent, the in-memory hook snapshot remained unchanged and the operation rejected. This is a controlled test reproduction, not evidence of native AsyncStorage/device failure, user data loss or restart behaviour.

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
| E-005 | Test source | `SOULSYNCMOBILE` `src/hooks/__tests__/useGuardianState.fault-injection.test.ts`, blob `b8894b23422f2dd7c949f716812a2ff078da1dde` at application baseline `1f50bd3387c61d51868140ec3776b94150a2d4c6` | Defines the synthetic second-write failure case and asserts one incident in mock storage, absent Harmony key, unchanged hook snapshot and rejected operation | Does not prove execution by itself; does not cover native storage, retry/restart or UI presentation |
| E-006 | CI execution | [GitHub Actions run 44297424933](https://github.com/Moshoeshoe333/SOULSYNCMOBILE/actions/runs/44297424933), exact head `1b989d1145587cf223fc9bbeecf8d1856536152c` | Run completed SUCCESS; `npm run test:guardian-faults` passed 2/2, including the partial-write case; typecheck, threat fixtures 13/13 and storage fault tests 10/10 also passed | Mock-backed hook harness on the recorded CI commit; not device/runtime, native persistence, restart recovery or a fix |

## 6. Root-cause analysis
- **Status:** Partial-write outcome reproduced in the synthetic hook harness; native persistence semantics and user impact remain unconfirmed
- **Hypothesis:** The logical scan operation is implemented as two independent key writes without an atomic commit or explicit recoverable partial-commit protocol.
- **Evidence supporting:** E-001 and E-002.
- **Evidence contradicting:** No contrary evidence inspected; storage adapter guarantees and restart behaviour remain untested.
- **Existing test source:** `src/hooks/__tests__/useGuardianState.fault-injection.test.ts` encodes the P-04 second-write failure scenario with a synthetic AsyncStorage mock. It asserts the incident key contains the new record, the Harmony key remains absent, the hook's in-memory state remains unchanged, and `analyzeAndLogInput` rejects.
- **Execution evidence:** GitHub Actions run `44297424933` completed SUCCESS on exact commit `1b989d1145587cf223fc9bbeecf8d1856536152c`; the Guardian hook fault suite passed 2/2. The current `main` branch was rechecked at `1f50bd3387c61d51868140ec3776b94150a2d4c6`, whose hook-test blob remains `b8894b23422f2dd7c949f716812a2ff078da1dde`. The successful run is on an ancestor commit, not the current HEAD.
- **Remaining evidence gap:** No native AsyncStorage/device run, process restart, retry, recovery, idempotency, actual-user impact or user-visible failure-path witness is attached. The test does not establish a production data-loss event.
- **Next discriminating proof:** after the owner approves the persistence consistency contract, specify and execute retry, restart restoration and UI failure-path checks on the supported runtime. Re-run relevant tests against the resulting exact commit.

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
| P-04 | `npm run test:guardian-faults`; synthetic incident write succeeds and Harmony write rejects | GitHub Actions run `44297424933` — SUCCESS | `1b989d1145587cf223fc9bbeecf8d1856536152c` (test commit; current `main` `1f50bd3387c61d51868140ec3776b94150a2d4c6`) | Mock storage contains one incident, Harmony key absent, hook snapshot unchanged, operation rejects | PASS; hook fault suite 2/2. Native storage/device, retry/restart and UI-failure evidence remain open | [Run 44297424933](https://github.com/Moshoeshoe333/SOULSYNCMOBILE/actions/runs/44297424933); test blob `b8894b23422f2dd7c949f716812a2ff078da1dde` |

## 11. Residual risk and follow-up
The synthetic partial-write outcome has been reproduced in the mock-backed hook harness in CI run `44297424933` at commit `1b989d1145587cf223fc9bbeecf8d1856536152c`. Current application `main` remains at `1f50bd3387c61d51868140ec3776b94150a2d4c6`, and the test source blob is unchanged. No native-device/runtime proof, retry/restart recovery proof, lost-update proof, duplication proof or user-visible failure-path witness is recorded. The persistence authority/commit contract remains unratified and requires owner approval before architecture or runtime remediation. No application source or test modification is authorized by this defect record.

## 12. Closure decision
- **Decision:** Keep open / Investigating
- **Approver/authority:** SoulSyncMobile project owner
- **Acceptance criteria met:** No
- **Reason:** Synthetic fault injection and its regression suite passed in CI, but no owner-approved consistency contract, corrective application change, native-device/runtime validation or recovery proof exists.
- **Closure evidence:** None

## 13. Reusable lesson
Existing CG-026 is relevant to evidence and repository boundaries. A new cross-project atomicity lesson may be proposed after the failure mode and preventive control are demonstrated; do not promote this source-level observation to Verified.
