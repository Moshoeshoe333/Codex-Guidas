# ScoutSA Prototype and Engagement Audit — 2026-11-24

**Audit ID:** CG-SOURCE-AUDIT-2026-11-24-SCOUTSA-01  
**Audit date:** 2026-11-24  
**Status:** Partial source audit; no runtime test execution; findings are bounded to inspected artifacts  
**Repository:** [Moshoeshoe333/ScoutSA](https://github.com/Moshoeshoe333/ScoutSA)  
**Branch inspected:** `prototype/internal-demo`  
**Exact branch head:** `e4a0a5a5c130f4d6e94c70b72a786e196fb3ae27`  
**Mainline boundary:** The isolated prototype branch does not authorize or alter mainline implementation, real-data, production, deployment or pilot gates.

## 1. Audit question and decision

Does the current ScoutSA repository support the claims being made about prototype maturity, verification and external engagement? Which lessons are sufficiently evidenced to transfer into Codex-Guidas?

**Decision:** The repository supports the description of a substantial, synthetic, static internal prototype under active hardening. It does **not** support a claim that the latest branch head is fully tested, independently accepted, production-ready, externally validated or pitch-ready. The recorded 23 November project-owner decision explicitly holds external validation, stakeholder interviews, partnership/funding pitches and active promotion until the prototype is working, tested, independently reviewed and accepted.

The agreed sequence is:

**Build → Test → Audit → Accept → Demonstrate → Pitch.**

This is the current ScoutSA project decision, not a universal prohibition on transparent early problem-discovery conversations.

## 2. Method and limitations

This review used GitHub repository metadata, the exact branch ref and commit, recursive source trees, and selected primary files fetched from the named branch. It inspected the root README, Constitution, gate-status document, prototype README, workflow configuration, Match-Day Handoff contract, importer, browser regression source and 23 November session ledger.

This audit did **not**:
- execute Node, Playwright, Chromium or any application code;
- run the hosted workflow or independently reproduce prior CI results;
- perform a complete AST, dependency, penetration, accessibility or runtime security audit;
- inspect every file and every branch in the repository;
- establish legal compliance, real-world safeguarding effectiveness, market demand, user value or commercial viability.

Source inspection is not test execution. A committed regression is not a passing regression. A missing result from a limited status endpoint is not evidence of failure or success.

## 3. Evidence register

| ID | Primary source | Exact inspected revision / evidence | What it supports |
|---|---|---|---|
| SA-01 | [Root README](https://github.com/Moshoeshoe333/ScoutSA/blob/e4a0a5a5c130f4d6e94c70b72a786e196fb3ae27/README.md) | Blob `e3435b1499c800278e31f0fe97fa3482d73f8437` | Mainline hold, synthetic prototype scope, external-engagement boundary and known verification limits |
| SA-02 | [Constitution](https://github.com/Moshoeshoe333/ScoutSA/blob/prototype/internal-demo/docs/00-constitution.md) | Blob `dcbf85f8e690fca87cd688adc3daf529a38293e1` | Evidence rule, safeguarding and privacy principles, and distinction between assertions, evidence and verification |
| SA-03 | [Gate status](https://github.com/Moshoeshoe333/ScoutSA/blob/prototype/internal-demo/docs/00-gate-status.md) | Blob `54746a50ee043a246cc2feb1e20c412144f9f94d` | Mainline implementation hold and separate prototype status |
| SA-04 | [Prototype README](https://github.com/Moshoeshoe333/ScoutSA/blob/prototype/internal-demo/prototype/README.md) | Blob `e7a58bfcee533cef3d248313d4765ad1a7e2a872` | Prototype maturity, historical CI scope, synthetic-only limitations and acceptance still outstanding |
| SA-05 | [Prototype workflow](https://github.com/Moshoeshoe333/ScoutSA/blob/prototype/internal-demo/.github/workflows/prototype-policy-tests.yml) | Blob `c1efe3b1720c8592b8cab707d9badafab3f95dd6` | Configured triggers and the current list of browser smoke scripts |
| SA-06 | [Handoff contract](https://github.com/Moshoeshoe333/ScoutSA/blob/prototype/internal-demo/prototype/MATCH-DAY-HANDOFF-CONTRACT.md) | Blob `7bab8733961ab3f6a4b2af777fe823f41b2deccd` | Version-1 package shape, relationships and declared limitations |
| SA-07 | [Player Tournament History importer](https://github.com/Moshoeshoe333/ScoutSA/blob/e4a0a5a5c130f4d6e94c70b72a786e196fb3ae27/prototype/player-tournament-history.html) | Blob `9b6f3119f2b38f7ceab5dd1d428253b87e507db9` | Exact root-envelope validation and current nested validation logic |
| SA-08 | [Tournament Day Operations browser smoke](https://github.com/Moshoeshoe333/ScoutSA/blob/e4a0a5a5c130f4d6e94c70b72a786e196fb3ae27/prototype/tests/tournament-day-operations.browser-smoke.cjs) | Blob `f3a4b07a0520e6ce89dc18b72252919c10444c60` | Committed scenarios for unknown envelope fields, rejected imports and preservation of the previously imported view |
| SA-09 | [23 November session ledger](https://github.com/Moshoeshoe333/ScoutSA/blob/e4a0a5a5c130f4d6e94c70b72a786e196fb3ae27/prototype/verification/SESSION-LEDGER-2026-11-23.md) | Blob `0b8d9f36cc16bd4103566a0f30720270334d95ad` | Latest recorded hardening, open UI-008 status and explicit no-pitch/no-validation hold |

## 4. Findings

### F-01 — Prototype and production authority are correctly separated

**Status:** Observed.

ScoutSA describes `prototype/internal-demo` as a static browser prototype using synthetic data. The root README and gate-status record keep mainline database execution, RLS, API, authentication, real identity processing, production deployment and live pilot activity on hold. The prototype does not authenticate people, verify real authority, enforce production access control or establish legal compliance.

**Assessment:** This is a sound boundary. A working prototype can prove selected workflows in a controlled synthetic environment; it cannot silently promote itself into a production system or lift a separate governance gate.

### F-02 — External engagement is now explicitly gated by demonstrated maturity

**Status:** Observed project decision.

The 23 November project-owner decision, repeated in the root and prototype READMEs, holds external validation, stakeholder interviews, partnership/funding pitches and active promotion as a pitch asset until the internal prototype is working, tested, independently reviewed and explicitly accepted.

**Assessment:** The decision corrects a real sequencing risk: external reach can create an impression of operational capability, readiness or traction before there is an artifact capable of supporting those impressions. If a concept is presented as a functioning product, that is misrepresentation. If it is accurately labelled as a concept, early problem discovery can be legitimate—but ScoutSA's current explicit hold is stricter and remains controlling.

**Required control:** No ScoutSA pitch or external validation until the prototype passes the agreed sequence and the project owner accepts it. Do not infer permission from a presentation, a green historical run, a documentation milestone or an interested response.

### F-03 — Historical green CI is not current-head verification

**Status:** Observed evidence boundary.

The recorded successful workflow #893 tested PR #11 head `61993f435f621db32a0e0fc2aefe33d2d569201e`, not the current branch head `e4a0a5a5c130f4d6e94c70b72a786e196fb3ae27`. Later commits added further renderer, navigation, import and regression changes. The session ledger says the new regressions had not been independently run at the latest exact head.

The workflow configuration currently enumerates **12** browser smoke scripts. The root/prototype README still describes **11** configured browser smoke scripts for the historical run. The historical run may accurately have run 11 at that earlier revision, but the current configured inventory and the summary wording need reconciliation.

The available commit-workflow lookup returned no PR-associated runs for the latest head, and the combined-status lookup returned no status records. The workflow lookup is limited to PR-triggered runs, so these empty results do not establish that no push-triggered run exists. They do mean this audit did not obtain current-head pass evidence.

**Assessment:** Latest-head verification remains unknown/unproven. Do not report the latest branch as green.

**Required control:** Pin every verification claim to exact commit, workflow run, command, environment, test inventory, completed/skipped suites and result. Reconcile documentation against the workflow file at the same revision.

### F-04 — Root envelope validation is stronger, but nested validation is not complete

**Status:** Observed source improvement plus open review items.

The importer now requires exactly the 17 documented root-envelope keys, rejects missing or unknown envelope properties, applies a 1 MB file limit, checks synthetic identifiers and fixture scope, validates several lineup/substitution/event/source relationships, and recomputes appearance intervals. The committed browser smoke includes an unknown-envelope-property case and checks that a previously imported view remains unchanged after that rejection.

The contract also states that each source record's `recordId` must point to an included originating lineup, substitution, event or report. The inspected importer does not visibly enforce that reverse/source-origin relationship. The importer also does not define strict per-record nested key allowlists or explicit collection-cardinality limits. A 1 MB file cap is useful, but it is not a substitute for a complete nested schema and bounded collection rules.

**Assessment:** Root-envelope strictness must not be described as complete payload-schema validation. Existing regression source is not proof of execution.

**Required control:** Validate each nested record type against the contract; enforce required fields, primitive types, allowed keys, reference integrity and reasonable collection limits; preserve state on every rejected or failed import stage; add adversarial tests for nulls, primitives, extra nested fields, oversized collections and dangling source-origin links.

### F-05 — Safe-rendering progress is real but bounded

**Status:** Observed through the 23 November session ledger.

The recorded 21-page source scan found zero occurrences of four selected literal patterns: `.innerHTML =`, `.outerHTML =`, `insertAdjacentHTML(` and `document.write(`. The ledger explicitly states that this is a bounded source-pattern count, not a full AST/runtime audit. UI-008 remains OPEN, with URL, export, handoff, output-context, exact-head CI and independent acceptance work outstanding.

**Assessment:** The source-pattern scan is useful evidence of a specific reduction in known sinks. It is not a security certification and does not prove that all unsafe output contexts have been found.

### F-06 — Documentation and workflow inventory have drifted

**Status:** Observed.

The current workflow file lists 12 browser smoke scripts while the README's configured-inventory wording says 11. The prototype README also repeats the UI-008 evidence-ledger link. These are small but concrete examples of why status documents must be reconciled against current source and why counts should be generated or tested where practical.

**Assessment:** Documentation drift can mislead a reader even when the underlying source change is sound. The same discipline applies to product claims, status dashboards, test counts and investor materials.

### F-07 — The importer has a remaining atomicity question

**Status:** Derived risk; not a confirmed defect.

For validation failures, the current control flow validates the parsed package before assigning it to `importedHandoff`, and the committed browser scenarios check preservation of the prior view for selected rejected inputs. After validation succeeds, however, the importer assigns `importedHandoff` before rebuilding the player selector and rendering the new view. The inspected test does not inject a failure during those later presentation steps.

**Assessment:** The tested rejection path is not proof of atomicity across every post-validation UI failure.

**Required control:** Stage the candidate data and candidate selector options separately, prepare the complete next view, then commit the state transition once. Add failure-injection coverage around post-validation rendering or explicitly document the remaining limit.

## 5. Positive controls worth preserving

- Separate mainline governance from isolated prototype work.
- Synthetic-only fixtures and explicit prohibition on real player/minor data in the prototype.
- Evidence and verification are distinct from assertion, authority and truth.
- Project-owner acceptance is an explicit gate, not inferred from activity.
- The workflow continues through browser suites after an earlier suite fails and preserves an aggregate failing exit status.
- Rejected import scenarios check that prior visible state is retained.
- UI-008 remains open rather than being closed by a narrow source-pattern count.

## 6. Transfer decisions for Codex-Guidas

| Proposed lesson | Transfer status | Codex-Guidas destination |
|---|---|---|
| External engagement must not outrun demonstrable maturity; distinguish concept discovery from product validation and pitching | Derived, context-sensitive; doctrine remains proposed | `doctrines/prototype-first-integrity.md`; lesson CG-042 |
| Test inventory and status summaries must reconcile to the exact source revision | Observed | Lesson CG-043 |
| Exact root-envelope validation does not establish nested payload validity or full import atomicity | Derived from source review; runtime proof pending | Lesson CG-044 |
| Current project status must preserve exact branch/commit, historical run boundaries and unknowns | Existing rule reinforced; no duplicate lesson created | Existing operating principles and evidence-first method |

Transfer principles, not ScoutSA-specific policy, domain assumptions or authority. Every target project must define its own permitted engagement, safeguarding, release and acceptance gates.

## 7. Final audit conclusion

ScoutSA has a meaningful internal prototype and a disciplined evidence/governance structure. It is not yet accepted as a completed prototype. The latest exact branch head has no verified test result in the evidence inspected here. The external engagement hold is explicit and should be respected without exception.

The most important transferable lesson is not “never speak to anyone before writing code.” It is:

> **Never let external claims, asks or implied capability outrun what the project can actually demonstrate. A concept must be presented as a concept; a prototype as a prototype; and a product as a product only when the evidence supports that claim.**

For ScoutSA, the stricter owner-approved order remains **Build → Test → Audit → Accept → Demonstrate → Pitch**.

No ScoutSA source files were changed by this audit. No ScoutSA gate, acceptance state or external-engagement hold was changed.


## Follow-up source review — 2026-11-24, later ScoutSA branch head

After this audit, nested Match-Day Handoff hardening was committed on ScoutSA's same isolated prototype branch. The current branch head at this follow-up is `d639cdf380530e4a3cb65576db7d055ce36cb1cd`.

- Importer source blob: `73c2434278cc81b56c61a1e14d742a81b108f74c`.
- Browser smoke source blob: `4a58f43a38ef7cd19f9ead44eb48c693d1d3b2f5`.
- Contract source blob: `6bc93fe2fb18caa3ecc0c1749e033c178ba9fda8`.
- Session ledger now contains Section 23.

The importer now has exact nested field allowlists for the current exporter records; bounded string and collection checks; source-origin and exact source-to-substitution/event/report checks; duplicate participation/appearance checks; substitution status/timing checks; and a rollback path for a post-validation render failure. New browser scenarios cover unknown nested properties, dangling source origin, null nested records, invalid/duplicate appearances, duplicate substitution relationships, oversized event collections and injected rendering failure.

**Verification is in progress, not complete.** Push workflow run #941 (`45354775012`) is pinned to the exact head above. At the time of this follow-up, the headless policy/documentation step and Playwright/Chromium installation had completed successfully, while the aggregate browser smoke step was still running. No browser pass is claimed until the run reaches a terminal result and its browser step is inspected.

This follow-up changes the status of F-04 from "not yet implemented" to "targeted source hardening committed; runtime verification pending." It does not establish that the new schema is bug-free, that every exporter state is covered, or that the importer is production-safe. The original source findings remain historically accurate at their inspected revision.


## Latest exact-head verification — 2026-11-24

The subsequent ScoutSA source and documentation updates were verified at exact branch head `8cdd62e5ae3316024fddef6fc7afb50f38af2520` by push workflow [#960](https://github.com/Moshoeshoe333/ScoutSA/actions/runs/45356935933).

- **122/122** Node tests passed.
- **12/12** configured Playwright/Chromium browser smoke scripts ran and passed.
- **24/24** specialist workspace interaction groups passed.
- The run's head SHA matches the ScoutSA branch head cited above.

The run includes the nested Match-Day Handoff importer checks and the regression corrections made after earlier failed attempts. Those earlier failures exposed test/contract mismatches; they were investigated and corrected rather than treated as passes. The successful run is current-head synthetic regression evidence, not formal prototype acceptance, full AST/runtime security certification, real-world safeguarding, legal compliance, user validation or product-market-fit evidence.

ScoutSA remains on its isolated `prototype/internal-demo` branch. UI-008 remains OPEN; the separate baseline-pinned AUD sequence remains blocked; mainline, real-data, production, deployment, pilot, external validation and pitching holds remain unchanged. The project has not been formally accepted as complete.
