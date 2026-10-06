---
type: Object
subtype: firmware
id: OBJ-90042
uid: 20261006060500005skellyspencer
status: Draft
tags:
  - reusable-architecture
  - firmware
  - battery-monitoring
  - temperature
reuseScope: cross-product
dependsOn:
  - "[[Control Circuit]]"
  - "[[Battery Temperature Measurement Circuit]]"
performs:
  - "[[Measure Battery Temperature]]"
dependencyOf:
  - "[[Hybrid State of Charge Estimator Firmware]]"
partOf:
  - "[[PosiCharge BMID]]"
---

# Battery Temperature Acquisition Firmware

Firmware that samples, converts, calibrates, and reports battery-temperature measurements.

## Notes

- [[PosiCharge BMID]] allocation is a **>=95% engineering assumption** because the product contains an electronic device and explicitly measures battery temperature using an electrolyte-immersed thermistor.
- The public evidence does not disclose the acquisition algorithm, filtering, calibration coefficients, ADC implementation, or firmware partitioning.

## Former ids
