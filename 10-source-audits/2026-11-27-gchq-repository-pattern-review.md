# External Repository Pattern Review — GCHQ Repositories

**Review date:** 2026-11-27  
**Repository:** `Moshoeshoe333/Codex-Guidas`  
**Review type:** Selective source inspection and transferable-pattern assessment  
**Status:** **DERIVED LEARNING / PROPOSED ADAPTATIONS — NOT A PRODUCT AUDIT, TEST RUN, OR IMPLEMENTATION AUTHORIZATION**

## 1. Purpose and method

This review examined selected source and documentation surfaces from six public GCHQ repositories to identify engineering practices that may strengthen our portfolio and Codex-Guidas. It extends the CyberChef review with Bailo, Stroom, Sleeper, LD-Explorer and Coreax.

The reviewed repository refs were:

| Repository | Branch / exact reviewed HEAD | Main subject |
|---|---|---|
| [CyberChef](https://github.com/gchq/CyberChef) | `master` — `2d82ad577c8a99a279b65deb7c601e614f655d60` | Local-first composable data operations |
| [Bailo](https://github.com/gchq/Bailo) | `main` — `bea1713706f710bc776fcc5a1460d80f61bcd59a` | Governed machine-learning lifecycle and artefact management |
| [Stroom](https://github.com/gchq/stroom) | `master` — `d6d3a22117bd56730ad7ca6f9ac232c6c40cad0c` | High-volume ingest, transformation, storage and analysis |
| [Sleeper](https://github.com/gchq/sleeper) | `main` — `746a08b4aa746955a478429efb8cdfaee13eda3f` | Serverless data storage and asynchronous ingest |
| [LD-Explorer](https://github.com/gchq/LD-Explorer) | `main` — `2f539662243404e8fcbdaec668fe1ecf6a349889` | Browser-based linked-data exploration and validation |
| [Coreax](https://github.com/gchq/coreax) | `main` — `141d091fb44500f908fe0c6d011bf9898137f614` | Coreset algorithms and empirical dataset summarisation |

Selected materials included READMEs, development/security guidance, core source files, design notes, data-ingest documentation, schema validation code, and test/benchmark descriptions. No repositories were cloned or built, and no test suites, benchmarks, or security scans were executed in this review. The findings below are therefore **source observations and derived lessons**, not independent verification of the external projects' runtime properties or of our own products.

## 2. Repository-specific observations

### 2.1 CyberChef — composable, inspectable operations

Inspected: [README](https://github.com/gchq/CyberChef/blob/2d82ad577c8a99a279b65deb7c601e614f655d60/README.md), [AGENTS.md](https://github.com/gchq/CyberChef/blob/2d82ad577c8a99a279b65deb7c601e614f655d60/AGENTS.md), [Dish](https://github.com/gchq/CyberChef/blob/2d82ad577c8a99a279b65deb7c601e614f655d60/src/core/Dish.mjs), [Operation](https://github.com/gchq/CyberChef/blob/2d82ad577c8a99a279b65deb7c601e614f655d60/src/core/Operation.mjs), [Recipe](https://github.com/gchq/CyberChef/blob/2d82ad577c8a99a279b65deb7c601e614f655d60/src/core/Recipe.mjs), and [security policy](https://github.com/gchq/CyberChef/blob/2d82ad577c8a99a279b65deb7c601e614f655d60/SECURITY.md).

Observed design patterns:
- Operations are composed into a recipe, with declared input/output data types and argument validation.
- The `Dish` abstraction distinguishes data types rather than treating every input as an untyped string.
- Breakpoints and step-through execution make intermediate transformations inspectable.
- The project prefers client-side processing where practical, separates large optional modules, and documents resource-exhaustion, XSS and prototype-pollution hazards.
- The security policy itself cautions that the tool does not guarantee the correctness or security of cryptographic operations.

Transferable lesson: use small, typed, independently testable stages only where the domain genuinely has a multi-stage workflow. Show stage outcomes and reasons where this improves diagnosis, but do not confuse a local transformation result with truth, authorization or approval.

### 2.2 Bailo — lifecycle governance, revisions and artefact scanning

Inspected: [README and logical flow](https://github.com/gchq/Bailo/blob/bea1713706f710bc776fcc5a1460d80f61bcd59a/README.md), [ModelCardRevision](https://github.com/gchq/Bailo/blob/bea1713706f710bc776fcc5a1460d80f61bcd59a/backend/src/models/ModelCardRevision.ts), [Review model](https://github.com/gchq/Bailo/blob/bea1713706f710bc776fcc5a1460d80f61bcd59a/backend/src/models/Review.ts), [ModelScan connector](https://github.com/gchq/Bailo/blob/bea1713706f710bc776fcc5a1460d80f61bcd59a/backend/src/connectors/artefactScanning/modelScan.ts), and [security policy](https://github.com/gchq/Bailo/blob/bea1713706f710bc776fcc5a1460d80f61bcd59a/SECURITY.md).

Observed design patterns:
- Model cards have explicit revisions, version numbers, authorship and timestamps; a uniqueness constraint addresses simultaneous update races.
- Reviews are represented by distinct review kinds and required fields rather than one ambiguous generic record.
- The application separates routes, services, repositories, persistence models and pluggable connectors for authentication, authorization, auditing and artefact scanning.
- The scanner checks file size and supported extensions before processing and distinguishes completed, skipped/unsupported and error outcomes.
- Stroom integration is optional and used to send event logging for later analysis; it is not a required dependency for every deployment.

Transferable lesson: treat a lifecycle record, its revisions, its review/approval and its artefact-scan outcome as separate facts. Unsupported, skipped or failed scanning is not a clean scan. Versioned schemas and human review can improve governance where models or controlled artefacts genuinely exist.

### 2.3 Stroom — raw-source preservation and transformation visibility

Inspected: [README](https://github.com/gchq/stroom/blob/d6d3a22117bd56730ad7ca6f9ac232c6c40cad0c/README.md), [document audit design note](https://github.com/gchq/stroom/blob/d6d3a22117bd56730ad7ca6f9ac232c6c40cad0c/stroom-docstore/design/doc_audit.md), and selected pipeline stepping tests including [TestTranslationStepping](https://github.com/gchq/stroom/blob/d6d3a22117bd56730ad7ca6f9ac232c6c40cad0c/stroom-app/src/test/java/stroom/pipeline/task/TestTranslationStepping.java).

Observed patterns:
- The README describes raw ingested data remaining available while pipelines transform, normalise and enrich it.
- Pipeline development supports stepping/debugging rather than treating the final transformed output as the only observable.
- Search indexes may have different retention periods; statistics and dashboards provide operational visibility.
- The document-store audit note proposes typed audit actions, snapshots and audit-to-snapshot links. This specific file is a design document and is not treated here as proof that the full proposed design is deployed.

Transferable lesson: preserve original evidence separately from derived/normalised representations where lawful and necessary; record transformation identity/version and lineage; make reprocessing and correction explainable. Retention must still follow approved purpose, minimisation, access and deletion controls—raw retention is not an excuse for indefinite storage.

### 2.4 Sleeper — ingest state, batching and cost/latency trade-offs

Inspected: [README](https://github.com/gchq/sleeper/blob/746a08b4aa746955a478429efb8cdfaee13eda3f/README.md), [standard ingest](https://github.com/gchq/sleeper/blob/746a08b4aa746955a478429efb8cdfaee13eda3f/docs/usage/standard-ingest.md), [ingest batcher](https://github.com/gchq/sleeper/blob/746a08b4aa746955a478429efb8cdfaee13eda3f/docs/usage/ingest-batcher.md), and ingest status/tracker source and tests.

Observed patterns:
- Ingest is asynchronous; job IDs and separate status/reporting surfaces make progress inspectable.
- Batching trades the time before data becomes queryable against storage/request cost and processing efficiency.
- Batch configuration includes minimum/maximum size and maximum file age; missing or unmatched file paths fail rather than silently producing a successful ingest.
- The batcher exposes pending and already-batched files through reports.
- Some bulk-import partitioning assumes an input sample is representative; the documentation calls out that assumption and the risk of simultaneous jobs doing duplicate work.

Transferable lesson: do not add queues, batching or cloud infrastructure merely because a large-scale platform uses them. Introduce them only after measured volume, latency and cost justify it, and make queued, accepted, rejected, running and completed states observable.

### 2.5 LD-Explorer — read-only linked-data exploration and schema validation

Inspected: [README](https://github.com/gchq/LD-Explorer/blob/2f539662243404e8fcbdaec668fe1ecf6a349889/README.md), [SHACL validation](https://github.com/gchq/LD-Explorer/blob/2f539662243404e8fcbdaec668fe1ecf6a349889/src/lib/util/shacl.ts), [SPARQL validation](https://github.com/gchq/LD-Explorer/blob/2f539662243404e8fcbdaec668fe1ecf6a349889/src/lib/querying/sparqlUtils.ts), and [two-source federation journey](https://github.com/gchq/LD-Explorer/blob/2f539662243404e8fcbdaec668fe1ecf6a349889/e2e/tests/journeys/federation-with-two-sources.spec.ts).

Observed patterns:
- The app is described as browser-only; its data-source interactions are read-only and source configuration/data persist in memory only.
- It can explore local and remote linked-data sources and federate queries across active sources.
- It validates SPARQL syntax and can apply SHACL shapes to combined local data sources.
- Its validation summary exposes conformance, individual constraint findings, data/shape counts and source count.

Transferable lesson: for a genuine cross-source relationship problem, a read-only exploration stage and explicit schema/constraint validation can help identify inconsistencies before committing data changes. RDF, SPARQL or SHACL are optional tools, not a required data model for our projects. Query validity and shape conformance do not establish that source claims are true.

### 2.6 Coreax — representative reduction requires measured fidelity

Inspected: [README](https://github.com/gchq/coreax/blob/141d091fb44500f908fe0c6d011bf9898137f614/README.md), [benchmark methodology](https://github.com/gchq/coreax/blob/141d091fb44500f908fe0c6d011bf9898137f614/documentation/source/benchmark.rst), and unit/integration/performance test structure.

Observed patterns:
- Coresets seek a smaller weighted subset that approximates selected statistical properties of a larger dataset; they are not equivalent to an arbitrary sample.
- The benchmark compares multiple methods, sizes and metrics, includes random sampling and full-data baselines, and repeats stochastic runs with different seeds.
- The documentation identifies trade-offs introduced by dimensionality reduction and MapReduce and notes that those steps can affect quality.
- Performance is considered alongside downstream task quality rather than time alone.

Transferable lesson: representative reduction is an analytical approximation, not evidence preservation. Any future summarisation must be evaluated against a full-data baseline and simple sampling baseline, across relevant metrics and repeated seeds. Preserve rare, high-severity and legally/materially significant records for full inspection; never let a compressed subset become the source of truth for incident or safeguarding decisions.

## 3. Portfolio adoption assessment

| Product / repository | Useful transfer | Decision in this review |
|---|---|---|
| Codex-Guidas | Capture reusable patterns, provenance, evidence class, applicability and non-adoption boundaries. | **ADOPT AS KNOWLEDGE**, not as a product architecture mandate. |
| UCI-Foundation | Source-preserving staged intelligence intake, versioned transformations, explicit scan states, bounded read-only source exploration and cautious analytical sampling. | **ADD TO PROPOSED METHODOLOGY ONLY**. No collection, scanning service, publication, deployment or customer activity is authorized. |
| ScoutSA | Reviewable steps and version-aware evidence may be useful later, but current safeguards, unresolved semantics, external-validation priority and implementation holds dominate. | **NO PROJECT-LEDGER CHANGE**. Avoid duplicate governance and no gate movement. |
| SoulSync 3 | Explicit types, immutability, golden vectors and deterministic contract evidence already dominate its current work. Generic recipe processing and coreset reduction add no demonstrated value to Coordinate99. | **NO PROJECT-LEDGER CHANGE**. Preserve current Python reference and ratification boundaries. |
| SoulSyncMobile | Offline layered threat analysis and adversarial fixtures already align with several patterns; a targeted source check identified a narrow review question about intermediate URL-parse outcomes. | **BOUNDED METHODOLOGY-LEDGER NOTE ADDED** (MD-CYBERCHEF-001); no application code change. Preserve runtime-evidence priority and G-BOOT OPEN. |
| NAVIGRE / Mall-Navigre | Its existing freshness → authorization → route → operational state → verified result chain already separates the critical truths. Gate 3 remains frozen and route/geometry evidence remains bounded. | **NO PROJECT-LEDGER CHANGE**. Do not add generic recipe/RDF infrastructure or change any gate. |

These non-adoption decisions are intentional. Repeating an existing control or adding architecture without an evidenced gap would reduce the value of the ledgers.

## 4. Rules carried into Codex-Guidas

1. Keep raw source, normalized data, derived analysis, human review and publication decision distinct.
2. Treat each material transformation as versioned and reproducible where feasible; record explicit skipped, unsupported, failed, unknown and completed outcomes.
3. Use typed contracts and bounded resource limits at untrusted input boundaries.
4. Retain human authorization for consequential decisions; intermediate processing results do not grant authority.
5. Use scale infrastructure only after representative workload, cost and latency evidence justify it.
6. Treat statistical reduction as an approximation; prove fidelity and preserve the complete source evidence.
7. Use read-only federation and formal data-shape validation only for a demonstrated cross-source problem.
8. Transfer principles, not frameworks or dependencies. Reassess fit, cost, security, maintainability and project authority locally.

## 5. Reusable intake method

This review now serves as an example record for the [External Repository Learning Method](../02-methodologies/external-repository-learning.md), using the [External Repository Review Record template](../09-templates/external-repository-review.md). Future reviews should reuse the method and template, not copy this review's candidate patterns or assume the same projects have the same needs.

## 6. Evidence limitations

- This is selective static source inspection at the exact branch heads listed above; branches can advance after this review.
- No code was executed, no tests were run, no security posture was independently tested and no benchmarks were reproduced.
- A design document, README statement, test file or architecture diagram is not itself runtime evidence.
- No product implementation, dependency selection, cloud architecture, data retention decision, legal conclusion, project gate transition or operational authorization follows from this review.
- All receiving projects must re-check the cited source, scope and current repository state before relying on an adoption decision.

**Governing rule:** learn broadly; adopt narrowly; verify locally; preserve project authority.


### Post-review refinement — SoulSyncMobile (2026-11-27)

After the portfolio table was drafted, the current SoulSyncMobile threat-analysis source was checked at application commit [`1f50bd3387c61d51868140ec3776b94150a2d4c6`](https://github.com/Moshoeshoe333/SOULSYNCMOBILE/commit/1f50bd3387c61d51868140ec3776b94150a2d4c6). The analysis identified one bounded, non-defect review question: URL parse exceptions in the current classifier skip that candidate, while the public result does not expose a separate parse outcome. A short reminder was therefore added to the independent [SoulSyncMobile forensic ledger](https://github.com/Moshoeshoe333/SOULSYNCMOBILE-ledger/blob/main/methodology-delta.md). It does not change the application, scoring, thresholds, policy mapping, or G-BOOT state. The original “no change” assessment remains valid for the other portfolio projects.

### Post-review refinement — agent instruction patterns (2026-11-27)

A follow-up inspection examined agent/developer guidance at the same repository heads already listed above:

| Repository / source | Exact reviewed revision | Observed operating-guidance pattern |
|---|---|---|
| [Bailo AGENTS.md](https://github.com/gchq/Bailo/blob/bea1713706f710bc776fcc5a1460d80f61bcd59a/AGENTS.md) | `bea1713706f710bc776fcc5a1460d80f61bcd59a` | Describes the monorepo and layer boundaries; provides verified commands by component; distinguishes unit, integration and end-to-end tests; records runtime/tool versions, code conventions, security controls and contribution rules. |
| [Stroom AGENTS.md](https://github.com/gchq/stroom/blob/d6d3a22117bd56730ad7ca6f9ac232c6c40cad0c/AGENTS.md) | `d6d3a22117bd56730ad7ca6f9ac232c6c40cad0c` | Leads with high-impact agent rules; records project-specific Git and branch boundaries, human-only issue/PR actions, generated and third-party paths, specialized UI guidance, coding conventions and required build checks. |
| [Sleeper developer guide](https://github.com/gchq/sleeper/blob/746a08b4aa746955a478429efb8cdfaee13eda3f/docs/developer-guide.md) | `746a08b4aa746955a478429efb8cdfaee13eda3f` | Uses a linked-document model for environment setup, build and deployment tools, module architecture, coding conventions, test strategy, validation and specialized development workflows. No root AGENTS.md was found at this reviewed revision. |

**Derived pattern:** effective agent guidance is a local operating contract, not a universal prompt. It should tell an agent what repository it is in, which boundaries it must preserve, what actions it may take, which commands are valid, what material is protected, what proof is required and when human review is mandatory. A concise root guide can link to specialist documents rather than duplicating them.

**Important non-transfer decision:** do not adopt the GCHQ repositories' individual Git permissions, language conventions, technology versions, build commands or contribution rules as portfolio-wide defaults. These are project-owned policies and legitimately differ. At the receiving project, inspect the current instructions and require an explicit owner decision for consequential permissions such as commits, pushes, history changes, issue/PR operations, deployments, production data and spending.

**Codex-Guidas refinement:** a proposed [Agent Instructions Template](../09-templates/agent-instructions-template.md) has been added for project owners to adapt. It is a template only; it does not create or ratify an AGENTS.md in ScoutSA, SoulSync, SoulSyncMobile, NAVIGRE or UCI. Lesson [CG-050](../01-lessons-learned/ledger.md) records the derived control.

**Evidence limits:** this was static document inspection at the exact revisions above. No external repository was cloned or executed; no commands, builds, test suites, deployments or security checks were run. The absence of a root AGENTS.md in Sleeper does not imply an absence of its developer or contribution rules.
