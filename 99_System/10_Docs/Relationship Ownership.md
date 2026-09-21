# Relationship Ownership

Relationships have one **authoritative authored direction** but paired relationships are **persisted on both endpoint notes**.

Create/edit the forward field on the owning note. Nodian generates the inverse field on the related note and the generated inverse is committed as derived YAML. Do not treat the inverse as a second source of truth or hand-edit it independently.

| Forward | Inverse | Meaning |
|---|---|---|
| `subtypeOf` | `supertypeOf` | specialization / inheritance |
| `hasPart` | `partOf` | composition / decomposition |
| `dependsOn` | `dependencyOf` | true prerequisite/reliance, not execution order |
| `derivedFrom` | `derivedBy` | provenance/basis |
| `supersedes` | `supersededBy` | lifecycle replacement |
| `describes` | `describedBy` | explanatory/definition relationship |
| `tracesTo` | `tracesFrom` | legacy/import trace only |
| `instanceOf` | `hasInstance` | concrete occurrence realizes reusable type |
| `performs` | `performedBy` | Thing performs Function |
| `hasDesign` | `designOf` | element has applicable Design |
| `hasStateMachine` | `stateMachineOf` | Thing governed by State Machine |
| `hasContext` | `contextOf` | Thing has modeled Context |
| `hasBehavior` | `behaviorOf` | Function/State has detailed Functional Flow |
| `appliesTo` | `applies` | Requirement/other applicability scope |
| `satisfies` | `satisfiedBy` | Function/Design fulfills Requirement |
| `verifies` | `verifiedBy` | Verification demonstrates Requirement |
| `subject` | `subjectOf` | Use Case focal Thing |
| `hasParticipant` | `participatesIn` | external participant in Use Case |
| `realizedBy` | `realizes` | Use Case implemented by Function |
| `optionOf` | `hasOption` | optional Use Case variant |
| `connects` | `connectedBy` | Interface connects Things |
| `carries` | `flowsOn` | Interface carries Item Flow |
| `source` | `sourceOf` | origin endpoint |
| `target` | `targetOf` | destination endpoint |
| `hasState` | `stateOf` | State Machine owns State |
| `hasTransition` | `transitionOf` | State Machine owns Transition |
| `startState` | `startStateOf` | verification/step start state |
| `endState` | `endStateOf` | verification/step end state |
| `operatingState` | `operatingStateOf` | state context during Verification |
| `exercises` | `exercisedBy` | Verification exercises Transition |
| `addresses` | `addressedBy` | Function/Design/Thing addresses issue/failure |
| `affects` | `affectedBy` | Issue affects model element |
| `causes` | `causedBy` | cause/effect |
| `usesSetup` | `usedByPlan` | Plan uses Setup |
| `resultOf` | `hasResult` | Result records Verification execution |
| `hasEvidence` | `evidenceFor` | Result points to evidence |

## Symmetric relationships

`conflictsWith` may be used for a genuine mutual semantic incompatibility. Author it once on the semantically owning side; the mirrored `conflictsWith` is generated navigation data.

## One-way contextual properties

`sequence`, `initialState`, `finalState`, `trigger`, `plannedDUTs`, `scopeRequirements`, `dut`, `equipmentUsed`, `provides*`, `requires*`.

## Repository synchronization contract

A clean repository state contains generated inverses for every configured pair.

- interactive edits: Nodian auto-sync updates related endpoints;
- Git/AI/bulk edits: run Nodian Full sync;
- MDSE Bootstrap runs a full relationship reconciliation on startup;
- Model Health reports missing inverses.

## Canvas visibility contract

When both endpoints of an authoritative relationship are present on the same semantic Canvas, show one labeled edge using the exact forward relationship field. Do not add a duplicate reverse edge solely for the generated inverse.
