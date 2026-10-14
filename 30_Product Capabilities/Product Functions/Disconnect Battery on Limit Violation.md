---
type: Function
subtype:
id: FUNC-90006
uid: 20261013233000017skellyspencer
status: Draft
tags:
  - battery-protection
  - bms
  - product-function
subtypeOf:
  - "[[Protect Battery from Harm]]"
performedBy:
  - "[[EnerSys NexSys iON Battery]]"
  - "[[Hyster Power Cellect]]"
describedBy:
  - "[[BMS Function Definitions]]"
---

# Disconnect Battery on Limit Violation

## Definition

Open the battery's power path when voltage, current or temperature leaves the safe operating area.

## Notes

- Neutral definition: protection by preventing operation outside the safe operating area, and precharge control of contactors ([[Document - Wikipedia Battery Management System (retrieved 2026-10-13)]]).
- Evidence for products: the NexSys iON manual says a safe-disconnect system acts when voltage, current or temperature limits are exceeded and that the BMS controls the main contactors ([[Document - EnerSys NexSys iON Operating Manual (Spanish, GLOB-ES-OM-NEX-ION 0323)]]); Hyster says its BMS opens the charge contactor if a cell nears an unsafe limit (see [[Hyster Power Cellect]]).
- Related: deep-discharge protection is the narrower [[Protect Battery from Deep Discharge]].
- No Requirement is linked (intentional gap).

## Aliases


## Former ids
