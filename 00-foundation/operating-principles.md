# Operating Principles

**Status:** Adopted working principles; reviewable, not immutable law.

## North star
Build to learn. Test to know. Measure to improve. Expand only when evidence earns it.

## Rules
1. Evidence before expansion: significant work must improve usability, reduce material risk, test an important assumption, produce adoption/commercial evidence, or remove a real milestone blocker.
2. Claims are bounded by evidence. The strength of a claim must never exceed the strength of its support.
3. Documentation serves a decision, implementation, test, handover, audit or learning outcome. Documentation volume is not product progress.
4. One primary product milestone at a time. Protect focus; maintain or deliberately pause other projects.
5. Prefer the smallest complete, observable vertical slice over broad unfinished architecture.
6. No implementation across an unresolved decision gate.
7. Security, privacy and safeguarding are release requirements.
8. Meaningful failures and near-misses produce lessons and, where practical, regression tests or preventive controls.
9. Separate design, implementation, test evidence, runtime proof and user evidence.
10. Prefer reversible, proportionate decisions. Speculative future needs alone do not justify complexity.
11. Preserve provenance: source project, artifact, commit, test run, date and limitations.
12. Review, challenge and retire practices when evidence changes.

## Evidence ladder
| Level | Evidence | Permitted description |
|---|---|---|
| E0 | Requirement/design documented | Designed |
| E1 | Automated tests pass for defined cases | Tested against defined cases |
| E2 | End-to-end workflow runs in controlled environment | Demonstrated working |
| E3 | Realistic data and adversarial cases exercised | Tested under realistic conditions |
| E4 | Independent users complete defined tasks | User-tested |
| E5 | Repeat use and measurable value observed | Adoption evidence |
| E6 | Willingness to pay and actual transactions | Commercial evidence |

Levels are not automatic. Record scope, date, environment, sample size and failures. Evidence is specific to the claim tested.

## Decision filter
Before significant work, state the user/problem/risk, observable outcome, scope, exclusions, required evidence, smallest safe implementation and stop/rollback condition. If no useful answer exists, backlog the idea.

## Portfolio focus
A prior planning hypothesis allocated 80% of development attention to ScoutSA, 10% to UCI, 5% to SoulSync and 5% to NAVIGRE. This is not measured time or a permanent commitment. Reassess against value, risk and capacity.

## Change control
Changes to these principles require rationale, affected projects, evidence, risks and effective date. Never silently rewrite historical decisions.

## Epistemological foundation
Our reasoning sequence is **Point → Knowing → Witness → Gate**. The 33-perspective filter and three-pass 99-tier sieve are methods for structured scrutiny, not guarantees of truth or a fully validated 99-check standard. The detailed 33-lens taxonomy remains open. See [the doctrine](../doctrines/33-tier-framework.md).

## Human context and honesty
Build around lived constraints, dignity, privacy, accessibility, safeguarding and sustainable use. For community/youth-facing systems, safeguarding is a precondition for relevant live exposure. Separate synthetic technical tests from empirical user validation. Record material unvalidated assumptions visibly. Critique decisions and systems without blaming people; never conceal failure or overstate evidence.

## Sustainable allocation
The 80/10/5/5 portfolio split is a provisional planning hypothesis for available project-development attention only. It does not displace livelihood, rest, urgent obligations or evidence-based reprioritisation. Review it regularly; see [Portfolio Ecology](../doctrines/portfolio-ecology.md).
