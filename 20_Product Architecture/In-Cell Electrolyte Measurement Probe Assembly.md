---
type: Object
subtype: assembly
id: OBJ-90082
uid: 20261006193000002skellyspencer
status: Draft
tags:
  - reusable-architecture
  - battery-monitoring
  - electrolyte
  - probe
reuseScope: cross-product
hasDesign:
  - "[[In-Cell Specific Gravity Probe]]"
  - "[[Electrolyte-Immersed Temperature Sensor]]"
hasPart:
  - "[[Specific Gravity Sensing Element]]"
partOf:
  - "[[AMETEK Prestolite Power TruBid]]"
performs:
  - "[[Measure Electrolyte Specific Gravity]]"
  - "[[Measure Battery Temperature]]"
dependencyOf:
  - "[[Specific Gravity Measurement Circuit]]"
  - "[[Measure Battery Temperature]]"
---

# In-Cell Electrolyte Measurement Probe Assembly

## Definition

Probe assembly inserted into a flooded battery cell to measure one or more electrolyte properties.

## Notes

- [[AMETEK Prestolite Power TruBid]] explicitly uses an in-cell probe that continuously monitors electrolyte temperature and specific gravity.
- The source verifies the shared probe assembly and the two measured properties, but does not reveal whether those properties use separate sensor elements, a shared transducer, or integrated electronics.
- The assembly therefore contains only a technology-neutral [[Specific Gravity Sensing Element]] for the specific-gravity role; the temperature sensing technology remains unspecified for TruBID.

## Former ids
