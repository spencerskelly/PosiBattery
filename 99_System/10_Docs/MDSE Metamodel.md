# MDSE Metamodel — Base Vault

This vault is a practical engineering model, not a SysML clone. Notes are first-class model elements; YAML carries stable identity, controlled type/kind, and explicit semantic relationships. Folder location is for human browsing and automation, not meaning.

## Current element types

| Type | ID | Folder | Typical use |
|---|---|---|---|
| Thing | `THG` | `10_Things` | electrical, circuit, mechanical, software, firmware |
| Interface | `INT` | `20_Interfaces` | electrical & material, data, mechanical, generic physical, environmental |
| Item Flow | `IFLOW` | `21_Item_Flows` | information, energy, material |
| Context | `CTX` | `25_Contexts` | general |
| Function | `FUNC` | `30_Functions` | system, hardware, software, module |
| Functional Flow | `FFLOW` | `31_Functional_Flows` | general |
| State | `STATE` | `35_States` | general |
| State Machine | `SM` | `36_State_Machines` | general |
| Transition | `TRANS` | `37_Transitions` | general |
| Requirement | `REQ` | `40_Requirements` | functional, design, standard, stakeholder |
| Design | `DES` | `41_Designs` | characteristic, decision |
| Use Case | `UC` | `45_Use_Cases` | what, where, why, when |
| Actor | `ACT` | `47_Actors` | general |
| Failure Mode | `FM` | `50_Failure_Modes` | general |
| Issue | `ISS` | `51_Issues` | engineering issue, lifecycle risk |
| Info | `INFO` | `55_Info` | need, objective, concern, decision, assumption, rationale, finding, analysis, trade study, calculation, milestone, lesson learned |
| Step | `STEP` | `60_Verification/01_Steps` | general |
| Verification | `VER` | `60_Verification/02_Verifications` | test, analysis, inspection, demonstration |
| Procedure | `PROC` | `60_Verification/03_Procedures` | test, assembly, configuration, commissioning, calibration, maintenance, repair, decommissioning |
| Setup | `SETUP` | `60_Verification/04_Setups` | general |
| Plan | `PLAN` | `60_Verification/05_Plans` | general |
| Result | `RES` | `60_Verification/06_Results` | general |
| Document | `DOC` | `70_Documents` | standard, specification, report, drawing |
| Artifact | `ART` | `71_Artifacts` | image, document |

## Modeling rules

- Reuse definitions before duplicating them. Use `subtypeOf` for true specialization.
- Author semantic relationships, not vague associations.
- Author only the forward/owner-side relationship as semantic truth. Nodian generates and persists inverse YAML; repository integrity requires inverses to be synchronized before handoff.
- `Function` is product-controlled behavior. `Use Case` is externally controlled behavior or scenario.
- `Requirement.appliesTo` defines scope; only `Function` and `Design` use `satisfies`.
- `Verification.verifies` traces evidence-producing verification to Requirements.
- `Functional Flow` owns contextual ordering/topology. Do not encode flow order as global Function dependencies.
- Use `target`, not the retired `destination` vocabulary.
- `Thing` is the physical/software model element. Discipline is `kind`, not a separate top-level type.
- `tracesTo` exists only for imported/legacy ambiguity. Prefer a defined semantic relationship.

## Identity

Every modeled note receives a stable ID and is named `<ID> - <Name>.md`. IDs and `formerIds` are never reused. Relationships are Obsidian links; IDs are identity/provenance, not relationship pointers.

## Lifecycle

Working status vocabulary: `Draft`, `Review`, `Approved`, `Deprecated`, `Retired`.


## Generalization and specialization

Generalization exists to establish meaning, not merely hierarchy.

Create a subtype only when the child adds an invariant semantic distinction that cannot be adequately represented by a property, Requirement/Design, configuration, state/date, version, owner/location, or ordinary instance data.

Use `instanceOf` for concrete occurrences, named examples, deployed instances, and configured realizations. Folder placement substitutes for neither relationship.

## Control and modeling authority

`control` is independent from semantic type and `boundary`. Use `controlled`, `modifiable`, `contextual`, or `reference`. Control differences do not justify subtypes.

## Journey and interaction boundary

Stakeholder journeys may cross people, external systems, organizations, manual handoffs, and the modeled product. A journey is evidence for scope discovery; it is not automatically a Use Case, Function, or Requirement.

External interfaces are modeled concrete-first. Generalize only after repeated concrete interactions demonstrate stable shared semantics.

## Ruleset authority

See [[MDSE Modeling Ruleset 1.18]] for the concise governing ruleset.
