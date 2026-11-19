# Startup repository and engineering-knowledge benchmark

**Research date:** 2026-11-19  
**Scope:** Codex-Guidas as a cross-project engineering knowledge base; lessons from startup software engineering and public GitHub repository operations  
**Status:** Research synthesis and proposed improvements; not a maturity certification

## Executive assessment

Codex-Guidas is best positioned as a **Git-native engineering memory and evidence layer**, not a replacement for an issue tracker, service catalog, incident platform or external documentation product.

The strongest patterns worth adopting are:

1. Keep decision and lesson records close to version control, searchable and reviewable.
2. Make templates proportionate: lightweight for routine changes, fuller evidence records for consequential decisions.
3. Link incident learning to a named owner, a measurable corrective action, a due/review date and verified completion.
4. Test the knowledge tooling itself, not only the content it manages.
5. Treat repository security and software-supply-chain controls as a separate, inspectable concern.
6. Measure whether prior knowledge changes decisions and reduces recurrence; do not measure success by the number of documents or frameworks.

The most important startup lesson is not to build more process. It is to connect problem discovery, requirements, design, tests and release evidence tightly enough that we do not build the wrong thing or mistake a prototype for a proven product.

## 1. Evidence base and limitations

This review combines peer-reviewed empirical studies, official documentation and inspected public repository/product documentation.

- **Startup engineering study:** Klotins, Unterkalmsteiner and Gorschek analysed 88 startup experience reports, covering 25 relatively successful and 63 closed startups. The authors concluded that inadequate requirements engineering was a central source of engineering difficulty. This is a study of experience reports, not a random census of all startups.
- **GitHub Actions failure study:** Zheng et al. analysed 375 failed workflow executions from 260 open-source Java projects and surveyed 151 developers. It provides a concrete failure taxonomy for that sample; it is not startup-specific and should not be generalised to every language or CI platform.
- **Documentation drift study:** A study of more than 3,000 GitHub projects examined obsolete references from documentation to source-code elements. Its measured rates concern outdated code-element references, not every form of stale documentation.
- **Product documentation:** MADR, Log4brains, Backstage, GitBook, GitLab and Rootly pages describe their own capabilities. They are useful for product comparison, not independent proof that one product improves business outcomes.
- **Security guidance:** OWASP, GitHub and OpenSSF provide threat and control guidance. A listed risk is not a measured frequency claim.

We distinguish **common in the cited samples**, **recommended controls**, and **tail-risk scenarios**. We do not present every plausible failure mode as statistically common in startups.

## 2. Similar repositories and products

| Example | What it does well | What Codex-Guidas should borrow | What not to copy now |
|---|---|---|---|
| [MADR](https://github.com/adr/madr) | Markdown ADR templates with full and minimal variants; decision records remain in Git | Offer a short record for routine decisions and a fuller one where context/consequences matter; preserve status and history | Do not force every project learning into an architecture decision record |
| [Log4brains](https://github.com/thomvaill/log4brains) | Docs-as-code ADR knowledge base; CLI creation, local preview, generated searchable site and decision timeline | Improve navigation and retrieval; chronological decision context is useful when a decision is revisited | It is ADR-centred and should not replace defect evidence, test records or incident ownership |
| [Backstage TechDocs](https://backstage.io/docs/features/techdocs/) | Markdown documentation connected to a software catalog; teams can discover docs from a service entry | Later, connect project/service records to canonical documentation and owners | Backstage is a developer-portal platform. Its setup and operational burden are not justified by our current portfolio size |
| [GitBook](https://gitbook.com/docs/) | Git sync, visual editing, change requests, publishing, access control and content analytics | Consider as an optional publishing front end if external audiences need polished documentation | Do not move canonical evidence or project authority out of Git merely to gain a hosted editor |
| [GitLab Incident Review](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/incident-review/) | Blameless reviews, defined roles, owner accountability and corrective actions | Make action ownership explicit; ask whether the action addresses the cause rather than just the symptom | Do not impose a heavyweight incident review on every small defect |
| [Rootly](https://rootly.com/incident-postmortems/action-items) | Tracks follow-up actions with owners, priority, due dates and status; can sync into ticketing tools | Keep actions linked to their originating incident and review overdue work | Automated incident coordination and ticket synchronisation are premature until incident volume requires them |
| [OpenSSF Scorecard](https://github.com/ossf/scorecard) and [Best Practices Badge](https://openssf.org/projects/best-practices-badge/) | Structured repository-security checks and self-assessed best-practice criteria | Use individual security findings as prompts for risk reduction, with evidence and applicability notes | Do not turn one aggregate score into a quality verdict or certification; Scorecard itself documents heuristic limits |

### Product-fit recommendation

Keep the current architecture: Markdown and Git remain the source of truth; the small Python CLI remains the retrieval layer; CI checks record integrity.

The nearest feature match for decision history is Log4brains/MADR. The closest future publishing options are GitBook or a lightweight static documentation site. Backstage becomes relevant when there are enough distinct services, owners and dependencies to justify a catalog. Rootly/incident.io-style incident coordination becomes relevant when incidents require multiple responders, escalation and cross-system action tracking. None is a replacement for the evidence and authority boundaries already defined here.

## 3. Common startup engineering and repository mistakes

### A. Requirements disconnected from the real user problem

The startup study found that requirements engineering was the most discussed software-engineering area and a central activity, but practices were often rudimentary or poorly aligned with design, quality and business goals. Vague product value propositions make it harder to identify target users, stakeholders, functional requirements and quality needs. The authors connect these inadequacies to technical debt, poor quality and wasted effort on irrelevant features.

**Control for our projects:** Before significant implementation, record the user/problem, value proposition, assumptions, evidence source, decision, observable acceptance criteria and stop condition. A prototype should test a specific assumption, not silently become production architecture.

### B. Testing only after users expose obvious defects

The startup study reports cases where testing happened when an obvious issue emerged and user feedback substituted for rigorous internal testing. It also warns that release-time code checks can miss design and stress failures.

Separately, the 2026 GitHub Actions study found test failures to be the largest category in its sample: 120 of 375 failed workflow executions (32%). Most of these were unit-test failures, with integration-test failures also present.

**Control for our projects:** Test the invariant and the boundary that can fail, not merely the happy path. Keep unit, integration, end-to-end, build, device/runtime and user evidence distinct. Add regression tests for defects when practical, and track flaky tests rather than repeatedly rerunning them until CI turns green.

### C. Build and workflow configuration treated as incidental

The GitHub Actions study identifies source-code compilation, build configuration, quality checks, dependency resolution and workflow configuration as recurring failure categories. In its developer survey, around 60% reported build configuration issues at least sometimes; roughly half reported test, source-code, quality-check or workflow configuration issues at least occasionally.

**Control for our projects:** Keep setup commands reproducible; document the supported runtime; validate environment configuration; keep CI permissions minimal; and test the actual workflow path. When a run fails, distinguish a project failure from a runner, network, permission or third-party-action failure before changing application code.

### D. Prototype shortcuts accumulating into permanent architecture

The startup study describes prototypes that help clarify uncertain requirements, but notes that continuing to add features to a makeshift product degrades architecture and accumulates technical debt.

**Control for our projects:** Label prototype and production boundaries. Record which shortcuts are temporary, who accepts them, what evidence triggers hardening and what would cause the prototype to be discarded. Avoid speculative infrastructure before a user or technical need is demonstrated.

### E. Quality attributes not prioritised against user value

The study reports weak definition of quality requirements and cases where teams over-invested in attributes such as scalability without a corresponding market need. It also notes that poor product quality can damage adoption and reputation.

**Control for our projects:** Set minimum quality thresholds for relevant attributes—security, reliability, usability, performance, accessibility and recovery—based on the intended users and use case. Do not optimise an impressive metric that does not change user value or risk.

### F. Documentation silently drifting away from code

The documentation-drift study found that 28.9% of the most popular projects in its top-1,000 dataset had at least one outdated code-element reference at the time of analysis; 82.3% had at least one during their history. The outdated references could persist for years.

**Control for our projects:** Keep examples executable where possible; validate local links and command examples; review references when source files or APIs change; record the source revision and review scope. Our current link validator checks that local Markdown targets exist, but it does not yet prove that every code symbol, command or behavioural description is current.

### G. Corrective actions that do not prevent recurrence

GitLab's incident review guidance emphasises understanding contributing causes and implementing preventive actions. It assigns a review initiator, a directly responsible individual and a bar raiser. It warns against generic actions, symptom-only fixes and actions unlikely to prevent recurrence or improve response time. Rootly's product documentation similarly keeps follow-ups linked to the source incident with an owner, priority, due date and status.

**Control for our projects:** Link each corrective action to the originating defect, make it specific and testable, assign an owner and date, and record the evidence that closes it. A completed ticket is not automatically proof that recurrence risk has fallen.

## 4. Less frequent or tail-risk mistakes worth testing

The evidence does not support calling every item below a common startup failure. Some are low-frequency workflow failures; others are high-impact security or correctness risks for which frequency varies by ecosystem and threat model.

| Failure pattern | Why it is dangerous | Practical control |
|---|---|---|
| Unresolvable GitHub Actions reference (deleted/private repo, typo or missing tag) | CI can stop before project tests even start | Verify action owner, repository and immutable revision; monitor dependency updates |
| Poisoned pipeline execution or untrusted pull-request code in a privileged workflow | A contributor may gain access to secrets or write-capable workflow tokens | Separate untrusted PR validation from privileged workflows; review workflow changes; avoid unsafe `pull_request_target` patterns |
| Mutable third-party action or dependency reference | Reviewed code can be replaced upstream after review | Prefer workflow dependency lockfiles or verified full commit SHAs; keep updates deliberate |
| Over-privileged CI identity or leaked credentials | A compromised job can affect more than the job needs | Least-privilege `GITHUB_TOKEN`, scoped credentials, secret scanning and rotation after exposure |
| Dependency confusion, typosquatting or compromised package maintainer | A build can execute attacker-controlled code under normal dependency resolution | Minimise dependencies; verify package identity and provenance; use lockfiles and dependency monitoring |
| Artifact substitution or weak release provenance | A release may not correspond to the source revision and build that were tested | Record source revision, build identity and artifact hash; add signing/provenance where release risk justifies it |
| Partial persistence, duplicated retries or non-idempotent imports | The system can show success while leaving records inconsistent or processing the same event twice | Inject partial failures; test retries, replay, idempotency and reconciliation |
| Backup that has never been restored, or migration that cannot be rolled back | Data recovery may fail precisely when it is needed | Run restore drills; test forward and backward migration plans on representative data |
| Tenant/role boundary confusion or private data in logs and artifacts | Data can be disclosed across users, organisations or access boundaries | Test authorisation at every boundary; minimise and redact logs; test exported artifacts |
| Single-maintainer knowledge concentration | A key person becoming unavailable can stall fixes, releases and incident response | Document critical paths, ownership and handover steps; build a second maintainer when feasible |

The 2026 GitHub Actions study observed only three cases of unresolvable action references among its 375 failures, making that failure uncommon in that particular sample. This does not make supply-chain compromise unimportant: OWASP separately identifies insufficient flow control, identity/access, dependency-chain abuse, poisoned pipeline execution, credential hygiene, artifact integrity and insufficient logging as major CI/CD risk areas.

## 5. What we should improve in Codex-Guidas

### Immediate, proportionate improvements

1. **Test the knowledge CLI as software.** Add unit tests for frontmatter parsing, duplicate IDs, allowed states, index coverage, broken links, retrieval filters and overdue review-queue behaviour. CI currently has smoke tests; unit tests will make edge cases reproducible.
2. **Harden workflow dependencies.** Pin third-party GitHub Actions to verified commit SHAs or use GitHub's workflow dependency lockfile where supported. Add a weekly Dependabot schedule for GitHub Actions so updates are proposed rather than silently drifting.
3. **Add a focused repository security policy.** A public repository should explain how to report a sensitive security issue. Enable secret scanning/push protection, dependency alerts and code scanning where available. The presence of a `SECURITY.md` file does not itself prove these settings are active.
4. **Verify default-branch governance.** Use a ruleset to require PRs and passing CI on `main`. A solo maintainer should not impose an artificial multi-person approval gate that cannot be met; introduce independent review when another qualified maintainer exists.
5. **Improve documentation freshness checks selectively.** Retain current local-link checks; add executable command examples and source references to important technical claims. Consider symbol/reference checking only when drift appears in practice.
6. **Keep licence choice explicit.** There is currently no `LICENSE` file on `main`, consistent with the repository's stated decision not to grant an external reuse licence yet. Do not add a licence by automation. Resolve ownership and intended reuse first.

### Later, only if use justifies it

- Generate a searchable static site while keeping Markdown/Git canonical.
- Add a project/service catalog only when separate projects have enough owners, interfaces and operational dependencies to make cross-navigation difficult.
- Add incident workflow automation only when response volume, multi-person coordination or overdue corrective actions become a demonstrated problem.
- Add semantic retrieval or a database only when keyword retrieval is shown to miss relevant records or become operationally slow.

## 6. How to measure whether these improvements work

Do not count markdown files, templates or tool integrations as impact. Establish a baseline and review:

- eligible investigations with a prior-knowledge search recorded;
- cases where a prior record materially changed the diagnosis, design or tests;
- corrective actions closed with exact receiving-project verification;
- recurrence of known failure modes after controls were adopted;
- repository-tool regressions caught by unit tests before merge;
- stale documentation references discovered and corrected;
- time from defect intake to defensible cause or next discriminating test.

A rise in reported defects can mean better detection, not deteriorating quality. Interpret recurrence and investigation time alongside project exposure and reporting quality.

## 7. Research references

### Startup engineering and testing
- Klotins, E., Unterkalmsteiner, M. & Gorschek, T. (2019). *Software engineering in start-up companies: An analysis of 88 experience reports*. Empirical Software Engineering. [https://doi.org/10.1007/s10664-018-9620-y](https://doi.org/10.1007/s10664-018-9620-y)
- Zheng, L. et al. (2026). *Why Do GitHub Actions Workflows Fail? An Empirical Study*. ACM Transactions on Software Engineering and Methodology. [https://doi.org/10.1145/3749371](https://doi.org/10.1145/3749371)

### Documentation quality and drift
- *Detecting outdated code element references in software repository documentation* (2023). Empirical Software Engineering. [https://doi.org/10.1007/s10664-023-10397-6](https://doi.org/10.1007/s10664-023-10397-6)
- DORA, [Documentation quality](https://dora.dev/capabilities/documentation-quality/)

### Security, repository and CI/CD controls
- OWASP, [CI/CD Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/CI_CD_Security_Cheat_Sheet.html)
- OWASP, [Top 10 CI/CD Security Risks](https://owasp.org/projects/top-10-cicd-security-risks)
- GitHub, [Secure use reference for GitHub Actions](https://docs.github.com/en/actions/reference/security/secure-use)
- GitHub, [Workflow dependency lockfiles](https://docs.github.com/en/actions/concepts/security/workflow-dependency-lockfiles)
- GitHub, [Dependabot version updates](https://docs.github.com/en/code-security/concepts/supply-chain-security/dependabot-version-updates)
- GitHub, [Protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
- OpenSSF, [Scorecard](https://github.com/ossf/scorecard) and [Best Practices Badge](https://openssf.org/projects/best-practices-badge/)

### Knowledge, decisions and incident learning examples
- [MADR](https://github.com/adr/madr)
- [Log4brains](https://github.com/thomvaill/log4brains)
- Backstage, [TechDocs](https://backstage.io/docs/features/techdocs/)
- GitBook, [Documentation and Git sync](https://gitbook.com/docs/)
- GitLab, [Incident Review](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/incident-review/)
- Rootly, [Post-incident action items](https://rootly.com/incident-postmortems/action-items)

## 8. Decision

Adopt the small, Git-native improvements first: unit tests for the CLI, pinned CI dependencies, dependency update monitoring, and a clear security-reporting path. Preserve the existing methodology and authority boundaries. Do not introduce a developer portal, incident SaaS, semantic search service or aggregate maturity score until actual usage shows a need.
