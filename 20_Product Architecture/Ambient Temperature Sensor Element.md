---
type: Object
subtype: component
id: OBJ-90046
uid: 20261006070000002skellyspencer
status: Draft
tags:
  - reusable-architecture
  - battery-monitoring
  - temperature
reuseScope: cross-product
hasDesign:
  - "[[Ambient Temperature Sensor]]"
partOf:
  - "[[AMETEK Prestolite Power WBID Pro]]"
performs:
  - "[[Measure Battery Temperature]]"
---

# Ambient Temperature Sensor Element

## Definition

Temperature-sensing component that measures the local ambient environment around the battery or monitoring device.

## Notes

- [[AMETEK Prestolite Power WBID Pro]] explicitly distinguishes ambient temperature sensing from electrolyte temperature sensing.
- Sensor technology is not published, so this Object remains technology-neutral rather than being classified as a thermistor, RTD, or semiconductor sensor.
- The physical sensor element is modeled separately from [[Ambient Temperature Sensor]], which captures the sensing-locus Design.

## Former ids
