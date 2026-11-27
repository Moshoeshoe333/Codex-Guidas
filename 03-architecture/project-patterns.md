# Cross-Project Architecture Patterns

These are reusable patterns and cautions, not a mandate to impose one architecture on every product.

## Source of truth and stable identity
Identify the authoritative record for each entity. Use stable identifiers rather than display names or mutable attributes. Define ownership, lifecycle, correction and deletion rules. Preserve provenance for externally supplied or verified attributes.

**ScoutSA:** Player Passport was treated as the authoritative player-profile concept. Tournaments, teams, players, coaches and statistics should relate through stable identifiers, subject to approved design gates.

## Explicit state machines
Model lifecycle states, allowed transitions, actor permissions, required evidence and rejection reasons. Make corrections auditable; do not silently overwrite history. Separate internal state from presentation labels.

## Fail-closed boundaries
When input is missing, malformed, stale or untrusted, define the safe outcome explicitly. Fail-closed must include a clear reason, safe recovery path and audit record.

**SoulSyncMobile:** ALLOW / WARN / DENY was the intended decision vocabulary. This design does not prove every runtime path has been verified.

## Offline-first systems
Define local data ownership, protection, retention, backup limits, duplicate delivery, retries, clock changes, interrupted writes and conflict resolution. Test device loss and corrupted local storage. Ordinary app preferences should not be treated as a secure vault for secrets.

**SoulSyncMobile:** Expo / React Native and AsyncStorage were part of the recorded design.

## Uncertain and time-sensitive signals
For GPS, reputation and threat feeds, store observation time, source, accuracy/confidence, freshness/decay, expiry and model version. Never render an estimate as certainty.

**NAVIGRE:** A location-confidence design recorded a 0.5/block parameter and 24-hour half-life. Treat this as project-specific, not a universal GPS standard.

## Architecture decision records
Record context, problem, options, decision, rationale, evidence, assumptions, consequences, risks, revisit trigger and status (proposed / accepted / superseded).

## Avoiding overengineering
Before adding a service, abstraction, table, framework or integration, identify the demonstrated problem, smallest adequate alternative, operating cost, reversal path and acceptance test. A future possibility alone is insufficient justification.

## External patterns assessed — 2026-11-27

The following are optional refinements derived from the [GCHQ repository pattern review](../10-source-audits/2026-11-27-gchq-repository-pattern-review.md). They do not supersede project-specific architecture or authorize implementation.

### Typed and inspectable processing stages
For a genuine multi-step process, define each stage's input/output contract, validation rules, resource limits, allowed side effects and explicit completed / skipped / unsupported / failed / unknown outcome. Keep intermediate diagnostics inspectable when useful. A stage result is not authorization or proof of a downstream claim.

### Source-to-derived lineage
Where source artefacts are used, keep the original source identity separate from normalized data, enrichment, analyst interpretation and publication. Record transformation/version, timestamps and corrections so results can be reproduced or challenged. Apply purpose limitation, data minimisation, access and retention/deletion requirements; preservation does not mean indefinite storage.

### Lifecycle revisions and review
For governed artefacts, distinguish stable subject identity from revision identity, authorship, review/approval and scan status. Use versioned schemas where records evolve. Unsupported, skipped or failed scanning must remain distinct from a clean completed scan. Do not introduce a registry or review engine unless the product has a real governed lifecycle.

### Scale and asynchronous work
Queues, batchers, distributed storage and serverless compute are design choices for demonstrated volume/cost/latency problems—not defaults. Any asynchronous process should expose job identity, accepted/queued/running/rejected/failed/completed states, matched inputs and retry/recovery behaviour.

### Linked-data exploration
Read-only federation and formal shape validation can help investigate a real cross-source relationship problem. Preserve source boundaries and report validation findings. RDF, SPARQL and SHACL are optional techniques; syntax validity or shape conformance does not establish factual truth.

### Representative data reduction
Sampling/coresets may help exploratory statistics or performance work only after fidelity is measured against full-data and simple-random baselines across appropriate metrics and repeated seeds. Keep rare, high-severity and materially important records available for full inspection. No reduced dataset replaces source evidence or a complete incident corpus.

### Explicit non-adoption
Do not import CyberChef's generic recipe model, Bailo's complete ML lifecycle, Stroom's ingestion platform, Sleeper's cloud-scale architecture, LD-Explorer's RDF stack or Coreax's coreset algorithms wholesale. Each project must demonstrate need, cost/maintenance fit, security and privacy implications, reversal path and acceptance criteria before considering implementation.
