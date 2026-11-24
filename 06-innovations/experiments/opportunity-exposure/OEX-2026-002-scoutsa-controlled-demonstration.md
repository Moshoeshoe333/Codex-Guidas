# OEX-2026-002 — ScoutSA Controlled Demonstration Readiness

**Recorded:** 2026-11-24  
**Status:** HOLD · INTERNAL PROTOTYPE / ACCEPTANCE WORK ONLY · NO EXTERNAL EXPOSURE  
**Project:** [Moshoeshoe333/ScoutSA](https://github.com/Moshoeshoe333/ScoutSA)  
**Branch inspected:** `prototype/internal-demo`  
**Related framework:** OFN-001 / CG-042

## 1. Question and hypothesis

**Question:** When the internal ScoutSA synthetic-data prototype is complete, tested at the exact current head, independently reviewed and formally accepted, can a carefully bounded demonstration to appropriate adult football stakeholders create qualified product feedback and legitimate next steps?

**Hypothesis:** A controlled, evidence-led demonstration of a working product will produce more meaningful stakeholder feedback than promoting a concept or documentation package without an accepted prototype.

This experiment is **not authorised to begin external execution**. The preconditions below remain mandatory.

## 2. Current source-backed state — 2026-11-24

The repository contains a static browser prototype and a synthetic review engine on a branch separate from mainline. The prototype README describes a working synthetic-data demonstration, not a production system.

### Verified records and exact boundaries

- Latest inspected branch head at time of this record: `57f5244bf977093ea46c2953bea301e9335ced15`, commit dated 2026-11-24 10:53:50 UTC. A subsequent push started workflow #1008 at head `0ed06bde6317aab847ec3283a1c1afbb0d7b4472`.
- Workflow [#1003](https://github.com/Moshoeshoe333/ScoutSA/actions/runs/45375310485) passed at exact head `ed74b9c019ae2fde07d9d328364d1aa67c5bb741`: 127/127 Node tests, 12/12 configured Playwright/Chromium scripts, 8/8 Discovery groups, 8/8 workspace-hub groups and 25/25 specialist interaction groups. That result is **not** evidence for later commits.
- Workflow [#1007](https://github.com/Moshoeshoe333/ScoutSA/actions/runs/45379103145) failed at exact head `57f5244bf977093ea46c2953bea301e9335ced15`. Node/headless and the standard browser smoke step passed, but the focused Firefox/WebKit import and Blob-export check failed in WebKit at the Player Tournament History 390px mobile viewport assertion. Firefox passed the corresponding check. The observed content included a 640px-wide table inside a 332px table wrapper and a 1px shell overflow.
- Workflow [#1008](https://github.com/Moshoeshoe333/ScoutSA/actions/runs/45379538765) was **in progress** at the time of this record, at head `0ed06bde6317aab847ec3283a1c1afbb0d7b4472`. No success or failure is inferred.
- The 24 November UI-008 reviews explicitly leave UI-008 **OPEN**. The reviewed scope is bounded source inspection and selected browser tests, not complete AST/interprocedural analysis, a full dependency/runtime network audit, penetration test, legal/privacy/safeguarding assessment or release acceptance.
- The UI-008 review still lists independent acceptance and additional proof, including complete runtime/dependency and cross-browser boundaries, as open.
- The project branch contains a launch-channel catalogue captured on 24 November, but that catalogue is explicitly **not a launch plan** and must not be used to submit, pay for placements, contact platform operators, solicit votes or promote ScoutSA before the governing gate is cleared.

Primary records:
- [Prototype README](https://github.com/Moshoeshoe333/ScoutSA/blob/prototype/internal-demo/prototype/README.md)
- [UI-008 dynamic attribute and file-boundary review](https://github.com/Moshoeshoe333/ScoutSA/blob/prototype/internal-demo/prototype/verification/UI-008-DYNAMIC-ATTRIBUTE-AND-FILE-BOUNDARY-REVIEW-2026-11-24.md)
- [UI-008 dynamic DOM and handoff-context review](https://github.com/Moshoeshoe333/ScoutSA/blob/prototype/internal-demo/prototype/verification/UI-008-DYNAMIC-DOM-AND-HANDOFF-CONTEXT-REVIEW-2026-11-24.md)
- [Session ledger — 23 November](https://github.com/Moshoeshoe333/ScoutSA/blob/prototype/internal-demo/prototype/verification/SESSION-LEDGER-2026-11-23.md)

## 3. Non-negotiable sequence

**Build → Test → Audit → Accept → Demonstrate → Pitch.**

No external validation, stakeholder interviews, partnership/funding pitches, public launch submissions or active promotion while the internal prototype is not accepted.

## 4. Precondition gates — all required

| Gate | Required evidence | Status at registration |
|---|---|---|
| Internal workflow completeness | Defined demonstration journey, known limitations and no misleading dead-end or placeholder capability | Prototype exists; formal acceptance pending |
| Exact-head regression | Required Node and browser suite passes at the exact current branch head; record run ID and SHA | **HOLD** — #1007 failed; #1008 was running |
| Cross-browser/mobile | Required Chromium, Firefox and WebKit checks pass at agreed viewports, including the failing 390px Player Tournament History case | **HOLD** |
| UI-008 closure | Remaining sink, attribute, handoff, import/export and build-boundary questions reviewed with evidence; independent acceptance recorded | **OPEN** |
| Baseline-pinned adversarial review | Required AUD sequence completed against its exact authorised baseline, or an explicitly approved replacement contract | **BLOCKED / NOT EVIDENCED** |
| Independent review | Reviewer inspects exact source/test head, findings, limitations and residual risks; no self-certification | **NOT RECORDED** |
| Project-owner acceptance | Explicit acceptance of the named prototype scope, limitations and demo conditions | **NOT RECORDED** |
| Mainline boundary | No inference that prototype acceptance authorises database, RLS, API, authentication, real identity processing, deployment or production | **Must remain intact** |

A green CI run is necessary evidence for its defined tests, not sufficient acceptance of the product.

## 5. Design of the later controlled demonstration — not yet authorised

Only after all preconditions above are closed and accepted:

- Begin with a very small group of adult football stakeholders whose roles are relevant to the demonstrated workflow.
- Use synthetic records only. No real player profiles, minors' data, identity documents, private contact details, real consent records or live safeguarding cases.
- Ask participants to complete defined tasks rather than asking only whether they like the idea.
- Capture task completion, friction, misunderstood states, trust concerns, missing workflow steps and willingness to take a concrete next step.
- Separate product usability, institutional partnership interest and commercial willingness to pay.
- State the prototype's limitations and non-production status before each demonstration.
- Record consent before recording feedback; minimise retained personal information.
- Do not imply verified opportunities, placements, player exposure, legal compliance or production controls that have not been evidenced.

Possible initial sample: 3–5 adult practitioners across organiser / coach / academy roles, subject to explicit owner approval and availability. This is a proposed small discovery sample, not a market-representative sample.

## 6. Measurement plan for the later authorised phase

| Stage | Operational definition | Record |
|---|---|---|
| Relevant exposure | Named adult stakeholder receives an approved demo invitation | Count, source and role |
| Qualified response | Stakeholder confirms relevance and a specific reason to engage | Count and reason |
| Access | Stakeholder accepts a demo session | Count and date |
| Task evidence | Stakeholder attempts defined prototype tasks | Completion, friction, assistance |
| Trust / readiness | Stakeholder understands limits and identifies evidence or changes needed before real use | Observed concerns and conditions |
| Outcome | Concrete next step agreed, such as a second task session or scoped review | Exact commitment and owner |

Do not equate invitation, attendance or praise with product validation. Any commercial conversation is a separate evidence class.

## 7. Stop rules

Stop the external phase immediately if the demo requires real/minor data, the prototype behaves differently from its accepted scope, a critical safeguarding or privacy concern appears, a stakeholder interprets synthetic verification as real-world authority, or a participant is pressured to provide data or endorsement.

## 8. Current decision

**HOLD.** Continue internal prototype completion, exact-head testing, UI-008 and independent review. Do not begin external exposure. The 23 November green run and 24 November #1003 green run are tied to their exact earlier commits; the 24 November #1007 failure and #1008 in-progress state are retained, not concealed.


## 10. 24 November rerun update — exact-head regression corrected

After this record was first written, workflow [#1008](https://github.com/Moshoeshoe333/ScoutSA/actions/runs/45379538765) completed successfully at exact branch head `0ed06bde6317aab847ec3283a1c1afbb0d7b4472`:

- Node headless suite: **128/128 passed**.
- Configured Chromium browser smoke checks: passed, including 8/8 Discovery & Request Review groups and 8/8 Workspace Hub groups.
- Specialist workspace interaction groups: **25/25 passed**.
- Focused Firefox and WebKit import / Blob-export checks: passed, including the 390px Player Tournament History viewport assertion that failed in #1007.

This is exact-head regression evidence for the workflow's declared tests and scope. It does not resolve the broader UI-008 open items, prove every browser/runtime path, close the baseline-pinned AUD sequence, replace independent review, or grant project-owner acceptance.

**Updated status:** the specific WebKit viewport regression observed at #1007 is resolved in the tested #1008 head. The external demonstration/pitch track remains **HOLD** until the remaining UI-008 review and other preconditions in Section 4 are closed and formally accepted.
