---
type: Object
subtype: electrical
id: OBJ-90911
uid: 20261014000000017skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - lithium
  - bms
  - external-product
productCategory: battery-accessory
interfaces:
  - can-bus
subtypeOf:
  - "[[Battery Management System]]"
performs:
  - "[[Measure Battery Voltage]]"
  - "[[Balance Cells]]"
  - "[[Estimate State of Charge]]"
  - "[[Calculate Charge and Discharge Current Limits]]"
  - "[[Detect Isolation Fault]]"
  - "[[Disconnect Battery on Limit Violation]]"
  - "[[Communicate Battery State over CAN]]"
madeBy:
  - "[[Ewert Energy Systems]]"
hasDesign:
  - "[[Standalone Battery Management System]]"
  - "[[Passive Cell Balancing]]"
---

# Orion BMS 2

## Definition

Standalone BMS for series-connected lithium packs of 24 to 180 cells, with state of charge, current limits, two CAN interfaces and charger and contactor outputs.

## Notes

**Summary:**
Standalone BMS for series-connected lithium packs of 24 to 180 cells, with state of charge, current limits, two CAN interfaces and charger and contactor outputs.

**Marketed features:**
- Up to 180 series cells per unit, in 12-cell configurations from 24 to 180
- Passive cell balancing
- Calculates state of charge, discharge current limit (DCL) and charge current limit (CCL)
- Two programmable CAN 2.0B interfaces and OBD2 diagnostic support
- Hardware support for SAE J1772 pilot and proximity lines and CHAdeMO
- Can directly drive certain contactors; two multi-purpose outputs

**Summary and features sources:**
Maker or publisher marketing claims as stated, not independently verified.
- [[Document - Orion BMS 2 Product Page (retrieved 2026-10-13)]] <https://www.orionbms.com/products/orion-bms-standard/>
- [[Document - Orion BMS 2 Specifications (Ewert Energy Systems)]] <https://www.orionbms.com/downloads/documents/orionbms2_specifications.pdf>

- Manufacturer: Ewert Energy Systems
- External product: not made by PosiCharge; recorded to define BMS functions and designs (owner decision 2026-10-13).
- Specification sheet (B3, see map): cell voltage measured from 0.5 V to 5 V at 0.1 mV resolution; 200 mA passive balancing; two CAN 2.0B interfaces at 125 to 1000 kbps with CANopen and J1939 compatibility cited; isolation fault detection circuit; ISO 7637 load dump and EN 50498 EMC listed; one digital output controls a charger and two enable charge and discharge. These come from [[BMS Product Function and Requirement Driver Map]] (BF1 to BF6, BF10, RD4).
- Thermistors need a separate Thermistor Expansion Module, which the product page lists as its own product.
- **Not stated in the sources read:** certifications on the product page; J1939 and CANopen on the product page (the sheet cites them, see C206); the state-of-charge method; what 'pack health' means; protections as a named list on the product page.
- **Functions performed, with citations** (V = verified this pass):
  - [[Measure Battery Voltage]] (V): spec sheet, see map BF1
  - [[Balance Cells]] (V): product page: 'Performs intelligent cell balancing (passive)'
  - [[Estimate State of Charge]] (V): product page: 'Calculates state of charge (SOC)'
  - [[Calculate Charge and Discharge Current Limits]] (V): product page
  - [[Detect Isolation Fault]] (V): spec sheet, see map BF10
  - [[Disconnect Battery on Limit Violation]] (V): spec sheet, see map BF2; product page says it can directly drive certain contactors
  - [[Communicate Battery State over CAN]] (V): product page: two CAN 2.0B interfaces
- See [[External BMS Product Landscape]] for the comparison.


## Aliases



## Former ids
