---
id: "DEF-YYYY-NNN"
record_type: "defect"
status: "New"
projects: []
layer: "unknown"
component: null
failure_mode: null
severity: null
origin_date: null
last_reviewed: null
verification_due: null
evidence_class: "Reported"
verification_status: "not-claimed"
source_path: "Unknown"
review_scope: "intake only; state what was and was not reviewed"
---

# DEF-YYYY-NNN — [Short factual title]

**Current loop stage:** DETECT / CONTAIN / RECORD / TRIAGE / SEARCH / HYPOTHESIZE / FIX / VERIFY / LEARN / CLOSE  
**Record maturity:** Intake / Investigating / Evidence-complete / Closure review

## Loop-stage checklist
- [ ] DETECT — preserve original signal and reproduction context
- [ ] CONTAIN — record action or explicitly state no containment / not required
- [ ] RECORD — allocate ID, link register and create evidence entry
- [ ] TRIAGE — severity/rationale, scope, owner and next action
- [ ] SEARCH — terms, lesson IDs, DEF IDs and no-match result
- [ ] HYPOTHESIZE — facts, competing explanations and discriminating test
- [ ] FIX — owning-project authorization and smallest-change contract
- [ ] VERIFY — exact commit, command, environment, results and untested scope
- [ ] LEARN — promotion decision and bidirectional links, or reason not warranted
- [ ] CLOSE — acceptance criteria, residual risk and owner approval

- **State:** See frontmatter and [canonical taxonomy](../00-foundation/record-taxonomy.md).
- **Severity:** S0 / S1 / S2 / S3 / S4; provisional until triage evidence supports it.
- **Date detected:**
- **Date recorded:**
- **Last updated:**
- **Owning project/repository:**
- **Affected branch/ref:**
- **Affected full commit SHA:** Unknown / [SHA]
- **Environment and command/procedure:**
- **Owner / next-action owner:**
- **Next action and review horizon:**
- **Related issue/PR/CI run/log:**
- **Related lessons:** CG-XXX / none found
- **Reporter/source:** [Avoid personal or sensitive data]

## 1. Summary
One or two factual sentences describing the signal, without turning a hypothesis into a fact.

## 2. Expected behaviour
What should have happened? Link the requirement, invariant or decision.

## 3. Observed behaviour and reproduction
- Original signature / raw evidence location:
- Reproduction steps:
- Signal class: deterministic / intermittent / environment-specific / user-reported / SOURCE-OBSERVED / other
- Reproduction result and exact conditions:
- What has not been reproduced:

Preserve the earliest reliable failure output. Redact sensitive material and link to restricted evidence rather than copying it here.

## 4. Containment
- Action and start time:
- What risk was reduced:
- Remaining exposure:
- Reversibility / rollback:
- Accountable owner:
- Review/expiry date or event trigger:
- If not contained, why and who owns the residual exposure:

Containment is not a fix and does not confirm root cause.

## 5. Impact and triage
- Actual demonstrated impact:
- Potential impact (clearly labelled):
- Affected users/data/components:
- Scope: known / unknown, with rationale:
- Security / privacy / safeguarding / integrity implications:
- Severity and rationale:
- Severity history (date, prior → new, decision owner, reason):
- Owner:
- Next concrete action and expected time horizon:

## 6. Evidence ledger
| Evidence ID | Type | Exact ref (commit/run/log/report) | Date/context | Observation | Limitation |
|---|---|---|---|---|---|
| E-001 | Source / test / CI / runtime / report | | | | |

Every material claim should cite an Evidence ID. If no artifact is available yet, state that and identify the next evidence to collect.

## 7. Similarity search
- Search date:
- Search terms used:
- Lesson IDs searched:
- Prior DEF IDs searched:
- Owning-project issues/commits/tests searched:
- Related projects consulted (principle only):
- Matches / explicit no-match:
- Why each candidate is or is not the same cause:
- Candidate controls to investigate:

A match is a lead, not proof of a shared root cause. Do not omit the search because no match was found.

## 8. Root-cause hypotheses
| Hypothesis | Confidence (qualitative) | Supporting evidence IDs | Contradicting evidence IDs | Discriminating test and expected outcomes | Status |
|---|---|---|---|---|---|
| H-01 | Low / Medium / High (working judgement only) | | | | Open / supported / rejected |

- **Confirmed cause:** Unknown until discriminating evidence supports it.
- **Next discriminating test:** [Specific test or inspection]
- **Why this test distinguishes alternatives:** [Explain]

Do not confirm a cause from temporal correlation, one plausible code path or a test that does not distinguish alternatives.

## 9. Corrective action contract
- Expected behaviour and violated invariant:
- Smallest affected boundary:
- Exact files/components and rationale:
- Owning-project authorization / decision reference:
- Tests to add or update:
- Compatibility / migration / rollback implications:
- Security / privacy / safeguarding implications:
- Acceptance criteria:
- Change PR / commit (when authorized):

A DEF record does not itself authorize implementation.

## 10. Regression and acceptance evidence
| Check | Command / procedure | Environment / dependency versions | Exact commit | Expected | Actual | Evidence link | Not tested |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

Distinguish static inspection, unit, integration, browser, build, install, device/runtime and user evidence. A result applies only to its recorded commit and conditions.

## 11. Residual risk and follow-up
- Remaining unknowns:
- Residual exposure:
- Accepted by / authority (or Unknown):
- Deferred work:
- Follow-up owner:
- Due date / review trigger:

## 12. Learning promotion decision
- Reusable principle/control beyond this project? Yes / No / Unclear
- Existing CG lesson to update: CG-XXX / none
- New CG lesson proposed: CG-XXX / none
- Evidence level and exact supporting Evidence IDs:
- Applicability boundaries / counterexamples:
- DEF → CG link:
- CG → DEF reciprocal link:
- If no lesson is warranted, explain why:

Prefer updating an existing lesson. One-off corrections stay in this DEF. Proposed/Derived status is not Verified status.

## 13. Closure decision
- **Decision:** Keep open / Contained / Closed / Won't fix / Reopened
- **Approver / owning-project authority:**
- **Acceptance criteria met:**
- **Regression evidence and exact commit:**
- **Security / safeguarding / integrity review:**
- **Residual risk explicitly accepted:**
- **Reason and closure evidence:**
- **Reopen trigger:**

Closure requires owning-project approval. If criteria are not met, keep the record open or blocked.

## Intake minimum

At first capture, complete only what is known: ID/title, state, provisional severity, owning project and affected ref (or Unknown), one-sentence observation, one evidence entry or explicit evidence gap, and residual-risk statement. Expand the record as investigation proceeds; do not invent missing details.

Before submitting, run `python scripts/codex.py validate`. A clean validator confirms structure and links, not root-cause truth or closure authority.
