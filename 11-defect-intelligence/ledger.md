# Defect Intelligence Ledger

**Repository:** Codex-Guidas  
**Register status:** Active; initial cross-project index  
**Purpose:** Preserve faults, defects, near misses, failed tests, evidence gaps and corrective lessons so they can be retrieved and used to prevent recurrence.

> A recorded finding is not automatically a reproduced defect. A proposed correction is not a verified correction. Never upgrade status without evidence.

## 1. Operating rules

1. Preserve the original failure or observation before changing anything.
2. Assign a stable record ID and link the detailed project evidence.
3. Separate observed facts, source-level findings, reproduction results, root-cause hypotheses and interpretations.
4. Record exact repository, branch, commit, environment, command, inputs, logs and date where available.
5. Assess impact and contain risk before pursuing a fix.
6. Reproduce with the smallest safe test; use synthetic data for fault injection unless real data is explicitly necessary and authorized.
7. Make only the smallest authorized correction.
8. Add a regression test and test the prevention mechanism itself.
9. Verify against the exact corrected commit; preserve failed runs and residual risks.
10. Search for analogous exposure in other projects, but transfer only the lesson—not unexamined project-specific assumptions.
11. Close only with evidence, owner, date, exact commit/run and residual-risk statement.
12. Never put secrets, credentials, personal messages, banking data or unnecessary personal information in this ledger.

## 2. Status vocabulary

| Status | Meaning |
|---|---|
| REPORTED | A concern has been reported but not yet independently inspected. |
| SOURCE-OBSERVED | The relevant source/configuration was inspected; runtime behaviour may remain untested. |
| REPRODUCED | A controlled test or exact reproduction demonstrated the failure. |
| HYPOTHESIS | A possible cause or impact requiring verification. |
| CONTAINMENT-PROPOSED | A containment action has been proposed but not verified. |
| CONTAINED | Evidence confirms the immediate risk is bounded. |
| FIX-PROPOSED | A corrective change is documented but not authorized/applied. |
| FIXED-UNVERIFIED | A change exists, but the relevant verification has not passed. |
| VERIFIED | The reproduction and relevant regression/prevention checks passed on an exact commit/environment. |
| CLOSED-WITH-RESIDUAL-RISK | Closure is evidence-backed and remaining limitations are explicit. |
| SUPERSEDED | Replaced by a newer record; preserve the historical link and reason. |

Do not use “resolved” as a synonym for “documented”, “implemented” or “tests passed”.

## 3. Required record template

For every new record, capture as much as is known; unknown fields must remain explicitly unknown.

- **Record ID / title:**
- **Project / repository:**
- **Date first observed / reporter:**
- **Status:**
- **Severity / rationale / affected users:**
- **Exact branch, commit, environment and configuration:**
- **Expected behaviour / contract:**
- **Observed behaviour:**
- **Evidence references (files, lines, logs, run IDs, screenshots):**
- **Reproduction steps / minimal synthetic case:**
- **Confirmed facts:**
- **Root-cause hypothesis and confidence:**
- **Impact, blast radius and data-integrity implications:**
- **Containment / immediate safety action:**
- **Corrective change and authorization:**
- **Preventive control (contract, code, test, CI, monitoring, procedure or training):**
- **Regression test and expected result:**
- **Verification commit, run, environment, result and date:**
- **Residual risk / untested scope:**
- **Cross-project analogues and applicability limits:**
- **Owner / review trigger / closure decision:**

## 4. Initial records

### DI-2026-11-18-SSM-001 — SoulSyncMobile read-only Tri-Tier 33 pilot findings

- **Project:** `Moshoeshoe333/SOULSYNCMOBILE`
- **Status:** SOURCE-OBSERVED; no dynamic reproduction or remediation verified.
- **Observed target revision:** `main` at `b85a83c9f672a11c71b94090826710475d8b6f86` (2026-10-02).
- **Detailed evidence:** [Tri-Tier 33 Pilot 01 — SoulSyncMobile](../doctrines/tri-tier-33/pilots/2026-11-18-soulsyncmobile-readonly-pilot-01.md).
- **Framework:** CG-TT33 v0.3.0-draft; this is a bounded desk review, not a security audit or framework validation.

The detailed report contains eight findings:

| Finding | Summary | Evidence/status boundary |
|---|---|---|
| F-01 | Malformed URL parsing can skip an input and potentially fall through to ALLOW | Source-level path observed; runtime/exploitability not established |
| F-02 | `safe` maps to `ALLOW`, whose user meaning is ambiguous | Policy clarification required; not a confirmed unsafe outcome |
| F-03 | Confidence score has no inspectable calibration contract | Evidence gap; calibration not performed |
| F-04 | Hand-authored fixtures are regression examples, not detection-effectiveness validation | Coverage limitation observed; no corpus validation |
| F-05 | CI and dependency reproducibility lack evidence for the inspected revision | OPEN; workflow not rerun and tree not exhaustively inspected |
| F-06 | Persisted JSON is cast to typed records without runtime shape validation; offline assurance is unwitnessed | Source-level weakness observed; runtime consequences untested |
| F-07 | Hydration failure can be represented as a ready, empty ledger | Source path observed; synthetic fault injection not run |
| F-08 | One logical scan is written across two sequential, non-atomic storage operations | Source path observed; partial-write failure not dynamically reproduced |

**Linked verification designs:** P-01 through P-09 in the detailed report. All nine are proposed synthetic-only probes and remain NOT RUN until execution evidence is attached.

**Immediate next step at initial review (2026-11-18):** Define the persistence contract and execute controlled, isolated synthetic tests. Subsequent work added and executed targeted Guardian hook fault tests; see the dated follow-up sections below. This historical initial recommendation is not the current evidence state.

**Authorization boundary:** This record does not authorize modifications to SoulSyncMobile, CI dispatch, release, production data handling or deployment. Any remediation requires a separate proposal and owner approval.

**Cross-project lessons to test—not assume:**
- A missing/failed read must not masquerade as a valid empty state.
- A multi-write logical action needs an explicit commit/consistency contract.
- Runtime data must be validated at trust boundaries; static types do not validate stored JSON.
- A low heuristic score is not proof of safety; UI wording must match what was actually measured.
- Regression fixtures do not establish real-world detection effectiveness.
- Test failure, test absence and test non-execution are different states.

**Closure condition:** Reproduce or falsify the relevant probes; approve and implement any required fix through the target project's governance; pass the exact regression and prevention tests; record exact commit/run and residual risk. Until then this record remains SOURCE-OBSERVED.

---

## 5. Retrieval and maintenance

- Add new project records here using stable IDs; keep detailed evidence and remediation history in the project-specific report or ledger.
- Link each central entry to its canonical detailed record. Do not duplicate full reports or silently overwrite history.
- Review OPEN, REPRODUCED, FIXED-UNVERIFIED and overdue records at each relevant project gate.
- Periodically search for repeated failure patterns across repositories and update reusable lessons with clear applicability limits.
- A green test suite does not prove all failure modes are covered; record what was not tested.


### Follow-up implementation — SSM-PERSISTENCE-FI-001 test harness

- **Status:** TEST HARNESS VERIFIED for the bounded CI scope; underlying application findings remain SOURCE-OBSERVED.
- **Target repository:** `Moshoeshoe333/SOULSYNCMOBILE`.
- **Target commit:** `c7a1b73516a40a3684c833290f5315993d199430`.
- **Base inspected:** `b85a83c9f672a11c71b94090826710475d8b6f86`.
- **Files added:** `test-support/async-storage-mock.mjs`, `test-support/async-storage-mock.d.mts`, `test-support/async-storage-loader.mjs`, `src/storage/__tests__/storageManager.fault-injection.test.ts`.
- **Package change:** Added `npm run test:storage-faults` and routed the existing `test:threat` script through the shared TypeScript test loader; application source files were not modified.
- **Verification:** New files and package script were fetched back from GitHub and inspected. A local temporary harness executed the inspected storage-manager logic and passed 10/10 tests under Node `v22.16.0`. More importantly, GitHub Actions run `44295046974` on exact target commit `4396215ebb190c856312eb083909bf4f6757e4fd` completed SUCCESS: `npm run typecheck` passed; `npm run test:threat` passed all 13 fixtures; `npm run test:storage-faults` passed all 10 tests (0 failures). This verifies the committed test suite on the GitHub Node `22.13.1` environment, not native-device AsyncStorage, app restart, offline behaviour, or hook-level transaction semantics.
- **Test coverage authored:** missing/malformed incident data; invalid incident shape characterization; incident read/write rejection; unmeasured/malformed/invalid Harmony data; Harmony normalization write failure; clear-storage failure.
- **Important characterization:** Source inspection shows `getHarmonyState()` catches a normalization-write rejection in its broad catch and returns UNMEASURED while the invalid bytes remain stored. The test now records this observed behaviour rather than asserting a rejection that the current implementation does not produce.
- **Important limitation:** The harness replaces the AsyncStorage package with an isolated in-memory mock while exercising the actual `storageManager` module. It does not prove native AsyncStorage, device restart, offline behaviour, hook hydration, or the two-write scan transaction. Those remain separate probes.
- **CI integration:** Added `npm run test:storage-faults` to `.github/workflows/typecheck.yml` in commit `8886b367225a2b4f80d98ca4d19b060135ad18e4`. No workflow was manually dispatched; GitHub automatically queued runs on `main` pushes. Run `44294591099` failed at `npm run typecheck` with TS5097 because the test imported `../storageManager.ts` while `allowImportingTsExtensions` is not enabled. Corrected the test to use an extensionless import and updated the test-only loader to resolve it (`bbd70470a48b1c72f0e11d1571d51c3cee4189d0`, `955103f2ea16b1d3b3f002b9b14e2713916e14aa`). Run `44294672395` passed TypeScript typecheck but failed the pre-existing `test:threat` command because Node 22 could not resolve extensionless imports (`ERR_MODULE_NOT_FOUND`). Run `44294689420` failed for the same resolver issue. The shared loader now resolves the existing threat-engine and fixture modules as well as the storage manager; `test:threat` now uses that loader. Run `44294923393` reached the fixture assertion and failed specifically on stale `EWALLET-001` expected severity 28; three existing indicators match its text, so the correct characterization under current scoring is 42. Fixture expectation corrected in target commit `4396215ebb190c856312eb083909bf4f6757e4fd`. Final run `44295046974` on that exact commit completed SUCCESS with typecheck + both test suites passing.
- **Workflow hygiene lesson:** Creating several sequential commits directly on `main` caused repeated, overlapping push-triggered CI runs. For future multi-file changes, prefer one atomic tree commit or a dedicated branch/PR so validation runs once against a coherent snapshot. No manual CI dispatch occurred.
- **Dependency observation:** The `npm install` log for run `44294312497` reported 23 dependency vulnerabilities (2 moderate, 21 high). This is an untriaged package-manager summary only; package identities, paths, exploitability and production impact are not yet established. Do not run `npm audit fix` or upgrade dependencies without a separate scoped review.
- **Next gate at this follow-up's time:** Design and execute a hook-level test for hydration failure and the incident-write/Harmony-write partial-commit case. This was subsequently completed in the CI witness documented below. Remaining gates are owner ratification of the persistence authority/commit contract, native-device/restart/UI recovery validation, and a separate read-only dependency review before any upgrade. The recorded npm audit summary is not an approved fix recommendation. Do not change app runtime code until the persistence contract and dependency compatibility questions are resolved.


### Follow-up protocol — SSM-PERSISTENCE-FI-001

- **Status:** TEST DESIGN ONLY; NOT EXECUTED.
- **Protocol:** [Synthetic Persistence Fault-Injection Protocol](../doctrines/tri-tier-33/pilots/2026-11-18-soulsyncmobile-persistence-fault-injection-protocol.md).
- **Priority sequence:** P-01 hydration read failure → P-04 partial two-write failure → P-07 write rejection → P-02 malformed JSON → P-03 invalid record shape.
- **Safety boundary:** Isolated mock storage and synthetic fixtures only. No real SMS/banking data, no production storage, no application behavior changes and no CI dispatch under this protocol.
- **Decision required before execution:** Project-owner approval for test-only changes and ratification of the logical persistence authority/commit model. If that contract is undecided, assertions remain BLOCKED-PENDING-DECISION.
- **Current result for this standalone five-probe protocol:** All five probes remain NOT RUN in the record of this protocol. This does not mean the later, separate Guardian hook fault-injection suite was unexecuted; its CI witness is recorded below. This protocol is not itself evidence of application behaviour.



### Follow-up — Guardian hook persistence fault injection and dependency audit

- **Target repository:** `Moshoeshoe333/SOULSYNCMOBILE`.
- **Base:** `4396215ebb190c856312eb083909bf4f6757e4fd`.
- **Hook-test commit:** `a3c6ae3a945aee82612a91c8072f8202347a6c78`; TypeScript assertion correction: `b010ce0096a36f95fa5588776fe1c5ba1c449eac`.
- **Scope:** Added a minimal test-only hook renderer and React-hook mock; added two characterization tests for hydration-read failure and partial incident/Harmony persistence. Added `npm run test:guardian-faults` and included it in GitHub Actions. No application runtime file was changed.
- **Source-observed behaviour 1:** `useGuardianState` catches any hydration error, replaces the in-memory snapshot with empty defaults, and sets `ready=true`. This can present failed restoration as an apparently ready empty ledger.
- **Source-observed behaviour 2:** `analyzeAndLogInput` persists incidents first and Harmony second, then updates its in-memory snapshot only after both writes succeed. A Harmony write failure can therefore leave a persisted incident while the in-memory ledger remains unchanged.
- **Test status:** First CI attempts failed TypeScript strictness on inferred callback parameters and nullable mock-storage data (runs `44297060361`, `44297072328`). Test-only type corrections committed as `b010ce0096a36f95fa5588776fe1c5ba1c449eac`. Run `44297244025` failed typecheck because the second readiness predicate remained implicitly typed; corrected globally in commit `1b989d1145587cf223fc9bbeecf8d1856536152c`. GitHub Actions run `44297424933` on exact commit `1b989d1145587cf223fc9bbeecf8d1856536152c` completed SUCCESS. Typecheck passed; threat fixtures 13/13 passed; storage fault tests 10/10 passed; Guardian hook fault tests 2/2 passed. The two hook tests reproduced both characterized failure modes in the isolated mock-backed hook harness.
- **Dependency audit witness:** Push-triggered run `44297111073` completed the read-only `npm audit --json` report step successfully before the separate TypeScript test failure. Audit summary: 23 findings (21 high, 2 moderate, 0 critical), affecting 22 package names in the resolved install graph. Direct vulnerable packages reported: `expo` and `react-native`; remaining packages are transitive, including Expo CLI/Metro, Metro, Babel preset, React Native codegen/community CLI, `tinyglobby`, `picomatch`, and `minimatch`.
- **Advisory detail:** npm audit reported GHSA-g3hv-75wg-m249 for minimatch (potential denial of service via globparts amplification) and GHSA-fc5q-39xc-vjpf for picomatch (ReDoS through repeated extglobs). npm's suggested remediation changed between unpinned installs: an earlier run suggested Expo 50.0.2, while the latest successful audit run `44297424933` suggested Expo 54.0.33 and React Native 0.83.10, both with major-version change flags, despite this app declaring Expo ~57.0.0 and React Native 0.86.0. This drift reinforces that the graph is not locked and that npm's proposed versions are not safe instructions. This is not a safe automated fix recommendation; do not apply it. First establish the correct supported SDK/dependency matrix and inspect each advisory's affected code paths.
- **Evidence limitation:** No committed package lockfile was found in the inspected tree. `npm install` resolves an ephemeral dependency graph on each CI run; audit results can change and are not yet pinned to a reproducible lockfile. The audit summary does not prove runtime exploitability in the shipped app. Treat it as a high-priority dependency supply-chain investigation, not 23 confirmed exploitable app vulnerabilities.
- **CI hygiene:** Multiple sequential commits to `main` generated overlapping push-triggered CI runs and redundant installs. Future test-only multi-file changes should use one atomic tree commit where possible.
- **Next gate:** Verify run `44297244025` and the Guardian test logs. Then define persistence semantics explicitly: whether a scan is one logical transaction, whether a durable outbox/journal is justified, what the UI reports after partial persistence, and how hydration failure is surfaced. No runtime fix or dependency upgrade until that contract and supported Expo/RN compatibility are reviewed and ratified.



### Verification update — Guardian fault tests CI witness

- **Exact target commit:** `1b989d1145587cf223fc9bbeecf8d1856536152c`.
- **GitHub Actions run:** `44297424933` — SUCCESS.
- **Checks:** TypeScript typecheck PASS; threat fixture suite 13/13; persistence-adapter suite 10/10; Guardian hook suite 2/2.
- **Guardian test outcomes:** (1) injected incident-ledger read rejection resulted in `ready=true` with empty in-memory ledger; (2) injected Harmony write rejection left the incident persisted while the hook snapshot/export remained unchanged. These are controlled mock-backed reproductions of the inspected hook logic, not physical-device tests.
- **Dependency audit from the same run:** 23 findings (21 high, 2 moderate, 0 critical). Direct affected dependencies: Expo and React Native. Transitive affected packages include Expo CLI/Metro, Metro, Babel preset, React Native codegen/community CLI, `tinyglobby`, `picomatch`, `minimatch`, `jest-util`, and `jest-worker`. The two advisory records exposed directly in the audit JSON are GHSA-g3hv-75wg-m249 (minimatch DoS) and GHSA-fc5q-39xc-vjpf (picomatch ReDoS).
- **Important version drift:** The npm audit recommendation varied across fresh `npm install` runs (Expo 50.0.2 in one run, Expo 54.0.33 in the latest, React Native 0.83.10), each marked as a major-version change. The app declares Expo ~57.0.0 and React Native 0.86.0. No dependency was changed. Do not treat the suggested versions as an approved fix.
- **Residual limits:** The audit graph is not lockfile-pinned; runtime exploitability and production reachability have not been established. Hook tests use a minimal React-hook harness and mock AsyncStorage; native storage, process restart, OS-level lifecycle, and actual device behaviour remain untested. The persistence contract is not ratified and application runtime remains unchanged.



### Decision package — SSM-PERSISTENCE-CONTRACT-DECISION-001

- **Status:** PROPOSAL ONLY — NOT RATIFIED.
- **Document:** [SoulSyncMobile Persistence Contract — Decision Proposal](../doctrines/tri-tier-33/pilots/2026-11-18-soulsyncmobile-persistence-contract-decision-proposal.md).
- **Document commit:** `5533c260198eb8294daa9bd9119b7289144ec48c`.
- **Recommendation:** Evaluate a single versioned canonical Guardian snapshot (Option B) to remove the known two-key split-write sequence. This is not a claim of AsyncStorage crash atomicity and is not authorization to implement.
- **Decision required:** Owner ratification of the persistence authority, commit boundary, failure states, retention limits, migration and native-device acceptance tests.
- **Dependency workstream:** Resolve the SDK/RN compatibility and reproducible-lockfile questions before proposing any upgrades. No dependency change has been made.


### Follow-up — SoulSync Guardian Gate A candidate implementation (2026-11-27)

- **Target repository:** `Moshoeshoe333/SOULSYNCMOBILE`.
- **Mainline baseline:** `1f50bd3387c61d51868140ec3776b94150a2d4c6`; main was not modified by this candidate.
- **Candidate PR:** [#22 — Implement privacy-first manual triage MVP](https://github.com/Moshoeshoe333/SOULSYNCMOBILE/pull/22).
- **Implementation source snapshot inspected:** `d13038507107e993c55d1ae34f688f18bdeaef5e`; Git tree `f3e8c4ce2b6f91ad56a2e9bec772a4cbb474a71b).
- **Current disposition:** PR observed open and unmerged. The candidate branch is not a mainline correction and no defect is closed by this follow-up.

**Candidate changes relevant to existing records**

- **DEF-2026-003:** The candidate Guardian hook at blob `2a4f258f1254c788f0e95e2d5c020a8407ebc46f` performs bounded, in-memory analysis and does not call a persistence adapter. The assessed recursive tree contained 34 paths, was not truncated, and had no path-name matches for `storage` or `async-storage`. The PR removes the old AsyncStorage adapter/dependency and scan-history path. This is source-level evidence of removing the app-controlled raw-scan persistence path; it is not device-level privacy evidence.
- **DEF-2026-004:** The candidate type contract at blob `561932c21b58a85e42ac501fb03edb9e938eb608` defines four advisory assessments and no confidence/action field. The heuristics at blob `0c8528ac0785a014d7f22f5c112573e0d0d38f18` route malformed URLs to `unable_to_assess`, detected URL indicators to at least `caution`, and do not claim link enforcement. Fixture and assertion files were updated at blobs `686022cb846a0c29fe0d6817dcb8fa2e7e01f61f` and `dda7aefdead2026e94eae0d90910c6b728104d40`.

**Verification boundary**

- Exact-head GitHub Actions run [46017679147](https://github.com/Moshoeshoe333/SOULSYNCMOBILE/actions/runs/46017679147) on `d13038507107e993c55d1ae34f688f18bdeaef5e` concluded **FAILURE**; the job named `typecheck` returned no step records, and the log endpoint returned 404 / BlobNotFound. The failing phase is unknown.
- No passing CI or test-suite witness is claimed for this candidate source snapshot.
- No Android/iOS build, physical-device runtime, network-disabled test, independent labelled corpus, user-comprehension study, or platform privacy test is claimed.
- The candidate's heuristic thresholds remain provisional; fixture expectations are regression specifications, not efficacy evidence.

**Record disposition:** DEF-2026-003 and DEF-2026-004 remain **Investigating** against mainline. Reassess after PR merge or rejection, exact-head CI diagnostics and tests, and the relevant separate acceptance evidence. Do not mark either finding fixed/verified from source changes or a documentation-only commit alone.
