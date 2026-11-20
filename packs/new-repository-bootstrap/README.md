# Pack: New Repository Bootstrap and Assurance

**Pack ID:** CG-PACK-006  
**Version:** 1.0.0  
**Maturity:** Proposed baseline template; must be adapted, owned and evidenced in each receiving repository. It is not a standard, certification or claim of compliance.  
**Upstream source:** Codex-Guidas, `packs/new-repository-bootstrap/`

## Purpose

Help a team establish a small, reviewable repository foundation before significant implementation or external release. The pack connects repository identity, decision ownership, engineering practice, security, data handling, documentation and operational readiness.

It is deliberately a **minimum baseline plus risk-triggered overlays**. A small library, an internal prototype, a public website and a system handling children's data or financial value do not need identical controls.

## Start here

1. Read the [baseline checklist](BASELINE-CHECKLIST.md).
2. Select the [risk overlays](RISK-OVERLAYS.md) triggered by the product, users, data, integrations and deployment model.
3. Copy the repository-level [pack adoption record](../ADOPTION-RECORD.md) into the target repository and record the exact upstream commit and local owner.
4. Mark each applicable control with a status and evidence reference. Record why a control is not applicable or who accepted a residual risk.
5. Resolve stop conditions before public launch, handling sensitive data or performing irreversible operations.

## Working principles

- **Start with the problem, not the framework.** Identify the user, the outcome, scope and exclusions before selecting tooling.
- **Assign authority.** Name the repository owner and decision owner. Identify a recovery or backup maintainer where trust and capacity permit; do not invent a second-person approval rule for a solo maintainer.
- **Choose controls by exposure.** Use the baseline for every repository and add only the overlays justified by actual risks.
- **Verify the real control.** A policy file, configuration snippet or passing unrelated CI run does not prove a GitHub setting, deployment, recovery path or user-facing safeguard works.
- **Keep local authority local.** This pack does not decide licensing, architecture, legal compliance, data retention, security acceptance or release readiness for the receiving project.
- **Keep the record honest.** Separate not assessed, planned, implemented, verified, not applicable and accepted risk. Every important claim needs a source.
- **Prefer reversible decisions.** Record decisions with meaningful consequences and define rollback or stop conditions before irreversible work.

## Adoption profiles

Use these as selection prompts, not maturity levels:

| Profile | Typical use | Additions |
|---|---|---|
| Private/internal | Learning repo, internal tool, research prototype | Repository ownership, clean source control, reproducible setup, proportionate tests, secrets hygiene and an explicit data boundary |
| Public/community | Public code, external contributions, downloadable releases | Public-facing security-reporting route, contribution expectations, licence/rights decision, maintainer capacity and release provenance |
| User-facing product | Deployed service, app or website | User requirements, threat and privacy review, access control, operational monitoring, incident response and tested recovery |
| Higher-risk domain | Children, sensitive personal data, money, safety-critical activity or privileged automation | Apply every relevant overlay and require specialist review before exposure |

A repository may fit more than one profile. Profiles do not replace the trigger-based overlays.

## What this pack does not do

This pack does not:
- grant a software or documentation licence;
- establish compliance with POPIA, the Children's Act, PCI DSS or any other law or standard;
- certify that a repository is secure, reliable or production-ready;
- choose a cloud provider, framework, database, package manager or branching model;
- require every optional community-health file, testing framework or automation product;
- prove that an implementation behaves as documented.

Use qualified legal, privacy, security, safeguarding or domain advice where the project risk requires it.

## Stop conditions

Pause the affected activity when:
- repository, code or content ownership is materially unclear before external distribution;
- the intended user, decision owner or acceptance criteria cannot be identified;
- secrets or production access are being introduced without an approved handling method;
- sensitive or children's data could be exposed before the relevant privacy/safeguarding controls are reviewed;
- a money/value flow lacks defined ledger, retry, reversal and reconciliation rules;
- an irreversible data change has no credible backup, restore or recovery plan;
- the public security-reporting path is absent or misleading for a public release;
- a critical failure or release-blocking risk remains unexplained or is not explicitly accepted by the authorized owner.

A stop condition is a reason to resolve the gap, reduce scope or decline the release—not to hide the gap in documentation.

## Evidence and status vocabulary

For each checklist item, record one of:

- **Not assessed** — no adequate review has been performed.
- **Planned** — an owner and intended action exist; the control is not yet present.
- **Implemented** — the control exists in code, configuration, process or platform settings, but its behaviour may not yet be verified.
- **Verified** — direct evidence demonstrates the control in the receiving repository and relevant environment.
- **Not applicable** — include the reason and the decision owner.
- **Accepted risk** — include the residual risk, rationale, authorized owner and review/expiry trigger.

Use exact evidence where possible: commit SHA, file path, test command and result, CI run URL, platform setting evidence, deployment identifier, restore exercise or reviewed operational observation. Do not mark a control Verified merely because a document exists.

## Adaptation and provenance

Use [ADOPTION-RECORD.md](../ADOPTION-RECORD.md) for the source commit, pack version, local changes, owner, review and approval. Keep this pack as an upstream snapshot; update it deliberately rather than overwriting local repository policy.

The broader [Evidence-First Engineering pack](../evidence-first-engineering/README.md) describes how to move from a question and evidence contract to an authorized, verified change.

## Licensing boundary

Codex-Guidas currently has no outbound reuse licence recorded. Public visibility is not a general permission to copy, redistribute or relicense this material. Use it only where you have the necessary rights or authorization; external reuse requires the repository owner to resolve and publish an explicit licensing decision. This pack does not change that boundary.
