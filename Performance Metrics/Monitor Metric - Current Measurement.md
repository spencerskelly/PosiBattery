---
type: Info
subtype:
id: INFO-00132
uid: 20261002195812524skellyspencer
status: Draft
tags:
  - performance-metric
  - monitor
  - comparison
describes:
  - "[[Battery Monitoring and Identification Device]]"
  - "[[Measure Battery Current]]"
  - "[[External Shunt Current Sensing]]"
  - "[[Shuntless Current Sensing]]"
  - "[[Hall-Effect Current Sensing]]"
  - "[[Split-Core Current Sensor]]"
---

# Monitor Metric - Current Measurement

## Definition

Current Measurement: Method and range of battery current measurement.

## Notes

- **Code and class:** MM04; monitor metric. Unit or format: method; A range; resolution; accuracy.
- **Comparability rule:** Permanent range, peak range and sensor range differ; shunt and Hall types are not directly comparable on accuracy; note bidirectional.
- **Direction:** wider range and finer resolution.
- **Values on file (as stated in each product note; n/s means not stated):**
  - [[AMETEK Prestolite Power BID with Ah Accumulator]]: samples charge and discharge current over 100 times per second; stores every Ah incl. regeneration
  - [[Access Control Group CellTrac]]: no shunt; range n/s
  - [[Advanced Charging Technologies BATTview]]: resolution +/-1 A minimum
  - [[EnerSys Wi-iQ]]: Hall; +/-1000 A; 1 A resolution; bidirectional
  - [[HOPPECKE trak collect]]: shunt; 500 A permanent; 0 to +/-2100 A; 1% (+/-10 to 2100 A) (C39)
  - [[Philadelphia Scientific eGO!pro]]: Hall split-core; bidirectional; range n/s
  - [[PosiCharge Battery Rx]]: +/-1000 A range
  - [[PosiCharge PosiGuard]]: resolution 100 mA
  - [[Power Designers PowerTrac 3]]: sheet: shuntless intercell or Hall effect; +/-500 A typical, 1 A resolution (C47); earlier note: shuntless; range n/s
  - [[Power Designers PowerTrac DT3]]: Hall; +/-500 A typical; 1 A resolution; bidirectional
  - [[Power Designers PowerTrac SP+]]: external 50 mV shunt; 500 A shunts offered
- **Source rule:** the product note holds the source URL for each value; this note copies the value for comparison. If they differ, the product note wins and this note is fixed.
- **Gaps and to-do:** 10 product(s) have a value; document-based values to be added as documents are supplied.

## Aliases

- MM04
- Current Measurement

## Former ids
