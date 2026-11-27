# Testing and Verification Discipline

## Proof boundary
A green suite is evidence about the tests that ran, not proof that the entire product is correct, secure or ready for users.

Record repository/branch, commit SHA, environment and runtime versions, exact command, test count/result, skipped tests, warnings, known gaps and CI artifact/link.

## Verification layers
1. Static checks and formatting
2. Unit tests
3. Contract and schema tests
4. Integration tests
5. End-to-end workflow tests
6. Negative and adversarial tests
7. Build and runtime verification
8. Independent user-task testing
9. Repeat-use and operational monitoring

Do not substitute one layer for another.

## Regression learning loop
Preserve failing output and reproduction steps; identify the earliest failing boundary; classify root cause as unknown/suspected/confirmed; write a minimal reproducer; fix the cause; add regression coverage; run focused and wider tests; verify CI/runtime; record residual risk and lesson ID.

## CI integrity rules
- Never edit tests solely to turn a failure green.
- If a test is obsolete or incorrect, explain why and deliberately replace its coverage.
- Do not report a workflow as passed when only an earlier stage passed.
- Distinguish committed code, CI pass, artifact built, artifact installed and runtime tested.
- Keep secrets out of logs and repository files.
- Track flaky tests rather than silently ignoring them.

## Historical project evidence leads (not a fresh re-run)
- SoulSync Run #25 was reported as 64/64 tests passing; Run #29, associated with commit ddcd790..., was also reported as 64 tests passing.
- SoulSync recorded a deep-immutability freeze and a separate 99-contract freeze. These labels do not prove every contract or runtime is covered.
- SoulSyncMobile had G-BOOT open and no verified APK in the recorded state; an EAS/Gradle failure was reported. Do not describe the app as released or runtime-validated on that basis.
- ScoutSA had a PostgreSQL 17 CI runtime witness; this was a limited technical witness, not proof of a complete production application.

Re-check original workflows and artifacts before reusing these statements as current status.

## Additional verification discipline — pipeline, ingestion and sampling (2026-11-27)

The [GCHQ repository pattern review](../10-source-audits/2026-11-27-gchq-repository-pattern-review.md) suggests several refinements for future work:

- **Stage-level tests:** test each meaningful transformation's accepted input, output contract, invalid input, boundary cases, resource limits and explicit failure/unknown outcomes. For workflows, add integration tests for stage ordering and the data passed between stages.
- **Intermediate diagnostics:** where step-through/debug traces are useful, verify that they correspond to actual execution and do not disclose secrets or unnecessary personal data.
- **Ingestion state tests:** exercise unmatched inputs, rejected jobs, partial failures, retries, duplicate submissions and recovery. A queued/accepted job is not a completed ingest.
- **Artefact-scan semantics:** test unsupported type, over-limit size, scanner skip, scanner error and clean completed result separately. Only the last state may support a claim of a completed clean scan within the scanner's stated scope.
- **Sampling/coreset validation:** benchmark against the full dataset and a simple random baseline; use multiple seeds for stochastic methods; report sample size, downstream task metrics, distribution/coverage limits, runtime and preprocessing effects. Do not discard rare or high-impact cases merely to improve average performance.
- **Performance gates:** use representative workloads and report both quality/correctness and resource cost. A speed gain does not compensate for degraded correctness, lost coverage or weakened safeguards.

These are proposed verification practices. They do not add new tests, change test counts, or establish a verification status in any project.
