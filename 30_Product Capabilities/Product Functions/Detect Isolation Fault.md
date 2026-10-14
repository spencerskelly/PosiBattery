---
type: Function
subtype:
id: FUNC-90008
uid: 20261014000000006skellyspencer
status: Draft
tags:
  - battery-protection
  - bms
  - product-function
subtypeOf:
  - "[[Protect Battery from Harm]]"
performedBy:
  - "[[Orion BMS 2]]"
describedBy:
  - "[[BMS Function Definitions]]"
  - "[[External BMS Product Landscape]]"
---

# Detect Isolation Fault

## Definition

Detect a loss of electrical isolation between the high-voltage battery circuit and the chassis.

## Notes

- Neutral definition: the encyclopedia article lists ground fault among the conditions a BMS protects against ([[Document - Wikipedia Battery Management System (retrieved 2026-10-13)]]); it does not describe isolation monitoring.
- Product evidence: the Orion BMS 2 specification sheet lists an isolation fault detection circuit ([[Document - Orion BMS 2 Specifications (Ewert Energy Systems)]]). No other product read states it (BF10 in [[BMS Product Function and Requirement Driver Map]]).
- Related driver: UL 2580 tests include isolation resistance (RD1 in the same note); the clause was not read.
- No Requirement is linked (intentional gap).

## Aliases



## Former ids
