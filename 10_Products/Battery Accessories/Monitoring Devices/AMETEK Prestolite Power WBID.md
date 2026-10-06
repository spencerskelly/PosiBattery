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
  - scope-aftermarket
subtypeOf:
  - "[[Battery Monitoring Device]]"
  - "[[Battery Identification and Charge Interface Device]]"
performs:
  - "[[Measure Battery Voltage]]"
  - "[[Measure Battery Temperature]]"
  - "[[Accumulate Amp-Hours]]"
  - "[[Log Battery Events and Usage]]"
  - "[[Communicate with Charger]]"
  - "[[Transmit Battery Data Wirelessly]]"
hasDesign:
  - "[[Current Integration Amp-Hour Accumulation]]"
  - "[[Non-Volatile Event Memory]]"
  - "[[ZigBee 2.4 GHz Interface]]"
  - "[[DC-Cable Power-Line Communication]]"
  - "[[Battery-Charger Data Communication Design]]"
hasPart:
  - "[[Battery Current Measurement Circuit]]"
  - "[[Battery Current Acquisition Firmware]]"
  - "[[Amp-Hour Accumulator Firmware]]"
  - "[[Control Circuit]]"
  - "[[Amp-Hour Counter State Memory]]"
madeBy:
  - "[[AMETEK Prestolite Power]]"
---

# AMETEK Prestolite Power WBID

## Definition

Obsolete AMETEK Prestolite Power Wireless Battery Identification Device, replaced by the WBID Pro.

## Notes

**Summary:**
Obsolete AMETEK Prestolite Power wireless battery identification device that captured lift-truck battery data for fleet monitoring, replaced by the WBID Pro.

**Marketed features:**
- Recorded temperature, Ah in/out, EQ hours and connects per day; 30-day fleet summary
- Six I/O channels for temperature, level or LED indicators
- Data to the charger over the DC cable without extra connectors
- ZigBee wireless link to DataLink 2/3; range up to 500 ft in-truck and 3,000 ft between chargers (as stated)
- One device covers 12-40 cells
- Status: obsolete; WBID Pro is the direct replacement

**Summary and features sources:**
Maker or publisher marketing claims as stated, not independently verified.
- AMETEK Prestolite Power (T1), retrieved 2026-10-04. <https://www.prestolitepower.com/products/obsolete-products/wbid>
- Yahoo Finance (press release) (T2), retrieved 2026-10-04. <https://finance.yahoo.com/news/ametek-prestolite-power-launches-wireless-142836825.html>
- MH&L (T2), retrieved 2026-10-04. <https://mhlnews.com/new-products/article/22054269/wireless-forklift-battery-monitor-new-products>

- The vendor lists the WBID as obsolete with WBID Pro as the direct replacement, and notes compatibility with DataLink and IntelliFleet software. Source: AMETEK Prestolite Power obsolete-products page (T1), retrieved 2026-10-02. <https://www.prestolitepower.com/products/obsolete-products/wbid>
- A 2014 release says the WBID stores all data over the battery's life, communicates with the charger over the DC cable without special or auxiliary connectors, and needs only one device for 12 to 40 cells; a 2017 release says data moves by ZigBee or over DC cables with a connectivity range up to 500 ft when truck-mounted. Source: Marketwired release (2014) and trade coverage (2017) (T2 (dated)), retrieved 2026-10-02. <https://finance.yahoo.com/news/ametek-prestolite-power-launches-wireless-142836825.html>
- **Relevance:** this is the only retrieved example of charger communication carried on the DC cable. Whether WBID Pro keeps it is not stated (conflicts C11).
- **Functions performed, with citations** (V = verified this pass, C = carried from seed text, U = user-stated):
  - [[Measure Battery Voltage]] (V): <https://finance.yahoo.com/news/ametek-prestolite-power-launches-wireless-142836825.html>
  - [[Measure Battery Temperature]] (V): <https://finance.yahoo.com/news/ametek-prestolite-power-launches-wireless-142836825.html>
  - [[Accumulate Amp-Hours]] (V): <https://finance.yahoo.com/news/ametek-prestolite-power-launches-wireless-142836825.html>
  - [[Log Battery Events and Usage]] (V): <https://www.prestolitepower.com/products/obsolete-products/wbid> <https://finance.yahoo.com/news/ametek-prestolite-power-launches-wireless-142836825.html>
  - [[Communicate with Charger]] (V): <https://finance.yahoo.com/news/ametek-prestolite-power-launches-wireless-142836825.html>
  - [[Transmit Battery Data Wirelessly]] (V): <https://mhlnews.com/new-products/article/22054269/wireless-forklift-battery-monitor-new-products>
- **Design characteristics, with citations:**
  - [[ZigBee 2.4 GHz Interface]] (V): <https://mhlnews.com/new-products/article/22054269/wireless-forklift-battery-monitor-new-products>
  - [[DC-Cable Power-Line Communication]] (V): <https://finance.yahoo.com/news/ametek-prestolite-power-launches-wireless-142836825.html>
- **Sources used for the mapping above:** Prestolite obsolete-products WBID page <https://www.prestolitepower.com/products/obsolete-products/wbid>; Marketwired release via Yahoo Finance (2014, dated) <https://finance.yahoo.com/news/ametek-prestolite-power-launches-wireless-142836825.html>; M H&L New Products (2017, dated) <https://mhlnews.com/new-products/article/22054269/wireless-forklift-battery-monitor-new-products>
- **Truck parts (round 31):** typical (inferred from the device type, not from a source): mounts on [[Truck Battery Compartment]]. See [[Truck Part Connection Register]].

- **Architecture realization — amp-hour accumulation:** this battery-mounted device records amp-hours in/out over long-term battery history. [[Current Integration Amp-Hour Accumulation]] and [[Amp-Hour Accumulator Firmware]] are allocated at **>=95% engineering confidence** because producing persistent Ah-in/out totals requires current integration, while the internal current-sensing topology and firmware partition are not published.

- **Architecture realization — charger communication:** published evidence establishes data exchange with a compatible charger, supporting [[Battery-Charger Data Communication Design]]. The transport and message set remain product-specific.

## Aliases

- WBID
- Wireless Battery Identification Device


## Former ids
