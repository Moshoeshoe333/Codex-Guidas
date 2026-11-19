# Codex-Guidas Defect Intelligence System

**Status:** Proposed operating mechanism — ready for controlled manual use.  
**Version:** 0.1  
**Owner:** Project maintainers  
**Last reviewed:** 2026-11-18

## 1. Purpose

Turn defects, near misses, confusing test failures and operational surprises into reusable engineering knowledge. The system should reduce repeat failures and shorten diagnosis without becoming a bureaucracy or an autonomous authority to change production code.

It is a learning and traceability mechanism, not a guarantee of defect-free software.

## 2. Operating loop

`DETECT → CONTAIN → RECORD → TRIAGE → SEARCH → HYPOTHESIZE → FIX → VERIFY → LEARN → CLOSE`

1. **Detect:** preserve the first reliable signal (test output, log, user report, monitoring event or reproducible observation).
2. **Contain:** protect users/data and stop unsafe progression where needed. Follow the owning project's incident process.
3. **Record:** create a defect ID and capture exact source boundary.
4. **Triage:** assess impact, severity, scope, exploitability and urgency.
5. **Search:** search this repository's lesson ledger and prior defect records for similar symptoms, causes and controls.
6. **Hypothesize:** separate observed facts from suspected root causes. Keep multiple hypotheses when evidence is ambiguous.
7. **Fix:** make the smallest authorized change that addresses the demonstrated cause.
8. **Verify:** run targeted regression tests and relevant wider checks. Record exact command, environment, commit and outcome.
9. **Learn:** update the defect record and, only when reusable, add or revise a cross-project lesson.
10. **Close:** close only when acceptance criteria are met and residual risk is explicit. Otherwise leave open, mitigated or blocked.

## 3. Defect record identity

Use IDs `DEF-YYYY-NNN` (for example, `DEF-2026-001`). IDs are unique within this knowledge base. Do not reuse IDs after closure or withdrawal.

A defect record must link to:
- owning repository and affected branch/ref;
- exact affected commit SHA (or explicitly say unknown);
- issue, PR, CI run, log or user report where available;
- the lesson IDs searched or applied;
- corrective change commit and regression evidence, when available.

Do not paste secrets, personal data, access tokens, private player information or sensitive incident details into this repository. Redact and link to access-controlled evidence where appropriate.

## 4. Severity and priority

Use impact-based severity, not emotional language or the number of files changed. The canonical S0–S4 definitions are maintained in [record taxonomy](../00-foundation/record-taxonomy.md); do not redefine them in individual packs or registers.

Severity may change as evidence develops. Record who changed it, when and why. A security or safeguarding concern should be escalated under the relevant project policy even if its immediate user impact is not yet known.

## 5. State model

The canonical defect workflow states and meanings are maintained in [record taxonomy](../00-foundation/record-taxonomy.md). Do not use “fixed” as a synonym for “closed.” Code can be changed while verification remains pending.

## 6. Evidence and root-cause discipline

Every record separates:

- **Observed facts:** directly supported by logs, source, reproduction or testimony.
- **Impact:** demonstrated effect; distinguish actual impact from plausible worst case.
- **Hypotheses:** possible explanations with confidence and evidence for/against.
- **Confirmed cause:** only when a discriminating test, trace or code-path analysis supports it.
- **Unknowns:** facts still missing.

A symptom is not a root cause. Temporal correlation is not proof of causation. A green test does not prove an untested path safe.

## 7. Similarity search

Before proposing a fix, search:
1. the lessons ledger by symptom, component and failure mode;
2. this defect register for prior records;
3. the owning repository's issues, commits, tests and incident notes;
4. related projects only for transferable principles, not presumed identical causes.

Record the search terms and matching IDs. If no match is found, record that too. A match is a lead, not proof.

## 8. Fix and verification contract

A corrective change should state:
- expected behaviour and violated invariant;
- smallest affected boundary;
- files/components to change and why;
- tests to add or update;
- compatibility, migration and rollback implications;
- security/privacy/safeguarding implications;
- acceptance criteria.

Verification must record exact repository, branch, full commit SHA, command, environment/dependency versions, test scope, result and evidence link. Distinguish static checks, unit tests, integration tests, browser workflows, builds, installation, device/runtime execution and user validation.

Never transfer a successful result to a different commit without an explicit evidence rule and re-verification.

## 9. Learning promotion

Promote a defect into the cross-project lesson ledger only when it has a reusable principle or control.

- One-off project-specific correction: keep it in the project defect record.
- Reusable but not yet proven control: lesson status **Proposed** or **Derived**.
- Reproducibly demonstrated control: may be **Verified**, with exact evidence.
- Contradicted or replaced control: mark **Superseded**, preserving history.

Do not create a new lesson for every defect. Prefer linking to an existing lesson and improving its evidence.

## 10. Automation boundaries

Automation may:
- collect CI metadata and logs;
- detect recurring error signatures;
- suggest similar lessons and prior defects;
- draft a defect record;
- remind maintainers of missing evidence fields.

Automation must not, without explicit authorized review:
- change severity or close a safety/security incident;
- promote a lesson to Verified;
- modify production policy or security controls;
- bypass project decision gates;
- merge code, change access or deploy a fix.

Model-generated similarity and root-cause suggestions are hypotheses only. Human maintainers remain accountable for triage, authorization and closure.

## 11. Minimal operational metrics

Review monthly or at a meaningful release boundary:
- new defects by severity;
- open and reopened defects;
- median time to contain S0/S1 issues;
- recurrence rate for known failure modes;
- percentage of closed defects with regression evidence;
- defects with unknown root cause;
- lessons reused by more than one project.

Do not optimize for fewer reported defects. A rise in recorded defects may reflect better detection. Interpret trends alongside exposure, usage and reporting quality.

## 12. Definition of done

A defect is eligible for closure only when:
- the observed failure and impact are described;
- the fix is authorized and linked to an exact commit;
- acceptance criteria pass at the relevant evidence level;
- regression coverage exists where practical, or the reason it cannot be added is documented;
- security/safeguarding and data-integrity implications are reviewed where relevant;
- residual risks and follow-up work are explicit;
- the owning project's authority approves closure.

## 13. First implementation boundary

Start with manual Markdown records and search. Do not build a database, bot, dashboard or cross-repository automation until repeated usage demonstrates a real bottleneck. The first proof is whether the process helps us find and prevent a repeated defect with less time and better evidence.


## 14. Structured retrieval

Individual records carry machine-readable frontmatter. The metadata schema defines fields; record taxonomy is the canonical lifecycle/severity vocabulary. Use the repository search before triage and the review queue during monthly maintenance. Search results are suggestions only; maintainers inspect evidence and determine whether causes are genuinely equivalent.
