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
performs:
  - "[[Estimate State of Charge]]"
hasDesign:
  - "[[State of Charge Estimation Design]]"
supertypeOf:
  - "[[Voltage-Based State of Charge Estimator Firmware]]"
  - "[[Coulomb Counting State of Charge Estimator Firmware]]"
  - "[[Hybrid State of Charge Estimator Firmware]]"
partOf:
  - "[[HOPPECKE trak collect]]"
  - "[[Stryten M-Series Li610 Battery]]"
  - "[[EnerSys Wi-iQ]]"
  - "[[Exide Motion+ EasyMonitor]]"
  - "[[PosiCharge BMID]]"
---

# State of Charge Estimation Firmware

## Definition

Firmware that calculates battery state of charge from available measurements, battery configuration, and stored algorithm state.

## Notes

- The software performer is separated from the sensing hardware that supplies its inputs.
- The generic firmware role intentionally does not require one specific measurement set because different algorithms have different mandatory inputs.
- Algorithm-specific measurement dependencies are carried by the candidate firmware subtypes.
- **PosiCharge BMID assumption:** SOC-estimation firmware is modeled at >=95% confidence because the BMID is publicly documented as recognizing state of charge and is an electronic battery-mounted device. The exact algorithm is not public.
- **EnerSys Wi-iQ assumption:** SOC-estimation firmware is allocated at **>=95% engineering confidence** because Wi-iQ measures battery voltage/current/temperature, provides a usable SOC value to truck/charger interfaces, and already has modeled voltage-acquisition firmware. The exact SOC algorithm is not published.
- **Exide Motion+ EasyMonitor assumption:** SOC-estimation firmware is allocated at **>=95% engineering confidence** because EasyMonitor electronically acquires battery state including voltage/current-related usage data and reports SOC while its internal algorithm is unpublished.
- **HOPPECKE / Stryten assumption:** [[HOPPECKE trak collect]] and [[Stryten M-Series Li610 Battery]] are allocated the generic SOC firmware role at **>=95% engineering confidence** because the former is a battery-mounted DSP-based controller reporting SOC and the latter has an integrated BMS that reports SOC. Their exact algorithms are not published.
- No equivalent allocation is made to [[PosiCharge PosiGuard]] because the current PosiGuard evidence set does not explicitly establish that it estimates SOC.

## Former ids
