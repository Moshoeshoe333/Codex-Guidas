# Cross-Project Knowledge Crosswalk

**As-of:** 2026-11-18  
**Status:** Historical synthesis from prior project discussions and selected recorded identifiers. Not a fresh audit of every repository.

## ScoutSA
**Purpose:** South African grassroots football opportunity network; initial focus on Vaal Triangle / Sedibeng, with a path toward Gauteng and national reach.

**Transferable lessons:** Documentation growth is not implementation progress; prove one observable workflow before expanding architecture; distinguish exposure, visibility, discoverability, trust, verification, contact and placement; use stable identifiers for tournament/team/player/coach relationships; keep under-18 safeguarding and opportunity provenance as release gates; synthetic data does not validate demand.

**Recorded evidence leads:** Canonical status document docs/00-gate-status.md. Gate 1 was recorded closed; Gate 2 conceptual ERD-ready but not closed. RLS/API/UI/schema implementation was deferred pending decision package, MVP boundary freeze and ERD. PostgreSQL 17 CI runtime witness existed but is not a complete product. Case SCOUTSA-026; commit prefix 05f59fe5...; validation pack prefix 750c812.... Pilot design commit recorded as 92b5457ad5d9cef75bb56b5e89db27bd20759c11.

**Next proof:** Tournament organiser vertical slice using synthetic data, correction flows and permission tests; then supervised adult usability sessions.

## SoulSync 3
**Purpose:** Deterministic intelligence/security core with explicit contracts, evidence verification and governed state transitions.

**Transferable lessons:** Contract boundaries and immutability need mutation/adversarial tests; test counts require exact commit, command and environment; do not weaken tests to obtain green CI; separate frozen contract state from runtime coverage and release claims.

**Recorded evidence leads:** Commit ddcd7904... associated with deep immutability and Run #29 reported 64 tests passing; Run #25 also reported 64/64. A 99-contract freeze and a separate 003B Run #68 with 125 tests were discussed; relationship to ratification needs source verification.

**Next proof:** Inspect current branch, freeze/ratification authority, tests and supported runtime matrix before expansion.

## SoulSyncMobile
**Purpose:** Offline SMS/URL threat-scanning mobile application.

**Transferable lessons:** Offline-first creates persistence, retry, clock and recovery concerns; ALLOW/WARN/DENY needs precise semantics; build, install and runtime correctness are separate gates; local persistence is not automatically secure storage.

**Recorded evidence leads:** Expo / React Native / TypeScript design; AsyncStorage local ledger discussed. G-BOOT remained open; no APK was verified, and an EAS Gradle build error was reported.

**Next proof:** Reproducible build, target-device installation, offline/adversarial tests and persistence/privacy review.

## NAVIGRE
**Purpose:** Smart indoor mall navigation and parking locator concepts.

**Transferable lessons:** Location estimates need uncertainty and freshness; scores must expose inputs and thresholds; confidence decay is a model assumption to validate; defer broad platform expansion until a narrow user task is proven.

**Recorded evidence leads:** NAVIGRE 2 parking locator Core 0.1; Gate 2 design recorded GPS confidence parameter 0.5/block and 24-hour half-life; Sieve score 37/99 and Gate 3 frozen.

**Next proof:** Verify current source artifacts, then test confidence and parking discovery against observed real-world conditions.

## UCI
**Purpose:** Cyber threat intelligence research and potential dashboard for global cyber attacks.

**Transferable lessons:** Separate reported events, confirmed incidents, attribution and analysis; preserve source URLs, observation times, confidence and corroboration; do not treat single-source social posts as verified intelligence; research should inform decisions, not automatically trigger infrastructure expansion.

**Next proof:** Define a narrow intelligence question, reliable source set, deduplication rules and analyst workflow before implementation.

## Cross-project rule
Transfer principles, not assumptions. A pattern safe in one project may be inappropriate in another. Every adoption must state context, constraints, evidence and required adaptation.

---

## Source-audit reconciliation — 2026-11-18

This section supersedes any older summary where the inspected source files provide a more precise boundary. It is still a partial audit, not a fresh test execution.

### ScoutSA — source-confirmed current boundary

- Canonical source: [docs/00-gate-status.md](https://github.com/Moshoeshoe333/ScoutSA/blob/main/docs/00-gate-status.md), blob `c79cde2979ad44f2a5811f20cf573cdc428a6013`.
- Gate 1 closed; Gate 2 closed at conceptual level; ERD/MVP/schema/physical-table boundaries frozen or ratified at their stated levels.
- SQL remains draft/reviewed. PostgreSQL 17.11 isolated non-production witness recorded 26 tables and 17 foreign keys.
- Migration/database, RLS, API, UI and production implementation remain HOLD / unauthorized; access-policy ratification remains required.
- Controlled next move: external validation, not further speculative architecture and not implementation.
- [Engineering integrity policy](https://github.com/Moshoeshoe333/ScoutSA/blob/main/docs/engineering-integrity.md) records DOC-001 to DOC-004 and CI-001, including wrong-branch writes, fragile generated tests, stale README/gate summaries and zero-byte workflow files. It requires explicit branch writes, read-back, diff inspection and branch-specific controls.
- The pilot design remains strategy/research only; no live pilot or public listing is authorized.

### SoulSync 3 — source-confirmed methodology and tests

- [33-Tier Framework](https://github.com/Moshoeshoe333/soulsync-3/blob/main/docs/33-tier-framework.md), blob `bf3badc8a30a44779354302b66787da0c28eff05`, defines Point → Knowing → Witness → Gate.
- The same document expressly says detailed definitions and validation of all 33 tiers remain incomplete. Do not call it a fully specified standard.
- [Coordinate test file](https://github.com/Moshoeshoe333/soulsync-3/blob/main/tests/test_coordinate99.py), blob `ebd57d9a644b0998ad09531e2d1e1a817a2811dc`, includes nested mutation rejection and source-detachment tests. The source audit did not rerun them.
- The recent framework documentation commit is `e7771d4b087ce9ff66ceb45b0cf86114e9241cb7`; the deep immutability test commit is `ddcd79046248c8ee4b04238b0489b92199de21fd`.

### SoulSyncMobile — three-repository evidence boundary

- Application: [SOULSYNCMOBILE](https://github.com/Moshoeshoe333/SOULSYNCMOBILE). README says OPEN / evidence pending; G0–G8 gates remain relevant. AsyncStorage is described as bootstrap storage; SQLite remains a production gate.
- Forensic ledger: [SOULSYNCMOBILE-ledger](https://github.com/Moshoeshoe333/SOULSYNCMOBILE-ledger). E-007 Run #72 is historical CI/Semantic/fixture evidence for its exact older baseline; G-BOOT mobile runtime was not executed and runtime remains N/A in that record.
- Runtime evidence: [SOULSYNCMOBILE-runtime-evidence](https://github.com/Moshoeshoe333/SOULSYNCMOBILE-runtime-evidence). Keep physical runtime witness artifacts separate from app code and ledger interpretation.
- Current app package declares Expo ~57, React Native 0.86, React 19.2.3 and TypeScript ~5.9.2. These declarations do not prove installed runtime compatibility.
- A recent fixture import correction is commit `b85a83c9f672a11c71b94090826710475d8b6f86`; this is a narrow test-source fix, not a verified APK or runtime pass.
- Do not transfer E-007 evidence to later app commits without exact-boundary verification.

### NAVIGRE / Mall-Navigre — evidence boundary clarified

- Correct repository identity: [Mall-Navigre](https://github.com/Moshoeshoe333/Mall-Navigre).
- [Master Evidence Ledger](https://github.com/Moshoeshoe333/Mall-Navigre/blob/main/docs/MASTER-EVIDENCE-LEDGER.md), blob `1d8d04a675105febfd424adaf47e2bfbb064e760`, defines L0–L6 and prohibits evidence inheritance from PR head to squash merge.
- [Pass 5 policy simulation](https://github.com/Moshoeshoe333/Mall-Navigre/blob/main/docs/CORE-0.2-GATE-2-PASS-5-POLICY-SIMULATION.md), blob `e03849a3711ccda8d0159f9b7f2f11c77df20df6`, recommends stored confidence and freshness remain separate; it is analysis, not production authorization.
- Spatial Seam 4 merge commit: `161afcaa2ad85335649dd1040b414078f7a4636a`. The new boundary authorizes only a current routing start; it does not claim a route exists or is verified. The merge SHA still needs its own execution evidence before claims are promoted.
- Gate 3 concurrency remains recorded frozen; physical Mall of Africa positioning and sensor deployment are not proven.

### UCI

No UCI repository was present in the accessible repository listing during this audit. Keep UCI classified as a research/product concept until its source of truth is identified. Do not fabricate a repository or infer implementation.

For full source references and audit limitations, see [Repository Archaeology — 2026-11-18](../10-source-audits/2026-11-18-repository-archaeology.md).


---

## Source-audit reconciliation — 2026-11-24

This update supersedes the 18 November ScoutSA "controlled next move: external validation" statement. The project-owner decision recorded on 23 November is now stricter: external validation, stakeholder interviews, partnership/funding pitches and active promotion as a pitch asset remain on hold until the internal prototype is working, tested, independently reviewed and explicitly accepted.

### ScoutSA — current prototype boundary

- Repository: [Moshoeshoe333/ScoutSA](https://github.com/Moshoeshoe333/ScoutSA).
- Inspected branch and exact head: `prototype/internal-demo`, `e4a0a5a5c130f4d6e94c70b72a786e196fb3ae27`.
- The branch contains a static synthetic-data prototype. It is separate from mainline and does not authorize real player/minor data, production use, deployment, live pilot activity or mainline implementation.
- The agreed order is **Build → Test → Audit → Accept → Demonstrate → Pitch**. No external validation or pitching before the working prototype has been tested, independently reviewed and explicitly accepted.
- Historical workflow #893 passed at PR #11 head `61993f435f621db32a0e0fc2aefe33d2d569201e`; it is not evidence for the later current branch head. The 24 November audit did not obtain exact-head CI evidence. The available workflow lookup is PR-run-limited; empty results are inconclusive, not a failed run.
- A current source mismatch was observed: the workflow lists 12 browser smoke scripts, while the README describes 11 configured scripts for the historical run. Reconcile the wording and counts at the relevant revision.
- Match-Day Handoff now checks the exact 17-key root envelope and has a committed unknown-envelope regression. Nested schema allowlists, collection bounds, source-origin relationship enforcement and complete post-validation atomicity remain review items. No latest-head browser pass is claimed.
- UI-008 remains OPEN. The recorded 21-page source-pattern scan is bounded evidence, not a full AST/runtime security audit.
- Mainline implementation, real-data, production, deployment, external-validation, stakeholder-outreach and pitching gates remain unchanged.

**Primary audit:** [ScoutSA Prototype and Engagement Audit — 2026-11-24](../10-source-audits/2026-11-24-scoutsa-prototype-audit.md).  
**Transferable doctrine:** [Prototype-First Integrity and External Engagement](../doctrines/prototype-first-integrity.md).

Transfer principles, not ScoutSA's project-specific authorization or safeguarding rules. The 18 November status remains historical context only.


### ScoutSA — 24 November nested handoff follow-up

At branch head `d639cdf380530e4a3cb65576db7d055ce36cb1cd`, the Match-Day Handoff importer has been hardened beyond the 17-key root envelope: exact nested field allowlists, bounded collection/text checks, source-origin and exact source-record pairing, duplicate appearance/substitution checks, and a staged import rollback path are committed. The contract and Section 23 of the ScoutSA session ledger record the limits and scope.

Push workflow run #941 (`45354775012`) is pinned to that exact head. At the time this entry was written, policy/documentation checks and Playwright/Chromium installation were complete; the browser smoke step remained in progress. No browser test pass is claimed. UI-008 and all project-level external engagement/mainline/production holds remain unchanged.
