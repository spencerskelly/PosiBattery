---
type: Object
subtype: software
id: OBJ-90112
uid: 20261006184500007skellyspencer
status: Draft
tags:
  - reusable-architecture
  - software
  - can
  - truck-control
  - battery-protection
reuseScope: cross-product
hasDesign:
  - "[[CAN-Coordinated Deep Discharge Shutdown]]"
dependsOn:
  - "[[CAN Communication Circuit]]"
performs:
  - "[[Protect Battery from Deep Discharge]]"
partOf:
  - "[[Hyster Power Cellect]]"
---

# CAN Deep Discharge Shutdown Logic

## Definition

Control logic that receives battery discharge state over CAN and coordinates a controlled vehicle shutdown or operating restriction.

## Notes

- Allocation to [[Hyster Power Cellect]] is **>=95% engineering confidence** because Hyster explicitly publishes CAN-based battery/truck integration and controlled shutdown at complete discharge.
- The exact software partition between the Power Cellect option package and the truck controller is not published.
- This Object therefore represents the reusable coordinated-control role rather than a claim about a specific ECU.

## Former ids
