# Codex-Guidas

A living engineering knowledge base documenting lessons learned, development methodologies, architectural principles, innovations, security practices, testing strategies, failures and proven solutions across our projects.

The master compendium of software engineering principles, operating rules, project methodologies, and hard-earned lessons from our development journey. Rooted in truth, evidence-based execution, and the 33-Tier approach.

> **Build to learn. Test to know. Measure to improve. Expand only when evidence earns it.**

## Why this repository exists

See [PURPOSE.md](PURPOSE.md) for the primary outcome, scope boundaries and success measures.

We preserve reusable engineering knowledge so that each project benefits from the mistakes, discoveries, experiments and verified practices of the others. This is not a document-counting exercise: knowledge should help us make better decisions, prevent recurring defects, reduce risk, build useful products and validate real-world value.

## Start here

| Area | Purpose |
|---|---|
| [Operating principles](00-foundation/operating-principles.md) | Portfolio-wide rules and evidence ladder |
| [Lessons learned index](01-lessons-learned/ledger.md) | Per-record lessons CG-001 onward; original ledger preserved in archive |
| [Evidence-first development](02-methodologies/evidence-first-development.md) | Research, decision, implementation and verification workflow |
| [Which method should I use?](docs/method-selection.md) | Choose the right method without combining maturity scores |
| [Methodology–knowledge architecture](docs/methodology-knowledge-architecture.md) | How reasoning methods, knowledge retrieval and project authority work together |
| [Architecture patterns](03-architecture/project-patterns.md) | Reusable design patterns and boundaries |
| [Security and safeguarding](04-security/safeguarding-and-threat-modeling.md) | Threat modelling, privacy and safety lessons |
| [Testing and CI](05-testing-verification/verification-and-ci.md) | Verification layers and regression discipline |
| [Innovation register](06-innovations/project-innovation-register.md) | Ideas, experiments and next proof |
| [Product validation](07-product-business/product-validation.md) | Usability, adoption and commercial evidence |
| [Project crosswalk](08-project-crosswalks/project-status.md) | ScoutSA, SoulSync, SoulSyncMobile, NAVIGRE and UCI |
| [UCI methodology integration boundary](08-project-crosswalks/uci-methodology-integration-boundary.md) | Proposed boundary between Codex-Guidas, UCI and the two 33 frameworks |
| [Lesson template](09-templates/lesson-template.md) | Standard format for new entries |
| [Knowledge application record](09-templates/knowledge-application-record.md) | Record meaningful use of a prior lesson in another project |
| [Framework Assessment Record](09-templates/framework-assessment-record.md) | Proposed evidence-linked record for bounded framework assessments |
| [Defect Intelligence](11-defect-intelligence/README.md) | Defect intake, similarity search, verification and learning loop |
| [33-Perspective Register](doctrines/33-perspective-master-register.md) | Proposed lenses for evidence-led, proportionate decision review |

## Find a prior lesson or defect

Run the local search tool before triage or implementation:

    python scripts/codex.py search "partial write storage"
    python scripts/codex.py search "hydration failure" --project SOULSYNCMOBILE
    python scripts/codex.py review-queue
    python scripts/codex.py validate

Search results are candidate records, not a root-cause verdict. Inspect the evidence and applicability boundary before reusing a control.

## How methodology and knowledge work together

Use the [methodology–knowledge architecture](docs/methodology-knowledge-architecture.md) for consequential investigations and decisions. It keeps four responsibilities distinct: reasoning methodology, specialist assessment instruments, Codex-Guidas institutional memory and each owning project's authority. A worked, bounded example demonstrates how to apply a relevant lesson without assuming identical root cause or transferring proof.

## Reusable knowledge packs

The [Reusable Knowledge Packs](packs/README.md) directory provides bounded, versioned units that can be copied into existing repositories or used to seed new ones. It includes an adoption record, machine-readable manifest, provenance rules and explicit maturity limitations. Teams can fork the whole repository or selectively adopt one pack; copying a pack does not transfer project-specific authority or prove its controls.

## Technical integrity framework

The [Tri-Tier 33 Framework](doctrines/tri-tier-33/README.md) assesses codebase (Mind), persistence (Body), user interface (Spirit) and their seven Harmony seams. It is a proposed v0.3.0 technical instrument, distinct from the broader 33-Perspective strategic review. Its 99 tiers are proportionate assessment lenses, not 99 mandatory manual exercises or a certification.

## Philosophy and doctrine

The [doctrines](doctrines/README.md) record how we reason, build for human realities, sustain a portfolio and communicate uncertainty. They guide decisions but do not substitute for project-specific controls or evidence. The [invariants catalogue](03-architecture/invariants-catalogue.md) translates recurring boundaries into practical checks.

## Evidence and status discipline

Entries distinguish **Observed**, **Derived**, **Proposed**, **Verified** and **Superseded** knowledge. Historical project notes are not a fresh repository audit. Verify exact source artifacts, full commit hashes, test runs and current status before relying on them as release or audit evidence.

A passing test proves only the tested cases in the recorded environment. A design is not implementation. A build is not runtime verification. Synthetic data is not market demand. A prototype is not a validated product.

## Contribution rule

See [CONTRIBUTING.md](CONTRIBUTING.md), the [canonical record taxonomy](00-foundation/record-taxonomy.md) and the [metadata schema](00-foundation/metadata-schema.md). Pull requests are checked for record metadata, ID uniqueness, index coverage and local Markdown links.

Every significant lesson should include its source, context, date, evidence class, impact, root-cause confidence, corrective/preventive action, verification method and residual risk. Do not promote a proposal to a verified practice without reproducible evidence.

Transfer principles, not assumptions: a technique must be adapted and re-validated in each project's context.

## Initial knowledge import

The first import is a curated synthesis from prior work on ScoutSA, SoulSync 3, SoulSyncMobile, NAVIGRE and the UCI threat-intelligence concept. It is intentionally conservative where current repository evidence has not yet been re-audited.

## Source archaeology

The initial source audit is recorded in [Repository Archaeology — 2026-11-18](10-source-audits/2026-11-18-repository-archaeology.md). It inspected selected primary files and commits across ScoutSA, SoulSync 3, SoulSyncMobile and NAVIGRE. It is a partial audit, not a fresh test execution. The [33-Tier Framework method](02-methodologies/33-tier-framework.md) is also indexed here; its own source explicitly leaves detailed specification and validation of all 33 tiers as open work.

## UCI relationship boundary

Codex-Guidas is a reusable engineering knowledge base, not an institutional command layer. UCI maintains its own proposed institutional governance; projects retain their own implementation and release authority. The UCI cross-reference is informational and does not make the proposed charter binding on Codex-Guidas or other projects.
