---
type: Object
subtype: circuit
id: OBJ-90019
uid: 20261005213400006skellyspencer
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
  - "[[Resistive Divider ADC Voltage Measurement]]"
---

# Resistive Divider ADC Voltage Measurement Circuit

## Definition

Direct battery-voltage sensing circuit using a precision resistive divider, protection/filtering, and ADC conversion.

## Notes

- The ADC may be an MCU peripheral or an external converter.
- Divider ratio, impedance, tolerance, creepage, transient withstand, and filtering are product-specific.
- This is a strong generic candidate for 24–96 V battery monitors, but it is not asserted as the internal topology of PosiCharge BMID or PosiGuard without schematic evidence.

## Former ids
