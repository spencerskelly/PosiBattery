---
type: Design
subtype:
id: DES-90010
uid: 20261005222800004skellyspencer
status: Draft
tags:
  - general-design
  - battery-monitoring
  - software
subtypeOf:
  - "[[State of Charge Estimation Design]]"
dependsOn:
  - "[[Battery Voltage Measurement Design]]"
  - "[[Current Sensing Design]]"
  - "[[Electrolyte-Immersed Temperature Sensor]]"
---

# Hybrid State of Charge Estimation

## Definition

State-of-charge estimation combining current integration with voltage, temperature, battery configuration, and periodic correction.

## Notes

Candidate implementations may combine:
- coulomb counting;
- voltage/SOC lookup;
- temperature compensation;
- charge-state/event recognition;
- capacity or aging correction;
- model-based correction.

This is a candidate method only. No PosiCharge product is assigned to this child Design without implementation evidence.

## Former ids
