---
type: Object
subtype: circuit
id: OBJ-90074
uid: 20261006175500006skellyspencer
status: Draft
tags:
  - reusable-architecture
  - battery-monitoring
  - alert
  - circuit
reuseScope: cross-product
hasDesign:
  - "[[Abnormal Condition Alert Design]]"
performs:
  - "[[Alert on Abnormal Condition]]"
---

# Abnormal Condition Threshold Circuit

## Definition

Hardware-only circuit that recognizes an abnormal sensor or battery condition by comparing a signal against a threshold.

## Notes

- Possible realizations include a comparator, reference, hysteresis network, timer, latch and output driver.
- This is an alternative to programmable [[Abnormal Condition Evaluation Logic]] for simple monitors or dedicated protection/indicator circuits.
- No current product is allocated to this Object because the available public sources do not prove a hardware-only alert-decision topology.

## Former ids
