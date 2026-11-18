# Pack: Human-Centred Safety Boundaries

**Pack ID:** CG-PACK-005  
**Version:** 1.0.0  
**Maturity:** Review prompts and design principles; not a compliance standard or legal opinion.  
**Upstream source:** doctrines/33-perspective-master-register.md, 03-architecture/invariants-catalogue.md, project-specific safety records.

## Purpose
Prompt teams to examine how data, permissions, authority, interfaces and operational workflows can expose or harm people.

## Review prompts

### Purpose and minimisation
- What exact task requires each data element?
- Can the task be completed with aggregate, team-level, synthetic or less sensitive data?
- Who can see, change, export, retain and delete it?
- What is the retention and deletion basis?

### Authority and consent
- Who may submit, view, correct, publish, contact or approve?
- Is authority specific to the resource, purpose, time and scope?
- How is authority revoked, expired or disputed?
- Does a technical permission merely enable a capability, or is there valid authority to use it?

### Safeguarding and abuse cases
- Who could exploit this workflow?
- Could a person be exposed to unwanted contact, coercion, impersonation or retaliation?
- Are escalation, reporting and response responsibilities explicit?
- Are children or vulnerable people involved? If so, obtain qualified, jurisdiction-specific review before processing or contact.

### Security and containment
- What are the trust boundaries and abuse paths?
- What happens when identity, authority, evidence or network state is unknown?
- Are defaults safe? Are failures contained?
- Can sensitive data leak through logs, exports, analytics, backups or shared devices?

### Human control and correction
- Can affected people challenge inaccurate records?
- Are original assertions preserved when corrected?
- Is the reason, actor, authority and time attributable?
- Does automation make or imply decisions beyond its evidence?

## Non-negotiable practice
- Do not collect sensitive data merely because it may be useful later.
- Do not infer legal compliance from a checklist.
- Do not treat verification as a guarantee of safety or truth.
- Do not treat identity verification as unlimited authority.
- Do not let a numeric score compensate for an unresolved critical safety failure.
- Escalate jurisdiction-specific legal, privacy and safeguarding questions to qualified reviewers.

## Limitations
This pack is a structured prompt set only. It does not establish compliance with POPIA, the Children's Act, GDPR or any other law. Each project must identify its actual jurisdiction, data controller/operator roles, lawful basis, retention obligations, threat model and competent review requirements.
