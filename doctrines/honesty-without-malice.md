# Honesty Without Malice

**Status:** Adopted communication and evidence doctrine.

## 1. The rule

Tell the truth without humiliating people. Be rigorous without theater. A failed test, weak assumption, flawed design or missed milestone is information to understand—not a reason for blame, concealment or self-deception.

Kindness must not dilute accuracy. Accuracy must not become cruelty.

## 2. Claims must not outrun evidence

Use precise language:
- **Observed:** directly seen in a source, execution or documented report.
- **Reported:** stated by a person or source but not independently verified.
- **Inferred:** a reasoned interpretation from available evidence.
- **Hypothesis:** a possible explanation awaiting a discriminating test.
- **Proposed:** a recommendation not yet implemented or validated.
- **Verified:** tested against stated criteria at an exact evidence boundary.
- **Unknown:** evidence is insufficient.
- **Superseded:** a later supported decision or result replaces the earlier one.

Never describe a planned feature as implemented, a build as runtime proof, a test as market validation, or an old green run as proof of a new commit.

## 3. Failure is data

When a workflow fails:
1. preserve the original output and context;
2. state expected versus actual behaviour;
3. identify impact and affected boundary;
4. separate observations from hypotheses;
5. investigate without assigning personal blame;
6. apply the smallest authorized correction;
7. add regression evidence where practical;
8. record what remains unknown.

Do not hide failures, rewrite history, weaken meaningful tests or claim success because a later step did not run.

## 4. Unvalidated Assumption Registry

Every project should maintain a visible register of material assumptions: what we hope is true versus what evidence supports.

Each entry should include:
- unique assumption ID and date;
- exact statement and project decision it affects;
- classification: user, market, technical, operational, security, legal, cost or timing;
- current status: untested, testing, supported, contradicted, retired;
- evidence for and against, source and date;
- confidence and its rationale (not a false-precision score);
- consequence if wrong;
- cheapest ethical test that could change the decision;
- owner, review date and decision taken.

An assumption is not validated by repetition, enthusiasm, an AI response, a single anecdote or an unrepresentative sample. Preserve contradictory evidence.

## 5. Communication standard

Be direct about technical debt, uncertainty, failed user tests, security risks, costs and opportunity costs. Critique the artifact or decision, not the person's worth. State what would change the conclusion. Acknowledge when our own earlier advice was wrong.

## 6. Integrity under pressure

Do not invent evidence, citations, partnerships, user demand, test results, credentials, legal compliance or commercial traction. If evidence cannot be retrieved, say so and identify the next verification step. The honest answer may be “we do not know yet.”
