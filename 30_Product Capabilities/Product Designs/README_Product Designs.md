# Product Designs

## Purpose

This folder contains reusable technical solution concepts—the implementation choices that can support Product Functions. Product Design notes record reusable patterns observed across products rather than single-product claims.

## Hierarchy-backed navigation

Use the modeled general Design hierarchy as the primary navigation structure. Specific Designs remain reusable leaves beneath these families.

### Battery construction and integration

- [[Lead-Acid Battery Construction Design]]
- [[Battery Integrated Feature Design]]
- [[Electrolyte Level Sensing Design]]
- [[Battery Temperature Reporting to Charger]]
- [[Battery Temperature Measurement Design]]
- [[Battery Sensor Mounting Design]]

### Charging and energy interfaces

- [[Charger Power Stage Design]]
- [[Charger Operator Interface Design]]
- [[Vehicle Energy Interface Design]]
- [[Fuel Cell Power Design]]

### Battery construction and maintenance

- [[Air Injection Electrolyte Circulation]]
- [[Battery Cell Watering Design]]

### Protection and control

- [[Deep Discharge Protection Design]]

### Sensing, state, and data

- [[Battery Abuse Cycle Analytics]]
- [[Battery Event and Usage Logging Design]]
- [[Cloud Battery Data Upload Design]]
- [[Battery Replacement Timing Prediction Design]]
- [[Cell Failure Diagnostic Design]]
- [[Current Sensing Design]]
- [[Missed Equalization Recovery Design]]
- [[Lead-Acid Desulfation Charge Control Design]]
- [[Equalization Event Tracking Design]]
- [[State of Charge Estimation Design]]
- [[Voltage Imbalance Detection Design]]
- [[Vehicle State Sensing Design]]
- [[Data Handling Design]]
  - [[Current Integration Amp-Hour Accumulation]]
  - [[Remaining Runtime Estimation Design]]
  - [[Usage-History State of Health Analytics]]
- [[Object and Proximity Sensing Design]]

### Communications and interfaces

- [[PC Battery Data Export Design]]
- [[Device Configuration and Service Design]]

- [[Battery-Charger Data Communication Design]]

- [[CAN Battery State Communication Design]]
- [[CAN Vehicle Operating Limit Command]]
- [[Wired Interface Design]]
- [[Wireless Battery Data Communication Design]]
- [[Wireless Interface Design]]

[[Bluetooth Interface]] is intentionally a nested reusable family under Wireless Interface Design because it can represent unspecified Bluetooth evidence while also specializing into BLE and Class 1 variants.

### Operator, warning, and control

- [[Abnormal Condition Alert Design]]
- [[Low Electrolyte Alert Design]]
- [[Warning and Display Device Design]]
  - [[Display Device Design]]
    - [[Vehicle Operator Display Design]]
  - [[Indicator and Alarm Design]]
- [[Vehicle Control Device Design]]
  - [[Operator Identification Design]]
  - [[Pre-Shift Checklist Enforcement Design]]
- [[Remote Vehicle Diagnostics Design]]
- [[Truck Telemetry Reporting Design]]
- [[Operator Access Authorization Design]]
  - [[Operator Presence Sensing Design]]
- [[Vehicle Drive Design]]

### Packaging and mounting

- [[Enclosure and Mounting Design]]

The complete Design inventory remains available through `BASE_all_Product Designs.base`. Do not create physical folders merely to mirror this hierarchy.

## Traceability

Follow these relationships when evaluating a Design:

- **Design → Product:** `designOf`
- **Design → Function:** `dependencyOf`
- **Function → Design:** `dependsOn`
- **Metric → Design:** `describes`

Step 55 found that all **95 specific Designs** are product-backed and source-backed, while direct Function dependency coverage is intentionally sparser. A missing Function dependency should therefore be reviewed, not automatically filled.

[[Reverse-Polarity Protection]] is the one known specific Design without a modeled general parent and remains a classification candidate.

## Navigation

- [[CANVAS_Product Designs]] — visual map of design concepts.
- `BASE_all_Product Designs.base` — exhaustive Design inventory.
- `BASE_local_Product Designs.base` — direct contents of this folder.

## Related areas

- [[README_Product Functions|Product Functions]] — behavior supported by Designs.
- [[README_Performance Metrics|Performance Metrics]] — dimensions used to compare or characterize Designs.
- [[README_Products|Products]] — cataloged offerings embodying Designs.
- [[README_Research|Research]] — comparative evidence and gap analysis.

## Maintenance

Use a Design note for a reusable implementation pattern, not for a single product claim. Preserve product evidence through `designOf`; link to Functions only where a supported dependency exists; link to metrics only where the metric meaningfully characterizes the Design.

- [[Wired Remote Charger Control Design]]
- [[Remote Charger Management Design]]

- [[Load-Handling Image Capture Design]]

- [[Impact-Triggered Vehicle Lockout Design]]

- [[Temperature-Compensated Charge Control Design]]
- [[BMS-Directed Charge Control Design]]
- [[Adaptive Charge Profile Control Design]]
