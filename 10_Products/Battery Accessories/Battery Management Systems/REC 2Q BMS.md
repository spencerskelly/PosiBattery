---
type: Object
subtype: electrical
id: OBJ-90912
uid: 20261014000000018skellyspencer
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
madeBy:
  - "[[REC (BMS maker)]]"
hasDesign:
  - "[[Standalone Battery Management System]]"
  - "[[Master and Cell Monitor BMS Topology]]"
performs:
  - "[[Communicate Battery State over CAN]]"
---

# REC 2Q BMS

## Definition

Standalone BMS for 4 to 16 series cells with integrated CAN communication; combines in a master-slave configuration for up to 240 cells.

## Notes

- **Update 2026-10-17 (customer traceability review):** performs [[Communicate Battery State over CAN]] because the REC page states integrated CAN communication and compatibility with inverters; which CAN protocol and which values are sent are not stated.
**Summary:**
Standalone BMS for 4 to 16 series cells with integrated CAN communication; combines in a master-slave configuration for up to 240 cells.

**Marketed features:**
- Manages 4 to 16 series cells
- Integrated CAN communication protocol
- Compatible with a variety of inverters
- Master-slave configuration for higher voltage, up to 240 cells with the 2Q BMS, with multiple programmable relays and digital outputs

**Summary and features sources:**
Maker or publisher marketing claims as stated, not independently verified.
- [[Document - REC BMS Product Page (retrieved 2026-10-13)]] <https://www.rec-bms.com/>

- Manufacturer: REC (BMS maker)
- External product: not made by PosiCharge; recorded to define BMS functions and designs (owner decision 2026-10-13).
- The page states no protections, balancing current, state of charge or contactor outputs.
- **Not stated in the sources read:** balancing method and current; protection functions; state of charge; which CAN protocol; any certification; date.
- **Functions performed, with citations** (V = verified this pass):
- See [[External BMS Product Landscape]] for the comparison.


## Aliases



## Former ids
