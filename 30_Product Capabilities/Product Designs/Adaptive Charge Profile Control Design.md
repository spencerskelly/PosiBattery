---
type: Design
subtype:
id: DES-90951
uid: 20261006232000001skellyspencer
status: Draft
tags:
  - charger
  - adaptive-charging
  - control
supertypeOf:
  - "[[Ri-Based Adaptive Charging]]"
  - "[[Diagnostic-Loop Adaptive Charging]]"
designOf:
  - "[[Adaptive Charge Profile Control Firmware]]"
  - "[[Fronius Selectiva 4.0]]"
  - "[[EnerSys IMPAQ Charger]]"
realizes:
  - "[[Adapt Charge to Battery Condition]]"
dependencyOf:
  - "[[Adapt Charge to Battery Condition]]"
dependsOn:
  - "[[Charger Power Stage Design]]"
---

# Adaptive Charge Profile Control Design

## Definition

Reusable charger-control design that adjusts current, voltage, phase timing, or charge characteristic during a session based on measured or inferred battery condition.

## Notes

- The Design sits above the charger power stage: it decides how the charge profile should change, while [[Charger Power Stage Design]] delivers the commanded electrical output.
- Inputs may include internal resistance, voltage response, current response, temperature, state of charge, elapsed time, or inferred battery status depending on product.
- [[Ri-Based Adaptive Charging]] captures the Fronius Selectiva strategy.
- [[Diagnostic-Loop Adaptive Charging]] captures the EnerSys IMPAQ heavy-duty diagnostic-loop strategy.
- Exact control law, thresholds, filtering, sample rate, phase transitions, safety limits, and battery models remain product-specific.

## Former ids
