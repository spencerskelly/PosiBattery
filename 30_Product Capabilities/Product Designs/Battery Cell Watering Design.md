---
type: Design
subtype:
id: DES-90925
uid: 20261006191500001skellyspencer
status: Draft
tags:
  - battery
  - watering
  - maintenance
  - general-design
supertypeOf:
  - "[[Float-Valve Single-Point Watering]]"
  - "[[Injector Level-Sensing Watering]]"
  - "[[Charger-Controlled Automatic Watering]]"
realizes:
  - "[[Water Battery Cells]]"
dependencyOf:
  - "[[Water Battery Cells]]"
designOf:
  - "[[Exide Automatic Watering System and Level Sensor]]"
  - "[[Midac Aquamatic Watering System]]"
  - "[[Water Battery Cells]]"
---

# Battery Cell Watering Design

## Definition

Reusable design family for refilling flooded lead-acid battery cells to the required electrolyte level through a common watering path, automatic valve, injector, or charger-controlled fill system.

## Notes

- Current products use materially different mechanisms, so the Function is decomposed into three child Designs rather than treated as one generic accessory.
- The Design does not assume a pump, pressurized tank, deionizer, cart, or fixed water source unless product evidence establishes it.
- Water quality, fill pressure, cell count, connection type, and maintenance procedure remain product-specific.

## Former ids
