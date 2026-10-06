---
type: Design
subtype:
id: DES-90008
uid: 20261006074500001skellyspencer
status: Draft
tags:
  - battery-monitoring
  - design-characteristic
  - temperature
  - cell-connector
subtypeOf:
  - "[[Battery Temperature Measurement Design]]"
designOf:
  - "[[Wrap-Around Cell Connector Sensor Assembly]]"
  - "[[Exide Motion+ EasyMonitor]]"
realizes:
  - "[[Measure Battery Temperature]]"
describedBy:
  - "[[Metric - Temperature Sensing]]"
---

# Cell-Connector Temperature Sensing

## Definition

Battery-temperature sensing at or through a cell-connector-mounted sensor assembly.

## Notes

- [[Exide Motion+ EasyMonitor]] is the verified implementation currently represented: Exide states that its 3-in-1 sensor wraps around a cell connector and measures temperature, electrolyte level, and voltage symmetry.
- This Design captures the **temperature-sensing implementation**. [[Wrap-Around Cell Connector Probe]] separately captures the **mounting arrangement** of the same physical [[Wrap-Around Cell Connector Sensor Assembly]].
- Keeping these as separate Designs preserves the vault rule that each specific Design has one general parent while allowing one physical assembly to embody multiple design characteristics.
- The temperature-sensing technology inside the assembly is not published.

## Former ids
