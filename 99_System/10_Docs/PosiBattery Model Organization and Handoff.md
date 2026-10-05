# PosiBattery Model Organization and Handoff

## Purpose

This note tells the next engineer or AI how to continue PosiBattery without confusing the current research-oriented organization with the target MDSE product-model organization.

The governing runtime remains:

- MDSE release: `0.8.0`
- Modeling Ruleset: `1.23`
- Workbench: `0.1.17`
- Bootstrap: `0.3.1`
- relationships schema: `1.35`
- element-types schema: `1.17`
- Local Model schema: `0.2`

Read first:

1. `AGENTS.md`
2. `99_System/02_AI/AI_INSTRUCTIONS.md`
3. `99_System/10_Docs/MDSE Modeling Ruleset 1.23.md`
4. `99_System/10_Docs/MDSE Vault File and Folder Structure 0.8.md`
5. this note

## Authoritative PosiBattery vault-level organization

The repository has already been reorganized substantially into the numbered PosiBattery domain structure:

```text
10_Products/
20_Product Architecture/
30_Product Capabilities/
40_Use and Operations/
50_Customer Needs/
60_Stakeholders and Ecosystem/
70_Research and Evidence/
80_Decisions and Planning/
90_Definitions and Reusable Reference/
99_System/
```

This numbered structure is the authoritative vault-level information architecture for PosiBattery and the required destination framework for new stable content and future migrations. It is still being reconciled: some folders contain mixed artifact classes, some navigation files retain pre-migration paths, and the root still contains temporary/migration-source areas such as `Downloads`, `_Cost Driver Research`, `_EMS Research`, and `_Power Conversion Research`.

Do not interpret current placement as semantic proof. Existing links, note identity, explicit relationships, schemas, and evidence provenance remain more important than cosmetic folder uniformity.

The controlled incremental cleanup sequence is `80_Decisions and Planning/PosiBattery Architecture Improvement Plan.md`. Follow that plan one approved step at a time rather than performing an ad hoc bulk reorganization.

## Product-context navigation pattern

Within a specific product or product-family context, the latest MDSE product navigation pattern may be used where it improves clarity:

```text
00 Product Abstract/
00 Product Definition/
01 Product Use Case/
02 Product Context/
03 Product Requirement/
04 Product Function/
05 Product Design/
06 Product Validation/
07 Product Assembly/
09 Product in Progress/
```

Supporting reusable-definition areas may also be used when needed:

```text
Object/
Port/
Item_Flow/
Requirement/
Definitions/
```

This 00–09 structure is subordinate to the authoritative numbered vault taxonomy. It is a product-context navigation pattern, not a second root taxonomy or an ontology. Element type and relationships remain authoritative.

## Meaning of the target areas

### 00 Product Abstract

High-level product framing, product families, product intent, value proposition, scope boundaries, major variants, and concise executive-level model entry points.

Do not duplicate detailed architecture here.

### 00 Product Definition

Authoritative product definitions and reusable product-level concepts. This is the preferred home for notes that define what a product/product family is rather than how it is implemented.

### 01 Product Use Case

Externally controlled behavior, actor goals, operational scenarios, and user/customer interactions.

Actors themselves remain Actor notes. Use Case = externally controlled behavior; Function = product-controlled behavior.

### 02 Product Context

External systems, organizations, environments, surrounding equipment, operating context, source constraints, and other context needed to interpret the modeled product.

Do not convert context into structural `partOf` relationships unless it is truly physical/architectural composition.

### 03 Product Requirement

Requirements in product context, including applicability and traceability.

The Requirement note remains authoritative regardless of folder. Folder placement does not create applicability.

### 04 Product Function

Product-controlled behavior definitions and functional decomposition.

Reusable Function definitions belong here when product-oriented navigation benefits from it.

### 05 Product Design

Design choices, solution concepts, architecture decisions, and reusable design definitions.

### 06 Product Validation

Verification intent, Procedures, Setups, Plans, Results, evidence, and related validation structure.

### 07 Product Assembly

Product architecture and contextual composition where assemblies, local part occurrences, endpoints, connections, and Item Flows are important.

Use the Local Model for contextual occurrences. Do not duplicate reusable Objects merely because they appear in multiple assemblies.

### 09 Product in Progress

Unresolved work, investigation notes, temporary model-development material, review queues, and active synthesis that has not yet earned a stable semantic home.

This is not a permanent dumping ground. Mature concepts should move to their proper model area.

## Mapping from transitional PosiBattery areas

Several of the named areas below now exist beneath numbered domains rather than at the vault root. Their content remains authoritative until a controlled migration step explicitly reclassifies or moves it. When content is reviewed or promoted into a product-specific model, use this guidance:

| Current area | Likely target role |
|---|---|
| Customer Actors | Actor definitions supporting Product Use Case / Product Context |
| Customer Needs | Product Abstract / Product Definition / Product Requirement depending maturity |
| Organizations | Product Context |
| Performance Metrics | Definitions / Product Requirement / Product Validation depending semantics |
| Product Designs | Product Design |
| Product Functions | Product Function |
| Products | Product Definition and Product Assembly depending whether the note is a reusable definition or contextual architecture |
| Research | Product in Progress until findings are promoted into stable model elements |
| Source Documents | Context/evidence; retain source identity rather than converting every document into model structure |
| Downloads | raw source/attachment holding area only |

Do not bulk-convert a folder based on this table. Classify each concept semantically when it is touched.

## Folder creation rule

Do not create all target folders merely because they appear above.

Create a target area when one of these is true:

- it already contains authoritative content;
- new work needs the area immediately;
- migration of existing content into it has been intentionally approved;
- a primary navigation view materially benefits from it.

Avoid empty scaffolding.

When a primary top-level target area becomes active, use the standard navigation set:

```text
README_<folder>.md
BASE_local_<folder>.base
BASE_all_<folder>.base
CANVAS_<folder>.canvas
```

Lower-level folders receive navigation artifacts only when they provide real navigation value.

## Workbench expectations

Workbench 0.1.17 is installed as the current verified candidate used by the WB-106 acceptance repository.

It supports the current Local Model 0.2 contract and occurrence-aware views. Contextual part occurrences, endpoints, connections, flows, and exposed boundaries should remain local-model records rather than being expanded into duplicate standalone notes.

The Workbench is a derived interface over Markdown/YAML. Markdown/YAML remains authoritative.

## Handoff rule

The next tool or user should improve the model incrementally:

1. preserve note identity and existing relationships;
2. classify before moving;
3. use the target product folders for new stable product-model work;
4. migrate older content only when it is already being reviewed;
5. use `09 Product in Progress` for unresolved synthesis rather than inventing weak element types;
6. run Workbench/Bootstrap release checks after structural changes;
7. keep Git history as the approval/recovery boundary.

A folder cleanup that breaks links or obscures provenance is worse than an imperfect but stable folder name.
