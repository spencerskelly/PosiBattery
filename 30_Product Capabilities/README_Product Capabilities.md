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
