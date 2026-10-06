---
type: Function
subtype:
id: FUNC-00005
uid: 20261002164202351skellyspencer
status: Draft
tags:
  - battery-monitoring
  - extra
  - product-function
subtypeOf:
  - "[[Sense Battery State]]"
performedBy:
  - "[[In-Cell Electrolyte Measurement Probe Assembly]]"
  - "[[Specific Gravity Sensing Element]]"
  - "[[Specific Gravity Measurement Circuit]]"
  - "[[Specific Gravity Acquisition Firmware]]"
  - "[[AMETEK Prestolite Power TruBid]]"
dependsOn:
  - "[[In-Cell Specific Gravity Probe]]"
realizedBy:
  - "[[In-Cell Specific Gravity Probe]]"
---

# Measure Electrolyte Specific Gravity

## Definition

Measure the specific gravity of the electrolyte as a charge-state indicator.

## Notes

- Only one product (Prestolite TruBid) states this in retrieved sources.
- Current public evidence establishes an in-cell probe that continuously measures specific gravity, but not the physical density-sensing principle.
- Product links are made only where a source states the behavior; no link means unknown, not absent. Overview: [[Function Map]].
- No Requirement is linked: nothing here is a committed requirement, so model-health will show these Functions without satisfied Requirements. That gap is intentional.
- **Sources** (product, evidence level, web page):
  - [[AMETEK Prestolite Power TruBid]] (V): <https://dcvelocity.com/articles/31462-ametek-s-trubid-system-accurately-measures-battery-charge>
- **Extra (round 30):** documented for 0 of 21 battery maker groups (0 percent), currently delivered by the verified [[In-Cell Specific Gravity Probe]] implementation; rule and caveats remain in [[Extra Functions Register]].

## Implementation Allocation

The only product-backed implementation currently known is [[In-Cell Specific Gravity Probe]], realized physically by [[In-Cell Electrolyte Measurement Probe Assembly]].

### Verified physical path

- [[AMETEK Prestolite Power TruBid]] places a probe in a flooded battery cell and continuously measures electrolyte specific gravity.
- [[Specific Gravity Sensing Element]] represents the required physical sensing role inside that probe, but remains technology-neutral because the source does not disclose the transduction principle.
- The same published probe assembly also monitors electrolyte temperature, so [[In-Cell Electrolyte Measurement Probe Assembly]] performs both this Function and [[Measure Battery Temperature]].

### Electronic acquisition path

- [[Specific Gravity Measurement Circuit]] represents the sensor excitation/readout/conditioning role and is allocated to TruBID at **>=95% engineering confidence**.
- [[Specific Gravity Acquisition Firmware]] represents conversion, calibration, filtering and reporting of the measured value and is allocated at **>=95% engineering confidence**.
- Neither allocation claims a particular ADC, optical interface, pressure sensor, bridge circuit, density model, calibration curve or temperature-compensation algorithm.

### Sensing-principle boundary

Potential specific-gravity sensing methods include buoyancy, hydrostatic pressure, optical/refractive measurement, conductivity-related inference, acoustic methods, or other density-sensitive transducers. None is assigned to TruBID from the available evidence.

Because only one product-backed implementation exists, the Function currently depends directly on [[In-Cell Specific Gravity Probe]]. If a second materially different implementation is found, generalize these implementations under a dedicated specific-gravity measurement Design family.

## Aliases


## Former ids
