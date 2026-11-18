# SoulSyncMobile — Synthetic Persistence Fault-Injection Protocol

**Protocol ID:** SSM-PERSISTENCE-FI-001  
**Prepared:** 2026-11-18  
**Target repository:** `Moshoeshoe333/SOULSYNCMOBILE`  
**Target revision for initial planning:** `b85a83c9f672a11c71b94090826710475d8b6f86`  
**Related defect record:** `DI-2026-11-18-SSM-001`  
**Related findings:** F-06, F-07, F-08  
**Related proposed probes:** P-01, P-02, P-03, P-04, P-07  
**Status:** TEST DESIGN ONLY — NOT EXECUTED; acceptance contract requires owner ratification.

> This document defines controlled tests. It does not claim the tests have run, does not modify SoulSyncMobile, and does not authorize application, CI, release or production changes.

## 1. Objective

Determine whether SoulSyncMobile preserves truthful user-visible state and consistent durable records when local persistence is unavailable, corrupt, structurally invalid or partially writable.

Use synthetic fixtures and an injected storage adapter. Do not use real SMS, banking messages, credentials, personal records or production storage.

## 2. Preconditions and safety

Before execution:

1. Obtain explicit project-owner authorization for test-only changes in the target repository.
2. Confirm the exact target commit and inspect the current test runner, package scripts and dependency lock state.
3. Run in an isolated test process with a fresh in-memory/mock storage adapter. Do not point tests at a developer's real AsyncStorage, emulator profile or production account.
4. Ensure each test resets adapter state and does not share state with another test.
5. Capture tool versions, command, environment, exact commit, test output and date.
6. Keep tests deterministic: no network, wall-clock dependence, random IDs without fixed seeds, or real user data.
7. Do not dispatch CI or alter application behavior as part of this protocol without separate approval.

If these preconditions cannot be met, stop and record NOT RUN with the reason.

## 3. Contract questions that must be settled

The following are proposed acceptance principles, not yet ratified product requirements:

- A successfully loaded empty incident ledger must be distinguishable from a failed or corrupt read.
- A failed read must not be silently converted into a trusted empty history.
- A scan must not be presented as durably recorded until its defined persistence commit point has succeeded.
- If multiple keys represent one logical operation, the system must define which record is authoritative and how partial writes are recovered.
- Invalid persisted records must not be trusted merely because JSON parsing succeeded.
- Recovery must preserve valid historical evidence; do not silently discard or overwrite records.
- If degraded operation is permitted, the UI must clearly disclose what is unavailable and which actions are disabled.

**Owner decision required:** Is Harmony state authoritative, derived/rebuildable from the incident ledger, or a separately committed record? Do not select an implementation strategy before this is answered.

## 4. Synthetic fixtures

Use stable, minimal values such as:

- Incident A: fixed ID `synthetic-incident-A`, fixed timestamp, valid declared fields, benign synthetic message label.
- Incident B: fixed ID `synthetic-incident-B`, fixed timestamp, valid declared fields.
- Harmony snapshot: fixed synthetic counters/state with a known relationship to the incident fixture set.
- Corrupt payload: literal malformed JSON, e.g. `{"incidents":[`.
- Invalid-shape payload: valid JSON with a missing required ID or invalid nested result shape.

No real phone numbers, names, message bodies, bank names, account details or URLs are needed.

## 5. Probe sequence and expected observations

### P-01 — Storage hydration read rejects

**Injection:** Configure the mock adapter so the incident-history `getItem` rejects with a deterministic synthetic storage error. Keep the Harmony read deterministic.

**Observe:**
- Hook hydration result and readiness state.
- Whether the UI differentiates `loaded-empty` from `load-failed`.
- Whether scan/save controls remain enabled.
- Whether an error/degraded state is visible and actionable.
- Whether the failure is logged without exposing sensitive content.

**Proposed acceptance principle:** The application must not present a failed read as a successfully loaded empty ledger. Product owner must ratify whether normal scans are blocked or a clearly disclosed degraded mode is allowed.

**Capture:** Exact error, state transitions, rendered text/control state, storage calls and any writes attempted after failure.

### P-04 — First logical write succeeds; second write rejects

**Injection:** Let the incident-list write succeed. Make the subsequent Harmony-state write reject. Start from known empty synthetic storage.

**Observe:**
- Exact durable values after rejection.
- In-memory hook snapshot after rejection.
- Whether the UI reports success, failure or pending.
- Whether retry creates duplicate incidents.
- What hydration displays after a simulated restart/re-mount.
- Whether a repair/reconciliation path exists and preserves the incident record.

**Proposed acceptance principle:** The UI must not claim the complete logical scan was committed if the defined commit contract did not complete. The system must have a deterministic recovery/consistency rule; silent disagreement is unacceptable.

**Owner decision required:** Choose and document the authority/commit model before deciding whether a single record, derived state, transaction abstraction or recoverable journal is appropriate.

### P-07 — Storage write rejects

**Injection:** Make the write operation reject before persistence. Repeat with rejection after a prior successful operation if the adapter can distinguish those cases.

**Observe:**
- Whether the user sees a clear save failure.
- Whether an uncommitted result is labelled as saved.
- Whether retry is available and idempotent.
- Whether the in-memory display falsely advances.
- Whether prior durable history remains intact.

**Proposed acceptance principle:** A failed write must not be represented as a successful durable save. Retry behaviour must not duplicate the logical incident.

### P-02 — Malformed JSON on read

**Injection:** Seed the mock store with malformed JSON.

**Observe:**
- Whether parsing failure is surfaced as corruption/unavailable.
- Whether an empty fallback is returned and then treated as valid.
- Whether subsequent save overwrites the corrupt payload.
- Whether the user/operator has a documented recovery route.

**Proposed acceptance principle:** Corrupt data must be distinguishable from an empty ledger. No automatic destructive replacement without an explicit recovery policy.

### P-03 — Valid JSON, invalid record shape

**Injection:** Seed syntactically valid JSON containing an incident with a missing required field or invalid nested result.

**Observe:**
- Runtime schema validation result.
- Whether invalid records are rejected, quarantined or accepted.
- Whether valid neighboring records remain recoverable.
- Whether error output avoids echoing sensitive payloads.

**Proposed acceptance principle:** Parsed JSON is untrusted input. Runtime validation must precede use as a typed incident record. Quarantine/recovery semantics require owner approval.

## 6. Cross-probe regression checks

After the primary injection tests, verify:

- A normal successful read of an empty store is still recognized as loaded-empty.
- A normal successful scan persists the expected record and state.
- A failed write does not erase or mutate previously committed history.
- Repeating a retry with the same logical operation does not create duplicates, if idempotent retry is part of the ratified contract.
- Remount/restart does not transform failed/corrupt storage into an apparently healthy empty store.
- No test relies on real network access or live user data.

Do not weaken assertions to obtain a green test run. If a contract is undecided, mark the assertion BLOCKED-PENDING-DECISION rather than guessing.

## 7. Result record template

For each probe, append:

| Field | Value |
|---|---|
| Probe ID | |
| Target repository / branch / exact commit | |
| Test file and test name | |
| Environment / runtime / package versions | |
| Synthetic fixture identifier | |
| Injected fault | |
| Ratified expected contract / decision reference | |
| Actual result | |
| Pass / fail / blocked / not run | |
| Logs / run URL / artifact reference | |
| Date and observer | |
| Regression result | |
| Uncovered scope / residual risk | |

A test is **REPRODUCED** only when the injected condition and failure are observed in the target implementation. A test is **VERIFIED** only when the corrected target commit passes the reproduction and relevant regression checks, and the preventive control itself is exercised.

## 8. Stop conditions

Stop and seek owner decision if:
- the test would touch real user data or non-isolated storage;
- the current repository revision differs materially from the planning revision;
- the intended commit/authority model is unclear;
- the test requires changing application behavior or dispatching CI without authorization;
- the observed result risks destructive data mutation;
- a test failure cannot be distinguished from a test harness defect.

## 9. Current execution status

| Probe | Status |
|---|---|
| P-01 | NOT RUN — protocol only |
| P-04 | NOT RUN — protocol only |
| P-07 | NOT RUN — protocol only |
| P-02 | NOT RUN — protocol only |
| P-03 | NOT RUN — protocol only |

**Conclusion:** The next valid step is owner-approved, isolated test-only implementation against the exact current SoulSyncMobile revision. This protocol creates no evidence that the application currently passes or fails any of these injections.
