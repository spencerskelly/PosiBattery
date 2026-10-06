---
type: Design
subtype:
id: DES-90922
uid: 20261006184500003skellyspencer
status: Draft
tags:
  - battery-protection
  - truck-control
  - deep-discharge
subtypeOf:
  - "[[Deep Discharge Protection Design]]"
designOf:
  - "[[Crown RC 5700 Series]]"
  - "[[Battery Discharge Interlock Logic]]"
---

# Truck Battery Discharge Interlock

## Definition

Truck-side protection that uses battery-discharge state to inhibit lift, require re-key, reduce functionality, or otherwise prevent continued damaging discharge.

## Notes

- [[Crown RC 5700 Series]] is the verified implementation currently represented. Crown explicitly publishes a battery-discharge indicator with lift interrupt and re-key behavior.
- This Design places the enforcement in the truck control architecture rather than in the battery pack.
- The source does not disclose the exact SOC/voltage threshold, whether the BDI directly drives the interlock, or which controller owns the final decision.

## Former ids
