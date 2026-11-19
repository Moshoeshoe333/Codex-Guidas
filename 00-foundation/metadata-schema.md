# Structured record metadata

Structured record files begin with YAML frontmatter delimited by three hyphens. Values use a deliberately small YAML subset: JSON-quoted strings, JSON flow arrays, or null. This keeps the files valid YAML while allowing validation with Python's standard library and no third-party parser.

## Required fields

| Field | Type | Rule |
|---|---|---|
| id | string | Stable unique record ID; also matches filename stem and first heading. |
| record_type | string | lesson or defect. |
| status | string | Lesson status or defect workflow state from record-taxonomy.md. |
| projects | array of strings | Project names supported by the source; empty array when unknown. |
| layer | string | Retrieval tag: mind, body, spirit, infra, process, cross-cutting or unknown. |
| component | string or null | Known component; null when not established. |
| failure_mode | string or null | Known failure mode; null when the source does not establish one. |
| severity | string or null | S0–S4 for defect records; null when not applicable/known. |
| origin_date | ISO date or null | Date first observed/originated; do not infer missing historical dates. |
| last_reviewed | ISO date or null | Date the record content was actually reviewed. |
| verification_due | ISO date or null | Follow-up date for pending verification; not a verification result. |
| evidence_class | string | Preserve source evidence wording. Do not collapse it into lifecycle status. |
| verification_status | string | pending, source-only, not-claimed, verified or blocked. |
| source_path | string | Provenance pointer to the source record or artifact. |
| review_scope | string | What this metadata/content review did and did not establish. |
| tags | optional array of strings | Curated retrieval tags; omit or use an empty array when not established. Tags are labels, not evidence or status. |

## Interpretation rules

- Null means unknown or not applicable. It is not a guessed default.
- Layer and component values are retrieval facets, not architecture certification.
- Optional tags are curated by a maintainer; do not infer them from a model suggestion or automatically promote them to evidence. The generated index preserves only explicitly supplied tags.
- The original ledger is retained in 01-lessons-learned; individual lesson files are the current indexed records.
- The 2026-11-19 migration set last_reviewed to that date for a structural review of record text and metadata only. It did not re-execute source tests or independently validate each referenced project.
- A 2026-12-19 deadline was assigned to entries explicitly marked as pending verification in the source ledger. This is an administrative follow-up date, not evidence that verification is complete.
- Pending records without a due date are surfaced by the review queue; do not quietly omit them.
- Do not add credentials, personal data, private messages or unnecessary sensitive incident detail.

## Validation

Run: python scripts/codex.py validate

The checker validates frontmatter shape, required fields, allowed state values, ISO dates, filename/ID agreement, uniqueness and lesson-index coverage. It uses only the Python standard library.
