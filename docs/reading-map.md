# Reading map

**Purpose:** Help a reader find the right kind of knowledge without reorganising the repository's evidence records.

Codex-Guidas uses [Diátaxis](https://diataxis.fr/) as a lightweight content-design lens. Diátaxis describes four user needs: learning by doing, accomplishing a task, looking up authoritative information and understanding why something works. It is a navigation aid here—not a new evidence status, maturity score or mandatory folder structure.

## Tutorials — learn by doing

Start with a guided sequence:

- [First knowledge search](tutorials/first-knowledge-search.md) — run the CLI, validate the knowledge base and interpret search results.

A tutorial should help a new reader complete a safe learning journey. It should not hide important limitations or imply that a successful command validates the content.

## How-to guides — accomplish a task

- [Contributing to Codex-Guidas](../CONTRIBUTING.md) — add or update a lesson or defect with provenance.
- [Defect Intelligence](../11-defect-intelligence/system.md) — detect, triage, investigate, verify and close a defect.
- [Knowledge application](methodology-knowledge-architecture.md) — decide whether a prior lesson should be applied, adapted, referenced or rejected.
- [Knowledge application record](../09-templates/knowledge-application-record.md) — capture consequential cross-project transfer.

How-to guidance should name prerequisites, decision authority, expected outcome and stop conditions.

## Reference — look up authoritative information

- [CLI commands and examples](tutorials/first-knowledge-search.md#commands)
- [Metadata schema](../00-foundation/metadata-schema.md)
- [Record taxonomy](../00-foundation/record-taxonomy.md)
- [Lesson index](../01-lessons-learned/ledger.md)
- [Defect register](../11-defect-intelligence/README.md)
- [Templates](../09-templates/)

Reference material should be precise, bounded and updated alongside the thing it describes.

## Explanation — understand the reasoning

- [Operating principles](../00-foundation/operating-principles.md)
- [Methodology and knowledge architecture](methodology-knowledge-architecture.md)
- [Method selection](method-selection.md)
- [Startup repository benchmark](research/2026-11-19-startup-repo-and-engineering-knowledge-benchmark.md)
- [Doctrines](../doctrines/README.md)
- [Source archaeology](../10-source-audits/2026-11-18-repository-archaeology.md)

Explanations give context and rationale. They do not override the current record taxonomy, source project or decision authority.

## Important boundary

A lesson, defect, evidence ledger, decision record or project crosswalk is an **evidence/knowledge object**. It may contain explanation and reference information, but it should not be forced into a tutorial or how-to category simply to make the taxonomy complete.

Keep the existing domain folders and historical records in place. Use the reading map to improve discovery. Reorganise files only when reader evidence shows that the current information architecture is causing real friction.
