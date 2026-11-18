# Evidence-First Development Methodology

## Workflow
1. **Question:** State the user problem, risk or decision.
2. **Contract:** Record decision, as-of date, scope, exclusions, comparisons, required sources, output and stop condition.
3. **Baseline:** Inspect repository, branch, current code, tests, CI and runtime evidence before proposing changes.
4. **Independent lanes:** Seek independent evidence for consequential claims.
5. **Evidence ledger:** Assign claim IDs; capture source, date, artifact, relevance, confidence, contradictions and gaps.
6. **Analysis:** Separate facts, interpretations, assumptions, hypotheses and recommendations.
7. **Decision gate:** Identify authority and evidence required to proceed.
8. **Smallest implementation:** Change only what is authorized and necessary for acceptance criteria.
9. **Verification:** Run focused tests, relevant regression suite, CI and runtime/user checks as appropriate.
10. **Closeout:** Record commit, commands, results, failures, risks and next smallest action.
11. **Knowledge transfer:** Add reusable lessons with provenance and applicability boundaries.

## Evidence rules
- Snippets, model memory and summaries are leads, not primary evidence.
- Prefer source files, test output, CI records, runtime observations and direct user-task observations.
- Distinguish source authority from source independence.
- Record publication/observation date and check date.
- Preserve contradictions and missing evidence.
- Use explicit states: unknown, proposed, designed, implemented, tested, demonstrated, user-tested, adopted, commercially validated.
- Never infer adoption, safety, compliance or demand from a successful build.

## Acceptance contract
- Problem / decision:
- User or risk affected:
- Current baseline:
- Scope and exclusions:
- Observable acceptance criteria:
- Security, privacy and safeguarding constraints:
- Required evidence:
- Stop / rollback conditions:
- Decision authority:

## Research engineering protocol
Question → contract → independent query lanes → source fetching → evidence ledger → verification → sourced report.

The report identifies Claim ID, status, evidence, contradictions, dates, source independence, missing proof and limitations. Claim strength must never exceed evidence strength.

## Stop conditions
Stop and reassess if a gate is unresolved, sensitive data/access is unapproved, a test failure is unexplained, source-of-truth ownership is unclear, scope exceeds the contract, or no user/risk/learning/milestone benefit remains.