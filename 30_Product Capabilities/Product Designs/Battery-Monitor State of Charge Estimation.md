---
type: Design
subtype:
id: DES-90036
uid: 20261006204500001skellyspencer
status: Draft
tags:
  - battery-monitoring
  - design-characteristic
  - software
  - state-of-charge
subtypeOf:
  - "[[State of Charge Estimation Design]]"
designOf:
  - "[[PosiCharge BMID]]"
  - "[[EnerSys Wi-iQ]]"
  - "[[Exide Motion+ EasyMonitor]]"
  - "[[HOPPECKE trak collect]]"
---

# Battery-Monitor State of Charge Estimation

## Definition

State-of-charge estimation executed in a battery-mounted monitoring or identification device using locally acquired battery measurements and stored battery state/configuration.

## Notes

- Product-backed examples currently represented are [[PosiCharge BMID]], [[EnerSys Wi-iQ]], [[Exide Motion+ EasyMonitor]], and [[HOPPECKE trak collect]].
- The Design identifies **where the estimation is performed**, not the mathematical algorithm.
- Voltage-only, current-integration, hybrid, model-based, and chemistry-specific algorithms remain possible implementations unless a product source identifies the method.
- Product allocations are based on direct SOC reporting plus battery-side electronic measurement/processing; exact firmware partition is an explicit >=95% engineering-confidence assumption where not published.

## Former ids
