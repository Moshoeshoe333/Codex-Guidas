# 33-Perspective Register — Three-Project Case-Study Review

**Review date:** 2026-11-18  
**Status:** Comparative desk review; evidence-backed repository checks are limited and explicitly identified below.  
**Purpose:** Test the usefulness of the proposed 33-perspective register against ScoutSA, SoulSyncMobile and Mall Navigre without overstating validation or granting implementation authority.

## 1. Executive finding

The three project contexts expose useful blind spots and improve the operational wording of the register. They do **not**, on the evidence inspected for this review, establish that the register has been empirically validated or formally ratified as Version 1.0.

The correct disposition is:
- retain the 33 perspectives as a **proposed working register**;
- integrate the five operational refinements below into existing perspectives rather than expanding beyond 33;
- record the three reviews as controlled desk-review case studies;
- require real stakeholder/device/field evidence before calling any case study empirical;
- preserve each project's own gate and authority boundary.

**No implementation, deployment, pilot or production authorization is created by this review.**

## 2. Evidence boundary

### 2.1 ScoutSA — Tournament Organiser workflow

**User-proposed target:** A narrow organiser workflow covering tournament registration, team associations, fixtures/results, correction history and scoped verification status.

**Repository evidence inspected:** ScoutSA on main, README blob 2fdc4689e53bd0ac9e6a9ec2e3695c6eb493fe70; docs/00-gate-status.md blob c79cde2979ad44f2a5811f20cf573cdc428a6013.

**Observed current boundary:** Gate 1 closed; Gate 2 closed at conceptual level; MVP and schema boundaries frozen; SQL is a reviewed draft with an isolated non-production PostgreSQL runtime witness. Migration/database execution, RLS, API, UI, production implementation and pilot remain on hold or unauthorized. The controlled next move is external validation. Mainline and the isolated prototype/internal-demo branch are separate.

**Assessment:**
- Safeguarding, guardian authority, consent, disclosure and access separation are material non-compensable concerns.
- Tournament, team, match, player and coach associations must not be translated directly into new tables or public views without checking the frozen domain/relationship boundary and unresolved carry-forward decisions.
- An append-only correction history is a strong proposed requirement, but its exact semantics and authorization must be derived and ratified before implementation.
- An organiser verification label must be scoped: who verified what, under which authority, at what time, using which evidence? It must not imply that a player, team, result or opportunity is guaranteed.
- Offline/resilient score entry and low-friction field use are hypotheses requiring realistic workflow tests.
- The proposed vertical slice is not currently authorized for implementation on mainline. A supervised adult-organiser discovery/usability activity may be considered only within the current external-validation scope and safeguarding constraints.

**Case-study result:** The register correctly surfaces human safety, consent, data disclosure, error correction, field usability, evidence provenance and adoption. It also catches a governance conflict: a proposed workflow cannot bypass the existing mainline implementation hold.

**Evidence level:** Repository/document inspection only for the status above. No live organiser test, production workflow or E2 browser implementation was established by this review.

### 2.2 SoulSyncMobile — Offline autonomy and threat boundary

**User-proposed target:** Preserve core offline value, privacy and reproducibility under a constrained maintenance allocation; prevent UCI research infrastructure from bleeding into the mobile runtime.

**Repository evidence inspected:** SOULSYNCMOBILE README blob e9b82c85147cfbaa4f3c942a4968c022dbbd9092.

**Observed README claims/boundaries:** Expo React Native + TypeScript; AsyncStorage adapter described as bootstrap persistence; deterministic compound-risk scoring; fail-closed analysis/storage boundaries; SQLite remains a production gate; G0–G8 status is OPEN / evidence pending. The README explicitly says runtime compatibility must be established by CI/device evidence.

**Assessment:**
- Offline-first should be treated as a runtime contract to prove, not an architecture label.
- AsyncStorage use alone does not prove either adequate encryption or a confirmed privacy vulnerability. Inspect exact data classes, platform threat model, implementation, backup behaviour, device compromise assumptions and actual network paths before making a finding.
- “Zero external transmission unless explicitly triggered” is a candidate privacy rule, but must be reconciled with the app's actual threat-update and user-requested network capabilities. Any transmission needs purpose limitation, clear user control and data minimization.
- UCI should remain a research/intelligence boundary unless a separately approved, minimal interface is justified. Research scripts and pipelines should not become mobile runtime dependencies by convenience.
- Every requested OS permission, background process and network capability should map to a current, user-visible requirement; remove unused permissions.
- A clean-room build after a dormant period is a useful maintenance test, but the 90-day interval is a proposed trigger, not a proven universal threshold.

**Case-study result:** The register surfaces local sovereignty, offline resilience, permission proportionality, dependency decay and architectural scope isolation. It also prevents an unverified claim that the current storage is definitely plaintext or that encryption is already adequate.

**Evidence level:** Repository README inspection only. No fresh build, static manifest audit, dependency audit, network capture, encryption review or physical-device test was executed in this case-study review.

### 2.3 Mall Navigre — Physical uncertainty and operating economics

**User-proposed target:** Preserve the project while examining localization uncertainty, map/hardware maintenance, entry friction, commercial buyer evidence and portfolio cost.

**Repository evidence inspected:** Mall-Navigre README blob c92b25ddea881518839c52521c2853c49be08b47.

**Observed README boundaries:** The project distinguishes PR-head execution evidence from merge-boundary evidence; schematic mall geometry remains unverified; localization/sensors are interfaces rather than physical positioning proof; confidence is explicit; low-confidence localization requires landmark confirmation; temporary infrastructure unavailability is not routable; several advanced features are deferred. The README's detailed audit state is dated 2026-09-14 and must not be represented as a fresh CI audit.

**Assessment:**
- Physical-digital coupling is a genuine missing emphasis: tenant changes, floorplan revisions, renovations, beacon battery decay, sensor drift and changing access routes can invalidate digital state.
- Every time-sensitive physical fact needs provenance, owner, verification timestamp, expiry/staleness policy and a low-friction correction process.
- Navigation should communicate confidence and use zone/landmark guidance when precise localization is unsupported. Do not present schematic geometry or interface-level sensors as physical accuracy.
- Hardware density, accuracy ranges, Android/iOS support percentages and other numeric claims in the supplied case-study narrative remain unverified until independently sourced for the target venue and devices.
- Entry friction should be tested: does a first-time visitor receive useful guidance before being forced through installation or registration?
- B2B willingness to pay and B2C adoption remain hypotheses until buyer/user behaviour and budget ownership are evidenced.
- Preservation mode should not become a reason to invent work; keep the evidence current enough to avoid false claims, then wait for a justified decision.

**Case-study result:** The register surfaces physical state decay, confidence/freshness, operational ownership, entry friction, commercial validation and portfolio restraint.

**Evidence level:** README/document inspection only. No live mall survey, positioning test, operator interview, user adoption test, hardware maintenance trial or current merge-boundary CI recheck was executed here.

## 3. Five refinements to the existing 33 perspectives

These are refinements, not five additional perspectives:

| Refinement | Existing perspective(s) | Operational question added |
|---|---|---|
| Offline grace and data conservation | P16, P18, P22 | Does the core task survive intermittent connectivity, packet loss and limited data without losing user input, duplicating writes or silently corrupting state? |
| Dependency decay and build reproducibility | P20, P25, P29 | Can a fresh clone be built and verified after a period of dormancy using documented, pinned dependencies and without expired external services or undocumented secrets? |
| Permission proportionality and scope isolation | P08, P10, P25 | Does every permission, background process and integration map to a current user-visible capability and an explicit authority boundary? |
| Physical-digital coupling and maintenance burden | P11, P14, P22, P28 | Which real-world changes can silently invalidate digital state, and who verifies, updates, expires or withdraws it? |
| Entry friction and immediate utility | P01, P27, P31 | How many steps stand between a first-time user and useful value, and is each step necessary for safety, consent or the task? |

## 4. Cross-project learning

1. **A feature proposal is not authorization.** A proposed workflow must reconcile with the target repository's current gate.
2. **A storage technology name is not a privacy assessment.** Inspect data sensitivity, implementation, threat model and runtime behaviour.
3. **Offline-first is not proven by local storage.** Test no-network, intermittent-network, retry, duplicate submission, conflict and recovery paths.
4. **Physical truth decays.** Digital representations of people, places, permissions and infrastructure need owners, timestamps and invalidation rules.
5. **Permission is capability-specific.** Minimize OS, API, data and human access; document the purpose and withdrawal path.
6. **Build reproducibility decays.** Pin dependencies, document setup, reduce volatile external dependencies and periodically prove a clean build.
7. **Entry friction must be balanced against protection.** Remove needless barriers, but never remove safeguarding, consent or authorization gates merely to improve conversion.
8. **Portfolio percentages are planning hypotheses.** They do not override livelihood, available capacity, urgent project gates or evidence-based reprioritization.

## 5. Register disposition

**Recommended version:** 0.2 — refined, still proposed.

Do not mark Version 1.0 RATIFIED yet. Three desk reviews demonstrate cross-context usefulness, but they do not establish empirical validation. Before ratification:

1. Test the revised register against at least one real decision in each project.
2. Record actual observations, test artifacts, participant roles (without unnecessary personal data), dates, environment and limitations.
3. Obtain appropriate independent challenge for safeguarding/legal, mobile security/privacy and physical positioning/operations.
4. Record false positives, missed risks, duplicate lenses and review effort.
5. Obtain explicit owner ratification and record the exact commit.

**Current status:** Three project desk reviews documented; five refinements proposed; empirical validation and formal ratification remain open.
