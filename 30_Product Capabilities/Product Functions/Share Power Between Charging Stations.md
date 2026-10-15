---
type: Function
subtype:
id: FUNC-00133
uid: 20261013185053915skellyspencer
status: Draft
tags:
  - charger
  - product-function
subtypeOf: []
satisfies: []
performedBy:
  - "[[HVPS Communications Kit]]"
  - "[[PosiCharge High Voltage Power Station (DC)]]"
  - "[[PosiCharge MVS400 and MVS800]]"
realizes:
  - "[[Connect Chargers and Batteries Safely at the Site]]"
dependsOn:
  - "[[Charger-Group Peer Load Management]]"
---

# Share Power Between Charging Stations

## Definition

Balance or divide the energy delivered among several charging stations (or among the vehicles they serve) instead of each station acting alone.

## Notes

- **Solution link added 2026-10-14 (reviewed, owner "y"):** depends on [[Charger-Group Peer Load Management]]: PosiCharge MVS400 and MVS800 share power with up to three more power stations, prioritizing the lowest state of charge (MVS-400 sheet, T1). The HVPS DC variant and its communication kit are owner-stated (U) to do the same and are not linked to the Design.
- Defined at station level. [[Balance Cells]] is cell-level balancing inside a battery and is a different function.
- Evidence differs by product, and the mechanisms are not shown to be the same: the MVS wording says power sharing prioritizes the lowest state of charge; the DC listing is an owner statement only (communication kit that balances energy transfer with other stations). No source found yet describes the High Voltage Power Station kit.
- ITW GSE's "Power Share" (surplus grid power distributed to eGPUs and other eGSE) is a site-level load offering from another maker and is not linked here (see [[ITW GSE]]).
- No Requirement is linked (intentional gap).
- **Sources** (product, evidence level, web page):
  - [[HVPS Communications Kit]] (U): owner statement 2026-10-13; no web page found.
  - [[PosiCharge High Voltage Power Station (DC)]] (U): owner statement 2026-10-13 in this vault's working session; no web page found. The AC listing does not share power, per the same statement.
  - [[PosiCharge MVS400 and MVS800]] (V): <https://posicharge.com/wp-content/uploads/2026/01/MVS-400.pdf> (MVS400 sheet: up to three additional power stations, power sharing that prioritizes the lowest state of charge)

## Aliases


## Former ids
