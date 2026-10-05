---
type: Object
subtype: electrical
id: OBJ-00165
uid: 20261003084359645skellyspencer
status: Draft
tags:
  - battery-interface
  - option-package
  - scope-oem-option
subtypeOf:
  - "[[Power Source Interface]]"
performs:
  - "[[Communicate Battery State over CAN]]"
  - "[[Protect Battery from Deep Discharge]]"
  - "[[Display Battery Status to Operator]]"
  - "[[Report Truck Telemetry]]"
  - "[[Adapt Truck to Battery Chemistry]]"
hasDesign:
  - "[[CAN Interface]]"
madeBy:
  - "[[Hyster-Yale]]"
integratesWith:
  - "[[EnerSys NexSys TPPL Battery]]"
offeredWith:
  - "[[Hyster Tracker Telemetry]]"
---

# Hyster Power Cellect

## Definition

Hyster optional package that lets an electric truck switch between lead-acid, TPPL and lithium-ion batteries over CAN, with a controlled shutdown on full discharge.

## Notes

**Summary:**
Hyster power option that lets electric trucks switch between lead-acid, TPPL and lithium-ion battery modes and communicate with the battery over CAN.

**Marketed features:**
- Quick switching between lead-acid, TPPL and lithium-ion modes without external accessories
- Full integration with EnerSys NexSys TPPL and lithium-ion batteries
- Battery data shown on the factory Battery Discharge Indicator; state-of-charge warnings
- Battery status and charging habits viewable in Hyster Tracker with optional telemetry
- Marketed for mixed fleets, ICE-to-electric conversion and higher resale value

**Summary and features sources:**
Maker or publisher marketing claims as stated, not independently verified.
- EnerSys (T1), retrieved 2026-10-04. <https://www.enersys.com/de/about-us/news/fleet-managers-get-powerful-flexibility-combining-enersys-technology-breadth-with-yale-power-key-and-hyster-power-cellect/>
- Hyster (T1), retrieved 2026-10-04. <https://www.hyster.com/globalassets/coms/hyster/north-america/documents/trucks/0000hbxxbc001_e_en-us_hyster-solutions-brochure-view.pdf>

- Hyster says Power Cellect is an option on 27 Hyster electric forklift models, uses a CAN bus between a qualified battery and the truck, lets users switch between lead-acid, TPPL and lithium-ion, triggers a controlled shutdown at complete discharge, and shows battery state of health and lifetime discharge when Hyster Tracker is added. Source: Hyster release (2024-01-31) via Industrial Distribution (T2), retrieved 2026-10-03. <https://www.inddist.com/new-products/material-handling-storage/product/22885612/hyster-power-cellect-provides-forklift-battery-freedom>
- EnerSys states Hyster-Yale approved full integration of NexSys TPPL with Hyster Power Cellect and Yale Power Key. Source: EnerSys release (2023-07-19) (T1), retrieved 2026-10-03. <https://www.enersys.com/de/about-us/news/fleet-managers-get-powerful-flexibility-combining-enersys-technology-breadth-with-yale-power-key-and-hyster-power-cellect/>
- **Functions performed, with citations:**
  - [[Communicate Battery State over CAN]] (V): <https://www.inddist.com/new-products/material-handling-storage/product/22885612/hyster-power-cellect-provides-forklift-battery-freedom>
- **Design characteristics, with citations:**
  - [[CAN Interface]] (V): <https://www.inddist.com/new-products/material-handling-storage/product/22885612/hyster-power-cellect-provides-forklift-battery-freedom>
- **Functions performed, with citations:**
  - [[Protect Battery from Deep Discharge]] (V): <https://www.inddist.com/new-products/material-handling-storage/product/22885612/hyster-power-cellect-provides-forklift-battery-freedom>
- The brochure says Power Cellect lets a truck switch between lead acid, TPPL and lithium-ion battery modes without external accessories, on numerous Hyster electric models. Source: Hyster solutions brochure (read round 20) (T1), retrieved 2026-10-03. <https://www.hyster.com/globalassets/coms/hyster/north-america/documents/trucks/0000hbxxbc001_e_en-us_hyster-solutions-brochure-view.pdf>
- **Truck parts (round 31):** typical (inferred from the device type, not from a source): mounts on [[Truck Battery Compartment]]; connects to [[Truck Battery Compartment]]. See [[Truck Part Connection Register]].
- Hyster's lithium-ion FAQ says its LFP batteries are managed by a BMS that monitors cell voltage, module temperature and pack current, that the BMS communicates with the charger over CAN messaging to adjust the charge current and keep every cell inside its safe zone, that it opens the charge contactor if any cell nears an unsafe limit, that a custom Hyster CAN protocol links battery and charger so only the recommended chargers can be used, that lead-acid chargers cannot charge it, and that the battery needs a power signal from the charger which many third-party chargers do not provide. Source: Hyster lithium-ion batteries FAQ (EMEA) (T1), retrieved 2026-10-03. <https://www.hyster.com/en-gb/emea/industry-solutions/power-sources/lithium-ion-batteries/>
- **Functions performed, with citations** (V = verified this pass, C = carried from seed text, U = user-stated):
  - [[Display Battery Status to Operator]] (V): <https://www.enersys.com/de/about-us/news/fleet-managers-get-powerful-flexibility-combining-enersys-technology-breadth-with-yale-power-key-and-hyster-power-cellect/>
  - [[Report Truck Telemetry]] (V): <https://www.enersys.com/de/about-us/news/fleet-managers-get-powerful-flexibility-combining-enersys-technology-breadth-with-yale-power-key-and-hyster-power-cellect/>
  - [[Adapt Truck to Battery Chemistry]] (V): <https://www.enersys.com/de/about-us/news/fleet-managers-get-powerful-flexibility-combining-enersys-technology-breadth-with-yale-power-key-and-hyster-power-cellect/>

## Aliases

- Power Cellect


## Former ids
