---
type: Object
subtype: firmware
id: OBJ-90151
uid: 20261006233500003skellyspencer
status: Draft
tags:
  - reusable-architecture
  - firmware
  - charger
  - bms
reuseScope: cross-product
hasDesign:
  - "[[BMS-Directed Charge Control Design]]"
dependsOn:
  - "[[Control Circuit]]"
  - "[[Communication Interface Circuit]]"
performs:
  - "[[Charge Under BMS Control]]"
partOf:
  - "[[PosiCharge ProCore Edge]]"
  - "[[Delta-Q IC650]]"
  - "[[Fronius SelectION]]"
  - "[[Lester Summit Series II]]"
  - "[[Exide Motion+ Lithium Charger]]"
  - "[[Charge Under BMS Control]]"
---

# BMS-Directed Charge Control Firmware

## Definition

Charger-side firmware that receives BMS charge permission and charge-limit information, validates it, and converts it into charger output commands while preserving local charger safety constraints.

## Notes

- Candidate responsibilities include BMS session establishment, message validation, voltage/current limit handling, charge enable/disable, heartbeat monitoring, timeout/fallback, fault reporting, and command clamping.
- The communication transport is provided by the selected interface circuit, commonly CAN.
- The physical current and voltage output is produced by the charger power stage rather than this firmware Object.
- Internal firmware partitioning is generally unpublished and should be treated as an engineering abstraction unless directly identified.

## Former ids
