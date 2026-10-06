---
type: Object
subtype: circuit
id: OBJ-90084
uid: 20261006193000004skellyspencer
status: Draft
tags:
  - reusable-architecture
  - battery-monitoring
  - electrolyte
  - specific-gravity
reuseScope: cross-product
dependsOn:
  - "[[In-Cell Electrolyte Measurement Probe Assembly]]"
  - "[[Control Circuit]]"
dependencyOf:
  - "[[Specific Gravity Acquisition Firmware]]"
partOf:
  - "[[AMETEK Prestolite Power TruBid]]"
performs:
  - "[[Measure Electrolyte Specific Gravity]]"
---

# Specific Gravity Measurement Circuit

## Definition

Electronic circuit that excites, reads, conditions, or converts the output of a specific-gravity sensing element into a controller-readable signal.

## Notes

- Allocation to [[AMETEK Prestolite Power TruBid]] is an **>=95% engineering-confidence assumption** because TruBID continuously measures specific gravity and electronically communicates/uses that measurement, while its internal circuitry is not published.
- Depending on the undisclosed sensor principle, a realization could use bridge excitation, oscillator/frequency measurement, optical drive/readout, analog amplification, ADC conversion, or a dedicated sensor IC.
- No specific circuit topology is selected without stronger evidence.

## Former ids
