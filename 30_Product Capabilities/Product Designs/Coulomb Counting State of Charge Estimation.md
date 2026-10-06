---
type: Design
subtype:
id: DES-90009
uid: 20261005222800003skellyspencer
status: Draft
tags:
  - general-design
  - battery-monitoring
  - software
subtypeOf:
  - "[[State of Charge Estimation Design]]"
dependsOn:
  - "[[Current Sensing Design]]"
---

# Coulomb Counting State of Charge Estimation

## Definition

State-of-charge estimation by integrating measured battery current over time from a known or periodically corrected SOC reference.

## Notes

Typical implementation requires:
- bidirectional current measurement;
- time integration in firmware;
- rated or learned usable capacity;
- charge/discharge efficiency handling;
- periodic SOC correction to control integration drift.

This is a candidate method, not an assertion about any PosiCharge product.

## Former ids
