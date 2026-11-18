# Evidence, Verdicts and Tier Passport

**Framework:** CG-TT33 v0.3.0-draft

## 1. Separate the epistemic objects

- **Claim:** proposition someone wants to rely on.
- **Evidence:** artifact or source that may support or challenge the claim.
- **Observation:** what was directly seen/measured under stated conditions.
- **Interpretation:** explanation or inference drawn from observations.
- **Status:** current disposition after applying defined criteria.
- **Authority:** person/process empowered to approve an action. Evidence alone is not authority.

Do not collapse these into a single “verified” label.

## 2. Evidence record

Minimum fields:
- Evidence ID and linked claim/tier/finding IDs.
- Source kind and exact source reference (repository/path/blob SHA, commit, CI run, test report, device/session, interview record or primary source URL).
- Captured/observed date and assessor.
- Build/commit/configuration and environment.
- Method, sample/data shape and reproducibility instructions.
- Direct observation/result, including failures.
- Applicability: what it supports and what it does not support.
- Provenance, independence and transformations.
- Limitations, freshness/expiry and recheck trigger.
- Privacy classification and redaction location.

## 3. Tier passport template

~~~yaml
framework: CG-TT33
framework_version: 0.3.0-draft
project_profile: "<profile-id-and-version>"
tier_id: "C-01"
disposition: "Applicable" # Applicable | Not applicable | Not assessed
not_applicable_reason: null
claim: "<bounded proposition>"
scope:
  component: "<component>"
  data_classes: []
  users: []
  environment: "<environment>"
owner: "<accountable role>"
source:
  repository: "<owner/repo>"
  ref: "<branch-or-tag>"
  commit: "<full SHA>"
  paths: []
evidence_level: "L0" # L0..L6; claim-specific, not a universal score
evidence_ids: []
verdict: "OPEN" # SOLID | SOFT | OPEN | GHOST
findings: []
limitations: []
next_verification: "<smallest useful check>"
review_trigger: "<date, event or change>"
assessed_at: "<ISO-8601>"
assessor: "<role>"
~~~

This is an illustrative record format, not a validated schema. Projects should validate their own schema before automation.

## 4. Verdict decision rules

- **SOLID:** current evidence supports the exact bounded claim under recorded conditions; material counter-evidence is resolved or explicitly bounded.
- **SOFT:** some evidence supports the claim, but meaningful limits remain.
- **OPEN:** not enough applicable evidence, unresolved uncertainty or no inspectable owner/source.
- **GHOST:** a current authoritative claim conflicts with inspected current state because the claimed artifact/control is absent or materially different.

Do not assign SOLID from declarations alone. Do not label a historical claim GHOST if it is clearly marked superseded. A failed test is evidence and must remain linked even after a fix.

## 5. Applicability and proportionality

Every tier has a disposition:
- Applicable: assess to the depth required by risk.
- Not applicable: record why, who accepted the exclusion and when it should be reconsidered.
- Not assessed: scope/review gap, never equivalent to Not applicable or Pass.

A tier may be assessed at different depths. The framework does not require 99 separate manual essays. Generate inventories, SHAs, test links and repeated fields from tooling where reliable; retain human judgement for applicability, interpretation and authority.

## 6. Freshness and change invalidation

Reassess evidence when relevant source files, dependencies, schema, policy, build configuration, runtime environment, threat model, users, jurisdiction or operational conditions change. Evidence is not permanently current because its file remains in the repository.

## 7. Privacy and evidence safety

Do not place secrets, credentials, raw personal data or sensitive safeguarding details in public passports/ledgers. Use synthetic or redacted evidence, restricted storage and stable references where needed. A witness report must not become a new data-exposure channel.
