# DEF-2026-001 — Storage hydration failure can be masked as an empty ledger

- **State:** Investigating
- **Severity:** S4 (mock-backed hook behaviour reproduced in CI; native-device/user impact not established)
- **Date detected:** 2026-11-18
- **Last updated:** 2026-11-27
- **Owning project/repository:** SoulSyncMobile — `Moshoeshoe333/SOULSYNCMOBILE`
- **Affected branch/ref:** `main`
- **Original detection baseline:** `b85a83c9f672a11c71b94090826710475d8b6f86` (initial read-only inspection)
- **Latest revalidated application baseline (2026-11-27):** `1f50bd3387c61d51868140ec3776b94150a2d4c6` (`main`; relevant hook and UI source blobs remain unchanged)
- **Owner:** SoulSyncMobile project maintainer (to be assigned)
- **Related CI run:** [44297424933](https://github.com/Moshoeshoe333/SOULSYNCMOBILE/actions/runs/44297424933) — successful on exact test commit `1b989d1145587cf223fc9bbeecf8d1856536152c`
- **Related lessons:** CG-002, CG-011
- **Reporter/source:** Codex-Guidas Tri-Tier 33 read-only pilot 01

## 1. Summary
Source inspection found that a storage hydration error is caught and converted into an unmeasured/empty in-memory snapshot while the hook marks itself ready. The dashboard may therefore present a failed load as an ordinary empty ledger. Runtime impact remains unverified.

## 2. Expected behaviour
A successfully loaded empty ledger must be distinguishable from unavailable, corrupt or unreadable storage. The UI should not imply successful hydration when the storage read failed.

## 3. Observed behaviour
In the inspected source, the Guardian state hook catches errors loading Harmony state and incident logs, resets the snapshot to empty/unmeasured defaults, and sets `ready=true`. The dashboard uses readiness to enable analysis and displays incident count without a storage-health/error indicator.

This was initially a source-path observation. A later synthetic, mock-backed hook test reproduced the readiness/empty-ledger behaviour in CI on exact commit `1b989d1145587cf223fc9bbeecf8d1856536152c` (run `44297424933`). The test asserts `ready=true`, an empty in-memory incident ledger and an empty exported incident array after injected storage-read failure. This is controlled hook-harness evidence, not a native AsyncStorage, device-restart or user-session observation. Production behaviour remains unverified on a physical device.

## 4. Impact and scope
- **Actual impact:** Not established; no runtime reproduction or user report inspected.
- **Potential impact:** A user could mistake unavailable history for a genuinely empty history and proceed without understanding that prior records were not loaded.
- **Affected users/data/components:** Potentially users of the affected hydration path; precise scope unknown.
- **Scope known or unknown:** Source path identified; runtime/platform scope unknown.
- **Workaround / containment:** No workaround validated. Until tested, do not represent an empty fallback as confirmed successful storage hydration.

## 5. Evidence ledger
| Evidence ID | Type | Exact ref (commit/run/log) | Observation | Limitation |
|---|---|---|---|---|
| E-001 | Source | `SOULSYNCMOBILE` `src/hooks/useGuardianState.ts`, blob `db52b38fd4c9f8909f33df78c8e2752e18993fe2` | Hydration catch path resets snapshot and sets ready | Source inspection only; no fault injection |
| E-002 | Source | `SOULSYNCMOBILE` `App.tsx`, blob `17b1b37df4f93547c099129cff883571c5e9b1d5` | Dashboard readiness/count presentation lacks explicit storage error state | Source inspection only; no UI runtime witness |
| E-003 | Assessment | Codex-Guidas `doctrines/tri-tier-33/pilots/2026-11-18-soulsyncmobile-readonly-pilot-01.md`, blob `fd2b543792afd9dbcd05808f29eab170a96ad043`, finding F-07 | Initial consolidated finding and limitations | Assessment is not an independent runtime test |
| E-004 | Test source | `SOULSYNCMOBILE` `src/hooks/__tests__/useGuardianState.fault-injection.test.ts`, blob `b8894b23422f2dd7c949f716812a2ff078da1dde` at current application baseline `1f50bd3387c61d51868140ec3776b94150a2d4c6` | Defines the synthetic hydration-read rejection case and asserts ready/empty hook state and empty export | Test source alone is not execution evidence; mock-backed hook harness only |
| E-005 | CI execution | [GitHub Actions run 44297424933](https://github.com/Moshoeshoe333/SOULSYNCMOBILE/actions/runs/44297424933), head commit `1b989d1145587cf223fc9bbeecf8d1856536152c` | Run completed SUCCESS; `npm run test:guardian-faults` passed 2/2, including the hydration case; typecheck, threat fixtures 13/13 and storage fault tests 10/10 also passed | Run is on an ancestor of current `main`; it proves the recorded harness tests at that exact commit, not native-device or current-HEAD runtime behaviour |

## 6. Root-cause analysis
- **Status:** Synthetic hook-harness behaviour reproduced; native runtime and user impact not confirmed
- **Hypothesis:** Hydration error handling collapses a storage failure into the same state representation used for a successfully loaded empty ledger.
- **Evidence supporting:** E-001 and E-002.
- **Evidence contradicting:** No contrary evidence inspected; caller/runtime behaviour remains untested.
- **Remaining discriminating proof:** Agree the owner-approved storage-state contract; test UI error communication, restart/restoration and native AsyncStorage behaviour on the supported device/runtime. Do not count the mock-backed CI run as device proof.

## 7. Similarity search
- **Search terms:** storage hydration failure; empty ledger fallback; fail-closed; persistence read error
- **Lesson IDs searched:** CG-002, CG-011
- **Prior defect IDs:** No individual DEF record found at intake.
- **Similarity result:** Related to test-scope honesty and fail-closed semantics; no claim of identical root cause in another project.

## 8. Corrective action
None authorized or implemented. Remediation requires owner review after P-01 reproduction and an explicit storage-state contract.

## 9. Preventive and detective controls
- **Proposed:** Model loaded-empty, unavailable, corrupt and loading as distinct states.
- **Proposed:** Add synthetic read-failure tests and a UI assertion that unavailable storage is never rendered as a confirmed empty ledger.
- **Verified:** None.

## 10. Regression and acceptance evidence
| Check | Command / procedure | Environment | Exact commit | Expected | Actual | Evidence link |
|---|---|---|---|---|---|---|
| P-01 | `npm run test:guardian-faults` — synthetic adapter rejects `getItem` in the hook harness | GitHub Actions, run `44297424933` | `1b989d1145587cf223fc9bbeecf8d1856536152c` | Test records `ready=true`, empty in-memory incidents and empty export after read rejection | PASS as a mock-backed characterization; suite 2/2 | [Run 44297424933](https://github.com/Moshoeshoe333/SOULSYNCMOBILE/actions/runs/44297424933) |

## 11. Residual risk and follow-up
Native AsyncStorage behaviour, process/device restart, restoration, visible error communication, platform scope and actual user impact remain unknown. The hook-level synthetic test now reproduces the characterized ready/empty state in CI. Next action: obtain owner approval for the storage-state contract and define the native/runtime and UI acceptance checks. No application remediation is authorized by this record.

## 12. Closure decision
- **Decision:** Keep open / Investigating
- **Approver/authority:** SoulSyncMobile project owner
- **Acceptance criteria met:** No
- **Reason:** The mock-backed characterization test passed, but no owner-approved contract, corrective change, native-device/runtime validation or recovery proof exists.
- **Closure evidence:** None

## 13. Reusable lesson
Existing CG-011 is relevant. Consider a new cross-project lesson only after the failure mode and preventive control are demonstrated; do not promote this source-level observation to Verified.
