---
type: Object
subtype: firmware
id: OBJ-90092
uid: 20261006204500005skellyspencer
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
  - "[[Battery Voltage Acquisition Firmware]]"
  - "[[Battery Current Acquisition Firmware]]"
  - "[[Battery Temperature Acquisition Firmware]]"
performs:
  - "[[Estimate State of Charge]]"
---

# Hybrid State of Charge Estimator Firmware

## Definition

Candidate SOC-estimation firmware that combines current integration with voltage, temperature, battery configuration, and one or more correction mechanisms.

## Notes

- **Candidate implementation, not a product claim.**
- Possible implementations can combine coulomb counting, voltage/SOC lookup, temperature compensation, capacity or aging correction, charge-state recognition, and model-based correction.
- No current product is allocated because the available product evidence does not identify a hybrid SOC algorithm.

## Former ids
