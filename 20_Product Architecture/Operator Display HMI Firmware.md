---
type: Object
subtype: firmware
id: OBJ-90069
uid: 20261006170500005skellyspencer
status: Draft
tags:
  - reusable-architecture
  - operator-interface
  - display
  - firmware
reuseScope: cross-product
dependsOn:
  - "[[Operator Display Controller Circuit]]"
performs:
  - "[[Display Battery Status to Operator]]"
partOf:
  - "[[EnerSys Truck iQ]]"
  - "[[Crown Gena Operating System]]"
---

# Operator Display HMI Firmware

## Definition

Firmware or embedded HMI software that converts battery-state information into operator-facing values, icons, warnings, pages, or widgets.

## Notes

- Allocation to [[EnerSys Truck iQ]] is an **>=95% engineering-confidence assumption** because it is an electronic touchscreen dashboard with multiple live battery values and alerts, while EnerSys does not publish its internal firmware architecture.
- Allocation to [[Crown Gena Operating System]] is functionally direct because Gena is itself the truck operating/HMI software; this reusable note represents the battery-status presentation role within that software.
- The firmware does not imply the source transport. Product-specific battery data can arrive through BLE, CAN, or internal vehicle signals.

## Former ids
