---
type: Object
subtype: electrical
id: OBJ-90916
uid: 20261014000000022skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - lithium
  - bms
  - external-product
subtypeOf:
  - "[[Battery Management System]]"
performs:
  - "[[Measure Battery Voltage]]"
  - "[[Measure Battery Current]]"
  - "[[Measure Battery Temperature]]"
  - "[[Estimate State of Charge]]"
  - "[[Accumulate Amp-Hours]]"
madeBy:
  - "[[Batrium]]"
hasDesign:
  - "[[Standalone Battery Management System]]"
---

# Batrium ShuntMon2

## Definition

Shunt-based sensor of the Batrium BMS that measures voltage, current and temperature and tracks amp-hours in and out for state of charge.

## Notes

**Summary:**
Shunt-based sensor of the Batrium BMS that measures voltage, current and temperature and tracks amp-hours in and out for state of charge.

**Marketed features:**
- Measures voltage, current and temperature
- Tracks Ah in and out to determine SOC%
- Current accuracy typically plus or minus 1.0%
- 500 A (400 A continuous) or 1000 A (800 A continuous) versions, maximum 650 VDC
- Built-in isolation for power and serial communication

**Summary and features sources:**
Maker or publisher marketing claims as stated, not independently verified.
- [[Document - Batrium BMS Product Guide (undated)]] <https://wiki.batrium.com/documents/batrium_bms_product_guide.pdf>

- Manufacturer: Batrium
- External product: not made by PosiCharge; recorded to define BMS functions and designs (owner decision 2026-10-13).
- Design note: it is a sensor in the master and cell monitor arrangement of the same system, but the guide does not say how it connects, so it is not linked to that topology.
- **Not stated in the sources read:** the serial protocol; temperature measurement range; SOC method beyond Ah counting and its drift handling.
- **Functions performed, with citations** (V = verified this pass):
  - [[Measure Battery Voltage]] (V): guide
  - [[Measure Battery Current]] (V): guide
  - [[Measure Battery Temperature]] (V): guide
  - [[Estimate State of Charge]] (V): guide: Ah in and out to SOC%
  - [[Accumulate Amp-Hours]] (V): guide: tracks Ah in and out
- See [[External BMS Product Landscape]] for the comparison.


## Aliases



## Former ids
