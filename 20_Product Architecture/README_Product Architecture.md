# Product Architecture

## Purpose

This is the canonical PosiBattery domain for product and platform realization: architectures, subsystems, assemblies, implementation Designs, Artifacts, Objects, interfaces, Ports, Item Flows, and other realization structure.

Folder placement supports navigation only. Element type, explicit relationships, applicability, source provenance, and Local Model records remain authoritative for engineering meaning.

See [[Canonical Vault Top-Level Taxonomy 0.1]] and [[PosiBattery Model Organization and Handoff]].

## What belongs here

Use this domain for stable architecture and realization content such as:

- product or platform architecture definitions;
- reusable subsystem and assembly definitions;
- implementation-oriented Designs;
- physical, electrical, firmware, software, and interface realization structure;
- reusable Objects, Ports, and Item Flows when architecture is their primary role;
- architecture-level diagrams or artifacts that define realization rather than evidence or planning.

Do not move a concept here solely because it is technical. Functions, requirements, metrics, states, failure modes, and verification intent belong primarily under [[README_Product Capabilities|Product Capabilities]] when capability is their primary role.

## Product-context relationship

A product-specific `05 Product Design` or `07 Product Assembly` workspace may organize local product context beneath a product or family when useful. Shared architecture definitions remain canonical here and should be linked into product contexts rather than duplicated.

Use Local Model occurrences for contextual composition where applicable.

## Vehicle architecture sets

- [[Industrial Truck Anatomy]] — abstract industrial-truck assembly and its reusable structural subsystems.
- [[GSE Vehicle Anatomy]] — abstract GSE vehicle assembly and its reusable structural subsystems.

These architecture sets are canonical here. Product-domain notes should link to them rather than duplicate their definitions.

## Current curated architecture view

[[CANVAS_Product Architecture]] now provides the first meaningful architecture map. It shows:

- [[Battery-Connected Product]] as the shared reusable root;
- [[Industrial Truck Anatomy]] and [[GSE Vehicle Anatomy]] as abstract reusable vehicle assemblies;
- representative structural parts from each assembly using only explicit `hasPart` relationships.

The canvas is intentionally selective. It does not show all 24 child parts, product-specific occurrences, Ports, Item Flows, or inferred connections. Use `BASE_all_Product Architecture.base` for the full recursive architecture inventory.

## Navigation



- `BASE_local_Product Architecture.base` — direct Markdown contents of this domain.
- `BASE_all_Product Architecture.base` — recursive Markdown contents of this domain.
- [[CANVAS_Product Architecture]] — curated architecture-domain map.

This domain is intentionally sparse today. Do not create architecture notes merely to populate the navigation set; add model content only when supported by product-development work or controlled migration.

## Related areas

- [[README_Products|Products]] — product and offering identity.
- [[README_Product Capabilities|Product Capabilities]] — functions, requirements, metrics, states, and verification.
- [[README_Definitions and Reusable Reference|Definitions and Reusable Reference]] — reusable external or cross-product concepts.
- [[README_Research and Evidence|Research and Evidence]] — evidence and research supporting architecture claims.
