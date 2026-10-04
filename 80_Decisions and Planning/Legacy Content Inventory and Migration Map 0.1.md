---
element_type: plan
status: active
scope:
  kind: cross-product
created: 2026-10-04
related_backlog:
  - [[80_Decisions and Planning/Knowledge Base Backlog#KB-001]]
  - [[80_Decisions and Planning/Knowledge Base Backlog#KB-002]]
  - [[80_Decisions and Planning/Knowledge Base Backlog#KB-006]]
---

# Legacy Content Inventory and Migration Map 0.1

## Purpose

This document records the first-pass inventory of legacy PosiBattery content and the proposed migration from the existing top-level folders into the canonical product-first taxonomy. It is a planning artifact only. It does not authorize a file move, rename, merge, edit, or deletion.

All legacy locations remain authoritative until the affected batch has been approved, migrated, checked, and recorded as complete.

## Migration controls

- Preserve every existing note, Base, Canvas, and relationship unless a later approved action explicitly changes it.
- Do not silently resolve conflicting classifications, duplicate identities, or uncertain scope. Record them below and create follow-up work.
- Migrate coherent batches only after the relevant notes, links, navigation, and validation approach have been reviewed.
- Treat folders as canonical storage locations, not the complete meaning of an element. Element type, scope, evidence, and typed relationships provide the model semantics.
- Update links, navigation, and relevant Bases/Canvases as part of the same controlled migration batch.
- Run applicable name and dependency checks after every batch.

## Target taxonomy

| Target folder | Role |
| --- | --- |
| `10_Products` | Product and offering identity |
| `20_Product Architecture` | Product/platform realization and implementation |
| `30_Product Capabilities` | Functions, requirements, properties, metrics, states, failure modes, verification |
| `40_Use and Operations` | Use cases, workflows, procedures, setups, environments, operational issues |
| `50_Customer Needs` | Customer/user outcomes, needs, pain points, and constraints |
| `60_Stakeholders and Ecosystem` | Actors, organizations, roles, suppliers, partners, competitors, regulators, and standards bodies |
| `70_Research and Evidence` | Source records, research synthesis, evidence/provenance |
| `80_Decisions and Planning` | Backlog, decisions, assumptions, conflicts, model quality, and planning |
| `90_Definitions and Reusable Reference` | Reusable domain concepts and controlled vocabulary |
| `99_System` | Vault methodology, schemas, templates, scripts, and administration |

## Legacy-folder map

| Legacy location | Inventory summary | Proposed target | Migration disposition |
| --- | --- | --- | --- |
| `Customer Actors` | 11 actor/role notes, Bases, Canvas, README | `60_Stakeholders and Ecosystem/Actors/` | Direct candidate; migrate as one controlled batch with views |
| `Customer Needs` | 22 need notes, Bases, Canvas, README | `50_Customer Needs/` | Direct candidate; migrate as one controlled batch with views |
| `Products` | Product categories, type notes, named offerings, Bases, Canvas, README | `10_Products/` | Direct structure candidate; retain category branches after distinguishing category/type/family/offering |
| `Product Functions` | Broad functional model, Bases, Canvas, README | `30_Product Capabilities/Functions/` | Direct candidate; retain function hierarchy and formalize decomposition/specialization links |
| `Performance Metrics` | Metric definitions and comparison criteria, Bases, Canvas, README | `30_Product Capabilities/Performance Metrics/` | Classification review required for metrics versus comparison criteria |
| `Product Designs` | Large mixed library of designs, technical patterns, capability-like notes, Bases, Canvas, README | `20_Product Architecture/`, `30_Product Capabilities/`, and `90_Definitions and Reusable Reference/` | Classification-first; do not mass-move |
| `Organizations` | Organization entities, archetypes, ledgers, vocabulary, offering indexes, Bases, Canvas, synthesis notes | Primarily `60_Stakeholders and Ecosystem/Organizations/` | Split by artifact class; do not mass-move |
| `Research` | Synthesis, maps/registers, planning, governance/audits, business analysis, Bases, Canvas, README | `70_Research and Evidence/` and `80_Decisions and Planning/` | Split by artifact class; reconcile planning records |
| `Source Documents` | Source-record notes, Bases, Canvas, README | `70_Research and Evidence/Source Records/` | Direct candidate |
| `Downloads` | Public-source binary PDFs, including duplicate files | No canonical destination; temporary ingestion area | Process/cleanup candidate only; match sources and preserve provenance before approved deletion batches |
| `Definitions` | Note-layout guidance, author guidance, EA guidance, property dictionary | Mostly `99_System/` | Split system/meta-model material from true reusable domain definitions |
| `Definitions/Properties` | Controlled property and relationship vocabulary | `99_System/` | Retain as meta-model controls pending relationship-vocabulary review |

## Direct-migration candidates

These areas are structurally coherent enough to plan as early migration batches, subject to link/view validation:

| Batch | Legacy source | Proposed destination | Pre-migration checks |
| --- | --- | --- | --- |
| M-01 | `Customer Actors` | `60_Stakeholders and Ecosystem/Actors/` | Confirm actor naming, actor-to-need links, Canvas/Base path handling |
| M-02 | `Customer Needs` | `50_Customer Needs/` | Confirm need naming and links to actors/functions/products |
| M-03 | `Product Functions` | `30_Product Capabilities/Functions/` | Confirm functional hierarchy and dependency links |
| M-04 | `Performance Metrics` | `30_Product Capabilities/Performance Metrics/` | Separate measurable metrics from categorical comparison criteria |
| M-05 | `Source Documents` | `70_Research and Evidence/Source Records/` | Confirm source-record naming, outbound evidence links, and view updates |

## Classification-first candidates

### Products

`Products` is a useful product hierarchy but mixes generalized product types, category branches, product-family concepts, and named offerings. Preserve the category branches under `10_Products/` while applying a later identity distinction:

- `product_category`
- `product_type`
- `product_family`
- `product_variant`
- `specific_offering`

Examples observed include industrial traction batteries and industrial battery chargers as type-level records, plus battery, charger, forklift, ground-support-equipment, fuel-cell, software/platform, and accessory branches.

### Product Designs

`Product Designs` is not a single artifact type. Each note must be classified by scope and semantic role before moving:

| Candidate class | Proposed target | Examples |
| --- | --- | --- |
| Product/platform architecture or implementation | `20_Product Architecture/` | Battery onboard charger, charger power stage, vehicle energy interface, product-specific BMS design |
| Capability/behavior framed as a design | `30_Product Capabilities/` | Hibernation mode, extended watering interval, regenerative braking, multi-voltage output |
| Reusable technical concept or reference pattern | `90_Definitions and Reusable Reference/` | CAN, Bluetooth, Wi-Fi, LoRa, current-sensing approaches, silicon-carbide power stage |
| Scope-unconfirmed hybrid | Decision after note-level review | Integrated BMS, cloud portal integration, wireless-interface design, current-sensing design |

A generic technology name does not establish that the note describes a PosiCharge-specific implementation. Treat scope as unconfirmed unless the note metadata, body, or relationships establish it.

### Organizations

`Organizations` contains several incompatible artifact classes:

| Artifact class | Proposed target | Notes |
| --- | --- | --- |
| Canonical organizations | `60_Stakeholders and Ecosystem/Organizations/` | Companies, institutions, suppliers, OEMs, partners, competitors, regulators |
| Organization/market archetypes | `60_Stakeholders and Ecosystem/Organization Types/` or `90_Definitions and Reusable Reference/` | Battery maker, truck OEM, dealer/distributor, monitor maker; determine whether modeled stakeholder type or reusable taxonomy |
| Relationship controls | `99_System/` | Business relationship vocabulary and related controlled semantics |
| Relationship ledger and offering indexes | `80_Decisions and Planning/Model Views and Registers/` initially | Preserve as controlled analytical registers; later determine generated-view strategy |
| Industry/portfolio synthesis | `70_Research and Evidence/Research Synthesis/Ecosystem Analysis/` | Industrial supply/private-label analysis and product-offering synthesis |

### Research

`Research` mixes evidence synthesis with planning and governance. Proposed classification:

| Research class | Proposed target | Examples |
| --- | --- | --- |
| External research synthesis | `70_Research and Evidence/Research Synthesis/` | Battery/charger/monitor matrices, charge-profile comparisons, competitor landscapes, catalog reviews |
| Business and portfolio analysis | `70_Research and Evidence/Research Synthesis/Business and Portfolio Analysis/` | PosiCharge/Ampure/Power Designers portfolio and market analysis |
| Market/customer analysis | `70_Research and Evidence/Research Synthesis/Market and Customer Analysis/` | Market segments and jobs-to-be-done; link to canonical needs and stakeholders |
| Ecosystem analysis | `70_Research and Evidence/Research Synthesis/Ecosystem Analysis/` | Competitive/partner and supply-chain/overlap analysis |
| Source provenance/evidence management | `70_Research and Evidence/Provenance and Evidence Management/` | Evidence conventions, public evidence registers, source context |
| Maps, registers, and dependency analysis | `80_Decisions and Planning/Model Views and Registers/` initially | Function/design maps, product-to-need maps, connection/dependency registers |
| Planning, backlog, objectives | `80_Decisions and Planning/` | Investigation backlog, coverage plan, document wishlist, objectives |
| Governance, audits, and decisions | `80_Decisions and Planning/Model Quality and Decisions/` | Link audit, note-reuse audit, change/decision tracker, conflicts/open questions |

The legacy `Research/Knowledge Base Next Steps.md` overlaps the canonical `80_Decisions and Planning/Knowledge Base Backlog.md`. Reconcile its active items, historical value, and unresolved work before archiving, replacing, or deleting it.

### Definitions and properties

The legacy `Definitions` folder is overloaded. Existing observed content is largely methodology/meta-model guidance rather than reusable domain knowledge:

| Legacy content | Proposed target | Decision |
| --- | --- | --- |
| Note layout, author-code changes, EA source-section guidance | `99_System/10_Docs/` or related system administration | Treat as system documentation |
| Property dictionary and individual property notes | `99_System/` | Retain as meta-model controls pending relationship-vocabulary review |
| Future domain definitions | `90_Definitions and Reusable Reference/` | Only domain/reusable concepts belong here |

## Evidence and download controls

`Source Documents` is the canonical source-record candidate. `Downloads` is not a knowledge-model domain and should remain a temporary ingestion area until processed.

Before any PDF deletion:

1. Match the binary to an existing or newly created source-record note.
2. Capture decision-relevant information in source-linked Markdown and canonical element notes.
3. Preserve source URL, document title/identity, revision/date when available, access date, page/section references, unresolved questions, and omitted-but-potentially-useful data.
4. Identify duplicate binaries and records without recoverable source URLs.
5. Request a separate approved deletion batch.

Known duplicate groups identified by matching file SHA include the Hyster solutions brochure, `133294183726805278`, Toyota Assist brochure, GNB MP overview, `d0631ac8-a3f8-4b21-8640-bf6f41154ae8`, and trak collect brochure. Duplicates are not authorized for deletion by this map.

## Identified conflicts and open decisions

| ID | Topic | Current ambiguity/conflict | Required resolution |
| --- | --- | --- | --- |
| MIG-001 | Definition boundary | Legacy `Definitions` is mostly meta-model/system content, while new `90_...` is intended for reusable domain concepts | Approve system/domain split and define criteria |
| MIG-002 | Product-design scope | Design library mixes architecture, capabilities, and reusable technical patterns | Define metadata and note-level classification process |
| MIG-003 | Organization archetypes | Some organization notes describe market roles rather than real organizations | Decide stakeholder-type versus reusable-taxonomy placement |
| MIG-004 | Metric semantics | Existing metric notes mix measured quantities, categorical attributes, and commercial comparison fields | Define metric/property/comparison-criterion types |
| MIG-005 | Research planning overlap | Multiple legacy planning/backlog files overlap the new canonical backlog | Reconcile work items and retain historical context |
| MIG-006 | Relationship assets | Vocabulary, ledger, and related registers are valuable but span system control and analytical views | Define source of truth, generated-view policy, and canonical location |
| MIG-007 | Download retention | Source PDFs include duplicates and may lack stable URLs or source-record notes | Build a controlled extraction/retention/deletion queue |
| MIG-008 | View artifacts | Bases and Canvases have path-sensitive links/views | Establish update and validation method before moves |

## Recommended migration sequence

1. Define common element metadata and relationship usage rules before moving classification-sensitive content.
2. Establish the `30_Product Capabilities` subfolder structure and metadata distinctions for functions, metrics, properties, comparison criteria, requirements, states, failure modes, and verification.
3. Reconcile the planning/backlog records so `80_Decisions and Planning` has one visible current backlog with preserved legacy context.
4. Migrate the direct, low-ambiguity domains in small batches: actors, needs, functions, source records, then metrics.
5. Review and classify product hierarchy, organization archetypes, product designs, research artifacts, and definitions before moving them.
6. Process downloads source by source; authorize binary cleanup only after extraction and provenance checks.
7. Update and validate Bases, Canvases, links, names, and dependency checks after every batch.

## Work added to backlog

This map identifies follow-on work that should remain visible in the canonical backlog:

- Create the element metadata and type-extension standard.
- Publish relationship-vocabulary usage and directionality guidance.
- Define metric/property/comparison-criterion semantics.
- Reconcile legacy planning and backlog files.
- Create a Base/Canvas migration validation procedure.
- Create a controlled source-document and download processing queue.
- Define an organization archetype taxonomy.
- Classify the product-design library at note level.

## Change history

| Version | Date | Change |
| --- | --- | --- |
| 0.1 | 2026-10-04 | First-pass legacy content inventory and non-destructive migration map |
