# Portfolio Repository Inventory

**Snapshot date:** 2026-11-27  
**Scope:** GitHub repositories visible to the connected `Moshoeshoe333` account at the time of inspection.  
**Method:** repository discovery, exact `main` branch HEAD capture, README inspection, and selected canonical-status / technology-decision reads.  
**Status:** Portfolio orientation snapshot — **not** a complete code audit, security audit, release review, or revalidation of every project gate.  
**Capture timing:** branch heads were captured before this inventory was published. The Codex-Guidas row therefore records its pre-publication baseline `f411895dfa05d5097e78b70984f4a071cd900d97`; the inventory itself was published in commit `7fd554580e0ba8fc7e6bff6e46a1be5fe5a97abc`.

> This inventory answers: which repositories exist, what role their visible records describe, what exact `main` revision was inspected, and where status evidence needs refreshing. It does not authorize changes in any receiving repository.

## 1. How to read this inventory

- **Main HEAD** is the exact SHA returned by the repository's `main` branch at the snapshot. It is not a claim that the entire repository was audited.
- **README / status** is the repository's own declared description or status. A README is a source to inspect, not independent evidence that a service, control, product or release is operating.
- **Evidence ceiling** says what was actually inspected here. “README only” means no implementation or runtime claim is made.
- **Re-audit required** means a status source is older than the inspected branch head, a referenced artifact could not be found on `main`, or the repository's role remains unclear.

A project status is current only to the date and revision of its governing source. Do not transfer a test result, gate state, approval or readiness claim to a later commit without an explicit evidence rule.

## 2. Portfolio map

### Codex-Guidas — engineering knowledge and governance

| Repository | Main HEAD at capture | Inspected source | Orientation and evidence ceiling |
|---|---|---|---|
| [Codex-Guidas](https://github.com/Moshoeshoe333/Codex-Guidas) | `f411895dfa05d5097e78b70984f4a071cd900d97` | README, root `AGENTS.md`, Project Operating Guide, onboarding/ADR/task templates, defect records and system | The portfolio's reusable engineering knowledge base and project-operating guide. This snapshot records the repository's own documentation changes; it is not a full audit of every methodology or pack. |

### Primary product, research and institutional repositories

| Repository | Main HEAD | Visible role / status | Status source and evidence ceiling |
|---|---|---|---|
| [ScoutSA](https://github.com/Moshoeshoe333/ScoutSA) | `a8bd8e470f3add27a6ac6f4cbde8f79e4c16dec9` | South African grassroots football opportunity network. README records Gate 1 closed, Gate 2 closed at conceptual level, MVP/schema boundaries frozen, and implementation / RLS / API / UI / pilot held pending external validation and policy/legal decisions. | README and `docs/00-gate-status.md` (blob `c79cde2979ad44f2a5811f20cf573cdc428a6013`). The gate document's current note is dated **2026-11-13**, while `main` was advanced on **2026-11-27**. Treat the recorded holds as the latest located gate statement, not as a fresh 27 November gate revalidation. |
| [soulsync-3](https://github.com/Moshoeshoe333/soulsync-3) | `a539976ca3f39d8388ccf54ea0a1bdee10131b28` | Deterministic intelligence/security core. Python remains the authoritative reference for the bounded Coordinate99 Rust study. | README plus RUST-001–RUST-005 documents. RUST-004 records a bounded, isolated non-production parity prototype; RUST-005 records review/remediation/CI pass. Production integration is **not authorized**. This is a targeted technology/evidence read, not a full SoulSync 3 audit. |
| [SOULSYNCMOBILE](https://github.com/Moshoeshoe333/SOULSYNCMOBILE) | 1f50bd3387c61d51868140ec3776b94150a2d4c6 | Exact-main CI run [45989069198](https://github.com/Moshoeshoe333/SOULSYNCMOBILE/actions/runs/45989069198) passed typecheck plus threat, storage-fault and Guardian-hook fault suites. G-BOOT physical runtime remains OPEN / PAUSED. | [PR #21](https://github.com/Moshoeshoe333/SOULSYNCMOBILE/pull/21) proposes a docs-only README/build-plan update; its PR check failed before job steps/logs were available. Current main has no package-lock and CI uses npm install; audit is report-only. Rust analysis remains proposed/not selected/not implemented; TypeScript / Expo / React Native remain baseline. |
| [Mall-Navigre](https://github.com/Moshoeshoe333/Mall-Navigre) | 44db8dbaabe78f98017a427aaf5ac33a4572690c | Exact current-main CI and browser truth workflows passed on this SHA: runs [45989093853](https://github.com/Moshoeshoe333/Mall-Navigre/actions/runs/45989093853) and [45989093818](https://github.com/Moshoeshoe333/Mall-Navigre/actions/runs/45989093818). | README/master ledger still carry the 2026-09-14 e94e358 point-in-time zero-run note. [PR #19](https://github.com/Moshoeshoe333/Mall-Navigre/pull/19) proposes docs-only reconciliation; its PR checks failed before job steps/logs were available. Geometry, sensors, accessibility, security/privacy, device performance and Gate 3 remain open/frozen. |
| [UCI-Foundation](https://github.com/Moshoeshoe333/UCI-Foundation) | `f3a6a931570e1a050dd6de87a24d3c9bb16dcb02` | South African-rooted cyber-intelligence and resilience initiative at an early institutional/documentation stage. The institutional status register says Gate 0 remains open and no operational service, live platform, incorporation or commercial service is evidenced. | README and `docs/00-institutional-status.md` (blob `f83785e6e644ff7ccd076cd63571176a97819e99`), conclusion dated **2026-11-19**. `main` has a later commit dated **2026-11-27**; inspect whether that change affects institutional status before using the 19 November conclusion as current. |
| [POPIA-COMPLIANCE-APP](https://github.com/Moshoeshoe333/POPIA-COMPLIANCE-APP) | `febd028edada89e488672977c630aeade118379f` | SME-focused POPIA compliance and security-incident-management concept. README describes Phase 0 only and says no production incident processing, legal-decision automation or personal-information collection is implemented. | README only. It links to `docs/phase-status.md`, but that path was not present in the inspected `main` root tree (which contained only `README.md`). Verify whether the status file moved or exists only on another branch; do not rely on the broken link as a current gate record. |
| [Alchemy-Shield](https://github.com/Moshoeshoe333/Alchemy-Shield) | `be564dfb9b1ff44e7c0a6bfc3fc75a18d2296196` | Offline-first digital-resilience platform concept for South African SMEs and consumers. README describes Phase 0 foundation/technical-contract review; modules are not operational and later phases require explicit owner ratification. | README plus [PR #1](https://github.com/Moshoeshoe333/Alchemy-Shield/pull/1), which was verified **open and draft** on 2026-11-27 (head `0a9bf3197341375671025dc5598d8b9c76450d52`). No merge or Phase 1 authorization is implied. |

### Supporting, website and evidence repositories

These repositories have a distinct role from the primary product or institutional repositories. A supporting README does not establish the status of its paired application.

| Repository | Main HEAD | Visible role | Evidence ceiling / re-audit note |
|---|---|---|---|
| [ScoutSA-Website](https://github.com/Moshoeshoe333/ScoutSA-Website) | `58ecf93295b146736c7e3fde2d23f13a9691fb2d` | README describes it as the official ScoutSA website and lists a hosted Lovable URL. | README only; no deployment, security, content, or relationship-to-mainline audit performed. |
| [SOULSYNCMOBILE-ledger](https://github.com/Moshoeshoe333/SOULSYNCMOBILE-ledger) | 36f8f7f0904d7f8053f4f0bbcedd3f31c60d952d | Independent forensic/methodology ledger; intentionally separate from app source. | Its records need to distinguish historical forensic baseline 88afab, current app main 1f50bd3387c61d51868140ec3776b94150a2d4c6, G-BOOT harness 3eae8a53d5c41503201235022f05c21fa45dfdc3, E-007 0de0f9de135b644395b9c5c5f74855dbd43a2111 and APK build head 9ce7b6f32164e5a42dc397971aabba52fe880d76. [PR #3](https://github.com/Moshoeshoe333/SOULSYNCMOBILE-ledger/pull/3) proposes docs-only separation; no CI workflow was found. |
| [SOULSYNCMOBILE-runtime-evidence](https://github.com/Moshoeshoe333/SOULSYNCMOBILE-runtime-evidence) | 3ffb2fbf0ca33c77c67ea06ba9d1ceb25980da0a | Intended runtime-execution evidence, test-log and G-BOOT witness repository. | The inspected main tree contains only README.md; no physical-device runtime artifacts were located. G-BOOT remains OPEN / PAUSED. |
| [soulsync-guardian-eas](https://github.com/Moshoeshoe333/soulsync-guardian-eas) | `a3d2c7121ed0ee54f0bc2da623cc355206052620` | README describes an Expo application with EAS build and Firebase integration. | README only; relationship to the current SOULSYNCMOBILE application and release/runtime status are not established here. |
| [Soulsync-guardian](https://github.com/Moshoeshoe333/Soulsync-guardian) | `f11e217441af2ecb4a8bfe10229c5c66a8d6e6bd` | README contains only the title and a generic “State of the art coding” description. | Purpose, ownership relationship, current role and readiness are **not established** by the inspected source. Owner classification is required before treating it as an active product repository. |

## 3. Rust technology decision map

These are the Rust positions found in the inspected project records as of 2026-11-27. They are deliberately not collapsed into a portfolio-wide “Rust adoption” status.

| Project | Recorded Rust position | Boundary that remains in force |
|---|---|---|
| **SoulSync 3** | **Bounded parity demonstrated / isolated research prototype.** RUST-003 defines a bounded cross-language profile; RUST-004 implements a standalone Coordinate99 prototype; RUST-005 records adversarial/boundary review and CI pass. | Python remains authoritative. Prototype is non-production; no production integration, runtime replacement or authority increase is authorized. No performance advantage is claimed. |
| **ScoutSA** | **Architecture hypothesis / deferred / not selected / not implemented.** A future Rust backend/service is a candidate only after external-validation, safeguarding, access-policy, legal and implementation gates permit it. Axum and SQLx are examples for comparison, not selected dependencies. | TypeScript remains the likely web/application layer; PostgreSQL remains the relational integrity boundary; Python may support research/analytics. No backend, migration, RLS, API or implementation gate is opened by the note. |
| **Mall-Navigre** | **Proposed / conditional / not selected / not implemented.** A small Rust library could be evaluated for deterministic graph/routing only if representative benchmarks reveal a material limitation in the current TypeScript implementation. | Next.js / TypeScript remains baseline. No rewrite, Rust dependency, native module, FFI, optimization claim or production integration is authorized. |
| **SOULSYNCMOBILE** | **Proposed / not selected / not implemented.** A small pure deterministic threat-normalization/scoring kernel is a possible future experiment if measured performance or cross-platform reuse justifies it. | Expo / React Native / TypeScript remains baseline. No Rust crate, native module, FFI, Expo plugin, build dependency, workflow, persistence migration or application behavior change is authorized by the proposal. |
| **UCI-Foundation, POPIA-COMPLIANCE-APP, Alchemy-Shield and supporting repositories** | No project-specific Rust decision was established from the inspected README/status sources in this snapshot. | This is an evidence gap, not proof that Rust has been rejected or approved. Check each project's own decision register before proposing a language change. |

**Portfolio rule:** Rust is a candidate component technology, not a portfolio migration objective. Evaluate each use on its own workload, trust boundary, maintenance capacity, build/release integration, interoperability and measurable advantage. A successful isolated prototype does not authorize another project's implementation.

## 4. Portfolio status sources that need reconciliation

| Priority | Repository / source | Observed inconsistency or age | Required next verification |
|---:|---|---|---|
| 1 | Mall-Navigre — README and master evidence ledger | Exact current main CI and browser workflows pass on 44db8d, but project docs still present the 2026-09-14 e94e358 zero-run note as current. PR #19 checks failed before steps/logs were available. | Diagnose PR workflow-start issue and review reconciliation; prioritize physical geometry, accessibility, security/privacy and device performance. Gate 3 remains frozen. |
| 2 | SOULSYNCMOBILE — README/build plan | Exact-main CI run 45989069198 passes bounded tests on 1f50bd, but status prose doesn't distinguish CI from physical runtime. PR #21 check failed before steps/logs. Audit is report-only; no lockfile is committed. | Diagnose PR CI startup, review PR #21, address dependency reproducibility, keep G-BOOT OPEN / PAUSED pending device proof. |
| 3 | SOULSYNCMOBILE-ledger — README/milestone ledger | Historical forensic baseline 88afab, app main 1f50bd, G-BOOT 3eae8a, E-007 0de0f and APK evidence are separate lineages. | Review PR #3 and keep exact evidence streams separate; G-BOOT stays open until physical Android runtime. |
| 4 | ScoutSA — docs/00-gate-status.md | Latest located executive note is 2026-11-13; current main has a 2026-11-27 documentation commit. | Re-read current branch history and gate/access-policy evidence; don't infer implementation authority from a technology note. |
| 5 | UCI-Foundation — docs/00-institutional-status.md | Status conclusion is dated 2026-11-19; current main has a later 2026-11-27 commit. | Check newer decisions affecting Gate 0, service boundary, risk ownership or status. |
| 6 | POPIA-COMPLIANCE-APP — README status link | README points to docs/phase-status.md, not present in inspected main tree. | Restore canonical status file or correct link; recheck README consistency. |
| 7 | Supporting repositories with minimal README records | ScoutSA-Website, runtime-evidence, soulsync-guardian-eas and Soulsync-guardian were not fully inspected. | Confirm owner, canonical role, pairing, source of truth and current evidence before relying on them. |

## 5. Current source rebaseline

The detailed 2026-11-27 review is in [Mainline Evidence Rebaseline — NAVIGRE and SoulSyncMobile](../10-source-audits/2026-11-27-mall-navigre-soulsyncmobile-rebaseline.md). Three documentation-only PRs remain open and unmerged: [NAVIGRE #19](https://github.com/Moshoeshoe333/Mall-Navigre/pull/19), [SOULSYNCMOBILE #21](https://github.com/Moshoeshoe333/SOULSYNCMOBILE/pull/21), and [SOULSYNCMOBILE-ledger #3](https://github.com/Moshoeshoe333/SOULSYNCMOBILE-ledger/pull/3). Two PR workflow checks failed before job steps were recorded; log endpoints returned BlobNotFound, so cause is unknown. No project gate is advanced.

## 6. Inventory maintenance rules

1. Re-capture exact `main` SHAs before a material portfolio review. Never silently reuse a stale SHA.
2. Record each project's own canonical status document and its as-of date; do not let this inventory become a competing project status register.
3. Keep supporting code, websites, forensic ledgers and runtime-evidence repositories distinct from application source.
4. Record missing links, stale baselines and unknown ownership explicitly. Unknown is not zero, absent or approved.
5. Update the Rust map only when a project's own ADR, decision record, gate or approved implementation evidence changes.
6. Do not promote a proposed or prototype technology to selected/adopted without that project's decision authority and acceptance evidence.
7. This inventory is navigation and freshness control. It does not authorize implementation, change a project gate or certify any repository.
