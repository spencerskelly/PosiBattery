---
type: Object
subtype: circuit
id: OBJ-90021
uid: 20261005213400008skellyspencer
status: Draft
tags:
  - reusable-architecture
  - battery-monitoring
  - voltage
reuseScope: cross-product
subtypeOf:
  - "[[Battery Voltage Measurement Circuit]]"
hasPart:
  - "[[Precision Resistive Divider Network]]"
  - "[[Voltage Input Protection and Filter]]"
  - "[[Analog-to-Digital Converter]]"
hasDesign:
  - "[[Mid-Battery Differential Voltage Measurement]]"
dependsOn:
  - "[[Mid-Battery Voltage Tap Harness]]"
partOf:
  - "[[EnerSys Wi-iQ]]"
  - "[[Exide Motion+ EasyMonitor]]"
dependencyOf:
  - "[[Voltage Imbalance Evaluation Firmware]]"
  - "[[Voltage Imbalance Comparator Circuit]]"
performs:
  - "[[Detect Voltage Imbalance]]"
  - "[[Measure Battery Voltage]]"
---

# Mid-Battery Differential Voltage Measurement Circuit

## Definition

Voltage-measurement circuit with an additional midpoint/balance input used to compare battery halves.

## Notes

- Requires a physical midpoint/balance connection such as [[Mid-Battery Voltage Tap]].
- May reuse the same ADC and controller resources as overall battery-voltage measurement.
- This solution is linked to products only when midpoint measurement is documented.

## Former ids
