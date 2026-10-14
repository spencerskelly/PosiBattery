---
type: Design
subtype:
id: DES-90964
uid: 20261014000000010skellyspencer
status: Draft
tags:
  - battery
  - design-characteristic
  - bms
subtypeOf:
  - "[[Battery Management System Design]]"
designOf:
  - "[[Orion BMS 2]]"
describedBy:
  - "[[External BMS Product Landscape]]"
  - "[[BMS Function Definitions]]"
---

# Passive Cell Balancing

## Definition

Cells are equalized by draining the higher cells through resistors as heat.

## Notes

- Neutral definition: passive balancing dissipates energy from the high cells ([[Document - Wikipedia Battery Management System (retrieved 2026-10-13)]], [[Document - MathWorks Battery Management System Overview (retrieved 2026-10-13)]]).
- Orion BMS 2 states passive balancing; the specification sheet gives 200 mA (BF3 in [[BMS Product Function and Requirement Driver Map]]; [[Document - Orion BMS 2 Product Page (retrieved 2026-10-13)]]).
- Batrium LongMon, BlockMon and LeafMon state a bypass current of 0 to 2 A (typically 1 A) ([[Document - Batrium BMS Product Guide (undated)]]); the guide does not use the word passive. Not linked as a design of those cell monitors, which have no note.
- Figures are in different units across makers; see C208.
- No Requirement is linked (intentional gap).

## Aliases



## Former ids
