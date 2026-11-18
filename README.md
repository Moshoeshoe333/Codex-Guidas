# Codex-Guidas

A living engineering knowledge base documenting lessons learned, development methodologies, architectural principles, innovations, security practices, testing strategies, failures and proven solutions across our projects.

> **Build to learn. Test to know. Measure to improve. Expand only when evidence earns it.**

## Why this repository exists

We preserve reusable engineering knowledge so that each project benefits from the mistakes, discoveries, experiments and verified practices of the others. This is not a document-counting exercise: knowledge should help us make better decisions, prevent recurring defects, reduce risk, build useful products and validate real-world value.

## Start here

| Area | Purpose |
|---|---|
| [Operating principles](00-foundation/operating-principles.md) | Portfolio-wide rules and evidence ladder |
| [Lessons learned ledger](01-lessons-learned/ledger.md) | Cross-project lessons CG-001 onward |
| [Evidence-first development](02-methodologies/evidence-first-development.md) | Research, decision, implementation and verification workflow |
| [Architecture patterns](03-architecture/project-patterns.md) | Reusable design patterns and boundaries |
| [Security and safeguarding](04-security/safeguarding-and-threat-modeling.md) | Threat modelling, privacy and safety lessons |
| [Testing and CI](05-testing-verification/verification-and-ci.md) | Verification layers and regression discipline |
| [Innovation register](06-innovations/project-innovation-register.md) | Ideas, experiments and next proof |
| [Product validation](07-product-business/product-validation.md) | Usability, adoption and commercial evidence |
| [Project crosswalk](08-project-crosswalks/project-status.md) | ScoutSA, SoulSync, SoulSyncMobile, NAVIGRE and UCI |
| [Lesson template](09-templates/lesson-template.md) | Standard format for new entries |\n| [Defect Intelligence](11-defect-intelligence/README.md) | Defect intake, similarity search, verification and learning loop |

## Evidence and status discipline

Entries distinguish **Observed**, **Derived**, **Proposed**, **Verified** and **Superseded** knowledge. Historical project notes are not a fresh repository audit. Verify exact source artifacts, full commit hashes, test runs and current status before relying on them as release or audit evidence.

A passing test proves only the tested cases in the recorded environment. A design is not implementation. A build is not runtime verification. Synthetic data is not market demand. A prototype is not a validated product.

## Contribution rule

Every significant lesson should include its source, context, date, evidence class, impact, root-cause confidence, corrective/preventive action, verification method and residual risk. Do not promote a proposal to a verified practice without reproducible evidence.

Transfer principles, not assumptions: a technique must be adapted and re-validated in each project's context.

## Initial knowledge import

The first import is a curated synthesis from prior work on ScoutSA, SoulSync 3, SoulSyncMobile, NAVIGRE and the UCI threat-intelligence concept. It is intentionally conservative where current repository evidence has not yet been re-audited.


## Source archaeology

The initial source audit is recorded in [Repository Archaeology — 2026-11-18](10-source-audits/2026-11-18-repository-archaeology.md). It inspected selected primary files and commits across ScoutSA, SoulSync 3, SoulSyncMobile and NAVIGRE. It is a partial audit, not a fresh test execution. The [33-Tier Framework method](02-methodologies/33-tier-framework.md) is also indexed here; its own source explicitly leaves detailed specification and validation of all 33 tiers as open work.
