---
type: Object
subtype: electrical
id: OBJ-00044
uid: 20261002164202412skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - forklift
  - lead-acid
  - scope-aftermarket
  - status-unclear
subtypeOf:
  - "[[Battery Monitoring Device]]"
  - "[[Battery Identification and Charge Interface Device]]"
describedBy:
  - "[[Battery Product Landscape Conflicts and Open Questions]]"
performs:
  - "[[Measure Battery Temperature]]"
  - "[[Measure Electrolyte Specific Gravity]]"
  - "[[Indicate Battery Status Locally]]"
  - "[[Communicate with Charger]]"
  - "[[Transmit Battery Data Wirelessly]]"
  - "[[Detect Cell Failure]]"
hasDesign:
  - "[[In-Cell Specific Gravity Probe]]"
  - "[[Electrolyte-Immersed Temperature Sensor]]"
  - "[[Local LED Indicator]]"
  - "[[Battery-Top Mounting]]"
hasPart:
  - "[[In-Cell Electrolyte Measurement Probe Assembly]]"
  - "[[Specific Gravity Measurement Circuit]]"
  - "[[Specific Gravity Acquisition Firmware]]"
  - "[[LED Status Indicator Element]]"
madeBy:
  - "[[AMETEK Prestolite Power]]"
---

# AMETEK Prestolite Power TruBid

## Definition

AMETEK Prestolite Power battery charge monitor that sits on the battery, puts a probe in a cell and works with the charger to end charge on measured state.

## Notes

**Summary:**
AMETEK Prestolite Power battery charge monitor with an in-cell probe that works with the charger to end charge on measured state.

**Marketed features:**
- Probe monitors electrolyte temperature and specific gravity
- More accurate charge reading than conventional devices (maker claim)
- Works with the charger to extend charge to manufacturer recommendations
- Ensures only one 100 percent charge per day; detects cell failures
- Six on-board LEDs; wireless download to charger and DataLink software

**Summary and features sources:**
Maker or publisher marketing claims as stated, not independently verified.
- DC Velocity (T2), retrieved 2026-10-04. <https://dcvelocity.com/articles/31462-ametek-s-trubid-system-accurately-measures-battery-charge>

- Trade press says TruBid sits on top of the battery, inserts a probe into a cell, continuously monitors electrolyte temperature and specific gravity, extends the charge with the charger to meet the manufacturer's recommendation, detects cell failures, shows status on six LEDs, and wirelessly downloads data to the charger and to DataLink software. Source: DC Velocity (undated) (T2), retrieved 2026-10-02. <https://dcvelocity.com/articles/31462-ametek-s-trubid-system-accurately-measures-battery-charge>
- **Status unclear:** TruBid does not appear on the current Prestolite Data Devices page (which lists WBID Pro, BID, BID with Ah Accumulator, Site Probe and WID2). It may be discontinued; not confirmed.
- **Functions performed, with citations** (V = verified this pass, C = carried from seed text, U = user-stated):
  - [[Measure Battery Temperature]] (V): <https://dcvelocity.com/articles/31462-ametek-s-trubid-system-accurately-measures-battery-charge>
  - [[Measure Electrolyte Specific Gravity]] (V): <https://dcvelocity.com/articles/31462-ametek-s-trubid-system-accurately-measures-battery-charge>
  - [[Indicate Battery Status Locally]] (V): <https://dcvelocity.com/articles/31462-ametek-s-trubid-system-accurately-measures-battery-charge>
  - [[Communicate with Charger]] (V): <https://dcvelocity.com/articles/31462-ametek-s-trubid-system-accurately-measures-battery-charge>
  - [[Transmit Battery Data Wirelessly]] (V): <https://dcvelocity.com/articles/31462-ametek-s-trubid-system-accurately-measures-battery-charge>
  - [[Detect Cell Failure]] (V): <https://dcvelocity.com/articles/31462-ametek-s-trubid-system-accurately-measures-battery-charge>
- **Design characteristics, with citations:**
  - [[Electrolyte-Immersed Temperature Sensor]] (V): <https://dcvelocity.com/articles/31462-ametek-s-trubid-system-accurately-measures-battery-charge>
  - [[Local LED Indicator]] (V): <https://dcvelocity.com/articles/31462-ametek-s-trubid-system-accurately-measures-battery-charge>
  - [[Battery-Top Mounting]] (V): <https://dcvelocity.com/articles/31462-ametek-s-trubid-system-accurately-measures-battery-charge>
- **Sources used for the mapping above:** DC Velocity (undated) <https://dcvelocity.com/articles/31462-ametek-s-trubid-system-accurately-measures-battery-charge>
- **Truck parts (round 31):** typical (inferred from the device type, not from a source): mounts on [[Truck Battery Compartment]]. See [[Truck Part Connection Register]].

- **Architecture realization — specific gravity measurement:** the in-cell probe and continuous specific-gravity measurement are verified. [[In-Cell Electrolyte Measurement Probe Assembly]] captures the physical probe, while [[Specific Gravity Sensing Element]] remains technology-neutral because the transduction principle is not published. [[Specific Gravity Measurement Circuit]] and [[Specific Gravity Acquisition Firmware]] are allocated at **>=95% engineering confidence** because TruBID electronically reports/uses a continuous specific-gravity value while its internal circuit and firmware partition are not disclosed.
- **Architecture boundary — cell failure detection:** the available source explicitly states that TruBID detects cell failures, and separately states that its in-cell probe monitors electrolyte temperature and specific gravity. Neither the source nor Prestolite's public description explains how those measurements are converted into a cell-failure diagnosis. Accordingly, no [[Cell Failure Diagnostic Firmware]] or [[Cell Failure Threshold Circuit]] is assigned as a product part, and no cell-voltage / impedance / specific-gravity diagnostic method is asserted.

## Aliases

- TruBid


## Former ids
