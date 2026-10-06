---
type: Design
subtype:
id: DES-90037
uid: 20261006204500002skellyspencer
status: Draft
tags:
  - battery
  - design-characteristic
  - software
  - state-of-charge
  - bms
subtypeOf:
  - "[[State of Charge Estimation Design]]"
designOf:
  - "[[Stryten M-Series Li610 Battery]]"
---

# Integrated BMS State of Charge Estimation

## Definition

State-of-charge estimation performed by a battery's integrated battery-management system rather than by a separate battery-monitor accessory.

## Notes

- [[Stryten M-Series Li610 Battery]] is the current product-backed example: the battery has an integrated BMS and reports state of charge.
- The BMS locus is >=95% engineering confidence; the exact SOC algorithm is not published.
- This Design does not imply coulomb counting, open-circuit-voltage lookup, Kalman filtering, or another particular algorithm.

## Former ids
