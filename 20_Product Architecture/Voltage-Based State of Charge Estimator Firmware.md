---
type: Object
subtype: firmware
id: OBJ-90090
uid: 20261006204500003skellyspencer
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
performs:
  - "[[Estimate State of Charge]]"
---

# Voltage-Based State of Charge Estimator Firmware

## Definition

Candidate SOC-estimation firmware that derives state of charge primarily from measured battery voltage and a chemistry/configuration-specific voltage-to-SOC relationship.

## Notes

- **Candidate implementation, not a product claim.**
- Possible implementations include open-circuit-voltage lookup after rest, loaded-voltage compensation, chemistry-specific curves, and temperature compensation.
- No current product is allocated because the available product evidence does not identify a voltage-only SOC algorithm.

## Former ids
