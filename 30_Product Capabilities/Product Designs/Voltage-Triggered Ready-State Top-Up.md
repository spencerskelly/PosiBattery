---
type: Design
subtype:
id: DES-00143
uid: 20261014175143932skellyspencer
status: Draft
tags:
  - charger
  - control
  - design-characteristic
subtypeOf:
  - "[[Charge Profile Control Design]]"
designOf:
  - "[[PosiCharge ProCore Solo]]"
dependsOn:
  - "[[Charger Power Stage Design]]"
dependencyOf:
  - "[[Float Charge Battery]]"
---

# Voltage-Triggered Ready-State Top-Up

## Definition

Charger control that stays connected to a battery and, when the battery voltage falls below a set level, charges it back up to a ready-state voltage.

## Notes

- Design characteristic found in a product, not a decision by us. Added 2026-10-14 (IB-236).
- **Basis:** owner statement 2026-10-14 (U), about the PosiCharge ProCore Solo: when connected and the battery drops below a voltage, charging brings it to the optimal ready-state voltage. PosiCharge's sheet (T1) says only 'plug and go, float charge, no battery monitor required'. The trigger voltage, the ready-state voltage, the charge current and the chemistries it applies to are not stated anywhere yet (IB-238).
- **Difference from a classic float charge:** a classic float holds a constant voltage continuously. The owner's description is a threshold that restarts charging, which is a different control. The Function keeps the name Float Charge Battery because the sheet uses it (C274).
- **Sources** (product, evidence level, basis):
  - [[PosiCharge ProCore Solo]] (U): owner statement 2026-10-14; <https://posicharge.com/wp-content/uploads/2026/02/5x7_ProCore-Solo-1.pdf> (V, the words 'float charge' and 'no battery monitor required' only)

## Aliases


## Former ids
