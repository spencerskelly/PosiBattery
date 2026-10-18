---
type: Object
subtype: electrical
id: OBJ-90914
uid: 20261014000000020skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - lithium
  - bms
  - external-product
productCategory: battery-accessory
interfaces:
  - usb
  - rs-485
subtypeOf:
  - "[[Battery Management System]]"
performs:
  - "[[Disconnect Battery on Limit Violation]]"
madeBy:
  - "[[Batrium]]"
hasDesign:
  - "[[Standalone Battery Management System]]"
  - "[[Master and Cell Monitor BMS Topology]]"
---

# Batrium WatchMonCORE

## Definition

Supervisor unit of the Batrium BMS that watches 1 to 250 cells through separate cell monitors and triggers external devices from configurable logic.

## Notes

**Summary:**
Supervisor unit of the Batrium BMS that watches 1 to 250 cells through separate cell monitors and triggers external devices from configurable logic.

**Marketed features:**
- Watches between 1 and 250 cells
- Distributed cell monitors provide 'capable of 28 Ah / day balancing adjustment for each cell'
- Configurable control logic triggers external devices based on cell data
- Configurable 30 VDC, 5 A relay, for example to trip a remote circuit breaker
- 4-stage state-of-charge display
- Firmware updates over USB

**Summary and features sources:**
Maker or publisher marketing claims as stated, not independently verified.
- [[Document - Batrium BMS Product Guide (undated)]] <https://wiki.batrium.com/documents/batrium_bms_product_guide.pdf>

- Manufacturer: Batrium
- External product: not made by PosiCharge; recorded to define BMS functions and designs (owner decision 2026-10-13).
- Expansion3 adds 3 mechanical 30 VDC, 5 A relays and 3 isolated solid-state relays rated 65 VDC, 5 A, and works with all previous WatchMon supervisors (not given a note).
- **Not stated in the sources read:** CAN, Modbus and RS485 (not mentioned in the guide; Expansion3 lists RS485 as a future option); protection thresholds; any certification; date.
- **Functions performed, with citations** (V = verified this pass):
  - [[Disconnect Battery on Limit Violation]] (V): guide: configurable logic triggers external devices from cell data, relay for a breaker trip
- See [[External BMS Product Landscape]] for the comparison.


## Aliases



## Former ids
