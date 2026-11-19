# New Repository Bootstrap — Baseline Checklist

**Pack:** CG-PACK-006 · **Version:** 1.0.0  
**Use with:** [Pack overview](README.md) and [risk overlays](RISK-OVERLAYS.md)

This is a decision and evidence checklist, not a scorecard. Apply every baseline section, mark individual controls according to the status vocabulary below, and add risk overlays where triggered. Tailor the controls to the repository's purpose and exposure.

## Record before starting

- Repository name and URL:
- Default branch:
- Visibility: private / internal / public:
- Purpose and intended users:
- Problem or decision this repository supports:
- Owning person/team:
- Decision owner:
- Recovery/backup maintainer, if applicable:
- Intended lifecycle: experiment / internal tool / product / library / archived:
- Planned exposure or release date:
- Data and user groups in scope:
- Applicable risk overlays:
- Date assessed / next review trigger:

## Status and evidence

| Status | Meaning |
|---|---|
| Not assessed | No adequate review yet |
| Planned | Action and owner identified; not implemented |
| Implemented | Present in code, configuration, process or platform setting |
| Verified | Direct evidence demonstrates operation in the receiving repository and relevant environment |
| Not applicable | Reason and decision owner recorded |
| Accepted risk | Residual risk, authorized owner, rationale and review/expiry trigger recorded |

For each control, maintain the evidence reference in the target repository. Evidence may include a path, exact commit SHA, test command/result, CI run URL, reviewed platform setting, deployment identifier or recovery exercise. Avoid storing credentials, personal data or sensitive incident details in the checklist.

## 1. Identity, ownership and scope

| ID | Control prompt | Minimum evidence to retain | Status / evidence |
|---|---|---|---|
| BOOT-01 | Is the purpose, intended user, problem and desired outcome explicit? | README statement or approved project brief with scope and exclusions | |
| BOOT-02 | Is there a named repository owner and a decision owner for consequential changes/releases? | Owner and authority recorded in repository or project documentation | |
| BOOT-03 | Is repository visibility intentional and reviewed against the code, issues, secrets and data it contains? | Visibility decision and access review | |
| BOOT-04 | Are source, documentation, assets and third-party materials' ownership and intended reuse understood? | Provenance/rights notes; unresolved items identified | |
| BOOT-05 | Is the lifecycle clear (prototype, internal use, public library, deployed product or archived)? | Lifecycle and prototype/production boundary stated | |

**Decision:** If ownership or rights are unclear, do not externally distribute or invite contributions that imply permissions have been granted.

## 2. Requirements, architecture and change authority

| ID | Control prompt | Minimum evidence to retain | Status / evidence |
|---|---|---|---|
| BOOT-06 | Is the user problem distinguished from the proposed solution? | Problem statement, assumptions and evidence source | |
| BOOT-07 | Are acceptance criteria observable and tied to user or risk outcomes? | Testable acceptance criteria for the first meaningful increment | |
| BOOT-08 | Are important exclusions, dependencies and stop conditions explicit? | Scope boundary and stop condition | |
| BOOT-09 | Are consequential or hard-to-reverse decisions recorded with alternatives and consequences? | Lightweight decision record or ADR where useful | |
| BOOT-10 | Are prototype shortcuts and deferred production controls visible? | Prototype label, owner and hardening/discard trigger | |

Do not create an ADR for every trivial change. Use decision records where they preserve context that would otherwise be lost.

## 3. Source control and review

| ID | Control prompt | Minimum evidence to retain | Status / evidence |
|---|---|---|---|
| BOOT-11 | Is the default branch and change path understood? | Branch naming/merge approach documented | |
| BOOT-12 | Are review and merge protections appropriate to the repository's ownership and risk? | Actual branch rules/settings inspected; note unsupported or unavailable controls | |
| BOOT-13 | Are high-risk paths or files assigned clear ownership where multiple maintainers exist? | CODEOWNERS or an equivalent ownership process, if useful | |
| BOOT-14 | Can changes be traced to a PR, commit or documented direct-maintainer change? | Review history and commit provenance | |

Do not claim branch protection is enabled because a policy document recommends it. Verify the actual repository settings. Do not impose a two-person approval requirement when no second qualified maintainer exists; document the solo-maintainer limitation and compensating checks.

## 4. Build, tests and software supply chain

| ID | Control prompt | Minimum evidence to retain | Status / evidence |
|---|---|---|---|
| BOOT-15 | Can a new maintainer reproduce the supported local setup? | Runtime/tool versions, dependency lockfiles and working setup commands | |
| BOOT-16 | Do automated checks protect the important invariants and failure boundaries? | Tests for the highest-risk paths; exact command and result | |
| BOOT-17 | Does CI run the relevant tests and build on the intended change path? | Successful workflow run tied to the commit under review | |
| BOOT-18 | Are CI permissions and secrets minimal, and are untrusted contributions prevented from accessing privileged credentials? | Workflow permission review and trigger/secret boundary | |
| BOOT-19 | Are workflow actions and external build dependencies pinned or otherwise controlled and reviewed? | Dependency references, update process and review evidence | |
| BOOT-20 | Is dependency vulnerability and update handling proportionate to exposure? | Enabled/available alerts or a documented manual review process | |
| BOOT-21 | Can a release artifact be tied back to the source revision and build process? | Release notes, source commit and artifact/build provenance where applicable | |

A passing unit suite is not integration, device, security or production verification. Separate test layers and name what was not exercised. Automated scanners are signals requiring triage, not proof that no vulnerability exists.

## 5. Security, data and privacy foundation

| ID | Control prompt | Minimum evidence to retain | Status / evidence |
|---|---|---|---|
| BOOT-22 | Is there a rule for preventing secrets and production credentials from entering source control, logs and artifacts? | Secret-handling procedure; scanner/settings status separately verified | |
| BOOT-23 | Are authentication, authorization and privileged actions identified and tested where relevant? | Roles/access model and negative tests for important boundaries | |
| BOOT-24 | Is data collection limited to what the product needs, with categories and sensitivity identified? | Data inventory or concise data-flow note | |
| BOOT-25 | Are storage, access, retention, deletion, logging and backup expectations defined for relevant data? | Data handling decisions and tested procedures where required | |
| BOOT-26 | Is there a clear vulnerability/incident reporting and response route appropriate to the repository's exposure? | Reporting channel verified to reach an owner; response owner/process | |
| BOOT-27 | Are third-party services and permissions understood at each trust boundary? | Integration inventory, scopes/permissions and data shared | |

A SECURITY.md file alone does not enable private vulnerability reporting, secret scanning, push protection, code scanning or dependency alerts. Verify each relevant platform setting separately. For jurisdiction-specific obligations, obtain appropriate privacy/legal advice rather than treating this checklist as a compliance determination.

## 6. Documentation, operations and recovery

| ID | Control prompt | Minimum evidence to retain | Status / evidence |
|---|---|---|---|
| BOOT-28 | Can a new contributor understand what the repository does and how to run its safe checks? | README with purpose, setup, test and limitations | |
| BOOT-29 | Are contribution, support and conduct expectations documented where the project accepts contributors or users? | CONTRIBUTING/support/conduct guidance as appropriate | |
| BOOT-30 | Is the licence/IP decision explicit before external distribution or accepting contributions under stated terms? | Approved licence and contribution terms, or explicit restricted/no-outbound-licence decision | |
| BOOT-31 | Is there an operator path for deploy, rollback, incident response and routine maintenance where the repository is deployed? | Runbook or concise operational procedure | |
| BOOT-32 | Are backup and restore, migration recovery and data-loss scenarios tested where data matters? | Restore/migration exercise and recorded outcome | |
| BOOT-33 | Are changelog, versioning and release notes used when consumers need a stable release contract? | Version/release record, or a reason they are not currently needed | |
| BOOT-34 | Are accessibility, usability, performance and reliability expectations appropriate to intended users? | Acceptance criteria and proportionate verification | |

Do not add CODE_OF_CONDUCT.md, CHANGELOG.md, a docs website or a service catalogue merely to complete a template. Add them when the audience, release model or operating need warrants them.

## 7. First-release / first-use gate

Before exposing the repository to users, accepting external contributions, deploying or distributing artifacts, record:

- [ ] Intended user and acceptance criteria are clear.
- [ ] All applicable baseline controls have a recorded disposition.
- [ ] Triggered risk overlays have been reviewed by an appropriate owner/specialist.
- [ ] Relevant tests pass on the exact candidate commit; untested areas are disclosed.
- [ ] Secrets, access permissions and data exposure have been checked.
- [ ] Ownership/licensing and public contribution terms are resolved for the intended distribution.
- [ ] Security reporting and incident ownership are real and reachable for the intended exposure.
- [ ] Deployment, rollback, backup/restore and migration recovery are credible and tested where applicable.
- [ ] Residual release-blocking risks are resolved or explicitly accepted by an authorized owner.

**Release decision:** Proceed / Proceed with documented conditions / Hold / Retire  
**Decision owner:**  
**Candidate commit / artifact:**  
**Evidence set:**  
**Accepted residual risks and review date:**  

## Review triggers

Revisit the checklist when the project changes its audience, visibility, data categories, user age group, payment/value flows, authentication model, external integrations, deployment region, privilege level, release model or maintainer ownership. Reassess affected controls rather than mechanically repeating every question.

## Pack completion rule

A completed checklist records the decisions and evidence available at a point in time. It does not certify the repository. The receiving project owns its controls, implementation, legal obligations, security posture and release decision.
