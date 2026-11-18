# Framework Assessment Record (FAR)

**Template ID:** CG-TPL-FAR-001  
**Version:** 0.1  
**Status:** Proposed reusable template — not ratified or validated  
**Owner:** Assessment lead / project owner  
**Canonical home:** Codex-Guidas / 09-templates  
**Use:** Record a bounded assessment using Tri-Tier 33, the 33-Perspective framework, or both as distinct instruments.

> **Evidence before verdict. Verdict before recommendation. Recommendation is not authorisation.**
>
> This template does not certify security, privacy, legal compliance, safety, quality or release readiness. It does not grant permission to inspect systems, access data, run tests or conduct active testing.

---

## A. Assessment identity and control

| Field | Record |
|---|---|
| Assessment ID | FAR-YYYY-NNN |
| Title | |
| Status | Draft / In Review / Final / Superseded |
| Assessment lead | |
| Project owner / accountable decision owner | |
| Reviewers and roles | |
| Independent reviewer? | Yes / No / Not available — explain |
| Conflicts of interest | |
| Created / updated dates | |
| Intended audience | |
| Intended use | |
| Confidentiality / handling label | |
| Related decision IDs | |
| Related defect / risk / claim IDs | |

## B. Question and decision contract

**Primary question:**  
[What precise question must this assessment answer?]

**Decision to be informed:**  
[What decision may the assessment inform? Do not imply the assessment itself makes the decision.]

**Decision owner:**  
[Name/role with actual authority.]

**As-of date and time / timezone:**  

**Scope:**  
[Repositories, products, components, workflows, users, data classes, environments, jurisdictions and versions included.]

**Explicit exclusions:**  
[What is not assessed and why?]

**Required comparisons / baseline:**  
[Previous commit, target architecture, policy, control requirement, expected behaviour or other comparator.]

**Must-resolve questions:**  
[List questions that block a reliable recommendation.]

**Source rules:**  
[Primary sources, permitted access, evidence freshness, independence, data restrictions.]

**Stop conditions:**  
[Unauthorised access, sensitive data exposure, unexpected production impact, scope drift, missing permission, safety concern, or other stop trigger.]

**Assessment depth and rationale:**  
[Routine / Material / High consequence / Strategic, or project-defined equivalent. This is a planning label, not a calibrated risk score.]

## C. Permission and safety boundary

| Check | Status | Evidence / owner / notes |
|---|---|---|
| Authority to inspect the named repositories/assets confirmed | Confirmed / Not confirmed / N/A | |
| Written authorisation required? | Yes / No / Unknown | |
| Written authorisation recorded and in scope? | Yes / No / N/A | |
| Production access required? | Yes / No | |
| Personal or sensitive data expected? | Yes / No / Unknown | |
| Data minimisation and handling controls defined? | Yes / No / N/A | |
| Minors / vulnerable users / community safeguarding relevant? | Yes / No / Unknown | |
| Legal, contractual or regulatory review needed? | Yes / No / Unknown | |
| Active testing explicitly authorised? | Yes / No / N/A | |
| Stop contact and escalation path defined? | Yes / No | |

**Gate rule:** If required authority is absent or unclear, do not proceed with the relevant access or test. If proceeding could create material harm, privacy exposure or unauthorised impact, classify the assessment as **HOLD — permission or safeguard unresolved**.

## D. Framework selection

Select only the instrument(s) relevant to the question. Keep their results separate.

| Instrument | Selected? | Version / source commit | Why selected | Limitations |
|---|---|---|---|---|
| Tri-Tier 33 technical assessment | Yes / No | | | |
| 33-Perspective multidisciplinary review | Yes / No | | | |
| Other project-specific review | Yes / No | | | |

**Framework distinction:**
- **Tri-Tier 33:** Mind (codebase), Body (persistence), Spirit (user interface) and Harmony seams. Use its exact tier IDs, dispositions and verdict vocabulary from the source version assessed.
- **33-Perspective:** multidisciplinary challenge across need/context/legitimacy; design/evidence/operational integrity; sustainability/impact/resilience. Use the exact perspective definitions from the source version assessed.
- Do not merge the two instruments into one score, substitute one for the other, or imply either is certification.

## E. Assessed source baseline

| Field | Record |
|---|---|
| Repository / system name | |
| Canonical repository URL | |
| Visibility / access limitation | |
| Branch / tag | |
| Exact commit SHA / immutable version | |
| Working tree state, if known | Clean / Dirty / Unknown / N/A |
| Source files and line ranges | |
| Build / release artifact identifier | |
| Environment / OS / runtime / device | |
| Configuration / feature flags | |
| Data set / fixture / sample and origin | |
| Test run / CI workflow / execution ID | |
| Assessment start and end | |
| Source retrieval date | |
| Reproduction instructions | |

If the exact assessed commit or equivalent immutable state cannot be established, record that limitation prominently. Do not describe the result as a reproducible assessment of the current project.

## F. Evidence register

Create one row per evidence item. Give each item a stable ID (for example, FAR-YYYY-NNN-E001).

| Evidence ID | Claim ID supported | Source / exact locator | Evidence class | Date / environment | Method / observer | Result | Limitations / counter-evidence |
|---|---|---|---|---|---|---|---|
| | | | Observed / Derived / Proposed / Verified / Unknown / Superseded | | | | |

**Evidence handling rules**
1. Separate the source observation from interpretation and conclusion.
2. Preserve original source, exact commit, file/line, test log, screenshot or measurement where applicable.
3. Record publication date separately from event date and retrieval date.
4. Group copied or syndicated reports under their common upstream source; copies are not independent corroboration.
5. Record contradictory and negative evidence; do not discard it because it complicates the conclusion.
6. A test result supports only the tested cases, configuration, version and environment.
7. Mark AI-generated summaries or suggestions as secondary analysis until checked against primary evidence.
8. Do not include passwords, PINs, OTPs, private keys, unnecessary personal data or unredacted victim information in the record.

## G. Findings register

Use one row per finding. Give each a stable ID (for example, FAR-YYYY-NNN-F001).

| Finding ID | Severity / rationale | Claim or requirement | Observation | Interpretation / root-cause confidence | Evidence IDs | Counter-evidence / unknowns | Owner |
|---|---|---|---|---|---|---|---|
| | | | | Confirmed / Probable / Possible / Unknown | | | |

**Finding status:** Open / Accepted risk / Corrected — pending verification / Verified closed / Deferred / Rejected with rationale.

Do not state a root cause as confirmed unless evidence distinguishes it from plausible alternatives.

## H. Tri-Tier 33 module — complete only if selected

**Framework source/version:**  
**Source repository and exact commit:**  
**Assessment profile/depth:**  
**Tier definitions source:**  

For every tier considered, create a passport record:

| Tier ID | Exact tier question / definition | Disposition | Component / scope | Claim | Evidence IDs | Verdict | Gap / counter-evidence | Next verification / owner |
|---|---|---|---|---|---|---|---|---|
| C-xx / D-xx / U-xx | | Applicable / Not applicable (reason) / Not assessed | | | | SOLID / SOFT / OPEN / GHOST | | |

**Tri-Tier verdict meanings (use the source framework's current definitions):**
- **SOLID:** bounded claim supported by current, applicable and reproducible evidence; no unresolved material contradiction is known.
- **SOFT:** partial evidence exists, but coverage, freshness, scope or conditions limit the claim.
- **OPEN:** evidence is missing, insufficient, stale or a material question remains unresolved.
- **GHOST:** a current authoritative claim says an artifact/control exists or is active, but inspection of the claimed current source/state shows it absent, unreachable or materially different. Record the expected source, inspected ref and reproduction. Do not use GHOST merely for a stale historical claim.

**Disposition rules:**
- Applicable: in scope and relevant.
- Not applicable: explain why, who accepted the exclusion and the review trigger.
- Not assessed: no conclusion; never treat as a pass.

### H1. Harmony seam review

Use the seven Harmony invariants and exact probe definitions from the assessed Tri-Tier 33 source version. Do not invent or rename probes in this record.

| Harmony ID | Invariant / probe source | Applicable? | Evidence IDs | Result | Critical failure? | Unknowns / follow-up |
|---|---|---|---|---|---|---|
| H-1 | | | | Pass / Fail / Partial / Not assessed | | |
| H-2 | | | | Pass / Fail / Partial / Not assessed | | |
| H-3 | | | | Pass / Fail / Partial / Not assessed | | |
| H-4 | | | | Pass / Fail / Partial / Not assessed | | |
| H-5 | | | | Pass / Fail / Partial / Not assessed | | |
| H-6 | | | | Pass / Fail / Partial / Not assessed | | |
| H-7 | | | | Pass / Fail / Partial / Not assessed | | |

**Harmony interpretation:**  
[Describe observed cross-layer agreements/disagreements. Do not infer seam integrity from separate layer results.]

## I. 33-Perspective module — complete only if selected

**Framework source/version:**  
**Source repository and exact commit:**  
**Assessment profile/depth:**  

For each perspective used, retain its exact ID and wording from the source version. Do not replace it with an invented summary.

| Perspective ID | Exact perspective question | Status | Evidence IDs | Finding IDs | Contradictions / unknowns | Action / owner |
|---|---|---|---|---|---|---|
| P-xx | | Addressed / Gap / Unknown / Not applicable (reason) | | | | |

**Group synthesis**
1. Need, context and legitimacy:
2. Design, evidence and operational integrity:
3. Sustainability, impact and resilience:

A perspective marked Addressed is not proof of compliance or success; it means the question was examined with the evidence and limitations recorded.

## J. Non-compensable gate review

A high score, positive finding count or commercial benefit cannot offset a failed or unresolved critical gate.

| Gate | Status | Evidence / finding IDs | Required action | Decision owner |
|---|---|---|---|---|
| Authority and permission | Clear / Blocked / Unknown / N/A | | | |
| Privacy and data minimisation | Clear / Blocked / Unknown / N/A | | | |
| Safety and safeguarding | Clear / Blocked / Unknown / N/A | | | |
| Evidence integrity and provenance | Clear / Blocked / Unknown / N/A | | | |
| Security-critical risk | Clear / Blocked / Unknown / N/A | | | |
| Legal / contractual boundary | Clear / Blocked / Unknown / N/A | | | |
| Conflict of interest / independence | Clear / Blocked / Unknown / N/A | | | |
| Release / operational authority | Clear / Blocked / Unknown / N/A | | | |

**Gate outcome:** Clear for recommendation / Hold / Reject / Not assessed  
**Rationale:**  

## K. Contradictions, uncertainty and limitations

**Contradiction register:**  
[Claim A vs Claim B, source IDs, dates, whether sources are independent, current resolution.]

**Unknowns:**  
[What cannot currently be established?]

**Assumptions:**  
[State each assumption and how it could change the conclusion.]

**Coverage limitations:**  
[Files, systems, users, data, tests, environments or source classes not examined.]

**Freshness / expiry triggers:**  
[Events or dates that require reassessment.]

**Confidence statement:**  
[Bounded statement explaining evidence quality, independence, coverage and unresolved uncertainty. Avoid unsupported numerical confidence.]

## L. Recommendation — not the decision

Choose one:
- **Proceed:** no identified blocking issue within this bounded scope; this is not release authorisation.
- **Proceed with conditions:** specified actions must be completed before the named next step.
- **Hold:** material evidence, authority, safety or risk question remains unresolved.
- **Reject:** the proposal is not justified or acceptable within the stated scope and constraints.

**Recommendation and rationale:**  
**Conditions / blockers:**  
**Required actions:**  
**Proposed owners:**  
**Verification criteria:**  
**Target review date / trigger:**  

## M. Actual decision record — completed by the authorised decision owner

| Field | Record |
|---|---|
| Decision ID | |
| Decision owner and authority basis | |
| Decision date | |
| Actual decision | Approved / Approved with conditions / Deferred / Rejected / No decision |
| Scope approved | |
| Explicit exclusions | |
| Conditions and stop triggers | |
| Risk acceptance, if any, and authority | |
| Dissent / reviewer reservations | |
| Implementation owner (only if approved) | |
| Verification required before next gate | |

**Important:** The assessment lead's recommendation is not the actual decision. If the owner lacks authority, record **No decision — authority not established**.

## N. Corrective action and verification tracker

| Action ID | Finding / gate ID | Corrective or preventive action | Owner | Due / trigger | Verification method | Result / evidence | Residual risk |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

Preserve failed attempts and original results. A later pass does not erase an earlier failure. Close an action only when its stated verification criterion has been met and evidence is linked.

## O. Final review and publication control

- [ ] Scope and exact source baseline recorded.
- [ ] Framework versions and selection rationale recorded.
- [ ] Evidence links are traceable and accessible to authorised reviewers.
- [ ] Observations are separated from interpretation.
- [ ] Contradictions, negative evidence and unknowns are retained.
- [ ] Non-compensable gates are explicitly reviewed.
- [ ] Recommendation is separated from actual decision.
- [ ] Corrective actions have owners and verification criteria.
- [ ] Sensitive data and secrets are excluded or appropriately redacted.
- [ ] Claims are bounded to the assessed commit, environment and scope.
- [ ] Publication / sharing approval is recorded where required.

**Prepared by:**  
**Reviewed by:**  
**Decision owner:**  
**Final record date:**  
**Record version:**  
**Supersedes:**  
**Correction history:**  

---

## P. Assessment summary for readers

**Question assessed:**  
**System / project and exact commit:**  
**Framework(s) used:**  
**Scope and exclusions:**  
**Most material findings:**  
**Blocking gates:**  
**Recommendation:**  
**Actual decision (if made):**  
**What this assessment does not establish:**  
**Next verification step:**  

**Reader warning:** This is a bounded assessment record, not a certification, penetration-test report, legal opinion, compliance attestation, safety guarantee or release approval.
