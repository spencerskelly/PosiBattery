---
type: Design
subtype:
id: DES-90033
uid: 20261006193000001skellyspencer
status: Draft
tags:
  - battery-monitoring
  - design-characteristic
  - electrolyte
  - specific-gravity
subtypeOf:
  - "[[Battery Sensor Mounting Design]]"
designOf:
  - "[[AMETEK Prestolite Power TruBid]]"
  - "[[In-Cell Electrolyte Measurement Probe Assembly]]"
describedBy:
  - "[[Measure Electrolyte Specific Gravity]]"
---

# In-Cell Specific Gravity Probe

## Definition

Specific-gravity measurement using a probe inserted into a flooded battery cell and immersed in the electrolyte.

## Notes

- [[AMETEK Prestolite Power TruBid]] is the verified implementation currently represented: published sources state that its probe is inserted into a cell and continuously measures electrolyte specific gravity.
- The retrieved sources do **not** disclose whether the probe determines density through buoyancy, pressure, optical properties, conductivity, acoustic response, or another principle.
- This Design is placed under [[Battery Sensor Mounting Design]] because the strongest verified design characteristic is the in-cell probe arrangement. If a second, materially different specific-gravity sensing principle is found, create a dedicated general specific-gravity measurement Design family and re-parent the implementations.
- The Design does not imply that the temperature and specific-gravity channels use the same sensing element, only that the published TruBID probe assembly performs both measurements.

## Former ids
