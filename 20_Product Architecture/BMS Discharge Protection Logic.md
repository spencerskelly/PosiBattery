---
type: Object
subtype: firmware
id: OBJ-90110
uid: 20261006184500005skellyspencer
status: Draft
tags:
  - reusable-architecture
  - firmware
  - battery-protection
  - deep-discharge
reuseScope: cross-product
hasDesign:
  - "[[BMS Discharge Limitation]]"
performs:
  - "[[Protect Battery from Deep Discharge]]"
partOf:
  - "[[EnerSys NexSys iON Battery]]"
---

# BMS Discharge Protection Logic

## Definition

Battery-management firmware or control logic that detects a protected low-discharge state and requests or enforces discharge limitation.

## Notes

- Allocation to [[EnerSys NexSys iON Battery]] is evidence-backed at the architectural level because EnerSys explicitly states that its integrated BMS performs discharge-voltage limitation.
- The exact actuation path is not published, so this Object does not assert a specific contactor driver, current-limit actuator, or truck command.
- Candidate responsibilities include low-voltage thresholding, cell-minimum evaluation, persistence, hysteresis, fault escalation, shutdown request, and recovery criteria.

## Former ids
