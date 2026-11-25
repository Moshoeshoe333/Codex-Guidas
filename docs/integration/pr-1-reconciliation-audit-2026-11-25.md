# PR #1 Reconciliation Audit — 2026-11-25

**Status:** Review artifact; no integration authorization  
**Target:** `codex/retrieval-enforcement-2026-11-19` into current `main`  
**Reviewed refs:** current `main`; PR #1 feature branch  
**Review method:** GitHub compare metadata and read-only inspection of selected source files. No local checkout, test execution, workflow execution, merge, rebase or mainline write was performed.

## 1. Executive finding

PR #1 contains useful structured-record, retrieval, assurance and CI foundations, but it is not safe to merge or rebase as-is. The branch is **44 commits ahead and 40 behind** current `main`. Its compare reports 84 changed paths, including 41 new lesson records, a rewritten lesson ledger, new scripts/tests and workflow/configuration files.

Current `main` contains newer Opportunity Exposure material absent from the feature branch's lesson migration. A full read of the canonical lesson ledger confirms that **CG-042 is already a formal lesson entry** at the end of `01-lessons-learned/ledger.md`. It is a derived heuristic linked to external field note `OFN-001`, explicitly not empirically validated or project-verified. The innovation register's `OFN-001 / CG-042` reference is therefore consistent with the lesson ledger. PR #1's archive and individual lesson files stop at CG-041, so CG-042 must be migrated as an existing lesson, not newly invented or omitted. The complete GitHub compare inventory lists exactly 41 added paths under `01-lessons-learned/lessons/`: `CG-001.md` through `CG-041.md`, with no additional lesson record path. Current `main` therefore has 42 canonical ledger IDs versus 41 individual lesson files on the feature branch; the feature branch is missing exactly one current canonical ID, CG-042.

## 2. Blocking integrity conditions

### R1 — Preserve and migrate existing CG-042

- The current `main` lesson ledger contains CG-001 through CG-042, including a formal CG-042 row at the end of the ledger.
- CG-042's lesson statement is: “Deliberately widen exposure to relevant opportunities, but separately measure discoverability, access, trust and realised outcomes.”
- Its origin is *The Luck Field Manual* / Polymath Investor (2026-10-05), with internal field note OFN-001.
- Its evidence class is **Derived heuristic; not empirically validated or project-verified**. Its downside, privacy, safety and framework-separation guardrails must remain attached.
- The field note and three experiment records are present on current `main`; they must be preserved during integration.
- PR #1's archived ledger and individual lesson files stop at CG-041. Do not infer that its 2026-11-19 archive supersedes the newer CG-042 entry.

**Required resolution:** migrate the existing CG-042 wording, origin, evidence class, reusable control and field-note cross-reference without promoting its status. Preserve OFN-001 and all experiment records. Do not rewrite the heuristic as a verified control or treat the experiment registrations as completed results.

### R2 — ID allocation must not collide with unmigrated legacy IDs

The proposed `scripts/new_record.py` `next_id()` implementation scans only `01-lessons-learned/lessons/CG-*.md`. Current `main` stores CG-001 through CG-042 in the monolithic ledger and has no individual lesson directory in its tree.

If the allocator is introduced before the complete migration, it can allocate an ID already present in the legacy ledger. The concrete first-collision case is: legacy ledger contains CG-001–CG-042, the individual-record directory is absent/empty, and the allocator proposes CG-001 instead of the next unused ID. This is a migration-order defect, not a theoretical concern.

**Test gap observed:** the inspected `tests/test_codex.py` imports and exercises `scripts/codex.py`; it does not import or test `scripts/new_record.py`. The allocator therefore has no visible regression coverage in that suite for legacy-ledger collisions.

**Required resolution:** either (a) migrate all current canonical lesson IDs into individual records and validate uniqueness before enabling the allocator, or (b) make the allocator check both individual records and the legacy ledger during a staged migration. Add a direct allocator regression test where the legacy ledger contains CG-042 but the individual-record directory does not; the next allocated ID must be CG-043. Also test duplicate/corrupt ID inputs and verify the migrated individual-record set includes CG-001 through CG-042 exactly once.

### R3 — Ledger/index transition must be atomic at repository level

PR #1 changes `01-lessons-learned/ledger.md` from a substantive register into an index and adds `ledger-archive-2026-11-19.md`. The archive preserves the pre-split ledger through CG-041, but it does not contain the later OFN-001 field note or experiment portfolio.

**Required resolution:** reconcile the full current mainline ledger first; preserve the historical archive as historical, not as the latest source of truth; build the new index from all migrated records; validate exact set equality between record IDs and index IDs.

## 3. Positive design elements observed

- `00-foundation/record-taxonomy.md` distinguishes lesson lifecycle status, defect state, severity, evidence class and verification status.
- `scripts/codex.py` provides deterministic metadata validation, local-link validation, keyword/tag retrieval and a pending-verification queue.
- The CLI explicitly warns that a retrieval miss is not proof that no related record exists and that a match is not proof of same cause.
- Verified-claim validation requires evidence references and named author/auditor/ratifier declarations, while the taxonomy states that CI cannot authenticate evidence quality or authority.
- `scripts/build_index.py` declares Markdown records as the source of truth and emits a derived JSON retrieval index.
- The proposed workflow includes tests and integrity checks. These are design assets only until executed on the final integrated commit.

## 4. Additional review conditions

| ID | Area | Required check before acceptance |
|---|---|---|
| R4 | Record metadata | Review every migrated record for preserved wording, origin, source path, project scope, status and verification boundary. Migration metadata must not imply source re-audit. |
| R5 | Search | Test exact, partial, multi-term, tag, project, type and negative queries; document that all-term matching can miss synonyms and semantic equivalents. |
| R6 | Evidence parsing | Test malformed frontmatter, duplicate keys, malformed evidence tables, dangling evidence IDs and placeholder values. |
| R7 | Record creation | Source-level risk: `create_record()` writes the new Markdown file before `insert_table_row()` updates the ledger/register. If the register update fails, the record may remain orphaned. Define atomic or recoverable semantics; inject failure between writes and assert rollback or a detectable/recoverable incomplete state. Also test existing targets, malformed/missing register headers and retry behaviour. |
| R8 | Assurance register | Validate JSON/schema/path references and confirm every assurance claim remains explicitly proposed or unassessed unless supported by evidence. |
| R9 | CI | Confirm workflow triggers, permissions, action provenance, runtime versions and exact-head execution. No passing status is currently established for the PR #1 head in this review. |
| R10 | Current mainline | Preserve current README, project innovation register, Opportunity Exposure note and experiments; inspect all overlapping paths before transplanting feature changes. |

## 5. Integration sequence

1. Freeze the current mainline snapshot and record its exact SHA.
2. Build a migration inventory of all lesson IDs on current mainline and on the feature branch. The source compare currently establishes 42 canonical mainline ledger IDs (CG-001–CG-042) and 41 feature-branch individual files (CG-001–CG-041); re-run this inventory at integration time against the then-current refs.
3. Reconcile CG-001–CG-041 against the current ledger; do not assume metadata migration independently verifies source claims.
4. Migrate the existing CG-042 lesson verbatim in meaning, preserving its Derived heuristic classification and OFN-001 provenance.
5. Resolve the ID allocator's legacy-collision risk and add the regression case where a legacy ledger ending at CG-042 yields CG-043 as the next ID.
6. Rebuild the index and assert exact record/index ID-set equality for all canonical lesson records, CG-001 through CG-042.
7. Port the retrieval scripts, tests and workflow in a focused integration branch; review file-level differences against current mainline.
8. Execute all checks on the exact proposed head and inspect the run SHA, logs and failures.
9. Submit the integrated branch for review. Do not merge until checks, review and maintainer ratification are complete.

## 6. Evidence boundary

This audit is a **read-only source review** of selected files and GitHub compare metadata. It does not establish that the scripts or tests execute successfully, that the proposed workflow is active, that GitHub branch protection is configured, or that the assurance register is operationally effective.

No lesson status, project gate, external project authority or implementation state is changed by this document.

**Decision:** PR #1 remains unmerged and requires a migration-safe integration pass.

## 7. Migration acceptance specification (proposed; not executed)

This section defines the minimum evidence required before a migration branch can be accepted. It is an acceptance contract, not authorization to implement or merge.

| Gate | Acceptance criterion | Required evidence | Failure disposition |
|---|---|---|---|
| M1 — Snapshot | Record exact base-main and feature-branch SHAs; repeat the inventory against those immutable refs. | Commit SHAs, compare output and path inventory. | Stop if refs move or inventory cannot be reproduced. |
| M2 — ID inventory | Canonical source IDs and migrated record IDs each contain CG-001 through CG-042 exactly once. No missing, duplicate, malformed or unexpected IDs. | Machine-readable ID sets plus human-readable mismatch report. | Reject migration; do not allocate new IDs. |
| M3 — Content preservation | Each migrated record preserves the source lesson's meaning, origin, evidence class, reusable control, limitations and project scope. | Per-ID source-to-target reconciliation; explicit exception log for any intentional editorial change. | Reject silent rewrites or unsupported metadata enrichment. |
| M4 — CG-042 provenance | CG-042 retains the Luck Field Manual / Polymath Investor origin, 2026-10-05 date, OFN-001 link, and “Derived heuristic; not empirically validated or project-verified” boundary. Privacy, safety, quality and downside guardrails remain. | Exact source/target comparison and link validation for the field note and experiment records. | Reject omission, promotion, or treatment of experiment registration as outcome evidence. |
| M5 — ID allocator | With legacy ledger IDs through CG-042 and an absent/empty individual-record directory, next lesson ID is CG-043. With migrated IDs through CG-042, next ID is also CG-043. | Direct unit tests against temporary repository fixtures. | Block allocator release until collision is impossible under the supported migration state. |
| M6 — Index integrity | Markdown records remain authoritative; generated index IDs equal record IDs exactly, with no duplicates, omissions or dangling paths. Rebuilding twice produces identical output for unchanged inputs. | Index build logs, set-equality assertion, link/path validation and deterministic rebuild comparison. | Reject index drift; regenerate from source records, never hand-edit derived output as authority. |
| M7 — Record-write recovery | Failure between record-file creation and register/index update cannot silently leave an apparently successful partial record. Retry and pre-existing-target behaviour are deterministic. | Fault-injection tests for write/update failure, malformed or missing register header, existing target, and retry after failure. | Require rollback or an explicit detectable/recoverable incomplete state; no silent orphan. |
| M8 — Retrieval behaviour | Exact, partial, multi-term, tag, project and type queries return expected fixtures; negative queries do not fabricate results. Known all-term/synonym limitations are documented. | Query fixture matrix with expected IDs and observed output. | Fix false results or document bounded recall; never claim semantic completeness. |
| M9 — Validation boundaries | Malformed frontmatter, duplicate keys/IDs, dangling evidence refs, malformed evidence tables and placeholder claims fail safely. Derived/Proposed lessons are not promoted by migration. | Negative test results and record-status diff. | Reject silent coercion, auto-promotion or evidence-class inflation. |
| M10 — Workflow assurance | Required workflow runs on the exact proposed integration SHA; inspect triggers, permissions, dependencies/actions, runtime and every job result. | Run URL, exact head SHA, job logs and status summary. | No green-by-inheritance from PR head, prior commit or another branch. |
| M11 — Mainline preservation | README, innovation register, OFN-001 field note, experiment records and unrelated current-main content remain intact unless a separately reviewed change explains otherwise. | Changed-path review and targeted source/target comparisons. | Reconcile each overlap; do not overwrite newer mainline work. |
| M12 — Authority and review | Migration does not change project gates, ratification, lesson verification status or external-project authority. Final diff receives independent review and explicit maintainer approval. | Exact-head diff, review record and approval. | Keep PR unmerged; implementation evidence does not self-ratify. |

### Minimum release decision

Acceptance requires all M1–M12. A failed, skipped, unexecuted or unobservable gate is not a pass. Report each gate as PASS, FAIL, NOT RUN or BLOCKED, with a source reference. Do not collapse partial success into a single green status.

The migration may be considered technically acceptable only after exact-head checks and independent review. Merge remains a separate maintainer decision. This specification itself does not authorize implementation, status promotion, or merge.


## 8. Read-only lesson path inventory — 25 November 2026

A direct GitHub Contents API read was performed against the PR #1 feature branch directory:

`01-lessons-learned/lessons/` at `codex/retrieval-enforcement-2026-11-19`.

**Observed path inventory:**
- Directory response contains exactly 41 entries.
- Names are the contiguous sequence `CG-001.md` through `CG-041.md`.
- No `CG-042.md` entry is present.
- The current `main` ledger read contains canonical IDs CG-001 through CG-042.

**Inventory result:** path presence is confirmed for 41/42 canonical IDs; CG-042 is absent from the PR #1 individual-record directory. This independently confirms the one-record path gap described in R1–R3.

**Important limitation:** this is a filename/path inventory, not a per-record content reconciliation. It does not establish that the 41 files preserve the exact wording, provenance, evidence classes, reusable controls, limitations or scope of their corresponding mainline ledger rows. M3 remains NOT RUN until each source/target pair is compared. No record file was changed, and no migration or implementation was performed.


## 9. Per-record content reconciliation — 25 November 2026

A read-only, per-ID comparison was performed for all 41 feature-branch records against the corresponding canonical rows in current `main`'s `01-lessons-learned/ledger.md`. The compared fields were:

- lesson statement/title;
- source/origin;
- evidence-class wording; and
- reusable-control wording.

**Observed result:** all four fields matched for every ID from CG-001 through CG-041 (164 field comparisons; 41 records × 4 fields). No wording mismatch was observed in this comparison.

A separate row-level comparison of current `main` and the PR #1 feature-branch archive `ledger-archive-2026-11-19.md` found 41 archived rows and 42 current-main rows. All 41 shared rows matched exactly after whitespace normalization; the only current-main ID absent from the archive is CG-042.

### Reconciliation disposition

| Scope | Result | Interpretation |
|---|---|---|
| CG-001–CG-041 path inventory | PASS | All 41 expected individual record paths exist exactly once in the feature directory. |
| CG-001–CG-041 core content fields | PASS | Lesson, origin, evidence class and reusable control match the current canonical ledger rows. |
| Shared archive rows | PASS | All 41 archived ledger rows match their current-main counterparts. |
| CG-042 migration | BLOCKED | Canonical current-main row exists; feature archive and individual-record directory omit it. |
| Full 42-record migration completeness | FAIL / BLOCKED | 41/42 records are represented on the feature branch; full-set equality is not met. |
| Metadata semantics beyond compared fields | NOT RUN | Project tags, layer/component taxonomy, lifecycle status, review dates, source-path metadata and verification-status fields require a separate schema/meaning review. |
| Runtime, tests and CI | NOT RUN | No local execution or hosted workflow run was performed for this reconciliation. |

### Metadata interpretation boundary

The individual records contain structured metadata that is not represented in the legacy ledger columns (for example project tags, layer/component labels, lifecycle status, review dates and verification status). Those fields are not proven correct merely because the four core content fields match. In particular, lifecycle status and evidence class are separate concepts and must not be conflated. The migration review must validate the metadata taxonomy and each assigned value against its definitions and source evidence; no status promotion is authorized by this comparison.

### Gate update

- M1 — PARTIAL: the reviewed refs and source paths are identified, but integration-time snapshot re-freeze remains required.
- M2 — FAIL: CG-042 is absent from the feature record set; expected 42, observed 41.
- M3 — PARTIAL: the four core content fields pass for CG-001–CG-041; CG-042 and the additional metadata semantics remain unresolved.
- M4 — BLOCKED: CG-042 has not yet been migrated or compared.
- M5–M12 — NOT RUN: allocator, index, write-recovery, retrieval, negative-validation, workflow, preservation and independent-approval gates remain unexecuted.

This reconciliation is source-level evidence only. It does not authorize implementation, lesson-status changes, or merge.


## 10. Structured metadata semantic review — 25 November 2026

A read-only inspection was performed against the PR #1 feature-branch copies of:

- `00-foundation/record-taxonomy.md`;
- `00-foundation/metadata-schema.md`;
- `09-templates/lesson-template.md`;
- `scripts/codex.py`; and
- all 41 individual lesson-record frontmatter blocks, CG-001 through CG-041.

No source files, metadata, tests, scripts or workflows were changed by this review.

### 10.1 Semantics that are explicitly separated and appear internally coherent

- `status` is the lesson lifecycle classification (Observed, Derived, Proposed, Verified or Superseded).
- `evidence_class` preserves the source's evidence wording and is not a second lifecycle status.
- `verification_status` is separately represented (pending, source-only, not-claimed, verified or blocked).
- `verification_due` is a follow-up date, not a verification result.
- `layer` and `component` are described as retrieval facets, not architecture certification.
- `severity` is not applicable to lesson records unless formally assessed; the inspected lesson records use null.
- `last_reviewed` is explicitly described as the 2026-11-19 structural metadata/content review, not a fresh source audit.
- The inspected records do not claim a Verified lesson or set `verification_status: verified`. Pending verification dates remain tracking metadata, not completion evidence.

These distinctions align with the taxonomy's warning that an allowed status or green metadata validator does not establish the truth of a claim.

### 10.2 Unresolved taxonomy and normalization questions

1. **Layer meanings are not defined.** The schema allows `mind`, `body`, `spirit`, `infra`, `process`, `cross-cutting` and `unknown`, but the taxonomy does not define their intended meaning or provide assignment criteria. Examples include CG-001 using `spirit` with `user-interface`, CG-028 using `mind` with `testing-and-ci`, and CG-033 using `mind` with `immutability`. These may be deliberate retrieval choices; the current documentation does not provide enough criteria to judge them as correct or incorrect.

2. **Component values have no controlled vocabulary or assignment guidance.** The schema says component should be a known component, but neither the taxonomy nor validator supplies an authoritative component registry. The inspected values include `user-interface`, `testing-and-ci`, `safeguarding`, `localization`, `scoring`, `persistence`, `repository-integrity` and `immutability`. The validator checks only string-or-null, so a typo or semantically inconsistent assignment can pass.

3. **Project identifiers are not normalized by a registry.** The records use values such as `SoulSync 3`, `SOULSYNCMOBILE`, `Mall-Navigre`, `ScoutSA`, `UCI` and `cross-project`. These appear to identify distinct projects or scopes, but no canonical identifier map, alias policy or validation rule is defined. This can fragment project-filtered retrieval if equivalent spellings are introduced later.

4. **The phrase “verification_status is a retrieval field” is narrower than its operational use.** The field is also coupled to Verified lifecycle status by validation rules and drives the pending-verification queue. That behaviour is sensible, but the taxonomy should describe it as a verification-tracking state used for retrieval/queueing, not merely a passive retrieval label.

5. **`failure_mode` is free text.** This is useful for nuanced records, but the validator cannot detect inconsistent naming or duplicate concepts. No controlled taxonomy is currently specified. This is a retrieval-quality limitation, not proof that any individual failure-mode value is wrong.

### 10.3 What this review does and does not establish

| Area | Result | Boundary |
|---|---|---|
| Lifecycle/evidence/verification separation | PASS — definition-level | The taxonomy clearly distinguishes these concepts; this does not independently validate every source claim. |
| Required metadata shape in inspected records | PARTIAL | Frontmatter was inspected; no validator or tests were executed. |
| Layer assignment semantics | BLOCKED / underspecified | Allowed values exist, but definitions and assignment criteria are absent. |
| Component assignment semantics | BLOCKED / underspecified | No controlled vocabulary or semantic validator exists. |
| Project identifier normalization | BLOCKED / underspecified | No canonical registry or alias policy exists. |
| Verification tracking interpretation | PARTIAL | Behaviour is visible in schema and code; wording should reflect queue/validation use as well as retrieval. |
| Per-record source-to-metadata correctness | NOT RUN | Requires a source-to-record assignment review; structural consistency cannot prove semantic correctness. |
| Runtime, tests and CI | NOT RUN | No execution was performed. |

### 10.4 Recommended resolution before migration acceptance

Treat these as documentation/schema questions to resolve in a separately reviewed migration proposal:

- Define each layer and provide inclusion/exclusion examples.
- Decide whether components and project identifiers require canonical registries; if yes, publish the registries and a safe alias/migration policy.
- Clarify the operational meaning of `verification_status`.
- Add a per-record metadata rationale or review matrix for layer, component and project assignments, with explicit `unknown`/null where the source does not justify a classification.
- Add tests for invalid layer values, unknown component/project identifiers if registries are adopted, and preservation of lifecycle/evidence/verification distinctions.

Do not bulk-relabel records based on intuition. In particular, the examples above are review questions, not confirmed misclassifications. Any taxonomy or assignment change must preserve historical meaning and be independently reviewed.

### 10.5 Gate impact

- M3 — remains PARTIAL: core content comparison passes for CG-001–CG-041, but semantic correctness of several metadata facets is not established and CG-042 is absent.
- M9 — NOT RUN: the code was inspected, but negative validator tests were not executed.
- M12 — NOT RUN: no independent review or maintainer approval has been recorded.
- M1, M2 and M4–M8, M10–M11 retain the dispositions in Section 9 unless new exact evidence is supplied.

This section records a read-only semantic review. It does not authorize metadata edits, implementation, status promotion, project-gate changes or merge.


## 11. CG-042 source reconciliation and proposed migration target — 25 November 2026

A read-only review of current `main` was performed for:

- `01-lessons-learned/ledger.md` — canonical CG-042 row;
- `06-innovations/opportunity-exposure-field-note.md` — OFN-001;
- `06-innovations/experiments/opportunity-exposure/README.md` — portfolio boundary;
- `OEX-2026-001-career-discoverability.md`;
- `OEX-2026-002-scoutsa-controlled-demonstration.md`; and
- `OEX-2026-003-sme-security-snapshot.md`.

The source row in the current mainline ledger states:

- **Lesson:** “Deliberately widen exposure to relevant opportunities, but separately measure discoverability, access, trust and realised outcomes.”
- **Origin:** External reference, *The Luck Field Manual* / Polymath Investor, 2026-10-05; internal field note OFN-001.
- **Evidence class:** “Derived heuristic; not empirically validated or project-verified”.
- **Reusable control:** “Use bounded, low-cost experiments to increase relevant encounters and make credible work discoverable. Track qualified next steps and outcomes rather than impressions alone. Protect privacy, safety, quality and downside; do not treat visibility or persistence as proof of success.”

### 11.1 Source limitations and application boundaries

OFN-001 identifies the manual as an external practitioner's synthesis / directional heuristic, not an empirically validated causal model. The field note distinguishes it from the 33-tier technical framework and 33-perspective register. Its applications are proposals to test, not approved project requirements.

The experiment portfolio states that its three tracks are pre-registered and are not completed market experiments. Current boundaries include:
- Career discoverability: application-correction work is in progress; the portfolio does not claim a completed outcome or improved response rate.
- ScoutSA: external demonstration remains HOLD pending its own exact-head, audit, independent-review and project-owner acceptance gates.
- SME security snapshot: desk research only; existing public competitors are counter-evidence to a generic market-gap claim, and buyer demand/willingness to pay remain unestablished.

These records are context and boundary evidence. They do not validate the external manual, establish commercial outcomes, or authorise activity in any project. The CG-042 lesson should link to OFN-001 without importing volatile experiment execution status into the lesson's reusable control.

### 11.2 Proposed CG-042 target record (specification only; not created)

The following is a candidate migration target. It is not a committed record and must be compared against the frozen mainline source at integration time.

```yaml
id: "CG-042"
record_type: "lesson"
status: "Derived"
projects: ["cross-project"]
layer: "unknown"
component: null
failure_mode: null
severity: null
origin_date: "2026-10-05"
last_reviewed: "2026-11-25"
verification_due: null
evidence_class: "Derived heuristic; not empirically validated or project-verified"
verification_status: "not-claimed"
source_path: "01-lessons-learned/ledger.md (frozen current-main source ref to be recorded at M1)"
review_scope: "migration_source_and_metadata_review_only; no causal validation or project experiment verification"
tags: ["opportunity-exposure", "discoverability", "access", "trust", "outcomes", "bounded-experiments"]
```

**Candidate record body:**

```markdown
# CG-042 — Deliberately widen exposure to relevant opportunities, but separately measure discoverability, access, trust and realised outcomes.

**Source / origin:** External reference: *The Luck Field Manual* / Polymath Investor, 2026-10-05; internal field note OFN-001.

**Evidence class (preserved):** Derived heuristic; not empirically validated or project-verified.

**Lesson status:** Derived.

## Reusable control

Use bounded, low-cost experiments to increase relevant encounters and make credible work discoverable. Track qualified next steps and outcomes rather than impressions alone. Protect privacy, safety, quality and downside; do not treat visibility or persistence as proof of success.

## Provenance and limitations

This lesson is derived from an external practitioner heuristic and its internal source note, OFN-001. It is not an empirically validated causal model, a guarantee of opportunity or success, or an approved requirement for any project. The field note preserves the source attribution, paraphrase boundary, counterweights and source register.

The three linked opportunity-exposure experiment tracks are separate, pre-registered applications with their own permissions, measures, risks and decision gates. Registration is not execution or outcome evidence. A result in one track does not validate another track or the external manual as a whole.

This external heuristic is separate from the Codex-Guidas 33-tier technical framework and 33-perspective register. Shared use of the number 33 does not establish equivalence or validation.

**Source note:** [Opportunity Exposure Field Note — OFN-001](../06-innovations/opportunity-exposure-field-note.md).

**Verification boundary:** No empirical, causal, market, project-control or outcome verification is claimed by this migration.
```

### 11.3 Field-by-field decision notes

- `status: Derived` preserves the canonical lifecycle classification; do not promote to Verified.
- `evidence_class` preserves the full source wording verbatim; do not shorten it to “Derived”.
- `verification_status: not-claimed` is preferred over `pending`: the record is not asserting a control awaiting a technical rerun. It is a derived external heuristic with no empirical validation claim.
- `origin_date: 2026-10-05` refers to the attributed manual date, not the later internal note date.
- `last_reviewed: 2026-11-25` records this migration-source/metadata review only. It must not be represented as an empirical review.
- `layer: unknown` and `component: null` deliberately avoid inventing a classification while the layer/component taxonomy remains underspecified (Section 10).
- `projects: ["cross-project"]` is a candidate retrieval scope, not evidence that any project has adopted or validated the heuristic.
- The candidate source path must be pinned to the exact frozen mainline commit during M1. Do not let a moving branch name stand in for immutable provenance.
- Tags are retrieval aids only; they are not evidence, authority or status.

### 11.4 CG-042 migration disposition

| Check | Result |
|---|---|
| Canonical source lesson and origin | FOUND in current mainline ledger |
| OFN-001 source note and attribution | FOUND |
| Explicit non-validation boundary | FOUND and must be retained |
| Experiment portfolio and three separate tracks | FOUND; tracks retain independent status/permission boundaries |
| Proposed target wording and metadata | DRAFTED as specification only |
| Target record created on PR #1 | NO |
| Source/target exact comparison | NOT RUN — no target exists |
| Link validation / index inclusion | NOT RUN |
| Empirical or project verification | NOT CLAIMED |

The proposed target uses conservative metadata where taxonomy definitions are absent. It is a migration specification, not permission to create or commit the record. M1 must freeze exact source refs; M2–M4 must be re-run against the actual target; all M5–M12 gates remain governed by Section 7.


## 12. Lesson allocator and record-creation failure analysis — 25 November 2026

Read-only source inspection was performed on PR #1 branch `codex/retrieval-enforcement-2026-11-19` for:

- `scripts/new_record.py`;
- `scripts/codex.py`;
- `scripts/build_index.py`; and
- `tests/test_codex.py`.

No scripts or tests were changed or executed.

### 12.1 Confirmed allocator defect against the legacy-ledger migration state

In `scripts/new_record.py`, `next_id("lesson")` enumerates only:

```python
(root / "01-lessons-learned" / "lessons").glob("CG-*.md")
```

It chooses the maximum number found in those filenames and defaults to zero. It does not inspect `01-lessons-learned/ledger.md`.

**Deterministic consequence:** when the existing ledger contains CG-001 through CG-042 but the individual-record directory is empty (the pre-migration state identified in Sections 8–9), the allocator returns CG-001. That is an ID collision with the canonical source ledger, even though the new individual-record directory itself contains no files.

This is a confirmed source-level defect under the documented migration precondition. The exact runtime reproduction was NOT RUN.

**Required regression cases:**

| Case | Fixture | Required result |
|---|---|---|
| A1 — legacy ledger only | Ledger contains CG-001…CG-042; lesson directory empty | Allocate CG-043 |
| A2 — migrated records | Individual files CG-001…CG-042; ledger/index agrees | Allocate CG-043 |
| A3 — mixed migration | Ledger highest ID 042; files highest ID 040 | Allocate CG-043; never reuse an ID present in either source |
| A4 — file ahead of ledger | Files include CG-043; ledger ends at 042 | Allocate CG-044 or fail closed pending reconciliation; never allocate 043 |
| A5 — duplicate/malformed ledger IDs | Duplicate, malformed or inconsistent references | Fail with actionable diagnostic; do not silently choose a potentially colliding ID |
| A6 — gap in sequence | Existing IDs 001 and 003, no 002 | Allocate max+1 (004), not the first gap, unless a separately approved allocation policy says otherwise |

The allocator must be defined against an authoritative, reconciled ID inventory. During migration, it must account for both legacy and individual-record representations or explicitly refuse allocation until reconciliation completes. It must not treat a missing file projection as proof that an ID is unused.

### 12.2 Record creation is not transactional across the record and register

The inspected `create_record()` sequence is:

1. Determine ID and target.
2. Create target directory.
3. Write the individual record file.
4. Insert the corresponding row into the lesson ledger or defect register.
5. Return the target path.

If step 4 raises (for example, missing/malformed table header, permission or I/O failure), step 3 has already persisted the record. There is no rollback or explicit incomplete-state marker in the inspected function.

This is a confirmed partial-write exposure in source structure. A fault-injection reproduction was NOT RUN.

**Required failure/recovery tests:**

| Case | Injected condition | Required result |
|---|---|---|
| W1 — missing register | Record file write succeeds; register absent | Atomic rollback, or a detectable incomplete state with exact recovery instructions |
| W2 — malformed register | Expected table header absent | No silent orphan; report both target and failed register operation |
| W3 — register write failure | Raise OSError after record write | Roll back created file where safe, or preserve an explicit recoverable transaction marker |
| W4 — retry after failure | Retry same creation after W1–W3 | No duplicate ID, no overwrite, no ambiguous half-complete state |
| W5 — pre-existing target | Target path already exists | Refuse before mutating register or target |
| W6 — successful creation | Valid template and register | Exactly one record and exactly one matching register row |
| W7 — malformed template | Non-quick template has invalid frontmatter delimiter | No record or register mutation |
| W8 — interrupted process | Simulate interruption between record and register writes | Next validation/recovery pass detects the incomplete transaction |

A simple catch-and-delete is not automatically sufficient: rollback must not delete a file that existed before the operation or remove a register row not created by this operation. The implementation proposal should define the transaction boundary and recovery semantics before code is changed.

### 12.3 Existing test coverage does not exercise the allocator

The inspected `tests/test_codex.py` dynamically imports `scripts/codex.py`. Its fixtures and tests cover record parsing, duplicate keys/IDs, validation, evidence references, retrieval, review queue and local links. The inspected file does not import `scripts/new_record.py` or test `next_id()` / `create_record()`.

This is a coverage gap in the inspected test module, not proof that no other test file exists. The full PR test inventory and workflow configuration still require a repository-wide exact-head review.

### 12.4 Index integrity boundary

The inspected `scripts/build_index.py` describes Markdown records as the source for a derived JSON index. The validator in `scripts/codex.py` compares lesson-file IDs with the Markdown ledger's linked IDs. Neither observation alone establishes that the full migration preserves every record's content and metadata, nor that the generated JSON index is byte-deterministic across repeated builds.

Required migration checks remain:
- exact set equality: canonical lesson IDs = individual record IDs = ledger/index IDs = generated JSON IDs;
- uniqueness and no dangling record paths;
- deterministic index rebuild twice from the same immutable source snapshot;
- no source Markdown changes caused by index generation;
- explicit handling of extra, malformed or duplicate IDs.

### 12.5 Disposition and acceptance impact

| Item | Source finding | Status |
|---|---|---|
| Legacy ledger collision | Allocator scans record filenames only; ledger-only CG-001…042 can yield CG-001 | **CONFIRMED SOURCE DEFECT; runtime reproduction NOT RUN** |
| Allocator regression coverage | Inspected test module does not import/test allocator | **CONFIRMED GAP IN INSPECTED MODULE; full test inventory NOT RUN** |
| Partial record/register write | Record file is written before register insertion; no rollback/recovery in inspected function | **CONFIRMED SOURCE EXPOSURE; fault injection NOT RUN** |
| Index determinism and exact migration equality | Build/validation code inspected only in part | **NOT RUN / NOT ESTABLISHED** |

M5 remains NOT RUN and cannot pass until A1–A6 are implemented and executed against the agreed migration states. M7 remains NOT RUN and cannot pass until W1–W8 are addressed with fault-injection evidence. M6 remains NOT RUN until exact-set and deterministic-rebuild evidence is attached. M10 still requires the exact proposed integration SHA and hosted workflow run evidence.

This section is a source-level audit and test specification. It does not modify PR #1, authorize implementation, promote any status, or authorize merge.


## 13. Index integrity, test coverage and hosted workflow audit — 25 November 2026

This section extends the read-only review to the exact PR #1 head:

- PR #1 head: `ea7b36e0e78c79c019bce9982bc419e39eeb7461`
- Comparison base: `6d1c38bb2b29936d059a36750d1cfc70815f4ed3`
- PR #1 branch: `codex/retrieval-enforcement-2026-11-19`
- Comparison: `main...ea7b36e0e78c79c019bce9982bc419e39eeb7461`
- GitHub compare result: `diverged`, 44 commits ahead, 40 behind; 44 commits in the head-side comparison.
- PR #1 remains open and draft.

The following exact-head files were inspected read-only: `scripts/build_index.py`, `scripts/codex.py`, `tests/test_capture_and_index.py`, `tests/test_codex.py`, `00-foundation/metadata-schema.md`, and `.github/workflows/knowledge-integrity.yml`. No code or tests were changed or executed.

### 13.1 Index builder behaviour

The index builder:

- Reads individual Markdown lesson files matching `CG-*.md` and defect files matching `DEF-*.md`.
- Extracts an explicit subset of frontmatter fields and the first H1 title.
- Sorts records by `(id, record_path)`.
- Serializes JSON with stable indentation and a trailing newline.
- Exposes `--check`, which compares an existing output file byte-for-byte with a freshly rendered index.

This is a useful deterministic design at source level. It does not, by itself, prove that a generated index was built or that all canonical sources are reconciled.

### 13.2 Test coverage: determinism claim is stronger than the assertion

The test named `test_index_is_deterministic_and_preserves_explicit_tags` invokes `build_index_data(root)` once. It asserts record count, tag preservation and title extraction. It does not invoke the builder twice, compare serialized output, exercise `render_index()`, or test the CLI `--check` path.

The workflow invokes `build_index.py --output /tmp/knowledge-index.json` and checks that one expected defect ID has a particular tag. It does not invoke `--check`, compare two independent builds, compare all generated IDs to source IDs, or verify that index generation leaves source Markdown unchanged.

Therefore:
- Deterministic sorting/serialization is **SUPPORTED BY SOURCE INSPECTION**.
- Repeated-build determinism is **NOT TESTED BY THE INSPECTED TEST**.
- Workflow enforcement of `--check` or full index equality is **NOT PRESENT IN THE INSPECTED WORKFLOW**.
- No index build or test was executed during this audit.

### 13.3 Cross-source equality and validation boundary

The inspected `codex.py` validator:
- Checks unique IDs across discovered individual lesson and defect record files.
- Compares the set of individual lesson-file IDs with valid linked IDs extracted from `01-lessons-learned/ledger.md`.
- Checks local Markdown links for missing targets.
- Does not, in the inspected validation path, compare a complete canonical ID inventory across legacy lesson rows, lesson files, defect register rows, and generated JSON index records.
- Does not establish semantic equivalence of migrated record content or metadata.

The index builder consumes the individual lesson/defect files; it does not independently reconcile those files against the legacy lesson ledger or defect register before emitting JSON. A generated index can therefore be internally well-formed while a migration or source-reconciliation defect remains elsewhere.

Required acceptance evidence:
1. Define the canonical source inventory and parsing rules for lesson and defect IDs.
2. Assert exact set equality between the agreed canonical source, individual record files, Markdown indexes/registers, and generated JSON index.
3. Assert uniqueness and reject malformed, duplicate, missing and extra IDs.
4. Assert every emitted `record_path` resolves to the intended file.
5. Build twice from the same immutable snapshot and compare exact bytes.
6. Confirm the build/check process does not mutate source Markdown.
7. Exercise both successful and stale/missing-index `--check` cases.

### 13.4 Hosted workflow source review

The workflow is named `Knowledge integrity` and declares:
- Triggers: pushes to `main`, all pull requests, and manual dispatch.
- Workflow permission: `contents: read`.
- Runner: `ubuntu-latest`.
- Python: `3.12`.
- Pinned commit SHAs for checkout and setup-python actions.
- Steps for unittest discovery, knowledge validation, assurance-register validation, fixed-date queue smoke tests, temporary JSON index generation, and tag/search/review-queue smoke tests.

Positive source-level properties:
- Read-only repository permission is declared.
- Third-party GitHub Actions are pinned to full commit SHAs.
- The workflow has no deployment or repository-write step in the inspected file.

Limits and follow-up:
- No explicit `timeout-minutes`, concurrency policy, or Python version matrix is declared.
- Pull requests are not path-filtered; all PRs trigger the workflow.
- Several smoke tests use fixed historical `--as-of` dates and hard-coded expected IDs. Those fixtures must be kept synchronized with the intended source data and should not be confused with a current-date operational review.
- The workflow definition is not execution evidence.

### 13.5 Exact-head hosted evidence

For exact head `ea7b36e0e78c79c019bce9982bc419e39eeb7461`, the connector returned:
- PR-triggered workflow-runs list: empty.
- Combined commit status entries: empty.

The workflow-runs action is documented as returning PR-triggered runs only and the first page. The empty response is therefore recorded narrowly: **no PR-triggered workflow run was returned by this query, and no combined status entries were returned**. This does not prove that no workflow of any trigger type has ever run, and it does not prove a pass.

No hosted workflow pass/fail evidence for the exact head was established in this audit. M10 remains **NOT RUN / NOT ESTABLISHED**.

### 13.6 Updated acceptance disposition

| Area | Finding | Disposition |
|---|---|---|
| Index serialization | Sorted records and stable JSON serialization are implemented in source | SOURCE-INSPECTED; not executed |
| Repeated-build determinism | Named test calls builder once; no repeated comparison | NOT TESTED |
| Workflow index assurance | Builds temporary JSON and checks one known record/tag; no `--check` or full-set equality | INSUFFICIENT FOR FULL INDEX INTEGRITY |
| Cross-source ID equality | Lesson-file/ledger set comparison exists; complete ledger/register/file/JSON reconciliation is not established | PARTIAL |
| Workflow source design | Read-only permission and SHA-pinned actions; no explicit timeout/concurrency/matrix | SOURCE-INSPECTED |
| Exact-head CI evidence | No PR-triggered run returned and combined status list empty for exact head | NOT ESTABLISHED; NOT A PASS |
| Branch integration risk | 44 ahead / 40 behind; diverged | RECONCILIATION REQUIRED; NO BLIND REBASE OR MERGE |

M6 remains NOT RUN until the complete equality, path-integrity, deterministic-rebuild and non-mutation checks are executed against a frozen source snapshot. M10 remains NOT RUN until the exact proposed integration SHA has inspectable hosted workflow evidence. The current empty status response is not a green result.

This section remains a read-only audit. It does not authorize implementation, branch rewriting, status promotion, project-gate changes or merge.


## 14. M1 migration baseline freeze — 25 November 2026

### 14.1 Frozen source revision

The migration baseline is pinned to the immutable current-mainline commit:

- Repository: `Moshoeshoe333/Codex-Guidas`
- Branch at inspection: `main`
- Frozen commit: `6d1c38bb2b29936d059a36750d1cfc70815f4ed3`
- Commit URL: https://github.com/Moshoeshoe333/Codex-Guidas/commit/6d1c38bb2b29936d059a36750d1cfc70815f4ed3
- The repository's latest-commit query returned this same SHA as the current mainline tip at the time of the freeze.
- This is a source snapshot reference, not a branch lock. Any later mainline change creates a new baseline and requires reconciliation; do not silently substitute a moving `main` ref.

### 14.2 Frozen source artifacts and blob identities

| Source artifact | Blob SHA at frozen commit | Purpose |
|---|---|---|
| `01-lessons-learned/ledger.md` | `d2ba7d44d583c7d372e2484b5bd98a4224576003` | Canonical pre-migration lesson ledger and CG-042 source row |
| `06-innovations/opportunity-exposure-field-note.md` | `d6a5e110c0e1ec887f75a96e6c8d2eb61cc8687f` | OFN-001 source attribution, limitations and counterweights |
| `06-innovations/experiments/opportunity-exposure/README.md` | `1f0dd59d0e7f406d4085d08a458b83fbd80fb39e` | Three-track portfolio register and independent status boundaries |
| `06-innovations/experiments/opportunity-exposure/OEX-2026-001-career-discoverability.md` | `eb3a49b392c0a31846cb6c855f2d00d0dcc13472` | Career discoverability track |
| `06-innovations/experiments/opportunity-exposure/OEX-2026-002-scoutsa-controlled-demonstration.md` | `2c42257b432253cc2cd8a4c0a38d5c278b9ac07f` | ScoutSA controlled-demonstration track |
| `06-innovations/experiments/opportunity-exposure/OEX-2026-003-sme-security-snapshot.md` | `29a94b9cd7e1756dd47c10e771a5a126334ee18a` | SME security snapshot track |

The full source contents were fetched at the frozen commit. The blob SHAs above are the exact file identities returned by the repository API.

### 14.3 Canonical lesson inventory check

The frozen `01-lessons-learned/ledger.md` contains 42 distinct lesson IDs:
- First: `CG-001`
- Last: `CG-042`
- IDs are sequential from CG-001 through CG-042 in the parsed ledger table.
- The CG-042 row exactly records: “Deliberately widen exposure to relevant opportunities, but separately measure discoverability, access, trust and realised outcomes.”
- Its origin is the external reference *The Luck Field Manual* / Polymath Investor, dated 2026-10-05, plus internal field note OFN-001.
- Its evidence class is “Derived heuristic; not empirically validated or project-verified”.
- Its reusable control retains bounded, low-cost experiments, qualified next steps/outcomes, privacy, safety, quality and downside protections, and the warning not to treat visibility or persistence as proof of success.

This establishes the pre-migration ledger inventory at the frozen source revision. It does not establish equivalence with PR #1's individual-record projection or generated JSON index.

### 14.4 M1 disposition

| M1 criterion | Evidence | Result |
|---|---|---|
| Immutable baseline commit identified | Exact mainline SHA recorded | PASS |
| Canonical lesson ledger pinned | Exact path and blob SHA recorded | PASS |
| CG-042 source row captured | Exact source row and evidence wording checked | PASS |
| OFN-001 and all three experiment tracks pinned | Exact paths and blob SHAs recorded | PASS |
| Source limitations and separate track boundaries preserved as migration constraints | Source artifacts pinned; Section 11 target specification retained | PASS |
| Full migration target inventory reconciled | PR #1 branch still diverges and CG-042 target absent | NOT RUN |
| Source/target content and metadata equivalence | No CG-042 target record exists on PR #1 | NOT RUN |

**M1 disposition: SOURCE BASELINE FROZEN; MIGRATION RECONCILIATION NOT COMPLETE.** The frozen snapshot is now suitable as the immutable reference for subsequent M2–M4 comparisons. M1's source-freeze subcriteria pass; this must not be represented as approval of the migration or closure of the overall integration gate.

### 14.5 Scope and authority boundary

This phase records source identities and a canonical inventory only. It does not create or modify CG-042 on PR #1, change scripts/tests, alter mainline, rewrite branches, promote a lesson to Verified, authorize any project experiment, or approve a merge. The next phase is a read-only source-to-target reconciliation of all 42 lessons and their metadata against the PR #1 branch at its exact head. Any change to that head invalidates the target-side comparison and requires a fresh exact-head audit.


## 15. Frozen-baseline migration reconciliation — M2 to M4 — 25 November 2026

This review compares PR #1 at exact head `ea7b36e0e78c79c019bce9982bc419e39eeb7461` with the frozen mainline source snapshot `6d1c38bb2b29936d059a36750d1cfc70815f4ed3` recorded in Section 14. The PR #1 head did not change during this read-only comparison.

### 15.1 M2 — inventory and migration coverage

- Frozen source ledger inventory: 42 unique, sequential IDs, CG-001 through CG-042.
- PR #1 individual lesson files: CG-001 through CG-041 (41 records).
- CG-042 individual target file: absent.
- PR #1 retains the archived pre-split ledger containing the 41 earlier lesson rows; the frozen current-mainline ledger contains all 42.
- No duplicate or missing ID was found within the 41-file target sequence itself; the migration is incomplete relative to the 42-record frozen source.

**M2 disposition: PARTIAL / FAIL FOR COMPLETE MIGRATION.** The 41-record projection is present, but CG-042 is missing. Do not treat the PR #1 migration as complete.

### 15.2 M3 — source-to-target content comparison

The earlier four-field comparison in Section 9 was tied to the same frozen mainline base SHA recorded in Section 14. It compared 41 individual target records against the source ledger and found:
- 41/41 lesson titles matched;
- 41/41 origin/source fields matched;
- 41/41 evidence-class wording matched;
- 41/41 reusable-control wording matched;
- all 41 shared archive rows matched;
- CG-042 has no target record and therefore cannot be compared.

This represents 164/164 compared core fields matching across the 41 migrated records. It does not mean every metadata field is identical to the source ledger; the target schema adds retrieval and review metadata that did not exist in the legacy table. Nor does it establish independent re-verification of the lessons' underlying project claims.

**M3 disposition: PARTIAL.** All compared core fields for CG-001–CG-041 match, but the 42-record source-to-target reconciliation is incomplete until CG-042 is migrated and compared field by field.

### 15.3 M4 — metadata semantics review across CG-001–CG-041

The exact-head frontmatter of all 41 individual lesson records was inspected. The schema and taxonomy files were also inspected at the same PR #1 head.

**Observed consistency:**
- Lifecycle `status`, source `evidence_class` and `verification_status` remain separate fields.
- The observed lifecycle values are within the declared lesson vocabulary; no record in the inspected set claims `status: Verified`.
- Verification values are within the declared vocabulary (`pending`, `source-only`, `not-claimed`); no record claims `verification_status: verified`.
- Records marked `pending` carry a `verification_due` date in the inspected set.
- Layer values observed are members of the schema's allowed retrieval values: `mind`, `body`, `spirit`, `infra`, `process`; the schema also allows `cross-cutting` and `unknown`.
- Component values are strings or explicit nulls, consistent with the schema's type rule.
- Dates are represented as ISO dates or null in the inspected records.
- `severity` is null on the inspected lesson records, consistent with the rule that severity is not applicable to lessons absent formal assessment.
- The records' shared `source_path` points to the preserved archived ledger; `review_scope` limits the migration review to metadata/ledger-entry review and explicitly disclaims source re-execution.
- No inspected record claims that migration alone independently verified the underlying source project behaviour.

**Taxonomy limitations remain:**
- The schema declares layer values as retrieval tags but does not define operational meanings or assignment criteria for each layer. Values can therefore be syntactically valid without their semantic assignment being independently justified.
- The component field has no controlled vocabulary or canonical component registry; the strings are usable retrieval facets but cannot be treated as normalized classifications.
- Project identifiers are not governed by a canonical registry/alias policy. Examples in the inspected records include differing forms such as `SoulSync 3`, `SOULSYNCMOBILE`, `Mall-Navigre`, `ScoutSA`, `UCI` and `cross-project`. The evidence does not establish that these names are all aliases or that they should be normalized identically.
- The records do not carry per-field rationale explaining why a specific layer, component or project tag was selected. This prevents an auditor from independently assessing the semantic correctness of every retrieval classification from metadata alone.

These are taxonomy governance and semantic traceability limitations. They are not, on the evidence inspected, proof that a particular individual record has been deliberately or demonstrably misclassified.

**M4 disposition: STRUCTURAL REVIEW COMPLETE; SEMANTIC TAXONOMY OPEN.** The metadata is structurally consistent with the inspected schema rules, but semantic classification cannot be fully certified without controlled definitions, registries and per-record rationale. Do not promote metadata validity into content verification.

### 15.4 Consolidated M1–M4 gate position

| Gate | Result | Reason |
|---|---|---|
| M1 — immutable source baseline | SOURCE FREEZE PASS | Exact mainline SHA and source artifact blob identities pinned in Section 14 |
| M2 — inventory/migration coverage | PARTIAL / FAIL | 41 of 42 source lessons represented; CG-042 missing |
| M3 — source/target core content | PARTIAL | 164/164 compared fields match for CG-001–CG-041; CG-042 not migrated or compared |
| M4 — metadata semantics | STRUCTURAL REVIEW COMPLETE; OPEN | Types/vocabularies are structurally consistent; layer/component/project semantics remain underspecified |

No M2–M4 result authorizes implementation, migration of CG-042, taxonomy changes, branch rewriting, status promotion, or merge. Any subsequent change to the PR #1 head requires re-pinning and re-running the target-side comparison. The next step remains a separately scoped implementation decision after this reconciliation evidence is reviewed.


## 16. Approved-scope execution — isolated allocator work package — 25 November 2026

The user's instruction to proceed is treated as ratification to begin the previously proposed implementation scope, subject to the phase gates and explicit non-scope boundaries. Work has started on a clean branch from the frozen mainline; the diverged PR #1 branch has not been rebased, merged or modified.

### 16.1 New isolated work branch and pull request

- Branch: `codex/integration-core-capture-2026-11-25`
- Base: frozen `main` commit `6d1c38bb2b29936d059a36750d1cfc70815f4ed3`
- Pull request: [PR #5 — reconcile lesson ID allocation across legacy and migrated records](https://github.com/Moshoeshoe333/Codex-Guidas/pull/5)
- Exact PR head at this check: `724058c167775244dd55316abd7dc12725b099fb`
- PR #5 state: open, draft, unmerged; 3 files changed.
- PR #1 remains untouched and diverged.

### 16.2 Implementation scope now present on PR #5

- Lesson ID allocation reads both the canonical lesson ledger and individual lesson filenames, taking the maximum across both representations.
- Legacy bare IDs and migrated Markdown links are accepted.
- Missing or malformed ledger structure, malformed IDs, duplicate ledger IDs, inconsistent link targets and malformed individual filenames fail closed.
- Gaps use max-plus-one allocation rather than reusing the first missing number.
- Focused regression tests cover A1–A6, including duplicate, malformed and mismatched-link cases.
- A focused GitHub Actions workflow uses full commit SHAs for checkout and Python setup, declares `contents: read`, and runs only the allocator regression file.
- Template validation is moved before target-directory creation so a malformed template does not create a directory as a side effect.

### 16.3 Verification status and remaining limitations

For exact PR #5 head `724058c167775244dd55316abd7dc12725b099fb`, the workflow-runs query returned an empty list and the combined status query returned no status entries at the time checked.

Therefore:
- The code and tests are **committed to the PR branch**.
- A1–A6 are **specified in tests but NOT YET EXECUTED / NOT YET ESTABLISHED AS PASS**.
- Hosted CI is **NOT YET ESTABLISHED** for this exact head.
- No local test execution is claimed.
- The record/register partial-write exposure remains open; W1–W8 have not been addressed by this work package.
- CG-042 has not been migrated.
- PR #1's full retrieval implementation has not been transplanted.
- No merge, status promotion or owning-project gate change is authorized.

The allocator work package must not be treated as accepted until the exact-head workflow has run successfully and the implementation/tests have been reviewed. If the PR head changes, repeat the exact-head evidence check.


## 17. Allocator and record/index transaction verification update — 25 November 2026

This section supersedes the earlier “not yet executed” statements in Section 16.3 for the exact work-package heads recorded below. It does not change the frozen M1 baseline, the PR #1 reconciliation findings, or any owning-project gate.

### 17.1 PR #5 allocator acceptance evidence

- PR: [#5 — reconcile lesson ID allocation across legacy and migrated records](https://github.com/Moshoeshoe333/Codex-Guidas/pull/5)
- Branch: `codex/integration-core-capture-2026-11-25`
- Exact tested PR head: `724058c167775244dd55316abd7dc12725b099fb`
- Hosted workflow: [Lesson allocator regression, run #1](https://github.com/Moshoeshoe333/Codex-Guidas/actions/runs/45627741868)
- Runner: Ubuntu 26.04; Python 3.12.16
- Result: A1–A6 suite, 8/8 tests passed.

The hosted log shows all eight allocator tests passing, including legacy-only allocation, migrated records, mixed state, file-ahead state, duplicate/malformed identifiers, mismatched links and max-plus-one gap behaviour.

**Assessment:** The focused allocator execution criterion that was previously NOT RUN is now evidenced as PASS for this exact PR #5 head. Full integration acceptance remains separate. PR #5 remains open, draft and unmerged; no merge or branch rewrite is authorized.

### 17.2 PR #7 record/index transaction safety

- PR: [#7 — make record and index creation recoverable](https://github.com/Moshoeshoe333/Codex-Guidas/pull/7)
- Branch: `codex/record-transaction-safety-2026-11-25`
- Base branch: PR #5 branch at `724058c167775244dd55316abd7dc12725b099fb`
- Tested code/test head: `2b006d6736c9ad9607c0f70becd74ab4b1c70d8d`
- Current PR head at this audit update: `dd8dc5f75a382e63de4e2af897b8d86f32b4c84a`
- Difference after the tested code/test head: workflow-comment-only edits; no implementation or test logic changed.
- Hosted workflow: [Record transaction and allocator regression, run #8](https://github.com/Moshoeshoe333/Codex-Guidas/actions/runs/45631882338)
- Runner: Ubuntu 26.04; Python 3.12.16
- Allocator suite: 8/8 passed.
- Transaction suite: W1–W8, 8/8 passed.

The W1–W8 log records passing tests for preparation failure, journal-before-replacement ordering, rollback after a partial record/index write, rollback before the committed marker, committed cleanup recovery, idempotent prepared-journal recovery, lock refusal, malformed/path-traversal journal refusal and symlinked-target rejection (the latter is an additional assertion in W8).

An earlier intermediate workflow on superseded commit `83ee597c192c63431ce33edd58519e1d3a8bdd13` failed while regex escaping was incorrect. The regex correction and later hardening were committed; subsequent hosted runs, including run #8, passed. The failed intermediate run is retained as development history, not hidden or counted as a final pass.

### 17.3 What the transaction implementation does and does not establish

The current implementation uses:
- an exclusive repository-local lock around recovery, ID allocation and writes;
- a write-ahead journal with original file snapshots and prepared/committed states;
- in-memory construction of the record and updated index before destination mutation;
- individual same-directory atomic file replacements;
- rollback of prepared transactions and cleanup of committed journals;
- journal path allowlisting, traversal and symlink rejection, and checks that the record was previously absent while the index already existed.

It does **not** provide a true atomic commit across multiple independent files. It is recoverable single-host filesystem coordination, not a database transaction or cross-host distributed lock. A process crash can leave a lock file; stale-lock takeover is intentionally manual and must only occur after confirming no writer is active. On Windows, portable Python directory-handle fsync is unavailable in this implementation, so directory-entry crash durability is weaker than on the POSIX CI runner.

### 17.4 Updated gate/evidence disposition

| Criterion | Updated evidence | Disposition |
|---|---|---|
| A1–A6 allocator cases | PR #5 exact tested head; hosted 8/8 | Focused execution PASS; code review/integration acceptance remains separate |
| W1–W8 transaction cases | PR #7 tested code/test head; hosted 8/8 | Focused execution PASS; code review and platform limitations remain open |
| M6 index exact-set/deterministic rebuild | No new execution evidence in these PRs | NOT RUN / OPEN |
| Full PR #1 retrieval integration | Not transplanted; PR #1 remains diverged | NOT RUN / OPEN |
| Full M1–M12 acceptance | Not all criteria executed or reviewed | NOT PASSED |
| Merge authorization | No maintainer merge instruction | NOT AUTHORIZED |

The PR #5 and PR #7 work remains isolated and unmerged. PR #7 is stacked on PR #5 and must not be merged independently of its dependency. PR #1 remains untouched. The next technical work package, after review of the allocator/transaction changes, is index integrity: exact-set reconciliation across canonical records and projections, path integrity, deterministic repeated builds, and proof that index generation does not mutate Markdown sources.
