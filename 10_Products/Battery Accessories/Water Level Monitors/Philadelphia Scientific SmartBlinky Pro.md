---
type: Object
subtype: electrical
id: OBJ-00009
uid: 20261002150858945skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - forklift
  - lead-acid
  - scope-aftermarket
  - water-level
subtypeOf:
  - "[[Battery Water Level Monitor]]"
performs:
  - "[[Sense Electrolyte Level]]"
  - "[[Alert on Abnormal Condition]]"
  - "[[Indicate Battery Status Locally]]"
  - "[[Alert on Low Electrolyte Level]]"
hasDesign:
  - "[[Electronic In-Cell Electrolyte Probe]]"
  - "[[Local Low Electrolyte Alert]]"
  - "[[Local LED Indicator]]"
  - "[[Audible Alarm]]"
  - "[[Cable-Mounted Indicator Placement]]"
  - "[[Reverse-Polarity Protection]]"
hasPart:
  - "[[Electrolyte Level Acquisition Firmware]]"
  - "[[Electrolyte Level Measurement Circuit]]"
  - "[[Electronic Electrolyte Probe Assembly]]"
  - "[[LED Status Indicator Element]]"
  - "[[Audible Alarm Transducer]]"
  - "[[Low Electrolyte Alert Logic]]"
madeBy:
  - "[[Philadelphia Scientific]]"
---

# Philadelphia Scientific SmartBlinky Pro

## Definition

Philadelphia Scientific battery-installed electrolyte level monitor with visual and audible watering indication.

## Notes

**Summary:**
Philadelphia Scientific battery water-level monitor with smart sensing, delay and an audible alarm that signals when batteries need water.

**Marketed features:**
- Patented Smart Sensing and 24-hour SmartDELAY to avoid false indication and over-watering
- SmartBEEP audible alarm, frequency shows days low
- Multi-state LED (OK, fill soon, fill now, filled); SmartMOUNT on the battery cable
- Universal voltage and polarity; ANYCELL probe placement
- Standard and remote versions; FlexiTap, M4 or M10 connections
- UL Classified; for forklifts, scrubbers, aerial and marine

**Summary and features sources:**
Maker or publisher marketing claims as stated, not independently verified.
- Philadelphia Scientific (T1), retrieved 2026-10-04. <https://www.phlsci.com/products/blinky-battery-watering-monitors/smartblinky-pro/>
- Material Handling Wholesaler (T2), retrieved 2026-10-04. <https://www.mhwmag.com/?p=7981>

- Manufacturer: Philadelphia Scientific
- Market evidence checked: 2026-10-02
- Installation locus: battery-mounted electronic probe sensing electrolyte in a cell.
- Published applications include forklifts, scrubbers, aerial-access equipment, buggies, and marine.
- Published indication includes LED water-level status and SmartBEEP audible alarm.
- Vendor states compatibility with industrial lead-acid batteries and multiple battery connection types.
- Evidence: https://www.phlsci.com/products/blinky-battery-watering-monitors/smartblinky-pro/
- **Verification 2026-10-02 (partly re-verified (dated source)):** the LED indicator is mounted on the battery cable near the connector, with an audible SmartBEEP alarm and universal voltage and polarity, aimed at fast and opportunity charging where the battery stays in the truck. Source: M H&W magazine product item and award entry (undated, likely older) (T2) <https://www.mhwmag.com/?p=7981>
- **Refinement 2026-10-05:** Philadelphia Scientific's current product page explicitly states that SmartBlinky Pro is an electronic probe that senses electrolyte in a cell. The page names patented Smart Sensing Technology but does not disclose whether the underlying principle is conductive, capacitive, optical, or another method. This supports [[Electronic In-Cell Electrolyte Probe]] and [[Electronic Electrolyte Probe Assembly]].
- **Functions performed, with citations** (V = verified this pass, C = carried from seed text, U = user-stated):
  - [[Sense Electrolyte Level]] (V): <https://www.mhwmag.com/?p=7981>
  - [[Alert on Abnormal Condition]] (V): <https://www.mhwmag.com/?p=7981>
  - [[Indicate Battery Status Locally]] (V): <https://www.mhwmag.com/?p=7981>
  - [[Alert on Low Electrolyte Level]] (V): <https://www.phlsci.com/products/blinky-battery-watering-monitors/smartblinky-pro/>
- **Design characteristics, with citations:**
  - [[Electronic In-Cell Electrolyte Probe]] (V): <https://www.phlsci.com/products/blinky-battery-watering-monitors/smartblinky-pro/>
  - [[Local LED Indicator]] (V): <https://www.mhwmag.com/?p=7981>
  - [[Audible Alarm]] (V): <https://www.mhwmag.com/?p=7981>
  - [[Cable-Mounted Indicator Placement]] (V): <https://www.mhwmag.com/?p=7981>
  - [[Reverse-Polarity Protection]] (V): <https://www.mhwmag.com/?p=7981>
- **Sources used for the mapping above:** M H&W magazine item (undated, likely older) <https://www.mhwmag.com/?p=7981>
- **Implementation assumption — low electrolyte alert logic:** [[Low Electrolyte Alert Logic]] is allocated at **>=95% engineering confidence** because SmartBlinky Pro publishes SmartDELAY, multi-state LED alerting, and SmartBEEP behavior. The public source does not disclose whether this behavior is firmware, programmable logic, or dedicated electronics, so the reusable software-role Object captures the decision behavior rather than a specific MCU implementation.
- **Truck parts (round 31):** typical (inferred from the device type, not from a source): mounts on [[Truck Battery Compartment]]. See [[Truck Part Connection Register]].

## Aliases

- SmartBlinky Pro
- Smart Blinky Pro


## Former ids
