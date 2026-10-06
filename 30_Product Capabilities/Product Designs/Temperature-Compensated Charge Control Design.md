---
type: Design
subtype:
id: DES-90956
uid: 20261006234000001skellyspencer
status: Draft
tags:
  - charger
  - temperature
  - charge-control
supertypeOf:
  - "[[Direct Temperature Input Charge Compensation]]"
  - "[[Communicated Battery Temperature Charge Compensation]]"
designOf:
  - "[[Temperature Compensation Charge Control Firmware]]"
realizes:
  - "[[Compensate Charge for Battery Temperature]]"
dependencyOf:
  - "[[Compensate Charge for Battery Temperature]]"
dependsOn:
  - "[[Charger Power Stage Design]]"
---

# Temperature-Compensated Charge Control Design

## Definition

Reusable charger-control design that adjusts charge current, voltage, end point, or phase behavior according to battery temperature.

## Notes

- The Design represents charger-side compensation behavior, not temperature sensing itself.
- A temperature value can arrive from a direct charger-connected sensor or from a battery monitor, ID device, or BMS.
- [[Direct Temperature Input Charge Compensation]] covers charger-local temperature inputs.
- [[Communicated Battery Temperature Charge Compensation]] covers temperature delivered through a battery/charger communication path.
- The charger power stage executes the resulting current/voltage commands.
- Exact compensation slope, reference temperature, chemistry-specific limits, filtering, sensor-fault behavior, minimum/maximum thresholds, and fallback remain product-specific.

## Former ids
