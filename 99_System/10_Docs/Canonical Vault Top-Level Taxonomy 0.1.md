---
element_type: document
status: active
scope:
  kind: cross-product
created: 2026-10-04
related_backlog:
  - [[80_Decisions and Planning/Knowledge Base Backlog#KB-001]]
---

# Canonical Vault Top-Level Taxonomy 0.1

## Purpose

This document defines the target top-level information architecture for the PosiBattery vault. It provides a product-first numbered order for predictable alphabetical navigation while preserving reusable concepts, evidence traceability, and relationship-first modeling.

This is a target taxonomy, not an authorization to move, rename, or delete existing content. Content migration requires an inventory, an approved mapping, controlled batches, and integrity checks.

## Governing principles

- Folder placement gives a note one canonical storage location; it does not fully define meaning.
- Element type, scope, and explicit typed relationships carry the primary model semantics.
- One stable identity has one canonical note. Do not duplicate an element just because it applies to several products or contexts.
- Create a new note when public evidence introduces a distinct product, actor, need, function, design, organization, source, or reusable concept.
- Add information to the existing canonical note when evidence concerns the same identity.
- Preserve conflicting evidence and unresolved classification decisions. Record the conflict; do not silently select, merge, or delete alternatives.
- Separate evidence from model claims. Evidence supports, contradicts, or qualifies claims and relationships; it is not silently converted into fact.
- Keep the model useful at multiple levels of abstraction: business, stakeholder, use, product, system, architecture, component, and implementation.

## Canonical top-level folders

| Folder | Primary purpose | Canonical content examples |
| --- | --- | --- |
| `10_Products` | Product and offering identity | Products, product families, variants, offerings, configurations, portfolio records |
| `20_Product Architecture` | Product and platform realization | Architectures, designs, subsystems, artifacts, components, interfaces, ports, implementation flows |
| `30_Product Capabilities` | Product intent and measurable behavior | Functions, requirements, properties, metrics, states, failure modes, verification records |
| `40_Use and Operations` | Deployment and operational context | Use cases, workflows, procedures, setups, operating environments, operational issues |
| `50_Customer Needs` | Outcomes, needs, and constraints | Needs, desired outcomes, pain points, user problems, demand signals, customer constraints |
| `60_Stakeholders and Ecosystem` | Parties and external context | Customer actors, users, operators, buyers, maintainers, organizations, suppliers, partners, competitors, regulators, standards bodies |
| `70_Research and Evidence` | Source provenance and research synthesis | Source records, research notes, market analysis, evidence registers, external comparisons, standards research |
| `80_Decisions and Planning` | Work control and model governance | Backlog, decisions, assumptions, open questions, conflicts, model-quality findings, plans |
| `90_Definitions and Reusable Reference` | Cross-product concepts and controlled vocabulary | Definitions, technologies, protocols, units, abbreviations, shared reference architectures, taxonomies |
| `99_System` | Vault methodology and administration | Schemas, templates, scripts, checks, system documentation, tools, AI instructions |

## Specific and reusable elements

A note is stored according to its primary scope. Its relevance elsewhere is expressed through relationships and navigation, not duplicate copies.

| Scope kind | Canonical placement rule | Example |
| --- | --- | --- |
| `product-specific` | Store with the product, architecture, capability, or use context in which the element is specific | A BMS architecture unique to one product variant |
| `product-family` | Store with the product family or its shared architecture/capabilities | A common charger platform used by multiple variants in one product family |
| `platform-shared` | Store under architecture or capabilities when it is a managed internal platform spanning product families | A common firmware-update service shared by multiple product families |
| `cross-product` | Store in the domain that best expresses its role; link it to every applicable product/context | A fleet-availability need relevant to several products |
| `external-reference` | Store reusable public concepts under `90_Definitions and Reusable Reference`; store the supporting source and analysis under `70_Research and Evidence` | CAN-FD as a concept, with manufacturer/standards research notes as its evidence |

## Evidence separation

`70_Research and Evidence` retains source records and research synthesis. Each source-derived claim should preserve sufficient provenance to recover and assess the original material, including the source URL, document identity or revision where available, access date, and relevant page or section when applicable.

`90_Definitions and Reusable Reference` contains concise canonical notes for reusable concepts. These notes should link to the research and source records that support, contradict, or qualify their contents. They should not become unbounded source-extraction notebooks.

Temporary downloaded source artifacts may be deleted after their decision-relevant content, provenance, unresolved questions, and omitted-but-potentially-useful information have been captured in vault-native notes. If a source is private, unstable, access-controlled, or otherwise at risk of loss, record that condition before deletion.

## Relationship-first model

Typed relationships should express the engineering and business meaning that folders cannot. The expected traceability pattern is:

```text
Stakeholder → Need → Use / Operation → Requirement → Function → Architecture / Design → Product → Metric / Verification
```

The current relationship schema remains the source of truth for available relationship terms. Relationship-vocabulary work must document directionality, allowed endpoint types, applicability, evidence treatment, and ambiguous or prohibited terms before broad structural migration.

## Migration rules

1. Inventory existing content before moving files.
2. Map every existing content item to a proposed target location or explicitly mark it as ambiguous, duplicated, obsolete, or conflicting.
3. Do not silently delete files, merge notes, or choose between conflicting classifications.
4. Migrate small, coherent batches; record exceptions and follow-up work in the backlog.
5. Update navigation artifacts and canonical links as part of each migration batch.
6. Run applicable name and dependency checks after each batch and record failures for resolution.
7. Preserve source provenance and existing model relationships through every move.

## Deferred design decisions

The following are intentionally deferred until the related backlog work is completed:

- Exact subfolder structures within each top-level folder.
- Common frontmatter contract and type-specific metadata extensions.
- Relationship lifecycle, confidence, evidence, and applicability attributes.
- Final naming convention for folder README/index notes and model views.
- Detailed criteria for `platform-shared` versus `cross-product` scope.
- Automated migration, validation, and reporting mechanisms.

## Change history

| Version | Date | Change |
| --- | --- | --- |
| 0.1 | 2026-10-04 | Initial product-first numbered taxonomy, evidence separation, scope rules, and non-destructive migration principles |
