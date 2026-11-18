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
| — | — | — | — | No individual defect records migrated yet. Existing historical incident IDs remain in their source project records pending record-by-record extraction. | — |

## Intake rules

1. Copy the template to a new file named `DEF-YYYY-NNN-short-title.md`.
2. Assign the next unused ID after checking this directory.
3. Record facts before hypotheses.
4. Link exact commits and CI/runtime evidence; do not paste secrets or personal data.
5. Search existing CG lessons and DEF records before proposing a new control.
6. Update this register when state or severity changes.

## Historical incident migration

The ScoutSA incidents DOC-001–DOC-004 and CI-001 are documented in its engineering-integrity policy and in the source archaeology report. They have not yet been converted into individual DEF records because each needs its own exact affected commit, incident chronology, closure evidence and current recurrence assessment. Do not fabricate those fields. Convert them one at a time when source evidence is available.
