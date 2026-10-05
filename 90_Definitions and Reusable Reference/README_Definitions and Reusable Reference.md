# Definitions and Reusable Reference

## Purpose

This is the canonical PosiBattery domain for cross-product concepts and controlled vocabulary: definitions, technologies, protocols, properties, units, abbreviations, reference architectures, taxonomies, and other reusable concepts that should not be duplicated inside individual products.

See [[Canonical Vault Top-Level Taxonomy 0.1]] and [[PosiBattery Model Organization and Handoff]].

## Current reusable-reference areas

- [[README_Definitions|Definitions]] — shared vocabulary, note conventions, identifier guidance, and relationship/property semantics.
- [[README_Properties|Properties]] — semantic guide for identity, hierarchy, interaction, traceability, lifecycle, and temporary relationship fields.
- [[Property Dictionary]] — exhaustive tabular inventory of the controlled Property definitions.

The vault does not currently need empty Technologies, Protocols, Units, or similar folders. Create those areas only when enough real reusable content exists to justify distinct navigation.

## Placement guidance

Use this domain when a concept is reusable across products or contexts and its primary role is reference/definition rather than product identity, architecture realization, capability behavior, or evidence.

Examples that may belong here as the model grows include:

- communication protocols and externally defined interfaces;
- technologies used by multiple products;
- units and controlled value vocabularies;
- reusable taxonomies and classification concepts;
- shared reference architectures;
- abbreviations and terminology.

A concept's presence here does not make it a model relationship. Explicit relationships remain governed by the active schemas and relationship vocabulary.

## Navigation

Start with [[README_Definitions|Definitions]] for authoring conventions or [[README_Properties|Properties]] when choosing/interpreting metadata and relationship fields. Use [[Property Dictionary]] when you need the complete property inventory rather than semantic guidance.

- `BASE_local_Definitions and Reusable Reference.base` — direct Markdown contents of this root domain; currently intentionally sparse because reusable content lives below `Definitions`.
- `BASE_all_Definitions and Reusable Reference.base` — recursive inventory across all current reusable-reference material.
- [[CANVAS_Definitions and Reusable Reference]] — curated map of the active reusable-reference area and its governance/evidence boundaries.

## Governance boundary

Methodology, schemas, templates, scripts, and runtime administration belong under `99_System`. This domain contains reusable knowledge used by the model; it should not become a duplicate system-governance store.

The existing `Definitions` and `Definitions/Properties` folders remain migration candidates for later semantic review. Step 21 changes navigation only and does not reclassify those notes.

## Related areas

- [[README_Product Architecture|Product Architecture]] — reusable realization concepts when architecture is their primary role.
- [[README_Product Capabilities|Product Capabilities]] — reusable Functions, requirements, metrics, and behavior.
- [[README_Research and Evidence|Research and Evidence]] — evidence supporting reusable-reference claims.
