# SoulSyncMobile Persistence Contract — Decision Proposal

**Record:** SSM-PERSISTENCE-CONTRACT-DECISION-001  
**Date:** 2026-11-18  
**Status:** PROPOSAL ONLY — NOT RATIFIED  
**Target:** `Moshoeshoe333/SOULSYNCMOBILE`  
**Evidence baseline:** `1b989d1145587cf223fc9bbeecf8d1856536152c`  
**CI witness:** GitHub Actions run `44297424933` — SUCCESS

> This document proposes a persistence contract. It does not authorize application-code changes, schema migration, data deletion, dependency upgrades, or release.

## 1. Decision to make

Define what SoulSync Guardian means by a scan being saved, what happens when restoration or persistence fails, and which representation is authoritative.

The current implementation stores incidents and Harmony state under separate AsyncStorage keys. A scan writes the incident list first, then Harmony state. The in-memory snapshot changes only after both writes resolve.

## 2. Evidence established

The following controlled tests passed on the evidence baseline:

- TypeScript typecheck.
- Existing threat fixtures: 13/13.
- Storage adapter fault-injection tests: 10/10.
- Guardian hook fault-injection tests: 2/2.

The Guardian hook tests reproduced:

1. When the incident-ledger read rejects during hydration, the hook catches the error, substitutes empty defaults, and exposes `ready=true`.
2. When incident persistence succeeds and Harmony persistence rejects, the incident exists in mock storage but the hook's in-memory snapshot/export remains unchanged.

These are mock-backed tests of the actual hook and storage-manager modules. They do not establish native AsyncStorage crash guarantees, physical-device restart behaviour, or iOS/Android lifecycle semantics.

## 3. Required invariants

Any ratified contract should preserve these invariants:

1. **No false readiness:** failed restoration must never be presented as a successfully restored empty ledger.
2. **No silent data loss:** malformed or unreadable persisted data must not be silently replaced with an empty record.
3. **One defined authority:** exactly one representation is authoritative for a committed Guardian snapshot.
4. **Explicit commit boundary:** the application defines when a scan becomes committed and what the user sees before and after that boundary.
5. **Failure is visible:** persistence failure or uncertain outcome must be represented distinctly from a successful save.
6. **Retry safety:** retrying a scan must not silently create duplicate incidents or apply Harmony deltas twice.
7. **History is preserved:** migration and repair must not delete the old record until the new representation is verified.
8. **No unsupported guarantee:** AsyncStorage is a key-value store; do not claim database transactions or crash atomicity without platform-specific evidence.

## 4. Options

### Option A — Keep two keys and add recovery metadata

Continue storing incidents and Harmony separately, but introduce a journal/operation marker and recovery procedure.

**Advantages**
- Smaller migration from the current design.
- Keeps existing read/write boundaries.

**Costs and risks**
- More state transitions and recovery logic.
- The journal itself must be reconciled with two data writes.
- Requires idempotency, interrupted-operation handling, and corruption recovery.
- Still does not create a native multi-key transaction.

**Assessment:** Not recommended for the current small bootstrap implementation unless there is a demonstrated scale or separation requirement.

### Option B — One versioned canonical snapshot

Store a single versioned envelope under one canonical key, for example:

```ts
type GuardianLedgerV1 = {
  schemaVersion: 1;
  revision: number;
  incidents: IncidentLog[];
  harmony: HarmonyScoreState;
  lastOperationId: string | null;
};
```

A scan constructs the next complete snapshot and serializes it to the canonical key. The in-memory state is advanced only after the persistence contract's confirmation procedure succeeds.

**Advantages**
- Removes the known two-key split-write sequence.
- Makes authority and migration boundaries easier to describe.
- One persisted envelope can be validated as a whole.
- Easier to reason about revisions and duplicate operation IDs.

**Costs and risks**
- Rewrites the whole envelope for each scan.
- Storage size and retention need explicit limits.
- A single AsyncStorage `setItem` is not thereby proven crash-atomic.
- A rejected write can have an uncertain outcome; the application may need a read-back check before deciding whether to retry.

**Assessment:** Preferred candidate for the current MVP, subject to a size/retention review and native-device tests. Do not describe it as transactionally atomic.

### Option C — Replace AsyncStorage with a transactional persistence engine

Adopt a database with documented transaction semantics and explicit migration support.

**Advantages**
- Better fit if the ledger becomes large or multi-record workflows become more complex.
- May provide transaction guarantees that key-value storage does not.

**Costs and risks**
- New native dependency and platform-specific behaviour.
- More build, migration, backup, and compatibility burden.
- Not justified solely by the current two-key defect.

**Assessment:** Defer until measured requirements demonstrate that a database is warranted.

## 5. Recommended candidate contract

Recommend Option B for evaluation, not immediate implementation:

### Hydration

- Initial status is `loading`.
- Missing canonical record means a valid empty ledger.
- Successful parse and schema validation means `ready`.
- Read rejection means `restore_failed`, not `ready`.
- Malformed JSON or invalid shape means `corrupt`; preserve the original bytes and do not silently overwrite them.
- Provide an explicit retry path. Do not enable operations that imply a trustworthy restored ledger while state is unresolved.

### Scan commit

- Compute the candidate result and next snapshot in memory.
- Assign a stable operation ID before persistence.
- Persist one complete, versioned candidate envelope.
- Advance in-memory state only after the selected confirmation procedure succeeds.
- On failure, retain the previous in-memory snapshot and expose `save_failed` or `save_outcome_unknown` as appropriate.
- If the write outcome is uncertain, read back and compare the operation ID/revision before retrying. If read-back also fails, preserve the unknown state and avoid an automatic duplicate write.
- The UI must distinguish analysis result from durable-save status. A threat decision can be displayed while clearly stating that its ledger entry was not confirmed saved.

### Clear and migration

- Clear must have a defined durable commit boundary and failure status.
- Migration from the current two-key representation must read and validate both old values, construct a new envelope, write it, read it back, validate it, and only then mark migration complete.
- Do not delete legacy keys in the same unverified migration attempt.
- Preserve recoverability and record migration revision/version.

## 6. Required tests before implementation is considered complete

All tests use synthetic data and isolated storage.

| ID | Probe | Required observation |
|---|---|---|
| PC-01 | Missing canonical key | Valid empty ledger; ready |
| PC-02 | Read rejection | Restore failure; not ready |
| PC-03 | Malformed JSON | Corrupt status; bytes preserved |
| PC-04 | Valid JSON, invalid schema | Corrupt status; bytes preserved |
| PC-05 | Write rejects before persistence | Previous snapshot retained; save failure visible |
| PC-06 | Write persists then rejects | Read-back identifies committed operation or unresolved outcome |
| PC-07 | Retry same operation ID | No duplicate incident or double Harmony delta |
| PC-08 | App interruption around commit | Recovery result is deterministic or explicitly unknown |
| PC-09 | Clear rejects | Existing snapshot remains authoritative |
| PC-10 | Legacy two-key migration | New envelope validated before legacy data is retired |
| PC-11 | Concurrent queued scans | Monotonic revisions and no lost update |
| PC-12 | Native device restart | Persisted state restores correctly on supported Android/iOS targets |

A passing mock suite is necessary but not sufficient. PC-08 and PC-12 require native-device evidence.

## 7. Dependency audit — separate workstream

GitHub Actions run `44297424933` reported 23 npm audit findings: 21 high, 2 moderate, 0 critical.

The direct affected packages reported were Expo and React Native. The transitive graph included Expo CLI/Metro, Metro, Babel preset, React Native codegen/community CLI, `tinyglobby`, `picomatch`, `minimatch`, `jest-util`, and `jest-worker`.

The audit exposed GHSA-g3hv-75wg-m249 (minimatch denial-of-service condition) and GHSA-fc5q-39xc-vjpf (picomatch ReDoS condition).

The app declares Expo `~57.0.0` and React Native `0.86.0`. npm's suggested remediation changed across fresh installs and proposed older major-version targets. No dependency change is authorized by this proposal.

Before remediation:
- establish a committed, reproducible lockfile using the project's supported package manager;
- identify exact resolved package versions and dependency paths;
- verify the official Expo SDK / React Native compatibility matrix;
- inspect whether affected code is shipped, invoked, and exposed to attacker-controlled input;
- classify build-time versus runtime exposure;
- prepare a staged upgrade plan with rollback and full Android/iOS build validation.

Do not run `npm audit fix` or blindly apply npm's suggested downgrade.

## 8. Decisions requiring owner ratification

1. Is a Guardian scan considered one logical persistence operation?
2. Is Option B (one versioned canonical snapshot) approved as the implementation direction?
3. What incident retention/maximum snapshot size is acceptable?
4. Should a scan result be shown when its ledger save is unconfirmed, and what exact status wording is required?
5. Which Android/iOS device and restart tests are mandatory before release?
6. Who approves dependency remediation after compatibility review?

## 9. Gate

**Current gate: DECISION REQUIRED — NO IMPLEMENTATION AUTHORIZED.**

This document is a proposed contract, not a ratified one. A response to the questions above must be recorded before application runtime changes begin. Once ratified, implement the smallest approved change, run the synthetic regression suite, validate native device behaviour, and record residual risk.

