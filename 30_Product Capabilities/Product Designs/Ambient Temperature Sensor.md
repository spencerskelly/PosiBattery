---
type: Design
subtype:
id: DES-90904
uid: 20261006062500001skellyspencer
status: Draft
tags:
  - battery-monitoring
  - design-characteristic
  - temperature
subtypeOf:
  - "[[Battery Temperature Measurement Design]]"
designOf:
  - "[[Ambient Temperature Sensor Element]]"
  - "[[AMETEK Prestolite Power WBID Pro]]"
describedBy:
  - "[[Metric - Temperature Sensing]]"
---

# Ambient Temperature Sensor

## Definition

Temperature sensing of the air or local environment surrounding the battery or monitoring device rather than direct electrolyte or cell temperature.

## Notes

- [[AMETEK Prestolite Power WBID Pro]] explicitly identifies ambient temperature sensing in addition to electrolyte temperature sensing.
- This Design represents measurement locus, not sensor technology. The public source does not identify whether the ambient sensor is a thermistor, semiconductor sensor, RTD, or another technology.
- Ambient temperature is intentionally kept distinct from [[Electrolyte-Immersed Temperature Sensor]], [[External Thermistor Temperature Sensor]], and [[Internal Temperature Sensor]] because the measured physical quantity differs.
- [[Ambient Temperature Sensor Element]] captures the verified physical sensor occurrence without selecting a technology.
- No concrete circuit subtype is assigned until the sensor technology is established.

## Former ids

- Identity corrected 2026-10-06 from duplicate DES-90004; duplicate value is intentionally not reserved here.
