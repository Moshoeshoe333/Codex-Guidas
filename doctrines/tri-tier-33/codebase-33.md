# Mind — Codebase 33 (C-01…C-33)

**Framework:** CG-TT33 v0.3.0-draft  
**Analysis question:** Does the claim about executable code, contracts and build match the inspected live source and observed behaviour?

## Circle A — Existence and structure (C-01…C-11)

| ID | Tier | Assessment question / intent |
|---|---|---|
| C-01 | Entry-point inventory | Are app, service, CLI, worker, deep-link and scheduled entry points enumerated for the assessed scope? |
| C-02 | Module and dependency graph | Are module boundaries, imports, runtime dependencies and layer ownership understood? |
| C-03 | Dead-code and asset exposure | Are unused exports, assets and dependencies identified? Remove only with evidence and change control. |
| C-04 | Duplicate logic | Are duplicated rules, normalization, scoring and parsing paths identified and reconciled? |
| C-05 | Determinism and side effects | Are pure decisions separated from explicitly controlled I/O, time, randomness and external effects? |
| C-06 | Version and contract ownership | Is there a clear source of truth for API, policy, schema and decision-contract versions? |
| C-07 | Type and boundary integrity | Are compile-time types supplemented by runtime validation at untrusted boundaries? |
| C-08 | Constants and policy registry | Are thresholds, weights, patterns and policy identifiers governed rather than scattered? |
| C-09 | Error-path semantics | Does each material error/exception have a defined, observable and safe outcome? |
| C-10 | Naming and vocabulary coherence | Do code symbols and domain concepts avoid ambiguous synonym drift? |
| C-11 | Provenance and source lineage | Can critical decision paths be traced to authoritative source files, versions and owners? |

## Circle B — Correctness and trust (C-12…C-22)

| ID | Tier | Assessment question / intent |
|---|---|---|
| C-12 | Policy-profile conformance | Does the implementation conform to the project's explicitly adopted policy profile? Never assume another project's P1–P7. |
| C-13 | Rule uniqueness and completeness | Is each adopted rule implemented once or deliberately composed, with conflicts and precedence explicit? |
| C-14 | Observed vs derived typing | Are direct observations, user assertions, external assertions and derived inferences distinguishable in types and records? |
| C-15 | Severity and decision separation | Are diagnostic severity, confidence and decision outcome separate unless a documented policy explicitly connects them? |
| C-16 | Threat-boundary fidelity | Does the threat model describe actual implemented behaviour and known non-goals? |
| C-17 | Failure containment | Are malformed, conflicting, unavailable and adversarial inputs handled without unsafe fallback? |
| C-18 | Regression preservation | Are meaningful failures preserved as reproducible witnesses and mapped to corrective/preventive controls? |
| C-19 | Authorization enforcement | Are authorization decisions enforced at the actual operation boundary, not merely hidden in the UI? |
| C-20 | Data and decision minimisation | Does code avoid collecting, deriving, logging or exposing data not required for the stated purpose? |
| C-21 | Configuration and environment safety | Are secrets, feature flags, environment assumptions and unsafe defaults handled explicitly? |
| C-22 | Decision provenance | Can an important decision be reconstructed from its inputs, policy/version, transformation and evidence without overstating determinism? |

## Circle C — Verification and change discipline (C-23…C-33)

| ID | Tier | Assessment question / intent |
|---|---|---|
| C-23 | Rule-to-fixture traceability | Are important policy rules mapped to representative positive, negative and boundary fixtures? |
| C-24 | Property and invariant tests | Are properties, invariants, idempotency and monotonicity tested where mathematically and semantically justified? |
| C-25 | CI workflow truth | Do live workflow definitions and recorded runs support the claimed CI status for the exact commit? |
| C-26 | Witness-harness integrity | Are test/evidence harnesses reproducible, tamper-evident where needed, and clear about dirty trees and generated state? |
| C-27 | Ledger/reference integrity | Do evidence references resolve to exact reachable artifacts, commits, runs or immutable identifiers? |
| C-28 | Hardening-debt visibility | Are known hardening gaps tracked with owner, severity, rationale and closure evidence? |
| C-29 | Dependency exposure | Are decision-path dependencies inventoried, pinned or constrained appropriately, with licensing and vulnerability review? |
| C-30 | Domain-specific pattern coverage | Are jurisdiction-, language- or domain-specific patterns tested only where relevant, with source and expiry? |
| C-31 | Performance/resource envelope | Is performance measured on representative hardware and workloads against explicit user needs? |
| C-32 | Reproducibility | Can the same defined input, source version and environment reproduce the expected decision/evidence within declared tolerances? |
| C-33 | Capability and limitation disclosure | Can the system accurately state what its code does, does not do, and cannot establish? |

## Profile notes

- C-12/C-13 bind to the project's adopted policy profile; SoulSync P1–P7 are not universal.
- C-30 is conditional. South African detection patterns are relevant to SoulSync's intended context, not a mandatory feature of every project.
- C-31 requires an actual representative device/workload only when the claim concerns device/runtime performance; static code inspection cannot establish it.
- C-03 does not justify deleting code solely to improve a score. Preserve necessary compatibility and explain exclusions.

**Passport rule:** every C-tier is Applicable / Not applicable with reason / Not assessed. A declared check is not a verified check.
