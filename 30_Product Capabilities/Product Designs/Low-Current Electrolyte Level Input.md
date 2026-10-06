---
type: Design
subtype:
id: DES-90015
uid: 20261006083000001skellyspencer
status: Draft
tags:
  - battery-monitoring
  - design-characteristic
  - electrolyte
  - low-current
subtypeOf:
  - "[[Electrolyte Level Sensing Design]]"
designOf:
  - "[[Low-Current Electrolyte Level Input Circuit]]"
  - "[[HOPPECKE trak collect]]"
describedBy:
  - "[[Metric - Electrolyte Level Sensing]]"
---

# Low-Current Electrolyte Level Input

## Definition

Electrolyte-level sensing through a dedicated low-current electrical sensor input whose threshold characteristics are published but whose probe transduction principle is not.

## Notes

- [[HOPPECKE trak collect]] publishes electrolyte-level input values of 11.3 V supply, 55 µA trigger current, and 100 µA maximum current.
- These values support modeling a dedicated low-current sensing input.
- The source does not establish whether the connected probe is conductive, capacitive, optical, or another technology, so this Design intentionally stops at the electrical interface behavior.

## Former ids
