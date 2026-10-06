---
type: Object
subtype: assembly
id: OBJ-90047
uid: 20261006070000003skellyspencer
status: Draft
tags:
  - reusable-architecture
  - battery-monitoring
  - temperature
  - multifunction-sensor
reuseScope: cross-product
hasDesign:
  - "[[Wrap-Around Cell Connector Probe]]"
  - "[[Cell-Connector Temperature Sensing]]"
  - "[[Cell-Connector Electrolyte Level Sensing]]"
partOf:
  - "[[Exide Motion+ EasyMonitor]]"
performs:
  - "[[Measure Battery Temperature]]"
  - "[[Sense Electrolyte Level]]"
---

# Wrap-Around Cell Connector Sensor Assembly

## Definition

Multi-function sensor assembly wrapped around a battery cell connector to sense temperature together with electrolyte level and voltage symmetry.

## Notes

- Exide explicitly describes the [[Exide Motion+ EasyMonitor]] as using a 3-in-1 sensor installed by wrapping the probe around a cell connector.
- The published source establishes the physical mounting concept and the three measured conditions, but does not disclose the temperature-sensing technology or internal electronics.
- For this realization pass, the assembly is linked directly to [[Measure Battery Temperature]]. Its electrolyte-level and voltage-symmetry roles are already represented by the product and can be expanded when those Functions are realized in detail.

## Former ids
