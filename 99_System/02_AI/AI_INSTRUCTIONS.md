# MDSE AI Instructions

Before substantial model editing, read:
- `99_System/10_Docs/MDSE Modeling Ruleset 1.18.md`
- `99_System/10_Docs/MDSE Metamodel.md`
- `99_System/10_Docs/Relationship Ownership.md`
- `99_System/10_Docs/Model Evidence and Acceptance Standard.md`

Default AI-authored drafts and proposed changes to `90_Concept/AI_Workspace` unless the user/team explicitly authorizes promotion into maintained model folders.

## Early-build objective

AI should help create **broad initial coverage for review**, not artificial certainty. Optimize for surfacing missing concepts, relationships, interfaces, states, risks, requirements, and questions before team discussion.

## Modeling behavior

When proposing model content:
- classify the concept semantically before selecting a type;
- search/reuse before creating;
- use `instanceOf` for concrete occurrences and `subtypeOf` only for true reusable specialization;
- do not use folders as semantic evidence;
- use explicit relationships from `99_System/03_Schemas/relationships.yaml`;
- author only forward/owner-side relationship fields as semantic truth; generated inverses are derivative but must be reconciled before handoff;
- never invent weak relationship names;
- use `tracesTo` only for unresolved legacy/import ambiguity;
- separate external actor behavior (Use Case/journey) from product-controlled behavior (Function);
- keep flow topology in Functional Flow / Procedure rather than global Function dependency links;
- preserve unknown information as unknown; create a question, hypothesis, or model check instead of silently filling gaps;
- distinguish source evidence, derived engineering evidence, hypothesis, and example/scenario data;
- avoid premature standardization of external interfaces; capture concrete endpoints and flows first;
- apply `control` deliberately: controlled / modifiable / contextual / reference;
- keep model-facing folders under 25 modeled elements using real semantic subdivisions only;
- keep semantic Canvases readable and label known relationship edges explicitly.

## Before creating a new element

1. Search exact/similar titles.
2. Search aliases and definitions.
3. Compare intended relationships.
4. Decide reuse / subtype / instance / part / new concept.
5. Identify evidence or mark as hypothesis.
6. Identify control/boundary.
7. Identify the minimum meaningful relationships.

## Early coverage checklist

For a new model, actively consider whether evidence supports:
- product/system boundary and architecture Things;
- Actors and stakeholder journeys;
- Use Cases / external goals;
- Functions and ownership;
- Interfaces and Item Flows;
- Requirements and basis;
- Designs/decisions;
- contexts and operating states;
- state machines/transitions where behavior is state-dependent;
- failure modes/issues/risks;
- Documents/Artifacts/evidence;
- Verification strategy and gaps.

Do not create elements simply to fill every category. Missing categories may be valid; record questions/gaps for team review.

## Promotion discipline

Preferred progression:

`evidence/research → hypothesis/question → validated need/use case → Requirement → Function/Design → Thing allocation → Verification`

AI-generated breadth is a proposal for team discussion, not authority.
