# New Repository Bootstrap — Risk Overlays

**Pack:** CG-PACK-006 · **Version:** 1.0.0  
**Use with:** [Pack overview](README.md) and [baseline checklist](BASELINE-CHECKLIST.md)

Apply an overlay when its trigger is present or reasonably foreseeable. Multiple overlays may apply. These are prompts for local threat modelling and specialist review, not complete control standards.

## 1. Personal, sensitive or regulated data

**Trigger:** The system collects, stores, derives, shares or exposes personal, sensitive or regulated data.

- Map data categories, subjects, collection sources, purposes, recipients, storage locations and transfers.
- Identify the jurisdiction and the responsible decision-maker; obtain qualified privacy/legal review for applicable obligations.
- Minimise collection and avoid retaining data merely because it may be useful later.
- Define access roles, privileged access, audit events, retention, deletion, export and correction processes as applicable.
- Review consent or other lawful processing basis where required; do not treat a checkbox as a complete privacy programme.
- Review backups, logs, analytics, test fixtures and support tooling for unintended copies of personal data.
- Define incident escalation and breach assessment with an accountable owner.
- Use synthetic or appropriately de-identified test data; never place real secrets or unnecessary personal data in public issue trackers.

**Evidence examples:** data-flow map, purpose/retention decision, access tests, deletion exercise, privacy review and incident procedure.

## 2. Children, youth, public profiles or user-generated content

**Trigger:** Children or young people may use the product, be represented in records, receive opportunities or be contacted; or the system exposes user-generated content.

- Identify age groups, guardianship needs, consent and safeguarding decision owners before collecting profiles or enabling contact.
- Minimise public information and never expose a child's private contact details or location by default.
- Define who can view, search, invite, message, moderate, export or delete information; test negative cases.
- Provide reporting, blocking, moderation, escalation and response paths proportionate to risk.
- Verify adults, organisations and opportunity providers before enabling privileged contact or claims of legitimacy.
- Separate discoverability from access, and visibility from permission to contact.
- Define safe image/video handling, consent/withdrawal, takedown and retention procedures.
- Require specialist safeguarding and legal review before any live child-facing workflow or public personal profile.

**Evidence examples:** safeguarding threat model, guardian/consent flow tests, role matrix, reporting exercise, moderation runbook and approved launch gate.

## 3. Money, credits, balances, payments or financial entitlements

**Trigger:** The product stores, transfers, calculates or represents money, credits, points redeemable for value, balances, refunds or entitlements.

- Define the unit and currency explicitly. Use integer minor units or a suitable exact decimal representation; do not rely on binary floating-point for financial amounts.
- Define rounding, tax, fee, currency conversion and negative/zero boundary rules explicitly.
- Maintain an auditable ledger or equivalent source of truth with balanced and explainable postings.
- Make retries and externally triggered events idempotent; define duplicate, timeout, reversal and reconciliation behaviour.
- Test concurrent writes, partial failure, delayed callbacks, duplicate webhooks, refunds, chargebacks and recovery.
- Separate displayed balance from authoritative ledger state; never silently repair mismatches by overwriting evidence.
- Restrict and audit administrative adjustments; require approval for sensitive operations where appropriate.
- Review payment provider obligations and applicable financial/security requirements with qualified specialists.

**Evidence examples:** ledger invariants, exact arithmetic tests, idempotency tests, reconciliation report, adjustment audit and failure/recovery exercise.

## 4. Third-party services, integrations and software supply chain

**Trigger:** The repository uses external APIs, hosted providers, package registries, webhooks, plugins, build actions or third-party code.

- Inventory providers, data shared, privileges granted, subprocessors where relevant, and failure dependencies.
- Give integrations only the scopes and credentials they need; separate development, test and production secrets.
- Validate webhook authenticity, event identity, replay/duplicate handling and request size.
- Treat provider payloads, downloaded files, issue content and pull-request code as untrusted input.
- Pin and review build actions and dependencies; monitor updates and investigate transitive risk proportionately.
- Ensure CI workflows triggered by untrusted contributions cannot expose privileged secrets or write permissions.
- Define timeout, retry, circuit-breaker/fallback and reconciliation behaviour for consequential integrations.
- Record vendor outage, data export, offboarding and credential rotation plans.

**Evidence examples:** provider inventory, permission review, webhook negative tests, lockfiles, CI permission review and integration failure tests.

## 5. Mobile, offline-first, local storage or device-bound workflows

**Trigger:** The product runs on mobile devices, stores data locally, works offline, syncs later or depends on device capabilities.

- Classify local data and use platform-appropriate secure storage for secrets and sensitive data.
- Define lost/stolen-device, shared-device, logout and local-data deletion behaviour.
- Test offline queues, duplicate/retried operations, sync conflicts, clock skew, interrupted writes and recovery after restart.
- Make local and server source-of-truth rules explicit; avoid presenting stale local state as confirmed server state.
- Gate OS permissions by necessity and explain the user-facing reason.
- Test supported operating systems, device sizes, connectivity conditions and upgrade paths.
- Protect signing credentials and release artifacts; define rollback and emergency update procedures.
- State what has been tested on simulators, emulators, mocks and physical devices—these are not interchangeable evidence.

**Evidence examples:** device/data threat review, secure-storage checks, offline/restart tests, device matrix, signed build provenance and recovery results.

## 6. AI systems, agents or automated actions

**Trigger:** A model or agent reads untrusted content, accesses private data, calls tools, writes code, makes decisions or takes actions.

- Treat user text, documents, search results, tool output and retrieved content as untrusted data, not authority or instructions.
- Define allowed tools, scopes, side effects and data boundaries. Default to least privilege.
- Require human approval before high-impact, irreversible, financial, account, communication or production actions.
- Validate model outputs against typed schemas and authoritative rules before execution.
- Test prompt injection, data exfiltration, tool misuse, refusal boundaries, hallucination and adversarial inputs.
- Keep secrets and unnecessary personal data out of prompts, traces, analytics and training pipelines.
- Record model/provider/version changes and evaluate regressions before promoting them.
- Provide user-visible explanations, correction/appeal paths and human fallback where decisions materially affect people.
- Make deterministic code—not model confidence—the authority for security, financial and access-control decisions.

**Evidence examples:** tool permission matrix, prompt-injection tests, approval flow, output validation tests, redaction review and versioned evaluation results.

## 7. Public, safety-critical or high-availability services

**Trigger:** Failure could cause physical harm, substantial financial loss, major service disruption or broad exposure of sensitive information.

- Engage relevant domain specialists before choosing the architecture or release criteria.
- Establish measurable availability, recovery, latency and safety requirements from the actual use case.
- Identify hazards, failure modes, safe states, escalation and manual fallback.
- Test load, resilience, restore, rollback and failure injection at a proportionate level.
- Define monitoring, alert ownership, incident command and communications.
- Ensure a release can be stopped or rolled back without compounding harm.
- Record explicit risk acceptance by an authorized accountable person; unresolved safety-critical uncertainty is a hold condition.

**Evidence examples:** hazard/risk analysis, SLO or service requirements, recovery exercises, incident simulation and approved release review.

## Overlay decision record

For each triggered overlay, record:

| Field | Entry |
|---|---|
| Overlay / trigger | |
| Scope and data/users affected | |
| Decision owner and specialists consulted | |
| Applicable controls and exclusions | |
| Evidence reviewed | |
| Unresolved risks / stop conditions | |
| Decision: proceed / condition / hold | |
| Review trigger/date | |

Do not infer that an overlay is satisfied because a related feature or policy file exists. Verify the behaviour in the receiving project.
