# Products

## Purpose

This folder is the primary PosiBattery catalog for product categories, product families, variants, offerings, configurations, and portfolio records relevant to industrial motive power, charging, battery intelligence, fleet technology, material handling, and airport ground-support equipment.

See [[Canonical Vault Top-Level Taxonomy 0.1]] and [[Knowledge Base Backlog]].

## Product domains

- [[Industrial Traction Battery|Batteries]] — flooded lead-acid, valve-regulated lead-acid, and lithium-ion product families.
- [[Battery-Installed Device|Battery Accessories]] — monitoring and identification, BMS, connectors, watering, thermal management, protection, and telematics.
- [[Industrial Battery Charger|Chargers]] — industrial modular, light-duty, onboard, and wireless charging.
- [[Charger Accessory|Charger Accessories]] — cable management, connector accessories, controls/indicators, and mounting.
- [[Fleet Software and Platform|Fleet Software and Platforms]] — battery/charger management and truck telematics.
- [[Powered Industrial Truck|Forklifts]] — powered industrial trucks across Classes I–VII.
- [[Fuel Cell Power Unit|Fuel Cell Power Units]] — hydrogen fuel-cell power systems.
- [[Ground Support Equipment|Ground Support Equipment]] — baggage/tow tractors, belt loaders, cargo loaders, and pushback tractors.
- [[Vehicle Accessory|Vehicle Accessories]] — access control, cameras, operator assistance, displays, power interfaces, detection, and warnings.

## How to navigate this domain

Use the navigation layers for different questions:

- [[CANVAS_Products]] — curated orientation map of the major product domains and their architecture context.
- `BASE_all_Products.base` — recursive catalog for finding individual product records across the entire Products tree.
- `BASE_local_Products.base` — root-level view for only the direct contents of `10_Products`.
- Follow each abstract category/family note's specialization relationships to move from reusable product definitions to concrete offerings.

The Canvas is intentionally not exhaustive. Detailed categories and individual offerings belong in Bases and relationship navigation rather than being duplicated visually.

## Key information


- [[Battery-Connected Product]] — cross-cutting concept for products that connect to or interact with batteries.
- [[CANVAS_Products]] — visual product taxonomy and relationships.
- `BASE_all_Products.base` — view across all product records.
- `BASE_local_Products.base` — locally scoped product view.

## Product architecture context

Reusable vehicle anatomy is canonical under [[README_Product Architecture|Product Architecture]] rather than stored as product offerings:

- [[Industrial Truck Anatomy]] — reusable industrial-truck assembly and subsystem structure.
- [[GSE Vehicle Anatomy]] — reusable GSE assembly and subsystem structure.

These remain directly linkable from product notes and product research; their placement does not change their model identity or relationships.

## Related areas


- [[README_Organizations|Organizations]] — the companies that make, sell, distribute, or promote offerings.
- [[README_Source Documents|Source Documents]] — primary evidence for product claims.
- [[README_Product Functions|Product Functions]] — capabilities products perform.
- [[README_Product Designs|Product Designs]] — technical approaches embodied by products.
- [[README_Performance Metrics|Performance Metrics]] — comparable product attributes.
- [[README_Research|Research]] — matrices, landscapes, and product-catalog synthesis.

## Maintenance

Add a product record at the most specific supported category level. Preserve manufacturer evidence and link the record to its organization, source documents, relevant functions/designs, and applicable metrics.

## Folder review (2026-10-18)

Part of the vault-cleanup review: [[Vault Cleanup Findings 2026-10-18]] defines the finding IDs (F-xx) used below. Numbers come from a read-only audit of this folder on 2026-10-18.

### Snapshot

| Measure | Value |
| --- | --- |
| Markdown notes (this folder / incl. subfolders) | 2 / 571 |
| Typed model notes (incl. subfolders) | 570 (Object 570) |
| Status | Draft 570 of 570 |
| Notes with a `describedBy` link / notes linking a Document note anywhere | 321 / 291 of 570 |
| Tags | 106 distinct, 27 used once |
| Size | median 1,987 bytes; largest [[EnerSys Wi-iQ]] (27 KB) |
| Non-markdown files | .base 2, .canvas 1 |

### Subfolders

| Folder | Notes | Abstract | Flags |
| --- | --- | --- | --- |
| [[README_Batteries|Batteries]] | 92 | 5 | source-linked 86/87; 79 body-alias; 51 update-log |
| [[README_Battery Accessories|Battery Accessories]] | 107 | 14 | source-linked 52/93; 73 body-alias; 20 update-log; 11 off-schema subtype |
| [[README_Charger Accessories|Charger Accessories]] | 21 | 6 | source-linked 6/15; 9 body-alias; 2 update-log |
| [[README_Chargers|Chargers]] | 69 | 5 | source-linked 43/64; 61 body-alias; 13 update-log |
| [[README_Fleet Software and Platforms|Fleet Software and Platforms]] | 68 | 6 | source-linked 46/62; 39 body-alias; 7 update-log; 3 off-schema subtype |
| [[README_Forklifts|Forklifts]] | 58 | 8 | source-linked 43/50; 46 body-alias; 26 update-log |
| [[README_Ground Support Equipment|Ground Support Equipment]] | 21 | 5 | source-linked 0/16; 16 body-alias |
| [[README_Vehicle Accessories|Vehicle Accessories]] | 130 | 10 | source-linked 22/120; 83 body-alias; 7 update-log |

### Analysis

- All 570 model notes are `type: Object`. Category, family, variant and offering are told apart only by folder, `subtypeOf` chains and the 59 notes marked `abstract: true`; `productClass` (schema 1.18) is set on 10 of 570 (F-05).
- Every concrete offering has a maker link; the 59 notes without `madeBy` or `offeredBy` are all abstract category/family notes.
- Per-claim evidence sits inside `## Notes` as `Source … (T1), retrieved <date>, <URL>` bullets. Only 321 of 570 notes carry a `describedBy` link (F-02).
- Product notes are the stored source for the 55 Metric notes: each Metric copies product values and says the product note wins on disagreement, so every value exists twice (F-06).
- Existing Bases (`BASE_all_Products`, `BASE_offerings`) show file name, `subtypeOf`, `madeBy`, `offeredBy`, status and either folder or `offeredWith`. They do not show `abstract`, `productClass`, `describedBy`, tags or counts of performed Functions and Designs (F-13).
- The largest and most-linked notes are battery monitoring products ([[EnerSys Wi-iQ]], [[HOPPECKE trak collect]], [[PosiCharge PosiGuard]]); they hold the longest evidence logs.

### Key links

- [[EnerSys Wi-iQ]] — 110 inbound links
- [[HOPPECKE trak collect]] — 87 inbound links
- [[PosiCharge PosiGuard]] — 81 inbound links
- [[PosiCharge BMID]] (abstract) — 68 inbound links
- [[Power Designers PowerTrac 3]] — 63 inbound links
- [[Crown V-HFM3 Charger]] — 60 inbound links

### Improvement steps

1. **F-05** Backfill `productClass` across 560 Objects. Start with the 59 abstract notes, then use folder depth for the rest. This is what lets a Base group category, family, variant and offering.
2. **F-13** Add the Base views listed in the findings note (coverage audit, by maker, by class) before any content rework, so progress is measurable.
3. **F-02** Decide where evidence tier and retrieval date live (property, tag or prose), then apply across subfolders.
4. **F-03** and **F-04** Alias migration and Notes restructuring follow the layout decision; both are blocked on a decision (see findings note).
5. **F-16** Class IV to VII Forklifts, Protection and Disconnect Units and Thermal Management Devices hold one note each; keep as placeholders or merge into their parent.

## Product category and spec properties (2026-10-18)

Every Object under this folder carries `productCategory` (9 coarse values that mirror the category folders; `subtypeOf` remains the authority for the specific class, and `type`/`subtype` are unchanged). Category facet properties hold figures the note itself states, so products can be filtered and sorted without opening each note. Source text, citations and conflict notes stay in the note body; a facet is left out where a note records a source conflict. The contract is in `99_System/03_Schemas/element-types.yaml` (schema 1.19) and is checked by `99_System/09_Tools/check-product-facets.py`.

| productCategory | Objects | With facets | Facet properties |
| --- | --- | --- | --- |
| battery | 92 | 87 | chemistry, voltageClassV, voltageMinV/MaxV, capacityAhMin/Max, energyKwhMin/Max, ratedCycles, chargeProfile |
| charger | 69 | 43 | powerKwMin/Max, outputVoltageMinV/MaxV, outputCurrentMaxA, inputPhases, supportedChemistries, chargeProfile, moduleCountMin/Max, modulePowerKw, airGapMmMin/Max, efficiencyPct |
| industrial-truck | 58 | 40 | ratedLoadKgMin/Max, systemVoltageV, powerSource |
| battery-accessory | 108 | 23 | commInterfaces |
| vehicle-accessory | 130 | 8 | commInterfaces, detectionRangeM |
| fleet-software | 67 | 9 | commInterfaces |
| charger-accessory, gse, fuel-cell | 21, 21, 3 | 1, 1, 0 | commInterfaces where stated |

- `BASE_product_specs.base` has views for Batteries, Chargers, Wireless chargers, Industrial trucks, Connected products, Proximity detection range and a Category overview. It was written without Obsidian available here, so open it once to confirm the views render.
- Empty facets mean the note does not state the figure, not that the product lacks it.
- `commInterfaces` is named to avoid the governed Port relationship field `interfaces`.


## Company property (2026-10-18)

- `company` is a link to an organization note, on every concrete product Object (509 notes), so any Base can group or filter products by an identifiable organization without opening notes.
- It is a separation aid, not a claim about who built the product. Where `madeBy` exists, `company` equals its first link (446 notes). Where it does not, `company` is the brand owner or the organization named in the note: 25 by product brand prefix (Crown to Crown Equipment, Deka to East Penn Manufacturing, Cat to Mitsubishi Logisnext, and so on), 33 by an organization-name prefix, 3 set by hand.
- `madeBy`, `offers` and `subsidiaryOf` are unchanged. Brand-versus-legal-entity questions stay open there: Linde, STILL and Rocla are described as brands, PosiCharge and Power Designers as parts of Ampure, and no source in the vault names a separate legal manufacturer for them.
- New organization notes: [[Purkeys]] and [[SEEN Safety]], each with the product's `madeBy` link added.
- Not given a company: abstract class notes, the generic classes Class IV Internal Combustion Cushion Tire Truck, Class VI Tractor and Class VII Rough Terrain Forklift, and Battery Thermal Management Device (several vendors named, no single owner).
- Judgement call: Crown Battery EVOLUTION Series is set to Power Designers because the note says it repeats the REVOLUTION specification and names the PowerTrac; the "Crown Battery" name is not matched to any organization note (C33).
