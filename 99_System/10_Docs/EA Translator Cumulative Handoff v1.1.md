---
title: EA to MDSE Translator — Cumulative Handoff
shortTitle: EA → MDSE Translator Handoff
documentType: Translator Reference
status: PRIMARY-AMENDMENT-HANDOFF
authority: Cumulative working reference; incorporates the v1.0 GSE baseline and explicitly approved amendments through 2026-09-04
version: 1.1
date: 2026-09-04
baselineReference: EA_to_MDSE_Translator_Primary_Reference_v1.0_GSE
sourcePackagesReviewed:
  - GSE
  - Monitor System
  - Communications Design
  - 01 What
appliesTo: Sparx Enterprise Architect XMI -> MDSE Obsidian translation
amends:
  - Section 5.2 Requirements
  - Section 5.4 Functions and Activities
  - Section 5.6 EA Change
  - Section 5.11 EA Use Cases
  - Section 5.12 EA StateMachine
  - Section 6.2 Aggregation
  - Section 6.8 refine
  - Section 6.11 EA Usage
  - Section 6.12 EA extend
  - Section 9 State and Transition Model
  - Section 13 Deferred Topics
adds:
  - deriveReqt mapping
  - requirement stereotype semantic classification
  - refines/refinedBy relationship vocabulary
  - design-taxonomy StateMachine handling
  - semantic Use Case versus Function classification
  - semantic Use Case hierarchy review
  - EA include required-step handling
  - Actor semantic classification
  - external-system Actor correction
  - semantic realizedBy versus dependsOn handling
---

# EA to MDSE Translator — Cumulative Handoff

> **PURPOSE OF THIS HANDOFF**
>
> This document is the cumulative working reference for continuing the EA → MDSE translator review in a new chat or work session. It preserves the important decisions from the original **EA to MDSE Translator — Primary Reference v1.0 (GSE)** and explicitly incorporates the approved findings from the subsequent **Monitor System**, **Communications Design**, and **01 What** package reviews.
>
> Do not reopen an approved decision merely because a later package uses a different EA convention. Later evidence should either confirm the existing rule, expose a real conflict, or justify an explicit amendment.

## 1. Project Intent

The translator is not intended to reproduce Sparx EA, UML, or SysML mechanically inside Obsidian. It should convert source-model content into the practical MDSE metamodel while preserving:

- engineering meaning;
- useful traceability;
- reusable definitions;
- controlled inheritance/generalization;
- explicit semantic relationships;
- source provenance;
- enough detail for controlled re-import and review.

Obsidian is the primary working environment. The model should remain understandable to engineers who are not modeling specialists. Folder structure supports human browsing but does not define semantics.

The translator should prefer semantic relationships such as `subtypeOf`, `partOf`, `parent`, `derivedFrom`, `refines`, `satisfies`, `realizedBy`, `dependsOn`, `appliesTo`, `verifies`, etc. over preserving generic EA connector names.

## 2. Review Strategy

Continue package-by-package. For each package:

1. Inventory the local semantic element types and connector patterns.
2. Apply already-approved rules without reopening them.
3. Prioritize high-volume and high-impact patterns.
4. Compare unusual patterns against previous packages.
5. Add a new rule only when the engineering meaning is clear and the rule is useful beyond one isolated example.
6. Preserve unresolved cross-package endpoints in the pending relationship registry.
7. Flag ambiguity rather than silently coercing a type or relationship.

A package review is complete when the remaining unresolved items are isolated cases or lower-impact patterns that are better resolved by broader evidence.

---

# 3. Import Architecture — Unchanged Baseline

## 3.1 Controlled synchronization

Repeat EA imports use controlled synchronization.

- EA owns imported source-model semantics and approved mapped source fields.
- Obsidian owns MDSE IDs, vault placement, local/AI annotations, derived/query content, and enriched local documentation.
- Shared fields produce a conflict when both sides changed.

## 3.2 Provenance

Every imported note carries at least:

```yaml
eaGUID: EAID_...
eaPackage: <source package>
```

Merged/consolidated MDSE elements may carry multiple EA GUIDs.

Raw EA metaclass/stereotype information normally belongs in translator diagnostics and transformation logs rather than engineering frontmatter.

## 3.3 Cross-package references

Use a **pending relationship registry** when the remote endpoint has not yet been imported.

Store, where available:

- source GUID;
- target GUID;
- source/target names;
- source/target EA types;
- EA connector type;
- direction;
- package information;
- intended MDSE mapping if already known.

Do not create placeholder engineering notes merely to satisfy unresolved EA relationships.

## 3.4 Required translator outputs

Maintain:

1. **Identity Registry** — EA GUID ↔ MDSE ID ↔ filepath.
2. **Transformation Log** — merges, collapses, suppressed elements, semantic remaps, renames, relationship substitutions, consolidated interfaces/flows, source GUIDs.
3. **Model-Check Report** — ambiguous types/relationships, naming problems, unresolved ownership, suspicious source modeling.
4. **Pending Relationship Registry** — unresolved cross-package endpoints.

## 3.5 Data preservation

When an EA element is collapsed or semantically reclassified, preserve useful detail in the body of the resulting MDSE element and record the transformation. The simplified MDSE metamodel must not silently discard engineering content.

---

# 4. Core Translation Philosophy — Unchanged Baseline

1. **Most specific engineering meaning wins.** Generic UML types are implementation details when a stronger semantic interpretation is available.
2. **Type is semantic, not purely mechanical.** EA `State`, `Port`, `InformationItem`, `UseCase`, `Change`, `InstanceSpecification`, etc. may require semantic classification.
3. **Do not invent weak relationships.** Avoid carrying `trace`, `allocate`, generic `Association`, or vague `uses` relationships when a clearer MDSE relation exists.
4. **Store relationships once.** Prefer one authoritative direction and derive inverses for navigation.
5. **Do not merge by name alone.** Identity uses GUID, structure, classifier, parents, part numbers, roles, relationships, package, and engineering meaning.
6. **Folders do not create semantics.** EA package/ownership and Obsidian folder placement are contextual evidence only unless an approved semantic rule says otherwise.

---

# 5. Current Element-Type Translation Rules

## 5.1 Things and architecture — baseline

### EA `Hardware Component`

→ `Electrical`

### EA `Physical Component`

Classify semantically:

- physical hardware → `Mechanical` where appropriate;
- manuals/specifications → `Document`;
- labels/markings → `Artifact`;
- ambiguous → review.

### EA `Physical System Variant`

Pragmatic current mapping → `Electrical`, with architecture role handled separately.

### EA `Software Component`

- embedded/tied to physical product platform → `Firmware`;
- application/cloud/tool/service → `Software`;
- ambiguous → review.

### EA `Module`

Does not define discipline. Preserve architecture role separately.

## 5.2 Requirements — AMENDED

### `functionalRequirement`

→ `Requirement`, `requirementType: Functional`

### EA stereotype `Functional`

Approved synonym of `functionalRequirement`:

→ `Requirement`, `requirementType: Functional`

### `designConstraint`

→ `Requirement`, `requirementType: Design Constraint`

### Generic EA `requirement`

**Not type-bearing beyond being a Requirement.** Classify the requirement type semantically from:

- normative statement;
- explicit relationships;
- source/target context;
- engineering meaning.

If evidence is insufficient, flag for review rather than guessing.

Recommended model check:

```text
REQUIREMENT-TYPE-AMBIGUOUS
```

Examples from Monitor System:

- `Revenue Grade Metering` — statement describes measurement behavior; likely Functional.
- `Temperature Monitoring` — statement describes monitoring behavior; likely Functional.
- `Component Temperature` / `Monitor Usage` lacked enough useful documentation and should be reviewed.

### Embedded/internal EA Requirement

→ standalone MDSE Requirement; ownership does not automatically create semantics.

## 5.3 Interfaces and ports — baseline

### `ProxyPort`

→ `Interface`

### `FullPort`

→ `Electrical`

### Plain `Port`

Semantic classification. Examples from the baseline include:

- physical connector → Electrical;
- seal → Mechanical;
- keep-out/A-surface → Interface;
- signals may consolidate into an Interface/Item Flow model.

## 5.4 Function versus Use Case — MAJOR AMENDMENT

### MDSE Function

A **Function** is behavior performed or controlled by the product/system being modeled.

This includes:

- reusable product behavior;
- internal system behavior;
- a controlled series of steps where the modeled product owns the behavior.

### MDSE Use Case

A **Use Case** is behavior/activity that is **outside the control of the product being modeled**.

Typical Use Cases include:

- behavior performed by a person;
- behavior performed by a living actor;
- activity performed by an external organization;
- behavior performed by a third-party/external product or system.

A third-party product's behavior may therefore appear as a Use Case in this model even though that behavior would be a Function inside the third party's own product model.

### EA `Activity`

Classify semantically:

- product-controlled behavior → Function;
- human/external/uncontrolled behavior → Use Case;
- test behavior → Test/Step according to test-model rules;
- ambiguous → review.

### EA `UseCase`

**No longer universally type-bearing.** An EA Use Case must also be semantically classified.

- external/uncontrolled goal or action → Use Case;
- behavior actually performed by the modeled product → Function;
- low-level behavior embedded in a detailed scenario may become reusable Function + Function Usage / Functional Flow content;
- failure/problem content may become Issue when clearly modeled incorrectly;
- purely organizational/grouping shells may be suppressed if they have no independent engineering meaning.

This is especially important for the `01 What` package, which contains 975 unique EA Use Cases. Mechanical import would preserve contributor modeling style rather than engineering semantics.

## 5.5 State-shaped elements

### True persistent operating/mode/configuration condition

→ `State`

### Action-like State

→ `Function`

### Design-description State

→ `Design`

This rule is now reinforced by the Communications Design package; see Section 8.

## 5.6 EA `Change` — AMENDED

EA `Change` is **not type-bearing**. Classify case-by-case from actual engineering meaning.

Possible mappings include:

- Issue;
- Requirement;
- Design;
- another semantic MDSE element where justified.

Do not establish a global Change→Requirement or Change→Issue mapping.

### Approved package-specific example

`Temperature Sensor Unstable` in Monitor System is interpreted as an **Issue** because it describes an undesired/problem condition. Its connected Requirement and Function describe the response, not the type of the Change element.

Preserve the source EA Change type in provenance/transformation diagnostics.

## 5.7 Generic SysML `block`

Not type-bearing by itself. Classify by semantic meaning.

## 5.8 EA `InstanceSpecification` — baseline

### Real installed/serialized occurrence

→ real `instanceOf`

### Product-design occurrence / named design position

→ normal reusable Thing, usually with `subtypeOf` classifier and `partOf` owner rather than `instanceOf`.

### Firmware version modeled as instance

→ reusable Firmware subtype + structural placement; not `instanceOf`.

## 5.9 EA `InformationItem` — baseline

- one-to-one descriptive shadow → collapse into target note body;
- independent descriptive knowledge → `Info`, usually `describes` target;
- failure/problem content → Issue;
- one-to-one behavioral annotation → merge into State/Transition/Function/Design/Functional Flow body;
- ambiguous → review.

## 5.10 Physical Context — baseline

EA Physical Context → Use Case category `Where`, with a `subject` focal element and participant context rather than structural `partOf`.

## 5.11 Actor — NEWLY RESOLVED

### Actor definition

Actor = an external living/person role participating in behavior.

Actors may represent:

- individuals/roles;
- types of people;
- living things.

Actors may be related to:

- a broader/general actor by `subtypeOf` / `supertypeOf`;
- an organization by a suitable organization-membership representation when/if that relation is needed.

### External systems incorrectly modeled as Actors

Devices, products, software systems, vehicles, or other non-living systems modeled as EA Actors should be reclassified as **external Things**, not preserved as Actor solely because of the EA metaclass.

Example evidence in `01 What`: `Electric Vehicle` appears as an EA Actor reference; semantically it should be an external Thing.

### Actor ↔ Use Case

The MDSE model already supports Actor participation semantics. Preserve Actor participation when the endpoint truly is an Actor.

The exact generic relationship for an **external Thing participating in a Use Case** remains deferred until more representative examples justify adding or reusing a relation.

---

# 6. Current Relationship Translation Rules

## 6.1 Generalization — baseline, strongly reinforced

EA source = specific; destination = general.

```text
source subtypeOf destination
```

Derived inverse:

```text
destination supertypeOf source
```

Multiple inheritance is allowed where it reflects real semantics.

## 6.2 Aggregation — AMENDED

### Thing → Thing Aggregation

Structural meaning:

```text
source partOf destination
```

### Function → Function Aggregation

Monitor System established a distinct semantic pattern. Function Aggregation is decomposition, not physical structure:

```text
source parent destination
```

or equivalently destination `child` source, depending on the authoritative direction used by the vault.

Do **not** use `partOf` for Function decomposition.

Examples:

- `Analyze Ground Monitoring Signal` → child of `Sense Ground Integrity`.
- `Detect Changes in Ground Monitoring Signal` → child of `Sense Ground Integrity`.
- `Detect Residual Current` → child of `Prevent Residual Current`.

### Physical Context exception

Aggregation into a Physical Context remains participant membership, not `partOf`.

## 6.3 Generic Association — baseline

No global mapping. Classify by endpoints/meaning.

Examples retained from baseline:

- Use Case ↔ Thing subject relationship where the Thing is the focal subject;
- Issue ↔ Thing → `affects`;
- vague Thing ↔ Thing → ignore unless meaningful;
- information/documentation ↔ Thing → `describes`, `defines`, or `refines` only when clear.

## 6.4 `instanceOf` — baseline

Reserved for actual real-world occurrences, not variants, firmware versions, or reusable design positions.

## 6.5 `allocate` — baseline semantic mapping

No global mapping.

Approved patterns:

- Function → Thing → Thing `performs` Function;
- Design → Thing → Design `designOf` Thing / Thing `hasDesign` Design;
- Issue → Function/Use Case → Issue `affects` behavior;
- Information Item → behavior → `defines` only when logical;
- true State → Thing allocation → state ownership/context evidence, not invented State→Thing relation;
- firmware-version exception → `partOf` PCBA where already approved.

## 6.6 `satisfy` — CURRENT RULE RETAINED; NEW CONFLICT DEFERRED

Approved strict satisfaction patterns remain:

```text
Function satisfies Functional Requirement
State satisfies Functional Requirement
State Machine satisfies Functional Requirement
Design satisfies Design Constraint
```

Do not coerce an element's semantic type merely to preserve an EA `satisfy` connector.

### Deferred conflict from Communications Design

Some communication Designs are connected by EA `satisfy` to Functional Requirements. This may indicate:

- an omitted Function;
- inconsistent EA use of satisfy;
- a later need to distinguish applicability from satisfaction.

Do **not** globally convert these yet. More package evidence was explicitly requested before resolving the rule.

## 6.7 EA `Realisation` — baseline interim rule

Thing/Document/Firmware → Requirement Realisation currently maps conservatively to:

```text
Requirement appliesTo Thing
```

Do not expand Thing `satisfies` Requirement from existing evidence alone.

Unusual Activity→Activity Realisation remains deferred.

## 6.8 `refine` — AMENDED AND STRONGLY CONFIRMED

Add explicit non-inheriting MDSE relationship:

```text
refines / refinedBy
```

Meaning: source adds precision, detail, or constraint to the target engineering definition without implying fulfillment, derivation, decomposition, or specialization.

Approved endpoint patterns now include:

- Use Case `refines` Requirement;
- Requirement `refines` Function;
- Requirement `refines` Requirement.

The `01 What` package contains **294 explicit SysML `refine` connectors**, overwhelmingly reinforcing the Use Case→Requirement pattern.

Do not broaden endpoints merely because an InformationItem descriptive shadow used a refine connector; collapse such one-to-one shadows according to the InformationItem rule.

## 6.9 `deriveReqt` — NEW APPROVED RULE

EA `«deriveReqt»` Requirement source→Requirement destination maps to:

```text
source Requirement derivedFrom destination Requirement
```

Do not create an MDSE `deriveReqt` relationship.

If the destination is not imported:

- create a pending relationship registry entry;
- preserve target GUID and intended mapping;
- do not create a placeholder Requirement.

Monitor System provided 51 repeated Requirement→Requirement examples, making this a high-confidence rule.

## 6.10 `trace` — baseline principle retained

Never preserve generic EA `trace` mechanically.

Convert to a clearer semantic relation when evidence supports it, for example:

- Info → Thing → `describes`;
- Issue → Use Case/Requirement → `affects`;
- Thing → Requirement → reverse to Requirement `appliesTo` Thing.

Mixed Activity/State/Requirement trace patterns seen in Monitor System remain evidence for semantic review rather than a new blanket mapping.

## 6.11 Plain Dependency — baseline

Behavior dependency means `dependsOn` only when it reads as a true prerequisite/reliance.

Do not use Dependency as execution order; execution order belongs in Functional Flow topology.

## 6.12 EA `Usage` — MAJOR AMENDMENT FOR USE CASE → FUNCTION

The original provisional blanket mapping of Use Case→Function Usage to `dependsOn` is **superseded**.

Classify the relationship semantically:

### Function implements/performs the behavior that realizes the external scenario

```text
Use Case realizedBy Function
```

### Function is merely prerequisite/reliance and does not implement the scenario

```text
Use Case dependsOn Function
```

### Meaning unclear

Flag for relationship review.

Examples from `01 What` support this distinction:

- `Access Cloud Portal` → communication Function is plausibly `realizedBy`.
- `Configure Charger ID` → `Communicate with User` is plausibly `realizedBy`.
- broad supporting behaviors such as `Control System Operations` may be dependency rather than realization and should be reviewed semantically.

Do not introduce a generic MDSE `uses` relation from this EA pattern.

## 6.13 EA `extend` — CONFIRMED

EA `extend` means an optional/conditional Use Case option:

```text
optional Use Case optionOf base Use Case
```

Derived inverse:

```text
base Use Case hasOption optional Use Case
```

`01 What` contains **454 `extend` relationships**, making this an important high-volume rule.

Preserve extension conditions/details in the optional Use Case body or scenario context.

## 6.14 EA `include` — NEW SEMANTIC RULE

EA `include` means a **required step/behavior necessary to perform the Use Case**.

Do not create a new generic `include` relationship merely to reproduce UML.

Classify the included element first:

### Included element remains a Use Case

Represent it as required constituent/decomposition behavior, normally through the appropriate Use Case hierarchy (`parent` / `child`) when the semantic relationship is truly decomposition.

### Included element is actually product-controlled behavior

Reclassify it as Function and connect through:

- `Use Case realizedBy Function` when the Function implements the scenario; and/or
- Function Usage in the Use Case's Functional Flow when sequence/topology matters.

`01 What` contains **238 `include` relationships**, so this rule affects a large volume of import content.

## 6.15 EA explicit `Nesting` connector — STILL DEFERRED

Do not confuse this with XML ownership/nesting of Use Cases or States.

The generic EA **Nesting connector** remains deferred. Monitor System supplied two Requirement→Function-style examples but the user explicitly requested more examples before establishing a connector rule.

Requirement ownership remains context-only under Section 10.8 regardless.

---

# 7. Use Case Hierarchy — MAJOR NEW GUIDANCE

The `01 What` package contains 975 unique EA Use Cases:

- 33 top-level;
- 522 one level below a Use Case;
- 335 two levels below;
- 85 three levels below.

Therefore **942 of 975** are nested under another Use Case.

Many contributors populated this source model, and nesting was used inconsistently. It sometimes represents decomposition/parent-child and sometimes specialization/generalization.

## 7.1 Explicit Generalization

Explicit EA Generalization remains authoritative:

```text
specific subtypeOf general
```

## 7.2 Use Case ownership/nesting

EA Use Case nesting is **non-authoritative semantic evidence** and must be interpreted.

Use:

```text
"is a kind of"        → subtypeOf
"is a constituent of" → parent / child
unclear                → review
```

Do not mechanically generate 942 `parent/child` relationships from the `01 What` ownership tree.

Examples:

- `Assign/Input User Role as Administrator` is naturally a specialization of `Assign/Input User Role`.
- `Configure Battery Parameters` with constituent configuration activities may represent decomposition when the children are required subactivities.
- `Charge Lead Acid` / `Charge Lithium` under `Charge Vehicle` read more like variants/specializations than simple decomposition.

## 7.3 Relationship vocabulary remains distinct

Keep separate:

- `subtypeOf / supertypeOf` — kind-of, inheritance/generalization;
- `parent / child` — decomposition/hierarchy;
- `optionOf / hasOption` — optional/conditional behavior;
- `realizedBy / realizes` — external scenario implemented by product behavior;
- `dependsOn` — prerequisite/reliance.

---

# 8. StateMachine Semantic Classification — MAJOR AMENDMENT

The baseline already established that EA StateMachine is semantic, not mechanical. Communications Design adds a third important case.

## 8.1 True state model

If the model contains real persistent states and meaningful transitions:

→ first-class `State Machine` + `State` + `Transition`.

## 8.2 Single-state/detail behavior container

If the EA StateMachine is merely a behavior/detail container around one semantic State:

- collapse the generated StateMachine;
- preserve the actual State;
- create/retain the Functional Flow;
- connect `State hasBehavior Functional Flow`;
- preserve source StateMachine GUID in transformation log;
- derive meaningful names rather than using generated `EA_StateMachine#` names.

## 8.3 Non-behavioral StateMachine used as a Design taxonomy — NEW APPROVED RULE

Communications Design contains a StateMachine with communication concepts such as:

- Communications Design;
- Wired Interface;
- Wireless Interface;
- CAN Interface;
- BLE Interface;
- WiFi 802.11 Interface;
- Cellular Interface;
- PAN 802.15;
- LPWAN Interface;
- WLAN 802.11;
- etc.

The package itself notes that this is an older diagram whose protocol variants had been moved into “system states.” The model has a large state taxonomy but no meaningful transition behavior.

Approved translation:

- suppress the non-behavioral StateMachine as an MDSE State Machine;
- translate the communication “States” semantically to **Design**;
- preserve original State/StateMachine GUIDs and source structure in the transformation log.

Do **not** map these to MDSE Interface merely because their names contain “Interface.” They represent reusable communication/design choices or capabilities rather than a concrete boundary carrying Item Flows.

## 8.4 Former substate hierarchy in a Design taxonomy — APPROVED DEFAULT

When State/substate containment is reclassified as a Design taxonomy, default the hierarchy to **generalization**:

```text
child Design subtypeOf parent Design
```

Explicit EA Generalizations remain independently authoritative and may create additional inheritance.

Example:

```text
BLE Interface subtypeOf Wireless Interface
BLE Interface subtypeOf PAN 802.15
```

Multiple inheritance is acceptable.

Safeguard: if “child is a kind of parent” is semantically false, flag for review rather than forcing generalization.

This rule is specific to a State hierarchy already determined to be a non-behavioral Design taxonomy. It does not settle the generic EA Nesting connector.

---

# 9. Functional Flow Model — Baseline with Use Case Implications

Retain the baseline distinction:

- reusable Function = definition;
- Function Usage = contextual invocation inside one Functional Flow;
- Functional Flow owns ordering, guards, branches, decisions, and local execution topology;
- do not encode execution order as global Function→Function dependencies.

EA ControlFlow remains a local flow edge.

CallOperationAction / repeated behavior should reuse the canonical Function and create Function Usage in the owning flow.

### CallBehaviorAction

Monitor System supplied a CallBehaviorAction example, but the detailed rule remains deferred until more package evidence is available. The current candidate is to treat it similarly as a contextual invocation of reusable behavior rather than a new Function definition.

### Use Case detailed flows

`01 What` contains:

- 45 ControlFlows;
- 35 InstanceSpecifications;
- 15 unique Actions;
- decision/fork constructs;
- interactions/lifelines.

This is enough to confirm that some EA Use Cases contain real scenario topology, but detailed Use Case→Functional Flow conversion is still deferred until the higher-level semantic classification is stable.

---

# 10. Requirement Translation Rules — Baseline + Confirmations

## 10.1 Requirement title and normative statement

Use concise semantic title; preserve full normative statement in body.

Sentence-style embedded requirements should receive a concise generated title while preserving the source statement.

## 10.2 Legacy IDs

Strip bracketed legacy IDs from normative text and preserve them in `formerIds`.

## 10.3 Status

EA `Proposed` → MDSE `Draft`.

## 10.4 Priority

Do not import EA priority as an intrinsic Requirement property. `Must` is implicit default; context-specific exceptions may be documented in the body.

## 10.5 Ignore low-value metadata

Ignore default/non-engineering metadata such as author, timestamps, generic difficulty/complexity, default-only values, etc.

## 10.6 Requirement source

Resolve meaningful source to `derivedFrom` when a corresponding MDSE element exists; otherwise preserve source text in the body.

## 10.7 Verification intent

Preserve selected verifyMethod as body-level verification intent. It does not replace explicit `Test verifies Requirement`.

## 10.8 Requirement ownership — RETAINED

EA Requirement ownership/nesting is organizational/context evidence only.

Do not automatically create:

- parent/child;
- subject;
- appliesTo;
- satisfaction;
- refinement.

Explicit semantic relationships such as `refines`, `appliesTo`, `satisfies`, `derivedFrom`, etc. determine MDSE semantics.

If a Requirement is nested under a Function/Design/Use Case with no explicit semantic relationship, flag it for review and suggest likely semantics rather than silently creating one.

This rule remains settled even though the **generic EA Nesting connector** itself is still deferred.

---

# 11. Canonical Identity and Naming

Do not merge by name alone.

Compare:

- EA GUID;
- semantic type;
- supertype/parent;
- architecture role;
- classifier;
- structural relationships;
- part number;
- package/source;
- connected elements;
- engineering meaning.

## 11.1 Same-name different-type concepts — evidence, naming convention deferred

Communications Design includes same-name concepts that are clearly distinct, for example a Design concept and a Requirement with the same EA name such as `SmartGuard Interface`.

Do **not** merge these merely because the name matches.

The final global filename/title disambiguation convention remains deferred. Prefer semantic requirement titles derived from the normative statement where practical rather than blindly appending type labels, but do not establish a universal naming rule until broader imports are reviewed.

---

# 12. Package Review Findings and Evidence

## 12.1 GSE — baseline package

Established the original translator architecture and broad semantic principles, including:

- split authority and controlled synchronization;
- identity/transformation/model-check/pending registries;
- semantic type translation;
- initial Interface/Item Flow model;
- Functional Flow definition/usage distinction;
- State vs Function vs Design correction;
- Requirement ownership as context only;
- conservative Realisation/applicability handling;
- generic trace/allocate/dependency semantic conversion;
- StateMachine single-state/detail collapse;
- transition trigger deferral.

The original v1.0 reference remains useful for detailed GSE examples and low-level baseline rules not repeated here.

## 12.2 Monitor System — approved amendments and evidence

High-value package characteristics included a large functional model with many Requirements and relationships.

Approved findings:

1. `deriveReqt` Requirement→Requirement → `derivedFrom`.
2. Function→Function Aggregation → `parent/child`, never `partOf`.
3. Add `refines/refinedBy` relationship vocabulary.
4. EA `Functional` stereotype is a synonym for Functional Requirement.
5. Generic EA `requirement` requires semantic requirement-type classification.
6. EA `Change` is case-by-case; `Temperature Sensor Unstable` specifically maps to Issue.
7. Existing single-state/detail StateMachine collapse rule was reinforced.
8. Functional Flow / Function Usage strategy was reinforced.

Deferred evidence retained:

- explicit EA Nesting connector;
- mixed `trace` cases;
- Activity→Activity Realisation;
- Issue→State Usage;
- CallBehaviorAction details;
- questionable State classifications;
- transition trigger semantics.

## 12.3 Communications Design — approved amendments and evidence

This package is an old communication-design model represented largely as States inside a StateMachine.

Approved findings:

1. A non-behavioral EA StateMachine may actually be a Design taxonomy.
2. In that case suppress the StateMachine and translate semantic States to Design.
3. Former State/substate taxonomy hierarchy defaults to `subtypeOf`.
4. Explicit Generalization remains additive and authoritative.
5. Multiple inheritance is allowed.

Deferred:

- how to handle EA Design `satisfy` Functional Requirement mismatches;
- final same-name Design/Requirement naming convention;
- some cross-package dependencies until more packages are imported.

## 12.4 `01 What` — high-volume Use Case package

Unique local UML content includes approximately:

- 975 Use Cases;
- 454 `extend` relationships;
- 238 `include` relationships;
- 187 Usage relationships;
- 383 Associations;
- 264 Generalizations total;
- 294 explicit SysML `refine` relationships;
- 45 ControlFlows;
- 35 InstanceSpecifications;
- 15 unique Actions.

Use Case nesting depth:

- 33 top-level;
- 522 at depth 1;
- 335 at depth 2;
- 85 at depth 3.

Approved findings:

1. Use Case = behavior outside product control; Function = behavior controlled/performed by the modeled product.
2. EA UseCase metaclass requires semantic classification; do not import all 975 mechanically as MDSE Use Cases.
3. Use Case nesting is non-authoritative because contributors used it for both decomposition and generalization.
4. `extend` = `optionOf`.
5. `include` = required constituent behavior; translate semantically rather than preserving UML include.
6. Actors are living/person roles; systems/devices modeled as Actors become external Things.
7. Use Case→Function Usage is semantic: `realizedBy` when the Function implements the scenario, `dependsOn` when it is only a prerequisite/reliance.
8. Large refine volume strongly confirms Use Case→Requirement `refines`.

---

# 13. Model Checks

Established baseline checks:

```text
BINDING-NAME-MISMATCH
NOTELINK-CONTENT-MISSING
REQUIREMENT-OWNERSHIP-UNRESOLVED
```

Also continue generic checks for:

- ambiguous semantic type;
- ambiguous relationship;
- canonical identity conflict.

Recommended additions based on later packages:

```text
REQUIREMENT-TYPE-AMBIGUOUS
USECASE-TYPE-AMBIGUOUS
USECASE-HIERARCHY-AMBIGUOUS
RELATIONSHIP-SEMANTICS-AMBIGUOUS
```

These names are implementation recommendations; the semantic behavior (flagging ambiguity rather than guessing) is authoritative even if final diagnostic naming changes.

A potential `SATISFY-TYPE-MISMATCH` check is useful for Communications Design-style cases, but the relationship transformation itself remains deferred.

---

# 14. Deferred Topics — CURRENT LIST

Do not force decisions on the following until additional examples justify them:

1. **Transition trigger semantics** — Interface-based versus local/event triggers.
2. **Generic EA Nesting connector** — especially Requirement-related cases.
3. **Detailed Use Case scenario/flow transformation** — when/how Use Case steps become Functional Flow and Function Usage.
4. **CallBehaviorAction detailed handling** — candidate is contextual Function Usage, but broader examples are preferred.
5. **Activity→Activity Realisation** — insufficient semantic evidence.
6. **Issue→State Usage** — likely not literal Usage; more examples needed.
7. **Mixed `trace` patterns** not covered by existing semantic endpoint rules.
8. **Design satisfying Functional Requirement** — do not weaken strict satisfaction rules from Communications Design alone.
9. **Final same-name element naming/disambiguation convention** across different semantic types.
10. **External Thing participation in Use Case** — avoid adding a new relation until examples show what is needed.
11. **Rare isolated EA constructs** that do not materially affect translation volume or meaning.
12. **Further generic Interface normalization** where package context is insufficient.

---

# 15. Current Precedence / Do-Not-Reopen List

Unless new evidence creates a real contradiction, treat these as settled:

- EA provenance and controlled synchronization architecture.
- Pending relationship registry; no cross-package placeholders.
- Generalization → `subtypeOf/supertypeOf`.
- Thing Aggregation → structural `partOf`.
- Function Aggregation → `parent/child`.
- `deriveReqt` → `derivedFrom`.
- `refines/refinedBy` vocabulary and approved endpoints.
- Functional / functionalRequirement → Functional Requirement.
- Generic requirement stereotype requires semantic classification.
- Requirement ownership is context only; explicit semantic relation wins.
- EA Change is case-by-case.
- State-shaped content is classified semantically.
- Single-state/detail StateMachine collapses to State + Functional Flow.
- Non-behavioral StateMachine design taxonomy → Designs; hierarchy defaults to generalization.
- Function = behavior controlled by modeled product.
- Use Case = behavior outside modeled product control.
- EA UseCase metaclass is not mechanically type-bearing.
- Use Case nesting requires semantic review.
- `extend` → `optionOf`.
- `include` means required constituent behavior and should be translated semantically.
- Actor = living/person role; external systems/devices become Things.
- Use Case→Function Usage → semantic `realizedBy` versus `dependsOn`.
- Do not preserve generic `trace`, `allocate`, `Association`, or `Usage` simply because EA contains them.
- Do not merge by name alone.

---

# 16. Recommended Workflow for the Next Package

When reviewing the next EA package:

1. Identify its dominant semantic domain (physical architecture, interfaces, software, state behavior, tests, requirements, etc.).
2. Produce local element/connector counts using unique source IDs where possible; EA extension content can duplicate UML objects.
3. Apply the settled rules above first.
4. Specifically look for evidence related to the current deferred list.
5. Prioritize high-volume/high-impact patterns rather than isolated EA oddities.
6. If a deferred pattern becomes clear across multiple packages, present the evidence and recommend the simplest scalable rule.
7. Preserve unresolved endpoints by GUID rather than creating placeholders.
8. Keep a cross-package evidence matrix for patterns still under review.

Suggested evidence matrix:

| EA Pattern | GSE | Monitor System | Communications Design | 01 What | Current Translator Decision |
|---|---|---|---|---|---|
| Requirement ownership | evidence | repeated | limited | some | context only; explicit semantics win |
| explicit EA Nesting connector | sparse | 2 examples | — | TBD | deferred |
| `deriveReqt` | examples | 51 repeated | many | few | `derivedFrom` |
| Function Aggregation | — | 16 repeated | — | — | Function parent/child |
| `refine` | UC→Req | mixed endpoints | some | 294 repeated | explicit `refines` |
| non-behavioral State taxonomy | some state corrections | questionable states | strong evidence | indirect cross-links | State→Design when semantic; design taxonomy rule approved |
| Use Case type fidelity | initial | — | — | strong mixed evidence | semantic Use Case vs Function |
| Use Case hierarchy | baseline assumption | — | — | strong inconsistent contributor usage | semantic review |
| `extend` | examples | — | — | 454 | `optionOf` |
| `include` | limited | — | — | 238 | required constituent behavior |
| Actor type fidelity | deferred | — | — | strong evidence incl. systems-as-actors | living/person Actor; systems→external Thing |
| UC→Function Usage | provisional dependsOn | examples | — | 187 Usage | semantic `realizedBy` vs `dependsOn` |
| transition trigger | deferred | deferred | no useful transitions | limited | deferred |
| satisfy type mismatch | — | — | strong Design→FR concern | TBD | deferred |

---

# 17. Short Handoff Summary

The translator has moved from **EA-metaclass mapping** toward a consistent **semantic classifier**.

The most important recent evolution is that EA element type and containment are increasingly treated as evidence rather than authority when contributor conventions are inconsistent:

- Requirements are classified by normative meaning.
- States can become State, Function, or Design.
- Entire StateMachines can collapse or become Design taxonomies.
- EA Use Cases can become Use Cases, Functions, or local flow behavior depending on who controls/performs the behavior.
- Use Case nesting cannot be trusted as decomposition without semantic review.
- Actors are semantic external living/person roles; external systems become Things.
- Connector names such as Usage, trace, allocate, satisfy, include, extend, and refine are translated according to engineering meaning and approved MDSE relationship semantics.

The goal remains a lightweight model that improves traceability, reuse, navigation, analysis, and engineering decision-making without reproducing Enterprise Architect inside Obsidian.


---

# Appendix A — Original v1.0 GSE Primary Reference (Verbatim)

> **PRECEDENCE NOTE:** This appendix preserves the previous detailed import reference in full. Where the cumulative handoff sections above explicitly amend a v1.0 rule, the amended rule above takes precedence. Unamended detail in this appendix remains valid working guidance.

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
