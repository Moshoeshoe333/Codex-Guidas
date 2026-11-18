# Cross-Project Engineering Invariants Catalogue

**Status:** Adopted working invariants; applicability and implementation must be checked per project.  
**Purpose:** A compact set of boundaries that should survive changes in tools, frameworks and project direction.

An invariant is a rule whose violation should block the relevant decision or trigger review. It is not automatically enforced by code merely because it appears here.

| ID | Invariant | Practical interpretation | Example verification |
|---|---|---|---|
| INV-001 | Evidence ≠ Authority | Evidence informs a decision; only the proper decision owner/gate authorizes action. | Check approval and gate record before implementation. |
| INV-002 | Design ≠ Implementation | A diagram, specification or document is not working software. | Inspect source and deployed/runtime artifact separately. |
| INV-003 | Build ≠ Runtime | Compilation/build success does not prove installation or operational behaviour. | Execute on target runtime/device and record result. |
| INV-004 | Test Pass ≠ Product Validation | Automated tests do not prove usability, demand or commercial value. | Conduct supervised user research and measure outcomes. |
| INV-005 | Provenance ≠ Permission | Knowing an item's origin does not grant rights to access, process, expose or act on it. | Check consent, access policy, purpose and authority. |
| INV-006 | Confidence ≠ Freshness | A credible observation can become stale; freshness is a separate property. | Test age/expiry policy without rewriting source confidence. |
| INV-007 | Authorization ≠ Outcome | Permission to begin an action does not prove the action exists, completed or succeeded. | Verify downstream result independently. |
| INV-008 | Visibility ≠ Access | Being discoverable does not confer entitlement or contact permission. | Test authorization at every protected boundary. |
| INV-009 | Verification ≠ Guarantee | A check supports only the exact claims and scope it tested. | Publish verification scope and exclusions. |
| INV-010 | Fix ≠ Closure | A code change is not complete until relevant acceptance and regression checks pass. | Link fix commit, test command, environment and result. |
| INV-011 | Historical Green ≠ Current Green | CI evidence belongs to its exact commit, branch, environment and scope. | Re-run or prove an explicit evidence-transfer rule. |
| INV-012 | Synthetic ≠ Empirical | Synthetic data tests software behaviour, not real-world fit. | Validate with appropriately recruited real stakeholders. |
| INV-013 | Unknown ≠ Zero / False | Missing or unavailable information must not be silently coerced into a meaningful value. | Test explicit null/unknown states and downstream handling. |
| INV-014 | Discovery ≠ Authority | Automation may surface candidates; it does not acquire policy or production authority by itself. | Require human/authorized deterministic review before promotion. |
| INV-015 | More Complexity ≠ More Progress | Additional architecture is justified only by a demonstrated need or risk. | Name the user outcome, evidence and cost before adding it. |
| INV-016 | Safeguarding ≠ Optional Enhancement | Safety controls are preconditions for relevant live exposure, especially involving minors. | Abuse-case tests, consent/access review and accountable operations. |
| INV-017 | Attention ≠ Value | Activity, commits, documentation and dashboards are not themselves user outcomes. | Measure task completion, repeat use, risk reduction or value. |
| INV-018 | Similarity ≠ Same Cause | Matching symptoms or search results do not establish identical root cause. | Compare reproduction, code path and discriminating evidence. |

## Application

For a consequential design or release, list the applicable invariant IDs, evidence that each is satisfied, exceptions, owner and unresolved risks. Do not force irrelevant invariants onto a trivial change. Critical safety, privacy or security failures cannot be averaged away by passing unrelated checks.

## Change control

New invariants require a concrete failure mode, decision rationale, affected projects, proposed verification and review. Preserve retired invariants and explain why they changed.
