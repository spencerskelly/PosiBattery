---
type: Design
subtype:
id: DES-90006
uid: 20261005213400004skellyspencer
status: Draft
tags:
  - general-design
  - battery-monitoring
  - voltage
subtypeOf:
  - "[[Battery Voltage Measurement Design]]"
dependsOn:
  - "[[Mid-Battery Voltage Tap]]"
designOf:
  - "[[Mid-Battery Differential Voltage Measurement Circuit]]"
---

# Mid-Battery Differential Voltage Measurement

## Definition

Voltage-measurement design that uses overall battery voltage plus a midpoint/balance connection to compare the two halves of the battery.

## Notes

- Useful for detecting half-battery imbalance or wiring/cell-group problems.
- [[Mid-Battery Voltage Tap]] provides the physical battery connection/mounting concept.
- This design does not imply that every product measuring overall voltage also uses a midpoint tap.

## Former ids
