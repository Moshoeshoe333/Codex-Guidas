# Index integrity — source review and acceptance work package

**Assessment date:** 2026-11-25  
**Status:** Source-observed gap analysis; implementation not started  
**Related audit:** PR #4, Sections 8–17  
**Target under review:** PR #1 branch `codex/retrieval-enforcement-2026-11-19`, exact head `ea7b36e0e78c79c019bce9982bc419e39eeb7461`  
**Frozen comparison baseline:** `main` at `6d1c38bb2b29936d059a36750d1cfc70815f4ed3`

## 1. Source artifacts and provenance

| Artifact | Blob SHA | Review boundary |
|---|---|---|
| `scripts/build_index.py` | `c2829802aa007d80559ee2c5b2e102614c8379b1` | Read-only source inspection |
| `scripts/codex.py` | `bdfa9d688703d05c5d91afa2dd6bd5179e7a916b` | Read-only source inspection |
| `tests/test_capture_and_index.py` | `868904aba57ee67686c9652ba41023628a7cba8a` | Test-source inspection |
| `tests/test_codex.py` | `4ca9d5222776ac22db937c8280e6f13268a2d779` | Test-source inspection |
| `.github/workflows/knowledge-integrity.yml` | `a774f2778aa4b0baa0a1de11e226a9074491cd6e` | Workflow-source inspection |
| `11-defect-intelligence/README.md` | `c4389bc8f6c92e08b81131b6681751f96b1b92f2` | Register structure inspection |
| `11-defect-intelligence/ledger.md` | `0ffcc96cc64af6205c66a82be0468d630344b8fe` | Historical defect-ledger structure inspection |
| PR #1 branch lesson ledger | `b600b33c5f0c7fa1040d79cb61b5be5dae0d7049` | Migrated ledger snapshot; 41 individual lesson records |

The exact PR #1 source head and frozen mainline comparison are separate provenance boundaries. No code from PR #1 is accepted or transplanted by this document.

## 2. What the current source does

### 2.1 JSON builder

At the reviewed source head, `build_index.py`:
- enumerates `CG-*.md` files in the individual lesson directory and `DEF-*.md` files in the defect directory;
- reads each record's frontmatter and derives a title from the first Markdown heading;
- projects selected metadata into JSON;
- sorts records by ID and record path;
- emits a stable-looking JSON serialization with indentation and a trailing newline;
- offers `--check`, which compares an existing output file byte-for-byte with the current rendered projection.

These are source-level observations. They are not execution evidence.

The builder does not itself compare the lesson files with the frozen canonical lesson inventory, the lesson ledger, the defect README register or the defect ledger. It does not reject duplicate IDs before building, verify that metadata IDs agree with filenames, or assert that every record type is one of the expected values. A missing file can therefore reduce the generated record count without the builder itself knowing that a canonical record was omitted.

### 2.2 Existing validator

At the reviewed source head, `codex.py validate_records()`:
- checks metadata fields and record type/status constraints;
- detects duplicate IDs among discovered individual lesson and defect files;
- checks lesson filename stems against metadata IDs;
- extracts well-formed lesson links from the lesson ledger and compares those linked IDs with the discovered lesson-file set;
- checks local Markdown links.

It does not compare the migrated lesson set with the frozen mainline inventory or archived pre-migration source. It does not reconcile the defect README register or defect ledger against the discovered defect-file set. It also does not establish that a generated JSON index exactly equals the canonical record set.

### 2.3 Existing tests and workflow

The test named `test_index_is_deterministic_and_preserves_explicit_tags` calls `build_index_data(root)` once and checks record count, explicit tags and title. It does not compare repeated builds or serialized bytes. No test in the inspected file invokes the CLI `--check` path, verifies stale/missing index handling, checks exact source/index set equality, or proves source Markdown bytes remain unchanged.

The hosted workflow runs the validator and CLI tests, builds a JSON file under `/tmp`, and checks one known defect/tag. It does not invoke `build_index.py --check`, compare all source IDs with all JSON IDs, verify exact record counts by source, or prove the Markdown sources are unchanged. The index output directory is not present in the inspected PR #1 tree; the workflow uses a temporary output.

## 3. Material migration risk

The frozen mainline source inventory contains CG-001 through CG-042. The PR #1 migration branch contains individual lesson files CG-001 through CG-041; CG-042 is absent. The PR #1 branch's own migrated lesson ledger and individual file set can agree with one another while both omit CG-042 relative to the frozen source.

Therefore, equality between a migrated ledger and a migrated file directory is not sufficient migration-completeness evidence. The acceptance contract must retain an immutable pre-migration ID inventory and compare the migrated projection against it until the migration is explicitly reconciled.

## 4. Proposed index integrity acceptance matrix

| ID | Invariant | Required test/evidence |
|---|---|---|
| I1 | Canonical source inventory is complete | Compare frozen source ID set with migrated lesson IDs; explicitly fail when CG-042 or any source ID is absent. |
| I2 | Record identity is internally consistent | Reject malformed filenames, duplicate IDs, metadata ID/filename mismatch and record_type/path mismatch. |
| I3 | Lesson ledger and files reconcile exactly | Parse every data row; reject malformed/mismatched/duplicate links; compare exact ID sets, not only successfully parsed links. |
| I4 | Defect register ownership is explicit | Identify the canonical defect register before comparison; reconcile its IDs against defect files and keep historical defect-ledger semantics distinct. |
| I5 | JSON projection equals the accepted source set | Compare exact ID multisets/sets, counts by type, record paths and selected metadata fields against the accepted source records. |
| I6 | Every indexed path is valid and contained | Verify every record_path resolves to one existing expected file under the repository root; reject traversal, symlink escape and duplicate paths. |
| I7 | Repeated builds are deterministic | Render twice from unchanged inputs and compare exact bytes; verify stable ordering and serialization. |
| I8 | CLI check is meaningful | Test --check success for current output, failure for missing output, stale output, malformed JSON and wrong path/record content. |
| I9 | Index generation is read-only with respect to source records | Hash or byte-snapshot all Markdown source files before and after build/check; assert no source mutation. |
| I10 | Hosted workflow enforces the full contract | Run the complete tests, validator, build, exact-set reconciliation, repeated-build comparison and CLI --check on the exact PR head. |

## 5. Defect-register source-of-truth decision

**Decision for M6: `11-defect-intelligence/README.md` is the canonical operational defect register. `11-defect-intelligence/ledger.md` is treated as historical defect-intelligence evidence, not as a second operational register.**

This decision follows the reviewed source structure: the README explicitly presents and maintains the defect register, while the ledger preserves historical defect-intelligence records. The two artifacts therefore have distinct responsibilities and must not be subjected to interchangeable equality rules.

Implementation consequences:
- I4 will parse the operational register entries in `11-defect-intelligence/README.md` and compare their canonical DEF IDs with the individual defect-record files.
- `11-defect-intelligence/ledger.md` will be retained as historical evidence and checked for internal link/path integrity where appropriate; it will not independently define the current operational defect-file inventory.
- Any ambiguity, malformed register row, duplicate ID, missing target or unregistered defect file must fail closed rather than be silently skipped.
- The validator must report which source supplied each expected ID set, so future maintainers can audit the authority chain.
- This is a scoped source-of-truth decision for M6 in this integration work package. It does not grant the README authority over unrelated project registers or override future explicit maintainer ratification.

The decision resolves the previously open source-selection question. It does not prove that the register and defect files currently reconcile; that remains an implementation and execution test.

## 6. Design boundaries and sequencing

1. Do not transplant the diverged PR #1 branch wholesale.
2. Keep the frozen mainline ID inventory as an immutable migration reference.
3. Use the README as the canonical operational defect register and the ledger as historical evidence, as defined in Section 5.
4. Build a minimal accepted source contract and test matrix before implementation.
5. Keep builder output separate from Markdown source-of-truth files.
6. Do not use a green single-record smoke test as proof of complete index integrity.
7. Do not mark M6 PASS until I1–I10 have exact-head evidence and the migration source inventory is reconciled.
8. Do not infer full M1–M12 acceptance or merge authorization from this work package.

## 7. Current disposition

**M6 — index exact-set and deterministic integrity: NOT RUN / OPEN.**

This is a source-observed gap analysis and proposed acceptance contract. The defect-register source decision is now explicit in Section 5. No index implementation, tests, workflow or mainline files were changed by this assessment. The next implementation remains isolated and is gated on review of the PR #5 allocator and PR #7 transaction changes.
