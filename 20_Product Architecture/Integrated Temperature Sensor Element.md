---
type: Object
subtype: component
id: OBJ-90045
uid: 20261006070000001skellyspencer
status: Draft
tags:
  - reusable-architecture
  - battery-monitoring
  - temperature
reuseScope: cross-product
hasDesign:
  - "[[Internal Temperature Sensor]]"
partOf:
  - "[[Philadelphia Scientific eGO!core]]"
  - "[[Philadelphia Scientific eGO!plus]]"
  - "[[Philadelphia Scientific eGO!pro]]"
performs:
  - "[[Measure Battery Temperature]]"
---

# Integrated Temperature Sensor Element

## Definition

Temperature-sensing component integrated inside a battery monitoring device when the published source identifies an internal sensor but does not disclose the sensing technology.

## Notes

- Philadelphia Scientific explicitly states that [[Philadelphia Scientific eGO!core]], [[Philadelphia Scientific eGO!plus]], and [[Philadelphia Scientific eGO!pro]] include an internal temperature sensor.
- The component is modeled generically because the public sources do not identify thermistor, RTD, semiconductor, package, part number, or the exact thermal coupling to the battery.
- This Object realizes the physical sensor occurrence without asserting a circuit topology that is not published.

## Former ids
