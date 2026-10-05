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
