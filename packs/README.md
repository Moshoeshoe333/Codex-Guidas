# Reusable Knowledge Packs

This directory is the selective-reuse layer of Codex-Guidas. Each pack is a bounded, portable unit of methodology, principles, templates or engineering controls that can be copied or adapted into an existing repository, or used as the starting point for a new one.

## Design goals
- Reuse one useful capability without importing the whole knowledge base.
- Keep each pack understandable outside this repository.
- Preserve source, version, maturity, limitations and adaptation history.
- Keep project-specific authority, legal duties, security policy and architecture local.
- Make adoption reversible and reviewable.

## Pack catalogue

| Pack | Use it for | Maturity |
|---|---|---|
| [Point–Knowing–Witness–Gate](point-knowing-witness-gate/README.md) | Decision discipline and evidence boundaries | Foundational method; detailed 33-tier specification remains open |
| [Evidence-First Engineering](evidence-first-engineering/README.md) | Research-to-implementation workflow and evidence ledger | Working methodology |
| [33-Perspective Review](33-perspective-review/README.md) | Proportionate multi-lens decision challenge | Register v0.2; proposed, not ratified |
| [Defect Intelligence](defect-intelligence/README.md) | Defect capture, recurrence prevention and lessons | Operating structure; individual migration remains incomplete |
| [Human-Centred Safety Boundaries](human-centred-safety/README.md) | Privacy, safeguarding, authority and threat-boundary prompts | Principles and review prompts; not a compliance standard |

## How to use a pack
1. Read its README and maturity/limitations before copying anything.
2. Copy the complete pack directory into the target repository, or fork this repository if the team wants the full knowledge base.
3. Add a short adoption record using ADOPTION-RECORD.md.
4. Adapt terminology, roles, law, risk level, workflows and acceptance criteria to the target project.
5. Keep the upstream source path, source commit, pack version and local changes.
6. Add project-specific tests or operational evidence where the pack describes a control.
7. Review updates deliberately; do not overwrite local changes automatically.

## Transfer rules
- Transfer principles, not assumptions.
- A pack is guidance, not an authorization token.
- A proposed method does not become verified merely by being copied.
- A checklist does not replace domain expertise, legal advice, threat modelling or user research.
- If a pack conflicts with the target repository's governing policy, stop and resolve the conflict before adoption.
- Never import secrets, personal data, production credentials or unreviewed project-specific records.

## Forking options
- Whole repository fork: best when a team wants the full evolving compendium and its history.
- Selective pack copy: best when a project needs one methodology or control set.
- New project seed: start with only the packs justified by the project's risks and decisions.

Git subtree, submodule or package distribution can be considered later if repeated synchronized consumption justifies the operational overhead. The current source-of-truth is this repository; copied packs are snapshots until deliberately refreshed.

## Licensing and reuse boundary
No licence has been added by this pack structure. GitHub forking/copying mechanics do not themselves grant a general licence to third parties. Confirm repository ownership and choose an explicit licence before inviting external reuse or redistribution. Internal reuse across repositories under the same ownership should still retain provenance and review local permissions.
