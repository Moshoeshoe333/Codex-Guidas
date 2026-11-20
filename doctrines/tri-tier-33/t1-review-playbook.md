# Tri-Tier 33 — timeboxed T1 review playbook

**Status:** Proposed operating guide for a proportionate pilot; does not ratify CG-TT33.  
**Framework:** CG-TT33 v0.3.0-draft  
**Timebox:** Up to 2 hours  
**Last reviewed:** 2026-11-19

## 1. What T1 means here

T1 is a **review-depth/timebox label** for a focused, risk-first review. It is not a C/D/U tier ID, an L0–L6 evidence level, a SOLID/SOFT/OPEN/GHOST verdict or a certification. A T1 review does not assess all 99 lenses.

Use this playbook when a change is consequential enough to need a structured cross-layer check but does not justify a full specialist assessment. Escalate to a deeper review when the threat model, data sensitivity, under-18 users, irreversible persistence, external integrations or unresolved contradictions demand it.

## 2. Two-hour sequence

| Time | Activity | Output |
|---|---|---|
| 0–10 min | **Point:** state the decision, change boundary, users/data, exclusions and stop condition | One-sentence decision contract |
| 10–25 min | **Knowing:** inspect repository, branch, full commit, change diff, relevant prior CG/DEF records | Baseline and retrieval note |
| 25–65 min | **Witness — risk-first:** inspect the smallest relevant code, persistence and UI paths; run or inspect the most discriminating checks available | Evidence IDs, observations and limitations |
| 65–85 min | **Harmony seam check:** follow one critical user/data path across code → persistence → UI; inspect failure, retry and partial-completion behaviour | Cross-layer agreement/disagreement |
| 85–105 min | **Challenge:** test assumptions, inspect negative evidence, identify alternative explanations and unassessed lenses | Findings and residual risk |
| 105–120 min | **Gate preparation:** state what is supported, open, not assessed and who has authority to decide | Decision-ready handoff; no automatic approval |

If the scope cannot be inspected honestly within two hours, stop at the timebox and record the unassessed areas. Do not compress evidence or mark skipped work as passed.

## 3. Minimum passport set by change type

Select the relevant questions from the canonical C/D/U catalogues. The following are prompts for choosing passports, not a new fixed tier mapping:

| Change type | Minimum questions to passport |
|---|---|
| Persistence/schema/migration | What is the durable source of truth? Are writes atomic? What happens on partial failure, corruption, restart, migration and rollback? Are uniqueness, ordering and retention explicit? |
| Offline/local storage | What is available offline? How are stale data, retries, clock changes, duplicate delivery, device loss and recovery handled? What is disclosed to the user when storage is unavailable? |
| Scoring/ranking/decision logic | Are inputs, weights, thresholds, versions and missing-data semantics explicit? Can outputs be explained and reproduced? Are ties, boundary values and adversarial inputs tested? |
| Under-18 or safeguarding path | Who is the subject, who is the guardian/authorized actor, what consent and access checks apply, and can private contact or exposure bypass them? What is logged and minimized? |
| CI/build/release workflow | Which exact source ref is tested? Are actions/dependencies pinned? Can a wrong-branch write, secret exposure, skipped job or stale artifact occur? Does green CI correspond to the claimed artifact? |
| External integration/API | What is the trust boundary? How are authentication, authorization, timeout, retry, idempotency, rate limits, schema drift and data minimization handled? |

For each selected passport, record its exact canonical tier ID after consulting the relevant C/D/U document. Do not invent mappings from this table. A tier can be Applicable, Not applicable (reason required) or Not assessed; Not assessed is not a pass.

## 4. Evidence and findings

Use the existing [Evidence, Verdicts and Tier Passport](evidence-and-passport.md) format. At minimum record:
- exact repository, branch/ref, full commit and inspected paths;
- bounded claim and affected users/data/environment;
- evidence IDs, source/date/provenance and what each supports;
- disposition and reason;
- evidence level only where meaningful;
- verdict and counter-evidence;
- limitations, residual risk and next discriminating check;
- accountable owner and review trigger.

A source read is not a runtime test. A mock is not a device. A passing test supports only the tested cases. Do not assign SOLID to an entire subsystem from one narrow check.

## 5. Pilot examples and maturity

The repository currently contains a SoulSyncMobile read-only pilot documenting a bounded 15-tier application. That is an example of selective use, not proof that the framework is effective or complete.

Do not claim a ScoutSA Tri-Tier 33 pilot unless a dated, source-linked passport set is added. A project crosswalk or source archaeology note is not automatically a Tri-Tier 33 assessment.

## 6. Stop conditions

Stop and report OPEN / Not assessed when:
- the exact source baseline cannot be established;
- required evidence is unavailable or materially contradictory;
- a safety, privacy, security or safeguarding boundary is unclear;
- the review would require access or actions not authorized;
- the timebox expires before a claim can be supported.

The project owner retains the Gate. This playbook prepares evidence; it does not authorize implementation, release or risk acceptance.
