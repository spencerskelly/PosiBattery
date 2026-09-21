# MDSE Modeling Ruleset 1.18

## Status

Current reusable modeling ruleset for this base vault.

This document is the concise governing index. Detailed subject standards remain authoritative for their specific topics.

## 1. Model meaning before structure

1. Classify the concept semantically before choosing an element type.
2. Search for an existing definition before creating a new element.
3. Prefer, in order: reuse → instance → true specialization → decomposition/part → genuinely new concept.
4. Folder placement is navigation only. It is never proof of semantic type, ownership, scope, inheritance, or relationship.
5. Do not create elements merely because it is convenient to name something.

## 2. Generalization is for irreducible semantic difference

Use `subtypeOf` only when the child adds a reusable, invariant semantic distinction that cannot be represented adequately by:
- a property or parameter;
- a Requirement or Design;
- a configuration choice;
- lifecycle state or effective date;
- version information;
- owner or location;
- ordinary instance/occurrence data.

Use `instanceOf` for concrete occurrences, named examples, deployed/location-specific objects, and configured realizations.

Do not build type layers merely to make a taxonomy look complete.

## 3. Control is independent of type and boundary

Use `control` independently from semantic type, lifecycle, and `boundary`:
- `controlled` — the modeled product/team owns the definition or behavior;
- `modifiable` — not fully owned, but intentionally configured/maintained/annotated by us;
- `contextual` — modeled because it interacts with or constrains us, but not controlled by us;
- `reference` — reusable semantic/reference definition used for classification.

Do not create subtypes merely to represent control differences.

## 4. Relationships are explicit and repository-visible

1. Author only the forward/owner-side semantic relationship.
2. Paired and symmetric inverse fields are generated derivative YAML and must be persisted before the repository is considered relationship-complete.
3. Do not hand-maintain inverse semantics as a second source of truth.
4. Use the defined relationship vocabulary; do not invent vague associations.
5. Breadcrumbs, Bases, model-health checks, AI tooling, and Canvases should all see the same synchronized graph.
6. Semantic Canvases show one labeled edge in the authoritative direction; do not draw a duplicate reverse edge solely for the generated inverse.

## 5. Function means controlled behavior

A product Function must:
- represent behavior controlled by the modeled product;
- be performed by a controlled Thing;
- satisfy a justified Requirement when committed;
- be internal behavior or be grounded in a real interaction.

Do not convert a human step, external product behavior, operational activity, or market capability into our product Function merely because it appears in an end-to-end journey.

For cross-boundary behavior:
- human interaction → Actor / Use Case;
- system interaction → named Interface + Item Flow;
- source import → explicit Document/Artifact or concrete external Interface.

## 6. Stakeholder journeys are broader than Use Cases

A stakeholder journey may cross people, organizations, external products, manual handoffs, and the modeled product.

A journey is evidence used to discover scope. It is not automatically a Use Case, Function, or Requirement.

Promote only the portion that has a clear external actor goal or clear product responsibility.

## 7. External integrations are concrete first

For external interfaces:
1. identify the exact endpoints;
2. verify the interaction;
3. model the exact Interface;
4. model each verified directional Item Flow independently;
5. preserve unknown directions/fields as unknown;
6. generalize only after repeated evidence demonstrates useful common semantics.

A common business label does not prove a common contract.

## 8. Evidence is distinct from assertion

Model evidence classes:
- source evidence;
- derived engineering evidence;
- hypothesis;
- example/scenario data.

Do not silently fill missing information.

Common industry practice, AI inference, naming similarity, precedent, or likely implementation can create a question, hypothesis, candidate, or model check. It does not silently become accepted model truth.

Preferred promotion path:

`source/research → hypothesis → validated need/use case → Requirement → Function/Design → architecture allocation → Verification`

## 9. Requirements and satisfaction

- Requirement `appliesTo` defines scope/applicability.
- Only Function and Design use `satisfies`.
- A contextual element may be within Requirement scope without being treated as behavior we control.
- Committed Requirements require explicit basis and planned/actual verification before Approved status.

## 10. Verification separates intent from execution evidence

- Verification defines reusable verification intent.
- Procedure orders Steps and/or Verifications.
- Setup defines available test capability.
- Plan selects campaign/run content.
- Result records one execution and its evidence.

## 11. Navigation is shallow and semantic

Every model-facing folder contains:
- `00 - Views and Bases.md`
- `00 - Folder Contents.base`
- `00 - Folder Map.canvas`

Immediate folders should contain fewer than 25 modeled elements.

When subdivision is needed:
- use a durable intrinsic distinction;
- prefer element/behavior/evidence/role/flow/requirement kind before impacted feature/domain;
- never create arbitrary overflow buckets;
- keep hierarchy shallow;
- use Bases and focused Canvases rather than inventing false semantic layers.

Semantic Canvases should normally stay around 12 elements and leave enough space for readable relationship labels.

## 12. Function navigation is behavior-first

Function folder classification asks what kind of behavior is performed before what domain is affected.

Primary categories:
- Capability Groups
- Acquire and Input
- Maintain and Transform
- Evaluate and Decide
- Search and Resolve
- Present and Publish
- Coordinate and Transact
- Integrate and Exchange
- Govern and Administer
- Measure and Monitor

Capability groups remain semantic abstractions, not the physical navigation taxonomy.

## 13. Model changes must leave integrity visible

Before handoff or promotion:
- YAML parses;
- IDs are unique;
- filenames and IDs align;
- links resolve;
- inverse relationships are synchronized;
- subtype semantics are defensible;
- product Functions have controlled performers;
- committed Requirements have basis and satisfiers;
- verification gaps are visible;
- hypotheses remain distinguishable from accepted semantics;
- folder navigation remains within the semantic ceiling.

## 14. AI-assisted early modeling

AI may assist with broad initial coverage, but should optimize for useful questions and traceable hypotheses rather than apparent completeness.

AI should:
- inspect available evidence first;
- propose reusable semantic concepts before multiplying instances;
- identify missing actors, contexts, interfaces, risks, states, requirements, and verification needs;
- preserve uncertainty explicitly;
- create model checks/questions where source evidence is incomplete;
- avoid prematurely specializing or generalizing;
- distinguish observations from engineering conclusions;
- leave a reviewable trace from evidence to promoted model content.

Early AI coverage is a starting point for team discussion, not a substitute for team authority.
