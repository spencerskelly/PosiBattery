---
type: Design
subtype:
id: DES-90921
uid: 20261006184500002skellyspencer
status: Draft
tags:
  - battery-protection
  - bms
  - lithium
  - deep-discharge
subtypeOf:
  - "[[Deep Discharge Protection Design]]"
designOf:
  - "[[EnerSys NexSys iON Battery]]"
  - "[[BMS Discharge Protection Logic]]"
---

# BMS Discharge Limitation

## Definition

Battery-resident deep-discharge protection in which the BMS limits or interrupts discharge when cell or pack voltage approaches a protected lower limit.

## Notes

- [[EnerSys NexSys iON Battery]] is the verified implementation currently represented. EnerSys states that the integrated BMS performs charge and discharge voltage limitation and provides battery protection/control.
- The exact enforcement mechanism—contactor opening, current-limit command, truck request, or a combination—is not fully disclosed by the current source.
- This Design therefore captures the battery-resident protection locus without over-specifying the final power interruption hardware.

## Former ids
