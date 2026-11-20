# Defect Intelligence

A lightweight, evidence-led mechanism for learning from defects and preventing recurrence across projects.

## Start here

- [Operating system and rules](system.md)
- [Defect record template](defect-template.md)
- [Knowledge-application workflow](../docs/methodology-knowledge-architecture.md)
- [Knowledge-application record template](../09-templates/knowledge-application-record.md)
- [Cross-project lessons](../01-lessons-learned/ledger.md)
- [Source archaeology](../10-source-audits/2026-11-18-repository-archaeology.md)

## Register

| Defect ID | Project | Severity | State | Summary | Source / evidence |
|---|---|---|---|---|---|
| [DEF-2026-001](DEF-2026-001-storage-hydration-failure-masked-as-empty-ledger.md) | SoulSyncMobile | S4 | Investigating | Storage hydration failure may be represented as an empty ledger | Read-only source finding F-07; later mock-backed hook reproduction; native/UI checks remain open |
| [DEF-2026-002](DEF-2026-002-multikey-scan-persistence-is-not-atomic.md) | SoulSyncMobile | S4 | Investigating | Logical scan record spans two non-atomic writes | Read-only source finding F-08; mock-backed hook test; native/restart checks remain open |

## Intake rules

1. Copy the template to a new file named `DEF-YYYY-NNN-short-title.md`.
2. Assign the next unused ID after checking this directory.
3. Record facts before hypotheses.
4. Link exact commits and CI/runtime evidence; do not paste secrets or personal data.
5. Search existing CG lessons and DEF records before proposing a new control.
6. Update this register when state or severity changes.

## Historical incident migration

The ScoutSA incidents DOC-001–DOC-004 and CI-001 are documented in its engineering-integrity policy and in the source archaeology report. They have not yet been converted into individual DEF records because each needs its own exact affected commit, incident chronology, closure evidence and current recurrence assessment. Do not fabricate those fields. Convert them one at a time when source evidence is available.

## Retrieval and review queue

Use the repository search tool before triage:

    python scripts/codex.py search "hydration empty ledger"
    python scripts/codex.py search "partial write" --project SOULSYNCMOBILE
    python scripts/codex.py review-queue
    python scripts/codex.py validate

Search matches are candidate similarities, not proof of an identical cause. Record search terms and matching IDs in each defect record. The review queue surfaces pending verification and overdue follow-ups; deadlines are review triggers, not evidence.

For a consequential case where a prior lesson influences the response, record the applicability decision using the [knowledge-application template](../09-templates/knowledge-application-record.md). The [DEF-2026-001 worked example](../docs/examples/DEF-2026-001-knowledge-application.md) shows the intended boundary: CG-011 is useful at the principle level but does not establish identical root cause or authorize a receiving-project change.

Structured individual records use YAML frontmatter described in the metadata schema. Canonical state and severity meanings live in the record taxonomy.
