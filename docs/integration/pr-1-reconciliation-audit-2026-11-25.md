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
