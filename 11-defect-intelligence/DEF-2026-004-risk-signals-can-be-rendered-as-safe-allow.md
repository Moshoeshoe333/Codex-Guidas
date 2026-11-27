# DEF-2026-004 — Risk signals can be rendered as SAFE / ALLOW

- **State:** Investigating
- **Severity:** S4 (source/test-defined user-safety concern; actual user impact not established)
- **Date detected / last updated:** 2026-11-27
- **Owning project/repository:** SoulSyncMobile — Moshoeshoe333/SOULSYNCMOBILE
- **Affected branch/ref:** main
- **Affected full commit SHA:** 1f50bd3387c61d51868140ec3776b94150a2d4c6
- **Owner:** SoulSyncMobile project maintainer (to be assigned)
- **Related CI run:** [45989069198](https://github.com/Moshoeshoe333/SOULSYNCMOBILE/actions/runs/45989069198), successful on the exact affected commit
- **Related lessons:** CG-002, CG-011, CG-052; proposed CG-053
- **Reporter/source:** Codex-Guidas read-only product/system reassessment

## 1. Summary

The offline heuristic engine can detect a URL signal such as a shortened URL or raw IP URL, yet the aggregate score remains below the caution threshold. It returns riskLevel "safe" and action "ALLOW", and the UI renders those labels directly.

This is a source- and fixture-backed risk-communication concern. It may give users stronger reassurance than the engine's evidence supports. No user misunderstanding, financial loss or other actual harm is established.

## 2. Expected behaviour

The product should distinguish:
- no signal detected by the current local rule set;
- suspicious signal detected;
- insufficient evidence / unable to assess;
- high-risk combination of signals.

A lack of matched indicators must not be described as proof that a message or URL is safe. If the app does not actually prevent a user from opening a URL, its UI must not imply that it has allowed or blocked that action. Any revised thresholds, action vocabulary and user-facing language require an owner-approved policy contract and representative false-positive/false-negative evaluation.

## 3. Observed behaviour

At application baseline 1f50bd3387c61d51868140ec3776b94150a2d4c6:

1. src/services/threat/heuristics.ts adds "shortened URL" for configured URL shorteners and "raw IP URL" for IPv4-shaped URL hosts.
2. Each detected indicator adds 14 points. With one URL indicator the score is 14.
3. Scores below 25 map to riskLevel "safe".
4. actionForRisk("safe") returns "ALLOW".
5. App.tsx displays Action: ALLOW and Risk: SAFE without a nearby explanation that no safety verification was performed.
6. The app does not intercept the browser or messaging app and does not technically block or permit the destination URL; the result is an advisory classification.

The current fixtures explicitly expect this output:
- URL-001: shortened URL https://bit.ly/verify-account → severity 14, safe, allow.
- URL-IP-001: http://192.168.1.10/login → severity 14, safe, allow.
- MALFORMED-001: malformed URL plus urgency text → severity 14, safe, allow.

The fixture suite passed in GitHub Actions run 45989069198 on the exact application SHA. That confirms the behaviour is intentional in the current tests; it does not establish that the user-facing risk language is safe or calibrated.

## 4. Impact and scope

- **Actual impact:** Not established; no user report, misuse or loss was inspected.
- **Potential impact:** A user may interpret SAFE or ALLOW as a verified safe URL or as a technical blocking/allowing decision, even where the engine has detected a suspicious URL characteristic or has incomplete visibility.
- **Affected users/data/components:** Users relying on manual scan output; heuristic risk thresholds, action mapping, fixtures and UI wording.
- **Scope known or unknown:** The cited behaviour is confirmed in source and tests at the exact baseline. Real-world false-negative rate, user interpretation and resulting outcomes are unknown.
- **Workaround / containment:** Treat every result as advisory and verify through independently obtained official channels. The app itself should not yet be represented as a link-blocking or safety-guarantee product.

## 5. Evidence ledger

| Evidence ID | Type | Exact ref | Observation | Limitation |
|---|---|---|---|---|
| E-001 | Source | heuristics.ts blob d108f896cb04c5e65f743269a8f1b669e7065d53 at app commit 1f50bd3387c61d51868140ec3776b94150a2d4c6 | URL indicators add 14 points; scores below 25 map to safe; safe maps to ALLOW | Source inspection only |
| E-002 | Test fixture | fixtures.ts blob 0517cdfe3c1b078c81ae4d12eaa74babe043902c at same commit | Shortened URL, raw IP URL and malformed URL fixtures expect ALLOW | Fixture expectations are not product validation |
| E-003 | UI | App.tsx blob 17b1b37df4f93547c099129cff883571c5e9b1d5 at same commit | Displays Action and Risk labels directly, with no local explanation of the non-verification boundary | No device/UI usability test |
| E-004 | CI | Run 45989069198, exact source SHA 1f50bd3387c61d51868140ec3776b94150a2d4c6 | Threat fixture command completed successfully and reports 13 fixture cases passed | Test execution confirms current expectations, not that the expectations are safe or accurate |
| E-005 | Product boundary | README and SECURITY.md at same baseline | App is an offline heuristic scanner; SECURITY.md says it is not an antivirus or guarantee of safety | Does not resolve ambiguity created by SAFE / ALLOW labels |

## 6. Root-cause analysis

- **Status:** Suspected risk-communication and decision-threshold design gap; current mapping is confirmed in source.
- **Hypothesis:** The numeric threshold model and ALLOW vocabulary compress "no high-scoring pattern" and "safe" into one label, while the heuristic has no external reputation, sender verification or complete contextual view.
- **Evidence supporting:** E-001 through E-005.
- **Evidence contradicting:** No evidence that the app actually opened, executed or blocked a URL; ALLOW may have been intended only as the engine's low-risk policy output, not as an external action. The current UI does not make that distinction visible.
- **Discriminating test still needed:** Review the risk/outcome contract with the product owner and representative users; evaluate benign, suspicious, ambiguous, shortened, raw-IP, malformed, spoofed and unknown URL cases with an independently labelled corpus; test whether users interpret each output correctly.

## 7. Similarity search

- **Search terms:** false reassurance; safe label; allow action; URL risk; heuristic threshold; confidence calibration; unknown result
- **Lesson IDs searched:** CG-002, CG-011, CG-052
- **Prior defect IDs:** DEF-2026-001 storage hydration; DEF-2026-002 multi-key persistence; DEF-2026-003 raw text retention. They are not the same defect.
- **Similarity result:** Related to the general fail-closed / claim-strength principle, but the defect is specific to risk outcome vocabulary and threshold behaviour.

## 8. Corrective action

None authorised or implemented. First ratify:
- whether the scanner is purely advisory or is expected to control any external action;
- the meaning of each user-facing outcome;
- how insufficient evidence and unknown/malformed URLs are represented;
- whether a single URL indicator is enough to require caution;
- what evidence is required before any use of the word "safe";
- how thresholds are evaluated and versioned.

Do not change thresholds or policy action vocabulary from this finding alone.

## 9. Preventive and detective controls

**Proposed, not implemented:**
- Avoid a positive safety claim when the engine merely found no high-scoring pattern.
- Use explanatory outcomes such as "No known indicators detected — not verified safe", "Caution — verify independently", "High-risk signals detected", and "Unable to assess".
- Make clear that the app does not block URLs or scan other apps.
- Separate detected indicators from a calibrated risk estimate; do not call a fixed heuristic formula "confidence" without empirical calibration.
- Build a representative labelled test corpus and measure both false positives and false negatives.
- Require human-readable rationale and safe next steps for each outcome.

## 10. Regression and acceptance evidence

| Check | Procedure | Environment | Exact commit | Expected | Actual |
|---|---|---|---|---|---|
| P-01 | Evaluate shortened URL fixture | CI pure engine | 1f50bd3387c61d51868140ec3776b94150a2d4c6 | Product-approved outcome does not falsely imply verified safety | Existing test expects SAFE / ALLOW; change not authorised |
| P-02 | Evaluate raw IP URL fixture | CI pure engine | Same | Product-approved caution/unknown semantics | Existing test expects SAFE / ALLOW |
| P-03 | User comprehension test of result wording | Controlled adult usability test | Not run | Users understand the app did not verify or block destination | Not run |
| P-04 | Labelled corpus false-positive/false-negative evaluation | Controlled synthetic/anonymised dataset | Not run | Thresholds meet owner-approved criteria across relevant scam categories and language variants | Not run |

## 11. Residual risk and follow-up

The current thresholds and words are not calibrated against an independent representative dataset. A user may over-trust a low-risk label. No actual user harm has been established. Keep this finding Investigating until the product's advisory/operational boundary and outcome semantics are ratified and tested.

## 12. Closure decision

- **Decision:** Keep open / Investigating
- **Approver/authority:** SoulSyncMobile project owner
- **Acceptance criteria met:** No
- **Reason:** Outcome semantics, calibration and user comprehension remain unresolved.
- **Closure evidence:** None

## 13. Record propagation and synchronization

- **Canonical DEF record path:** 11-defect-intelligence/DEF-2026-004-risk-signals-can-be-rendered-as-safe-allow.md
- **Defect README register updated:** Yes — commit f6586a0e17a2009dde969222c4c10c080eeeb5b8
- **Chronological ledger follow-up added or linked:** Pending
- **Upstream source/run rechecked directly:** Yes — source blobs and current CI run re-fetched for exact main SHA
- **Exact tested commit and current project HEAD distinguished:** Yes — current main SHA is the tested SHA
- **Historical statements dated or qualified:** Yes
- **Related links checked:** Yes — source, fixture, UI and CI references read back
- **Atomic change / commit identity:** Detailed DEF created in fefecd2201d27eda5ceea47de1cf7dbfd6b42ce5; register updated in f6586a0e17a2009dde969222c4c10c080eeeb5b8. These linked documentation changes were not one atomic multi-file commit.

## 14. Reusable lesson

Proposed CG-053: absence of a detected signal is not proof of safety. Do not promote the lesson to Verified until risk wording and decision boundaries have been evaluated against a representative dataset and users.


## 15. Candidate outcome-semantics follow-up — PR #22 (2026-11-27)

**Disposition:** Mainline finding remains **Investigating**. The affected `main` baseline above has not changed. The candidate correction is on a separate, open, unmerged PR and is not a verified fix.

- **Candidate PR:** https://github.com/Moshoeshoe333/SOULSYNCMOBILE/pull/22
- **Branch:** `feat/gate-a-privacy-first-triage`
- **Inspected application source snapshot:** `d13038507107e993c55d1ae34f688f18bdeaef5e`

Candidate source evidence:
- The type contract (blob `561932c21b58a85e42ac501fb03edb9e938eb608`) defines `no_known_indicators`, `caution`, `high_risk_signals` and `unable_to_assess`; it no longer exposes the former `action` or numeric confidence fields.
- The heuristic implementation (blob `0c8528ac0785a014d7f22f5c112573e0d0d38f18`) classifies malformed URLs as unable to assess and detected URL indicators as at least caution.
- Updated fixtures (blob `686022cb846a0c29fe0d6817dcb8fa2e7e01f61f`) expect caution for shortened and IP-address URLs and unable-to-assess for the malformed URL example. The updated fixture test (blob `dda7aefdead2026e94eae0d90910c6b728104d40`) asserts the result has no confidence or enforcement-action field.

These are source and test-specification changes only. GitHub Actions run [46017679147](https://github.com/Moshoeshoe333/SOULSYNCMOBILE/actions/runs/46017679147) on the exact candidate SHA concluded **FAILURE**; the job returned no step records and its log endpoint returned 404 / BlobNotFound. No passing test-suite witness is claimed. No independent labelled dataset, representative false-positive/false-negative evaluation, threshold calibration, or user-comprehension evidence is available.

**Acceptance/closure:** Not met. Keep open against mainline. Reassess only after a reviewed merge, passing exact-head checks and separate corpus/user evaluation. Fixture expectations do not prove real-world detection efficacy; the new labels remain advisory, not a safety guarantee.
