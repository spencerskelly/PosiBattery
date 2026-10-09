---
type: Object
subtype: firmware
id: OBJ-90137
uid: 20261006215000003skellyspencer
status: Draft
tags:
  - reusable-architecture
  - firmware
  - charger
  - remote-management
reuseScope: cross-product
hasDesign:
  - "[[Remote Charger Management Design]]"
dependsOn:
  - "[[Control Circuit]]"
  - "[[Communication Interface Circuit]]"
performs:
  - "[[Manage Chargers Remotely]]"
partOf:
  - "[[ACT Quantum 2]]"
  - "[[ACT Quantum 3]]"
  - "[[ACT Quantum Outdoor]]"
  - "[[Crown V-HFM3 Charger]]"
  - "[[Fronius Selectiva 4.0]]"
  - "[[Lester Summit Series II]]"
  - "[[Manage Chargers Remotely]]"
---

# Charger Remote Management Agent

## Definition

Charger-side software or firmware that exposes authenticated remote management operations and applies approved configuration, update, diagnostics, or control actions to the charger.

## Notes

- Candidate responsibilities include remote session handling, command validation, configuration read/write, update staging, rollback coordination, diagnostics, response reporting, and local safety/ownership checks.
- The exact relationship to the charger safety controller and power-control firmware remains product-specific.
- A remote management command must not bypass charger safety functions.

## Former ids
