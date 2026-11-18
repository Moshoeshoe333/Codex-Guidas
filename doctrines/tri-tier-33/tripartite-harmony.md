# Tripartite Harmony — Mind · Body · Spirit

**Framework:** CG-TT33 v0.3.0-draft  
**Purpose:** Detect contradictions and unsafe drift between code, persisted records and user-facing behaviour.

Harmony is not an assumption that three layers must contain identical data. Each layer has a different responsibility. The invariant is that their representations and transitions remain semantically consistent, authorized and explainable.

## Seven Harmony Invariants

| ID | Invariant | Refined rule | Principal tier references |
|---|---|---|---|
| H-1 | One Vocabulary | Canonical domain concepts, identifiers and decision classes have governed definitions. Persistence and UI reference those definitions through versioned contracts; localization may vary wording without changing meaning. | C-08/C-10 · D-02/D-15 · U-04/U-08 |
| H-2 | Same Evidence Basis | A material decision shown to a user and persisted for audit must trace to the same decision event, inputs, policy/version and evidence provenance. Fixtures must represent that contract; they need not be byte-identical to production records. | C-18/C-22/C-23 · D-14/D-21 · U-18/U-19/U-25 |
| H-3 | Version and Compatibility Coherence | Each persisted decision identifies its producer and relevant schema/policy versions. Readers either support that version under an explicit compatibility contract or reject/quarantine safely; exact version equality is not always required. | C-06 · D-03/D-15 · U-30 |
| H-4 | Atomic Logical Action | One user-intended logical action has a defined identity and outcome. Required local state changes commit atomically; distributed side effects use explicit pending/outbox/retry states and idempotency. UI must not imply completion before the defined commit/acknowledgement point. | C-09/C-17/C-19 · D-05/D-19 · U-05/U-09/U-20 |
| H-5 | Truth Through Interruption | After crash, restart, offline operation or recovery, the UI reflects the last valid committed state plus any clearly labelled pending, stale or failed work. It must not present an uncommitted action as accepted or silently discard unresolved work. | C-17/C-26 · D-12/D-24/D-32 · U-09/U-10/U-27/U-30 |
| H-6 | Authority Does Not Escalate | UI presentation cannot grant authority; persistence cannot invent a decision class or trusted identity; code cannot exceed the caller's authenticated, delegated and purpose-scoped authority. | C-19/C-20 · D-08/D-13/D-20 · U-12/U-13/U-22/U-28 |
| H-7 | Traceable Disagreement | Every material cross-layer disagreement produces a privacy-safe, attributable finding linked to the relevant artifacts/events. Duplicate observations may be correlated; findings are not silently overwritten or auto-healed. | C-26/C-27 · D-14/D-22 · U-15/U-24 |

## Probe contract

Every probe must state:
- invariant and tier IDs;
- exact scenario and expected semantics;
- source commit/build/configuration;
- synthetic or approved test data;
- steps and observation points in all relevant layers;
- expected result and failure conditions;
- evidence artifact and run identifier;
- limitations and cleanup.

A probe may be static, unit, integration, CI, runtime, device or user-observed. Its evidence level is claim-specific.

## Minimum probe scenarios

1. **Canonical vocabulary:** change a controlled class identifier in a test branch; ensure consumers either migrate/resolve it or fail visibly, never silently invent a new class.
2. **Same evidence basis:** submit a known fixture; compare decision inputs, policy/version, persisted record and rendered explanation.
3. **Version compatibility:** read records produced by current, supported-old and unsupported-future versions; verify explicit compatibility or safe rejection.
4. **Atomic logical action:** inject failure before commit, after commit but before acknowledgement, and during retry; verify idempotency and honest pending/complete UI.
5. **Interruption/restart:** kill the process during a write, restart offline and online; inspect committed, pending, stale and failed states.
6. **Authority boundary:** attempt direct API/store operations and UI paths with missing, expired, revoked and out-of-scope authority.
7. **Disagreement ledger:** deliberately inject a mismatch between a test fixture, stored record and displayed state; verify a traceable finding without leaking sensitive data or auto-repairing the source.

## Scoring and reporting

If numeric indices are useful for trend comparison:

**Seam index = 100 × (applicable probes passed / applicable probes assessed).**

Rules:
- A probe is assessed only when its result is evidenced against the stated build/configuration.
- Not assessed is not a pass. Include it in the applicable denominator as not passed, and report coverage separately.
- Not applicable is excluded only with a written reason and reviewer/owner.
- Publish per-invariant results, not only an aggregate.
- Report **coverage**, **median seam index**, **lowest seam index**, and **critical blockers** together.
- Keep evidence strength separate; do not convert L0–L6 into arithmetic weights or assume CI evidence is universally stronger than runtime evidence.
- A median can summarize trend, but cannot override a failed critical invariant.

There is no universal pass threshold in v0.3.0. Each project must set thresholds and release gates through its own governance. No overall Harmony number certifies safety, compliance, readiness or correctness.

## Failure handling

No automatic cross-layer repair. Preserve the observed state, contain material risk, create a finding, identify authority and source of truth, decide the correction, implement the smallest authorized change, and rerun the probe plus relevant regressions. Record residual risk.
