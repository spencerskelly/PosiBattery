---
type: Design
subtype:
id: DES-90928
uid: 20261006191500004skellyspencer
status: Draft
tags:
  - battery
  - watering
  - charger-control
  - automatic
subtypeOf:
  - "[[Battery Cell Watering Design]]"
designOf:
  - "[[PosiCharge Single-Point Automatic Battery Watering]]"
  - "[[PosiCharge SVS200]]"
  - "[[Automatic Watering Control Logic]]"
---

# Charger-Controlled Automatic Watering

## Definition

Automatic battery watering in which charger-side control determines when to enable the watering cycle and supply water to the battery watering network.

## Notes

- PosiCharge explicitly describes its accessory as charger-controlled single-point automatic watering and states that it waters at the right time and level.
- [[PosiCharge SVS200]] explicitly offers automatic watering as an option.
- The current evidence does not establish the water-level sensor, solenoid valve, pump, reservoir, pressure regulator, or control algorithm. Those are intentionally not asserted.
- This Design captures the verified charger-control locus without over-specifying the hydraulic implementation.

## Former ids
