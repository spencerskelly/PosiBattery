---
type: Function
subtype:
id: FUNC-90005
uid: 20261013233000016skellyspencer
status: Draft
tags:
  - battery-protection
  - bms
  - product-function
subtypeOf:
  - "[[Protect Battery from Harm]]"
performedBy:
  - "[[Green Cubes SAFEFlex Battery]]"
  - "[[EnerSys NexSys iON Battery]]"
  - "[[Orion BMS 2]]"
  - "[[REC Active BMS]]"
  - "[[Batrium CellMate-K9]]"
describedBy:
  - "[[BMS Function Definitions]]"
---

# Balance Cells

## Definition

Equalize the charge of the cells in a pack so that no cell limits the usable capacity.

## Notes

- Neutral definition: equalizing cells through energy dissipation, energy shuffling or reduced charge current (passive drains high cells through resistors as heat; active moves charge between cells) ([[Document - Wikipedia Battery Management System (retrieved 2026-10-13)]], [[Document - MathWorks Battery Management System Overview (retrieved 2026-10-13)]]).
- Evidence for products: the vault records balancing by the internal BMS for Green Cubes SAFEFlex (see [[Green Cubes SAFEFlex Battery]]); the NexSys iON manual says its power modules can balance cells during use but gives no thresholds ([[Document - EnerSys NexSys iON Operating Manual (Spanish, GLOB-ES-OM-NEX-ION 0323)]]).
- Lead-acid equalization is a different function: see [[Equalize Battery on Schedule]].
- No Requirement is linked (intentional gap).

## Aliases


## Former ids
