---
type: Design
subtype:
id: DES-90963
uid: 20261014000000009skellyspencer
status: Draft
tags:
  - battery
  - design-characteristic
  - bms
subtypeOf:
  - "[[Battery Management System Design]]"
designOf:
  - "[[REC 2Q BMS]]"
  - "[[Batrium WatchMonCORE]]"
  - "[[Batrium CellMate-K9]]"
describedBy:
  - "[[External BMS Product Landscape]]"
  - "[[BMS Function Definitions]]"
---

# Master and Cell Monitor BMS Topology

## Definition

BMS split into a central unit that supervises and decides and cell-side units that measure and balance groups of cells.

## Notes

- Neutral terms: the encyclopedia names centralized, modular and distributed BMS topologies ([[Document - Wikipedia Battery Management System (retrieved 2026-10-13)]]). Which of its terms fits each product below is an analyst judgment, not a source statement.
- REC: the REC page says the master-slave configuration supports up to 240 cells with the 2Q BMS ([[Document - REC BMS Product Page (retrieved 2026-10-13)]]).
- Batrium: the WatchMonCORE supervisor works with separate cell monitors, and 'two or more CellMate-K9 can be daisy chained' ([[Document - Batrium BMS Product Guide (undated)]]).
- Not stated by any source read: the link between master and slave units (medium, protocol, isolation).
- No Requirement is linked (intentional gap).

## Aliases



## Former ids
