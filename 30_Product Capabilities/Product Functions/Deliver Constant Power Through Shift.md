---
type: Function
subtype:
id: FUNC-00059
uid: 20261003090225554skellyspencer
status: Draft
tags:
  - truck-function
  - product-function
subtypeOf:
  - "[[Supply Vehicle Energy Without Charging]]"
performedBy:
  - "[[Hyster J1.5-3.0UT(L)]]"
  - "[[Yale ERC080VHL]]"
  - "[[Nuvera PowerEdge]]"
  - "[[Plug Power GenDrive]]"
realizes:
  - "[[Stretch Truck Run Time per Charge]]"
dependsOn:
  - "[[Fuel Cell Hybrid Power Stage]]"
---

# Deliver Constant Power Through Shift

## Definition

Deliver steady voltage and power for the whole shift without droop as the energy source depletes.

## Notes

- **Solution link added 2026-10-14 (reviewed, owner "y"):** depends on [[Fuel Cell Hybrid Power Stage]] (fuel cell, buffer battery and power electronics). Nuvera PowerEdge and Plug Power GenDrive both say constant voltage; the Function's two truck performers (Hyster J1.5-3.0UT(L), Yale ERC080VHL) state no Design. [[Hydrogen Storage Tank]] was not linked: it sets refuel time and run time, not constancy.
- Truck-side behavior found in product descriptions. Product links only where a source states the behavior; no link means unknown.
- No Requirement is linked (intentional gap).
- **Sources** (product, evidence level, web page):
  - [[Plug Power GenDrive]] (V): <https://plugpower.com/wp-content/uploads/2014/12/GenDrive-Series-1000-Spec-Sheet.pdf>
  - [[Nuvera PowerEdge]] (V): <https://www.liftandaccess.com/news/hybrid-fuel-cell-forklifts-introduced>
  - [[Yale ERC080VHL]] (V): <https://www.yale.com/en-us/north-america/lithium-ion-forklifts/erc080vhl/>
  - [[Hyster J1.5-3.0UT(L)]] (V): <https://www.hyster.com/fr-fr/emea/chariots-elevateurs-electriques-4-roues/j1.5-3.5ut>

## Aliases


## Former ids
