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

**Immediate next step:** Define the persistence contract and execute controlled, isolated synthetic tests for hydration failure and partial-write failure. Capture actual outcomes before proposing application changes.

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

- **Status:** TEST HARNESS COMMITTED; EXECUTION NOT VERIFIED.
- **Target repository:** `Moshoeshoe333/SOULSYNCMOBILE`.
- **Target commit:** `c7a1b73516a40a3684c833290f5315993d199430`.
- **Base inspected:** `b85a83c9f672a11c71b94090826710475d8b6f86`.
- **Files added:** `test-support/async-storage-mock.mjs`, `test-support/async-storage-mock.d.mts`, `test-support/async-storage-loader.mjs`, `src/storage/__tests__/storageManager.fault-injection.test.ts`.
- **Package change:** Added `npm run test:storage-faults`; application source files were not modified.
- **Verification:** New files and package script were fetched back from GitHub and inspected. A local temporary harness then executed the exact fetched `storageManager.ts` source with the committed mock/test logic under Node `v22.16.0`: **10 tests passed, 0 failed**. This was not a full repository checkout, not GitHub Actions, not the native AsyncStorage implementation, and not a device run. Typecheck remains unverified. The run emitted Node experimental warnings for the loader and type stripping.
- **Test coverage authored:** missing/malformed incident data; invalid incident shape characterization; incident read/write rejection; unmeasured/malformed/invalid Harmony data; Harmony normalization write failure; clear-storage failure.
- **Important characterization:** Source inspection shows `getHarmonyState()` catches a normalization-write rejection in its broad catch and returns UNMEASURED while the invalid bytes remain stored. The test now records this observed behaviour rather than asserting a rejection that the current implementation does not produce.
- **Important limitation:** The harness replaces the AsyncStorage package with an isolated in-memory mock while exercising the actual `storageManager` module. It does not prove native AsyncStorage, device restart, offline behaviour, hook hydration, or the two-write scan transaction. Those remain separate probes.
- **CI boundary:** No workflow dispatch was requested or manually invoked. The existing workflow is configured for pushes to `main`; any automatic push-triggered run must be checked separately and must not be mistaken for execution of the new storage suite, which is not yet included in that workflow.
- **Next gate:** Run `npm run test:storage-faults` and `npm run typecheck` from the exact target checkout/commit in a controlled Node 22 environment; capture raw output. Then separately design a hook-level test for hydration failure and the incident-write/Harmony-write partial-commit case. Do not change app runtime code until the persistence authority/commit contract is explicitly decided.


### Follow-up protocol — SSM-PERSISTENCE-FI-001

- **Status:** TEST DESIGN ONLY; NOT EXECUTED.
- **Protocol:** [Synthetic Persistence Fault-Injection Protocol](../doctrines/tri-tier-33/pilots/2026-11-18-soulsyncmobile-persistence-fault-injection-protocol.md).
- **Priority sequence:** P-01 hydration read failure → P-04 partial two-write failure → P-07 write rejection → P-02 malformed JSON → P-03 invalid record shape.
- **Safety boundary:** Isolated mock storage and synthetic fixtures only. No real SMS/banking data, no production storage, no application behavior changes and no CI dispatch under this protocol.
- **Decision required before execution:** Project-owner approval for test-only changes and ratification of the logical persistence authority/commit model. If that contract is undecided, assertions remain BLOCKED-PENDING-DECISION.
- **Current result:** All five probes remain NOT RUN. This protocol is not evidence of application behaviour.
