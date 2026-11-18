# Tri-Tier 33 Pilot 01 — SoulSyncMobile Read-only Assessment

**Pilot ID:** CG-TT33-PILOT-001  
**Assessment date:** 2026-11-18  
**Target repository:** `Moshoeshoe333/SOULSYNCMOBILE`  
**Target branch:** `main`  
**Target head observed:** `b85a83c9f672a11c71b94090826710475d8b6f86`  
**Target head date:** 2026-10-02  
**Framework:** CG-TT33 v0.3.0-draft  
**Review type:** Remote source inspection / read-only desk pilot  
**Disposition:** Partial assessment; findings recorded; no gate advanced.

> This is not a security audit, penetration test, runtime/device test, legal opinion, production-readiness assessment or independent validation of the framework. No application files were modified and no commands were executed against the application.

## 1. Pilot question and contract

**Question:** Does a focused application of Tri-Tier 33 identify material, evidence-supported uncertainty or defects across SoulSyncMobile's threat-analysis logic, persistence contract and user-facing decision boundary?

**Decision supported:** Select the smallest useful follow-up verification work. This pilot does not authorize application changes, release, production storage migration or closure of any SoulSync gate.

**Scope:** Fifteen risk-selected tiers, five or six per layer, using source files available through the connected GitHub repository view on `main`.

**Out of scope:** Full repository tree enumeration, local build, test execution, CI rerun, APK installation, Android/iOS device observation, network capture, persistence runtime inspection, user study, threat corpus calibration and external specialist review.

**Stop condition:** Stop the pilot where a source path, run artifact or runtime observation cannot be inspected. Mark the tier OPEN or Not assessed; do not infer success or absence.

## 2. Repository state and evidence register

The most recent commit returned by the repository commit listing was `b85a83c9f672a11c71b94090826710475d8b6f86`, dated 2026-10-02. The latest commit message concerns a TypeScript test fixture import. The repository is private and the default branch is `main`.

| Evidence ID | Artifact | Exact reference | What it supports |
|---|---|---|---|
| E-01 | README | [README at inspected blob](https://github.com/Moshoeshoe333/SOULSYNCMOBILE/blob/main/README.md) · blob `e9b82c85147cfbaa4f3c942a4968c022dbbd9092` | Declared architecture, gates, AsyncStorage bootstrap statement, current OPEN/evidence-pending declaration |
| E-02 | package.json | [package.json](https://github.com/Moshoeshoe333/SOULSYNCMOBILE/blob/main/package.json) · blob `e1ba351318e517c326a8135f3fa01c4d461cc8b1` | Declared scripts and dependency ranges |
| E-03 | threat heuristics | [heuristics.ts](https://github.com/Moshoeshoe333/SOULSYNCMOBILE/blob/main/src/services/threat/heuristics.ts) · blob `d108f896cb04c5e65f743269a8f1b669e7065d53` | Normalization, URL parsing, indicator scoring, risk/action mapping |
| E-04 | type contracts | [types/index.ts](https://github.com/Moshoeshoe333/SOULSYNCMOBILE/blob/main/src/types/index.ts) · blob `204074d2ff8198c1e7036133f53d0a709062b0cf` | ScanInput, ThreatResult and IncidentLog declared fields |
| E-05 | threat fixtures | [fixtures.ts](https://github.com/Moshoeshoe333/SOULSYNCMOBILE/blob/main/src/services/threat/__tests__/fixtures.ts) · blob `d4ec0796324431838b4e11d6afec222eff58d7f5` | Thirteen declared threat fixtures and expected outputs |
| E-06 | fixture test runner | [threat-fixtures.test.ts](https://github.com/Moshoeshoe333/SOULSYNCMOBILE/blob/main/src/services/threat/__tests__/threat-fixtures.test.ts) · blob `d94ff883dc570c71780b68743aab37229f9ab01f` | Assertions performed by the fixture test |
| E-07 | CI workflow | [typecheck.yml](https://github.com/Moshoeshoe333/SOULSYNCMOBILE/blob/main/.github/workflows/typecheck.yml) · blob `61c2aa7cc37799bf974fa2dbd336a120b4078003` | Workflow definition: Node 22.13.x, npm install, typecheck and threat fixture script |
| E-08 | latest listed commit | [commit b85a83c](https://github.com/Moshoeshoe333/SOULSYNCMOBILE/commit/b85a83c9f672a11c71b94090826710475d8b6f86) | Repository revision/date boundary for this inspection |

**Evidence limitations**
- The combined status endpoint returned an empty status list for E-08. This is not proof that no CI run exists; it means this inspection did not obtain a passing run record.
- The test command is declared in package.json and CI workflow, but this pilot did not execute it. No test pass is claimed.
- Root candidates `package-lock.json`, `npm-shrinkwrap.json`, `yarn.lock` and `pnpm-lock.yaml` were not found by exact-path inspection. The repository tree was not exhaustively enumerated; do not turn this into a universal claim that no lockfile exists.
- Targeted candidate paths for persistence adapter and UI source were not resolved by the repository file fetch. This does not establish that those components are absent. Persistence and UI tiers therefore remain OPEN pending exact source references.
- README statements are declarations, not runtime witnesses.

## 3. Fifteen-tier assessment

Verdicts are bounded to the evidence above. SOLID is not awarded merely because a file exists.

| Tier | Assessment | Verdict | Basis |
|---|---|---|---|
| C-14 Observed vs derived typing | Types expose source, risk, confidence, indicators and action, but no explicit evidence/provenance class for an indicator or decision. | SOFT | E-03, E-04 |
| C-15 Severity and decision separation | Severity/risk/action are separate fields, but `actionForRisk` maps `critical → DENY`, `safe → ALLOW`, otherwise WARN. The meaning of ALLOW is not separately contracted. | SOFT | E-03, E-04 |
| C-17 Failure containment | URL parse failure is caught and skipped. A malformed URL can therefore contribute no URL indicator; remaining score can still resolve to safe/ALLOW. Caller-level containment was not inspected. | OPEN | E-03, E-05; see F-01 |
| C-23 Rule-to-fixture traceability | Thirteen fixtures cover several hand-authored cases; runner asserts severity, risk and action, not confidence, indicator set or harmonyDelta. | SOFT | E-05, E-06 |
| C-25 CI workflow truth | Workflow definition exists, but no current passing run/status evidence was returned for inspected head. | OPEN | E-07, E-08 |
| C-29 Dependency exposure / reproducibility | Dependency versions include ranges; workflow uses `npm install`. Common root lockfile candidates were not found. Actual resolved dependency tree and build reproducibility were not verified. | OPEN | E-02, E-07 |
| D-02 Schema and runtime guards | AsyncStorage adapter is declared in README; exact adapter and record validation implementation were not inspected. | OPEN | E-01; source gap |
| D-05 Transaction and atomicity contract | No inspected persistence implementation establishes atomic write semantics or recovery contract. | OPEN | E-01; source gap |
| D-10 Offline and sync semantics | README declares offline-first intent; no inspected persistence/queue/restart implementation establishes offline guarantees. | OPEN | E-01; source gap |
| D-13 Write validation | No inspected storage write boundary or authorization/validation path. | OPEN | source gap |
| D-19 Concurrency and conflict discipline | No inspected retry, concurrent-write or conflict-resolution implementation. | OPEN | source gap |
| U-04 Decision-display binding | No screen/component source was inspected to verify binding to canonical result/action values. | OPEN | E-04; UI source gap |
| U-05 State matrix | Loading, empty, error, pending, offline and recovery UI states could not be inspected. | OPEN | UI source gap |
| U-12 Claim-tone discipline | README declares offline-first and fail-closed boundaries, but runtime and caller evidence is unavailable; bounded analyzer behaviour raises a qualification question. | OPEN | E-01, E-03; F-01 |
| U-17 Empty/loading state safety | No UI implementation or device observation was inspected. | OPEN | UI source gap |

**Summary:** 6 code tiers, 5 persistence tiers and 4 UI tiers assessed. No tier is SOLID. Four code tiers are SOFT or OPEN as shown; all persistence and UI tiers remain OPEN because their implementation evidence was not available to this pilot. This is a partial evidence assessment, not a 15/99 score or a Harmony pass.

## 4. Findings ledger

### F-01 — Malformed URL handling can fall through to ALLOW

**Severity:** High-priority verification finding; exploitability and real-world impact not established.  
**Linked tiers:** C-17, U-12; related H-5/H-6 probe candidates.  
**Evidence:** E-03, E-05.

In `classifyUrl`, URL parsing exceptions are caught and the candidate is skipped. The fixture `MALFORMED-001` contains an invalid URL and urgency text; it expects score 14, risk `safe`, action `ALLOW`. If an input consists only of an unparseable URL and no other recognized pattern, the inspected code path appears capable of producing zero indicators, score 0, risk `safe`, action `ALLOW`.

This is in tension with the README's broad declaration of fail-closed analysis. The exact outer caller was not inspected, so the broader system-level claim remains OPEN rather than conclusively disproved.

**Next verification:** Add no code yet. First create a controlled, read-only test matrix for malformed-only URL, unsupported scheme, invalid percent escape, URL with whitespace/Unicode, shortened URL and valid benign text. Trace each input through caller → analyzer → action mapping → persisted event → UI. Record whether the system returns INVALID/UNKNOWN, WARN, DENY or ALLOW and why.

### F-02 — ALLOW semantics are ambiguous

**Severity:** High-priority policy clarification.  
**Linked tiers:** C-15, C-14, U-12; H-2/H-6 probe candidates.  
**Evidence:** E-03, E-04, E-05.

Fixtures explicitly expect `ALLOW` for a shortened URL and raw IP URL, each scoring 14 and classified as `safe`. The source defines `safe` as score below 25 and maps it directly to ALLOW. This may be an intentional low-signal policy, but ALLOW can be read by a person as “safe to trust.” A low heuristic score is not proof of safety.

**Next verification:** Ratify precise semantics for at least: analysis completed, no known indicator, low-confidence/no-signal, suspicious-but-unconfirmed, malformed/unanalysable, warning and deny. Consider separating analysis status, risk classification and recommended action. Do not change the enum until the product owner approves the policy meaning and UI wording.

### F-03 — Confidence score has no inspectable calibration contract

**Severity:** Medium-priority evidence gap.  
**Linked tiers:** C-14, C-23.  
**Evidence:** E-03, E-04, E-06.

The analyzer assigns confidence 70 when no indicators are found and otherwise derives confidence from indicator count, capped at 98. The inspected fixtures do not assert confidenceScore. No calibration dataset, false-positive/false-negative measurement or explanation of what the percentage means was inspected.

**Next verification:** Define whether this value represents confidence in detection, confidence in classification, or something else. Validate it against a labelled, representative corpus before displaying it as a probability or percentage.

### F-04 — Fixture coverage is a regression witness, not detection validation

**Severity:** Medium-priority evidence gap.  
**Linked tiers:** C-23, C-25.  
**Evidence:** E-05, E-06, E-07.

Thirteen hand-authored fixtures exercise expected branches, and the test runner checks selected outputs. These fixtures can protect against regressions in the declared examples. They do not establish sensitivity, specificity, generalization to current scams, or local-language coverage. The runner does not assert all fields of ThreatResult.

**Next verification:** Extend the test design only after policy semantics are agreed. Include benign lookalikes, ambiguous legitimate bank/SARS messages, malformed inputs, multilingual and code-switched examples, adversarial obfuscation, empty/oversized inputs, and expected uncertainty. Use independently labelled examples and preserve source/licensing/privacy provenance.

### F-05 — CI and dependency reproducibility remain unproven

**Severity:** Medium-priority engineering gate.  
**Linked tiers:** C-25, C-29.  
**Evidence:** E-02, E-07, E-08.

A workflow is configured to run typecheck and threat fixtures under Node 22.13.x, but this pilot obtained no status records for the inspected head and did not execute the workflow. The workflow uses `npm install`; common root lockfile candidates were not found by exact-path lookup. Resolved dependency versions and reproducible install evidence are therefore unknown.

**Next verification:** Enumerate the full repository tree and package manager artifacts; establish whether a lockfile exists elsewhere; inspect CI run IDs and logs for the exact commit; then assess clean-install reproducibility. Do not regenerate dependencies during this read-only pilot.

### F-06 — Persistence assurance is not evidenced in this pilot

**Severity:** Gate-blocking unknown, not a confirmed defect.  
**Linked tiers:** D-02, D-05, D-10, D-13, D-19; H-2/H-4/H-5/H-6 candidates.  
**Evidence:** E-01 only.

README describes an AsyncStorage adapter and calls it bootstrap persistence, with SQLite as a production gate. The exact adapter, record schema, write validation, transaction semantics, restart behaviour and retry/conflict handling were not inspected.

**Next verification:** Obtain exact source paths and inspect the adapter, domain repository, serialization contract, tests and migration boundary. Then design non-destructive synthetic-data tests for interrupted write, restart, duplicate submission, corrupted record, concurrent update and revoked/changed authority. No real personal data.

### F-07 — UI truthfulness and state handling are not evidenced in this pilot

**Severity:** Gate-blocking unknown, not a confirmed defect.  
**Linked tiers:** U-04, U-05, U-12, U-17; H-1/H-2/H-5/H-6 candidates.  
**Evidence:** E-01, E-04 only.

The README declares Expo React Native and React Navigation. No UI component/screen source or device observation was available to this assessment. It is unknown whether the interface distinguishes no indicators from safe, malformed/unanalysable input from benign input, pending storage from committed storage, or warning from denial.

**Next verification:** Obtain exact screen/component paths and map each ThreatResult field to rendered copy, colour, icon, accessibility label and action. Then exercise empty, loading, malformed, warning, deny, persistence failure, restart and offline states on a supported device.

## 5. Harmony status

No end-to-end Harmony probe was executed. The following are candidate probes, not failed or passed tests:

| Invariant | Pilot status | Why |
|---|---|---|
| H-1 One Vocabulary | OPEN | Meaning of safe / ALLOW / confidence needs a shared contract across code, persistence and UI |
| H-2 Same Evidence Basis | NOT RUN | No end-to-end input → decision → stored record → rendered explanation trace |
| H-3 Version Coherence | OPEN | No inspected persistence schema/version compatibility evidence |
| H-4 Atomic Logical Action | NOT RUN | No write/acknowledgement boundary inspected |
| H-5 Truth Through Interruption | NOT RUN | No restart/offline/device witness |
| H-6 Authority Does Not Escalate | NOT RUN | No UI/API/store authorization path inspected |
| H-7 Traceable Disagreement | NOT RUN | No integrated finding-to-ledger witness run |

Do not compute a Harmony index from this desk review. A source-inspection note is not a Harmony probe execution.

## 6. Recommended next actions — still read-only first

1. Obtain a complete repository tree and exact paths for persistence, guardian state, navigation and screens.
2. Inspect the actual call chain from input source through `analyzeThreat` to action, persistence and UI.
3. Confirm the intended meaning of ALLOW, safe, confidenceScore and fail-closed.
4. Inspect package manager lockfile state and exact-commit CI run evidence.
5. Design synthetic-only Harmony probes for malformed input, persistence failure and restart.
6. Only after evidence and policy review, prepare a separate proposed remediation package for owner ratification.

**No application fix is authorized or included in this pilot.** A finding is not permission to change code. Any proposed remediation must be separately reviewed, approved and tested.

## 7. Framework learning

This pilot demonstrates why Tri-Tier 33 must:
- allow partial assessments without fabricating a system-wide score;
- preserve source declarations separately from implementation evidence;
- make missing source paths visible as OPEN rather than assume absent controls;
- distinguish a regression fixture pass from empirical detection effectiveness;
- expose cross-layer meaning problems such as `safe` → `ALLOW` before UI copy is trusted;
- require exact commit and run provenance;
- treat non-execution as an explicit limitation, not as an implied pass.

**Pilot conclusion:** Tri-Tier 33 identified one concrete code-path concern, several policy/measurement questions and substantial persistence/UI evidence gaps. It has demonstrated practical diagnostic value in this narrow desk pilot, but its overall effectiveness and defect-detection rate remain unvalidated.
