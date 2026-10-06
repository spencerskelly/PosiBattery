---
type: Design
subtype:
id: DES-90026
uid: 20261006175500003skellyspencer
status: Draft
tags:
  - battery-monitoring
  - design-characteristic
  - alert
  - operator-interface
subtypeOf:
  - "[[Abnormal Condition Alert Design]]"
designOf:
  - "[[Yale ERC050-060VGL]]"
  - "[[EnerSys Truck iQ]]"
  - "[[Operator Display HMI Firmware]]"
---

# Operator Dashboard Abnormal Alert

## Definition

Abnormal battery condition presented to the vehicle operator on a truck-mounted display or dashboard.

## Notes

- [[EnerSys Truck iQ]] explicitly displays battery alerts, alarms and other Wi-iQ battery parameters on its truck-mounted touchscreen.
- [[Yale ERC050-060VGL]] explicitly shows low-state-of-charge and early-shutdown warnings on the truck display.
- The Design reuses the existing vehicle/operator display architecture rather than creating another display technology.
- The battery-to-display transport is product-specific; Truck iQ explicitly uses BLE.

## Former ids
