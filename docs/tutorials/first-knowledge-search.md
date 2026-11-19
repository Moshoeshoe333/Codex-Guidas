# First knowledge search

This tutorial shows how to use Codex-Guidas to find and inspect a previous engineering lesson or defect.

## Prerequisites

- A local clone of the Codex-Guidas repository.
- Python 3.12 or a compatible Python 3 version supported by the project.
- A terminal opened at the repository root.

The CLI uses Python's standard library; no third-party Python package installation is required.

## 1. Check the knowledge records

Run:

```bash
python scripts/codex.py validate
```

The validator checks structured record metadata, IDs, lesson-index coverage and local Markdown link targets. A passing result confirms these structural checks only. It does not re-audit every source project or prove every lesson remains correct.

## 2. Search for a prior failure

For example:

```bash
python scripts/codex.py search "hydration failure"
```

All words in the query must match. Results are keyword matches, not semantic similarity and not root-cause conclusions.

Narrow a search to one project:

```bash
python scripts/codex.py search "hydration failure" --project SOULSYNCMOBILE
```

Other filters include `--type`, `--layer`, `--component` and `--failure-mode`. Run:

```bash
python scripts/codex.py search --help
```

## 3. Inspect the source record

Open any matching record and check:

- the originating repository and exact source revision;
- the evidence class and observation date;
- what was observed versus inferred;
- what the record explicitly says was not tested;
- whether the system, user, data and environment are comparable to the current problem.

A matching symptom is a lead. It does not establish that two defects have the same cause.

## 4. Review pending verification

Run:

```bash
python scripts/codex.py review-queue
```

The review queue surfaces records still marked pending. A due date is a reminder to review, not proof that a check has been completed.

## 5. Decide what to do with the lesson

For a consequential decision, use [the methodology–knowledge architecture](../methodology-knowledge-architecture.md) and its [knowledge-application record](../../09-templates/knowledge-application-record.md).

Choose whether the prior lesson should be applied, adapted, referenced only or rejected. Re-establish current facts and verification in the owning project. Codex-Guidas does not authorize a change to another repository.

## Commands

### Validate records

```bash
python scripts/codex.py validate
```

### Search all record types

```bash
python scripts/codex.py search "partial write storage"
```

### Search defects in a project

```bash
python scripts/codex.py search "storage read failure" --type defect --project SOULSYNCMOBILE
```

### Show pending follow-ups

```bash
python scripts/codex.py review-queue
```

### Run the CLI regression tests

```bash
python -m unittest discover -s tests -v
```

## Limitations

- Search is keyword/all-terms matching, not semantic search.
- Search results are candidate records, not proof of identical cause.
- A clean validator checks structure and local links, not source truth.
- Historical records may be stale; inspect exact commits and current project state.
- Only the owning project can authorize its implementation, release and residual-risk decisions.
