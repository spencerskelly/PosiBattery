---
type: Object
subtype: electrical
id: OBJ-00396
uid: 20261003195011087skellyspencer
status: Draft
tags:
  - truck-part
  - anatomy
  - battery-market-reference
abstract: true
partOf:
  - "[[Industrial Truck Anatomy]]"
hasPart:
  - "[[Battery Weight Verification Firmware]]"
---

# Truck Controller and CAN Bus

## Definition

Generic truck part: Motor and vehicle controllers, wiring harness and the vehicle network (CAN or LIN) that devices connect to.

## Notes

- Abstract, shared by every truck class; not every class has every part (a pallet truck has no overhead guard or counterweight, and mast types differ).
- Accessories map to this part in [[Truck Part Connection Register]]; the mapping is not written as frontmatter links (see that note).
- Raymond patent CA2733079A1 explicitly places its battery-weight verification software routine in the vehicle controller. [[Battery Weight Verification Firmware]] is therefore modeled as a reusable vehicle-controller firmware part rather than as firmware inside [[Raymond iBattery]].

## Aliases


## Former ids
