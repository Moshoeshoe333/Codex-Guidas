# Project Onboarding Method

**Status:** Working method for new and existing projects.  
**Owner:** The receiving project owner retains all project-specific authority.  
**Last reviewed:** 2026-11-27

## Purpose

Make it possible to understand a project, establish its real baseline, identify who owns important decisions and select only the Codex-Guidas controls that solve an actual need.

Onboarding is not a certification, architecture approval or permission to implement. It is a structured orientation and gap-discovery process. The receiving project's governing documents and decision owners remain authoritative.

Use this method when:
- creating a new project;
- bringing an existing repository into the Codex-Guidas portfolio;
- onboarding a new maintainer, collaborator or coding agent;
- materially changing project ownership, architecture, data handling or delivery model.

For a small contribution to a well-understood project, use the project-local startup procedure instead of repeating the full onboarding.

## 1. Identify the onboarding type

Choose one:

- **New project:** purpose and boundaries are being established; many technical and operational facts may be unknown.
- **Existing project:** inspect and preserve its actual state before proposing changes.
- **New maintainer or agent:** orient the person or agent to an existing project's source of truth, permissions and open gates. Do not treat access as a transfer of decision authority.
- **Material project transition:** record what changed, what is retained and what requires renewed approval.

Record the type, reason, owner, date and expected onboarding outcome in the [Project Onboarding Record](../09-templates/project-onboarding-record.md).

## 2. Establish identity and ownership

Confirm:
- project name, repository or system locations and concise purpose;
- intended users, stakeholders and affected communities;
- accountable project owner and technical maintainer;
- source-of-truth owners for requirements, domain rules, data, security, deployment and support;
- decision and approval authority, including escalation route;
- external partners, vendors and dependencies where relevant.

Distinguish the person who performs work from the person authorized to approve it. Where ownership is unknown or disputed, record the gap; do not infer authority from repository access or job title.

## 3. Establish the baseline

For an existing repository, inspect the live source:
- repository identity, default branch and current ref;
- full commit SHA and working-tree state where available;
- root and nested agent/developer instructions;
- canonical README, status, requirements, architecture, threat and operational records;
- build, test, CI and deployment configuration;
- open issues, unresolved decisions, known defects and release gates;
- exact commands and environmental prerequisites.

For a new project, state which items do not exist yet. Do not create fake historical baselines or make blank sections look like approved controls.

A baseline record must say what was inspected, when, at what revision and what was not inspected. Historical notes, summaries, screenshots and previous agent output are useful leads, not proof of current state.

## 4. Define the product and its boundaries

Write down:
- the problem and target users;
- observable user or operational outcome;
- initial use case and smallest useful vertical slice;
- explicit non-goals and deferred capabilities;
- success and failure measures;
- real-world constraints such as device, connectivity, language, accessibility, travel, power, cost and support;
- assumptions requiring research or user validation.

Avoid starting with a long feature list. Start with the user problem, the risky assumptions and the smallest safe way to learn.

## 5. Map information, trust and risk

At minimum, ask:
- What data is collected, created, imported, inferred, transformed, stored, shared and deleted?
- Which data is personal, sensitive, confidential, regulated or safety-critical?
- Who may access, change, export, correct or delete it?
- What are the trust boundaries and external inputs?
- What happens when dependencies, networks, storage, clocks or identity services fail?
- Could the project expose children or vulnerable people to harm, unsafe contact or unwanted visibility?
- Which laws, contracts, standards or qualified reviews may apply?
- What operational event requires containment, notification, recovery or escalation?

Record unknowns as unknown. A policy document, checklist, tool scan or passing test does not by itself establish legal compliance, security, safeguarding or safe operation. Obtain appropriately qualified and accountable review where consequence requires it.

## 6. Establish the decision and gate map

List the important decisions that must be made before implementation or release. Examples:
- product problem and MVP boundary;
- domain definitions and source-of-truth ownership;
- architecture, language/runtime, storage and external services;
- permissions, identity, privacy, safeguarding and retention;
- data migration and recovery;
- operational support, deployment and rollback;
- pilot, user validation and launch conditions.

For consequential or hard-to-reverse choices, use an [Architecture Decision Record](../09-templates/architecture-decision-record.md). Record rejected options and the reason they were rejected. An ADR documents a decision; it does not make the decision valid unless the named authority accepts it.

## 7. Select a proportionate Codex-Guidas baseline

Start with the receiving project's existing controls. Add only the relevant reusable practices:
- [Evidence-First Engineering](../02-methodologies/evidence-first-development.md) for claims, research and implementation evidence;
- [Project Task Contract](../09-templates/project-task-contract.md) for material tasks;
- [Agent Instructions Template](../09-templates/agent-instructions-template.md) where coding agents are used;
- [Security and Safeguarding](../04-security/safeguarding-and-threat-modeling.md) for trust, data and human safety boundaries;
- [Verification and CI](../05-testing-verification/verification-and-ci.md) for reproducible checks;
- relevant [Knowledge Packs](../packs/README.md), after reading their maturity and completing a local adoption record;
- [Defect Intelligence](../11-defect-intelligence/README.md) where defects and recurrence need structured tracking.

Do not import every pack or copy the whole Codex-Guidas hierarchy by default. Selective adoption is preferred. Each adopted pack must be adapted, owner-approved and locally revalidated. Pack adoption is not certification.

## 8. Establish the minimum operating surface

Before treating a project as ready for sustained work, identify where maintainers can find:
- project purpose, scope and current status;
- canonical requirements, decisions and source-of-truth records;
- setup and exact developer commands;
- focused and regression tests;
- CI status and how to identify the run for a commit;
- security, privacy and safeguarding requirements;
- defect reporting and incident escalation;
- release, rollback, backup and recovery procedure where applicable;
- agent instructions and permitted actions, if agents are used;
- owners, reviewers and handover contacts.

For a new project, these may initially be short records marked proposed or incomplete. Accuracy and ownership matter more than document count.

## 9. Agree the first milestone

The onboarding record should end with:
- one primary outcome;
- the smallest useful next task;
- acceptance criteria and required evidence;
- responsible person and decision owner;
- permissions and exclusions;
- stop/rollback conditions;
- open questions and review date.

Do not authorize broad implementation just because onboarding is complete. Each milestone retains its own task contract, decision gate and acceptance evidence.

## 10. Close onboarding without overstating readiness

Use one outcome:
- **Oriented:** identity, ownership and source-of-truth paths are known.
- **Baseline recorded:** inspected state and limitations are captured.
- **Ready for scoped work:** one bounded task has an owner, permissions, acceptance criteria and stop conditions.
- **Blocked:** a critical ownership, evidence, safety or authority gap prevents responsible progress.
- **Incomplete:** onboarding remains partial or required evidence is unavailable.

These are onboarding outcomes, not product maturity or release statuses. Revisit the record when ownership, architecture, data flows, external dependencies, user group or risk materially changes.

## Related records

- [Project Onboarding Record](../09-templates/project-onboarding-record.md)
- [Project Operating Guide](project-operating-guide.md)
- [Project Task Contract](../09-templates/project-task-contract.md)
- [Architecture Decision Record](../09-templates/architecture-decision-record.md)
