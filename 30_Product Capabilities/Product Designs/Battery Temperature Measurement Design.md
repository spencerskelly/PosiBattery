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
  - "[[External Thermistor Temperature Sensor]]"
  - "[[Internal Temperature Sensor]]"
  - "[[Ambient Temperature Sensor]]"
  - "[[Wrap-Around Cell Connector Probe]]"
realizes:
  - "[[Measure Battery Temperature]]"
dependencyOf:
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
- Specific implementations may sense electrolyte, battery case/cell surface, internal device temperature, or ambient temperature; those are separate child Designs when evidence supports them.
- [[Electrolyte-Immersed Temperature Sensor]] captures immersed-probe placement.
- [[External Thermistor Temperature Sensor]] captures products that explicitly use an externally connected thermistor.
- [[Internal Temperature Sensor]] captures products that explicitly integrate the sensor inside the monitor but do not disclose the sensing technology.
- [[Ambient Temperature Sensor]] captures products that explicitly distinguish surrounding-air temperature from direct battery temperature.
- [[Wrap-Around Cell Connector Probe]] captures the Exide 3-in-1 sensor arrangement where temperature is measured at a cell connector.
- Case/surface-mounted and cell-integrated temperature sensing remain unmodeled because the current product evidence does not establish a specific implementation.
- The generic Design separates the function from the exact sensor technology, mounting location, conditioning circuit, and acquisition method.

## Former ids
