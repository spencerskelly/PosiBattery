# Product Capabilities

## Purpose

This is the canonical PosiBattery domain for reusable product behavior, solution concepts, and comparison dimensions.

The domain should be navigated as a traceable chain rather than as three unrelated inventories:

**customer / operational intent → Function → Design → Product → Metric / evidence**

See [[Canonical Vault Top-Level Taxonomy 0.1]] and [[PosiBattery Model Organization and Handoff]].

## Primary navigation

### 1. Behavioral goals — what must be accomplished

Start with [[README_Product Functions|Product Functions]] when the question is *what should the product, system, or subsystem do?*

The six modeled goal branches are the primary behavioral navigation:

- [[Deliver Energy to Vehicles]]
- [[Keep Equipment Working in Its Environment]]
- [[Know and Protect Battery Condition]]
- [[Manage Fleet Use and Data]]
- [[Protect People and Equipment Near Vehicles]]
- [[Support the Operator]]

Each goal decomposes into reusable general Function families and then source-backed concrete Functions.

### 2. Solution families — how the behavior can be realized

Use [[README_Product Designs|Product Designs]] when the question is *what reusable technical approach can provide that behavior?*

Design navigation follows the modeled general Design hierarchy rather than arbitrary file-count grouping. The major reusable families cover battery construction and integration, charging/power conversion, sensing, communications/data, operator/safety devices, vehicle control/drive, energy interfaces, and packaging/mounting.

### 3. Comparison dimensions — how alternatives differ

Use [[README_Performance Metrics|Performance Metrics]] when the question is *how do we characterize or compare products, Functions, or Designs?*

Metrics currently fall into three practical navigation classes:

- **quantitative engineering measures** — voltage, current, power, capacity, efficiency, temperature, time, range, accuracy, mass, etc.;
- **categorical / enumerated attributes** — chemistry, interfaces, detection technology, charging regime, certification, identification method, etc.;
- **compound comparison summaries** — broader market-comparison dimensions such as BMS and Communication, Operator Feedback, or Warranty and Price.

These categories are navigation aids only. Step 56 identified that compound comparison metrics should not automatically be treated as atomic engineering properties or validation criteria.

## Traceability paths

Use these relationships to move through the capability model:

- **Customer Need / Use Case → Function:** `realizedBy`
- **Function → Customer Need / Use Case:** `realizes`
- **Product → Function:** inverse of Function `performedBy`
- **Function → Design:** `dependsOn`
- **Design → Function:** `dependencyOf`
- **Product → Design:** inverse of Design `designOf`
- **Function / Design / Product class → Metric:** inverse of Metric `describes`
- **Metric → Function / Design / Product class:** `describes`

Not every element is expected to carry every relationship. Missing links should be added only when supported by evidence or a deliberate engineering decision.

## Navigation assets

- `BASE_local_Product Capabilities.base` — direct Markdown contents of this domain.
- `BASE_all_Product Capabilities.base` — exhaustive recursive inventory across this domain.
- [[CANVAS_Product Capabilities]] — curated traceability-oriented map.
- [[Function and Design Levels]] — complete Function hierarchy and Design-level reference.

Use the Bases for exhaustive discovery. Use README and Canvas navigation for semantic exploration.

## Related domains

- [[README_Customer Needs|Customer Needs]] — problem/intent hypotheses that Functions may realize.
- [[README_Products|Products]] — observed offerings that perform Functions and embody Designs.
- [[README_Research|Research]] — evidence, comparison work, gap analysis, and source-backed interpretation.
- [[README_Use and Operations|Use and Operations]] — operational modeling area; currently not yet populated with detailed operational Use Cases.

## Scope guidance

Use this domain for stable reusable capability definitions and measurable/comparable behavior. Physical architecture and realization content belongs under [[README_Product Architecture|Product Architecture]] when that is its primary role.

Folder placement is navigation, not ontology. Do not create parallel semantic taxonomies solely to reduce file counts, and do not move Product Designs or Performance Metrics solely for visual consistency.

## Folder review (2026-10-18)

Part of the vault-cleanup review: [[Vault Cleanup Findings 2026-10-18]] defines the finding IDs (F-xx) used below. Numbers come from a read-only audit of this folder on 2026-10-18.

### Snapshot

| Measure | Value |
| --- | --- |
| Markdown notes (this folder / incl. subfolders) | 9 / 506 |
| Typed model notes (incl. subfolders) | 502 (Design 245, Function 159, Info 56, Requirement 42) |
| Status | Draft 501 of 502; other 1 |
| Notes with a `describedBy` link / notes linking a Document note anywhere | 94 / 95 of 502 |
| Tags | 161 distinct, 68 used once |
| Size | median 1,403 bytes; largest [[Measure Battery Temperature]] (11 KB) |
| Non-markdown files | .base 8, .canvas 4 |

### Subfolders

| Folder | Notes | Abstract | Flags |
| --- | --- | --- | --- |
| [[README_California Regulatory Requirements|California Regulatory Requirements]] | 19 | 0 | source-linked 0/19; 5 update-log |
| [[README_Fire and Safety Code Requirements|Fire and Safety Code Requirements]] | 15 | 0 | source-linked 0/15 |
| [[README_Performance Metrics|Performance Metrics]] | 55 | 0 | source-linked 0/55; 40 body-alias |
| [[README_Product Designs|Product Designs]] | 246 | 1 | source-linked 62/246; 4 body-alias; 5 update-log |
| [[README_Product Functions|Product Functions]] | 159 | 0 | source-linked 32/159; 1 body-alias; 8 update-log |

### Analysis

- Composition is 245 Design, 159 Function, 56 Info and 42 Requirement notes. Eight notes sit directly in the domain root (BMID, PosiGuard and state-of-charge/health notes) outside the Functions, Designs and Metrics subfolders.
- Functions: 131 of 159 `realizes` a need, 139 have a performer, 47 have `realizedBy`; 28 Functions realize no need.
- Designs: 220 of 246 have `designOf`; 49 `realize` a Function; 62 have `describedBy`.
- Requirements: all 42 use `appliesTo`; 34 are regulatory or code requirements in two subfolders; only 6 notes in the domain use `satisfies` (F-13).
- The folder [[README_California Regulatory Requirements|California Regulatory Requirements]] also holds Washington (3), Oregon (2) and New Mexico (1) notes and 5 derived Charging Energy Reporting notes (F-11).
- Metrics are Info notes whose values are prose bullets; none sets the schema's measure properties (F-06).

### Key links

- [[Log Battery Events and Usage]] — 64 inbound links
- [[Measure Battery Temperature]] — 58 inbound links
- [[Alert on Abnormal Condition]] — 55 inbound links
- [[Sense Electrolyte Level]] — 54 inbound links
- [[Charge Battery Fast]] — 50 inbound links
- [[Transmit Battery Data Wirelessly]] — 49 inbound links

### Improvement steps

1. **F-06** Set `measureClass`, `valueType`, `unit` and `measurementMethod` on the 55 Metric notes; these properties already exist in the schema.
2. **F-11** Decide a folder name for the regulatory subfolder that matches its content (rename is navigation-only but needs an inventory and link check).
3. **F-13** Add Base views: Functions with no `realizes`, Designs with no `realizes`, Requirements with no satisfier.
4. **F-12** Review the 161 distinct tags (68 used once) in this domain.
