---
type: Design
subtype:
id: DES-90038
uid: 20261006212000001skellyspencer
status: Draft
tags:
  - battery-monitoring
  - design-characteristic
  - analytics
  - amp-hours
subtypeOf:
  - "[[Data Handling Design]]"
designOf:
  - "[[AMETEK Prestolite Power WBID]]"
  - "[[AMETEK Prestolite Power WBID Pro]]"
  - "[[Amp-Hour Accumulator Firmware]]"
  - "[[AMETEK Prestolite Power BID with Ah Accumulator]]"
  - "[[Access Control Group CellTrac]]"
  - "[[EnerSys Wi-iQ]]"
  - "[[Exide Motion+ EasyMonitor]]"
  - "[[HOPPECKE trak collect]]"
  - "[[Power Designers PowerTrac DT3]]"
  - "[[Power Designers PowerTrac SP+]]"
realizes:
  - "[[Accumulate Amp-Hours]]"
dependencyOf:
  - "[[Accumulate Amp-Hours]]"
---

# Current Integration Amp-Hour Accumulation

## Definition

Amp-hour accumulation by integrating measured battery current over elapsed time and maintaining separate or signed charge/discharge totals.

## Notes

- This is the product-backed implementation principle currently represented for [[Accumulate Amp-Hours]].
- [[AMETEK Prestolite Power BID with Ah Accumulator]] explicitly adds current monitoring, samples charge/discharge current more than 100 times per second, and tracks amp-hours including regenerative current.
- [[EnerSys Wi-iQ]], [[HOPPECKE trak collect]], [[Exide Motion+ EasyMonitor]], [[Power Designers PowerTrac DT3]], [[Power Designers PowerTrac SP+]], and [[Access Control Group CellTrac]] all publish current measurement or current-sensing behavior together with Ah charged/discharged, used, turnover, or throughput information.
- The mathematical integration principle is established, but sampling rate, numerical integration method, zero-offset correction, deadband, charge-efficiency correction, and rollover behavior remain product-specific unless published.
- Products that only **report** an Ah value received from another battery/BMS are not assigned this Design.

## Former ids
