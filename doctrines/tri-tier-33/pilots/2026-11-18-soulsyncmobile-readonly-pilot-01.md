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
| E-09 | storage adapter | [storageManager.ts](https://github.com/Moshoeshoe333/SOULSYNCMOBILE/blob/main/src/storage/storageManager.ts) · blob `17859deeb96a9fb87353151014ca3982e5668c62` | AsyncStorage read/write, JSON parsing, Harmony normalization, clear operation |
| E-10 | Guardian state hook | [useGuardianState.ts](https://github.com/Moshoeshoe333/SOULSYNCMOBILE/blob/main/src/hooks/useGuardianState.ts) · blob `db52b38fd4c9f8909f33df78c8e2752e18993fe2` | Hydration error handling, serialized operation queue, two-step persistence, snapshot publication |
| E-11 | dashboard | [App.tsx](https://github.com/Moshoeshoe333/SOULSYNCMOBILE/blob/main/App.tsx) · blob `17b1b37df4f93547c099129cff883571c5e9b1d5` | Loading/ready control, action display, asynchronous scan handler and error presentation |

**Evidence limitations**
- The combined status endpoint returned an empty status list for E-08. This is not proof that no CI run exists; it means this inspection did not obtain a passing run record for the inspected head.
- The test command is declared in package.json and CI workflow, but this pilot did not execute it. No test pass is claimed.
- Root candidates `package-lock.json`, `npm-shrinkwrap.json`, `yarn.lock` and `pnpm-lock.yaml` were not found by exact-path inspection. The repository tree was not exhaustively enumerated; do not turn this into a universal claim that no lockfile exists.
- Persistence and UI source are now inspected at E-09 through E-11. Runtime/device behaviour remains unwitnessed.
- README statements are declarations, not runtime witnesses.

## 3. Fifteen-tier assessment

Verdicts are bounded to the evidence above. SOLID is not awarded merely because a file exists.

| Tier | Assessment | Verdict | Basis |
|---|---|---|---|
| C-14 Observed vs derived typing | Types expose source, risk, confidence, indicators and action, but no explicit evidence/provenance class for an indicator or decision. | SOFT | E-03, E-04 |
| C-15 Severity and decision separation | Severity/risk/action are separate fields, but `actionForRisk` maps `critical → DENY`, `safe → ALLOW`, otherwise WARN. The meaning of ALLOW is not separately contracted. | SOFT | E-03, E-04 |
| C-17 Failure containment | URL parse failure is caught and skipped. For the inspected malformed-only input shape, the analyzer can return safe/ALLOW rather than an explicit unanalysable state. | SOFT | E-03, E-05; see F-01 |
| C-23 Rule-to-fixture traceability | Thirteen fixtures cover several hand-authored cases; runner asserts severity, risk and action, not confidence, indicator set or harmonyDelta. | SOFT | E-05, E-06 |
| C-25 CI workflow truth | Workflow definition exists, but no current passing run/status evidence was returned for inspected head. | OPEN | E-07, E-08 |
| C-29 Dependency exposure / reproducibility | Dependency versions include ranges; workflow uses `npm install`. Common root lockfile candidates were not found. Actual resolved dependency tree and build reproducibility were not verified. | OPEN | E-02, E-07 |
| D-02 Schema and runtime guards | Generic JSON parsing is cast to `IncidentLog[]` without validating record shape, required fields or nested ThreatResult values. | SOFT | E-09; see F-06 |
| D-05 Transaction and atomicity contract | Incident logs and Harmony state are written through two sequential AsyncStorage calls. No transaction/rollback spans the logical scan record. | SOFT | E-09, E-10; see F-08 |
| D-10 Offline and sync semantics | The implementation is local-first by declaration and uses AsyncStorage, but no network-disabled or device/restart witness was run. | OPEN | E-01, E-09; see F-06 |
| D-13 Write validation | Save methods accept typed values but perform no runtime validation before JSON serialization and storage. | SOFT | E-09; see F-06 |
| D-19 Concurrency and conflict discipline | The hook serializes its own operations through a promise queue; this does not establish cross-instance/process locking or conflict handling for other direct storage callers. | SOFT | E-09, E-10; see F-08 |
| U-04 Decision-display binding | Dashboard displays action, risk, severity, confidence, harmony delta and indicators from the returned result. The semantic caveat for ALLOW/no indicators is not displayed. | SOFT | E-03, E-11; see F-02, F-07 |
| U-05 State matrix | Dashboard has a loading/ready state and latest-result state, but no explicit storage error, save-pending, save-failed or recovery state. | SOFT | E-10, E-11; see F-07, F-08 |
| U-12 Claim-tone discipline | Dashboard labels the value `Confidence: n/100`; no calibration or explanation accompanies it. The UI displays action without explaining that ALLOW is heuristic non-detection, not proof of safety. | SOFT | E-03, E-11; see F-02, F-03 |
| U-17 Empty/loading state safety | The button is disabled while `ready` is false, but hydration failure sets `ready` true with empty defaults. The UI can therefore present an empty ledger as ready after a storage read failure. | SOFT | E-10, E-11; see F-07 |

**Summary:** 6 code tiers, 5 persistence tiers and 4 UI tiers assessed. No tier is SOLID. After the second source pass, 12 tiers are SOFT and 3 remain OPEN (C-25, C-29 and D-10). SOFT means a source-level weakness or bounded assurance gap was observed; it does not mean dynamic failure was reproduced. This is not a 15/99 score or a Harmony pass.

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

### F-06 — Persistence validation and offline assurance are incomplete

**Severity:** Material integrity assurance gap; source-level weaknesses confirmed, runtime consequences not tested.  
**Linked tiers:** D-02, D-10, D-13; H-2/H-5 candidates.  
**Evidence:** E-09, E-10.

The adapter parses incident JSON and casts it to `IncidentLog[]` without validating record shape, required fields or nested result values. Parse failure returns an empty fallback; storage read failures propagate to the hook. Save methods serialize typed values but do not validate runtime shape. The implementation uses local storage, but no network-disabled or device/restart witness was run.

**Next verification:** Test malformed JSON, valid JSON with invalid shape, storage read/write rejection, legacy data and restart using synthetic records. Establish a versioned validation and recovery contract before expanding the ledger. Keep device/offline behaviour OPEN until witnessed.

### F-07 — Hydration failure is presented as a ready empty ledger

**Severity:** High-priority reliability and user-trust defect candidate; source path confirmed, runtime reproduction not performed.  
**Linked tiers:** U-04, U-05, U-17; D-10; H-2/H-5 candidates.  
**Evidence:** E-10, E-11.

The hook catches any error while loading Harmony state and incident logs, resets the in-memory snapshot to unmeasured/empty, and sets `ready` to true. The dashboard uses `ready` to enable analysis and displays the incident count without a storage-health/error indicator. A storage read failure can therefore be represented to the user as an ordinary empty ledger.

**Next verification:** With a synthetic storage adapter that rejects `getItem`, verify the UI state. Distinguish “loaded and empty” from “could not load”; do not enable normal ledger operations until storage health is known or the user explicitly chooses a degraded mode.

### F-08 — A scan's logical record is persisted through two non-atomic writes

**Severity:** High-priority integrity defect candidate; partial-write failure not dynamically reproduced.  
**Linked tiers:** D-05, D-19, U-05; H-4/H-5/H-7 candidates.  
**Evidence:** E-09, E-10, E-11.

The hook writes the updated incident list first and the updated Harmony state second. Each operation is awaited, but there is no transaction spanning both keys. If the first write succeeds and the second fails, the durable incident list can advance while the Harmony state remains stale. The hook updates its in-memory snapshot only after both writes, and the dashboard awaits the promise without a local catch or visible save-failure state.

**Next verification:** Use a synthetic adapter that succeeds on incident write and fails on Harmony write. Verify persisted state, retry behaviour, displayed result and recovery after restart. Decide whether Harmony is derived and rebuildable from the incident ledger, whether a single atomic record is required, or whether an outbox/commit protocol is justified. Do not choose a design before the product's consistency contract is ratified.

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

1. Obtain complete repository-tree and package-manager artifact evidence; establish exact-commit CI run evidence.
2. Ratify the meaning of ALLOW, safe, confidenceScore and fail-closed before changing policy or UI copy.
3. Design synthetic-only fault-injection tests for storage hydration failure and partial two-key persistence.
4. Define the logical commit point for a scan: which durable record is authoritative, what can be rebuilt, and how retries avoid duplication.
5. Test malformed JSON and structurally invalid records; distinguish an empty ledger from an unavailable/corrupt ledger.
6. Only after evidence and policy review, prepare a separate proposed remediation package for owner ratification.

**No application fix is authorized or included in this pilot.** A finding is not permission to change code. Any proposed remediation must be separately reviewed, approved and tested.

## 7. Framework learning

This pilot demonstrates why Tri-Tier 33 must:
- allow partial assessments without fabricating a system-wide score;
- preserve source declarations separately from implementation evidence;
- distinguish a missing source path from a source-inspected weakness;
- distinguish a regression fixture pass from empirical detection effectiveness;
- expose cross-layer meaning problems such as `safe` → `ALLOW` before UI copy is trusted;
- distinguish an empty store from an unavailable store;
- inspect logical operations spanning multiple persistence writes, not only each storage call individually;
- require exact commit and run provenance;
- treat non-execution as an explicit limitation, not as an implied pass.

**Pilot conclusion:** The second source pass strengthened the pilot: it identified a malformed-input decision concern, a misleading storage-hydration fallback, a non-atomic multi-key logical write, unvalidated persisted record shapes, and missing UI failure states. These are source-supported findings; no fault injection, runtime test or device witness was performed. The framework has demonstrated practical diagnostic value in this narrow desk pilot, but its overall effectiveness and defect-detection rate remain unvalidated.
