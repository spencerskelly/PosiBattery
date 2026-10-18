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

## Folder review (2026-10-18)

Part of the vault-cleanup review: [[Vault Cleanup Findings 2026-10-18]] defines the finding IDs (F-xx) used below. Numbers come from a read-only audit of this folder on 2026-10-18.

### Snapshot

| Measure | Value |
| --- | --- |
| Markdown notes (this folder / incl. subfolders) | 163 / 197 |
| Typed model notes (incl. subfolders) | 196 (Object 180, Verification 8, Info 4, Item Flow 2, Port 2) |
| Status | Draft 196 of 196 |
| Notes with a `describedBy` link / notes linking a Document note anywhere | 6 / 4 of 196 |
| Tags | 129 distinct, 50 used once |
| Size | median 1,056 bytes; largest [[PosiCharge BMID End-to-End Traceability Demonstration]] (7 KB) |
| Non-markdown files | .base 2, .canvas 2 |

### Subfolders

| Folder | Notes | Abstract | Flags |
| --- | --- | --- | --- |
| [[README_Ground Support Equipment Architecture|Ground Support Equipment Architecture]] | 13 | 13 | source-linked 0/13 |
| [[README_Industrial Truck Architecture|Industrial Truck Architecture]] | 13 | 13 | source-linked 0/13 |
| PosiCharge BMID Validation | 6 | 0 | source-linked 0/6 |
| SOC and SOH Validation | 2 | 0 | source-linked 0/2; thin |

### Analysis

- Composition is 180 Object, 8 Verification, 4 Info, 2 Item Flow and 2 Port notes. `reuseScope` is set on 153 of 196, the most consistent use of a sparse property in the vault.
- Evidence: 6 of 196 notes have `describedBy` and 4 link any Source Document. [[Battery Current Measurement Circuit]] is `partOf` ten specific products; each product has its own source, but the circuit-level claim has none and is not marked as analyst inference (F-02).
- Subtype values outside the schema list (element-types 1.18: electrical, circuit, mechanical, software, firmware, part): 24 `component` and 19 `assembly` Objects, plus 2 Ports with a blank subtype (schema: proxy, full). The repo audit does not check this (F-05).
- Placement: the 8 Verification notes live in the two Validation subfolders, while the taxonomy table puts verification records under `30_Product Capabilities` (F-11).
- Hub notes: the truck anatomy notes are among the most linked in the vault ([[Truck Controller and CAN Bus]]: 83 inbound).
- The truck and GSE anatomy subfolders each hold 13 notes with parallel subsystems; only 1 of 13 notes in each uses `subtypeOf`, so shared subsystems are not expressed as generalizations.

### Key links

- [[Truck Controller and CAN Bus]] (abstract) — 83 inbound links
- [[Control Circuit]] (abstract) — 58 inbound links
- [[Truck Battery Compartment]] (abstract) — 57 inbound links
- [[Truck Controls and Display]] (abstract) — 36 inbound links
- [[Truck Drive and Brakes]] (abstract) — 33 inbound links
- [[Truck Mast]] (abstract) — 33 inbound links

### Improvement steps

1. **F-05** Decide the vocabulary for 43 `component`/`assembly` Objects: change the notes to schema values, or request a schema extension through the controlled release. Do not edit the schema file directly.
2. **F-05** Set `subtype` (proxy or full) on [[iBMID - Battery Interaction]] and [[iBMID - Charger Communication]].
3. **F-02** Link Source Documents through `describedBy` where a source exists, and mark remaining claims as analyst-derived.
4. **F-11** Decide whether Verification notes stay here or move to 30 (a move is a migration batch under the taxonomy rules).
5. **F-13** Add Base views: Objects by `reuseScope`, Objects missing `performs`/`hasDesign`, `partOf` fan-out per architecture note.
