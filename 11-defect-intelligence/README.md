# Defect Intelligence

A lightweight, evidence-led mechanism for learning from defects and preventing recurrence across projects.

## Start here

- [Operating system and rules](system.md)
- [Defect record template](defect-template.md)
- [Cross-project lessons](../01-lessons-learned/ledger.md)
- [Source archaeology](../10-source-audits/2026-11-18-repository-archaeology.md)

## Register

| Defect ID | Project | Severity | State | Summary | Source / evidence |
|---|---|---|---|---|---|
| [DEF-2026-001](DEF-2026-001-storage-hydration-failure-masked-as-empty-ledger.md) | SoulSyncMobile | S4 | Investigating | Storage hydration failure may be represented as an empty ledger | Mock-backed hook reproduction recorded in CI run 44297424933; native-device/runtime and remediation pending |
| [DEF-2026-002](DEF-2026-002-multikey-scan-persistence-is-not-atomic.md) | SoulSyncMobile | S4 | Investigating | Logical scan record spans two non-atomic writes | Mock-backed partial-write reproduction recorded in CI run 44297424933; consistency decision and device/recovery proof pending |

## Intake rules

1. Copy the template to a new file named `DEF-YYYY-NNN-short-title.md`.
2. Assign the next unused ID after checking this directory.
3. Record facts before hypotheses.
4. Link exact commits and CI/runtime evidence; do not paste secrets or personal data.
5. Search existing CG lessons and DEF records before proposing a new control.
6. Update this register when state or severity changes.
7. For each material evidence event, synchronize the detailed DEF record, this register and any relevant chronological ledger follow-up in one coherent change. The detailed DEF record is the canonical current-state record; the ledger is chronology/context, not a substitute.

**Record integrity:** Update the detailed record and this index together. Do not leave a current register summary saying a test is pending when a later execution is recorded elsewhere; preserve earlier dates as historical observations and state the exact revision/run for any newer evidence.

## Historical incident migration

The ScoutSA incidents DOC-001–DOC-004 and CI-001 are documented in its engineering-integrity policy and in the source archaeology report. They have not yet been converted into individual DEF records because each needs its own exact affected commit, incident chronology, closure evidence and current recurrence assessment. Do not fabricate those fields. Convert them one at a time when source evidence is available.
