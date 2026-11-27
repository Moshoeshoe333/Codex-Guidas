# Mainline Evidence Rebaseline — NAVIGRE and SoulSyncMobile

**Audit date:** 2026-11-27  
**Method:** Exact branch-head/workflow inspection, historical-baseline comparison, source/test/workflow review, exact-head run verification.  
**Scope:** Read-only source audit and documentation-only PR proposals. No application code, test code, dependencies, workflows, release settings, production data or project gates changed.

> CI evidence is limited to commands and environment on the exact SHA. It is not physical runtime or permission to advance a project gate.

## NAVIGRE

Current main: 44db8dbaabe78f98017a427aaf5ac33a4572690c. Historical 2026-09-14 baseline: e94e3583ba46c7358fcd018ee5a2c877ea2cab0a. Compare: 7 commits ahead, 0 behind.

- [Navigre CI run 45989093853](https://github.com/Moshoeshoe333/Mall-Navigre/actions/runs/45989093853) — SUCCESS on exact current main; npm ci, typecheck, npm test.
- [Parking Truth Test run 45989093818](https://github.com/Moshoeshoe333/Mall-Navigre/actions/runs/45989093818) — SUCCESS on exact current main; Playwright Chromium, production build, server startup and browser tests.

The old zero-run statement for e94e358 was true for its September audit time and SHA; it is not the current mainline state.

Browser test source tests/e2e/parking-truth.spec.ts blob 161d33428d185cd02b65c0dc759273520d7b27f2 tests: (1) save → reload → recover → browser offline → find car, disclosing unverified geometry; (2) malformed persisted parking data fails closed. This is bounded browser integration evidence, not physical indoor positioning, real mall geometry, deployed sensors, accessibility certification, security/privacy completeness or L6 readiness.

Localization freshness, temporal resolution, graph validation and routing-start authorization tests are in current main's unit suite; npm test passed. These are not full physical sensor-to-route validation.

Remaining NAVIGRE gaps: real Mall of Africa topology/geometry remains schematic/unverified; GPS/BLE/Wi-Fi are abstractions; accessibility verification is partial; performance/battery and security/privacy review remain outstanding; multi-mall operational proof incomplete; Gate 3 concurrency FROZEN. Rust routing-core remains proposed/conditional/not selected/not implemented; TypeScript remains baseline.

[NAVIGRE PR #19](https://github.com/Moshoeshoe333/Mall-Navigre/pull/19) proposes docs-only README/master-ledger reconciliation. PR head 6109d6d418f178ce3d14af53bdd15a00cfcd6333, base 44db8d. Runs 46013448916 (Navigre CI) and 46013448731 (Parking Truth Test) both failed on attempt 1 and again after a failed-job retry (attempt 2). All four job attempts recorded zero executed steps; the second-attempt log requests returned BlobNotFound. The workflow definitions on main declare ordinary pull_request checks and were not changed by this PR. The underlying pre-step failure remains unknown; this is not evidence that npm, typecheck, unit tests, build or Playwright tests failed. PR remains open/unmerged.

## SOULSYNCMOBILE application mainline

Current app main: 1f50bd3387c61d51868140ec3776b94150a2d4c6.

[Exact-main run 45989069198](https://github.com/Moshoeshoe333/SOULSYNCMOBILE/actions/runs/45989069198) completed SUCCESS on that SHA: typecheck, threat, storage-fault and Guardian-hook fault suites passed. The workflow also runs a read-only npm audit report with || true; audit advisories do not fail the job. Current main has no committed package-lock and CI uses npm install, not npm ci. This is not a clean audit or reproducible dependency graph claim.

[SOULSYNCMOBILE PR #21](https://github.com/Moshoeshoe333/SOULSYNCMOBILE/pull/21) proposes a documentation-only README/build-plan update. Head 47f8cf5db01c450e329d777586d982f2db8eb8ed, base 1f50bd. Run 46013545936 failed on attempt 1 and again after a failed-job retry (attempt 2). Both job attempts recorded zero executed steps; the second-attempt log request returned BlobNotFound. The workflow definition on main declares ordinary pull_request checks and was not changed by this PR. The underlying pre-step failure remains unknown; this is not evidence that npm install, typecheck or any test command failed. PR remains open/unmerged.

## Separate SoulSyncMobile forensic/runtime tracks

| Track | Exact identity | Witness | Evidence ceiling |
|---|---|---|---|
| App main | 1f50bd3387c61d51868140ec3776b94150a2d4c6 | run 45989069198 SUCCESS | Mainline Node/CI test commands |
| G-BOOT harness | branch forensic/g-boot-witness-harness, head 3eae8a53d5c41503201235022f05c21fa45dfdc3 | runs [36731354793](https://github.com/Moshoeshoe333/SOULSYNCMOBILE/actions/runs/36731354793) and [36731365501](https://github.com/Moshoeshoe333/SOULSYNCMOBILE/actions/runs/36731365501) SUCCESS | Harness integrity, claims/typecheck, Semantic33, threat, storage/persistence tests; not physical device |
| E-007 | branch forensic/e007-zero-width-boundary, head 0de0f9de135b644395b9c5c5f74855dbd43a2111 | [run #72 / 36712210801](https://github.com/Moshoeshoe333/SOULSYNCMOBILE/actions/runs/36712210801) SUCCESS | Semantic 33 + zero-width boundary and threat fixtures; not G-BOOT runtime |
| APK build | branch forensic/wu-eas-android-id-001, head 9ce7b6f32164e5a42dc397971aabba52fe880d76 | [run 36997718097](https://github.com/Moshoeshoe333/SOULSYNCMOBILE/actions/runs/36997718097) SUCCESS | EAS build artifact, not device install/boot/runtime |

The runtime-evidence repository main tree at 3ffb2fbf0ca33c77c67ea06ba9d1ceb25980da0a contains only README; no physical-device runtime artifact was located. G-BOOT remains OPEN / PAUSED. An APK build and CI runs cannot substitute for device install, boot, user journey, persistence, restart/recovery and offline runtime.

[SOULSYNCMOBILE-ledger PR #3](https://github.com/Moshoeshoe333/SOULSYNCMOBILE-ledger/pull/3) proposes docs-only separation of these streams. Head 497793c64a5f278291703af58671f11a63c7ad63, base 36f8f7. No CI workflow was found in that ledger repo; PR remains open/unmerged.

## PR validation follow-up — 2026-11-27

A read-only retry investigation was performed after the first PR checks failed:

| PR / check | Workflow run | Attempt-1 job | Attempt-2 job | Result on attempt 2 |
|---|---:|---:|---:|---|
| NAVIGRE #19 — Navigre CI | 46013448916 | 140554491363 | 140562252481 | Failed; zero steps |
| NAVIGRE #19 — Parking Truth Test | 46013448731 | 140554491328 | 140562266601 | Failed; zero steps |
| SOULSYNCMOBILE #21 — typecheck | 46013545936 | 140554817257 | 140562283393 | Failed; zero steps |

The three failed-job rerun requests were accepted by GitHub. The resulting second attempts still failed before the first declared workflow step. Fetching the second-attempt job logs returned HTTP 404 with BlobNotFound for all three jobs. The accessible job summaries do not expose a root-cause diagnostic. This supports the bounded conclusion **pre-step Actions failure, cause unknown**; it does not support claims of application test failure, runner allocation failure, repository-permission failure or a GitHub-wide incident.

The NAVIGRE workflow files .github/workflows/ci.yml and .github/workflows/e2e-truth-test.yml, and the SOULSYNCMOBILE .github/workflows/typecheck.yml, were read from main. Each declares a pull_request trigger; none was changed in the documentation PR. The ledger repository has no workflow configured in its inspected repository tree, so PR #3 has no CI check to retry.

All three PRs remain open and unmerged. Their diffs remain confined to two documentation files each. No workflow or application changes were made during this investigation. Do not merge solely on the assumption that the failures are harmless; obtain a successful PR validation or an independently accepted review path first.
## Findings and next proof

| Claim | Status |
|---|---|
| NAVIGRE current-main CI/browser checks | Verified for bounded checks |
| NAVIGRE physical indoor positioning | Not established |
| SoulSyncMobile current-main CI | Verified for bounded commands |
| SoulSyncMobile dependency reproducibility / clean audit | Not established |
| G-BOOT harness CI | Verified for harness scope |
| E-007 equals G-BOOT runtime | No; separate semantic branch |
| APK build proves install/boot | No |
| SoulSyncMobile physical-device runtime | Not established; G-BOOT OPEN / PAUSED |

Next: diagnose pre-step PR CI failures; review PRs #19/#21/#3; prioritize NAVIGRE geometry/accessibility/security/performance evidence; preserve G-BOOT until a full physical Android witness exists; establish lockfile-based dependency reproducibility. No app code or project gate changed.
