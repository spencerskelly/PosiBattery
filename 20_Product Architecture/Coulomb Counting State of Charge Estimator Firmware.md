---
type: Object
subtype: firmware
id: OBJ-90091
uid: 20261006204500004skellyspencer
status: Draft
tags:
  - reusable-architecture
  - firmware
  - battery-monitoring
  - state-of-charge
reuseScope: cross-product
subtypeOf:
  - "[[State of Charge Estimation Firmware]]"
dependsOn:
  - "[[Battery Current Acquisition Firmware]]"
performs:
  - "[[Estimate State of Charge]]"
---

# Coulomb Counting State of Charge Estimator Firmware

## Definition

Candidate SOC-estimation firmware that integrates battery current over time from a known or periodically corrected state-of-charge reference.

## Notes

- **Candidate implementation, not a product claim.**
- Typical inputs include bidirectional current, elapsed time, usable capacity, charge/discharge efficiency, and a correction/reference mechanism to limit integration drift.
- No current product is allocated because the available product evidence does not identify coulomb counting as the SOC algorithm.

## Former ids
