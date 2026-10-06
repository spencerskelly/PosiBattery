---
type: Function
subtype:
id: FUNC-00025
uid: 20261002165629051skellyspencer
status: Draft
tags:
  - battery-monitoring
  - extra
  - product-function
subtypeOf:
  - "[[Sense Battery State]]"
performedBy:
  - "[[Mid-Battery Differential Voltage Measurement Circuit]]"
  - "[[Voltage Imbalance Evaluation Firmware]]"
  - "[[Voltage Imbalance Comparator Circuit]]"
  - "[[EnerSys Wi-iQ]]"
  - "[[Exide Motion+ EasyMonitor]]"
  - "[[Hyster Battery Tracker]]"
dependsOn:
  - "[[Voltage Imbalance Detection Design]]"
realizedBy:
  - "[[Voltage Imbalance Detection Design]]"
realizes:
  - "[[Prevent Battery Abuse and Premature Replacement]]"
---

# Detect Voltage Imbalance

## Definition

Detect imbalance between the two halves of the battery or between cells, usually from a mid-battery voltage reading.

## Notes

- Verified detection is stated for Wi-iQ (overall and half-battery voltage / balance input), Exide Motion+ EasyMonitor (middle-voltage tap / voltage symmetry), and Hyster Battery Tracker (imbalance exception reporting; sensing topology not published).
- [[EnerSys Truck iQ]] was removed as a performer on 2026-10-06: its source says it **displays** cell imbalance received from Wi-iQ over BLE, which supports [[Display Battery Status to Operator]] rather than proving that Truck iQ performs the detection.
- Citations are listed under Sources below. Links to products are made only where a source states the behavior.
- **Sources** (product, evidence level, web page):
  - [[EnerSys Wi-iQ]] (V): <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>
  - [[Exide Motion+ EasyMonitor]] (V): <https://www.exidegroup.com/en/product/easymonitor> <https://www.exidegroup.com/en/document/easy-monitor-leaflet>
  - [[Hyster Battery Tracker]] (V): <https://www.hyster.com/4a9a28/globalassets/coms/hyster/north-america/documents/telematics/0109het6fc001_e_en-us_battery-tracker-flyer.pdf>
- **Extra (round 30):** documented for 2 of 21 battery maker groups (10 percent); implementation is now traced through [[Voltage Imbalance Detection Design]]. Rule and caveats remain in [[Extra Functions Register]].

## Implementation Allocation

### Verified midpoint / symmetry path

[[Midpoint Voltage Symmetry Detection]] depends on [[Mid-Battery Differential Voltage Measurement]], implemented physically by [[Mid-Battery Voltage Tap Harness]] and [[Mid-Battery Differential Voltage Measurement Circuit]]. The circuit supplies section-voltage measurements; [[Voltage Imbalance Evaluation Firmware]] compares them and produces the imbalance state.

- **[[EnerSys Wi-iQ]]:** verified overall and half-battery voltage measurement with a balance wire. The midpoint sensing path is verified; the evaluation firmware role is an **>=95% engineering-confidence assumption** because EnerSys does not publish the internal algorithm or firmware partition.
- **[[Exide Motion+ EasyMonitor]]:** verified middle-voltage tap and voltage-symmetry / imbalance detection. The midpoint sensing path is verified; the evaluation firmware role is an **>=95% engineering-confidence assumption**.

### Hardware-only alternative

[[Voltage Imbalance Comparator Circuit]] represents a dedicated analog/comparator implementation that could detect imbalance without programmable firmware. No current product is assigned because the public sources do not establish such a topology.

### Technology-unspecified detection

[[Hyster Battery Tracker]] explicitly reports imbalance as an exception / email-alert condition, so the Function remains verified. Its public literature does **not** identify midpoint sensing, cell-level measurement, or where the imbalance algorithm runs; no specific child Design or sensing circuit is assigned.

### Presentation boundary

[[EnerSys Truck iQ]] displays cell imbalance received from [[EnerSys Wi-iQ]] over BLE. It is therefore a consumer/presentation endpoint, not a detector in this Function.

## Aliases


## Former ids
