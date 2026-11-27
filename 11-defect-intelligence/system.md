# Codex-Guidas Defect Intelligence System

**Status:** Proposed operating mechanism — ready for controlled manual use.  
**Version:** 0.2  
**Owner:** Project maintainers  
**Last reviewed:** 2026-11-27

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

## 4. Evidence propagation and record synchronization

Keep three record roles distinct:

- **Detailed DEF record:** canonical current state, evidence ledger, open questions, corrective action and closure decision for one defect.
- **Defect README register:** concise navigation/index view. Its state, severity and evidence summary must agree with the detailed DEF record.
- **Defect ledger:** chronological and cross-project learning context. A later follow-up entry supplements the detailed record; it does not replace updating the canonical record and index.

When a material evidence event occurs (new reproduction, CI run, source revalidation, correction, owner decision or closure):

1. Verify the upstream source or run directly where access permits. Capture the exact repository, branch, full tested commit, run ID, result and limitations.
2. Re-check the receiving project's current branch head. State clearly when evidence comes from an ancestor or older revision.
3. Update the detailed DEF record with the new evidence and its limits. Preserve what was known at earlier dates; add a dated follow-up rather than silently rewriting history.
4. Update the README register summary and state in the same change.
5. Append a dated ledger note or link to the relevant evidence when chronology or cross-project learning warrants it.
6. Inspect all affected references and commit the coherent update atomically where practical.

Do not let a historical statement such as "not run" remain unqualified as a current status after a later run exists. Conversely, do not infer that every planned probe passed because one targeted test suite passed. Keep evidence scope precise.

If evidence cannot be independently rechecked, label it as reported or source-recorded rather than independently verified. If the source record and index disagree, flag the inconsistency and resolve it before relying on the status.

## 5. Severity and priority

Use impact-based severity, not emotional language or the number of files changed.

| Severity | Meaning | Typical response |
|---|---|---|
| **S0 Critical** | Active exploitation, material data loss/corruption, severe safety risk, or broad service compromise | Contain immediately; invoke owner incident process; no routine release until controlled |
| **S1 High** | Major workflow unavailable, significant security/privacy exposure, unsafe access path, or integrity failure | Prioritised fix and explicit release decision |
| **S2 Moderate** | Important function impaired with workaround; limited scope or recoverable data issue | Schedule promptly; test workaround and fix |
| **S3 Low** | Minor defect with low impact and safe workaround | Backlog and fix when justified |
| **S4 Observation** | Near miss, quality concern or improvement opportunity without demonstrated user impact | Record if reusable; avoid inflating defect counts |

Severity may change as evidence develops. Record who changed it, when and why. A security or safeguarding concern should be escalated under the relevant project policy even if its immediate user impact is not yet known.

## 6. State model

- **New:** recorded, not yet triaged.
- **Triaged:** impact and owner assessed.
- **Investigating:** evidence collection and hypotheses in progress.
- **Contained:** immediate risk reduced; root cause may remain open.
- **Fix proposed:** corrective change identified, not yet verified.
- **In verification:** fix exists and tests/evidence are being evaluated.
- **Closed:** acceptance criteria passed and residual risk accepted by the proper owner.
- **Blocked:** progress depends on an external decision, access or prerequisite.
- **Won't fix:** explicit rationale and authorized acceptance of residual risk.
- **Reopened:** recurrence or failed acceptance criteria after closure.

Do not use “fixed” as a synonym for “closed.” Code can be changed while verification remains pending.

## 7. Evidence and root-cause discipline

Every record separates:

- **Observed facts:** directly supported by logs, source, reproduction or testimony.
- **Impact:** demonstrated effect; distinguish actual impact from plausible worst case.
- **Hypotheses:** possible explanations with confidence and evidence for/against.
- **Confirmed cause:** only when a discriminating test, trace or code-path analysis supports it.
- **Unknowns:** facts still missing.

A symptom is not a root cause. Temporal correlation is not proof of causation. A green test does not prove an untested path safe.

## 8. Similarity search

Before proposing a fix, search:
1. the lessons ledger by symptom, component and failure mode;
2. this defect register for prior records;
3. the owning repository's issues, commits, tests and incident notes;
4. related projects only for transferable principles, not presumed identical causes.

Record the search terms and matching IDs. If no match is found, record that too. A match is a lead, not proof.

## 9. Fix and verification contract

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

## 10. Learning promotion

Promote a defect into the cross-project lesson ledger only when it has a reusable principle or control.

- One-off project-specific correction: keep it in the project defect record.
- Reusable but not yet proven control: lesson status **Proposed** or **Derived**.
- Reproducibly demonstrated control: may be **Verified**, with exact evidence.
- Contradicted or replaced control: mark **Superseded**, preserving history.

Do not create a new lesson for every defect. Prefer linking to an existing lesson and improving its evidence.

## 11. Automation boundaries

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

## 12. Minimal operational metrics

Review monthly or at a meaningful release boundary:
- new defects by severity;
- open and reopened defects;
- median time to contain S0/S1 issues;
- recurrence rate for known failure modes;
- percentage of closed defects with regression evidence;
- defects with unknown root cause;
- lessons reused by more than one project.

Do not optimize for fewer reported defects. A rise in recorded defects may reflect better detection. Interpret trends alongside exposure, usage and reporting quality.

## 13. Definition of done

A defect is eligible for closure only when:
- the observed failure and impact are described;
- the fix is authorized and linked to an exact commit;
- acceptance criteria pass at the relevant evidence level;
- regression coverage exists where practical, or the reason it cannot be added is documented;
- security/safeguarding and data-integrity implications are reviewed where relevant;
- residual risks and follow-up work are explicit;
- the owning project's authority approves closure.

## 14. First implementation boundary

Start with manual Markdown records and search. Do not build a database, bot, dashboard or cross-repository automation until repeated usage demonstrates a real bottleneck. The first proof is whether the process helps us find and prevent a repeated defect with less time and better evidence.
