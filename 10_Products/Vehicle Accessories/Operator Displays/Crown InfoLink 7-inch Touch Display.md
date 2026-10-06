---
type: Object
subtype: electrical
id: OBJ-00220
uid: 20261003093855189skellyspencer
status: Draft
tags:
  - accessory
  - battery-market-reference
  - commercial-product
  - display
  - scope-oem-option
  - vehicle-accessory
subtypeOf:
  - "[[Operator Display]]"
performs:
  - "[[Alert Operator of Hazards]]"
  - "[[Enforce Pre-Shift Checklist]]"
  - "[[Detect and Record Impacts]]"
  - "[[Control Operator Access]]"
hasDesign:
  - "[[Operator Touch Display]]"
  - "[[Pre-Shift Checklist Enforcement Design]]"
madeBy:
  - "[[Crown Equipment]]"
offeredWith:
hasPart:
  - "[[Pre-Shift Checklist Enforcement Logic]]"
  - "[[Vehicle Enable Interlock]]"
  - "[[Crown ProximityAssist System]]"
---

# Crown InfoLink 7-inch Touch Display

## Definition

Crown 7 inch touch display on InfoLink-equipped trucks that shows visual and audible alerts such as ProximityAssist object detection.

## Notes

**Summary:**
Crown InfoLink operator touchscreen module that delivers visual messages, checklists, access control and impact alerts during operation.

**Marketed features:**
- 7 in color touch LCD (HD3000) with customizable widgets
- Illustrated electronic inspection checklists (OSHA compliance support)
- Impact monitoring and messages; analyzer mode for live impact testing
- Operator certification management and electronic truck access control; integrated proximity reader and on-screen keypad
- Safety reminders, Dynamic Coaching and two-way messaging
- Glove-friendly navigation buttons; 25 languages

**Summary and features sources:**
Maker or publisher marketing claims as stated, not independently verified.
- Crown (T1), retrieved 2026-10-04. <https://www.crown.com/en-us/fleet-management/infolink.html>
- Crown (T1), retrieved 2026-10-04. <https://www.crown.com/en-eu/fleet-management/forklift-fleet-management-infolink.html>
- Crown (T1), retrieved 2026-10-04. <https://www.crown.com/content/dam/crown/pdfs/en-us/operator-manuals/InfoLink/infolink-hardware-7inch.pdf>

- Crown says trucks with the InfoLink 7 inch touch display or the Gena operating system's 7 inch touch screen show visual and audible alerts when ProximityAssist detects an object. Source: IVT International and Food Logistics reports (T2), retrieved 2026-10-03. <https://www.ivtinternational.com/?p=22917>
- **Open:** the Gena operating system screen is a separate named item, not yet modeled.
- **Functions performed, with citations:**
  - [[Alert Operator of Hazards]] (V): <https://www.ivtinternational.com/?p=22917>
- **Design characteristics, with citations:**
  - [[Operator Touch Display]] (V): <https://www.ivtinternational.com/?p=22917>
- **Truck parts (round 31):** typical (inferred from the device type, not from a source): mounts on [[Truck Controls and Display]]; connects to [[Truck Controller and CAN Bus]]; acts on [[Truck Controls and Display]]. See [[Truck Part Connection Register]].
- **Functions performed, with citations** (V = verified this pass, C = carried from seed text, U = user-stated):
  - [[Enforce Pre-Shift Checklist]] (V): <https://www.crown.com/en-us/fleet-management/infolink.html>
  - [[Detect and Record Impacts]] (V): <https://www.crown.com/en-us/fleet-management/infolink.html>
  - [[Control Operator Access]] (V): <https://www.crown.com/en-us/fleet-management/infolink.html>

- **Architecture realization — pre-shift checklist:** published material explicitly describes electronic inspection checklists tied to truck access/lockout behavior, supporting [[Pre-Shift Checklist Enforcement Design]]. [[Pre-Shift Checklist Enforcement Logic]] is allocated at **>=95% engineering confidence** because the internal software partition is not published. [[Vehicle Enable Interlock]] captures the enforcement consequence when the checklist policy is not satisfied.

## Aliases


## Former ids
