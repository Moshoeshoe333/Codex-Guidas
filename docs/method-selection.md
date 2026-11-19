# Which method should I use?

This is the selection map for Codex-Guidas. Use the smallest method that answers the real question. The methods have different scopes; their scores and maturity states must not be combined.

## Default path: every consequential change

Use **Point → Knowing → Witness → Gate** as the decision discipline:

1. **Point:** state the problem, intended outcome, scope and decision.
2. **Knowing:** separate facts, assumptions, hypotheses, contradictions and unknowns.
3. **Witness:** collect inspectable evidence with source, date, method and limitations.
4. **Gate:** state required evidence, decision owner, stop condition and authorized next step.

Use this for research, defect triage and decisions that could materially affect users, data, money, safety or release scope. Keep it lightweight for routine changes.

## Select the specialist instrument

| Question | Use | Do not use it as |
|---|---|---|
| What happened, has it happened before, and what prevents recurrence? | Defect Intelligence workflow plus lesson search | Proof that a similar symptom has the same root cause |
| How mature is the evidence for an engineering claim? | Foundation evidence ladder E0–E6 | A universal quality score |
| Do code, persistence and UI remain truthful and safe across their boundaries? | Tri-Tier 33 (CG-TT33) | Release authorization or certification |
| Have broader human, strategic, operational, legal, commercial and lifecycle realities been considered? | 33-Perspective Master Register | A mandatory 33-box checklist or weighted score |
| Is a high-stakes question complex enough to need repeated multi-lens scrutiny? | Three-pass 99-tier sieve, selectively | 99 independently specified or validated tests |

## Keep the two evidence ladders separate

- **Foundation E0–E6** describes engineering evidence from documented design through tests, controlled workflows, realistic cases, user evidence and commercial evidence.
- **Tri-Tier L0–L6** is a technical-assessment evidence vocabulary used inside CG-TT33.

The labels answer different questions. Never add, average or transfer a level from one ladder to the other. State the exact claim, version, environment, sample and limitations.

## Maturity and current authority

- Point → Knowing → Witness → Gate is the default reasoning sequence described in the adopted working principles.
- The foundation E0–E6 ladder is the repository's general engineering evidence vocabulary.
- The 33-Perspective Register v0.2 is **proposed, not ratified**. Use selected relevant lenses only; its full taxonomy and validation remain open.
- The three-pass 99-tier sieve is a proportionate extension of the 33-perspective filter, not 99 validated checks.
- Tri-Tier 33 v0.3.0-draft is **proposed, not ratified**. It is a technical instrument for code, persistence, UI and cross-layer seams.
- The Defect Intelligence operating document is proposed for controlled manual use. It does not grant authority to modify an owning project.

## Quick decision rule

If a defect is being fixed, search first and verify the smallest correction. If a decision is consequential, write the Point/Knowing/Witness/Gate contract. Add a specialist method only when its distinct question is relevant. If a method does not change the evidence collected, the risk exposed or the decision made, do not add it.
