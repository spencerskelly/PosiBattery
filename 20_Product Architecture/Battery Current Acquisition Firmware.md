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
  - "[[Amp-Hour Accumulator Firmware]]"
  - "[[Coulomb Counting State of Charge Estimator Firmware]]"
  - "[[Hybrid State of Charge Estimator Firmware]]"
partOf:
  - "[[AMETEK Prestolite Power BID with Ah Accumulator]]"
  - "[[Access Control Group CellTrac]]"
  - "[[EnerSys Wi-iQ]]"
  - "[[Exide Motion+ EasyMonitor]]"
  - "[[HOPPECKE trak collect]]"
  - "[[Power Designers PowerTrac DT3]]"
  - "[[Power Designers PowerTrac SP+]]"
  - "[[PosiCharge PosiGuard]]"
---

# Battery Current Acquisition Firmware

Firmware that samples, calibrates, and reports the battery-current measurement.

## Notes

- [[PosiCharge PosiGuard]] allocation is a >=95% engineering assumption because the product publicly reports a digital current measurement with stated resolution.
- The sensing topology remains unknown for generic allocations.
- The amp-hour accumulator products are allocated this acquisition firmware role at **>=95% engineering confidence** because numerical Ah accumulation requires calibrated current samples, while their internal acquisition firmware partition is unpublished.

## Former ids
