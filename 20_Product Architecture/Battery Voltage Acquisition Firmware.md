---
type: Object
subtype: firmware
id: OBJ-90026
uid: 20261005213400013skellyspencer
status: Draft
tags:
  - reusable-architecture
  - firmware
  - battery-monitoring
reuseScope: cross-product
dependsOn:
  - "[[Control Circuit]]"
  - "[[Battery Voltage Measurement Circuit]]"
performs:
  - "[[Measure Battery Voltage]]"
partOf:
  - "[[EnerSys Wi-iQ]]"
  - "[[Exide Motion+ EasyMonitor]]"
  - "[[PosiCharge BMID]]"
  - "[[PosiCharge PosiGuard]]"
dependencyOf:
  - "[[Voltage-Based State of Charge Estimator Firmware]]"
  - "[[Hybrid State of Charge Estimator Firmware]]"
  - "[[Voltage Imbalance Evaluation Firmware]]"
---

# Battery Voltage Acquisition Firmware

## Definition

Firmware that samples the battery-voltage measurement channel, applies scaling/calibration, and provides a usable engineering value to higher-level battery functions.

## Notes

- Complements the analog measurement circuit; it does not imply a specific ADC or divider topology.
- **PosiCharge BMID / PosiGuard assumption:** software/firmware scaling of the measured voltage is >=95% likely for an electronic monitor reporting a digital voltage value, but the internal implementation is not publicly documented.
- Allocation to [[EnerSys Wi-iQ]] and [[Exide Motion+ EasyMonitor]] is likewise **>=95% engineering confidence** because both electronically acquire overall/midpoint voltage values used for imbalance detection; their internal acquisition firmware is not published.

## Former ids
