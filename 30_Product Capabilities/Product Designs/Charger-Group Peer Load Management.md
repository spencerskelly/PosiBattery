---
type: Design
subtype:
id: DES-00131
uid: 20261014155857260skellyspencer
status: Draft
tags:
  - fleet-software
  - design-characteristic
subtypeOf:
  - "[[Site Power Load Management Design]]"
designOf:
  - "[[Linde connect charger]]"
  - "[[Jungheinrich Active Load Management]]"
  - "[[Toyota Peak Load Management]]"
  - "[[Crown V-HFM3 Charger]]"
  - "[[PosiCharge MVS400 and MVS800]]"
dependencyOf:
  - "[[Share Power Between Charging Stations]]"
---

# Charger-Group Peer Load Management

## Definition

Chargers of one maker share a power budget through their own radio, cable or control unit, with priority by truck.

## Notes

- **Manual evidence (2026-10-14):** the PosiCharge DVS/MVS manual describes one main station and support stations, a power server in a communicated variable mode or a fixed 30 to 80 kW mode, and ports set to twice the station count (section 4.2). That is a main-station arrangement; it does not say how the main station divides power or that lowest state of charge goes first (that is from the MVS400 sheet). Source: [[Document - PosiCharge DVS and MVS GSE Operation and Maintenance Manual (5914769 rev C03)]] (T1). See C277.
- **Added 2026-10-14:** PosiCharge MVS400 and MVS800 fit by definition (power sharing among stations, lowest state of charge first); the Design's own text mentions radio, cable or control unit and the MVS sheet does not say which link PosiCharge uses.
- Each maker uses its own network; no common protocol is stated.
- A design characteristic found in products, not a decision by us. Added 2026-10-14.
- **Sources** (product, evidence level, document):
  - [[Linde connect charger]] (V): [[Document - Logistics Business Linde connect charger Article (2023-04-26)]]
  - [[Jungheinrich Active Load Management]] (V): [[Document - Jungheinrich Active Load Management Page (retrieved 2026-10-14)]]
  - [[Toyota Peak Load Management]] (V): [[Document - INDUSTRIAL Production Toyota Peak Load Management Article (2026-02-19)]]
  - [[Crown V-HFM3 Charger]] (V): [[Document - Crown Take Control of Forklift Energy Costs Blog (retrieved 2026-10-14)]]
  - [[PosiCharge MVS400 and MVS800]] (V): <https://posicharge.com/wp-content/uploads/2026/01/MVS-400.pdf>

## Aliases


## Former ids
