---
type: Object
subtype: circuit
id: OBJ-90078
uid: 20261006183500004skellyspencer
status: Draft
tags:
  - reusable-architecture
  - battery-monitoring
  - voltage
  - imbalance
reuseScope: cross-product
hasDesign:
  - "[[Voltage Imbalance Detection Design]]"
  - "[[Midpoint Voltage Symmetry Detection]]"
dependsOn:
  - "[[Mid-Battery Differential Voltage Measurement Circuit]]"
performs:
  - "[[Detect Voltage Imbalance]]"
---

# Voltage Imbalance Comparator Circuit

## Definition

Hardware-only circuit that compares battery-section voltages and asserts an imbalance state when their difference exceeds a defined criterion.

## Notes

- A practical implementation could use op-amp or comparator stages, references, resistor networks, hysteresis, filters, timers and an output latch.
- This is a valid alternative to [[Voltage Imbalance Evaluation Firmware]] for simpler monitors.
- No current product is allocated because the public evidence does not establish a hardware-only topology.

## Former ids
