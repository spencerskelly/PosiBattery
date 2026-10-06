---
type: Object
subtype: firmware
id: OBJ-90038
uid: 20261005222810011skellyspencer
status: Draft
tags:
  - reusable-architecture
  - firmware
  - battery-monitoring
reuseScope: cross-product
dependsOn:
  - "[[Control Circuit]]"
  - "[[Battery Current Measurement Circuit]]"
performs:
  - "[[Measure Battery Current]]"
dependencyOf:
  - "[[Coulomb Counting State of Charge Estimator Firmware]]"
  - "[[Hybrid State of Charge Estimator Firmware]]"
partOf:
  - "[[PosiCharge PosiGuard]]"
---

# Battery Current Acquisition Firmware

Firmware that samples, calibrates, and reports the battery-current measurement.

## Notes

- [[PosiCharge PosiGuard]] allocation is a >=95% engineering assumption because the product publicly reports a digital current measurement with stated resolution.
- The sensing topology remains unknown.

## Former ids
