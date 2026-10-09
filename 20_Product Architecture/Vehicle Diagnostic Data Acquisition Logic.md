---
type: Object
subtype: firmware
id: OBJ-90140
uid: 20261006222000002skellyspencer
status: Draft
tags:
  - reusable-architecture
  - firmware
  - vehicle
  - diagnostics
reuseScope: cross-product
hasDesign:
  - "[[Remote Vehicle Diagnostics Design]]"
dependsOn:
  - "[[Control Circuit]]"
performs:
  - "[[Diagnose Vehicle Remotely]]"
partOf:
  - "[[TUG Endurance Baggage Tractor]]"
  - "[[TUG ALPHA 1 Pushback]]"
  - "[[Diagnose Vehicle Remotely]]"
---

# Vehicle Diagnostic Data Acquisition Logic

## Definition

Vehicle-side software or firmware that reads controller faults and diagnostic state, assembles diagnostic records or snapshots, and exposes them for remote service access.

## Notes

- Candidate inputs include diagnostic trouble codes, controller faults, battery/BMS faults, ground-fault state, disconnected-device state, temperatures, voltages, operating state, and subsystem health.
- Exact buses, controller addresses, DTC formats, and snapshot triggers remain product-specific.
- This Object produces diagnostic data; remote transport and technician interpretation are represented separately.

## Former ids
