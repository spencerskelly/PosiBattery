---
type: Object
subtype: circuit
id: OBJ-90134
uid: 20261006212000003skellyspencer
status: Draft
tags:
  - reusable-architecture
  - circuit
  - vehicle-control
  - access-control
reuseScope: cross-product
dependencyOf:
  - "[[Operator Access Authorization Logic]]"
  - "[[Pre-Shift Checklist Enforcement Logic]]"
  - "[[Impact Lockout Decision Logic]]"
performs:
partOf:
  - "[[Toyota PIN Code Access Pad]]"
  - "[[Panacea Smart Start]]"
  - "[[Crown InfoLink]]"
  - "[[Crown InfoLink 7-inch Touch Display]]"
  - "[[TLD Aircraft Safety Docking]]"
  - "[[Control Operator Access]]"
---

# Vehicle Enable Interlock

## Definition

Vehicle-control interface that prevents traction, lift, ignition, or truck enable until operator authorization is satisfied.

## Notes

- The implementation can be a controller software inhibit, ignition/starter interlock, enable input, relay, CAN command, or another vehicle-control mechanism.
- Panacea Smart Start explicitly acts as a starter authorization device.
- Toyota's PIN access pad explicitly prevents unauthorized use, while its exact interlock implementation is not published.
- This reusable Object represents the enforcement role without asserting a specific relay or ECU.

## Former ids
