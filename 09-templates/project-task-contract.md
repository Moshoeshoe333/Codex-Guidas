# Project Task Contract Template

**Contract ID:** TASK-YYYY-NNN  
**Status:** Proposed / Authorized / In progress / Blocked / Complete / Superseded  
**Created:** YYYY-MM-DD  
**Last updated:** YYYY-MM-DD  
**Project / repository:**  
**Task owner:**  
**Decision owner:**  
**Human reviewer (if required):**

> Define the outcome, baseline, permissions and proof before material work begins.

## 1. Purpose and decision

- **Question / problem / risk:**
- **Affected user, system or stakeholder:**
- **Why this matters now:**
- **Decision this task should enable:**
- **Intended outcome:**
- **What would make this task not worth doing:**

## 2. Baseline and source of truth

| Item | Exact value |
|---|---|
| Repository URL / full name | |
| Branch / ref | |
| Baseline full commit SHA | |
| Working-tree state | |
| Relevant source paths and blob SHAs | |
| Canonical project documents | |
| Current milestone / gate | |
| Relevant CI, test or runtime evidence | |
| As-of date/time and timezone | |

Record unknowns explicitly. Do not use a historical status summary as proof of current repository state.

## 3. Scope and exclusions

**In scope**
- 

**Out of scope / explicitly prohibited**
- 

**Affected components, data classes, users or external systems**
- 

**Dependencies and prerequisites**
- 

## 4. Acceptance criteria

Define observable outcomes before execution. Each criterion should identify the proof that would satisfy it.

| ID | Acceptance criterion | Required evidence / method | Owner / reviewer | Result |
|---|---|---|---|---|
| AC-01 | | | | Not run |
| AC-02 | | | | Not run |

Do not weaken acceptance criteria after seeing a result. For an evaluation or audit, pre-register the rubric and critical failure conditions before execution.

## 5. Evidence and research plan

| Claim / question | Source or method | Required identity / quality | Known limitations |
|---|---|---|---|
| | | | |

- **Primary sources required:**
- **Independent corroboration required:**
- **Counter-evidence to seek:**
- **Important unknowns:**
- **Claims explicitly not being made:**

Distinguish source inspection, derived interpretation, proposed design, executed test, CI result, runtime observation and independent user/domain evidence. A test definition is not a test run.

## 6. Decision authority and permissions

Name the person or role authorized to approve the relevant decision, exception or release. If an approval is required but unavailable, the task remains blocked at that gate.

| Action | Permission | Conditions / limits |
|---|---|---|
| Read files and inspect repository history | Allowed / Restricted / Prohibited | |
| Edit files inside the defined scope | Allowed / Explicit approval required / Prohibited | |
| Run local read-only inspection | | |
| Run tests, builds or local services | | |
| Install or update dependencies | | |
| Change schemas, migrations or lockfiles | | |
| Stage changes or create commits | | |
| Push, merge, rebase or rewrite history | | |
| Deploy, publish or change external services | | |
| Access production or sensitive data | | |
| Send external communications or create external records | | |
| Incur cloud, API or other costs | | |

Use unambiguous values such as **Allowed**, **Allowed only with explicit authorization**, **Human only** or **Prohibited**. Do not leave consequential permissions blank. Tool availability does not grant permission.

## 7. Risks, invariants and safeguards

- **Security / threat exposure:**
- **Privacy / personal-data handling:**
- **Safeguarding / vulnerable users:**
- **Legal / contractual review required:**
- **Reliability / data-integrity / recovery:**
- **Compatibility / migration / dependency:**
- **Cost / operational burden:**
- **Project invariants that must remain true:**
- **Required reviewers and approvals:**

## 8. Stop, escalation and rollback conditions

Stop and escalate when:
- The baseline or source-of-truth owner is unclear.
- A required decision or gate is unresolved.
- The task would exceed the authorized scope or permissions.
- A critical security, privacy, safeguarding, legal or data-integrity issue is found.
- Required evidence is unavailable, contradictory or materially weaker than expected.
- A test fails unexpectedly or a destructive/external side effect is possible.

**Rollback / containment approach:**

**Who must be notified and who can authorize resumption:**

## 9. Execution log

Record material actions as they occur. Preserve exact command lines and outcomes where commands are run.

| Date/time | Action / command | Artifact, run or commit identity | Outcome / notes |
|---|---|---|---|
| | | | |

## 10. Closeout and decision

- **Outcome:** Complete / Incomplete / Blocked / Superseded / Cancelled
- **Acceptance criteria met:** Yes / No / Partially
- **Files, systems or decisions changed:**
- **Final branch / ref and full commit SHA (if applicable):**
- **Diff reviewed:** Yes / No / Not applicable
- **Commands actually run and results:**
- **Checks not run and why:**
- **Runtime / user / domain validation:**
- **Failures, contradictions and unresolved unknowns:**
- **Residual risks and rollback status:**
- **Gate decision, decision owner and date:**
- **Reusable lesson / defect record created:**
- **Smallest useful next action:**

A task is not complete merely because work was performed. Close it only against the agreed criteria, evidence and required authority. State incomplete or blocked work honestly.

## 11. Proportionate use

This template is for material work, consequential decisions, external research, agent tasks and changes that need handover or auditability. For a small, reversible task, use the short form below or record the necessary details in the existing task system. Do not create paperwork that adds no decision value.

### Short form for a low-risk task

- **Purpose / outcome:**
- **Baseline:**
- **Scope / exclusions:**
- **Acceptance proof:**
- **Permissions / authority:**
- **Stop condition:**
- **Closeout / next action:**
