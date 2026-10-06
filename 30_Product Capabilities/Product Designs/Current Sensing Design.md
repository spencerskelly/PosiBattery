---
type: Design
subtype:
id: DES-00078
uid: 20261003101711537skellyspencer
status: Draft
tags:
  - general-design
  - design-characteristic
supertypeOf:
  - "[[External Shunt Current Sensing]]"
  - "[[Hall-Effect Current Sensing]]"
  - "[[Shuntless Current Sensing]]"
  - "[[Split-Core Current Sensor]]"
dependencyOf:
  - "[[Coulomb Counting State of Charge Estimation]]"
  - "[[Hybrid State of Charge Estimation]]"
realizes:
  - "[[Measure Battery Current]]"
designOf:
  - "[[Battery Current Measurement Circuit]]"
  - "[[PosiCharge PosiGuard]]"
supportedBy:
  - "[[Document - PosiCharge PosiGuard Product Page]]"
---

# Current Sensing Design

## Definition

General design class: Ways of measuring battery current.

## Notes

- This Design is the selected reusable implementation family for [[Measure Battery Current]] when a product is known to measure current but the physical sensing topology is not established.
- Child Designs represent specific sensing methods and should be assigned to products only when evidence or an explicit engineering decision supports that method.
- [[PosiCharge PosiGuard]] is linked at the generic Design level because public evidence establishes current measurement but not whether the product uses a resistive, Hall-effect, shuntless, or split-core implementation.
- No Requirement is linked; this Function is currently modeled as a supporting product capability rather than a committed Requirement satisfaction path.

## Aliases


## Former ids
