---
type: Object
subtype: circuit
id: OBJ-90008
uid: 20261005212400008skellyspencer
status: Draft
tags:
  - reusable-architecture
  - communication
  - ble
reuseScope: cross-product
subtypeOf:
  - "[[Wireless Communication Circuit]]"
hasPart:
  - "[[BLE Radio Module]]"
hasDesign:
  - "[[Bluetooth Interface]]"
partOf:
  - "[[EnerSys Truck iQ]]"
  - "[[PosiCharge PosiGuard]]"
---

# BLE Communication Circuit

## Definition

Bluetooth/BLE radio circuit used to exchange data with a charger, mobile device, gateway, or other Bluetooth-capable peer.

## Notes

- The radio may be a module or an integrated radio SoC. The reusable model uses a module-level part until a product-specific implementation is known.
- Allocation to [[EnerSys Truck iQ]] is supported by EnerSys' explicit BLE link between Wi-iQ and Truck iQ; the exact radio/module implementation remains unpublished.

## Former ids
