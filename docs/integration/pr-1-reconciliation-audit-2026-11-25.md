# PR #1 Reconciliation Audit — 2026-11-25

**Status:** Review artifact; no integration authorization  
**Target:** `codex/retrieval-enforcement-2026-11-19` into current `main`  
**Reviewed refs:** current `main`; PR #1 feature branch  
**Review method:** GitHub compare metadata and read-only inspection of selected source files. No local checkout, test execution, workflow execution, merge, rebase or mainline write was performed.

## 1. Executive finding

PR #1 contains useful structured-record, retrieval, assurance and CI foundations, but it is not safe to merge or rebase as-is. The branch is **44 commits ahead and 40 behind** current `main`. Its compare reports 84 changed paths, including 41 new lesson records, a rewritten lesson ledger, new scripts/tests and workflow/configuration files.

Current `main` contains newer Opportunity Exposure material absent from the feature branch's lesson migration. The source check found an important distinction: the lesson ledger currently ends at **CG-041**; the innovation register labels the Opportunity Exposure material `OFN-001 / CG-042`, but there is no CG-042 row in the canonical lesson ledger. The field note itself is present and explicitly non-authoritative. Reconciliation must preserve it and resolve whether `CG-042` is intended as a formal lesson ID or only a cross-reference before creating or migrating a lesson record.

## 2. Blocking integrity conditions

### R1 — CG-042 must survive the migration

- The current `main` lesson ledger contains entries CG-001 through CG-041; the inspected complete ledger does **not** contain a CG-042 row.
- The innovation register describes the Opportunity Exposure experiments as `OFN-001 / CG-042`, while the field note's own canonical record ID is `OFN-001`.
- The field note, experiment portfolio and innovation-register entry are present on current `main`; the field note classifies the material as an external heuristic, not a validated causal model or project policy.
- The relationship between `CG-042` and `OFN-001` is therefore ambiguous: it may be an intended lesson cross-reference that was never added to the lesson ledger, rather than an existing canonical lesson record.
- PR #1's archived ledger and individual lesson files stop at CG-041. Do not infer that its 2026-11-19 archive supersedes mainline material added later.

**Required resolution:** preserve `OFN-001`, its provenance, limitations and experiment artifacts. Before adding a CG-042 lesson, decide whether a distinct lesson is intended; if yes, author it from an explicitly reviewed statement and link it to OFN-001. Do not silently convert the field note into a lesson or claim that a CG-042 ledger entry already exists.

### R2 — ID allocation must not collide with unmigrated legacy IDs

The proposed `scripts/new_record.py` `next_id()` implementation scans only `01-lessons-learned/lessons/CG-*.md`. Current `main` still stores CG-001 through CG-041 in the monolithic ledger and has no individual lesson directory in its tree.

If the allocator is introduced before the complete migration, it can allocate an ID already present in the legacy ledger. The concrete first-collision case is: legacy ledger contains CG-001–CG-041, the individual-record directory is absent/empty, and the allocator proposes CG-001 instead of the next unused ID. This is a migration-order defect, not a theoretical concern.

**Required resolution:** either (a) migrate all current canonical lesson IDs into individual records and validate uniqueness before enabling the allocator, or (b) make the allocator check both individual records and the legacy ledger during a staged migration. Add a regression test where the legacy ledger contains CG-041 but the individual-record directory does not; the next allocated ID must be CG-042. Separately resolve whether the innovation-register label `CG-042` is a formal lesson ID or an OFN-001 cross-reference.

### R3 — Ledger/index transition must be atomic at repository level

PR #1 changes `01-lessons-learned/ledger.md` from a substantive register into an index and adds `ledger-archive-2026-11-19.md`. The archive preserves the pre-split ledger through CG-041, but it does not contain later CG-042 material.

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
| R7 | Record creation | Test failure between record-file creation and ledger/index update; ensure no orphan or duplicate record is silently left behind. |
| R8 | Assurance register | Validate JSON/schema/path references and confirm every assurance claim remains explicitly proposed or unassessed unless supported by evidence. |
| R9 | CI | Confirm workflow triggers, permissions, action provenance, runtime versions and exact-head execution. No passing status is currently established for the PR #1 head in this review. |
| R10 | Current mainline | Preserve current README, project innovation register, Opportunity Exposure note and experiments; inspect all overlapping paths before transplanting feature changes. |

## 5. Integration sequence

1. Freeze the current mainline snapshot and record its exact SHA.
2. Build a migration inventory of all lesson IDs on current mainline and on the feature branch.
3. Reconcile CG-001–CG-041 against the current ledger; do not assume metadata migration independently verifies source claims.
4. Add CG-042 as an individual record with its original heuristic status, source attribution, limitations and cross-link to the field note.
5. Resolve the ID allocator's legacy-collision risk and add the CG-042 regression case.
6. Rebuild the index and assert exact record/index ID-set equality, including CG-042.
7. Port the retrieval scripts, tests and workflow in a focused integration branch; review file-level differences against current mainline.
8. Execute all checks on the exact proposed head and inspect the run SHA, logs and failures.
9. Submit the integrated branch for review. Do not merge until checks, review and maintainer ratification are complete.

## 6. Evidence boundary

This audit is a **read-only source review** of selected files and GitHub compare metadata. It does not establish that the scripts or tests execute successfully, that the proposed workflow is active, that GitHub branch protection is configured, or that the assurance register is operationally effective.

No lesson status, project gate, external project authority or implementation state is changed by this document.

**Decision:** PR #1 remains unmerged and requires a migration-safe integration pass.