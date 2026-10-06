---
type: Design
subtype:
id: DES-90001
uid: 20261006060500001skellyspencer
status: Draft
tags:
  - general-design
  - design-characteristic
  - battery-monitoring
supertypeOf:
  - "[[Electrolyte-Immersed Temperature Sensor]]"
realizes:
  - "[[Measure Battery Temperature]]"
designOf:
  - "[[Battery Temperature Measurement Circuit]]"
  - "[[PosiCharge BMID]]"
supportedBy:
  - "[[Document - PosiCharge BMID FAQ]]"
---

# Battery Temperature Measurement Design

## Definition

General design class for measuring battery temperature and delivering a controller-readable temperature value.

## Notes

- This is the reusable implementation family for [[Measure Battery Temperature]].
- Specific implementations may sense electrolyte, battery case/cell surface, internal cell temperature, or ambient temperature; those are separate child Designs when evidence supports them.
- [[PosiCharge BMID]] is linked because public PosiCharge evidence explicitly identifies an electrolyte-immersed thermistor.
- The generic Design separates the function from the exact sensor technology, mounting location, conditioning circuit, and acquisition method.

## Former ids
