---
type: Design
subtype:
id: DES-90902
uid: 20261006061500001skellyspencer
status: Draft
tags:
  - battery-monitoring
  - design-characteristic
  - temperature
  - thermistor
subtypeOf:
  - "[[Battery Temperature Measurement Design]]"
designOf:
  - "[[Power Designers PowerTrac 3]]"
  - "[[EnerSys Wi-iQ]]"
  - "[[Power Designers PowerTrac SP+]]"
  - "[[Thermistor Temperature Measurement Circuit]]"
describedBy:
  - "[[Metric - Temperature Sensing]]"
---

# External Thermistor Temperature Sensor

## Definition

Battery-temperature sensing using a thermistor located external to the monitoring electronics and connected to the device by wiring or a harness.

## Notes

- [[Power Designers PowerTrac 3]] explicitly specifies an external thermistor.
- [[EnerSys Wi-iQ]] explicitly specifies an external thermistor in the Wi-iQ4 manual.
- [[Power Designers PowerTrac SP+]] lists an external thermistor as an available option in its dated data sheet.
- This Design states sensor technology and external placement only. It does not claim electrolyte immersion, case attachment, or a specific thermistor part number.
- Both products can therefore share the same reusable [[Thermistor Temperature Measurement Circuit]] implementation family without implying identical physical packaging.

## Former ids

- Identity corrected 2026-10-06 from duplicate DES-90002; duplicate value is intentionally not reserved here.
