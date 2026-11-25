# Record creation transaction-safety design

**Status:** Proposed implementation contract  
**Date:** 2026-11-25  
**Depends on:** PR #5 lesson allocator branch, exact head 724058c167775244dd55316abd7dc12725b099fb  
**Scope:** scripts/new_record.py record-file plus canonical ledger/register update  
**Non-goals:** database-grade multi-file atomicity, cross-host distributed locking, automatic stale-lock takeover, or changing lesson/defect schemas.

## Problem statement

Record creation currently writes the new record before inserting its index row. A failure between those operations can leave an orphan record; a failure while writing the index can leave the repository inconsistent. Concurrent creators can also calculate the same next ID.

A filesystem generally cannot atomically replace two independent files as one operation. The implementation must not claim true multi-file atomicity. It will instead provide a recoverable transaction protocol with a write-ahead journal and a single-writer lock.

## Proposed protocol

1. Acquire an exclusive repository-local lock before recovery, ID allocation or writes. If the lock already exists, fail closed; do not guess whether its owner is stale.
2. If a prior transaction journal exists:
   - prepared: restore every recorded pre-transaction file state, then remove the journal;
   - committed: retain the committed files and remove the journal;
   - malformed/unknown state: fail closed and preserve the journal for inspection.
3. Compute the next ID while holding the lock.
4. Build the complete new record and complete updated ledger/register contents in memory. Validate destinations and refuse overwrites.
5. Write and fsync a prepared journal containing repository-relative paths and exact original bytes (or an explicit “did not exist” marker) for every destination. The journal must be durable before the first destination replacement.
6. Atomically replace each destination file individually using a same-directory temporary file, flush/fsync and os.replace.
7. Atomically write/fsync the journal state as committed.
8. Remove the journal and fsync its directory. If cleanup fails after commit, leave the committed journal; a later invocation can safely clean it.

## Recovery and failure semantics

- Any failure before the committed marker triggers rollback from the journal.
- Rollback is idempotent: restoring an original byte sequence repeatedly has the same result.
- If rollback itself fails, retain the prepared journal. The next invocation must fail closed or retry recovery before allocating another ID.
- If a committed marker is visible after a filesystem error, preserve the journal and report an uncertain commit outcome for inspection; do not silently roll back or silently claim failure with no recovery evidence. If the committed marker is durable, cleanup can be retried.
- A process crash can leave a lock file. Automatic stale-lock removal is intentionally not implemented because process ownership cannot be safely inferred. An operator must establish that no writer is active before removing a stale lock.
- This is recoverable single-host filesystem coordination, not a database transaction and not a guarantee against hardware/filesystem corruption.

## W1–W8 acceptance matrix

| ID | Failure boundary | Required assertion |
|---|---|---|
| W1 | Before any destination replacement | Prepared journal is durable first; original files remain unchanged if preparation fails. |
| W2 | Failure on first destination replacement | No partial record/index state remains after successful rollback. |
| W3 | Failure after record replacement but before index replacement | Recovery restores the original record/index state; no orphan remains. |
| W4 | Failure after both replacements but before committed marker | Recovery rolls both files back to their original bytes. |
| W5 | Cleanup failure after committed marker | New record and index remain committed; journal remains recoverable and is cleaned on next recovery. |
| W6 | Recovery repeated after interruption | Recovery is idempotent and produces the same final bytes/state. |
| W7 | Existing lock / concurrent writer | Second writer fails closed without allocating or mutating files. |
| W8 | Malformed or path-traversal journal | Recovery refuses mutation and preserves the journal for inspection. |

## Implementation constraints

- Keep journal paths relative to the repository root; reject absolute paths, parent traversal, resolved paths outside the root, and any destination pair other than one approved record plus its matching lesson ledger or defect register.
- Do not use insert_table_row as an in-place side effect inside the transaction. Construct updated register text first.
- Preserve the original file bytes exactly during rollback.
- Do not silently delete malformed journals or locks.
- Do not report a committed transaction as rolled back merely because post-commit journal cleanup failed.
- Keep allocator A1–A6 coverage separate from W1–W8 coverage.

## Evidence boundary

Passing W1–W8 on a hosted exact-head workflow establishes the tested recovery behaviours under injected process-level failures. It does not prove database-grade atomicity, resilience to arbitrary power-loss/filesystem corruption, cross-machine coordination or correctness on every operating system.
