# Body — Persistence 33 (D-01…D-33)

**Framework:** CG-TT33 v0.3.0-draft  
**Analysis question:** Can the record be trusted on read, survive the failures the product promises to tolerate, and reconcile with code and UI?

## Circle A — Existence and structure (D-01…D-11)

| ID | Tier | Assessment question / intent |
|---|---|---|
| D-01 | Store inventory | Are stores, tables, files, caches, keys and external persistence locations inventoried for scope? |
| D-02 | Schema and runtime guards | Is each persisted record shape defined and validated at read/write boundaries? |
| D-03 | Version and migration path | Are schema versions and safe migrations defined before incompatible shape changes? |
| D-04 | Key and record lifecycle | Are creation, update, expiry, deletion, restore and key rotation/lifecycle paths understood? |
| D-05 | Transaction and atomicity contract | Are logical writes atomic where required, or explicitly modelled as staged/outbox/saga operations with recoverable states? |
| D-06 | Size, growth and retention | Are growth, quotas, retention and deletion behaviour justified by purpose and tested? |
| D-07 | Index and query cost | Are query paths and worst-case resource costs understood for expected scale? |
| D-08 | Read-detectable invariants | Can corruption, impossible combinations and stale references be detected safely on read? |
| D-09 | Backup, export and recovery necessity | Are backup/export/recovery mechanisms provided where the product needs them, with access, encryption, retention and restore risks assessed? Not every store needs an export path. |
| D-10 | Offline and sync semantics | If offline operation is promised or required, are local state, queueing, retries, idempotency, conflict and authority semantics explicit? |
| D-11 | Orphan and referential detection | Are orphaned records, broken references and partial lifecycle states detectable and handled? |

## Circle B — Correctness and trust (D-12…D-22)

| ID | Tier | Assessment question / intent |
|---|---|---|
| D-12 | Read validation and quarantine | Are malformed or untrusted records validated and safely quarantined without destructive guessing? |
| D-13 | Write validation | Are writes checked against domain invariants and authorization at the persistence boundary? |
| D-14 | Ledger integrity | Are audit/evidence records append-only or otherwise tamper-evident to the degree required by the threat model? |
| D-15 | Cross-reference and version integrity | Can records be tied to compatible schema, policy and producer versions? Exact version equality is not required if compatibility is explicit. |
| D-16 | Round-trip fidelity | Do serialize/deserialize cycles preserve the defined semantics, including unknown future fields where required? |
| D-17 | Time and ordering | Are timestamps, time zones, clock skew and event ordering handled explicitly? UTC storage is a default where suitable, not a substitute for domain semantics. |
| D-18 | Stored vs derived truth | Is it clear which values are source records, snapshots, caches or recomputable derivations? |
| D-19 | Concurrency and conflict discipline | Are concurrent writes, duplicate retries, stale edits and conflict resolution handled without silent data loss? |
| D-20 | Sensitive-data minimisation | Are sensitive fields limited, protected, access-scoped and retained only as justified? |
| D-21 | Fixture and persistence parity | Do fixtures, test contracts and actual persisted representations agree on the relevant semantics? |
| D-22 | Persistence failure evidence | Do material storage failures produce safe user/system states and actionable, privacy-safe evidence? |

## Circle C — Verification and change discipline (D-23…D-33)

| ID | Tier | Assessment question / intent |
|---|---|---|
| D-23 | Migration rehearsal | Are migrations rehearsed on representative, synthetic or safely redacted real-shaped data, with rollback/recovery evidence? |
| D-24 | Corruption and restart drills | Are corruption, interrupted writes, process kill and recovery tested for the product's promised failure model? |
| D-25 | Storage witness | Can an automated, read-only witness report schema, invariants, counts and integrity without exposing secrets or mutating production data? |
| D-26 | Key/field rename safety | Are key, field and identifier changes backward-compatible or safely migrated? |
| D-27 | Storage performance envelope | Is read/write performance measured at representative data volumes and devices? |
| D-28 | Schema-documentation parity | Can schema docs/types/migrations be checked against the live source of truth? |
| D-29 | Secret and credential handling | Are credentials and cryptographic secrets kept out of inappropriate stores/logs, with platform protection and threat assumptions documented? Do not require every store to be devoid of all sensitive values. |
| D-30 | Multi-device and transfer integrity | If export/import, sync or multi-device operation exists, are identity, ordering, duplication and conflict semantics tested? |
| D-31 | Retention and deletion enforcement | Are retention, deletion, legal hold and backup expiry actually enforced and evidenced? |
| D-32 | Recovery ordering | Do boot/read paths validate schema, key availability and integrity before trusting records? |
| D-33 | Storage disclosure and user control | Can the product accurately explain what it stores, where, why, for how long and how a user can access/delete it where applicable? |

## Profile notes

- Offline semantics (D-10) are conditional on actual product requirements. Do not infer offline requirements solely from geography or user assumptions.
- Backups, raw exports and device transfers increase exposure and must be justified, protected and tested.
- Retention and deletion must account for backups, replicas, legal obligations and shared-device realities.
- A local ledger is not automatically tamper-proof, encrypted or legally admissible.

**Passport rule:** identify the actual store and exact data class under assessment. Do not infer storage security from a library name or architecture diagram.
