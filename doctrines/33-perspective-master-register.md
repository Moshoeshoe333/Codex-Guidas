# 33-Perspective Master Register

**Status:** Proposed working register — not yet ratified as the canonical 33.  
**Version:** 0.2  
**Purpose:** Turn the 33-perspective doctrine into a repeatable, evidence-bearing decision aid without creating unnecessary ceremony.  
**Parent doctrine:** [33-Tier Epistemological Framework](33-tier-framework.md)

> The Point is the reason. The Knowing is the revelation of its application. The Witness is the evidence. The Gate is the authority to proceed.

## 1. Rules of use

1. This is a **proposed** set of 33 lenses. Names and definitions may change through review and ratification.
2. Apply lenses proportionately. A routine, reversible change does not need a full portfolio review.
3. For consequential decisions, record each lens as **Pass / Concern / Fail / Not assessed / Not applicable**, with a short evidence reference and owner.
4. A critical failure in safeguarding, consent, privacy, security, legal duty or data integrity cannot be averaged away by passing other lenses.
5. A perspective marked Not assessed is an explicit evidence gap, not a pass.
6. Similarity between projects is a lead for investigation, not proof that a control transfers unchanged.
7. The register does not authorize implementation. Project-specific gates and decision owners remain authoritative.
8. Do not assign numerical weights until the lenses have been tested against real decisions and the consequences of weighting are understood.

## 2. Proposed 33 perspectives

| ID | Perspective | Operational question | Evidence to seek | Failure signal | Verification approach |
|---|---|---|---|---|---|
| P01 | Purpose and problem fit | What real problem does this solve, for whom, and why now? | Problem statement, observed workflow, stakeholder testimony | Solution exists without a demonstrated problem | Compare proposal with observed needs; test the smallest problem hypothesis |
| P02 | Human dignity and autonomy | Does this preserve people's agency, dignity and ability to make informed choices? | User research, consent language, complaint/appeal paths | Coercion, manipulation, humiliation or avoidable dependency | Scenario review with affected users; inspect opt-out and appeal paths |
| P03 | Stakeholder and community fit | Have the people affected been identified and meaningfully heard? | Stakeholder map, consultation notes, dissenting views | Decisions made for a community without its input | Validate with representative stakeholders; record who was not reached |
| P04 | Accessibility and inclusion | Can people with relevant disabilities, literacy levels and access constraints use it? | Accessibility checks, usability sessions, device and language coverage | Exclusion is treated as an edge case without assessment | Test assistive use, low-literacy flows and alternative access paths |
| P05 | Language and cultural context | Are language, terminology and cultural assumptions appropriate to the setting? | Reviewed translations, local terminology, participant feedback | Ambiguous or culturally misplaced wording changes meaning or access | Native/competent speaker review and contextual user testing |
| P06 | Safeguarding and abuse resistance | Could this expose a person, especially a child or vulnerable user, to exploitation or harm? | Threat scenarios, safeguarding procedures, guardian/consent controls, escalation route | Unsafe contact, exposure or participation can occur without an effective control | Abuse-case testing; verify operational controls, not policy text alone |
| P07 | Privacy and data minimisation | Is each personal-data element necessary, protected and retained only as justified? | Data inventory, purpose, retention/deletion rules, access map | Excessive collection, public exposure or undefined retention | Trace data from collection to deletion; test access boundaries |
| P08 | Security and threat resistance | What can go wrong maliciously, and how is it prevented, detected and contained? | Threat model, attack surface, security tests, incident plan | Trust boundary or abuse path has no control or owner | Adversarial review, negative tests and dependency/security scanning |
| P09 | Legal and regulatory fit | Which duties apply in this jurisdiction and use case, and who has reviewed them? | Applicable law/guidance, counsel or competent review, compliance mapping | Unsupported compliance claim or unresolved legal blocker | Verify jurisdiction, current authority and exact obligations with qualified review |
| P10 | Consent, authority and permission proportionality | Who is allowed to decide, access, publish, contact, change or approve, and does every permission/background capability map to a current user-visible purpose? | Permission model, consent records, role definitions, delegation trail, OS/API permission inventory | Technical capability is mistaken for permission; unused or speculative permissions are retained | Test authorization and revocation paths; map each permission to an active user story and owner |
| P11 | Data quality, provenance and physical-digital freshness | Where did the data come from, how was it transformed, and which real-world changes could silently invalidate it? | Source records, timestamps, lineage, verification owner, staleness/expiry policy, update process | Unknown origin, stale data, silent transformation, tenant/map/device drift or unsupported assertion | Trace sample records end-to-end; simulate physical-state change and verify expiry, correction and re-verification |
| P12 | Evidence and uncertainty | Does the strength of each claim match the strength and independence of its evidence? | Evidence ledger, source quality, dates, limitations, counter-evidence | Hypothesis presented as fact or duplicate sources treated as independent | Reproduce the claim; seek disconfirming evidence and independent corroboration |
| P13 | Correctness and invariants | What must always remain true, and can the design or implementation violate it? | Explicit invariants, domain rules, property and regression tests | Contradictory states or untested critical assumptions | Derive boundary tests and verify invariants at relevant layers |
| P14 | Failure modes and blast radius | How can this fail, who is affected, and how far can the failure spread? | Failure-mode analysis, dependency map, incident history | Single defect can cause broad harm without detection or containment | Fault injection, negative-path tests and impact walkthrough |
| P15 | Resilience and recovery | Can the service recover safely from interruption, corruption or partial failure? | Backup/restore evidence, recovery procedure, degraded-mode behaviour | Recovery is assumed but never rehearsed | Restore drill and failure/restart tests with recorded outcomes |
| P16 | Offline grace and connectivity realities | Does the core task survive no network, weak signal, packet loss and intermittent connectivity without losing input, duplicating writes or corrupting state? | Offline requirements, local-write contract, sync queue, retry/idempotency rules, conflict policy, payload measurements, field tests | Core use blocks on network; dropped submissions vanish; retries duplicate actions; sync overwrites user state; data use is unaffordable | Test airplane mode, throttling, packet loss, retries, duplicate submission, conflict resolution and recovery; measure realistic payload/data cost |
| P17 | Device and resource constraints | Can intended devices handle the workload within memory, CPU, storage and power limits? | Device matrix, profiling, minimum requirements | Tested only on powerful developer hardware | Profile representative low-resource devices and long-running use |
| P18 | Bandwidth and data affordability | What data does the system consume, and what does that cost the user? | Payload measurements, transfer frequency, local network/data pricing assumptions | Hidden or recurring data cost blocks access | Measure realistic workflows on constrained connections |
| P19 | Financial and operating cost | What is the total cost to build, run, support and maintain this? | Cost model, hosting/tooling estimates, support effort, funding assumptions | Recurring liabilities or hidden labour are ignored | Scenario-based cost review and actual spend/effort tracking |
| P20 | Maintainability, dependency decay and simplicity | Can the system be understood, changed and repaired after dormancy without disproportionate effort or dependency rot? | Module boundaries, code/documentation quality, change history, pinned dependencies, setup instructions, external-service assumptions | Complexity exceeds demonstrated need; undocumented secrets; expired services; unpinned or abandoned dependencies break a fresh build | Independent change walkthrough and clean-room build from a fresh clone; record environment, date and exact commit |
| P21 | Developer cognitive load and handover | Can another capable person understand the work and continue it safely? | Setup guide, decision log, architecture notes, ownership map | Critical knowledge exists only in one person's memory | Fresh-person handover exercise and reproducible setup |
| P22 | Testability and observability | Can we detect, reproduce and explain whether the system behaves correctly? | Test strategy, logs, metrics, traceability, test data | Failures are invisible or test results cannot be tied to a version | Reproduce a known event from recorded evidence; inspect signal quality |
| P23 | Performance and scale | Does it meet realistic response and throughput needs at expected load? | Workload assumptions, benchmarks, latency/error measurements | Scale claims have no workload model or measurements | Benchmark representative workloads; document limits and bottlenecks |
| P24 | Interoperability and integration | Can it exchange data safely and correctly with required systems? | Interface contracts, schemas, mapping rules, integration tests | Informal coupling or undocumented assumptions break exchange | Contract tests and end-to-end integration against representative systems |
| P25 | Dependency and supply-chain risk | Which external components, services or people can compromise availability or integrity? | Dependency inventory, versions, licences, advisories, maintainer status | Untracked, abandoned or excessive dependency exposure | Review lockfiles/SBOM where available; assess critical dependency failure |
| P26 | Portability and vendor lock-in | Can the project move or operate if a provider, platform or tool becomes unavailable? | Export formats, deployment assumptions, migration path | Critical data or operation is trapped without a viable exit | Export/import test and provider-outage or migration tabletop exercise |
| P27 | Usability, entry friction and immediate utility | Can a first-time user reach meaningful core value without unnecessary install, registration or onboarding barriers, while retaining necessary safety and consent gates? | Task-based usability sessions, time-to-first-value, completion/error rates, abandonment reasons, safety/consent rationale for each step | Mandatory friction precedes value without a safety or task justification; users misunderstand key states or abandon the task | Observe representative first-time users; measure time-to-first-value and test lower-friction alternatives without weakening controls |
| P28 | Support and operations | Who monitors, responds, resolves and communicates when something goes wrong? | Runbooks, ownership, support channels, escalation and incident records | No accountable operator or response path | Simulate an incident and follow the operational handoffs |
| P29 | Reversibility and migration | Can this decision be undone or changed without unacceptable loss or harm? | Rollback plan, migration strategy, data export, decision record | Irreversible commitment made before uncertainty is reduced | Rehearse rollback/migration on a safe representative environment |
| P30 | Environmental and resource sustainability | Are energy, hardware, material and lifecycle impacts proportionate to the value? | Hosting/resource measurements, hardware lifecycle assumptions | Wasteful resource use without user or operational benefit | Measure resource use and compare lower-impact alternatives |
| P31 | Demand and adoption validation | Is there evidence that intended users will adopt or pay for this, rather than merely praise the idea? | Interviews, observed use, pilots, retention, willingness-to-pay evidence | Interest or synthetic tests are presented as demand | Run a small ethical pilot with observable behaviour and explicit success criteria |
| P32 | Measurable outcome and value | What outcome should improve, how will it be measured, and what would count as failure? | Baseline, metric definitions, denominator, target, guardrails | Activity or exposure is reported as impact | Compare against baseline and inspect outcome quality, not vanity metrics |
| P33 | Long-term viability and retirement | Can this be sustained, transferred, responsibly wound down or retired? | Ownership/funding outlook, maintenance plan, exit and deletion procedure | No sustainable owner or safe shutdown path | Review lifecycle scenarios, transferability and retirement rehearsal |

## 3. Cross-case refinements introduced in version 0.2

The three-project desk review identified five refinements. These are integrated into existing perspectives; the register remains at 33 lenses:

| Refinement | Existing lens | What to test |
|---|---|---|
| Offline grace and data conservation | P16, P18, P22 | Input preservation, idempotent retries, conflict handling, payload size and useful degraded-mode behaviour. |
| Dependency decay and build reproducibility | P20, P25, P29 | A clean-room build after dormancy using pinned dependencies and documented setup, without undocumented secrets or expired services. |
| Permission proportionality and scope isolation | P08, P10, P25 | Every OS/API permission, background process and integration maps to a current user-visible capability and explicit authority boundary. |
| Physical-digital coupling and maintenance burden | P11, P14, P22, P28 | Real-world changes that invalidate digital state; accountable owner, verified_at, staleness/expiry and correction process. |
| Entry friction and immediate utility | P01, P27, P31 | Barriers between first contact and useful value, and whether each barrier is necessary for safety, consent or task completion. |

These refinements arose from desk review, not yet from independently observed field/device experiments. The review record is [Three-Project Case-Study Review — 2026-11-18](case-studies/2026-11-18-three-project-register-review.md).

## 4. Decision record — minimum fields

For each consequential decision, record:

- **Decision ID / date / project / owner**
- **Point:** question, intended outcome and decision deadline
- **Scope:** users, systems, jurisdictions, exclusions and affected parties
- **Assessment:** P01–P33 status, evidence reference and short rationale
- **Critical blockers:** any Fail or unresolved high-consequence Concern
- **Unknowns:** what is not yet established and how it could be resolved
- **Counter-evidence:** strongest credible challenge to the preferred option
- **Gate:** who has authority to ratify and what must be true before proceeding
- **Next action:** smallest useful, reversible step
- **Review trigger:** event/date/metric that requires reassessment

A blank assessment is not approval. A completed register is not authorization.

## 5. Critical non-compensable checks

The following require explicit resolution when relevant; they cannot be averaged into an overall score:

- Safeguarding and abuse resistance (P06)
- Privacy and data minimisation (P07)
- Security and threat resistance (P08)
- Legal and regulatory fit (P09)
- Consent and authority (P10)
- Data quality and provenance (P11)
- Correctness of critical invariants (P13)

A project may identify additional non-compensable controls based on its own risk profile. A critical issue may require stopping, narrowing scope, or redesigning the proposal.

## 6. Proportionality levels

| Level | Typical use | Expected treatment |
|---|---|---|
| L0 — Routine | Small, reversible, low-risk maintenance | Assess directly relevant lenses; record unusual risk only |
| L1 — Material | User-facing feature, new dependency, data flow or workflow change | Assess relevant lenses, affected users and rollback path |
| L2 — High consequence | Personal data, money, safety, minors, security boundary or external integration | Explicit review of all relevant critical lenses, independent challenge and named approval |
| L3 — Strategic/irreversible | Major architecture, public launch, market commitment, high-impact automation | Full 33-lens review where applicable, counter-evidence, staged validation and formal gate decision |

These levels are proposed guidance, not calibrated risk thresholds. Projects must define their own triggers and approval authority.

## 7. Review and ratification

Before this register is called canonical:

1. Review overlaps, missing perspectives and unclear wording.
2. Test it against at least three real decisions from different project contexts, with actual execution or stakeholder evidence where the decision requires it. Desk reviews alone do not satisfy empirical validation.
3. Record false positives, missed risks, redundant questions and excessive effort.
4. Ask relevant domain reviewers to challenge specialist lenses (for example, legal, safeguarding, security and accessibility).
5. Revise the register and preserve the change rationale.
6. Obtain explicit owner ratification and record the version/commit.
7. Revisit after material incidents or evidence that a lens failed to surface a risk.

**Current state:** Version 0.2; 33 lenses with five operational refinements from three documented project desk reviews. Empirical validation and formal ratification remain open.
