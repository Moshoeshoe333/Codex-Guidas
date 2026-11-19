# Methodology and knowledge architecture

**Status:** Proposed operating interface for controlled use  
**Last reviewed:** 2026-11-19

## Purpose

This document defines how our reasoning methods, specialist assessment instruments, Codex-Guidas knowledge records and project decision authority work together.

It is an interface contract, not a new methodology, scoring framework, certification or command hierarchy. It does not ratify any proposed framework. Existing method definitions and their maturity labels remain authoritative in their own documents.

## Four distinct responsibilities

| Layer | Main question | What it owns | What it does not own |
|---|---|---|---|
| **1. Methodology** | How should we reason and investigate this question? | Point → Knowing → Witness → Gate; evidence-first development; evidence vocabulary | Historical project facts or project release authority |
| **2. Specialist instruments** | Which additional lens is needed for this particular question? | Relevant bounded assessment method, such as selected 33-Perspective lenses or Tri-Tier 33 | Universal scores, automatic decisions or ratification |
| **3. Codex-Guidas knowledge** | What have we previously observed, learned, proposed or verified? | Searchable lessons, defect records, provenance, applicability limits and review reminders | Owning-project source of truth, implementation authority or proof that an old finding still applies |
| **4. Owning project** | What is true now, and who may authorize action? | Current source, issue/incident record, project-specific tests, implementation, release and residual-risk decisions | Unqualified transfer of assumptions from another project |

These layers inform one another but must not be collapsed. The method determines the investigation; Codex-Guidas supplies historical context; the owning project supplies current evidence and authority.

## Default operating sequence

Use the smallest proportionate version of this sequence for consequential work:

1. **Point — define the decision.** State the user/risk problem, intended outcome, decision to make, scope, exclusions and stop condition.
2. **Knowing — establish what is known.** Separate observed facts, derived conclusions, assumptions, hypotheses, contradictions and unknowns. Capture the current project baseline.
3. **Retrieve — consult institutional memory.** Search Codex-Guidas lessons and defect records. Record terms, results and IDs considered. Search the owning project's issues, commits and tests as well. A match is a lead, not proof of identical cause.
4. **Witness — test applicability with evidence.** Inspect original evidence and dates. Compare system boundaries, versions, threat models, users, data, environment and operating conditions. Record where a prior lesson transfers and where it does not.
5. **Gate — decide whether and how to proceed.** Name the project decision owner, required evidence, acceptance criteria and explicit authorization. A lesson or AI recommendation cannot pass this gate.
6. **Execute and verify in the owning project.** Make only the authorized change. Record exact repository, branch, full commit SHA, commands, environment, test results, failures and untested surfaces.
7. **Learn — update the knowledge record.** Link the result back to the source project. Reuse an existing lesson where possible; add a new lesson only when a transferable principle or control has been established.

For low-risk routine changes, this may be a few lines in the PR or commit record. Do not make every minor edit complete a full assessment.

## When to create a knowledge-application record

Use [the knowledge-application template](../09-templates/knowledge-application-record.md) when at least one of these is true:

- a consequential defect, incident, security/privacy/safeguarding concern or data-integrity risk is being investigated;
- a prior lesson materially changes the proposed design, control or test plan;
- a project decision relies on evidence or a control transferred from another project;
- a known failure mode recurs, or a previous preventive control appears ineffective;
- an implementation decision is blocked on conflicting historical evidence.

Do not create an application record just to document a search that did not affect a decision.

## Applicability test: transfer principles, not assumptions

Before using an old lesson, explicitly ask:

- Is the underlying invariant the same, or only the symptom?
- Are the code path, architecture, persistence model and trust boundaries comparable?
- Are affected users, ages, permissions, data sensitivity and threat actors comparable?
- Are versions, platform, environment and dependency behaviour comparable?
- Does the source evidence actually support the proposed control?
- What new test is required in the receiving project?
- What important difference could make the transfer unsafe or ineffective?

Record one of four outcomes:

- **Apply:** context and evidence support adopting the control, subject to project verification.
- **Adapt:** principle is relevant but must be redesigned for the receiving context.
- **Reference only:** useful background; not a basis for the current change.
- **Reject:** not applicable or contradicted; record the reason.

No outcome means the control is verified in the receiving project. Only receiving-project evidence can establish that.

## Relationship to the 33-based methods and evidence ladders

- Point → Knowing → Witness → Gate remains the default reasoning sequence.
- The foundation E0–E6 ladder describes the evidence supporting an engineering claim.
- Tri-Tier 33's L0–L6 vocabulary answers a different technical-assessment question. Never add, average or transfer values between the ladders.
- The 33-Perspective Register, Tri-Tier 33 and three-pass 99-tier sieve retain their explicitly stated maturity and ratification status. Select only relevant lenses; do not turn them into mandatory checklists.
- A framework assessment does not automatically establish implementation readiness, product-market fit, legal compliance, security certification or release approval.

## Authority and AI boundary

Codex-Guidas maintainers may curate, classify and link knowledge. The owner of each project retains authority over its source code, priorities, tests, security posture, release and accepted residual risk.

AI or automation may search, summarize, identify missing evidence and suggest hypotheses. It may not independently:

- treat a similarity match as a confirmed root cause;
- promote a lesson to Verified;
- close a defect or accept residual risk;
- alter another project's production code, controls, access or deployment;
- ratify a methodology or override a project gate.

Where an action is not explicitly authorized, stop at recommendation and evidence preparation.

## Pilot and measures of real impact

Start with a manual pilot on consequential defects and decisions. Record:

| Measure | What to count | What it tells us |
|---|---|---|
| Search-before-action | Eligible cases with a recorded prior-knowledge search | Whether the retrieval step is actually used |
| Useful retrieval | Cases where a prior record changed diagnosis, design or tests | Whether the knowledge base is relevant |
| Applied controls | Cases that adapted a prior control and linked receiving-project verification | Whether learning transfers safely |
| Recurrence | Repeated failure modes after a control was adopted | Whether controls are effective over time |
| Evidence-complete closure | Closed records with exact change and acceptance evidence | Whether closure quality improves |
| Diagnosis effort | Time from intake to a defensible cause/next test | Whether retrieval reduces investigation friction |

Set a baseline before claiming improvement. Report small samples and confounders. A green validator proves record structure and links, not the accuracy of lesson content or the effectiveness of transferred controls.

## First worked example

See [the bounded application trace for DEF-2026-001](examples/DEF-2026-001-knowledge-application.md). It demonstrates retrieval and applicability analysis without authorizing an application change or claiming native-device verification.

## Governing references

- [Operating principles](../00-foundation/operating-principles.md)
- [Evidence-first development](../02-methodologies/evidence-first-development.md)
- [Method selection](method-selection.md)
- [Defect Intelligence operating model](../11-defect-intelligence/system.md)
- [Record taxonomy](../00-foundation/record-taxonomy.md)
- [Repository purpose and scope](../PURPOSE.md)
