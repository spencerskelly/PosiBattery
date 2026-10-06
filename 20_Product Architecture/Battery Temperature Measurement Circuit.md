---
type: Object
subtype: circuit
id: OBJ-90039
uid: 20261006060500002skellyspencer
status: Draft
tags:
  - reusable-architecture
  - battery-monitoring
  - temperature
abstract: true
reuseScope: cross-product
hasDesign:
  - "[[Battery Temperature Measurement Design]]"
dependsOn:
  - "[[Control Circuit]]"
dependencyOf:
  - "[[Battery Temperature Acquisition Firmware]]"
performs:
  - "[[Measure Battery Temperature]]"
supertypeOf:
  - "[[Thermistor Temperature Measurement Circuit]]"
---

# Battery Temperature Measurement Circuit

## Definition

Reusable hardware family for sensing battery temperature and conditioning the sensor signal for a controller.

## Notes

- This circuit family implements [[Measure Battery Temperature]].
- The concrete sensor technology and physical measurement location remain product-specific choices.
- [[Control Circuit]] provides shared acquisition/control resources but is not the temperature-sensing element itself.

## Former ids
