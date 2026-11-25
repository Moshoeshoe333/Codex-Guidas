# Allocator and record-transaction source review — 2026-11-25

**Review type:** Static source review of PR #5 and PR #7; no code execution performed by this review  
**Reviewed PR #5 head:** `724058c167775244dd55316abd7dc12725b099fb`  
**Reviewed PR #7 current head:** `dd8dc5f75a382e63de4e2af897b8d86f32b4c84a`  
**PR #7 tested code/test head:** `2b006d6736c9ad9607c0f70becd74ab4b1c70d8d`  
**PR #7 source blobs reviewed:** `scripts/new_record.py` = `26ca0b16f20ea5cbaf722eff9a34e14d25580955`; `tests/test_record_transaction.py` = `3c0074df2b98e7e52c083dc74b2065fd44e85194`; transaction design = `9ad53140f174c776de5be073620ac15934b648b9`; workflow = `419424cf0eedfce7e241c29c5e7c1743d0ec2565`.

## 1. Scope and evidence boundary

This review checks source-level correspondence between the stated protocol, implementation, tests and workflow. It does not replace the hosted test evidence already recorded in PR #4 Section 17. It does not establish operating-system coverage, race-freedom, power-loss durability or maintainer acceptance.

## 2. Findings requiring resolution or explicit acceptance

### RCR-01 — Validate repository paths before any filesystem side effect or source read

**Observed:** In `create_record()`, the implementation acquires the lock and allocates the ID, then may read the template and index, and calls `target_dir.mkdir(parents=True, exist_ok=True)` before `_apply_transaction_unlocked()` validates destination paths against the resolved repository root.

**Risk:** A symlinked repository subdirectory can cause pre-validation reads or directory creation outside the intended root. The later destination check prevents the transaction file replacements from proceeding through a resolved out-of-root destination, but it does not undo or prevent earlier reads/directory side effects.

**Required correction:** Validate the root and every relevant source/destination path (ledger/register, record directory, template, target, journal and lock) before reading or creating anything through those paths. Add tests for symlinked parent directories and verify that no outside file or directory is read or changed. Keep the current journal-recovery path checks as a separate defence.

**Disposition:** Static-review finding; not covered by the reported W1–W8 evidence.

### RCR-02 — Defect ID allocation must reconcile the operational register and fail closed

**Observed:** `next_id("defect")` derives the next sequence only from filenames matching a narrow `DEF-YYYY-NNN[-slug].md` expression. It does not inspect the canonical operational register `11-defect-intelligence/README.md`, and non-matching DEF-prefixed filenames are ignored rather than rejected.

**Risk:** A defect ID present in the operational register but missing from the file projection, or a malformed existing DEF-prefixed filename, may not influence allocation. A future creation could reuse an already registered ID or conceal an inconsistent defect inventory.

**Required correction:** Treat README register IDs and defect filenames as overlapping sources during staged migration; require exact identity/link agreement and reject malformed or duplicate IDs. Add tests for register-only IDs, file-only IDs, duplicate IDs, malformed DEF-prefixed filenames and max-plus-one behaviour. Keep the historical defect ledger out of the operational allocation source, consistent with the scoped M6 decision in the index-integrity gap analysis.

**Disposition:** Not covered by A1–A6, which are lesson allocator tests. Defect allocation requires its own acceptance suite.

### RCR-03 — W7 demonstrates lock-file contention, not a simultaneous-process race

**Observed:** The W7 test creates a pre-existing lock file and asserts that a second creation attempt fails without mutation. It does not launch two independent processes concurrently and observe their allocation/write behaviour.

**Risk:** The existing test verifies the fail-closed response to lock contention, but the test name/design wording can be read as evidence of a full concurrent-writer race test.

**Required correction:** Either narrow the acceptance wording to “existing-lock contention fails closed,” or add a multiprocessing/subprocess test in which two writers contend for the same repository and assert that no duplicate ID or partial state is produced.

**Disposition:** W7's reported pass remains valid for the assertion actually tested; broader concurrency behaviour is not established.

### RCR-04 — Atomic replacement changes destination file metadata

**Observed:** `_atomic_write()` creates a new `NamedTemporaryFile` and replaces the destination with `os.replace`. On POSIX, the temporary file normally has restrictive temporary-file permissions; the implementation does not preserve the original destination mode or other metadata.

**Risk:** Rewriting an existing ledger/register may silently change its permissions. The current byte-level rollback tests do not inspect file mode or metadata.

**Required correction:** Decide the intended permission policy. Either preserve the original mode when replacing an existing file (and set an explicit mode for new records), or document and test the deliberate restrictive mode. Include a POSIX mode assertion where supported.

**Disposition:** Metadata behaviour not covered by W1–W8.

## 3. Positive findings retained

- The implementation uses a repository-local exclusive lock around recovery, allocation and writes.
- The journal records original bytes or an explicit absent-file state and distinguishes prepared from committed transactions.
- Recovery rejects malformed journal structure, path traversal, symlink-resolved journal destinations and destination pairs outside the approved record/index shapes.
- The transaction writes each destination through a same-directory temporary file and atomic replacement.
- The committed-marker uncertainty path preserves the journal rather than silently claiming rollback.
- The hosted run #8 evidence remains bounded to the exact tested code/test head and the W1–W8 assertions actually present there.

## 4. Recommended disposition and sequencing

1. Keep PR #5 and PR #7 open, draft and unmerged while these findings are reviewed.
2. Resolve RCR-01 before treating the transaction path controls as complete.
3. Add a separate defect-allocation acceptance package for RCR-02; do not imply A1–A6 covers defect allocation.
4. Clarify or extend W7 as described in RCR-03.
5. Decide and test the file-permission policy in RCR-04.
6. Re-run hosted workflows on the exact final code/test head after any code or test changes.
7. Only then use the reviewed allocator/transaction base as a dependency for M6 index-integrity implementation.

## 5. Current disposition

**PR #5 allocator A1–A6:** hosted execution PASS on the recorded exact head; code review and integration acceptance remain separate.  
**PR #7 W1–W8:** hosted execution PASS on the recorded tested code/test head; this source review identifies additional path-validation and acceptance-scope gaps.  
**M6 index exact-set/deterministic integrity:** NOT RUN / OPEN.  
**Full M1–M12 acceptance:** NOT PASSED.  
**Merge authorization:** NOT GRANTED.

This document is a static review artifact. It changes no runtime code, tests, workflow, mainline file or owning-project gate.
