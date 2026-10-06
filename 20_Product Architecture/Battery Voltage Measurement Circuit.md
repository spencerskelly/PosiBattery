---
type: Object
subtype: circuit
id: OBJ-90018
uid: 20261005213400005skellyspencer
status: Draft
tags:
  - reusable-architecture
  - battery-monitoring
  - voltage
abstract: true
reuseScope: cross-product
supertypeOf:
  - "[[Resistive Divider ADC Voltage Measurement Circuit]]"
  - "[[Isolated Voltage Measurement Circuit]]"
  - "[[Mid-Battery Differential Voltage Measurement Circuit]]"
performs:
  - "[[Measure Battery Voltage]]"
hasDesign:
  - "[[Battery Voltage Measurement Design]]"
dependsOn:
  - "[[Control Circuit]]"
partOf:
  - "[[PosiCharge BMID]]"
  - "[[PosiCharge PosiGuard]]"
dependencyOf:
  - "[[Battery Voltage Acquisition Firmware]]"
---

# Battery Voltage Measurement Circuit

## Definition

Reusable circuit family that senses battery terminal voltage and provides a controller-readable measurement.

## Notes

- This is the product-independent implementation family for [[Measure Battery Voltage]].
- The circuit depends on [[Control Circuit]] for digital acquisition, scaling, calibration, and use of the sampled value.
- A product should select a concrete child circuit when the topology is known.
- **PosiCharge BMID / PosiGuard assumption:** some battery-voltage measurement circuit is treated as >=95% likely because both products are publicly documented as measuring battery voltage. The exact topology is not public.

## Former ids
