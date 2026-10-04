---
element_type: document
status: active
scope:
  kind: cross-product
created: 2026-10-04
related_backlog:
  - [[80_Decisions and Planning/Knowledge Base Backlog#KB-004]]
  - [[80_Decisions and Planning/Legacy Content Inventory and Migration Map 0.1#MIG-006]]
---

# Relationship Vocabulary Usage Guide 0.1

## Purpose

This guide defines how to use relationships in the PosiBattery vault so links express traceable model claims rather than undifferentiated association. It is a usage guide only. The current relationship schema and property vocabulary remain authoritative until a later approved schema reconciliation.

The guide prioritizes a compact core of high-value relationships for stakeholder, need, use, product, architecture, capability, metric, verification, and evidence traceability. Existing relationship terms not addressed here are preserved; they are neither removed nor redefined by this document.

## Governing rules

- A typed relationship is a directional claim from the current note to a target note.
- Use the active controlled relationship spelling; do not invent synonyms in note metadata.
- Store a relationship in the note that can best state and defend the claim.
- Relationship direction expresses meaning, not visual convenience.
- Use a relationship only when it adds semantic, traceability, structural, evidence, or decision value beyond an ordinary navigation link.
- A relationship can be `asserted`, `inferred`, `supported`, `validated`, or `disputed`; its maturity may differ from the source note’s overall status.
- Link source records when the relationship itself needs evidence. Preserve contradictory relationships and evidence rather than silently choosing one.
- Do not infer product-specific scope merely because an external reference concept appears in a product discussion.

## Relationship record format

Use the interim record structure from [[99_System/10_Docs/Common Element Metadata Standard 0.1]]:

```yaml
relationships:
  - type: <controlled-relationship-type>
    target: [[Canonical Target Note]]
    status: asserted | inferred | supported | validated | disputed
    evidence: []
    applicability: <optional context>
    notes: <optional concise qualifier>
```

Use ordinary Markdown links for navigation, bibliography, or incidental references that do not assert a model relationship.

## Core relationship vocabulary

### Traceability relationships

| Relationship | Direction | Use when | Typical source → target | Inverse/query view |
| --- | --- | --- | --- | --- |
| `hasNeed` | stakeholder to need | A stakeholder holds, experiences, or is responsible for a need | Actor/organization → customer need | Need is held by stakeholder |
| `arisesIn` | need to use/operation | A need is meaningful in a particular operational context | Customer need → use case/workflow/environment | Use context gives rise to need |
| `drives` | need/constraint/decision to requirement, function, design, or plan | The source materially motivates or influences the target | Need → requirement; decision → plan | Target is driven by source |
| `satisfies` | product, capability, function, design, or verification result to requirement/need | The source demonstrably fulfills the target obligation or outcome | Design → requirement; product → need | Target is satisfied by source |
| `realizedBy` | function, requirement, or design intent to implementing design/artifact | A target design or artifact implements the source behavior/intent | Function → design | Design realizes function |
| `verifies` | verification/result to requirement, function, design, or metric | A test, analysis, inspection, result, or review evaluates the target | Verification → requirement | Target is verified by source |
| `measures` | metric/measurement method to property, function, requirement, outcome, or product | A metric evaluates an attribute or outcome | Metric → availability; metric → function | Target is measured by source |
| `supports` | evidence/source/research to claim, element, or relationship target | Evidence provides support but does not prove universal validity | Source record → design claim | Target is supported by source |
| `contradicts` | evidence/source/claim to claim, element, or relationship target | Material evidence conflicts with a claim or interpretation | Source record → product claim | Target is contradicted by source |

### Structural relationships

| Relationship | Direction | Use when | Typical source → target | Avoid using when |
| --- | --- | --- | --- | --- |
| `hasPart` | whole to direct constituent | The target is a physical, logical, or defined architectural part of the source | Battery pack → cell module; charger → power stage | The target is merely associated or used with the source |
| `hasChild` | parent to immediate hierarchical child | The target is a controlled decomposition or taxonomy child | Product family → product variant; function → subfunction | The relationship is cross-cutting rather than hierarchical |
| `hasDesign` | product/system/capability to design | A design record is an intended realization for the source | Product → battery interface design | The design is only discussed as an external reference |
| `hasPort` | system/design/artifact to port/interface point | The target is a defined interaction point belonging to the source | BMS → CAN port | The target is a protocol or a remote system |
| `hasFlow` | system/design/use context to item/functional flow | The target flow is defined in the source context | Charger → charge-control flow | The flow only references the system |
| `hasState` | system/design/function to state | The target is a defined state in the behavior model | Charger → charging state | The target is an event or unrelated condition |
| `appliesTo` | rule/property/requirement/metric/reference to context | The source is applicable to the target product, use, environment, or domain | IP rating requirement → outdoor charger | The source is implemented by or part of the target |
| `optionOf` | variant/option to parent product/design | The source is an optional configuration of the target | Wireless interface option → charger family | The source is a mandatory constituent |
| `subtypeOf` | specialized type to more general type | The source is a semantic subtype of the target | Lithium-ion forklift battery → industrial traction battery | The relationship is part-whole or family-variant |

### Interaction and dependency relationships

| Relationship | Direction | Use when | Typical source → target | Notes |
| --- | --- | --- | --- | --- |
| `dependsOn` | dependent to prerequisite | The source requires the target to exist, operate, be true, or be resolved | Cloud telemetry → cellular connectivity | State the dependency condition in `notes` when material |
| `interfaces` | one interacting element to another | The source has a defined interface with the target | BMS → vehicle controller | Prefer ports/flows for detailed interface modeling |
| `exchanges` | one participant to another | The source exchanges material, energy, data, or control with the target | Charger → battery | Use `hasFlow` plus a flow note when the exchanged item needs its own identity |
| `transmits` | source to transmitted data/energy/item flow | The source sends a defined payload or flow | BMS → battery-state data | Pair with destination/interface details where material |
| `receives` | receiver to received data/energy/item flow | The source accepts a defined payload or flow | Charger → battery temperature | Pair with sender/interface details where material |
| `triggeredBy` | response/event/state to trigger | The source begins or changes because of the target | Charge termination → end criterion | Do not use for loose temporal association |
| `precedes` | earlier step/state to later step/state | The source must occur before the target in a defined process | Authenticate operator → enable vehicle | Use only for meaningful ordered behavior |

### Governance, provenance, and quality relationships

| Relationship | Direction | Use when | Typical source → target | Notes |
| --- | --- | --- | --- | --- |
| `derivedFrom` | derived item to source basis | The source was transformed, calculated, extracted, or synthesized from the target | Research synthesis → source record | Preserve method and limitations in the body |
| `references` | note to cited/referenced item | A non-assertive reference is useful but does not warrant a stronger semantic relationship | Product note → standard | Prefer `supports` or `contradicts` for evidentiary claims |
| `conflictsWith` | claim/requirement/design/decision to conflicting item | Both items cannot be simultaneously accepted without qualification | Requirement A → Requirement B | Link conflict evidence and decision status |
| `supersedes` | newer item to replaced item | The source replaces the target for current use | New decision → old decision | Do not delete the superseded target solely because it is replaced |
| `copyOf` | copy/derivative to source identity | The source is intentionally a copy of target content/record | Local source record → canonical source record | Avoid duplicate canonical elements; resolve identity separately |
| `describes` | explanatory note/source to described element | The source documents or explains the target | Datasheet → product offering | Use for document scope, not proof of every claim |

## Relationship selection rules

### Need, use, and product path

Use the traceability chain below where it adds decision value:

```text
Stakeholder --hasNeed--> Need --arisesIn--> Use / Operation
Need --drives--> Requirement --realizedBy--> Function --realizedBy--> Design
Design --hasDesign or hasPart--> Product Architecture / Product
Metric --measures--> Requirement / Function / Outcome
Verification --verifies--> Requirement / Design / Metric
Source Record --supports or contradicts--> Element or claim
```

The diagram is a guide, not a requirement that every element have every link. For example, an external-reference CAN-FD concept may relate to an interface design through `appliesTo` or `references` without claiming it is implemented in every product.

### Structural versus semantic choice

- Use `hasPart` for constituent structure.
- Use `hasChild` for a controlled hierarchy or decomposition.
- Use `subtypeOf` for “is a kind of.”
- Use `optionOf` for an optional product/design configuration.
- Use `realizedBy` for implementation of a function, requirement, or design intent.
- Use `satisfies` only when fulfillment is actually supported; do not use it for a possible or intended contribution.
- Use `drives` when the relationship is motivational or causal, not structural.

### Evidence and contradiction

- Use `supports` when a source supports a specific element, claim, or relationship.
- Use `contradicts` when a source materially conflicts with a claim, identity, capability, specification, relationship, or conclusion.
- A source can support one claim and contradict another. Do not assign a global truth value to a document.
- Record the contested claim, source scope/revision, and interpretation in the note body or a linked conflict record.
- Do not substitute `references` for `supports` merely to avoid recording uncertainty.

## PosiBattery examples

### Example 1: Battery-state visibility

```yaml
# In [[Know Battery State Before and During the Shift]]
relationships:
  - type: drives
    target: [[Estimate State of Charge]]
    status: supported
    evidence: []
    applicability: industrial traction-battery operation
    notes: The operational need motivates state-of-charge estimation.

# In [[Estimate State of Charge]]
relationships:
  - type: realizedBy
    target: [[Integrated Battery Management System]]
    status: provisional
    evidence: []
    applicability: battery systems with embedded monitoring
    notes: Product-specific applicability has not yet been established.

# In [[Metric - Availability]]
relationships:
  - type: measures
    target: [[Know Battery State Before and During the Shift]]
    status: inferred
    evidence: []
    applicability: fleet operation
    notes: Availability may be affected by battery-state visibility; quantify only with defined operating data.
```

### Example 2: Charging safety

```yaml
# In [[Connect Chargers and Batteries Safely at the Site]]
relationships:
  - type: arisesIn
    target: [[Battery Charging Operation]]
    status: asserted
    evidence: []
    applicability: charging sites

  - type: drives
    target: [[Connect Battery to Charger or Vehicle]]
    status: supported
    evidence: []
    applicability: industrial battery charging

# In [[Connect Battery to Charger or Vehicle]]
relationships:
  - type: realizedBy
    target: [[Breakaway Connector]]
    status: provisional
    evidence: []
    applicability: connector designs where unintended separation protection is required
```

### Example 3: External evidence

```yaml
# In [[Document - EnerSys IMPAQ and NexSys+ Charger Product Guide (AMER 0125)]]
relationships:
  - type: describes
    target: [[EnerSys IMPAQ Charger Family]]
    status: supported
    evidence: []

  - type: supports
    target: [[Metric - Charge Regimes Supported]]
    status: supported
    evidence: []
    applicability: offerings covered by the document revision
    notes: Support is limited to the named guide's scope and revision.
```

## Ambiguities and deferred decisions

The following existing vocabulary requires later schema reconciliation. This guide preserves the terms without choosing a final treatment:

| Topic | Existing terms | Open decision |
| --- | --- | --- |
| Design realization direction | `hasDesign`, `realizedBy`, `satisfies` | Define permitted source/target types and preferred direction for product-to-design traceability |
| Interaction semantics | `interfaces`, `exchanges`, `transmits`, `receives`, `hasFlow` | Define when a direct relationship is sufficient versus when a port/flow note is required |
| Hierarchy semantics | `hasChild`, `hasPart`, `subtypeOf`, `optionOf` | Define cardinality, allowable mixing, and query behavior |
| Evidence semantics | `references`, `describes`, `derivedFrom`, `supports`, `contradicts` | Define claim-level evidence representation and source-record granularity |
| Requirement semantics | `drives`, `satisfies`, `refines`, `tracesTo`, `verifies` | Define strict traceability direction and verification-result treatment |
| Lifecycle semantics | `supersedes`, `copyOf`, `equals` | Define identity, revision, duplicate, and archival policy |

## Relationship quality checks

Before approving a material relationship, check:

1. Is the relationship type more precise than `references` or a generic Markdown link?
2. Is the direction correct from the claim owner to its target?
3. Is the target canonical and unambiguous?
4. Is the scope/applicability clear?
5. Does the relationship require evidence, and is that evidence linked?
6. Is relationship status appropriate—especially for inferred or disputed claims?
7. Does it conflict with another element, source, or relationship? If so, has the conflict been recorded?
8. Would a reviewer understand why this link exists without reading every linked note?

## Adoption sequence

1. Compare this guide with `99_System/03_Schemas/relationships.yaml` and legacy property notes.
2. Identify conflicts, synonyms, missing inverses, and endpoint constraints in a schema-reconciliation plan.
3. Update the controlled schema, templates, and checks only in a separately approved implementation change.
4. Apply the reconciled usage rules first to new elements and then to controlled migration batches.
5. Add relationship-quality checks to integrity reporting after the standard is implemented.

## Change history

| Version | Date | Change |
| --- | --- |
| 0.1 | 2026-10-04 | Initial high-value relationship vocabulary, directionality, examples, ambiguity register, and adoption path |
