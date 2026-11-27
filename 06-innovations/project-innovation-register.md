# Project Innovation and Experiment Register

Ideas and directions are preserved here without confusing them with implemented or validated capabilities.

| Project | Innovation / direction | Recorded status | Next proof |
|---|---|---|---|
| ScoutSA | Tournament organiser workflow linking tournaments, teams, players, coaches, results and statistics through stable IDs | Proposed vertical slice | Build one end-to-end workflow; test corrections and permissions using synthetic data; then adult organiser usability sessions |
| ScoutSA | Player Passport with readiness and visibility controls | Designed / research concept | Validate data ownership, consent, status definitions and access rules |
| ScoutSA | Verified opportunity provenance and safeguarding gates | Requirements and research | Demonstrate publisher verification and abuse-case tests |
| SoulSync 3 | Deterministic policy core, immutable contracts, evidence verification and governed transitions | Implemented/tested in recorded runs, scope-specific | Re-run against current commit and supported runtimes |
| SoulSyncMobile | Offline SMS/URL threat scanning with ALLOW / WARN / DENY | Prototype/design; build gate open in recorded state | Reproducible build, device runtime and adversarial corpus |
| NAVIGRE | Indoor navigation and parking locator with confidence decay and scoring | Design/gate work recorded | Validate location confidence and parking discovery against real-world observations |
| Portfolio | Opportunity Exposure / "luck surface area" field note | External heuristic recorded; not validated or adopted as policy | Use the [Opportunity Exposure Experiment Record](../09-templates/opportunity-exposure-experiment.md) for any bounded local test; measure funnel stages separately and preserve downside, privacy and safety limits |
| UCI | Cyber threat intelligence dashboard and structured attack analysis | Research/product concept | Define reliable sources, deduplication, attribution/confidence and analyst workflow before infrastructure |

## Experiment template
- Experiment ID:
- Hypothesis and why it matters:
- User / risk:
- Smallest experiment:
- Inputs and data provenance:
- Method:
- Success and failure criteria:
- Results:
- Limitations and confounders:
- Decision: continue / change / stop / defer:
- Follow-up owner and date:

## Innovation discipline
An idea is not a feature. A prototype is not a product. A model score is not ground truth. A scanner is not comprehensive protection. A map estimate is not verified position. Preserve these boundaries in demos and marketing.

## Opportunity Exposure experiment tracks (2026-11-24)

These records turn OFN-001 / CG-042 into three distinct, bounded experiments. Registration is not execution or proof of results.

| Experiment | Track | Current status | Next proof |
|---|---|---|---|
| [OEX-2026-001](experiments/opportunity-exposure/OEX-2026-001-career-discoverability.md) | Career discoverability | Two OCJ application emails sent without attachments; two corrected packs prepared; fresh Z83 signature/initials and reasons for leaving still required | Complete Z83s and send corrective PDF follow-ups in the original threads before 27 Nov 2026 |
| [OEX-2026-002](experiments/opportunity-exposure/OEX-2026-002-scoutsa-controlled-demonstration.md) | ScoutSA controlled demonstration | **HOLD**; exact-head workflow #1009 passed at `d989fcd9` (128 Node, 12 Chromium, 25 specialist groups, 4 Firefox + 4 WebKit scripts), but UI-008 / baseline-pinned audit / independent acceptance remain unresolved | Close remaining review and obtain explicit owner acceptance before any external exposure |
| [OEX-2026-003](experiments/opportunity-exposure/OEX-2026-003-sme-security-snapshot.md) | SME security snapshot | Initial desk scan started; several existing offers found; differentiated need not established; no sales or outreach | Compare at least five offers on scope and cost; test whether third-party/operator assurance is a distinct buyer problem |

See the [portfolio index](experiments/opportunity-exposure/README.md). The three records are independent; no aggregate exposure score is used.


The OEX-2026-003 desk scan has identified direct counter-evidence to a novel supplier-assurance proposition: ASi Imperium publicly advertises supplier-specific assessments from R6,500. See the [experiment record](experiments/opportunity-exposure/OEX-2026-003-sme-security-snapshot.md). No distinct gap or buyer demand is established.


## Portfolio technology direction — selective Rust adoption (2026-11-27)

**Classification: PROPOSED PORTFOLIO DIRECTION — NOT AN IMPLEMENTATION, VALIDATION, OR TECHNOLOGY FREEZE.**

The portfolio will not replace Python or TypeScript wholesale. Rust is a selective option for bounded systems components where memory safety, explicit types, concurrency, native portability, or measured performance justify its additional learning, integration, and maintenance costs.

| Project | Proposed Rust role | Existing baseline to preserve | Trigger and proof required | Status |
|---|---|---|---|---|
| SoulSync 3 | First candidate: isolated, read-only Rust parity experiment for the 33-coordinate projection; potentially a shared typed core later | Python reference implementation; existing domain, semantic, serialization, hashing, and authority contracts | Freeze golden fixtures; prove differential parity, typed absence, immutability, provenance preservation, and measured value. Canonical serialization/hash work is excluded until byte-level compatibility is specified. | **PROPOSED / NOT IMPLEMENTED** |
| SoulSyncMobile | Possible native Rust threat-normalization/scoring kernel behind a narrow mobile interface | Expo / React Native / TypeScript UI and orchestration; current persistence and G-BOOT evidence boundary | Demonstrate a real bottleneck or cross-platform reuse benefit; prove fixture parity, fail-closed ALLOW/WARN/DENY behavior, Android/iOS builds, and device/offline/runtime evidence. | **PROPOSED / NOT SELECTED** |
| ScoutSA | Candidate backend/service layer (Axum + SQLx are examples for comparison, not selected dependencies) | Existing domain and safeguarding design, PostgreSQL boundary, TypeScript interface; current implementation holds | Only after external validation and all relevant policy, legal, access, and implementation gates. Compare lifecycle cost, maintainer capacity, RLS/transaction behavior, security reviewability, and operational support. | **DEFERRED / GATES UNCHANGED** |
| NAVIGRE / Mall-Navigre | Optional deterministic graph/routing library if real benchmarks establish a material need | Next.js / TypeScript application, localization boundary, current graph invariants and evidence gates | Prove TypeScript/Rust behavioral parity on identical graph fixtures, preserve R1–R6 and failure semantics, and measure representative end-to-end benefit. | **CONDITIONAL / NOT IMPLEMENTED** |
| Codex-Guidas | No current Rust requirement. A small standalone Rust CLI validator is only a future option if distribution or measured scale justifies it. | Python-based documentation, ledger, evidence, and consistency automation | Identify a concrete limitation in the current tooling; compare maintenance and portability; prove output parity before adoption. | **RETAIN PYTHON** |

### Portfolio-wide adoption controls

- Rust is a candidate tool, not a measure of engineering quality and not a default for every project.
- No project is to be rewritten merely to increase Rust usage.
- Keep the existing language implementation authoritative during any initial parity experiment.
- Do not infer that Rust automatically supplies application security, privacy compliance, authorization, safeguarding, data integrity, or correct business rules.
- Require an explicit contract, threat model where relevant, representative workload, failure tests, differential tests, maintainability assessment, and exact commit-level evidence before adoption.
- Keep experiments isolated and reversible. A benchmark, successful compile, or passing unit test is not alone proof of production suitability.
- Every project retains its own gate, ratification, and release authority. This cross-project note does not transfer authority between repositories.

**Next action:** treat SoulSync-3 as the first Rust learning/parity candidate, limited to a proposal and contract preparation. No Rust implementation or project gate transition is authorized by this register entry.


## GCHQ-derived UCI evidence-pipeline concept (2026-11-27)

**Status: PROPOSED RESEARCH DIRECTION ONLY — no service or collection authorization.**

A possible refinement to UCI's existing threat-intelligence concept is a source-preserving, staged evidence workflow: intake/reference → validation and safe handling → normalization/enrichment → analyst assessment → peer review → publication/correction decision. Keep original source artefacts distinct from derivatives and analyst interpretation, record transformation/version and explicit skipped/unsupported/error states, and apply retention/minimisation controls. Read-only linked-data exploration and representative-subset analytics are optional future techniques only where a concrete use case and fidelity evidence justify them. Never use reduced samples as evidence for incident conclusions or discard rare/high-severity signals.

Next proof: assess this workflow against the already documented UCI threat-intelligence methodology, risk register and Gate 0 service/data boundaries. No infrastructure, collection, scan service, active testing, public release, or customer activity is authorized.
