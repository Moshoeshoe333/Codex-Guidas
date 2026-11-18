# Tri-Tier 33 Framework
## Technical integrity across Mind · Body · Spirit

**Framework ID:** CG-TT33  
**Version:** 0.3.0-draft  
**Status:** Proposed technical assessment instrument; not ratified as a universal standard.  
**Source basis:** User-supplied Refined Tri-Tier 33 Framework reviewed 18 November 2026; Codex-Guidas evidence-first methodology; 33-Perspective Master Register v0.2.  
**Purpose:** Assess whether a software system's code, persistence and user interface are individually coherent and remain truthful across their boundaries.

> This is an instrument, not an authorization gate. It helps discover, describe and verify risk. Project owners and existing governance gates retain decision authority.

## 1. Position in the Codex-Guidas method system

Codex-Guidas distinguishes three complementary instruments:

| Instrument | Primary question | Scope |
|---|---|---|
| Point → Knowing → Witness → Gate | What is the question, what do we know, what is the evidence, and who may authorize the next step? | Epistemology and decision discipline |
| 33-Perspective Master Register | Have we considered human, strategic, operational, legal, commercial and lifecycle realities? | Project / product / organizational review |
| **Tri-Tier 33** | Do code, persistence and UI behave consistently, truthfully and safely, including at their seams? | Technical system assessment |

They are complementary, not competing scorecards. Do not add their scores together. A completed technical review cannot replace community validation, legal review, safeguarding approval, commercial evidence or a project-specific gate.

## 2. Architecture

- **Mind — Codebase (C-01…C-33):** decision logic, contracts, dependencies, errors, build and executable behaviour.
- **Body — Persistence (D-01…D-33):** durable records, schema, transactions, integrity, recovery, retention and disclosure.
- **Spirit — User Interface (U-01…U-33):** user inputs, navigation, state, explanations, accessibility, consent and presentation.

Each layer has three circles:
- **A — Existence and structure:** what exists, where it lives and how it is connected.
- **B — Correctness and trust:** whether behaviour and records respect contracts and boundaries.
- **C — Verification and change discipline:** whether claims can be reproduced, monitored, migrated and safely changed.

The 99 entries are assessment lenses, not 99 automatically mandatory controls. Every entry receives a passport disposition: Applicable, Not applicable (reason required), or Not assessed. Not assessed is never a pass.

## 3. Core rules

1. Claim strength must never exceed evidence strength.
2. CLAIM ≠ EVIDENCE ≠ OBSERVATION ≠ INTERPRETATION ≠ STATUS.
3. A design is not an implementation; an implementation is not proof of correct operation.
4. A passing test supports only the cases, build, environment and conditions it actually exercised.
5. Evidence does not confer authority to proceed.
6. No owner path or identifiable subject under assessment means the claim remains unknown; it does not mean the system is absent.
7. Preserve failures, contradictions, limitations and negative evidence.
8. Do not silently repair or normalize a cross-layer disagreement. Record, investigate, authorize and verify the correction.
9. Apply the least data, permission, dependency and operational complexity that can safely achieve the real task.
10. A project profile may add controls, but may not silently weaken a universal critical boundary.
11. A tier may be excluded only with a reason, owner and review trigger.
12. The framework itself must be tested against real defects and decisions; coverage is not proof of effectiveness.

## 4. Tier assessment and passports

Use one record per tier, generated from a common template where possible. Minimum fields:
- Tier ID and exact question.
- Disposition: Applicable / Not applicable / Not assessed.
- Scope, component, data class, user group and environment.
- Owner path: repository, branch, exact commit and file/line or system identifier.
- Claim being made.
- Evidence references, dates, provenance and applicability.
- Evidence level (L0–L6) where meaningful; otherwise explain why the ladder is unsuitable.
- Verdict: SOLID / SOFT / OPEN / GHOST.
- Finding IDs, counter-evidence, limitations and residual risk.
- Required next verification, accountable owner and review trigger.

**Verdicts**
- **SOLID:** the bounded claim is supported by current, applicable, reproducible evidence and no unresolved material contradiction is known.
- **SOFT:** partial evidence exists, but scope, coverage, freshness or conditions limit the claim.
- **OPEN:** evidence is missing, insufficient, stale or a material question remains unresolved.
- **GHOST:** an authoritative current claim says an artifact/control exists or is active, but inspection of the claimed current source/state shows it is absent, unreachable or materially different. Record the expected source, inspected ref and reproduction. A stale historical claim is not automatically a GHOST; classify it as stale/superseded unless current status still asserts it.

A SOLID verdict is local to its stated claim and conditions. It is not a general quality or release certification.

## 5. Evidence ladder — L0 to L6

- **L0 — Unknown / not inventoried**
- **L1 — Declared**
- **L2 — Statically verified**
- **L3 — Test-witnessed**
- **L4 — CI-witnessed**
- **L5 — Runtime-witnessed**
- **L6 — Device / real-user-witnessed**

This is a descriptive ladder, not a universal linear ranking of truth. Evidence levels are claim-specific and sometimes incomparable: a narrow, high-quality runtime observation may answer a different question from broad CI coverage. Record method, exact claim, version, environment, sample, date, result and limitation. Do not promote evidence merely because a higher-numbered activity occurred. For market, legal, security, safeguarding and accessibility claims, use evidence appropriate to that claim; L0–L6 alone may be inadequate.

**Evidence applicability fields:** claim supported; build/commit; environment/device; configuration; dataset/sample; test procedure; date/time; observer/runner; result; failure/negative evidence; scope not covered; expiry/recheck trigger.

## 6. Harmony — cross-layer agreement

The seven Harmony Invariants and their probes are specified in [Tripartite Harmony](tripartite-harmony.md). The [Tier ↔ Harmony Crosswalk](tier-harmony-crosswalk.md) maps every C, D and U tier to at least one invariant. Harmony is assessed at the seams, not inferred from three strong layer scores.

Report at least:
- per-invariant result and evidence references;
- applicable probe coverage;
- unresolved critical failures;
- not-assessed gaps;
- observed seam indices, where useful;
- lowest seam index and median seam index;
- evidence level/applicability separately from numeric score.

No single aggregate score can declare a system safe, ready or authorized. Critical blockers remain visible and non-compensable.

## 7. Proportional application

- **T0 — Routine:** relevant tiers only for small, reversible, low-risk changes.
- **T1 — Material:** affected layer tiers, changed seams, data flows, dependencies and rollback.
- **T2 — High consequence:** explicit review of relevant critical tiers, independent challenge and named approval.
- **T3 — Strategic / irreversible:** broad 99-tier applicability review, all seven Harmony invariants where relevant, counter-evidence, staged validation and formal project gate.

These are proposed review depths, not calibrated risk thresholds. Each project must define triggers. All 99 tier IDs remain in the register; effort is proportionate.

## 8. Adoption sequence

1. **Baseline only:** inspect live repository and establish scope; no score-based promotion.
2. **Risk-first passports:** start with the highest-risk applicable tiers, not all 99 manually.
3. **Report-only probes:** automate deterministic checks and publish findings without changing runtime behaviour.
4. **Cross-layer challenge:** test H-1…H-7 with synthetic/controlled data first.
5. **Project ratification:** project owner approves any project-specific requirements or gates.
6. **Expand coverage:** generate additional passports and scoreboards only when they improve decisions.
7. **Review effectiveness:** compare framework findings with actual defects, incidents, user evidence and missed risks.

## 9. Universal core vs project profile

The universal core defines the 99 lenses, evidence discipline, verdicts, Harmony semantics and non-compensable principles. A project profile supplies its own:
- policy rules and decision classes;
- jurisdiction and legal/safeguarding obligations;
- data classes and retention;
- device/platform envelope;
- offline, telemetry and integration promises;
- criticality, threat model and approval owners;
- project-specific tests and acceptance thresholds.

SoulSync-specific P1–P7, G-BOOT, E-008/E-009 and ZA detection patterns are not universal requirements. They belong in a SoulSync profile and are referenced by tier IDs only where applicable. ScoutSA and Mall Navigre must define their own profiles. Reuse the method, not another project's assumptions.

## 10. Governance and maturity

This v0.3.0 draft refines the source instrument. It is not formally ratified, empirically calibrated or independently validated. Do not claim universal certification, exhaustive defect detection, compliance, production readiness or proven reduction in defects.

Promotion requires:
1. review by technical and relevant domain practitioners;
2. application to materially different real project decisions;
3. evidence of useful findings and documented misses/false positives;
4. measurement of review effort and maintenance burden;
5. revisions with preserved rationale;
6. explicit owner ratification and a versioned decision record.

The 33-Perspective Master Register remains separate at v0.2 and proposed. Its strategic lenses can trigger deeper Tri-Tier reviews; Tri-Tier findings can inform strategic review. Neither silently ratifies the other.
