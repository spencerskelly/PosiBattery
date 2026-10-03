---
type: Object
subtype: electrical
id: OBJ-00165
uid: 20261003084359645skellyspencer
status: Draft
tags:
  - option-package
  - battery-interface
performs:
  - "[[Communicate Battery State over CAN]]"
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

- Hyster says Power Cellect is an option on 27 Hyster electric forklift models, uses a CAN bus between a qualified battery and the truck, lets users switch between lead-acid, TPPL and lithium-ion, triggers a controlled shutdown at complete discharge, and shows battery state of health and lifetime discharge when Hyster Tracker is added. Source: Hyster release (2024-01-31) via Industrial Distribution (T2), retrieved 2026-10-03. <https://www.inddist.com/new-products/material-handling-storage/product/22885612/hyster-power-cellect-provides-forklift-battery-freedom>
- EnerSys states Hyster-Yale approved full integration of NexSys TPPL with Hyster Power Cellect and Yale Power Key. Source: EnerSys release (2023-07-19) (T1), retrieved 2026-10-03. <https://www.enersys.com/de/about-us/news/fleet-managers-get-powerful-flexibility-combining-enersys-technology-breadth-with-yale-power-key-and-hyster-power-cellect/>
- **Functions performed, with citations:**
  - [[Communicate Battery State over CAN]] (V): <https://www.inddist.com/new-products/material-handling-storage/product/22885612/hyster-power-cellect-provides-forklift-battery-freedom>
- **Design characteristics, with citations:**
  - [[CAN Interface]] (V): <https://www.inddist.com/new-products/material-handling-storage/product/22885612/hyster-power-cellect-provides-forklift-battery-freedom>

## Aliases

- Power Cellect

## Former ids
