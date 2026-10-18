---
type: Object
subtype: software
id: OBJ-00433
uid: 20261013205343755skellyspencer
status: Draft
tags:
  - battery-charger-software
  - battery-market-reference
  - commercial-product
  - software
productCategory: fleet-software
subtypeOf:
  - "[[Battery and Charger Management Software]]"
describedBy:
  - "[[Document - Exide Sonnenschein Lithium Battery and GNB Fleet Sheet (MXSLITEPDF00820)]]"
  - "[[Document - GNB Motive Power Overview (2021-08)]]"
  - "[[Document - Exide GNB Fleet Brochure Page (retrieved 2026-10-14)]]"
performs:
  - "[[Upload Battery Data to Cloud Portal]]"
  - "[[Alert on Abnormal Condition]]"
  - "[[Show Battery and Charger State in Fleet Software]]"
hasDesign:
  - "[[Fleet State Dashboard Design]]"
madeBy:
  - "[[Exide Technologies]]"
offeredWith:
  - "[[Exide Sonnenschein Lithium Battery]]"
  - "[[Exide TENSOR xGEL Battery]]"
  - "[[Exide BattID]]"
---

# Exide GNB Fleet

## Definition

Exide GNB cloud fleet service for batteries and chargers, in tiers from battery rotation to multi-site management.

## Notes

- **Update 2026-10-14 (IB-226):** the Exide brochure page lists battery priority and availability and predicted remaining battery life on every tier, fleet utilization and uptime indication, online access and a KPI dashboard on Professional and Ultimate. State of charge is not listed. Linked to [[Show Battery and Charger State in Fleet Software]] on the strength of availability and dashboard display. Source: [[Document - Exide GNB Fleet Brochure Page (retrieved 2026-10-14)]] (T1, second-hand). Tiers here (Starter 50, Professional 100, Ultimate unlimited chargers) differ from the tiers above (Essential, Premium, Ultimate; 500 chargers) (C267).
- The Sonnenschein Lithium sheet says GNB Fleet monitors vital parameters of batteries and chargers, sends automated alarm emails to logistics, site and shift managers, lets batteries and chargers request service on themselves, runs on a secure cloud solution accessible from any device and analyzes data for energy management; tiers run from a rotation system for equal battery usage to multi-site management. Source: Exide GNB Sonnenschein Lithium and GNB Fleet sheet (T1, read through a summarizing tool), retrieved 2026-10-13. <https://exidegroup.com/es/sites/default/files/2020-11/GNB_MP_Sonnenschein_Lithium_MHB_GNB_Fleet_EN.pdf>
- **Not stated:** tier names, pricing, protocols, data stored, and how it relates to GNB Cloud and Motion+ Fleet (named in the organization note) (IB-176).
- **Functions performed, with citations:**
  - [[Upload Battery Data to Cloud Portal]] (V): secure cloud solution. <https://exidegroup.com/es/sites/default/files/2020-11/GNB_MP_Sonnenschein_Lithium_MHB_GNB_Fleet_EN.pdf>
  - [[Alert on Abnormal Condition]] (V): automated alarm emails. <https://exidegroup.com/es/sites/default/files/2020-11/GNB_MP_Sonnenschein_Lithium_MHB_GNB_Fleet_EN.pdf>


- **Update 2026-10-13 (tiers):** Essential: battery priority and availability indication, 1 user per unit, 500 managed chargers. Premium: adds cloud access, automatic email alerts, battery lifetime and warranty management with [[Exide BattID]], 3 users, 500 chargers. Ultimate: adds multi-site, multi-administrator roles, updates and remote support, 5 users, unlimited chargers. Kept as one note with a tier list. Source: GNB motive power overview 2021-08 (T1, second-hand; parts garbled), <https://www.exidegroup.com/eu/sites/default/files/2021-08/GNB_MP_Overview_EN_web.pdf>

## Aliases

- GNB Fleet


## Former ids
