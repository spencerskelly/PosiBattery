---
type: Object
subtype: circuit
id: OBJ-90039
uid: 20261005222810012skellyspencer
status: Draft
tags:
  - reusable-architecture
  - battery-monitoring
  - current
reuseScope: cross-product
subtypeOf:
  - "[[Battery Current Measurement Circuit]]"
hasPart:
  - "[[Current Measurement Resistor]]"
  - "[[Differential Measurement Amplifier]]"
  - "[[Analog-to-Digital Converter]]"
hasDesign:
  - "[[External Shunt Current Sensing]]"
---

# Resistive Current Measurement Circuit

## Definition

Battery-current measurement circuit that senses the small voltage across a calibrated low-resistance element and conditions it for ADC conversion.

## Notes

Typical implementation includes:
- calibrated low-resistance measurement element;
- differential or current-sense amplifier;
- input filtering and protection;
- ADC conversion;
- firmware offset/gain calibration and direction handling.

The market Design [[External Shunt Current Sensing]] maps to this reusable circuit realization.

## Former ids
