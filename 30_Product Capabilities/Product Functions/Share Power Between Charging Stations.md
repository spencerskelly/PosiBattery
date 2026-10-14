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
  - "[[PosiCharge High Voltage Power Station (DC)]]"
  - "[[PosiCharge MVS400 and MVS800]]"
---

# Share Power Between Charging Stations

## Definition

Balance or divide the energy delivered among several charging stations (or among the vehicles they serve) instead of each station acting alone.

## Notes

- Defined at station level. [[Balance Cells]] is cell-level balancing inside a battery and is a different function.
- Evidence differs by product, and the mechanisms are not shown to be the same: the MVS wording says power sharing prioritizes the lowest state of charge; the DC listing is an owner statement only (communication kit that balances energy transfer with other stations). No source found yet describes the High Voltage Power Station kit.
- ITW GSE's "Power Share" (surplus grid power distributed to eGPUs and other eGSE) is a site-level load offering from another maker and is not linked here (see [[ITW GSE]]).
- No Requirement is linked (intentional gap).
- **Sources** (product, evidence level, web page):
  - [[PosiCharge High Voltage Power Station (DC)]] (U): owner statement 2026-10-13 in this vault's working session; no web page found. The AC listing does not share power, per the same statement.
  - [[PosiCharge MVS400 and MVS800]] (V): <https://posicharge.com/wp-content/uploads/2026/01/MVS-400.pdf> (MVS400 sheet: up to three additional power stations, power sharing that prioritizes the lowest state of charge)

## Aliases


## Former ids
