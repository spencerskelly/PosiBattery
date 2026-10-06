---
type: Design
subtype:
id: DES-00001
uid: 20261002164202371skellyspencer
status: Draft
tags:
  - battery-monitoring
  - design-characteristic
subtypeOf:
  - "[[Battery Temperature Measurement Design]]"
describedBy:
  - "[[Metric - Temperature Sensing]]"
designOf:
  - "[[In-Cell Electrolyte Measurement Probe Assembly]]"
  - "[[PosiCharge BMID]]"
  - "[[PosiCharge Battery Rx]]"
  - "[[AMETEK Prestolite Power TruBid]]"
  - "[[AMETEK Prestolite Power WBID Pro]]"
  - "[[PosiCharge DVS150]]"
  - "[[Thermistor Temperature Measurement Circuit]]"
realizes:
  - "[[Report Battery Temperature to Charger]]"
supportedBy:
  - "[[Document - PosiCharge BMID FAQ]]"
dependencyOf:
  - "[[Hybrid State of Charge Estimation]]"
---

# Electrolyte-Immersed Temperature Sensor

## Definition

Temperature sensor placed in the cell electrolyte, so it reads electrolyte temperature rather than case or ambient temperature.

## Notes

- Stated for PosiCharge BMID, Battery Rx, Prestolite TruBid and WBID Pro. Whether other products immerse the sensor is not stated.
- For [[PosiCharge BMID]], the source further identifies the sensing technology as a thermistor; see [[Thermistor Temperature Measurement Circuit]] and [[Thermistor Temperature Sensor]].
- Product links are made only where a source states it. This note records a design characteristic found in products, not a decision by us. Overview: [[Design Map]].
- No Requirement is linked and nothing is satisfied; see the note on Functions for why.
- **Sources** (product, evidence level, web page):
  - [[PosiCharge BMID]] (V): <https://www.posicharge.com/faq/>
  - [[PosiCharge Battery Rx]] (V): <https://www.posicharge.com/source/PDF/BatteryRx.pdf>
  - [[AMETEK Prestolite Power WBID Pro]] (V): <https://www.prestolitepower.com/products/datadevices/wbid-pro>
  - [[AMETEK Prestolite Power TruBid]] (V): <https://dcvelocity.com/articles/31462-ametek-s-trubid-system-accurately-measures-battery-charge>
  - [[PosiCharge DVS150]] (V): <https://posicharge.com/products/dvs150/>

## Aliases


## Former ids
