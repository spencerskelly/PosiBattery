# PosiBattery Model Organization and Handoff

## Purpose

This note tells the next engineer or AI how to continue PosiBattery using the authoritative numbered vault architecture while preserving transitional content, product-context navigation, identity, relationships, and provenance.

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

## Placement rules for the 00–09 product pattern

The 00–09 pattern is a **product-context navigation layer**. It may be created beneath a specific product or product-family context when that product has enough engineering content to benefit from a dedicated working structure.

Use these rules:

1. **Do not create 00–09 folders at the vault root.** The authoritative root remains the numbered 10–99 taxonomy.
2. **Do not create the full 00–09 set automatically.** Create only the sections that contain real content or provide demonstrated navigation value.
3. **Do not duplicate reusable definitions.** A cross-product Function, Design, Object, Port, Requirement, technology, or other reusable concept keeps one canonical note in its numbered domain. The product context links to that note.
4. **Product-specific content may live in the product context** when its scope is genuinely specific to that product or family and the placement improves navigation.
5. **Contextual composition belongs in Local Model records where appropriate.** Reuse a canonical definition and model the product-specific occurrence rather than cloning the definition.
6. **00–09 numbering does not change type or relationship semantics.** A note in `04 Product Function` is not a Function merely because of its folder; its governed type and relationships remain authoritative.
7. **Evidence stays in the evidence layer.** Source records and research synthesis remain under `70_Research and Evidence`; product folders may link to them but should not become duplicate source repositories.
8. **Decisions and unresolved governance stay visible in `80_Decisions and Planning`.** `09 Product in Progress` is for product-context working material, not a replacement for vault-level governance.
9. **Promotion must preserve identity.** If product-context work matures into a reusable cross-product definition, move/reclassify the existing canonical note through a controlled step; do not create a second identity.
10. **Navigation artifacts are exception-based below the root.** A product or product-family context may receive a README/Base/Canvas only when it materially improves navigation.

### 00–09 to numbered-domain relationship

| Product-context area | Primary numbered-domain relationship | Placement rule |
|---|---|---|
| `00 Product Abstract` | `10_Products`, `50_Customer Needs`, `80_Decisions and Planning` | Product-specific framing may live in context; reusable product identity stays canonical in `10_Products`. |
| `00 Product Definition` | `10_Products` | Link to canonical product/family definitions; keep only product-context material locally when distinct. |
| `01 Product Use Case` | `40_Use and Operations` | Reuse canonical Use Cases when shared; product-specific scenarios may remain local if truly scoped to the product. |
| `02 Product Context` | `60_Stakeholders and Ecosystem`, `90_Definitions and Reusable Reference` | Link to actors, organizations, external systems, and reusable context definitions rather than copying them. |
| `03 Product Requirement` | `30_Product Capabilities` | Shared requirements remain canonical; product-specific requirements may be organized locally with explicit applicability. |
| `04 Product Function` | `30_Product Capabilities` | Shared Functions remain canonical and are referenced from the product context. |
| `05 Product Design` | `20_Product Architecture` and `30_Product Capabilities` | Product-specific realization may be local; reusable design definitions remain canonical in the appropriate numbered domain. |
| `06 Product Validation` | `30_Product Capabilities` | Reusable Verification/Procedure/Setup definitions remain canonical; product campaign context may be local. |
| `07 Product Assembly` | `20_Product Architecture` | Use reusable architecture definitions plus Local Model occurrences for contextual composition. |
| `09 Product in Progress` | `70_Research and Evidence`, `80_Decisions and Planning` | Temporary product-context synthesis only; mature evidence/governance content moves to its canonical numbered domain. |

This mapping is directional guidance for storage and navigation. It does not establish semantic relationships automatically.

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

## Primary navigation naming convention

For PosiBattery primary domain navigation, use the human-readable domain label without the numeric root prefix as the navigation stem:

- `README_<Domain>.md`
- `BASE_local_<Domain>.base`
- `BASE_all_<Domain>.base`
- `CANVAS_<Domain>.canvas`

Examples:

- folder `10_Products` → `README_Products.md`, `BASE_local_Products.base`, `BASE_all_Products.base`, `CANVAS_Products.canvas`
- folder `20_Product Architecture` → `README_Product Architecture.md`
- folder `70_Research and Evidence` → `README_Research and Evidence.md`

Do not use transitional forms such as `README - 20_Product Architecture.md` for active primary navigation.

This naming rule affects navigation filenames only. It does not rename the numbered root folders or change semantic identity.

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
3. use the authoritative numbered domains for canonical placement and the 00–09 pattern only as subordinate product-context navigation;
4. migrate older content only when it is already being reviewed;
5. use `09 Product in Progress` for unresolved synthesis rather than inventing weak element types;
6. run Workbench/Bootstrap release checks after structural changes;
7. keep Git history as the approval/recovery boundary.

A folder cleanup that breaks links or obscures provenance is worse than an imperfect but stable folder name.
