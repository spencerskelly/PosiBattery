---
type: Object
subtype: firmware
id: OBJ-90027
uid: 20261005222800005skellyspencer
status: Draft
tags:
  - reusable-architecture
  - firmware
  - battery-monitoring
reuseScope: cross-product
dependsOn:
  - "[[Control Circuit]]"
  - "[[Battery Voltage Acquisition Firmware]]"
performs:
  - "[[Estimate State of Charge]]"
hasDesign:
  - "[[State of Charge Estimation Design]]"
partOf:
  - "[[PosiCharge BMID]]"
---

# State of Charge Estimation Firmware

## Definition

Firmware that calculates battery state of charge from available measurements, battery configuration, and stored algorithm state.

## Notes

- The software performer is separated from the sensing hardware that supplies its inputs.
- The BMID family is already modeled with battery-voltage measurement, so voltage is a defensible input to the generic implementation.
- Some child algorithms additionally require battery current and temperature.
- **PosiCharge BMID assumption:** SOC-estimation firmware is modeled at >=95% confidence because the BMID is publicly documented as recognizing state of charge and is an electronic battery-mounted device. The exact algorithm is not public.
- No equivalent allocation is made to [[PosiCharge PosiGuard]] because the current PosiGuard evidence set does not explicitly establish that it estimates SOC.

## Former ids
