# Repository Archaeology — Initial Source Audit

**Audit date:** 2026-11-18  
**Scope:** Selected authoritative files and commit records from the linked project repositories.  
**Status:** Partial source audit; not a complete history, security audit, or fresh test execution.

## Audit method and limits

Repositories and default branches were identified through GitHub metadata. Selected files were fetched from their default branches and selected commits inspected. This establishes that the cited source artifacts existed at the fetched revisions. It does not execute code, rerun tests, independently validate legal claims, or prove that a historical workflow remains green today.

For the exact commit boundary, no combined commit statuses or PR-associated workflow runs were returned by the queried status endpoints for the selected recent commits. **No result is not a failed run**; it means this audit did not observe those records through those endpoints.

## 1. ScoutSA

**Repository:** [Moshoeshoe333/ScoutSA](https://github.com/Moshoeshoe333/ScoutSA)  
**Branch inspected:** `main`

### Primary sources inspected

- [Canonical gate status](https://github.com/Moshoeshoe333/ScoutSA/blob/main/docs/00-gate-status.md) — blob `c79cde2979ad44f2a5811f20cf573cdc428a6013`.
- [Engineering integrity policy](https://github.com/Moshoeshoe333/ScoutSA/blob/main/docs/engineering-integrity.md) — blob `a466c3092867549a46e49768c4dc1fab5bbc664e`.
- [Go-to-market and pilot design](https://github.com/Moshoeshoe333/ScoutSA/blob/main/docs/research/go-to-market-pilot-design-2026-10-09.md) — blob `0dfba765f600afaa2980e57b2e42fdf6b172f4b4`.
- Recent inspected commit: [`9ea9ef6`](https://github.com/Moshoeshoe333/ScoutSA/commit/9ea9ef69e57ebb057e7a869af6a4f462cdfbb673), documenting the mainline guard defect/correction.

### Source-backed findings

1. The canonical gate record explicitly states that Gate 1 is closed and Gate 2 is closed at conceptual level. The conceptual ERD, MVP boundary, MVP relationship subset, implementation prerequisites, schema boundary and physical table boundary are frozen/ratified at their recorded levels.
2. SQL remains a reviewed draft. A PostgreSQL 17.11 isolated non-production runtime witness is recorded for an exact SQL blob: 26 tables and 17 foreign keys observed. This does not authorize production migration.
3. Migration/database execution, RLS, API, UI and production implementation remain on hold or unauthorized. The access-policy matrix still requires ratification. External validation is the controlled next move.
4. The pilot design is explicitly a proposal and does not authorize RLS, migration, API/UI implementation, public listings or production use. It prioritizes synthetic/tabletop and closed adult organizational rehearsal before any limited live pilot.
5. The engineering-integrity policy defines a source-of-truth hierarchy: ratified decisions; source code/schemas; executed tests/workflows; verification records; gate status/README; planning notes.
6. It records concrete incidents:
   - DOC-001: version and test-count documentation drift.
   - DOC-002: a README write landed on the wrong branch because the branch argument was omitted.
   - DOC-003: initial documentation-integrity tests failed due to fragile generated regex/template syntax and brittle Markdown assertions; later successful runs are separately recorded.
   - DOC-004: README and gate-status summary drifted from the canonical current state.
   - CI-001: zero-byte PostgreSQL workflow placeholders created misleading zero-job CI failures.
7. Preventive controls include explicit branch arguments on writes, reading changed files back from the intended branch, inspecting diffs, testing direct string/line comparisons, checking zero-byte workflow files, and separate mainline/prototype integrity workflows.

### Transferable lessons

- Repository writes need branch identity as an explicit precondition.
- A successful write response is not a completed documentation correction; read-back and diff inspection are required.
- A CI failure must be attributed to the correct workflow, run and job. Empty or unrelated workflow entries can create misleading noise.
- Generated tests should use the simplest robust parsing strategy for the source format; test the guard itself before trusting it.
- Mainline and prototype are distinct authority/evidence boundaries. Passing one suite does not certify the other.
- Historical test success must remain attached to the exact run, commit, scope and environment.
- External validation is not permission to cross implementation holds.

### Important non-claims

This audit did not rerun the recorded CI runs, inspect every branch, or authorize implementation. The PostgreSQL witness is not a production migration, and no POPIA/Children's Act/SAFA/FIFA compliance conclusion is made.

## 2. SoulSync 3

**Repository:** [Moshoeshoe333/soulsync-3](https://github.com/Moshoeshoe333/soulsync-3)  
**Branch inspected:** `main`

### Primary sources inspected

- [33-Tier Framework](https://github.com/Moshoeshoe333/soulsync-3/blob/main/docs/33-tier-framework.md) — blob `bf3badc8a30a44779354302b66787da0c28eff05`.
- [Deep immutability test](https://github.com/Moshoeshoe333/soulsync-3/blob/main/tests/test_coordinate99.py) — blob `ebd57d9a644b0998ad09531e2d1e1a817a2811dc`.
- [Framework documentation commit](https://github.com/Moshoeshoe333/soulsync-3/commit/e7771d4b087ce9ff66ceb45b0cf86114e9241cb7).
- [Deep immutability test commit](https://github.com/Moshoeshoe333/soulsync-3/commit/ddcd79046248c8ee4b04238b0489b92199de21fd).
- [Repository README](https://github.com/Moshoeshoe333/soulsync-3/blob/main/README.md) — blob `f39189635d5666f3b41eb052fc365ce5d31b814a`.

### Source-backed findings

1. The repository describes a deterministic policy/evidence core with governed state transitions, cryptographic provenance and fail-closed execution as its design intent.
2. The 33-Tier Framework defines **Point → Knowing → Witness → Gate** and a research workflow from question/contract through source fetching, evidence ledger, verification and sourced report.
3. The framework explicitly says that the detailed tier definitions, dependencies, entry/exit criteria, evidence requirements and validation method remain open. It does not claim all 33 tiers are specified or independently validated.
4. The inspected test commit adds tests for deeply immutable structured observations, mutation rejection at nested mapping/list boundaries, and detachment from later mutation of the original source object.
5. The test file contains 15 named tests in the inspected version. This source inspection does not establish that all 15 or the full repository suite were executed on the current HEAD.

### Transferable lessons

- Immutability must include nested structures and source detachment, not only a frozen outer object.
- Absence should remain a typed state rather than being collapsed into zero, false or a guessed default.
- Provenance/lineage does not itself confer authorization.
- A semantic projection should not quietly create an execution or authorization path.
- A methodology must disclose its own incomplete specification and validation status.

### Important non-claims

No test suite was rerun in this audit. No cross-runtime compatibility, production security, or full 33-tier validation claim is made.

## 3. SoulSyncMobile and its evidence repositories

**Application:** [Moshoeshoe333/SOULSYNCMOBILE](https://github.com/Moshoeshoe333/SOULSYNCMOBILE)  
**Forensic ledger:** [Moshoeshoe333/SOULSYNCMOBILE-ledger](https://github.com/Moshoeshoe333/SOULSYNCMOBILE-ledger)  
**Runtime evidence repository:** [Moshoeshoe333/SOULSYNCMOBILE-runtime-evidence](https://github.com/Moshoeshoe333/SOULSYNCMOBILE-runtime-evidence)

### Primary sources inspected

- [Application README](https://github.com/Moshoeshoe333/SOULSYNCMOBILE/blob/main/README.md) — blob `e9b82c85147cfbaa4f3c942a4968c022dbbd9092`.
- [package.json](https://github.com/Moshoeshoe333/SOULSYNCMOBILE/blob/main/package.json) — blob `e1ba351318e517c326a8135f3fa01c4d461cc8b1`.
- [app.json](https://github.com/Moshoeshoe333/SOULSYNCMOBILE/blob/main/app.json) — blob `1ba216e6948baafc2018277344851fcf72876b50`.
- [Forensic ledger README](https://github.com/Moshoeshoe333/SOULSYNCMOBILE-ledger/blob/main/README.md) — blob `0c4760f7e38ab826eebfad9e42c31f92e6fb7dc6`.
- [Methodology Delta](https://github.com/Moshoeshoe333/SOULSYNCMOBILE-ledger/blob/main/methodology-delta.md) — blob `8346490cf8e0608da4daa7ddd5e7b7578f9a5752`.
- [Runtime evidence README](https://github.com/Moshoeshoe333/SOULSYNCMOBILE-runtime-evidence/blob/main/README.md) — blob `9eacbc4e930d98851653db2bd13ad437c551b8f3`.
- [Recent fixture import correction](https://github.com/Moshoeshoe333/SOULSYNCMOBILE/commit/b85a83c9f672a11c71b94090826710475d8b6f86).

### Source-backed findings

1. The app README describes SoulSync Guardian v3.1 as an offline-first mobile threat-analysis and personal-security ledger, with an explicit evidence-first method.
2. The README lists Expo React Native + TypeScript, offline threat analysis, AsyncStorage adapter, deterministic compound-risk scoring and fail-closed analysis/storage boundaries.
3. The README calls AsyncStorage a bootstrap layer and SQLite a production gate. It lists G0–G8 and states overall status **OPEN / evidence pending**.
4. The inspected package declares Expo `~57.0.0`, React Native `0.86.0`, React `19.2.3`, TypeScript `~5.9.2`, AsyncStorage `^2.2.0`, and scripts for typecheck and threat-fixture tests. Package declarations are not runtime compatibility evidence.
5. The forensic ledger separates application source from forensic evidence. It records a historical audited baseline and E-007 CI witness (Run #72), including 16 Semantic 33 cases and 16 threat fixtures with zero mismatches. It explicitly says G-BOOT runtime stages were not executed and mobile runtime remained N/A.
6. The ledger README identifies G-BOOT as open until actual mobile runtime evidence exists.
7. The methodology delta states discovery can be autonomous but authority cannot; candidate threat patterns must pass normalization, deterministic review and fixture/CI evidence before entering the threat fixtures. Agents must not directly modify the production threat engine or become a cloud dependency of the offline app.
8. It also records a minimal-change loop: FAILURE → MINIMAL FIX → DIFF AUDIT → INVARIANT AUDIT → EXECUTION.
9. The recent app commit fixes a fixture import path for TypeScript typechecking. This is a narrow test-source correction, not proof of a successful build or device runtime.

### Transferable lessons

- Preserve a three-way boundary between app code, forensic ledger and runtime evidence.
- CI harness execution is not physical mobile runtime evidence.
- Discovery and candidate generation can be automated; policy authority and production changes remain controlled.
- Keep threat decisions in a closed, deterministic vocabulary; model-assisted observations must not become authority.
- Use minimal fixes and audit the diff/invariants before broad refactors.
- AsyncStorage is explicitly a bootstrap persistence layer in this project, not an assumed production-grade ledger store.
- A current README's open gates take precedence over an older ledger baseline when describing current app maturity; historical evidence remains attached to its exact old commit.

### Reconciliation note

The forensic ledger's E-007 record is tied to an older audited baseline/PR head and run ID. The app repository has advanced to later commits. This audit did not establish that E-007 evidence transfers to the current application commit. The app README's **OPEN / evidence pending** status and G-BOOT hold are therefore retained. No APK, installation or mobile runtime success is claimed.

## 4. NAVIGRE / Mall-Navigre

**Repository:** [Moshoeshoe333/Mall-Navigre](https://github.com/Moshoeshoe333/Mall-Navigre)  
**Branch inspected:** `main`

### Primary sources inspected

- [Master Evidence Ledger](https://github.com/Moshoeshoe333/Mall-Navigre/blob/main/docs/MASTER-EVIDENCE-LEDGER.md) — blob `1d8d04a675105febfd424adaf47e2bfbb064e760`.
- [Gate 2 Pass 5 Policy Simulation](https://github.com/Moshoeshoe333/Mall-Navigre/blob/main/docs/CORE-0.2-GATE-2-PASS-5-POLICY-SIMULATION.md) — blob `e03849a3711ccda8d0159f9b7f2f11c77df20df6`.
- [Spatial Seam 4 merge commit](https://github.com/Moshoeshoe333/Mall-Navigre/commit/161afcaa2ad85335649dd1040b414078f7a4636a).

### Source-backed findings

1. The master ledger defines a seven-level evidence scale L0–L6 and explicitly says a test artifact is not execution evidence, workflow configuration is not execution evidence, and PR-head evidence does not automatically transfer to a squash-merge SHA.
2. It records historical L5 evidence for a specific PR head and withholds promotion to the then-current merge SHA because merge-boundary execution telemetry had not been observed at that audit time.
3. It explicitly lists capability gaps: GPS/BLE/Wi-Fi are interfaces/abstractions rather than operational indoor positioning; physical sensors are not deployed; accessibility, performance/battery, security/privacy, multi-mall runtime and real Mall of Africa validation remain gaps in that recorded ledger.
4. Gate 3 concurrency was frozen at L1 in the recorded evidence ledger.
5. Pass 5 policy simulation identifies a semantic distinction between stored observation confidence and freshness. It recommends evaluating freshness independently rather than silently rewriting stored confidence based on age.
6. Pass 5 is explicitly an analytical policy simulation, not L4 execution evidence or production authorization.
7. The Spatial Seam 4 commit adds a routing-start authorization boundary requiring fresh localization, node identity and current graph validation. The authorization result deliberately does not claim a route exists or is verified. Its commit message says exact-head CI and Parking Truth verification preceded the squash merge, but the inspected commit evidence document also requires independent inspection of the merge SHA.

### Transferable lessons

- Keep confidence and freshness as separate concepts when they answer different questions.
- A high confidence score cannot substitute for authorization, route existence or route verification.
- Authorization boundaries should be narrow and return explicit reasons; one boundary must not claim downstream outcomes.
- Stale, conflicting, unresolved, missing or graph-inconsistent localization should fail closed.
- Do not transfer PR-head test evidence automatically to a merge commit or later HEAD.
- Preserve explicit operational capability gaps instead of presenting interfaces as deployed sensors or validated positioning.

### Important non-claims

The 2026-09-14 master ledger is a historical evidence snapshot, not a complete current audit of every later change. This audit did not rerun NAVIGRE CI or browser truth tests against the inspected current mainline commit. Gate 3 remains recorded frozen; no physical mall-positioning or production-readiness claim is made.

## 5. Cross-project controls promoted by this audit

1. **Exact-boundary evidence:** every test/run result belongs to a repository, branch, commit, environment and test scope.
2. **Read-back verification:** after a repository write, fetch the exact path from the intended branch and inspect the resulting diff.
3. **Authority separation:** observations, analysis, recommendations, CI results and ratified decisions are different objects.
4. **Minimal change:** fix the earliest demonstrated failure boundary; do not use a narrow defect as an excuse for broad refactoring.
5. **No inherited green:** prior PR-head or historical run success does not certify a later commit.
6. **Explicit unknowns:** a missing workflow/status result is not automatically a failure or a pass.
7. **Product maturity honesty:** a serious engineering process does not establish a finished product, adoption or commercial validation.
8. **Context-bound transfer:** transfer a principle only after stating how the destination project's constraints change its implementation.

## 6. Next audit queue

- ScoutSA: inspect the mainline and isolated prototype branch separately; retrieve the exact current README, workflow definitions, documentation tests and latest hosted run details. Do not alter implementation gates.
- SoulSync 3: inspect the current test/CI contract and resolve the historical 99-contract / 003B run references against exact source commits.
- SoulSyncMobile: inspect the ledger's full evidence chronology and G-BOOT harness; identify the smallest physical Android runtime evidence step without changing the app architecture.
- NAVIGRE: reconcile the latest merge commit with the master ledger and exact merge-boundary telemetry; preserve Gate 3 freeze.
- UCI: no source repository was identified in this account listing; retain it as a research programme until its repository/source of truth is identified.
