---
title: EA to MDSE Translator — Primary Reference
documentType: Translator Reference
status: PRIMARY
authority: Primary reference unless explicitly amended or superseded
version: 1.0
date: 2026-09-03
sourcePackageReviewed: GSE
appliesTo: EA XMI -> MDSE Obsidian translation
supersedes: []
amends: []
---

# EA to MDSE Translator — Primary Reference

> **PRIMARY REFERENCE**
>
> This document is the authoritative working reference for the EA → MDSE/Obsidian translator unless a later reference document **explicitly states that it amends or supersedes a specific rule in this document**.
>
> Later package-review documents should add new rules, clarify existing rules, or explicitly amend named rules. A later document does **not** override this reference merely because it is newer. If a later package exposes a conflict, preserve the existing rule until the conflict is reviewed and an explicit amendment is approved.

## 1. Purpose

This document captures the approved decisions made while reviewing the GSE Enterprise Architect XMI export for translation into the MDSE Obsidian vault.

The translator is not intended to reproduce Enterprise Architect or SysML mechanically. Its purpose is to convert EA model content into the simpler MDSE metamodel while preserving engineering meaning, traceability, reusable definitions, useful detail, and enough provenance to support controlled re-import.

The model should remain understandable to engineers who are not modeling specialists.

## 2. Review and Evolution Strategy

The metamodel is **not considered final after this package**.

The agreed process is:

1. Review one representative EA package at a time.
2. Compare the package against the rules in this reference.
3. Stop only for:
   - significant new semantic patterns;
   - repeated patterns that justify a rule;
   - conflicts with an approved MDSE definition;
   - transformations that would cause meaningful information loss.
4. Ignore isolated EA oddities unless they materially affect translation.
5. Produce a new reference document for each package review.
6. New documents should:
   - add new rules; or
   - explicitly amend named rules from earlier references.
7. Do not apply the final translator broadly until representative packages have been reviewed and the metamodel has stabilized.

When a proposed mapping conflicts with an existing MDSE definition, show:
- the established MDSE rule/example;
- the new EA example;
- why they conflict;
- the recommended resolution.

Every new mapping rule requires explicit approval before it becomes authoritative.

---

# 3. Import Architecture

## 3.1 Controlled synchronization

Repeat EA imports use **controlled synchronization**.

The translator should:
- recognize previously imported EA elements;
- apply safe source-controlled changes automatically;
- preserve Obsidian-controlled content;
- flag shared-field conflicts rather than overwriting them.

## 3.2 Split authority

### EA-owned
EA owns imported source-model semantics and approved mapped source fields.

### Obsidian-owned
Obsidian owns:
- MDSE IDs;
- vault placement;
- AI/manual annotations;
- derived/query content;
- enriched local content;
- local documentation added after import.

### Shared
Fields that may reasonably be edited in both systems should produce a conflict when both sides change.

## 3.3 EA provenance on every imported note

Every imported note should carry:

```yaml
eaGUID: EAID_...
eaPackage: GSE
```

For consolidated MDSE elements, `eaGUID` may contain multiple source GUIDs if multiple EA elements were merged into one MDSE concept.

The old EA stereotype/UML metaclass should **not** normally be written into engineering-note frontmatter. Raw source type information may remain in translator diagnostics.

## 3.4 Obsidian structure controls placement

EA package hierarchy does not determine vault folder placement.

- MDSE/Obsidian folder and semantic rules determine note placement.
- `eaPackage` is provenance only.
- EA ownership can be useful evidence, but it is not automatically a semantic relationship.

## 3.5 Cross-package references

Use a **pending relationship registry** for relationships whose remote endpoint has not yet been imported.

Store:
- source EA GUID;
- target EA GUID;
- source/target names where available;
- source/target EA type where available;
- connector type;
- direction;
- package information;
- intended semantic mapping if already known.

Do not create placeholder engineering notes merely to satisfy cross-package relationships.

Resolve the relationship normally after both endpoints exist in MDSE.

## 3.6 Required translator outputs

Each import should produce or update:

1. **Identity Registry**
   - EA GUID ↔ MDSE ID ↔ filepath.

2. **Transformation Log**
   - merges;
   - collapses;
   - suppressed elements;
   - semantic remaps;
   - renames/corrections;
   - relationship substitutions;
   - consolidated interfaces/flows;
   - source GUIDs.

3. **Model-Check Report**
   - naming inconsistencies;
   - ambiguous types;
   - suspicious relationships;
   - missing NoteLink content;
   - unresolved semantic cases.

4. **Pending Relationship Registry**
   - unresolved cross-package endpoints.

## 3.7 Data-preservation principle

If translation removes, consolidates, or simplifies an EA element, preserve useful engineering detail in the body of the affected MDSE Thing, Interface, State, Function, Functional Flow, Requirement, etc., wherever practical.

Do not discard detail merely because the MDSE metamodel is simpler.

---

# 4. General Translation Principles

## 4.1 Most specific semantic meaning wins

Ignore generic UML implementation types when a more meaningful engineering interpretation exists.

Examples:
- EA `Hardware Component` should not become MDSE `Class`.
- EA `functionalRequirement` should not become generic UML Class.
- EA State-shaped elements may become State, Function, or Design depending on meaning.

## 4.2 Semantic mapping over mechanical mapping

EA types such as:
- `Port`;
- `State`;
- `InformationItem`;
- `block`;
- `InstanceSpecification`;

are not always type-bearing.

Names, relationships, owner context, classifier, and actual engineering meaning determine the MDSE result.

## 4.3 Do not invent weak relationships

Avoid generic `associatedWith`, `trace`, `allocate`, etc. when a clearer MDSE relationship exists.

If a connector has no useful semantic mapping, ignore it or flag it rather than preserving a vague relationship.

## 4.4 Store relationships once

Store each semantic relationship once in the natural authoritative direction.

Derive inverses for navigation/querying unless a plugin or engineering use case explicitly requires both directions.

Do not fill parent/system notes with large inverse arrays such as:
- `hasUseCase`;
- `hasRequirement`;
- `hasPart`;
- all incoming Function Usages.

Large inverse collections should normally be generated views/queries.

---

# 5. Approved Element-Type Translation Rules

## 5.1 Electrical / Mechanical / Software / Firmware / Document / Artifact

### EA `Hardware Component`
**Approved mapping:**

`Hardware Component` → `Electrical`

The generic UML `Class` is ignored.

### EA `Physical Component`
Semantic mapping, not one-to-one.

- clear physical hardware → `Mechanical`;
- manuals/specifications/documentation → `Document`;
- physical product labels/markings → `Artifact`;
- ambiguous cases → review.

Examples:
- enclosure panel → Mechanical;
- manual → Document;
- product label → Artifact.

### EA `Physical System Variant`
**Approved pragmatic mapping:**

`Physical System Variant` → `Electrical`

This is acknowledged as an imperfect fit under the current MDSE type vocabulary.

`architectureRole` such as Product/System is determined separately.

### EA `Software Component`
Semantic split:

- software clearly tied to an embedded physical product/platform → `Firmware`;
- application/cloud/tool/service software → `Software`;
- ambiguous → review.

Examples:
- `SW GSE` → Firmware;
- `SW - GSE Gen2` → Firmware;
- `SW - GSE Gen3` → Firmware.

### EA `Module`
Does not define discipline/type.

Map:
```yaml
architectureRole: Module
```

Determine `type` separately from semantics.

### Physical product labels
Physical labels/markings → `Artifact`.

Manuals/specifications/instructions → `Document`.

## 5.2 Requirements

### EA `functionalRequirement`
→ `Functional Requirement`

### EA `designConstraint`
→ `Design Constraint`

### EA embedded/internal Requirement
Promote to a standalone first-class MDSE Requirement.

Preserve legacy ID and reconstruct semantic relationship to the owner.

## 5.3 Interfaces and ports

### EA `ProxyPort`
→ `Interface`

Interface is defined broadly as a modeled boundary through which elements physically, electrically, logically, thermally, mechanically, or otherwise interact or must remain compatible.

Mechanical mating geometry can therefore be an Interface when it defines compatibility.

### EA `FullPort`
→ `Electrical`

Structural role is decided separately.

### EA plain `Port`
No blanket mapping.

Approved semantic rules:
- physical connector names using `P#` / `J#` → `Electrical`;
- `Seal` → `Mechanical`;
- `KeepOut Zone` / A-surface compatibility boundary → `Interface`;
- signal/data/power ports may be consolidated rather than becoming standalone notes;
- ambiguous → review.

Do not require every chip pin or low-level signal endpoint to become a standalone note.

## 5.4 Functions and activities

### EA `Activity`
Map by performer/context:

- behavior performed by product/system/component/software → `Function`;
- human/organizational behavior → `Use Case`;
- test/procedure behavior → appropriate Test/Step concept;
- ambiguous → review.

Examples:
- `Monitor Faults` → Function;
- `Develop Charger SW update` → Use Case;
- `Manually update charger software` → Use Case.

### EA State-shaped elements used as actions
If an EA State element actually describes behavior, map to `Function`.

Approved examples:
- `Calculate Charge Data` → Function;
- `Verify Battery` → Function;
- `Prepare PowerStage State` → Function.

### EA State-shaped elements used as design
If EA labels an element State but it actually describes a design characteristic/solution, map to `Design`.

Examples:
- `Mounted to Wall`;
- `Physical Dimensions`;
- `RoHS Compliant`;
- `Mean Time Between Failures MTBF`;
- `Field Wiring`;
- `Aesthetic Appearance`;
- `LED Integration`;
- `Configuration Data Storage`.

## 5.5 Issue

EA `Issue` → MDSE `Issue`.

Do not promote to `Risk` unless explicit risk semantics justify it.

InformationItems/actions that clearly describe failures, faults, defects, or undesirable conditions also become `Issue`.

## 5.6 EA `Change`

Do not create a general MDSE Change type from the GSE package.

Approved specific mapping:
- `OTA capability on all updated systems` → `Design Constraint`.

## 5.7 Generic SysML `block`

`block` is non-type-bearing.

Classify semantically.

Approved/provisional examples:
- charger blocks (`SVS 100 UL`, `MVS 330 CE`, `MVS 400`, `MVS_800`) → `Electrical`, unless canonical identity review proves they duplicate an existing MDSE element;
- `ACT Protocol` → provisionally `Firmware`, subject to later review if it is actually a Design/specification.

## 5.8 EA `InstanceSpecification`

Three distinct meanings:

### Real-world occurrence
A genuine serialized/installed occurrence:
```text
Parking Lot Charger SN12345 instanceOf PVS 330
```

Use `instanceOf`.

### Named product-design occurrence
Examples such as:
- K1;
- K2;
- C1;
- P/J connector positions;
- fans;
- transformers.

Map to a normal MDSE Thing:
- appropriate discipline;
- `subtypeOf` classifier;
- `partOf` owning product/design element where applicable.

Do **not** use `instanceOf`.

Example:
```text
Main Contactor - Server K1
  subtypeOf Circuit - Contactor
  partOf DVS 330 IP55
```

### Firmware version incorrectly modeled as InstanceSpecification
Firmware-specific correction:

```text
SW 1.024 subtypeOf SW GSE
SW 1.024 partOf PCBA - PS Control Gen3
```

Do not use `instanceOf`.

Do not generalize this exception beyond firmware without review.

## 5.9 EA `InformationItem`

`InformationItem` is non-type-bearing.

Approved handling:

### One-to-one descriptive shadow of one element
Collapse into the described element’s body.

Do not create a duplicate Info note.

Preserve source GUID and content in the transformation log/body.

### Independent descriptive knowledge
→ `Info`

Stored relationship:
```text
Info describes Thing
```

Derived inverse:
```text
Thing describedBy Info
```

### Problem/failure content
→ `Issue`

### One-to-one behavioral annotation
Merge into the body of the specific:
- State;
- Transition;
- Function;
- Design;
- Functional Flow;

when it has no independent reuse value.

### Ambiguous design/behavior logic
Preserve in the body of the most relevant existing element for now; refine classification later.

## 5.10 EA `Physical Context`

Approved mapping:

`Physical Context` → `Use Case`

with:
```yaml
category: Where
```

Use `subject` for the focal element.

EA Context Aggregations become local participant membership, not `partOf`.

Context generalization becomes normal:
- `subtypeOf`;
- `supertypeOf`.

Participant membership remains local to the Where Use Case and should not create reciprocal relationship noise on participant Things.

This supports Discover-phase questions such as:
- where is the element used/located;
- what surrounds it;
- what interfaces exist;
- what scenarios must be considered.

## 5.11 EA Use Cases

EA Use Case ownership/nesting → `parent / child`.

Keep distinct:
- `subtypeOf / supertypeOf` = specialization;
- `parent / child` = decomposition;
- `optionOf / hasOption` = optional/conditional behavior.

Actor mapping is deferred until a package with representative Actor elements is reviewed.

## 5.12 EA StateMachine

Semantic split:

### True state model
→ first-class `State Machine`.

### Single-state/detail/behavior container
Collapse into:
- actual `State`;
- `Functional Flow`.

Connect:
```text
State hasBehavior Functional Flow
```

Derived inverse:
```text
Functional Flow behaviorOf State
```

Preserve collapsed EA StateMachine GUIDs in the transformation log.

Do not use generated EA names such as `EA_StateMachine7` as MDSE titles.

---

# 6. Approved Relationship Translation Rules

## 6.1 Generalization

EA source is the specific element; destination is the general element.

Map:

```text
source subtypeOf destination
destination supertypeOf source
```

Store authoritative direction as appropriate; inverse may be derived.

Generalizations involving unresolved/deferred elements remain pending.

## 6.2 Aggregation

Combine EA composite and shared Aggregation.

Normal structural mapping:

```text
EA source partOf EA destination
```

Derived inverse:
```text
destination hasPart source
```

Do not preserve composite/shared as separate MDSE relationship types.

Preserve multiplicity/quantity separately when relevant.

### Exception: Physical Context / Where Use Case
Aggregation into a Physical Context does **not** mean `partOf`.

It becomes local participant membership in the Where Use Case.

## 6.3 Generic EA Association

No default `Association` mapping.

Map by semantic endpoint pattern.

### Use Case ↔ Thing
Stored:
```text
Use Case subject Thing
```

Derived inverse:
```text
Thing subjectOf Use Case
```

Do not use `appliesTo` for this pattern.

### Issue ↔ Thing
```text
Issue affects Thing
```

### Thing ↔ Thing with no useful qualifier
Ignore by default.

### Information/documentation element ↔ Thing
Use:
- `describes`;
- `defines`;
- `refines`;

only when the semantic meaning is clear.

If unclear, review.

### Diagram Text with no recoverable semantic content
Ignore.

### Instance relationship
Use classifier semantics, not generic Association.

## 6.4 `instanceOf`

Reserved for actual real-world occurrences.

Do not use `instanceOf` for:
- product-design positions;
- firmware versions;
- reusable variants.

## 6.5 EA `allocate`

No global mapping.

Approved patterns:

### Function → Thing
Translate to:
```text
Thing performs Function
```

### Design-description element → Thing
Translate to:
```text
Design designOf Thing
```

Derived inverse:
```text
Thing hasDesign Design
```

### Issue → Function / Use Case
```text
Issue affects Function/Use Case
```

### Information Item → Activity/behavior
Use:
```text
Information Item defines Function/Use Case
```

only when `defines` reads logically.

Otherwise flag for review.

### State → Thing
For true States, treat allocation as evidence of State Machine ownership/context rather than inventing a direct State→Thing relationship.

### Firmware version → PCBA
For approved firmware-version exception:
```text
Firmware version partOf PCBA
```

## 6.6 `satisfy`

Preserve the most specific valid satisfaction trace.

Approved:
```text
Function satisfies Functional Requirement
State satisfies Functional Requirement
State Machine satisfies Functional Requirement
Design satisfies Design Constraint
```

Do not automatically roll State-level satisfaction up to the State Machine.

If an EA State-shaped element is semantically a Function, it satisfies as a Function.

## 6.7 EA `Realisation`

For plain EA Thing/Document/Firmware → Requirement Realisation, use the conservative interim mapping:

```text
Requirement appliesTo Thing
```

Do not expand `satisfies` to Things from this package alone.

Revisit if later packages justify stronger satisfaction semantics.

## 6.8 `refine`

Approved:
```text
Use Case refines Requirement
```

This may target:
- Functional Requirement;
- Design Constraint;

when the semantics fit.

Example correction:
- `Single Portal Access` should be interpreted as `Single Portal Interface`, remaining a Design Constraint.

## 6.9 `trace`

Do not preserve generic `trace` when a clearer semantic relationship exists.

### Information Item → Thing
Default:
```text
Info describes Thing
```

Use `defines` or `refines` only when that meaning is clearly stronger/more accurate.

### Issue → Use Case
```text
Issue affects Use Case
```

Example:
```text
Spare Parts Cost affects Acquire Spare Parts
```

### Issue → Design Constraint / Requirement
```text
Issue affects Requirement
```

Example:
```text
Portal 2.0 affects Single Portal Interface
```

### Thing → Requirement
Reverse to:
```text
Requirement appliesTo Thing
```

### Thing → unnamed EA Text
Ignore unless recoverable semantic content exists.

## 6.10 Plain EA `Dependency`

Behavior → behavior:

```text
dependent behavior dependsOn prerequisite behavior
```

Use only when it reads logically as a prerequisite/dependency.

Do not confuse with Functional Flow execution order.

Approved examples include:
- `Monitor Connection dependsOn Communicate Vehicle Connection`;
- OTA-related human Use Cases depend on the OTA Design Constraint.

## 6.11 EA `Usage`

Use Case → Function Usage connector:

```text
Use Case dependsOn Function
```

when dependency semantics fit.

Avoid introducing a separate `uses` relationship from this pattern alone.

## 6.12 EA `extend`

Use:
```text
optional Use Case optionOf base Use Case
```

Derived inverse:
```text
base Use Case hasOption optional Use Case
```

Preserve extension conditions/details in the option Use Case body or later Use Case-flow context.

## 6.13 EA `Nesting`

Deferred.

Do not establish a mapping from the GSE package.

## 6.14 EA `NoteLink`

Do not create an MDSE NoteLink relationship.

When note content is available:
- preserve it in the linked/owning element body;
- promote semantically only when it clearly deserves to become Issue, Use Case, Requirement/Constraint, or Info.

When note content is missing from XMI:
- create a model-check warning;
- do not create an empty note.

Preserve Note GUID provenance in the transformation log.

---

# 7. Interface and Item Flow Model

## 7.1 Reference interface translation pattern

Approved reference pattern:

> **Two endpoint Things, one Interface per meaningful engineering boundary, and multiple Item Flows carried by that Interface.**

When physical connectors such as J#/P# are real hardware, they remain Electrical Things.

Example:

```text
PCBA A
  └─ J4 ── Interface ── P4
                       └─ Circuit B
```

Containment supports rolled-up visualization:

```text
PCBA A ── Interface ── Circuit B
```

## 7.2 Multiple flows on one Interface

An Interface may carry zero or more individually named and directed Item Flows.

Do not create a separate Interface for every low-level signal.

Example one boundary may carry:
- GND;
- 3.3VDC;
- 5VDC;
- UART0;
- UART1;
- UART4;
- SPI1.

## 7.3 Preserve port → flow → port detail

Where EA intentionally modeled endpoint-level detail, preserve a generated table in the Interface/Thing body.

Example:

| Source part | Source port | Flow | Destination port | Destination part |
|---|---|---|---|---|
| PCBA Control | J4 SPI1 | SPI1 | P4 SPI | RS232 Circuit |

This preserves useful local naming without creating notes for every signal endpoint.

Generic/reusable Interfaces can be normalized later after more packages are reviewed.

## 7.4 EA BindingConnector

BindingConnector is not a normal `connectsTo`.

Approved behavior:

- same semantic name on bound ports/interfaces → reuse the same MDSE Interface at multiple structural levels;
- different names → preserve through an Interface and create a naming/model-check warning;
- do not silently normalize names;
- if endpoints are actually different engineering elements, do not collapse/connect them—flag for review.

Suggested model check:
```text
BINDING-NAME-MISMATCH
```

## 7.5 EA InformationFlow

An EA InformationFlow becomes an Item Flow carried by an MDSE Interface.

Preserve:
- source → destination direction;
- individual flow identity;
- conveyed classification/type where meaningful.

Multiple EA InformationFlows across the same boundary consolidate under the same Interface.

Example:
- `UART0 TAG`;
- `UART1`;
- `UART4`;

may all share UART classification while remaining distinct flows.

Unnamed or semantically empty flows should trigger review rather than generate junk.

## 7.6 Plain EA Connector

Plain EA Connector represents actual interaction, unlike BindingConnector.

Map to:
- create/reuse Interface between endpoint Things;
- preserve port-to-port detail in Interface body;
- associate InformationFlows as Item Flows;
- if only a connection exists and no flow is known, still create the Interface.

Different local endpoint names on a plain Connector are not automatically naming errors.

---

# 8. Functional Flow Model

This is a major addition identified during GSE review.

## 8.1 First-class elements

Approved first-class element:

`Functional Flow`

Approved contextual concept:

`Function Usage`

## 8.2 Definition vs usage

`Function` = reusable behavior definition.

`Function Usage` = one contextual occurrence of a reusable Function inside exactly one Functional Flow.

A Function Usage:
- references a Function;
- is not a subtype of the Function;
- is not an `instanceOf` the Function;
- does not inherit sequencing from the Function;
- is scoped to one Functional Flow.

This prevents process relationships from leaking into unrelated Function visualizations.

## 8.3 Functional Flow owns topology

Sequence, branches, guards, loops, local control structure, and contextual flow edges belong to the Functional Flow—not to reusable Functions.

Do not add global `next`, `precedes`, or similar sequencing relationships to base Function notes.

## 8.4 Function visualization rule

Normal Function views should show definition relationships such as:
- satisfies;
- realizes;
- parent/child;
- dependency;
- general performer if universal.

They should **not automatically show every Function Usage**.

“Where is this Function used?” should be an explicit query/view.

## 8.5 Flow-control nodes

The following are local Functional Flow constructs by default, not MDSE notes:

- Initial;
- Final;
- Decision;
- Merge;
- Fork;
- Join;
- Timer/Event control nodes.

Promote only if later packages show a need for independent traceability, requirements, verification, or reuse.

## 8.6 Function Usage performer

A Function Usage may specify/override the actual performer for that product/flow context.

A reusable Function may have a default/general performer only when that performer is universally true.

## 8.7 State behavior

Approved relationship:

```text
State hasBehavior Functional Flow
```

Derived inverse:

```text
Functional Flow behaviorOf State
```

## 8.8 Entry / do / exit

Function Usage may contain controlled local metadata:

```yaml
behaviorRole: entry
```

Allowed working values:
- `entry`;
- `do`;
- `exit`.

Do not create separate global relationship types for these roles.

## 8.9 Local actions / Function Usage

When an EA local Action clearly implements a reusable Function, translate it as a Function Usage and preserve local target/context.

Example:

```text
Close K1
```

→ Function Usage of reusable:

```text
Close Contactor
```

with `K1` retained as local context.

Local low-level actions with no reusable engineering value may remain flow-local actions.

## 8.10 Mixed-content activity diagrams

Approved semantic interpretation:

- executable product behavior → Function Usage;
- undesirable/problem condition → Issue;
- explicit human-performed action → Use Case;
- neutral descriptive knowledge → Info;
- ambiguous → review.

Examples:
- `No fault showing when relay forced closed` → Issue;
- `Relay can easily be flipped and shut down` → Issue;
- human inspection/check action → Use Case.

## 8.11 EA ControlFlow

EA ControlFlow becomes a local Functional Flow edge.

Activities become Function Usages in that flow.

Guards remain local edge metadata.

No ControlFlow relationship is written onto reusable Function notes.

## 8.12 EA ObjectFlow

Approved handling:
- reuse an existing Item Flow when the behavioral transfer corresponds to a known reusable information/energy/material flow;
- keep context-only behavioral transfers local to the Functional Flow edge;
- if the same flow exists on a physical Interface, reference the same reusable Item Flow;
- ambiguous ObjectFlow → flag.

## 8.13 Same Item Flow in architecture and behavior

The same reusable Item Flow may be referenced by:
- an Interface in architecture;
- a local Functional Flow edge in behavior.

Do not propagate Functional Flow usage relationships back onto the Item Flow note.

Do not introduce `Item Flow Usage` yet.

## 8.14 Function Usage inputs/outputs

Do **not** add default `inputs` / `outputs` arrays to Function Usage.

Inputs/outputs are derived from incoming/outgoing Item Flow edges owned by the Functional Flow.

Item Flow alone does not necessarily imply execution order.

## 8.15 EA Sequence diagrams

EA `Sequence` connectors do not become standalone MDSE relationships.

Translate sequence-diagram content into local Functional Flow content based on message semantics:

- behavior/call message → Function Usage;
- information/data message → Item Flow;
- self-call → Function Usage by that participant;
- delay such as `Wait 1 second` → local Timer/Delay construct;
- ordering stays local to the Functional Flow.

Preserve participant/lifeline context.

## 8.16 CallOperationAction and repeated behavior

When EA invokes existing behavior:
- reuse the existing Function;
- create a Function Usage for that flow/state context.

If the invoked name does not map cleanly to an existing semantic element, review.

---

# 9. State and Transition Model

## 9.1 True states

Elements that represent persistent operating/mode/configuration conditions remain `State`.

## 9.2 State-shaped Function / Design correction

Use the semantic rules in Section 5:
- action-like State → Function;
- design-description State → Design.

## 9.3 StateFlow

Working rule:
- true State ↔ State flow → MDSE Transition;
- function-like StateFlow content belongs in Functional Flow behavior, not as a Transition between reusable Functions.

## 9.4 Transition trigger

**DEFERRED**

Do not change the current trigger metamodel based on the GSE package alone.

For now:
- preserve source State;
- preserve target State;
- preserve trigger/guard/effect detail in Transition body/import metadata;
- do not normalize Interface-based vs event-based trigger semantics yet.

Revisit after additional package reviews.

---

# 10. Requirement Translation Rules

## 10.1 Requirement title and statement

Use a concise EA requirement name as MDSE title when appropriate.

Place the full normative statement in the body.

For embedded sentence-style requirements:
- generate a concise semantic title;
- keep full requirement statement in body.

## 10.2 Legacy IDs

Strip bracketed legacy IDs such as:

```text
[SRS1036]
```

from the normative statement.

Preserve in:

```yaml
formerIds:
  - SRS1036
```

Assign the normal MDSE requirement ID.

## 10.3 Status

EA:
```text
Proposed
```

→ MDSE:
```text
Draft
```

## 10.4 Priority

Remove `priority` as an intrinsic Requirement property.

Reason: priority can vary by product/context.

Rules:
- `Must` is implicit default;
- non-Must application-specific priority is documented at the bottom of the Requirement body;
- do not import EA priority.

Example:

```markdown
## Applicability Exceptions

| Applies To | Priority | Notes |
|---|---|---|
| [[PVS 330]] | Should | Preferred for this variant |
```

## 10.5 Ignore low-value EA requirement metadata

Ignore:
- priority;
- difficulty;
- complexity;
- version;
- phase;
- author;
- created/modified dates;
- never-populated fields;
- default-only fields;
- picklist-definition boilerplate.

Preserve only actual engineering meaning or traceability.

## 10.6 Requirement `source`

If meaningful:
- resolve to `derivedFrom` when a corresponding MDSE element exists;
- otherwise preserve unresolved source text in the Requirement body.

Ignore blank/default source.

## 10.7 Requirement `verifyMethod`

If a real selected value exists:
- preserve in the Requirement body as verification intent.

It does not replace explicit:
```text
Test verifies Requirement
```

Ignore default/picklist-definition values.

## 10.8 Requirement ownership

EA Requirement ownership/nesting is organizational/context evidence only.

Do not automatically create:
- parent/child;
- subject;
- appliesTo;
- satisfaction.

Explicit relationships determine semantics.

If a nested Requirement lacks an explicit semantic relationship, flag it and suggest likely mapping.

---

# 11. Canonical Identity and Deduplication

Do not merge elements by name alone.

When an imported EA element appears to duplicate an existing MDSE element, compare:

- name;
- parent/supertype;
- architecture role;
- classifier;
- structural relationships;
- part number;
- source package;
- connected elements;
- engineering meaning.

If identity is clear:
- map the EA GUID to the canonical MDSE element;
- redirect imported relationships to the canonical element;
- preserve source GUIDs in provenance/transformation log.

If identity is uncertain:
- flag for review;
- do not automatically merge.

---

# 12. Model Checks Identified So Far

Suggested checks include:

## `BINDING-NAME-MISMATCH`
Bound endpoints appear semantically equivalent but use different local names.

## `NOTELINK-CONTENT-MISSING`
EA NoteLink exists but XMI does not contain recoverable note text.

## `REQUIREMENT-OWNERSHIP-UNRESOLVED`
Requirement is nested/owned in EA but no semantic relationship explains the ownership.

## Ambiguous semantic type
EA type/stereotype does not cleanly map to approved MDSE type.

## Ambiguous relationship
EA connector type exists but endpoint semantics do not support an approved relationship.

## Canonical identity conflict
Potential duplicate cannot be safely merged.

---

# 13. Deferred Topics

Do not resolve these from the GSE package alone:

1. Transition trigger semantics.
2. Detailed Use Case flow/scenario model.
3. Actor mapping.
4. EA Nesting.
5. Rare isolated EA constructs with insufficient examples.
6. Further generic Interface normalization.
7. Whether some provisional Firmware concepts such as `ACT Protocol` should later become Design.
8. Additional refinement of ambiguous design/behavior content currently preserved in note bodies.

---

# 14. Working Precedence Rules for Future Reference Documents

Every future package-review reference should include:

```yaml
status: PRIMARY-AMENDMENT
version: X.Y
amends:
  - "Section / Rule Name"
adds:
  - "New Rule Name"
```

Use the following precedence:

1. This document remains the baseline primary reference.
2. A later document overrides a rule only when it explicitly names the rule/section being amended or superseded.
3. An added rule supplements this reference but does not implicitly change unrelated rules.
4. If two documents conflict and neither explicitly amends the other, stop and review the conflict rather than guessing.
5. Package-specific exceptions remain package-specific unless explicitly promoted to a global rule.

---

# 15. Short Translator Philosophy

The EA → MDSE translator should:

- preserve engineering meaning rather than UML mechanics;
- reuse existing MDSE concepts whenever possible;
- avoid vague relationship types;
- avoid importing unused EA metadata;
- keep reusable definitions clean;
- keep flow/scenario relationships local to their owning flow/view;
- preserve removed detail in bodies and transformation logs;
- support controlled re-import;
- preserve cross-package identity;
- flag ambiguity instead of silently coercing it;
- evolve package-by-package before broad application.

This document is the **primary reference** for those decisions until explicitly amended.
