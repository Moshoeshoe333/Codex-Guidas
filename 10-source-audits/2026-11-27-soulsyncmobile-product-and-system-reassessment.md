# SoulSyncMobile Product and System Reassessment

**Review date:** 2026-11-27  
**Review ID:** SM-REASSESS-2026-11-27-01  
**Application repository:** Moshoeshoe333/SOULSYNCMOBILE (private)  
**Branch / baseline:** main — 1f50bd3387c61d51868140ec3776b94150a2d4c6  
**Review type:** Read-only product, architecture, security, privacy and verification assessment  
**Authority:** Recommendations only; no application implementation or gate transition authorised  
**Method:** Existing source → execution evidence → interpretation → proposed product boundary

## 1. Executive decision

**Recommendation: retain the project, but narrow its first product to a privacy-first, offline, manual scam-message and URL triage assistant.**

Do not attempt to build a full antivirus, device guardian, SMS interception service, bank-integrated fraud platform, threat-intelligence platform or subscription product at this stage.

The current codebase is a small technical prototype, not yet a complete mobile security product. It has a useful foundation:
- offline deterministic analysis;
- a typed TypeScript implementation;
- South African bank/SARS/eWallet/airtime signal patterns;
- basic normalisation for zero-width characters, selected Unicode lookalikes and percent-encoded text;
- synthetic threat fixtures and storage fault-injection tests.

The main weakness is not lack of features. It is a mismatch between what the code can establish and what the user-facing product appears to say. It also stores complete scanned message content without a clearly defined product need, while offering no visible history, export or deletion controls in the current screen.

The review recommends:
1. Keep the offline, deterministic, manual scanning concept.
2. Change the result language and decision semantics so that a lack of detected signals is never presented as verified safety.
3. Stop persisting raw scanned text by default.
4. Remove or redefine the unvalidated Harmony score and numeric confidence score.
5. Make storage and scan failures visible and distinguish unknown/unavailable from an ordinary empty state.
6. Improve the South African scam corpus and false-positive/false-negative evaluation before expanding features.
7. Defer SQLite, Rust, AI/cloud scanning, automatic SMS access, live threat feeds, subscriptions and broad product surface additions until justified by evidence.

**No app source, test, dependency, workflow, package manifest or gate was changed by this review.**

## 2. Exact baseline and material evidence

The private application repository was re-read at exact main commit:

- Repository: Moshoeshoe333/SOULSYNCMOBILE
- Branch: main
- Full SHA: 1f50bd3387c61d51868140ec3776b94150a2d4c6
- Tree SHA: 2efd17a3e4abcb4401b9bbeabdb784db58654c24
- Current README status: OPEN / evidence pending
- Current intended stack: Expo SDK 57, React Native 0.86, React 19.2.3 and TypeScript

The repository tree contains one active app screen (App.tsx), one Guardian hook, one heuristic service, one storage manager, type definitions, three test files and a small mock/hook test harness. There is no implemented multi-screen Ledger/Tips/Pro surface at this baseline.

### Current CI evidence

GitHub Actions run [45989069198](https://github.com/Moshoeshoe333/SOULSYNCMOBILE/actions/runs/45989069198) was re-read. It completed successfully on the exact current application SHA 1f50bd3387c61d51868140ec3776b94150a2d4c6.

Recorded environment:
- Ubuntu 26.04.1 hosted runner
- Node 22.13.1
- npm 10.9.2

Recorded outcomes:
- TypeScript typecheck: passed
- Threat fixtures: 13 fixture cases passed
- Storage fault-injection tests: 10/10 passed
- Guardian hook fault-injection tests: 2/2 passed
- Workflow conclusion: success

This is valuable E1/CI evidence for the defined checks. It is not an Android/iOS build, physical device installation, user workflow test, offline-network witness or G-BOOT runtime pass.

### Dependency-audit nuance

The same CI log reports three Moderate npm-audit entries in the resolved dependency graph, all associated with the minimatch GHSA-g3hv-75wg-m249 advisory through Expo / @expo/fingerprint dependency paths. The workflow intentionally uses npm audit --json followed by || true, so audit findings do not fail the job.

The advisory concerns pattern-amplification resource exhaustion in affected minimatch versions. Expo maintainers discussed the exact development-tooling dependency path in [Expo issue #52735](https://github.com/expo/expo/issues/52735): they stated that the relevant patterns are controlled by project changes and that this usage does not create an app-user vulnerability; the issue was closed as completed on 6 November 2026. This is important context. Do not treat the audit output as evidence that SoulSyncMobile is exploitable by an ordinary user. Equally, do not silently ignore audit output.

The source tree has no committed package-lock.json. The CI therefore runs npm install rather than npm ci and resolves the dependency graph at execution time. This is a reproducibility and supply-chain hygiene issue. The output's suggested expo@52 downgrade is a major SDK downgrade and should not be applied blindly to an SDK 57 project.

### Build and runtime boundary

The repository's older build-plan/evidence records a successful historical EAS APK build on an earlier source revision, while explicitly leaving physical installation, runtime, restart persistence and offline-device evidence unwitnessed. The current main workflow visible in the source tree is the typecheck/test workflow only. Current main has no current-commit Android device-runtime witness.

## 3. What the current app actually does

| Feature | Current status | Assessment |
|---|---|---|
| Manual message input | Implemented | The user pastes or types content into one multiline input |
| Local heuristic analysis | Implemented | Pure TypeScript regex/normalisation path; no live threat reputation |
| South African indicators | Partial | Five bank names, SARS/tax language, urgency, airtime/eWallet and a small URL indicator set |
| Zero-width and selected lookalike handling | Implemented, narrow | Useful start; not comprehensive Unicode/homograph defence |
| Percent decoding | Implemented, narrow | One decode attempt across the input; malformed escapes are preserved |
| URL extraction | Partial | Recognises http/https strings, configured shorteners, raw-IP-shaped hosts and a limited hostname structure heuristic |
| Risk/severity output | Implemented, uncalibrated | Count-and-threshold score; not a probability or measured likelihood |
| Confidence score | Implemented, not calibrated | Fixed formula, not supported by calibration evidence |
| Harmony score | Implemented, undefined as a security metric | Starts at 100 and decreases with scan severity; no demonstrated meaning, decay or recovery model |
| Local incident persistence | Implemented | Persists the whole IncidentLog array through AsyncStorage |
| User-accessible incident history | Not implemented in current App.tsx | UI shows only a count |
| Clear-history control | Hook method only | Not wired to the current UI |
| JSON export | Hook method only | Not wired to the current UI; exports records including original input text |
| User-facing storage error state | Not implemented | Hydration failures are caught and converted into a ready/empty state |
| User-facing save-failure state | Not implemented | App.tsx awaits the promise without a local catch/error message |
| SMS inbox ingestion/interception | Not implemented | The app is a manual paste scanner, not an SMS reader |
| Link blocking / browser protection | Not implemented | The result does not block, prevent or approve an external navigation |
| Sender/brand authentication | Not implemented | A bank name in text is not proof of impersonation or sender identity |
| Live URL/domain reputation | Not implemented | Offline-only local rules have no current reputation data |
| Cloud sync/account/telemetry | Not observed in current source | No basis to claim cloud monitoring or user accounts |
| Multi-screen Ledger/Tips/Pro | Roadmap only | Not part of the current app |
| Android/iOS production runtime | Unwitnessed at current main | G-BOOT remains open |

The actual product surface is therefore much narrower than the broader phrase "personal security ledger" may suggest. A more accurate description today is "experimental offline manual scam-message triage prototype".

## 4. Feature decisions: keep, change, add, defer and scrap

### KEEP

**A. Offline, local-first manual analysis**

This is the strongest product boundary. It avoids sending message contents to a remote service, reduces dependency on connectivity and is appropriate for privacy-sensitive scam triage. Keep the no-cloud/no-LLM core unless a separate user-valued need and consent/privacy assessment justify a later optional service.

This remains an architectural intention until the G7 network-disabled execution witness is completed.

**B. Deterministic, inspectable TypeScript rules**

Keep the pure local function and typed result direction. It is easier to reproduce, test and explain than opaque prompt-driven classification. Keep rule versioning and explicit indicators.

**C. South African context**

Keep the local context: Capitec, FNB, Absa, Nedbank, Standard Bank, SARS, airtime, eWallet and urgent payment language. It is a sensible starting set, not adequate national coverage.

**D. Normalisation primitives**

Keep NFKC, removal of selected zero-width characters, selected homoglyph handling and defensive URL parsing as an initial layer. Expand only through adversarial fixtures and expert review.

**E. Existing test discipline**

Keep the deterministic threat fixtures and storage/Guardian fault-injection harness. The tests are useful and currently pass on the exact main SHA. Add coverage only where it closes a real behavioural gap.

**F. Fail-closed analysis exception behaviour**

Keep the principle that an analysis exception must not be turned into a safe result. However, separate analysis failure from persistence failure and communicate both to the user honestly.

### CHANGE

**A. Change the product's promise**

Describe the product as a manual scam-message and URL triage assistant. It helps a person pause, inspect signals and choose a safer next step. It does not certify a message as safe, verify a sender, inspect the whole device, block a link, or replace antivirus, bank fraud controls or official reporting channels.

**B. Replace the current SAFE / ALLOW certainty**

The current mapping is a risk-communication defect. A single shortened URL or raw-IP URL produces one indicator (14 points), while riskLevel below 25 maps to safe and safe maps to ALLOW. The current fixtures explicitly expect SAFE / ALLOW for those cases.

The app does not technically allow or deny a browser action. It merely displays an advisory classification. The UI should communicate what was and was not detected, not imply an external access-control decision.

Candidate semantic states for owner review:
- No known indicators detected — not verified safe.
- Caution — verify independently.
- High-risk indicators detected — stop and verify before acting.
- Unable to assess — malformed input, unsupported input or insufficient evidence.

Do not change the existing PolicyAction contract or thresholds until the owner approves the outcome contract and a labelled test corpus exists.

**C. Remove or redefine numeric confidence**

The current value is 70 when no indicators are found and 55 + 10 per indicator, capped at 98 otherwise. This is not a calibrated probability. It should not be displayed as statistical confidence.

**D. Retire the Harmony score from the MVP pending validation**

The score starts at 100 and decreases by a function of severity. The repository documents recovery/decay as unimplemented. No evidence shows that this score corresponds to a measurable safety, resilience, wellbeing or behavioural construct. It can confuse users and contributes to the two-key persistence seam.

Recommendation: remove it from the user-facing product unless a clear user need, validated meaning, bounded interpretation and measurable benefit can be demonstrated. If removed, revisit the second persistence key and DEF-2026-002 under an approved consistency contract; do not automatically close that defect.

**E. Change data retention**

Do not retain raw SMS/message text by default. Process it in memory, show the result, then discard the raw input unless the user explicitly chooses an approved retention path.

If a local history feature is retained, persist only the minimum useful sanitised record: scan time, source category, rule-set version, detected indicator codes and the advisory outcome. Avoid storing raw message bodies, authentication tokens, full URLs with query/fragment values or derived fingerprints that can reveal the original content.

If raw-content retention is later justified, it needs a separate owner-approved data classification, purpose, consent, retention duration, deletion, export, backup, key-management and recovery contract.

**F. Make storage state and failures explicit**

Keep distinct states for loading, successfully empty, successfully populated, unavailable, corrupt and partially written data. A read failure must not be presented as a successfully loaded empty ledger.

The current App.tsx has no local catch or visible save-failure state around analyzeAndLogInput. A persistence rejection should produce a clear non-success state without losing the user's ability to understand whether analysis completed and whether the result was saved.

Runtime schema validation is also required: the current JSON.parse<T> cast does not validate that the persisted incident value is actually an array of valid IncidentLog objects.

**G. Re-evaluate local history**

The hook exposes clearHistory and exportLedgerAsJSON, but the current App.tsx does not expose either operation. It shows only the total incident count. This is not a coherent reason to retain full message contents indefinitely.

If history is a user-valued feature, make it explicit, sanitised, user-controlled, bounded and deletable. Otherwise remove persistence from the first MVP and keep scans ephemeral.

### ADD — only after the product contract is ratified

1. **Clear safety guidance:** tell users not to click, pay, share OTPs or follow instructions in suspicious messages. Recommend independently opening the bank's official app or using a contact channel found separately from the message.
2. **Transparent indicator explanations:** explain exactly which pattern matched (for example urgency language, bank-name mention, shortened URL), why it matters and what cannot be inferred.
3. **Unknown/unavailable result:** never force malformed or unsupported input into a safe answer.
4. **Input and resource bounds:** establish a maximum input length and graceful handling for long messages, many URLs and malformed/encoded input.
5. **User-controlled sanitised history, if validated:** provide view, per-record delete, clear-all, retention and export controls. Default to ephemeral scanning until then.
6. **Broader South African fixture coverage:** evaluate courier/delivery, mobile network, electricity/utility, employment/job, government-payment, eWallet, airtime and impersonation patterns. Include Afrikaans, English, isiZulu and Sesotho examples with appropriate human review. The current rule engine is English-centric; don't claim multilingual coverage before tests support it.
7. **Independent labelled evaluation corpus:** include benign, scam, ambiguous, adversarial, malformed and legitimate bank/government notifications; record source provenance and avoid real personal data.
8. **Accessibility and comprehension testing:** ensure results are understandable without relying on colour alone and test whether users understand that the app is advisory.
9. **Versioned rule packs:** record rule-set version in every sanitised scan result so later changes remain explainable and reproducible.

### DEFER

- Automatic SMS reading, notification interception, clipboard monitoring or accessibility-service surveillance. These materially increase privacy, permission, platform-policy and user-trust burdens; the current manual flow does not justify them.
- Live domain reputation feeds or external threat intelligence. Consider only as an optional, explicit, privacy-reviewed future feature; sending a URL to a remote service may itself disclose sensitive data.
- AI/LLM analysis in the security decision path. It conflicts with the current deterministic/offline boundary and adds uncertainty, data exposure and provider dependency.
- Cloud accounts, synchronisation, community reporting and shared threat feeds. Require a demonstrated user need, consent, moderation, privacy and operational capability first.
- Subscription / Pro / monetisation surface. No adoption, retention or willingness-to-pay evidence was inspected.
- SQLite production migration. G8 remains open, but a storage engine should not be chosen before the raw-data and persistence contracts are settled. SQLite alone does not encrypt sensitive data.
- Rust/native analysis core. Current workload and architecture do not demonstrate a material performance or portability need. Keep TypeScript as the reference implementation.
- Broad Ledger/Tips/Pro navigation. Build only a validated screen that supports the focused triage workflow.

### SCRAP FROM THE MVP

- Raw scanned message persistence by default.
- User-facing numerical Harmony score until its meaning and benefit are validated.
- Numerical confidence score until it is empirically calibrated.
- SAFE / ALLOW wording that can be mistaken for verified safety or actual link control.
- Claims or visual affordances implying antivirus protection, inbox monitoring, bank verification or URL blocking.
- Unused React Navigation and safe-area dependencies if a follow-up dependency audit confirms no code path needs them. They are declared but not imported by the current single-screen App.tsx.
- Features that exist only as labels or future roadmap descriptions but do not support the narrow first user task.

## 5. System findings that deserve priority

| ID / area | Current observation | Recommended treatment |
|---|---|---|
| DEF-2026-001 — hydration | Read failure is caught, state becomes empty/unmeasured and ready=true; users may proceed as if storage was loaded | Keep open; distinguish unavailable from empty and verify write behaviour after failed hydration |
| DEF-2026-002 — consistency | Incident and Harmony values are separate writes; current tests demonstrate the injected second-write case but do not complete retry/restart semantics | Keep open until owner-approved consistency contract and full recovery evidence |
| DEF-2026-003 — privacy | Complete scanned input is included in IncidentLog and serialised to AsyncStorage | Keep open; define retention and minimisation before storage redesign |
| DEF-2026-004 — risk wording | Shortened/raw-IP URL indicators can still yield SAFE / ALLOW | Keep open; ratify advisory result semantics and evaluate false negatives |
| UI error path | App.tsx awaits the scan promise without local catch or visible save-failure state | Add after UI outcome contract; no implementation authorised here |
| Input handling | No visible input-length bound; raw message can be arbitrarily large | Add bounded input and stress tests |
| Ledger integrity | Persisted JSON is cast to IncidentLog[] without runtime schema validation | Add schema validation and malformed-shape recovery tests |
| Growth/retention | Incident array grows without an explicit retention cap and is re-serialised as a whole on each write | Define whether history is needed, then bound/prune it under an approved contract |
| Decision calibration | Severity counts pattern matches; thresholds and confidence score are not empirically calibrated | Build labelled corpus; measure false positives and false negatives before adjusting thresholds |
| UX honesty | Current UI says Action and Risk, but does not clearly say no link is blocked or verified | Change language; test comprehension |
| Dependencies | React Navigation and safe-area-context are declared but not used by the current App.tsx | Remove only after a branch-level usage audit and CI confirmation |
| Dependency reproducibility | No committed package-lock.json; CI uses npm install | Add a reviewed lockfile and deterministic install path after dependency review |
| Runtime evidence | Current CI is green, but current main has no device/offline runtime witness | Preserve G-BOOT/G7 boundaries and collect device evidence before readiness claims |

## 6. Threat-engine review

The current engine is a bounded pattern matcher, not a general scam-detection or malicious-URL verification service.

### Positive characteristics
- Pure, deterministic function with no external network dependency visible in the inspected implementation.
- Explicit, versionable TypeScript data contracts.
- Some useful South African brand/service patterns.
- Basic handling for zero-width characters, NFKC and a small set of selected lookalikes.
- URL parsing uses the URL constructor rather than executing or opening links.
- Existing test fixtures cover benign, bank, SARS, urgency, eWallet, short URL, IP URL, zero-width, lookalike, encoded, compound and malformed examples.

### Coverage limitations
- The presence of a bank name is not proof of impersonation. No trusted sender/domain relationship is checked.
- Only a small bank list and a small set of English-language urgency / SARS / airtime / eWallet terms are covered.
- Only http/https substrings are extracted; configured URL shorteners are a small fixed list.
- No reputation, DNS, certificate, sender identity, domain-registration or live blocklist check exists. That is consistent with an offline MVP, but it limits the claims it can make.
- The lookalike mapping is a limited hand-maintained map, not comprehensive Unicode confusable detection.
- The severity formula counts matching patterns and adds class bonuses. The current confidence score is not calibrated.
- Existing fixtures validate expected current outputs; they do not prove real-world accuracy.

Do not expand the regex list indiscriminately. First establish a corpus with positive and negative examples, source provenance, labels, category coverage and an independent review process. More rules can increase false positives and may teach users to distrust useful warnings.

## 7. Data protection and storage guidance

React Native's official security guide describes AsyncStorage as an unencrypted key-value store and recommends not using it for secrets. It also notes that the app sandbox separates app data from other ordinary apps; this does not eliminate all risk from a compromised device, backups or other disclosure paths.

Expo SecureStore is designed for small local key-value secrets and may reject large payloads; Expo's documentation specifically warns that platform limits exist. It should not be used as a bulk incident-history database. If the owner later approves encrypted record storage, separate the data store from key management and review Android backup, iOS Keychain persistence, key invalidation, uninstall/reinstall and recovery behaviour.

The preferred first action is data minimisation, not simply swapping storage libraries:
1. Do not persist original message text by default.
2. Do not export raw input by default.
3. Avoid logging raw message text, URLs with tokens, OTPs or personal/financial data.
4. Define how the user views, deletes and expires any retained sanitised finding.
5. Only after that, decide whether any encrypted persistent data store is justified.

No claim of POPIA compliance should be made from offline/local storage alone.

## 8. Recommended focused MVP

**Product statement**

SoulSync Guardian is a privacy-first, offline manual scam-message and URL triage assistant for South African users. It explains detectable signals and recommends independently verifiable next steps. It does not certify a message as safe, verify the sender, monitor the inbox, block external links or replace antivirus/bank controls.

**Core user journey**
1. User chooses or pastes a message/URL manually.
2. App analyses it locally; raw input stays in memory by default.
3. App displays what matched, why it matters, what remains unknown and a plain-language next step.
4. User independently verifies through a trusted channel.
5. The app discards raw input. If sanitised history is later approved and useful, it is explicitly user-controlled and time-bounded.

**MVP non-goals**
- automatic SMS permission;
- browser interception or blocking;
- live threat feed;
- cloud account or synchronisation;
- AI/LLM decision engine;
- security score or confidence percentage;
- subscription/paywall;
- SOC/antivirus/bank-protection claims.

## 9. Proposed work sequence (decision gates, not implementation approval)

### Gate A — Product and data contract
- Ratify the single target user and primary problem.
- Ratify that results are advisory and links are not blocked.
- Decide whether scan history is necessary; default recommendation is ephemeral scans with no raw text persistence.
- Define what a sanitised record may contain, retention and deletion rules.
- Decide whether Harmony should be removed from the product.

**Exit evidence:** owner-approved product boundary and data contract. No code change before this.

### Gate B — Outcome semantics and heuristic evaluation
- Define no-signal, caution, high-risk and unable-to-assess semantics.
- Define why a shortened/raw-IP/malformed URL should not imply verified safety.
- Build a versioned labelled synthetic/anonymised corpus for relevant South African contexts and languages.
- Measure false positives and false negatives and review user comprehension.
- Replace uncalibrated score/confidence claims only after agreed criteria exist.

**Exit evidence:** approved decision table, corpus provenance, evaluation report, acceptance thresholds.

### Gate C — Minimal safety and privacy slice
After explicit owner authorisation, implement only approved changes: raw-text minimisation, honest storage/error state, user-visible failure handling, bounded input, schema validation and the approved advisory UI. Keep the smallest architecture possible.

**Exit evidence:** exact diff, tests, CI, data-inspection results, deletion/retention checks and reviewer sign-off.

### Gate D — Runtime verification
- Android and iOS build evidence on the exact candidate SHA.
- Install/boot on real devices.
- Manual scan flow and error states.
- Offline/network-disabled execution.
- Persistence/restart behaviour only if sanitised history is approved.
- Storage/backup/log/export review.
- Accessibility and adult user-comprehension evaluation.

**Exit evidence:** exact build artefacts, device/environment, steps, result, failures and G-BOOT/G7 evidence. CI alone does not close this gate.

### Gate E — Expansion decision
Only after repeatable user evidence should the team consider live threat updates, additional languages/categories, accounts, cloud sync, or paid functionality. Each addition needs its own privacy, security, cost and operational review.

## 10. Measures that would demonstrate genuine progress

Do not measure success by number of screens, rules, features or commits. Measure:
- false-negative rate on independently labelled relevant scam examples;
- false-positive rate on benign and legitimate financial/government messages;
- coverage by scam category, language and content type;
- rate of unsupported/unknown cases correctly reported as unable to assess;
- user comprehension of the advisory boundary and next steps;
- local processing latency and graceful handling of large inputs;
- percentage of scans that leave no raw text in persistent storage, logs or exports by default;
- successful deletion/retention enforcement if sanitised history is enabled;
- reproducible build and real-device/offline success on exact candidate commit;
- repeat use and user trust without inflated safety claims.

## 11. Explicit non-decisions

This review does not:
- change application code or tests;
- change ALLOW/WARN/DENY or any thresholds;
- choose SQLite, SecureStore, Rust or an encryption library;
- authorise telemetry, live threat feeds, LLM inference, SMS access or browser interception;
- close DEF-2026-001/002/003/004;
- advance G0–G8, G-BOOT or release readiness;
- establish POPIA compliance, antivirus capability or market demand.

The TypeScript implementation remains the baseline. Architectural complexity must be earned by evidence.

## 12. Sources

### Application evidence
- [SOULSYNCMOBILE main at 1f50bd3387c61d51868140ec3776b94150a2d4c6](https://github.com/Moshoeshoe333/SOULSYNCMOBILE/tree/1f50bd3387c61d51868140ec3776b94150a2d4c6)
- [Latest current-main CI run 45989069198](https://github.com/Moshoeshoe333/SOULSYNCMOBILE/actions/runs/45989069198)
- [DEF-2026-001](../11-defect-intelligence/DEF-2026-001-storage-hydration-failure-masked-as-empty-ledger.md)
- [DEF-2026-002](../11-defect-intelligence/DEF-2026-002-multikey-scan-persistence-is-not-atomic.md)
- [DEF-2026-003](../11-defect-intelligence/DEF-2026-003-raw-scan-content-retained-in-asyncstorage.md)
- [DEF-2026-004](../11-defect-intelligence/DEF-2026-004-risk-signals-can-be-rendered-as-safe-allow.md)

### Official platform and security references
- [React Native Security](https://reactnative.dev/docs/security)
- [Expo SDK 57 release notes](https://expo.dev/changelog/sdk-57)
- [Expo SecureStore documentation](https://docs.expo.dev/versions/latest/sdk/securestore/)
- [OWASP MASVS-STORAGE](https://mas.owasp.org/MASVS/05-MASVS-STORAGE/)
- [OWASP MASWE-0001 — Sensitive data stored unencrypted in private storage](https://mas.owasp.org/MASWE/MASVS-STORAGE/MASWE-0001/)
- [minimatch GHSA-g3hv-75wg-m249](https://github.com/isaacs/minimatch/security/advisories/GHSA-g3hv-75wg-m249)
- [Expo issue #52735 — analysis of Expo's minimatch development-tooling dependency path](https://github.com/expo/expo/issues/52735)

**Final recommendation:** protect the user, narrow the promise, minimise the data, make uncertainty visible and verify the core journey before adding more features.
