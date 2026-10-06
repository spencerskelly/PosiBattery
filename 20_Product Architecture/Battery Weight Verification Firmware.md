---
type: Object
subtype: firmware
id: OBJ-90097
uid: 20261006171500006skellyspencer
status: Draft
tags:
  - reusable-architecture
  - firmware
  - battery-monitoring
  - weight
reuseScope: cross-product
hasDesign:
  - "[[Stored Battery Weight Compatibility Verification]]"
dependsOn:
  - "[[Battery Specification Memory]]"
  - "[[Power-Line Communication Circuit]]"
partOf:
  - "[[Truck Controller and CAN Bus]]"
performs:
  - "[[Detect Battery Weight]]"
---

# Battery Weight Verification Firmware

## Definition

Vehicle-side firmware that retrieves the installed battery's stored weight specification, compares it with the vehicle minimum battery weight, and produces a compatibility result.

## Notes

- Raymond's patent explicitly places the weight-verification software routine in the vehicle controller.
- The routine requests the battery specification data from the battery sensor module, reads the vehicle minimum battery weight, compares the two values, and can restrict vehicle operation when the installed battery is too light.
- This Object is intentionally **not** modeled as part of [[Raymond iBattery]]; the battery module supplies the specification data while the vehicle controller performs the comparison.
- Source: <https://patents.google.com/patent/CA2733079A1/en>

## Former ids
