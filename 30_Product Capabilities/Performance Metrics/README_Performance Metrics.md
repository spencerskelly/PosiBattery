# Performance Metrics

## Purpose

This folder defines reusable comparison dimensions used to characterize products, Designs, Functions, and market offerings.

The current library is primarily a **comparison and evidence model**. It should not be assumed that every note is an atomic engineering property or a formal validation criterion.

## Navigation by metric semantics

### Quantitative engineering measures

Use these when the question is about a measurable magnitude, range, limit, or performance value.

Examples include:

- [[Metric - Nominal Voltage Range]]
- [[Metric - Capacity]]
- [[Metric - Output Power and Current]]
- [[Metric - Maximum Continuous Charge Current]]
- [[Metric - Charge Time]]
- [[Metric - Peak Efficiency]]
- [[Metric - Full-Cycle Efficiency]]
- [[Metric - Operating Temperature Range]]
- [[Metric - Voltage Measurement]]
- [[Metric - Current Measurement]]
- [[Metric - Detection Range and Accuracy]]
- [[Metric - Watering Interval]]

These are the strongest candidates for later decomposition into normalized reusable engineering Properties.

### Categorical or enumerated attributes

Use these when the comparison is a method, supported option, protocol, technology, certification, or named operating regime.

Examples include:

- [[Metric - Battery Identification Method]]
- [[Metric - Certifications and Standards]]
- [[Metric - Charge Regimes]]
- [[Metric - Charge Regimes Supported]]
- [[Metric - Chemistries Supported]]
- [[Metric - Detection Technology]]
- [[Metric - Equalize Scheduling]]
- [[Metric - Temperature Compensation Source]]
- [[Metric - Wired and Vehicle Interfaces]]
- [[Metric - Wireless Interfaces and Range]]

### Compound comparison summaries

Use these for broad market-comparison views, but do not treat them as single atomic properties without decomposition.

Examples include:

- [[Metric - BMS and Communication]]
- [[Metric - Communication and Remote Management]]
- [[Metric - Cycle Life and Warranty]]
- [[Metric - Onboard Accessories]]
- [[Metric - Operator Feedback]]
- [[Metric - Response Action]]
- [[Metric - Size and Mass]]
- [[Metric - Warranty and Price]]

Step 56 identified [[Metric - Warranty and Price]], [[Metric - Cycle Life and Warranty]], [[Metric - Size and Mass]], [[Metric - Output Power and Current]], and [[Metric - BMS and Communication]] as high-priority decomposition/clarification candidates if the model later formalizes engineering Properties or verification criteria.

## Cross-class reuse

A shared unit does not necessarily mean shared semantics.

For example, [[Metric - Nominal Voltage Range]] currently supports monitor, charger, and battery comparisons, but monitor supply/operating voltage, charger battery-voltage coverage, and battery nominal pack voltage are different engineering properties. Preserve the current comparison note until a deliberate property model is created.

## Traceability

Metric notes use `describes` to identify the reusable Products, Functions, or Designs they characterize.

- Step 54 found metric links on **21 of 103 concrete Functions**.
- Step 55 found metric links on **38 of 95 specific Designs**.

Metric coverage should be meaningful rather than universal.

## Evidence and validation boundary

Product notes remain authoritative for source URLs and product-specific values. Metric notes copy values for comparison.

Do not promote vendor-stated comparison values directly into Requirement acceptance limits. A formal validation criterion also needs a controlled method, operating conditions, tolerance, and pass/fail threshold.

## Navigation

- `BASE_all_Performance Metrics.base` — exhaustive metric inventory.
- `BASE_local_Performance Metrics.base` — direct contents of this folder.
- [[CANVAS_Product Capabilities]] — capability-level navigation connecting behavior, solutions, and measurements.

## Related areas

- [[README_Products|Products]] — entities being compared.
- [[README_Product Functions|Product Functions]] — capabilities that motivate measurement.
- [[README_Product Designs|Product Designs]] — implementation choices that affect measured outcomes.
- [[README_Research|Research]] — matrices and analyses applying the metrics.

## Maintenance

Create a metric note when a comparison dimension is reusable across more than one product or technology family. Keep metric definitions distinct from source evidence, product-specific results, and formal validation acceptance criteria.

## Folder review (2026-10-18)

Part of the vault-cleanup review: [[Vault Cleanup Findings 2026-10-18]] defines the finding IDs (F-xx) used below. Numbers come from a read-only audit of this folder on 2026-10-18.

### Snapshot

| Measure | Value |
| --- | --- |
| Markdown notes (this folder / incl. subfolders) | 56 / 56 |
| Typed model notes (incl. subfolders) | 55 (Info 55) |
| Status | Draft 55 of 55 |
| Notes with a `describedBy` link / notes linking a Document note anywhere | 0 / 0 of 55 |
| Tags | 6 distinct, 0 used once |
| Size | median 2,044 bytes; largest [[Metric - Nominal Voltage Range]] (5 KB) |
| Non-markdown files | .base 2, .canvas 1 |

### Analysis

- 55 Info notes, each with `describes`; only 6 distinct tags. Values per product are prose bullets under `## Notes`; unit or format and a metric code (for example CM08) are also prose.
- None of the schema's Info measure properties (`measureClass`, `valueType`, `unit`, `measurementMethod`) is set on any of the 318 Info notes in the vault (F-06).
- Each Metric copies values from product notes and states that the product note wins on disagreement, so edits must be made twice and can drift.
- Because values are text, a Base cannot sort, filter or compare products on a metric; comparison means reading notes one at a time. This blocks the stated goal of comparing products solidly.

### Key links

- [[Metric - Peak Efficiency]] — 11 inbound links
- [[Metric - Wireless Interfaces and Range]] — 11 inbound links
- [[Metric - BMS and Communication]] — 10 inbound links
- [[Metric - Temperature Sensing]] — 10 inbound links
- [[Metric - Electrolyte Level Sensing]] — 9 inbound links
- [[Metric - Nominal Voltage Range]] — 9 inbound links

### Improvement steps

1. **F-06** Set the four measure properties on all 55 Metrics now (in contract, no schema change).
2. **F-06** Decide where per-product values live: keep in Metric notes, generate them from product notes, or give each product-metric value its own record. Present as a decision with the Base consequences.
