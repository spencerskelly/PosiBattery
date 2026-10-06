---
type: Object
subtype: component
id: OBJ-90095
uid: 20261006171500004skellyspencer
status: Draft
tags:
  - reusable-architecture
  - memory
  - battery-identification
  - weight
reuseScope: cross-product
hasDesign:
  - "[[Stored Battery Weight Compatibility Verification]]"
partOf:
  - "[[Raymond iBattery]]"
dependencyOf:
  - "[[Battery Weight Verification Firmware]]"
---

# Battery Specification Memory

## Definition

Electronic memory associated with a battery that stores manufacturer specification data such as identity, nominal voltage, rated capacity, and battery weight.

## Notes

- Raymond's patent explicitly describes memory in the battery sensor module containing a manufacturer specification table and a stored battery-weight value.
- The exact memory technology is not specified; EEPROM, flash, FRAM, internal MCU nonvolatile memory, or another implementation must not be inferred.
- The [[Raymond iBattery]] allocation is evidence-backed by the Raymond battery sensor module architecture rather than an engineering assumption.
- Source: <https://patents.google.com/patent/CA2733079A1/en>

## Former ids
