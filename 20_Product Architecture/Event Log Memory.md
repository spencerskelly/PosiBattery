---
type: Object
subtype: component
id: OBJ-90122
uid: 20261006193000003skellyspencer
status: Draft
tags:
  - reusable-architecture
  - component
  - memory
  - logging
reuseScope: cross-product
hasDesign:
  - "[[Non-Volatile Event Memory]]"
dependencyOf:
  - "[[Battery Event Logger Firmware]]"
performs:
  - "[[Log Battery Events and Usage]]"
---

# Event Log Memory

## Definition

Persistent memory role used to retain battery event and usage records across power cycles.

## Notes

- The physical technology can be internal flash, external flash, EEPROM, FRAM, removable storage, or another non-volatile medium.
- Capacity, endurance, file system, record format, and rollover strategy remain product-specific.
- Existing product evidence for PowerTrac 3 / DT3, Wi-iQ, HOPPECKE trak collect and Prestolite devices supports persistent event/history retention without exposing a common memory technology.

## Former ids
