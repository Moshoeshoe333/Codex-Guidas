# External Repository Learning Method

**Status:** Proposed portfolio methodology  
**Owner:** Codex-Guidas maintainers / relevant project owner  
**Purpose:** Extract transferable engineering lessons from external repositories without copying architecture blindly, overstating evidence, or creating unnecessary project work.

> Learn broadly. Adopt narrowly. Verify locally. Preserve project authority.

## 1. Entry condition

Start a review only when it can answer a real question, such as:
- a known project weakness or unresolved design decision;
- a recurring defect or engineering cost;
- a concrete capability gap;
- a technology or architecture choice with material consequences;
- a need to compare a proposed approach with credible alternatives.

Do not review repositories merely to accumulate references. State the decision or learning question and the intended receiving project(s). Set a stop condition.

## 2. Source baseline and permitted inspection

For each repository, record its canonical URL, owner, default/selected branch, exact commit SHA, retrieval date, relevant paths and source types inspected. Prefer primary source code, tests, design documents, security policy, contributing guidance, licences and release notes.

Use the exact reviewed revision in source links where possible. If a repository advances, do not silently transfer observations to its new head.

Inspect only material relevant to the question. Public source inspection is not permission to probe deployed services, access private data, execute untrusted artefacts or conduct active security testing. Do not run builds, tests or benchmarks unless they are safe, proportionate and within the permitted environment; record when they were not run.

Record licence and attribution constraints before copying or adapting implementation code, assets or documentation. Architectural inspiration is not a substitute for licence review.

## 3. Evidence classification

Keep these categories separate:

- **Observed:** directly visible in the exact inspected source, documentation or recorded repository artefact.
- **Derived:** a transferable lesson inferred from one or more observations.
- **Hypothesis:** a possible local benefit that still needs a project-specific test or decision.
- **Verified locally:** the receiving project's defined acceptance criteria have been executed and reviewed on an exact source baseline.
- **Not assessed:** the review did not establish the matter.

A README description, architecture diagram, design note, test file or workflow definition is not proof that a capability works in production. Do not claim an external test passed unless the test was actually run and its conditions/results are recorded. A local code change does not itself verify the transferred lesson.

## 4. Extract the pattern, not the product

For each candidate pattern, record:
1. The concrete source observation and exact locator.
2. The underlying engineering principle.
3. The problem it solves and the conditions where it is useful.
4. Costs, limitations, failure modes and counter-evidence.
5. Whether the pattern duplicates an existing local control.
6. Security, privacy, safeguarding, legal, operational and maintenance implications.
7. The smallest reversible local adaptation and how it would be verified.

Do not recommend a dependency, framework, language migration or infrastructure platform solely because the external repository uses it.

## 5. Project-fit decision

Assess each receiving project independently. Choose one disposition:

- **Adopt as knowledge:** preserve a cross-project principle in Codex-Guidas only.
- **Record project reminder:** add a bounded, source-linked note because it identifies a material local gap or a decision to revisit.
- **Already covered — no change:** the project already has an adequate control; record the reason only when useful.
- **Defer:** plausible value, but timing, evidence, resources or project gates do not support action.
- **Reject / not applicable:** poor fit, disproportionate cost, conflicting invariant or unacceptable risk.

"No project-ledger change" is a valid and often preferable outcome. Do not create a reminder simply to show that a repository was reviewed.

## 6. Knowledge-transfer rules

- Add a cross-project lesson only when the pattern is genuinely reusable and not already captured.
- Keep the lesson **Derived** until evidence justifies a higher status.
- Add project-specific reminders only where they clarify a material gap, protect an invariant or guide a future decision.
- Project owners retain their own gate, ratification, release, legal, safety and operational authority.
- A Codex-Guidas entry does not authorize code, dependencies, migrations, data collection, external testing, deployment or publication.
- Preserve existing project constraints and explicitly state any unchanged gates.
- Prefer one consolidated source-review record over scattered duplicate notes.

## 7. Stop conditions and acceptance

Stop the review when the question is answered sufficiently, candidate patterns have been assessed against relevant projects, and no additional source is likely to change the decision. Stop or narrow scope if permissions, provenance, licensing, data handling or source identity become unclear.

A review is complete when:
- reviewed source revisions and inspected paths are traceable;
- observations are distinguished from inference and hypotheses;
- counter-evidence and limitations are visible;
- every relevant project has a fit disposition;
- any proposed local change has a specific owner, scope and proof requirement;
- Codex-Guidas and project ledgers are updated only where materially useful;
- written changes have been read back from the intended branch and their diffs checked.

Completion of the review is not implementation, local verification, project ratification or a gate transition.

## 8. Reference example

The [2026-11-27 GCHQ repository pattern review](../10-source-audits/2026-11-27-gchq-repository-pattern-review.md) is an example of selective source inspection across CyberChef, Bailo, Stroom, Sleeper, LD-Explorer and Coreax. It records both adopted knowledge and deliberate non-adoption decisions. A later, source-specific SoulSyncMobile check produced one bounded methodology reminder without changing application behavior or G-BOOT status.

## 9. Agent instruction design and inspection

When the review concerns AI coding-agent behaviour, inspect the repository's root and applicable nested AGENTS.md files at the exact reviewed revision. Also inspect the developer guide, coding conventions, test strategy, contributing guide, security policy and relevant CI workflows. An absent root AGENTS.md is a finding about that path and revision, not proof that the repository has no development rules.

Extract the operating contract rather than copying the source document. At minimum, assess:

- instruction scope, precedence and ownership;
- permission boundaries for file edits, dependency changes, Git staging/commits/history operations, issues/PRs, deployment, external services, production data and cost-incurring actions;
- architecture boundaries and protected/generated/vendored paths;
- verified runtime prerequisites and exact setup, test, lint and build commands;
- project-specific coding, security, privacy and contribution constraints;
- linked specialist documents and conditions that require human review.

Keep repository-specific rules separate. Two mature projects may legitimately grant different Git permissions or use different build systems. Never infer permission from tool availability, and never transfer a source repository's authority rules to a receiving project without its owner's decision.

Prefer a concise root instruction file that links to maintained technical guides. Record source paths, exact revisions and review dates for operational facts; do not guess commands or silently reuse stale instructions. Use the [Agent Instructions Template](../09-templates/agent-instructions-template.md) as a starting point, then validate every completed rule against the receiving repository.

The 2026-11-27 follow-up in the [GCHQ repository pattern review](../10-source-audits/2026-11-27-gchq-repository-pattern-review.md) compares Bailo and Stroom AGENTS.md files with Sleeper's developer-guide approach. Its findings are derived source observations, not universal permission policy.
