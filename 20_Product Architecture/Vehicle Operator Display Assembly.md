---
type: Object
subtype: assembly
id: OBJ-90067
uid: 20261006170500003skellyspencer
status: Draft
tags:
  - reusable-architecture
  - operator-interface
  - display
abstract: true
reuseScope: cross-product
hasDesign:
  - "[[Vehicle Operator Display Design]]"
hasPart:
  - "[[Operator Display HMI Firmware]]"
  - "[[Vehicle-Mounted Display Module]]"
  - "[[Operator Touchscreen Display Module]]"
  - "[[Battery Discharge Indicator Module]]"
  - "[[Operator Display Controller Circuit]]"
performs:
  - "[[Display Battery Status to Operator]]"
---

# Vehicle Operator Display Assembly

## Definition

Reusable vehicle-side HMI assembly that receives battery or truck state and presents it to the operator.

## Notes

- The visible display can be a touchscreen, multifunction display, or dedicated battery-discharge indicator.
- The assembly does not imply a particular battery-data transport. BLE, CAN, internal vehicle signals, and other sources remain separate communication implementations.
- The reusable assembly represents the complete operator-display role. Its `hasPart` list is the reusable option set; a product occurrence uses only the display technology supported by evidence.

## Former ids
