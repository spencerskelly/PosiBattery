---
type: Design
subtype:
id: DES-90901
uid: 20261006060500001skellyspencer
status: Draft
tags:
  - general-design
  - design-characteristic
  - battery-monitoring
supertypeOf:
  - "[[Electrolyte-Immersed Temperature Sensor]]"
  - "[[External Thermistor Temperature Sensor]]"
  - "[[Internal Temperature Sensor]]"
  - "[[Ambient Temperature Sensor]]"
  - "[[Cell-Connector Temperature Sensing]]"
  - "[[BMS Internal Temperature Sensing]]"
realizes:
  - "[[Measure Battery Temperature]]"
dependencyOf:
  - "[[Measure Battery Temperature]]"
designOf:
  - "[[Battery Temperature Measurement Circuit]]"
supportedBy:
  - "[[Document - PosiCharge BMID FAQ]]"
---

# Battery Temperature Measurement Design

## Definition

General design class for measuring battery temperature and delivering a controller-readable temperature value.

## Notes

- This is the reusable implementation family for [[Measure Battery Temperature]]. Products link to the applicable specific child Design; the general class itself is not product-owned.
- Specific implementations may sense electrolyte, battery case/cell surface, internal device temperature, or ambient temperature; those are separate child Designs when evidence supports them.
- [[Electrolyte-Immersed Temperature Sensor]] captures immersed-probe placement.
- [[External Thermistor Temperature Sensor]] captures products that explicitly use an externally connected thermistor.
- [[Internal Temperature Sensor]] captures products that explicitly integrate the sensor inside the monitor but do not disclose the sensing technology.
- [[Ambient Temperature Sensor]] captures products that explicitly distinguish surrounding-air temperature from direct battery temperature.
- [[Cell-Connector Temperature Sensing]] captures temperature measurement by the Exide 3-in-1 cell-connector assembly; [[Wrap-Around Cell Connector Probe]] separately describes its mounting arrangement.
- [[BMS Internal Temperature Sensing]] captures lithium systems whose BMS monitors temperature from sensors inside the battery system; it does not imply cell-level versus module-level placement unless the source states it.
- A distinct case/surface-mounted sensing Design remains unmodeled because the current product evidence does not establish one.
- The generic Design separates the function from the exact sensor technology, mounting location, conditioning circuit, and acquisition method.

## Former ids

- Identity corrected 2026-10-06 from duplicate DES-90001; duplicate value is intentionally not reserved here.
