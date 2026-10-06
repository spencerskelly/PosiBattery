---
type: Object
subtype: software
id: OBJ-00287
uid: 20261003141234136skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - scope-oem-option
  - software
  - truck-device
  - truck-oem-option
  - vehicle-accessory
subtypeOf:
  - "[[Truck Telematics Software]]"
hasPart:
  - "[[Battery State of Health Analytics Service]]"
  - "[[Raymond iWAREHOUSE ObjectSense]]"
  - "[[Raymond iWAREHOUSE Fieldsense]]"
  - "[[Raymond iWAREHOUSE Real-Time Location System]]"
  - "[[Raymond iWAREHOUSE Integrated Tether System]]"
performs:
  - "[[Estimate State of Health]]"
  - "[[Report Truck Telemetry]]"
  - "[[Detect and Record Impacts]]"
hasDesign:
  - "[[Usage-History State of Health Analytics]]"
madeBy:
  - "[[Raymond]]"
---

# Raymond iWAREHOUSE

## Definition

Raymond fleet management system with operator assist modules ObjectSense, Fieldsense, RTLS and Integrated Tether System.

## Notes

- Raymond describes iWAREHOUSE as a fully customizable fleet management system giving integrated intelligent forklift and impact data, and says the Model 8810 pallet truck is available with iWAREHOUSE telematics. Source: Raymond sell sheet and Inbound Logistics (T1/T2), retrieved 2026-10-03. <https://www.johnstonequipment.com/-/media/raymond/literature/truck-literature/counterbalanced-trucks/raymond-stand-up-counterbalanced-options-sell-sheet.pdf>
- Raymond's operator assist suite includes iWAREHOUSE ObjectSense, Fieldsense, Real-Time Location System and Integrated Tether System. Source: DC Velocity (T2), retrieved 2026-10-03. <https://www.dcvelocity.com/material-handling/raymond-showcases-products-that-better-connect-operator-and-forklift-truck>
- **Functions performed, with citations:**
  - [[Report Truck Telemetry]] (V): <https://www.johnstonequipment.com/-/media/raymond/literature/truck-literature/counterbalanced-trucks/raymond-stand-up-counterbalanced-options-sell-sheet.pdf>
  - [[Detect and Record Impacts]] (V): <https://www.johnstonequipment.com/-/media/raymond/literature/truck-literature/counterbalanced-trucks/raymond-stand-up-counterbalanced-options-sell-sheet.pdf>
  - [[Estimate State of Health]] (V): <https://www.raymondcorp.com/-/media/raymond/literature/iwarehouse/ibatterysellsheetsipl1030_0513.pdf>
- Raymond's iBATTERY/iWAREHOUSE sell sheet shows an iWAREHOUSE Gateway battery state-of-health dashboard and a Battery Cycles Detail chart that lists contributors such as over/under-discharge, water level and other critical factors; the collected data also includes capacity/efficiency, current, temperature, SOC, water level and fault codes. Source: Raymond iBATTERY sell sheet (T1), retrieved 2026-10-06. <https://www.raymondcorp.com/-/media/raymond/literature/iwarehouse/ibatterysellsheetsipl1030_0513.pdf>
- The options sheet says iWAREHOUSE telematics shows key and deadman hours, fault codes and impact data. Source: Raymond options sell sheet (T1), retrieved 2026-10-03. <https://www.johnstonequipment.com/-/media/raymond/literature/truck-literature/counterbalanced-trucks/raymond-stand-up-counterbalanced-options-sell-sheet.pdf>
- **Truck parts (round 31):** typical (inferred from the device type, not from a source): mounts on [[Truck Controller and CAN Bus]]; connects to [[Truck Controller and CAN Bus]]; acts on [[Truck Controller and CAN Bus]]. See [[Truck Part Connection Register]].

- **Architecture realization — battery state of health:** Raymond's published iBATTERY material places the battery state-of-health dashboard in iWAREHOUSE and identifies contributors including over/under-discharge, water level, battery capacity/efficiency, temperature, state of charge, current and fault codes. [[Usage-History State of Health Analytics]] and [[Battery State of Health Analytics Service]] therefore represent the verified analytics path. The weighting/formula, update cadence and execution architecture are not published.

## Aliases

- iWAREHOUSE

## Former ids
