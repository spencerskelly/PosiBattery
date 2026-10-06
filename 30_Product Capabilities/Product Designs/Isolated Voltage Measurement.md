---
type: Design
subtype:
id: DES-90005
uid: 20261005213400003skellyspencer
status: Draft
tags:
  - product-design
  - battery-monitoring
  - voltage
  - isolation
subtypeOf:
  - "[[Battery Voltage Measurement Design]]"
designOf:
  - "[[Isolated Voltage Measurement Circuit]]"
---

# Isolated Voltage Measurement

## Definition

Battery-voltage measurement using galvanically isolated analog or digital transfer between the battery measurement domain and the controller domain.

## Notes

Candidate realizations include:
- isolation amplifier;
- isolated ADC;
- sigma-delta modulator plus digital isolation;
- isolated measurement module.

Use when safety, common-mode range, grounding, or system partitioning requires isolation. No PosiCharge implementation is assumed.

## Former ids
