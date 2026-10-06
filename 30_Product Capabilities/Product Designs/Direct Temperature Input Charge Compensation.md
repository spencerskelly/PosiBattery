---
type: Design
subtype:
id: DES-90957
uid: 20261006234000002skellyspencer
status: Draft
tags:
  - charger
  - temperature
  - sensor-input
subtypeOf:
  - "[[Temperature-Compensated Charge Control Design]]"
dependsOn:
designOf:
  - "[[PosiCharge DVS150]]"
  - "[[Lester Summit Series II]]"
  - "[[Battery Temperature Measurement Design]]"
---

# Direct Temperature Input Charge Compensation

## Definition

Temperature-compensated charging in which the charger receives battery temperature directly from a charger-connected temperature sensor or temperature-input circuit.

## Notes

- This path applies when the charger has a dedicated battery-temperature input rather than receiving temperature through a battery communication device.
- Sensor technology, placement, connector, signal conditioning, calibration, and input scaling remain product-specific.
- [[Lester Summit Series II]] explicitly publishes a battery-temperature input and optional sensor.

## Former ids
