# Contributing to Codex-Guidas

## Before adding a lesson or defect

1. Search existing records first: python scripts/codex.py search "symptom or failure mode".
2. Record whether a relevant lesson/defect was found. A similarity match is a lead, not proof of the same root cause.
3. Use the correct template and preserve the owning project's exact repository, branch, full commit SHA, run, environment and evidence links where known.
4. Keep observed facts, hypotheses, derived lessons and proposed controls separate. Unknown fields remain null.
5. State applicability boundaries, residual risk and what was not tested.

## Status changes

Use the canonical record taxonomy. A lesson is not Verified because code was written, a PR merged, or a test was added. Verification needs an exact commit, command/procedure, environment, acceptance criteria and recorded result. Defect closure also requires the proper owning-project authority to accept residual risk.

## Pull requests

The pull request template contains the required evidence and review checklist. CI validates structured metadata, unique IDs, lesson-index completeness and local Markdown link targets.

Do not add dashboards, bots, databases or ML similarity search without evidence that the current manual retrieval path is a demonstrated bottleneck. Automation may find and suggest; humans and project governance authorize.

## Scope and reuse

Codex-Guidas does not grant authority over other repositories. Do not implement project changes merely because a record or pack recommends them. No external reuse licence is currently declared; do not represent the repository as openly licensed until its owner records that decision.
