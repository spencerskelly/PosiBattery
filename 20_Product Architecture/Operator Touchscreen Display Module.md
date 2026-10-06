---
type: Object
subtype: component
id: OBJ-90071
uid: 20261006170500007skellyspencer
status: Draft
tags:
  - reusable-architecture
  - operator-interface
  - display
  - touchscreen
reuseScope: cross-product
hasDesign:
  - "[[Operator Touch Display]]"
partOf:
  - "[[Vehicle Operator Display Assembly]]"
  - "[[EnerSys Truck iQ]]"
dependencyOf:
  - "[[Crown Gena Operating System]]"
  - "[[Pre-Shift Checklist Enforcement Logic]]"
performs:
  - "[[Alert on Abnormal Condition]]"
  - "[[Display Truck Status to Operator]]"
  - "[[Display Battery Status to Operator]]"
---

# Operator Touchscreen Display Module

## Definition

Touch-capable vehicle display module used to present battery status and other operator information.

## Notes

- [[EnerSys Truck iQ]] explicitly uses a 4.3-inch truck-mounted touchscreen, so the touchscreen module role is verified there.
- [[Crown Gena Operating System]] explicitly uses a 7-inch touchscreen; because Gena is modeled as software, the physical module is a dependency rather than a part of the software Object.
- Exact touch technology, controller, resolution, display bus, brightness, and supplier are not published in the current evidence.

## Former ids
