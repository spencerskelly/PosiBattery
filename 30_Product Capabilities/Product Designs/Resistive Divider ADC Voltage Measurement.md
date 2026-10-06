---
type: Design
subtype:
id: DES-90004
uid: 20261005213400002skellyspencer
status: Draft
tags:
  - general-design
  - battery-monitoring
  - voltage
subtypeOf:
  - "[[Battery Voltage Measurement Design]]"
designOf:
  - "[[Resistive Divider ADC Voltage Measurement Circuit]]"
---

# Resistive Divider ADC Voltage Measurement

## Definition

Voltage-measurement design that scales battery terminal voltage with a high-value resistive divider, conditions/protects the signal, and samples it with an ADC.

## Notes

Typical implementation elements include:
- high-value precision resistor divider;
- input protection;
- RC filtering;
- ADC input on a controller or external ADC;
- firmware scaling/calibration.

This is a common candidate for battery-mounted monitoring electronics, but it is not assigned to a specific PosiCharge product without schematic evidence.

## Former ids
