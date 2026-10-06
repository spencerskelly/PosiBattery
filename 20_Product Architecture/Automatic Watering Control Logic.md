---
type: Object
subtype: software
id: OBJ-90120
uid: 20261006191500009skellyspencer
status: Draft
tags:
  - reusable-architecture
  - battery
  - watering
  - charger-control
  - software
reuseScope: cross-product
hasDesign:
  - "[[Charger-Controlled Automatic Watering]]"
performs:
partOf:
  - "[[PosiCharge Single-Point Automatic Battery Watering]]"
  - "[[PosiCharge SVS200]]"
  - "[[Water Battery Cells]]"
---

# Automatic Watering Control Logic

## Definition

Charger-side control logic that enables an automatic battery watering cycle at the intended point in the charge process.

## Notes

- PosiCharge explicitly describes charger-controlled watering that operates at the right time and level.
- The current evidence does not disclose the trigger state, timer, sensor feedback, actuator type, pump/valve topology, or fault handling.
- This Object therefore captures the verified control role without inventing a specific controller partition or hydraulic component.

## Former ids
