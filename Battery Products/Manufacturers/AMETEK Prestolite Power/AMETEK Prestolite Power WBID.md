---
type: Object
subtype: electrical
id: OBJ-00043
uid: 20261002164202411skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - forklift
  - obsolete
subtypeOf:
  - "[[Battery Monitoring Device]]"
  - "[[Battery Identification and Charge Interface Device]]"
performs:
  - "[[Measure Battery Voltage]]"
  - "[[Measure Battery Temperature]]"
  - "[[Accumulate Amp-Hours]]"
  - "[[Log Battery Events and Usage]]"
  - "[[Transmit Battery Data Wirelessly]]"
  - "[[Communicate with Charger]]"
hasDesign:
  - "[[DC-Cable Power-Line Communication]]"
  - "[[ZigBee 2.4 GHz Interface]]"
---

# AMETEK Prestolite Power WBID

## Definition

Obsolete AMETEK Prestolite Power Wireless Battery Identification Device, replaced by the WBID Pro.

## Notes

- The vendor lists the WBID as obsolete with WBID Pro as the direct replacement, and notes compatibility with DataLink and IntelliFleet software. Source: AMETEK Prestolite Power obsolete-products page (T1), retrieved 2026-10-02. <https://www.prestolitepower.com/products/obsolete-products/wbid>
- A 2014 release says the WBID stores all data over the battery's life, communicates with the charger over the DC cable without special or auxiliary connectors, and needs only one device for 12 to 40 cells; a 2017 release says data moves by ZigBee or over DC cables with a connectivity range up to 500 ft when truck-mounted. Source: Marketwired release (2014) and trade coverage (2017) (T2 (dated)), retrieved 2026-10-02. <https://finance.yahoo.com/news/ametek-prestolite-power-launches-wireless-142836825.html>
- **Relevance:** this is the only retrieved example of charger communication carried on the DC cable. Whether WBID Pro keeps it is not stated (conflicts C11).
- **Functions performed (evidence):** [[Measure Battery Voltage]] (V); [[Measure Battery Temperature]] (V); [[Accumulate Amp-Hours]] (V); [[Log Battery Events and Usage]] (V); [[Transmit Battery Data Wirelessly]] (V); [[Communicate with Charger]] (V). V = verified this pass, C = carried from seed text, U = user-stated.
- **Design characteristics (evidence):** [[DC-Cable Power-Line Communication]] (V); [[ZigBee 2.4 GHz Interface]] (V).

## Aliases

- WBID
- Wireless Battery Identification Device

## Former ids
