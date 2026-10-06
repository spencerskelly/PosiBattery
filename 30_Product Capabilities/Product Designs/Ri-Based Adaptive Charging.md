---
type: Design
subtype:
id: DES-90952
uid: 20261006232000002skellyspencer
status: Draft
tags:
  - charger
  - adaptive-charging
  - internal-resistance
subtypeOf:
  - "[[Adaptive Charge Profile Control Design]]"
designOf:
  - "[[Fronius Selectiva 4.0]]"
---

# Ri-Based Adaptive Charging

## Definition

Adaptive charge-control strategy that uses effective battery internal resistance and related battery state to continuously shape the charging characteristic.

## Notes

- Fronius states that its Ri process derives battery condition from effective internal resistance, which varies with age, temperature, and state of charge, and adapts the charging characteristic for each charge.
- This Design does not assert the proprietary calculation, perturbation method, or exact current/voltage control law.

## Former ids
