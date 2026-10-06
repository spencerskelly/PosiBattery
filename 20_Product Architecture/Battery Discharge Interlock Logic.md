---
type: Object
subtype: firmware
id: OBJ-90111
uid: 20261006184500006skellyspencer
status: Draft
tags:
  - reusable-architecture
  - firmware
  - truck-control
  - battery-protection
  - deep-discharge
reuseScope: cross-product
hasDesign:
  - "[[Truck Battery Discharge Interlock]]"
dependsOn:
  - "[[Battery Discharge Indicator Module]]"
performs:
  - "[[Protect Battery from Deep Discharge]]"
partOf:
  - "[[Crown RC 5700 Series]]"
---

# Battery Discharge Interlock Logic

## Definition

Truck-side logic that uses battery-discharge state to inhibit selected truck functions or require an operator reset/re-key before continued operation.

## Notes

- Allocation to [[Crown RC 5700 Series]] is **>=95% engineering confidence** because Crown explicitly publishes BDI-based lift interrupt and re-key behavior, while the internal controller/software partition is not published.
- The exact relationship between the BDI module, truck controller, and lift/traction outputs remains undisclosed.
- This reusable Object represents the enforcement logic without inventing a specific controller part number.

## Former ids
