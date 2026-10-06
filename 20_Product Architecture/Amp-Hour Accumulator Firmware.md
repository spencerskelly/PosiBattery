---
type: Object
subtype: firmware
id: OBJ-90093
uid: 20261006212000002skellyspencer
status: Draft
tags:
  - reusable-architecture
  - firmware
  - battery-monitoring
  - amp-hours
reuseScope: cross-product
hasDesign:
  - "[[Current Integration Amp-Hour Accumulation]]"
dependsOn:
  - "[[Battery Current Acquisition Firmware]]"
  - "[[Control Circuit]]"
partOf:
  - "[[AMETEK Prestolite Power WBID]]"
  - "[[AMETEK Prestolite Power WBID Pro]]"
  - "[[AMETEK Prestolite Power BID with Ah Accumulator]]"
  - "[[Access Control Group CellTrac]]"
  - "[[EnerSys Wi-iQ]]"
  - "[[Exide Motion+ EasyMonitor]]"
  - "[[HOPPECKE trak collect]]"
  - "[[Power Designers PowerTrac DT3]]"
  - "[[Power Designers PowerTrac SP+]]"
performs:
  - "[[Accumulate Amp-Hours]]"
---

# Amp-Hour Accumulator Firmware

## Definition

Firmware that numerically integrates battery current over time to maintain charge, discharge, event, interval, or lifetime amp-hour counters.

## Notes

- The reusable implementation consumes calibrated current samples from [[Battery Current Acquisition Firmware]].
- [[Amp-Hour Counter State Memory]] is an optional supporting component for persistent/lifetime counters rather than a mandatory dependency for every session-level accumulator.
- Typical responsibilities include sample-time handling, sign convention, numerical integration, offset/deadband handling, counter rollover, event boundaries, and forwarding accumulated values to logging or reporting functions.
- Allocation to the listed products is **>=95% engineering confidence** where the product explicitly combines current monitoring or persistent Ah-in/out accumulation with battery-side electronic processing while the internal firmware partition is unpublished.
- [[AMETEK Prestolite Power BID with Ah Accumulator]] provides especially strong evidence because Prestolite states that it samples charge and discharge current more than 100 times per second and stores every amp-hour including regeneration.
- The exact integration algorithm and sampling architecture are not asserted.

## Former ids
