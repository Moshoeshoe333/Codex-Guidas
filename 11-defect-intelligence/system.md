# Codex-Guidas Defect Intelligence System

**Status:** Proposed operating mechanism — controlled manual use; not an autonomous incident system.  
**Version:** 0.3  
**Owner:** Project maintainers  
**Last reviewed:** 2026-11-19

## 1. Purpose and boundaries

Turn defects, near misses, confusing test failures and operational surprises into reusable engineering knowledge. The system should reduce repeat failures and shorten diagnosis without becoming bureaucracy or an autonomous authority to change production code.

It is a learning and traceability mechanism, not a guarantee of defect-free software. The [methodology–knowledge architecture](../docs/methodology-knowledge-architecture.md) defines how retrieval, evidence and owning-project authority interact.

**Authority rule:** A DEF record does not authorize a fix. The owning project controls implementation, release, severity acceptance and closure. Codex-Guidas maintainers curate the knowledge record; they do not acquire authority over another project's code or risk.

## 2. Operating loop

`DETECT → CONTAIN → RECORD → TRIAGE → SEARCH → HYPOTHESIZE → FIX → VERIFY → LEARN → CLOSE`

The stages describe work, not a rigid serial queue. For an urgent S0/S1 signal, containment and recording may proceed in parallel. Do not delay immediate risk reduction to complete paperwork.

| Stage | Required practice | Exit condition |
|---|---|---|
| **DETECT** | Preserve the earliest trustworthy signal: exact test output, log, report, monitoring event or reproducible observation. Record repository, branch/ref, full commit SHA (or Unknown), environment, command/procedure, timestamp and original signature. Classify the signal as deterministic, intermittent, environment-specific, user-reported or source-observed. | A durable signal note exists and another investigator could attempt reproduction. |
| **CONTAIN** | Follow the owning project's incident process for S0/S1. Prefer reversible, bounded actions. Record what changed, what remains exposed, who accepted any residual exposure, and a review/expiry trigger. Containment is not a root-cause fix. | Immediate risk is reduced, or residual exposure and accountable owner are explicit. |
| **RECORD** | Allocate a unique DEF ID; create the record; preserve facts before interpretation. Fill known fields and write Unknown where evidence is absent. Link the register, exact source artifacts and evidence IDs. | The DEF is discoverable from the register and contains at least one evidence entry or an explicit explanation that evidence is not yet available. |
| **TRIAGE** | Assess actual impact separately from plausible worst case; determine scope, urgency, exploitability, data-integrity and safeguarding implications. Assign an owner and next action. Severity may be provisional and must include rationale. | State, severity/rationale, owner, next action and time horizon are recorded. |
| **SEARCH** | Search the lesson ledger, prior DEFs, owning-project issues/commits/tests/incidents, then related projects for transferable principles only. Record exact terms, IDs considered, matches/no match and why a candidate is or is not the same cause. | Search terms and results are written into the DEF. A match remains a lead, not proof. |
| **HYPOTHESIZE** | List observations first. Keep plausible explanations separate, with confidence, supporting evidence, contradicting evidence and a discriminating test for each material hypothesis. | At least one testable hypothesis and its next discriminating check are recorded; otherwise state why investigation is blocked. |
| **FIX** | Define expected behaviour, violated invariant, smallest boundary, exact files/components, tests, compatibility/migration/rollback, security/privacy/safeguarding implications and acceptance criteria. Obtain the owning project's normal authorization before implementation. | An authorized change is linked, or a documented decision defers/rejects the fix and names the risk owner. |
| **VERIFY** | Verify the exact corrected repository, branch, full commit, command, environment/dependency versions, test scope, result and evidence. State what was not tested. Distinguish static, unit, integration, browser, build, install, device/runtime and user evidence. | Acceptance criteria pass at the relevant evidence level, or remaining failures/limits are explicit. |
| **LEARN** | Decide whether the finding is project-specific or reusable. Prefer updating an existing CG lesson. If a lesson is created/updated from a DEF, link DEF → CG and CG → DEF. Record applicability limits and uncertainty. | A linked lesson change exists, or the DEF explicitly records why no cross-project lesson is warranted. |
| **CLOSE** | Check closure criteria, regression evidence, residual risks and security/safeguarding/data-integrity review where relevant. The owning-project authority approves closure or explicitly accepts the residual risk. | The decision, approver, evidence and residual risk are recorded. Otherwise remain open, contained or blocked. |

### 2.1 DETECT: preserve the signal

Do not clean, normalize or replace failed output before preserving it. Keep raw evidence in an appropriate access-controlled location when it contains sensitive data; store a redacted reference in this repository. A source-inspection finding is **SOURCE-OBSERVED**, not reproduced. A mock-backed test is mock-backed evidence, not native-device or production evidence.

### 2.2 CONTAIN: state the boundary

Record:
- containment action and start time;
- affected feature/data/users and known remaining exposure;
- reversibility and rollback path;
- accountable owner;
- review/expiry date or event trigger.

If no safe containment is available, say so and keep the defect Investigating or Blocked with the residual exposure visible. Do not mark Contained merely because a warning was written.

### 2.3 TRIAGE: severity is not certainty

Use the canonical S0–S4 taxonomy. Severity represents impact; urgency and confidence are separate judgements. If impact is unknown, state the uncertainty and escalate plausible security/safeguarding exposure under the owning project's policy. Record every severity change with date, decision owner and reason.

### 2.4 SEARCH: mandatory before a material fix

Use this order:
1. Codex-Guidas lesson records by symptom, component and failure mode.
2. Codex-Guidas defect register and individual DEF records.
3. Owning repository's issues, commits, tests, CI runs and incident notes.
4. Related projects for transferable principles only.

Record search terms and candidate IDs even when there is no match. Search is not a causal conclusion; similarity does not establish a common root cause.

### 2.5 HYPOTHESIZE: demand a discriminating test

For each material hypothesis record:
- confidence as a qualitative working judgement, not a probability unless calibrated;
- evidence supporting and contradicting it;
- the smallest test/inspection that distinguishes it from alternatives;
- expected observations under each alternative.

Do not confirm a cause from timing, correlation, a single plausible code path or a test that does not distinguish competing explanations.

### 2.6 FIX and VERIFY: preserve authorization and exactness

A DEF is not a change request approval. No implementation may cross an unresolved owning-project decision gate. Verification belongs to the exact changed commit; a green PR head does not automatically verify a different merge commit or release artifact.

A test proves only the cases, environment and conditions exercised. Preserve failed tests and negative evidence after a correction.

### 2.7 LEARN: promotion checklist

Before creating or updating a CG lesson, answer:
- Is there a reusable principle or control beyond this one project?
- Is the control demonstrated, merely proposed, or only inferred?
- What exact evidence supports the lesson's status?
- Does an existing CG lesson already cover the principle?
- What are the applicability boundaries and known counterexamples?
- Is the DEF linked to the CG lesson and the CG lesson linked back to the DEF?
- If no lesson is warranted, is that decision recorded in the DEF?

One-off project corrections remain in the DEF. Reusable but unproven controls remain Proposed or Derived as appropriate. Verified is permitted only when the stated control was reproduced against explicit criteria on an exact revision and environment. The validator requires Evidence ledger references and named author, auditor and ratifier fields; it distinguishes limited self-review from independent review. See the promotion and assurance rules in record-taxonomy.md. Do not create a new lesson for every defect.

### 2.8 CLOSE: definition of done

Closure requires:
- observed signal and impact (or lack of demonstrated impact) described;
- authorized corrective change linked to an exact commit, or an explicit won't-fix decision by the proper authority;
- relevant acceptance criteria and regression evidence recorded;
- untested surfaces and residual risks stated;
- security, privacy, safeguarding and data-integrity implications reviewed where relevant;
- reusable-lesson decision recorded;
- owning-project authority and closure rationale named.

A closed record may retain residual risk only when the owner explicitly accepts it. Reopen on recurrence, failed acceptance criteria or new evidence that invalidates the prior conclusion. Use **Superseded** only when a newer record replaces the historical one and the link/reason is preserved.

## 3. State model

Canonical states are defined in [record-taxonomy.md](../00-foundation/record-taxonomy.md): New, Triaged, Investigating, Contained, Fix proposed, In verification, Closed, Blocked, Won't fix and Reopened.

These are not a mandatory linear sequence:
- New normally proceeds to Triaged, then Investigating.
- Containment may occur at any active stage; it does not imply root cause or fix.
- Blocked may be entered from any active stage when access, evidence or an external decision is missing.
- Fix proposed precedes In verification when a change exists and awaits evidence.
- Closed requires the closure criteria above.
- Reopened requires a recurrence or new evidence that invalidates closure.

Do not invent additional states in individual records. Record finer-grained evidence labels such as SOURCE-OBSERVED, REPRODUCED, FIXED-UNVERIFIED or MOCK-BACKED as evidence annotations, not competing lifecycle states.

## 4. Defect identity and evidence safety

Use IDs `DEF-YYYY-NNN`. IDs are unique and never reused. Every material claim should point to an Evidence ID in the record's evidence ledger. Each evidence entry identifies source, exact ref, observation, date/context and limitation.

A record should link to the owning repository, affected branch/ref, full commit SHA (or Unknown), issue/PR/CI/log where available, searched/applied CG lessons, corrective change and regression evidence when available.

Do not place secrets, credentials, raw personal data, private player information or sensitive safeguarding details in this repository. Redact and link to access-controlled evidence where appropriate.

## 5. Severity and priority

Use impact-based severity from the canonical taxonomy. Severity may change as evidence develops; record who changed it, when and why. Severity is not a confidence score or a priority queue by itself. Security and safeguarding concerns may require escalation before impact is fully known.

## 6. Automation boundaries

Automation may:
- collect CI metadata and logs;
- validate record structure, links and ID uniqueness;
- generate a searchable index;
- suggest similar lessons/DEFs and draft records;
- surface missing evidence, overdue reviews and stale Investigating records;
- calculate descriptive metrics from explicitly defined records.

Automation must not:
- confirm root cause from similarity;
- change severity or close safety/security items;
- accept residual risk;
- promote a lesson to Verified;
- modify production policy, merge code, change access or deploy a fix;
- bypass an owning-project decision gate.

Prediction and similarity outputs are hypotheses/prioritisation signals only. Human review remains responsible for interpretation, severity, containment and closure.

## 7. Measures: learning, not volume

At monthly or release boundaries, consider:
- new defects by severity and evidence class;
- open, blocked and reopened counts;
- time to contain S0/S1 (only where timestamps are reliable);
- recurrence of known failure modes;
- closed defects with exact-commit regression evidence / eligible closures;
- defects with unknown root cause;
- closed DEFs that updated or created a CG lesson;
- lessons applied by more than one project with receiving-project evidence.

State numerator, denominator, source, sample size and limitations. More recorded defects may indicate better detection, not worsening quality. Do not claim defect reduction or ROI from record counts alone.

## 8. Governing references

- [Canonical record taxonomy](../00-foundation/record-taxonomy.md)
- [Structured metadata schema](../00-foundation/metadata-schema.md)
- [Methodology–knowledge architecture](../docs/methodology-knowledge-architecture.md)
- [Defect record template](defect-template.md)
- [Knowledge-application record template](../09-templates/knowledge-application-record.md)
