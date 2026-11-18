# Security, Privacy and Safeguarding

## Foundational rule
Security and safeguarding are release requirements. A policy or design document is not proof that a control is implemented, effective or monitored.

## Threat-modelling loop
1. Identify assets, users, trust boundaries and data flows.
2. Identify attacker capabilities, incentives and abuse cases.
3. Record threats, impact and likelihood rationale.
4. Choose preventive, detective and recovery controls.
5. Define abuse-case tests and observable evidence.
6. Record residual risk and accountable acceptance.
7. Revisit when architecture, data, users or threats change.

## ScoutSA safeguards
Recorded product invariants:
- Exposure is not opportunity.
- Visibility is not access.
- Discoverability is not trust.
- Verification is not a guarantee.
- Contact is not placement.
- Exposure is not an outcome.

Recorded requirements:
- Players should not pay to be seen.
- Opportunity publication requires an authorised, verifiable source.
- Agent legitimacy must be checked; do not imply FIFA licensing without evidence.
- Under-18 users require guardian and safeguarding controls.
- Do not permit unverified scouts to privately contact minors.
- Do not expose minor contact details publicly.
- Do not claim POPIA or MySAFA integration/compliance without documented proof and appropriate review.
- Synthetic data is appropriate for early technical testing; real player data requires consent, access and safeguarding gates.

A recorded case, SCOUTSA-026, concerned unverified scout contact with a minor and was classified RED in the project risk work. Associated commit and validation-pack prefixes were recorded as 05f59fe5... and 750c812...; verify full hashes and source artifacts before relying on them in an audit.

## Mobile threat-scanning lessons
Treat message content and URLs as untrusted. Parse defensively. Test lookalike domains, redirects, encoding tricks, shortened links, Unicode/punycode, malformed schemes and offline conditions. Explain ALLOW / WARN / DENY decisions. Avoid claiming comprehensive detection; heuristics and feeds have coverage limits. Keep secrets out of ordinary preferences and logs.

## Privacy and minimisation
Collect only what is necessary for a defined purpose. Define retention, access, correction, deletion and disclosure. Separate public, private and restricted fields. Test authorization at the server boundary; hiding a UI element is not access control. Keep legal review distinct from technical implementation.

## Release checklist
Threat model reviewed; authentication and authorization tested server-side; sensitive data minimised and protected; abuse cases tested; logs avoid secrets; recovery and incident handling documented; residual risks visible and explicitly accepted.