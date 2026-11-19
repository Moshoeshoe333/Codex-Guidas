# Worked example — applying prior knowledge to DEF-2026-001

**Record type:** Illustrative knowledge-application trace  
**As of:** 2026-11-19  
**Owning project:** SoulSyncMobile  
**Source defect:** [DEF-2026-001](../../11-defect-intelligence/DEF-2026-001-storage-hydration-failure-masked-as-empty-ledger.md)  
**Status:** Investigation remains open. This example does not authorize or implement an application change.

## 1. Point — decision

Determine whether a storage hydration read failure can be distinguished from a successfully loaded empty incident ledger, and identify the next evidence required before proposing a fix.

**Scope:** The hydration state and its user-facing representation.  
**Exclusions:** Changing SoulSyncMobile code, claiming native-device reproduction, or closing the defect.

## 2. Knowing — current evidence

The source defect record reports:

- Source inspection of `src/hooks/useGuardianState.ts` found a catch path that resets in-memory state and sets `ready=true`.
- Source inspection of `App.tsx` found dashboard readiness/count presentation without an explicit storage-error indicator.
- A later mock-backed Guardian hook test on commit `1b989d1145587cf223fc9bbeecf8d1856536152c`, CI run [44297424933](https://github.com/Moshoeshoe333/SOULSYNCMOBILE/actions/runs/44297424933), reproduced the hook outcome: a rejected incident-ledger read produced `ready=true` with an empty in-memory ledger.
- The test used React-hook and AsyncStorage mocks. It did not exercise native-device AsyncStorage, process restart, or the complete user-visible UI flow.

**Claim boundary:** The failure path is reproduced in a bounded mock-backed hook harness. Native storage behaviour, full UI semantics, actual user impact and an application fix are not established.

## 3. Retrieval — relevant prior knowledge

The defect record identifies search terms including:

- `storage hydration failure`
- `empty ledger fallback`
- `fail-closed`
- `persistence read error`

It also records CG-002 and CG-011 as related lessons.

The relevant reusable principle from [CG-011](../../01-lessons-learned/lessons/CG-011.md) is to test allowed, warning, denied, unknown and malformed-input paths. That principle supports explicit handling of failure/unknown states, but it does not prove that CG-011 and DEF-2026-001 share the same root cause or that a particular implementation will correct this defect.

## 4. Witness — applicability analysis

| Prior knowledge | Applicability | Decision |
|---|---|---|
| CG-011: fail-closed decisions need explicit semantics and recovery paths | Relevant at the principle level: an unavailable ledger must not be represented as a confirmed empty ledger | **Adapt** the principle into explicit persistence-state semantics and project-specific tests |
| DEF-2026-001 evidence | Directly describes the current owning-project finding; it is the target record, not independent corroboration | Use as the baseline; do not count it as a second source |
| Generic lessons about test coverage | Useful only when mapped to the missing UI/native-storage surfaces | Reference only until specific acceptance tests are defined |

A plausible next test set is: successful empty read, successful non-empty read, rejected read, malformed/corrupt payload, retry/recovery, and user-visible error/unknown state. Native-device and restart tests should be selected by the owning project after reviewing platform support and risk.

## 5. Gate — authority and next action

- **Authority:** SoulSyncMobile project maintainer.
- **Authorization:** No application change is authorized by this Codex-Guidas example.
- **Next evidence:** Owner-approved UI-level assertion and native-storage lifecycle checks, with exact commit, command, environment and run links.
- **Stop condition:** Do not claim the user-facing behaviour is fixed or safe until the relevant acceptance criteria pass.
- **Current defect disposition:** Keep DEF-2026-001 in **Investigating**; verification remains **pending**.

## 6. Learning outcome

This trace demonstrates a disciplined transfer of a principle, not a completed remediation. It helps avoid two errors: mistaking similar language for the same root cause, and treating a mock-backed hook test as native-device or user-flow proof.

No new cross-project lesson is proposed. Update the existing defect and related lesson only when the owning project produces additional evidence. No severity, lesson maturity or closure status is changed by this example.
