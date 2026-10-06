---
type: Design
subtype:
id: DES-90008
uid: 20261005222800002skellyspencer
status: Draft
tags:
  - general-design
  - battery-monitoring
  - software
subtypeOf:
  - "[[State of Charge Estimation Design]]"
dependsOn:
  - "[[Battery Voltage Measurement Design]]"
---

# Voltage-Based State of Charge Estimation

## Definition

State-of-charge estimation based primarily on measured battery voltage and a chemistry/configuration-specific voltage-to-SOC relationship.

## Notes

Possible implementations include:
- open-circuit-voltage lookup after sufficient rest;
- loaded-voltage compensation;
- chemistry-specific lookup curves;
- temperature-compensated voltage mapping.

This method is comparatively simple but can be inaccurate during charge/discharge because terminal voltage depends on current, temperature, chemistry, age, and recent history.

## Former ids
