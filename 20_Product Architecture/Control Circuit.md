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
supertypeOf:
  - "[[Operator Display Controller Circuit]]"
dependencyOf:
  - "[[Amp-Hour Accumulator Firmware]]"
  - "[[Battery Weight Acquisition Firmware]]"
  - "[[Specific Gravity Measurement Circuit]]"
  - "[[Specific Gravity Acquisition Firmware]]"
  - "[[Battery Identification and Charger Communication Firmware]]"
  - "[[Battery Identification and Charger Communication Software Design]]"
  - "[[Battery Voltage Measurement Circuit]]"
  - "[[Battery Voltage Acquisition Firmware]]"
  - "[[State of Charge Estimation Firmware]]"
  - "[[Battery Current Acquisition Firmware]]"
  - "[[Battery Current Measurement Circuit]]"
  - "[[Local Status Presentation Firmware]]"
  - "[[LCD Display Interface Circuit]]"
  - "[[Battery Temperature Acquisition Firmware]]"
  - "[[Cell Failure Diagnostic Firmware]]"
  - "[[Battery Temperature Measurement Circuit]]"
  - "[[Battery Abuse Cycle Analytics Firmware]]"
  - "[[Equalization Event Tracking Firmware]]"
partOf:
  - "[[AMETEK Prestolite Power WBID]]"
  - "[[AMETEK Prestolite Power WBID Pro]]"
  - "[[AMETEK Prestolite Power BID with Ah Accumulator]]"
  - "[[Access Control Group CellTrac]]"
  - "[[Power Designers PowerTrac DT3]]"
  - "[[Power Designers PowerTrac SP+]]"
  - "[[HOPPECKE trak collect]]"
  - "[[Stryten M-Series Li610 Battery]]"
  - "[[EnerSys Wi-iQ]]"
  - "[[Exide Motion+ EasyMonitor]]"
  - "[[AMETEK Prestolite Power TruBid]]"
  - "[[PosiCharge BMID]]"
  - "[[PosiCharge PosiGuard]]"
  - "[[Raymond iBattery]]"
---

# Control Circuit

## Definition

Reusable controller electronics that execute product firmware and coordinate sensing, storage, communication, and decision logic.

## Notes

- This is shared infrastructure, not a complete realization of every Function that executes through it.
- Function allocation should point to the specific firmware, sensing circuit, communication circuit, or other implementation that actually provides the behavior.
- **PosiCharge BMID assumption:** presence of a control circuit is treated as a >=95% engineering assumption because public evidence describes an electronic battery-mounted device that stores identity/history and communicates battery information. No schematic or teardown has been found, so no MCU or processor part number is asserted.
- **TruBID assumption:** [[AMETEK Prestolite Power TruBid]] is allocated this shared controller role at **>=95% engineering confidence** because it continuously measures specific gravity, drives six LEDs, communicates wirelessly, and coordinates charging behavior. The exact MCU, processor, memory, and schematic are not published.
- **Raymond iBattery evidence:** Raymond patent CA2733079A1 explicitly describes a microcomputer in the battery sensor module; the [[Control Circuit]] allocation is therefore evidence-backed rather than inferred.
- **Wi-iQ / EasyMonitor assumption:** [[EnerSys Wi-iQ]] and [[Exide Motion+ EasyMonitor]] are allocated this shared controller role at **>=95% engineering confidence** because each locally acquires multiple battery measurements, drives local HMI, stores/processes state, and reports derived values such as SOC. Exact controller hardware is not published.

## Former ids
