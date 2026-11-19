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
### A note on the “91% of failed startups had no automated tests” figure

The 91% figure appears in a 2025/2026-era business/technology article attributing it to an individual audit of 47 failed startup codebases. I could not find a peer-reviewed study or an independently inspectable sampling protocol supporting that number. It may describe that particular audit, but it should **not** be repeated as a general startup failure statistic without the underlying data, selection criteria, definition of “automated testing” and audit method.

Better-described research reports materially different results:
- An ICSE 2018 technical-debt study surveyed 86 startups: 26 (about 30%) were attempting to implement test automation and 17 (about 20%) explicitly stated that no test automation was used. Manual exploratory testing was still reported as the primary quality practice. The study does not support “91% had no tests.”
- A study of 11 Namibian startups found that 86% of respondents reported spending substantial effort on manual testing and not performing automated testing. This is a small, geographically specific sample and is not a global estimate.
- A 2019 multi-vocal analysis of 88 startup experience reports found little discussion of testing and noted cases where teams relied on customers to expose obvious issues; it called for more research rather than claiming a universal percentage.

**Decision:** We adopt the engineering lesson—automate the high-value regression checks and test failure boundaries—but reject the 91% headline as a general fact. The definition also matters: “some automation exists,” “most tests are automated,” “meaningful coverage exists,” and “critical business paths are protected” are not interchangeable claims.

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
| [ECMWF Codex](https://github.com/ecmwf/codex) | Organisation-specific principles, ADRs, repository structure, project maturity, security disclosure, AI contributions and documentation guidance; changes through discussion and PRs | Keep one navigable governance index; link rules to templates, owners and review paths; make maturity and AI boundaries visible | Do not copy an organisation-wide policy catalogue into a solo-maintained repo without the people/process needed to enforce it |
| [GitHub Open Source Guides](https://github.com/github/opensource.guide) | Community-oriented guidance for creating, maintaining and contributing to open-source projects | Use as a reference when deciding whether to open external contributions, support and community processes | It is community/project-operations guidance, not a cross-project technical evidence ledger |
| [Awesome Guidelines](https://github.com/Kristories/awesome-guidelines) | Curated external coding standards and guidelines, organised by language and technology | Link to authoritative external standards instead of duplicating them; retain source, date and applicability | A curated list is not an internal learning system and does not verify that a guideline is suitable for a particular project |
| [UK Home Office Engineering Guidance and Standards](https://github.com/UKHomeOffice/engineering-guidance-and-standards) | Markdown-based standards site, local builds/tests, Playwright checks and scheduled stale-content review alerts with a dry-run rollout | Later, consider scheduled review reminders with dry-run first; pair review dates with accountable owners and controlled issue creation | Do not add a site generator and automatic issue creation before the manual review queue proves useful |
| [AI Engineering Hub](https://github.com/patchy631/ai-engineering-hub) | Large collection of runnable AI tutorials and projects organised by skill/difficulty | Separate learning/tutorial material from normative engineering controls; identify runnable examples and environment requirements | Large resource collections are not evidence repositories; project count is not proof of quality or adoption |

### Product-fit recommendation

Keep the current architecture: Markdown and Git remain the source of truth; the small Python CLI remains the retrieval layer; CI checks record integrity.
## 2A. Documentation organisation: use Diátaxis as a reading map, not a mass migration

[Diátaxis](https://diataxis.fr/) distinguishes four documentation needs: **tutorials** (learning by doing), **how-to guides** (accomplishing a task), **reference** (authoritative information) and **explanation** (understanding why). It is a content-design framework, not a requirement to move every file into four new directories.

For Codex-Guidas, the useful adaptation is a front-door reading map:
- **Tutorial:** first knowledge search and validation; a newcomer should be able to run the CLI and interpret its limits.
- **How-to:** triage a defect, apply a prior lesson, add a lesson, verify a change and perform a review.
- **Reference:** metadata schema, lifecycle taxonomy, CLI commands, templates, evidence ladders and project crosswalks.
- **Explanation:** methodology–knowledge architecture, operating principles, research findings and the rationale behind the 33-based methods.

Keep the existing domain folders and source-evidence layout. Add a navigational Diátaxis map and classify new user-facing docs where useful; do not re-home all 41 lessons or project records just to satisfy a documentation taxonomy. A defect record or lesson is an evidence object, not automatically a tutorial or how-to guide.

This also avoids a category error: **documentation-as-code is already partly implemented** because Markdown lives in Git, changes are reviewed through PRs, and CI validates metadata and local links. Adding MkDocs or Docusaurus would add a publishing layer, not create documentation-as-code from scratch. Build and publish a site only when there is a defined external audience, navigation problem or publishing need.

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

1. **Test the knowledge CLI as software — implemented on this branch.** Seven standard-library unit tests now cover frontmatter parsing, duplicate keys and IDs, local-link failures, overdue review behaviour, retrieval filters and valid index/record handling. CI runs them before the validator and smoke tests. Expand cases as real defects reveal gaps.
2. **Harden workflow dependencies — implemented on this branch.** The current workflow pins checkout and setup-python to verified full commit SHAs, with version comments, and `.github/dependabot.yml` requests weekly GitHub Actions dependency updates. Dependabot proposals still require review and passing CI.
3. **Add a focused repository security policy — document added on this branch; settings remain a maintainer action.** `SECURITY.md` must direct sensitive reports away from public issues and explain that GitHub private vulnerability reporting only works after it is explicitly enabled in repository settings. Separately verify secret scanning, push protection, dependency alerts and code scanning availability. A policy file does not prove any of these controls are active.
4. **Verify default-branch governance — still unverified.** Inspect the `main` branch ruleset/protection settings directly in GitHub. The research connection could read the branch SHA but could not read protection settings, so no conclusion is made about whether protection is enabled. If configuring a rule, require PR and CI checks; do not impose an unfulfillable two-person approval gate on a solo maintainer.
5. **Improve documentation freshness checks selectively.** Retain current local-link checks; add executable command examples and source references to important technical claims. Consider symbol/reference checking only when drift appears in practice.
6. **Keep licence choice explicit.** There is currently no `LICENSE` file on `main`, consistent with the repository's stated decision not to grant an external reuse licence yet. Do not add a licence by automation. Resolve ownership and intended reuse first.

### Later, only if use justifies it

- Generate a searchable static site while keeping Markdown/Git canonical.
- Add a project/service catalog only when separate projects have enough owners, interfaces and operational dependencies to make cross-navigation difficult.
- Add incident workflow automation only when response volume, multi-person coordination or overdue corrective actions become a demonstrated problem.
- Add semantic retrieval or a database only when keyword retrieval is shown to miss relevant records or become operationally slow.

## 6. How to measure whether these improvements work
## 5A. Assessment of the additional recommendations

| Recommendation | Decision for Codex-Guidas | Reason |
|---|---|---|
| Diátaxis | **Adopt selectively** as a reading map and content-design guide | Improves discovery without a disruptive repository-wide move |
| Documentation-as-code | **Already partly in place**; improve tests and freshness | Git, PRs and CI are already the canonical authoring path |
| Stronger README/front door | **Retain and refine** | README now states purpose, offers core paths, CLI commands, test command and benchmark; revisit with actual user feedback |
| CONTRIBUTING.md | **Already present** | Defines evidence, search and authority boundaries |
| SECURITY.md | **Added on this feature branch** | Explains private reporting is not active until enabled and verified in GitHub settings |
| CODE_OF_CONDUCT.md | **Defer until a public contributor/community process is intentionally opened** | A conduct standard matters when the project accepts public participation; avoid presenting a file as a substitute for moderation capacity |
| CHANGELOG.md and Semantic Versioning | **Defer until there are tagged user-facing releases or external CLI/API consumers** | Not every knowledge-base update is a release; PR history is sufficient while the project remains maintainer-led |
| CLA or DCO | **Do not add yet** | The repository has deliberately not chosen an outbound reuse licence. Resolve ownership, intended reuse and contribution policy first |
| MkDocs/Docusaurus | **Defer** | The repo's current audience and navigation needs do not justify maintaining a publishing toolchain |
| Link checking / Markdown lint | **Incremental** | Local Markdown target validation exists. Add linting and external-link checks only with controlled false-positive handling and maintainable tooling |
| New-repo bootstrap checklist | **High potential** as a separate reusable knowledge pack | Useful across projects, but it should be derived from actual project onboarding and risk requirements rather than copied as a generic 200-item checklist |

### Important IP distinction: DCO is not a CLA

The Linux Foundation describes the DCO as a contributor's affirmation that they have the right to submit a contribution under the project's stated licence. It is not itself a licence or contract and does not grant the project owner broader relicensing rights. A CLA is a separate agreement whose grant terms vary; it can provide broader inbound rights while copyright ownership generally remains with the author unless the agreement says otherwise.

Therefore neither should be added as a ritual:
1. Decide who owns existing text/code and which external uses are intended.
2. Select and review the outbound licence for the repository.
3. Decide whether contributions are open, restricted or maintainer-only.
4. Only then choose an appropriate inbound mechanism (DCO, CLA or another policy) with legal review.

Until those decisions are made, keep the repository's no-external-licence warning visible and do not imply that contributions can be relicensed or redistributed on terms that have not been agreed.

### Other claims in the supplied assessment

- **GPL:** Saying that using a GPL library always forces a proprietary startup to open-source its whole codebase is too broad. The GNU FAQ distinguishes incorporating/linking code into a combined program from using a GPL development tool or distributing separate independent programs alongside one another. Obligations depend on the licence version, how components are combined and whether the combined work is conveyed/distributed. LGPL and AGPL have different terms. Review each dependency and integration with qualified legal advice; do not make blanket claims.
- **Solo-maintainer risk:** This is real operational concentration, but hiring a co-maintainer prematurely is not the default remedy. First document ownership, recovery, release and incident steps; use least-privilege access; identify a backup maintainer when trust and capacity allow.
- **Regional configuration:** Hardcoded regions, account IDs, endpoints and resource names become risks when environments or deployment regions differ. Make environment-specific values configuration and test every supported deployment target; do not abstract for regions a project will never use.
- **Money and credits:** Where a project handles value, use explicit currency and decimal/minor-unit representations, defined rounding rules, idempotent credit/debit operations, ledger invariants and boundary tests. A generic `round()` call is not a financial policy.
- **Premature refactoring / “ego” / hiring by enthusiasm:** These are product and team-management risks, not repository defects in themselves. Translate them into observable practices: ship the smallest safe experiment, solicit disconfirming feedback, document decisions and recruit for a real capability gap. Do not use “launch fast” to bypass security, privacy or safeguarding gates.

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
- *Exploration of Technical Debt in Start-ups* (ICSE-SEIP 2018). Survey material from 86 startups reported that 26 (30%) were attempting test automation and 17 (20%) explicitly reported no automation; manual exploratory testing remained a primary practice. [Research publication record](https://www.researchgate.net/publication/325728693_Exploration_of_technical_debt_in_start-ups) (secondary-hosted paper text; verify publisher copy for formal citation).
- *Bridging the Gap: Addressing Software Testing Challenges in Namibian Startups through a Tailored Training Approach*. Study of 11 Namibian startups; 86% reported substantial manual testing and lack of automation. [IEEE Xplore](https://ieeexplore.ieee.org/document/10653696)
- The “91%” claim is attributed to an individual audit of 47 failed startups in business/technology reporting, not to the 86-startup academic survey. [Inc. coverage](https://www.inc.com/maria-jose-gutierrez-chavez/47-startups-failed-most-made-the-same-coding-mistake/91251802).
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
### Documentation, community health and IP
- Diátaxis, [Start here](https://www.diataxis.fr/start-here/)
- GitHub Docs, [Community health files](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file)
- Linux Foundation, [DCO](https://bestpractices.linuxfoundation.org/ip/contribution-mechanisms-dco.html) and [DCO/CLA contribution mechanisms](https://bestpractices.linuxfoundation.org/ip/contribution-mechanisms.html)
- GNU Project, [GPL Frequently Asked Questions](https://www.gnu.org/licenses/gpl-faq.en.html)
- [MADR](https://github.com/adr/madr)
- [Log4brains](https://github.com/thomvaill/log4brains)
- Backstage, [TechDocs](https://backstage.io/docs/features/techdocs/)
- GitBook, [Documentation and Git sync](https://gitbook.com/docs/)
- GitLab, [Incident Review](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/incident-review/)
- Rootly, [Post-incident action items](https://rootly.com/incident-postmortems/action-items)

## 8. Decision

Adopt the small, Git-native improvements first: unit tests for the CLI, pinned CI dependencies, dependency update monitoring, and a clear security-reporting path. Preserve the existing methodology and authority boundaries. Do not introduce a developer portal, incident SaaS, semantic search service or aggregate maturity score until actual usage shows a need.

## 9. Implementation status on the Codex-Guidas feature branch

As of 2026-11-19, the following controls have been added to `codex/retrieval-enforcement-2026-11-19` and validated in GitHub Actions:

- Seven CLI unit tests, in addition to metadata/link validation and search/review-queue smoke tests.
- `actions/checkout` and `actions/setup-python` pinned to verified full commit SHAs.
- Weekly Dependabot configuration for GitHub Actions.
- README links to this benchmark and documents the unit-test command.
- A repository `SECURITY.md` policy. Its private-reporting instructions are conditional: the maintainer must enable GitHub private vulnerability reporting in repository settings and verify the option is available before treating that channel as active.

These checks were run in hosted GitHub Actions on the feature branch; they do not prove that branch rules, secret scanning, push protection, dependency alerts or code scanning are enabled. Those repository settings require a separate owner/admin review. The branch remains a draft PR and these changes have not been merged into `main`.
