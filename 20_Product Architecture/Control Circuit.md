---
type: Object
subtype: circuit
id: OBJ-90001
uid: 20261005212400001skellyspencer
status: Draft
tags:
  - reusable-architecture
  - control
abstract: true
reuseScope: cross-product
dependencyOf:
  - "[[Battery Identification and Charger Communication Firmware]]"
  - "[[Battery Identification and Charger Communication Software Design]]"
  - "[[Battery Voltage Measurement Circuit]]"
  - "[[Battery Voltage Acquisition Firmware]]"
  - "[[State of Charge Estimation Firmware]]"
partOf:
  - "[[PosiCharge BMID]]"
  - "[[PosiCharge PosiGuard]]"
---

# Control Circuit

## Definition

Reusable controller electronics that execute product firmware and coordinate sensing, storage, communication, and decision logic.

## Notes

- This is shared infrastructure, not a complete realization of every Function that executes through it.
- Function allocation should point to the specific firmware, sensing circuit, communication circuit, or other implementation that actually provides the behavior.
- **PosiCharge BMID assumption:** presence of a control circuit is treated as a >=95% engineering assumption because public evidence describes an electronic battery-mounted device that stores identity/history and communicates battery information. No schematic or teardown has been found, so no MCU or processor part number is asserted.

## Former ids
