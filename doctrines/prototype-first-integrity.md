# Prototype-First Integrity and External Engagement

**Status:** Proposed doctrine — not ratified  
**Origin:** ScoutSA prototype and engagement audit, 2026-11-24  
**Applicability:** Cross-project principle; each project must define its own authorized gates  
**Related methods:** [Evidence-first development](../02-methodologies/evidence-first-development.md), [Product and Commercial Validation](../07-product-business/product-validation.md), [Operating Principles](../00-foundation/operating-principles.md)

## 1. Governing principle

**External claims must never outrun demonstrable capability.**

A project should not imply that a system works, that users have validated it, that partners have endorsed it, that demand exists, or that delivery is imminent unless evidence supports the exact claim.

External reach without a working prototype can become a performance of progress: attention, meetings, decks and promises may accumulate while the underlying capability remains unbuilt. If an unbuilt concept is represented as an operational product, that is bluffing by implication, even if no single sentence is an explicit lie.

The remedy is not silence or secrecy. It is accurate representation, proportionate sequencing and evidence-bounded claims.

## 2. Distinguish the engagement types

These activities are not interchangeable:

| Activity | What it can establish | What it cannot establish by itself |
|---|---|---|
| Problem discovery | A person or organisation reports a problem, need or current workaround | That a proposed product solves it |
| Concept discussion | A reaction to an explicitly labelled idea | Usability, product validation or demand |
| Prototype demonstration | The behaviour of the demonstrated artifact in its stated environment | Production readiness, safety, scale or adoption |
| Usability validation | Whether specified users can complete specified tasks in a defined test | Commercial viability or broad product-market fit |
| Partnership discussion | Interest in a possible relationship | Formal endorsement, commitment or product capability |
| Commercial validation | Evidence of willingness to pay, transactions and repeat value | Guaranteed future revenue or scalable growth |

Early discovery is legitimate when it is transparent about what exists and what does not. It becomes misleading when a concept is framed as a working product, exploratory interest is described as validation, or a possible relationship is presented as a partnership.

A project-owner decision may impose a stricter hold than this general distinction. That project-specific hold controls until explicitly changed by the authorized decision-maker.

## 3. Maturity and claim discipline

Use the following descriptions carefully:

1. **Concept:** an idea or hypothesis. No implementation is implied.
2. **Designed:** requirements, flows or architecture are documented. No working behaviour is implied.
3. **Prototype:** an artifact exists for exploration. State what works, what is simulated and what is missing.
4. **Working prototype:** a defined workflow has run in a named environment. Pin the claim to the exact revision and observed result.
5. **Reviewed prototype:** the defined workflow and relevant risks have received the required independent review. State unresolved findings.
6. **Accepted demonstration:** the authorized project owner has explicitly accepted the bounded artifact for demonstration. This is not production approval.
7. **Operational product:** the applicable production, security, privacy, safeguarding, support, reliability, legal and operational gates have been separately satisfied.

Never promote a project from one description to another through presentation quality, documentation volume, meeting count, model confidence or enthusiasm.

## 4. Engagement gate

For projects that require a prototype-first approach, use:

**Build → Test → Audit → Accept → Demonstrate → Pitch.**

- **Build:** deliver the smallest meaningful, observable workflow.
- **Test:** execute the relevant tests against the exact candidate revision; record failures and skipped checks.
- **Audit:** review source, security, safety, privacy, usability, operational limits and claim accuracy in proportion to risk.
- **Accept:** obtain explicit acceptance from the authorized project owner or governing authority. Record scope and exclusions.
- **Demonstrate:** show the accepted artifact without implying capabilities outside its evidence.
- **Pitch:** seek funding, partnerships or commercial commitments using claims that remain within the demonstrated and accepted scope.

No stage is automatically satisfied by completing the previous stage. A project may require additional legal, safeguarding, regulatory or domain-specific gates.

## 5. Minimum evidence before a pitch

Before a pitch that represents a product or working capability, retain:

- exact repository, branch and commit;
- the workflow or user task being demonstrated;
- environment, setup and data classification;
- test command, test inventory, pass/fail/skip counts and run link;
- known defects, exclusions and limitations;
- independent review scope and unresolved findings;
- explicit acceptance record and the authority of the accepter;
- a claim-to-evidence map for every material statement in the pitch.

A historical green run does not verify later commits. A test configuration is not a test result. A passing synthetic test does not prove real-world demand, safety or trust.

## 6. Stop conditions

Stop or reframe the engagement when:

- a concept is being described as implemented;
- a prototype is being described as production-ready;
- exploratory interest is being reported as validated demand;
- a conversation is being presented as partnership, endorsement or commitment without evidence;
- a historical test run is being used to imply current-head verification;
- unresolved safety, privacy, legal or authority questions are being concealed;
- the project owner has explicitly paused outreach or pitching.

The correct response is to disclose the true maturity, narrow the claim, return to the required build/test/review work, or decline the pitch until the gate is met.

## 7. Record the decision, not just the slogan

For each project, record:
- what external activity is permitted at the current stage;
- which claims may be made;
- which claims are prohibited;
- the required prototype and verification evidence;
- the decision owner and acceptance authority;
- the stop condition and review date.

This doctrine is a proposed control, not a universal law or an automatic authorization. It does not replace project governance, domain expertise, independent review or human acceptance.

## 8. Closing rule

**Do not sell the promise as though it were the proof. Build what can be demonstrated, demonstrate only what has been tested, and pitch only what the evidence and authorized acceptance can honestly carry.**
