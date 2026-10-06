---
type: Object
subtype: circuit
id: OBJ-90055
uid: 20261006083000002skellyspencer
status: Draft
tags:
  - reusable-architecture
  - battery-monitoring
  - electrolyte
  - low-current
reuseScope: cross-product
hasDesign:
  - "[[Low-Current Electrolyte Level Input]]"
partOf:
  - "[[HOPPECKE trak collect]]"
performs:
  - "[[Sense Electrolyte Level]]"
---

# Low-Current Electrolyte Level Input Circuit

## Definition

Electrical input circuit that excites or reads an electrolyte-level sensor using a low-current interface.

## Notes

- The current implementation is evidenced by [[HOPPECKE trak collect]], whose technical data sheet specifies 11.3 V, 55 µA trigger current, and 100 µA maximum current for electrolyte level.
- The values establish an electrical input circuit but do not identify the probe's underlying sensing technology.
- Comparator, ADC, current-source, protection, filtering, and firmware details remain unspecified.

## Former ids
