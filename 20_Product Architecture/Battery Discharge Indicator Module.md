---
type: Object
subtype: component
id: OBJ-90072
uid: 20261006170500008skellyspencer
status: Draft
tags:
  - reusable-architecture
  - operator-interface
  - battery-status
reuseScope: cross-product
hasDesign:
  - "[[Battery Discharge Indicator]]"
partOf:
  - "[[Crown RC 5700 Series]]"
  - "[[Vehicle Operator Display Assembly]]"
  - "[[Linde MT18 Multifunction Display]]"
dependencyOf:
  - "[[Hyster Power Cellect]]"
performs:
  - "[[Display Battery Status to Operator]]"
---

# Battery Discharge Indicator Module

## Definition

Dedicated operator-visible indicator or display element that presents battery discharge state or remaining battery capacity.

## Notes

- [[Linde MT18 Multifunction Display]] explicitly includes a battery discharge indicator and therefore contains this reusable role.
- [[Hyster Power Cellect]] explicitly uses the truck's factory Battery Discharge Indicator; the module is modeled as a dependency rather than a part of the Power Cellect option package.
- The physical display technology and signal interface remain unspecified.

## Former ids
