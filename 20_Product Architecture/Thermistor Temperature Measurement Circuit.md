---
type: Object
subtype: circuit
id: OBJ-90040
uid: 20261006060500003skellyspencer
status: Draft
tags:
  - reusable-architecture
  - battery-monitoring
  - temperature
  - thermistor
reuseScope: cross-product
subtypeOf:
  - "[[Battery Temperature Measurement Circuit]]"
hasPart:
  - "[[Thermistor Temperature Sensor]]"
hasDesign:
  - "[[Electrolyte-Immersed Temperature Sensor]]"
partOf:
  - "[[PosiCharge BMID]]"
performs:
  - "[[Measure Battery Temperature]]"
supportedBy:
  - "[[Document - PosiCharge BMID FAQ]]"
---

# Thermistor Temperature Measurement Circuit

## Definition

Temperature-measurement circuit using a thermistor as the sensing element.

## Notes

- [[PosiCharge BMID]] is allocated this circuit at **>=95% engineering confidence** because PosiCharge explicitly identifies an electrolyte-immersed thermistor in the BMID.
- The source establishes the sensor type and placement, but not the exact bias network, ADC topology, linearization method, or component part number.

## Former ids
