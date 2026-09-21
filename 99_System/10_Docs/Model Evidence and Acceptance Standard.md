# Model Evidence and Acceptance Standard

## Governing principle

No durable model element exists only because it is convenient to name. Every accepted element must have a clear semantic role, evidence/basis, and enough relationships to explain why it exists and how it differs from neighboring concepts.

## Evidence classes

1. **Source evidence** — authoritative document/system, direct stakeholder statement, observed behavior, cited source.
2. **Derived engineering evidence** — conclusion logically derived from identified source elements; derivation is recorded.
3. **Hypothesis** — plausible but unverified; keep in Info/analysis until validated.
4. **Example/scenario data** — illustrative data used to exercise the model; never treated as product truth.

## No-assumption rule

Missing information remains missing.

Do not convert common practice, likely architecture, AI inference, naming similarity, folder proximity, or precedent into accepted model truth without evidence.

Inference may create a hypothesis, model check, candidate, or question. It does not silently become an asserted relationship or committed model element.

## Acceptance gates

### Thing
- unique ID and non-duplicative definition;
- correct `control`/boundary classification where relevant;
- `subtypeOf` only for true specialization;
- `instanceOf` for concrete occurrence/realization;
- decomposition and cross-type relationships where they add meaning.

### Use Case
- external actor goal/context stated;
- `subject` and participants identified where applicable;
- enough scenario/preconditions to expose needs;
- `realizedBy` only for Functions that actually implement the scenario.

### Requirement
- one principal normative obligation;
- `appliesTo` identifies scope;
- explicit basis/evidence;
- planned/actual Function or Design satisfier for committed behavior;
- verification strategy before Approved status.

### Function
- controlled product behavior when promoted as product Function;
- distinct reusable definition;
- controlled performer;
- satisfies at least one Requirement when committed.

### Design
- chosen characteristic/decision, not merely a taxonomy label;
- satisfies at least one Requirement when committed;
- applied/owned through defined relationships.

### Verification
- verifies one or more Requirements;
- method and objective acceptance criteria;
- Result/evidence location defined when executed.

## Preferred trace chain

`Actor → Use Case/Need → Requirement → Function/Design → Thing → Verification`

Other bases such as regulations, source specifications, risks, or architecture constraints are valid when explicit.

## Duplicate-prevention gate

Before assigning an ID:
1. search exact/similar names;
2. search aliases and definitions;
3. compare intended relationships;
4. decide reuse / subtype / instance / part / new concept;
5. verify no ID collision.

## Promotion rule

`research/source → hypothesis → validated need/use case → Requirement → Function/Design → architecture allocation → Verification`
