---
type: Function
subtype:
id: FUNC-00024
uid: 20261002164202370skellyspencer
status: Draft
tags:
  - battery-monitoring
  - extra
  - product-function
subtypeOf:
  - "[[Sense Battery State]]"
performedBy:
  - "[[Raymond iBattery]]"
  - "[[Battery Weight Verification Firmware]]"
  - "[[Load-Cell Battery Weight Measurement Assembly]]"
  - "[[Battery Weight Acquisition Firmware]]"
dependsOn:
  - "[[Battery Weight Determination Design]]"
realizedBy:
  - "[[Battery Weight Determination Design]]"
---

# Detect Battery Weight

## Definition

Determine the battery's weight or stored weight specification, for example to verify compatibility with a truck.

## Notes

- Stated only for Raymond iBattery.
- Product links are made only where a source states the behavior; no link means unknown, not absent. Overview: [[Function Map]].
- No Requirement is linked: nothing here is a committed requirement, so model-health will show these Functions without satisfied Requirements. That gap is intentional.
- **Sources** (product, evidence level, web page):
  - [[Raymond iBattery]] (V): <https://mhlnews.com/archive/article/22045964/raymond-battery-module>
  - [[Raymond iBattery]] implementation architecture (V): <https://patents.google.com/patent/CA2733079A1/en>
- **Extra (round 30):** documented for 1 of 21 battery maker groups (5 percent), delivered by devices or software; the reusable realization family is now [[Battery Weight Determination Design]]. Rule and caveats remain in [[Extra Functions Register]].

## Implementation Allocation

The reusable realization family is [[Battery Weight Determination Design]], with two concrete alternatives.

### Product-backed stored-specification method

[[Stored Battery Weight Compatibility Verification]] is verified for [[Raymond iBattery]] from Raymond's battery-monitoring patent:

[[Battery Specification Memory]] -> [[Power-Line Communication Circuit]] -> [[Battery Weight Verification Firmware]]

The battery sensor module stores manufacturer specification data including a battery-weight value. When the battery is installed, the vehicle controller requests the specification record over the battery-cable power-line communication path, compares the stored battery weight with the vehicle minimum, and can restrict operation if the battery is too light.

This is a **stored-data verification method**, not a physical scale. The model therefore does not assign a load cell, strain gauge, or force sensor to Raymond iBattery.

### Direct physical measurement alternative

[[Direct Load-Cell Battery Weight Measurement]] remains a concrete reusable engineering option:

[[Load-Cell Battery Weight Measurement Assembly]] -> [[Battery Weight Acquisition Firmware]]

The assembly can use [[Load Cell Weight Sensor]] elements with [[Load Cell Signal Conditioning Circuit]] electronics and calibration/tare logic. No current product in the evidence set is assigned this Design.

### Interface boundary

The Raymond source makes the battery-to-vehicle data path clear, but no standalone Interface/Connection notes are added here because governed contextual endpoint instances are not yet established for this product interaction. The physical path is captured by [[DC-Cable Power-Line Communication]] and [[Power-Line Communication Circuit]].

## Aliases


## Former ids
