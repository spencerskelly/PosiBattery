---
type: Object
subtype: electrical
id: OBJ-00095
uid: 20261002193402951skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - battery
  - ibms
productCategory: battery
subtypeOf:
  - "[[Lithium-Ion Traction Battery]]"
describedBy:
  - "[[Document - Exide Solition Light Datasheet (EU)]]"
performs:
  - "[[Measure Battery Voltage]]"
  - "[[Measure Battery Current]]"
  - "[[Communicate with Charger]]"
hasDesign:
  - "[[Integrated Battery Management System]]"
  - "[[Battery-Charger Data Communication Design]]"
madeBy:
  - "[[Exide Technologies]]"
offeredWith:
  - "[[Exide Motion+ Lithium Charger]]"
  - "[[Exide Motion+ Premium Charger]]"
integratesWith:
  - "[[Exide Motion+ Lithium Charger]]"
---

# Exide Solition Light Traction Battery

## Definition

Exide lithium-ion battery for cleaning machines, pallet trucks and wheelchairs, with a BMS that controls the Motion+ Lithium Charger.

## Notes

- The leaflet says Solition fits cleaning machines, pallet trucks and electric wheelchairs, runs 24/7, and its battery management system monitors voltage, current and other parameters and controls the Motion+ Lithium Charger. Source: Exide Solition leaflet (T1), retrieved 2026-10-02. <https://exidegroup.com/us/en/document/solition-light-traction-battery-leaflet>
- **Design characteristics, with citations:**
  - [[Integrated Battery Management System]] (V): <https://exidegroup.com/us/en/document/solition-light-traction-battery-leaflet>
- **Functions performed, with citations (round 40, gap review 2026-10-03):**
  - [[Measure Battery Voltage]] (V): <https://exidegroup.com/us/en/document/solition-light-traction-battery-leaflet>
  - [[Measure Battery Current]] (V): <https://exidegroup.com/us/en/document/solition-light-traction-battery-leaflet>
  - [[Communicate with Charger]] (V): <https://exidegroup.com/us/en/document/solition-light-traction-battery-leaflet>
- **Design characteristics, with citations (round 40, gap review 2026-10-03):**
  - [[Integrated Battery Management System]] (V): <https://exidegroup.com/us/en/document/solition-light-traction-battery-leaflet>

- **Architecture realization — charger communication:** published evidence establishes data exchange with a compatible charger, supporting [[Battery-Charger Data Communication Design]]. The transport and message set remain product-specific.

- **Update 2026-10-13 (EU data sheet):** three LFP models LTB24025O / LTB24050P / LTB24100P, 25.6 V, 25 / 50 / 100 Ah (0.64 / 1.28 / 2.56 kWh), 4,000 cycles at 0.2C 80% DoD 25 C, charge 0 to 45 C, discharge -20 to 55 C, IP54, wired RJ45 display, up to 4 modules in parallel, UN38.3 / CE / UKCA / IEC 62619 / IEC 62133. **Conflict-visible (C234):** the data sheet lists external communication as "No" while the leaflet-based statements above say the BMS controls the Motion+ Lithium Charger; the two documents may describe different variants. This note also carries `partOf` the Motion+ Lithium Charger, which no source supports (C229 pattern). Source: <https://www.exidegroup.com/eu/en/document/solition-light-traction-battery-datasheet>

## Aliases

- Solition


## Former ids
