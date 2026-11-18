# Cross-Project Knowledge Crosswalk

**As-of:** 2026-11-18  
**Status:** Historical synthesis from prior project discussions and selected recorded identifiers. Not a fresh audit of every repository.

## ScoutSA
**Purpose:** South African grassroots football opportunity network; initial focus on Vaal Triangle / Sedibeng, with a path toward Gauteng and national reach.

**Transferable lessons:** Documentation growth is not implementation progress; prove one observable workflow before expanding architecture; distinguish exposure, visibility, discoverability, trust, verification, contact and placement; use stable identifiers for tournament/team/player/coach relationships; keep under-18 safeguarding and opportunity provenance as release gates; synthetic data does not validate demand.

**Recorded evidence leads:** Canonical status document docs/00-gate-status.md. Gate 1 was recorded closed; Gate 2 conceptual ERD-ready but not closed. RLS/API/UI/schema implementation was deferred pending decision package, MVP boundary freeze and ERD. PostgreSQL 17 CI runtime witness existed but is not a complete product. Case SCOUTSA-026; commit prefix 05f59fe5...; validation pack prefix 750c812.... Pilot design commit recorded as 92b5457ad5d9cef75bb56b5e89db27bd20759c11.

**Next proof:** Tournament organiser vertical slice using synthetic data, correction flows and permission tests; then supervised adult usability sessions.

## SoulSync 3
**Purpose:** Deterministic intelligence/security core with explicit contracts, evidence verification and governed state transitions.

**Transferable lessons:** Contract boundaries and immutability need mutation/adversarial tests; test counts require exact commit, command and environment; do not weaken tests to obtain green CI; separate frozen contract state from runtime coverage and release claims.

**Recorded evidence leads:** Commit ddcd7904... associated with deep immutability and Run #29 reported 64 tests passing; Run #25 also reported 64/64. A 99-contract freeze and a separate 003B Run #68 with 125 tests were discussed; relationship to ratification needs source verification.

**Next proof:** Inspect current branch, freeze/ratification authority, tests and supported runtime matrix before expansion.

## SoulSyncMobile
**Purpose:** Offline SMS/URL threat-scanning mobile application.

**Transferable lessons:** Offline-first creates persistence, retry, clock and recovery concerns; ALLOW/WARN/DENY needs precise semantics; build, install and runtime correctness are separate gates; local persistence is not automatically secure storage.

**Recorded evidence leads:** Expo / React Native / TypeScript design; AsyncStorage local ledger discussed. G-BOOT remained open; no APK was verified, and an EAS Gradle build error was reported.

**Next proof:** Reproducible build, target-device installation, offline/adversarial tests and persistence/privacy review.

## NAVIGRE
**Purpose:** Smart indoor mall navigation and parking locator concepts.

**Transferable lessons:** Location estimates need uncertainty and freshness; scores must expose inputs and thresholds; confidence decay is a model assumption to validate; defer broad platform expansion until a narrow user task is proven.

**Recorded evidence leads:** NAVIGRE 2 parking locator Core 0.1; Gate 2 design recorded GPS confidence parameter 0.5/block and 24-hour half-life; Sieve score 37/99 and Gate 3 frozen.

**Next proof:** Verify current source artifacts, then test confidence and parking discovery against observed real-world conditions.

## UCI
**Purpose:** Cyber threat intelligence research and potential dashboard for global cyber attacks.

**Transferable lessons:** Separate reported events, confirmed incidents, attribution and analysis; preserve source URLs, observation times, confidence and corroboration; do not treat single-source social posts as verified intelligence; research should inform decisions, not automatically trigger infrastructure expansion.

**Next proof:** Define a narrow intelligence question, reliable source set, deduplication rules and analyst workflow before implementation.

## Cross-project rule
Transfer principles, not assumptions. A pattern safe in one project may be inappropriate in another. Every adoption must state context, constraints, evidence and required adaptation.