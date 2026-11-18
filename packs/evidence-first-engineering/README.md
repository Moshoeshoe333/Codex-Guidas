# Pack: Evidence-First Engineering

**Pack ID:** CG-PACK-002  
**Version:** 1.0.0  
**Maturity:** Working methodology; adapt and validate per project.  
**Upstream source:** 02-methodologies/evidence-first-development.md

## Purpose
A repeatable path from a question to an authorized, verified change, without confusing research, design, implementation and evidence.

## Workflow
1. **Question:** state the user problem, risk or decision.
2. **Contract:** capture decision, as-of date, scope, exclusions, comparisons, required sources, output and stop condition.
3. **Baseline:** inspect the actual repository, branch, files, tests, CI and runtime evidence.
4. **Independent lanes:** seek independent evidence for consequential claims.
5. **Evidence ledger:** assign claim IDs; record source, date, provenance, confidence, contradiction and gaps.
6. **Analysis:** separate fact, interpretation, assumption, hypothesis and recommendation.
7. **Decision gate:** name the authority and evidence needed to proceed.
8. **Smallest authorized change:** implement only what the decision permits.
9. **Verification:** run focused tests, relevant regressions, CI and runtime/user checks as applicable.
10. **Closeout:** record exact commit, commands, environment, outcomes, failures and residual risks.
11. **Knowledge transfer:** extract a reusable lesson with provenance and applicability limits.

## Claim-state vocabulary
Unknown · Proposed · Designed · Implemented · Tested · Demonstrated · User-tested · Adopted · Commercially validated.

Use only states supported by evidence. A successful build does not establish adoption, safety, legal compliance or market demand.

## Minimum evidence ledger
| Field | Meaning |
|---|---|
| Claim ID | Stable identifier |
| Claim | Exact proposition being assessed |
| Status | Supported / contradicted / unknown / proposed |
| Source | Exact artifact, URL, test run or observation |
| Date | Source date and check date |
| Provenance | Origin and transformation |
| Independence | Whether corroboration is genuinely independent |
| Limitation | What the source cannot establish |
| Counter-evidence | Strongest credible challenge |
| Next verification | Smallest action to resolve uncertainty |

## Stop conditions
Pause if authorization is missing, sensitive access is unapproved, a critical test failure is unexplained, source-of-truth ownership is unclear, scope exceeds the contract, or the work no longer produces user value, risk reduction or justified learning.

## Adaptation
Projects may replace tools and templates but should preserve separation between claims, evidence, authority, implementation and verification.
