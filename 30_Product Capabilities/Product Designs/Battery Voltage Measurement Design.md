---
type: Design
subtype:
id: DES-90003
uid: 20261005213400001skellyspencer
status: Draft
tags:
  - product-design
  - battery-monitoring
  - voltage
supertypeOf:
  - "[[Resistive Divider ADC Voltage Measurement]]"
  - "[[Isolated Voltage Measurement]]"
  - "[[Mid-Battery Differential Voltage Measurement]]"
realizes:
  - "[[Measure Battery Voltage]]"
---

# Battery Voltage Measurement Design

## Definition

General implementation design for measuring traction-battery terminal voltage and converting it into a digital value usable by product firmware.

## Notes

The design family supports several implementation paths:
- [[Resistive Divider ADC Voltage Measurement]] for direct high-impedance scaling into an ADC.
- [[Isolated Voltage Measurement]] when galvanic isolation is required between the battery measurement domain and the controller domain.
- [[Mid-Battery Differential Voltage Measurement]] when a midpoint/balance tap is used to compare battery halves in addition to overall terminal voltage.

A product should select the narrowest supported implementation rather than inheriting every alternative.

## Former ids
