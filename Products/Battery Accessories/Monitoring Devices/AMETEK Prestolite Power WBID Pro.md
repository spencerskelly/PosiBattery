---
type: Object
subtype: electrical
id: OBJ-00011
uid: 20261002150858947skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - forklift
  - scope-aftermarket
  - telemetry
subtypeOf:
  - "[[Battery Monitoring Device]]"
describedBy:
  - "[[Battery Product Landscape Conflicts and Open Questions]]"
performs:
  - "[[Measure Battery Temperature]]"
  - "[[Sense Electrolyte Level]]"
  - "[[Accumulate Amp-Hours]]"
  - "[[Estimate State of Charge]]"
  - "[[Log Battery Events and Usage]]"
  - "[[Track Equalization]]"
  - "[[Indicate Battery Status Locally]]"
  - "[[Transmit Battery Data Wirelessly]]"
  - "[[Upload Battery Data to Cloud Portal]]"
hasDesign:
  - "[[Electrolyte-Immersed Temperature Sensor]]"
  - "[[ZigBee 2.4 GHz Interface]]"
  - "[[Local LED Indicator]]"
madeBy:
  - "[[AMETEK Prestolite Power]]"
---

# AMETEK Prestolite Power WBID Pro

## Definition

AMETEK Prestolite Power battery-mounted monitoring device that records forklift-battery operating history and supports wireless fleet data collection.

## Notes

- Manufacturer: AMETEK Prestolite Power
- Market evidence checked: 2026-10-02
- Vendor explicitly describes WBID Pro as a battery-mounted monitoring device.
- Published data includes average/minimum/maximum temperature, amp-hours in/out, equalization hours, connection counts, idle/use/charge time, event logs, and state of charge.
- Options include electrolyte-level and temperature sensors and an LED output module.
- Published wireless access uses ZigBee and integrates with IntelliFleet / Insight Cloud workflows.
- Evidence:
  - https://www.prestolitepower.com/products/datadevices/wbid-pro
  - https://www.prestolitepower.com/products/datadevices
- **Verification 2026-10-02 (re-verified):** WBID Pro is a battery-mounted monitoring device with level sensors, electrolyte and ambient temperature sensors, a configurable LED output module and ZigBee data access; it is compatible with Insight Cloud. Source: AMETEK Prestolite Power WBID Pro page (T1) <https://www.prestolitepower.com/products/datadevices/wbid-pro>
- **Verification 2026-10-02 (lineage):** the earlier WBID is listed as obsolete, with WBID Pro as direct replacement; the WBID was compatible with IntelliFleet and DataLink software. Source: AMETEK Prestolite Power obsolete-products page (T1) <https://www.prestolitepower.com/products/obsolete-products/wbid>
- **Verification 2026-10-02 (dated; applies to the obsolete WBID):** a 2014 press release said WBID data communication to the charger can run over the DC cable without special or auxiliary connectors, and that one WBID covers 12-40 cells. Source: AMETEK Prestolite Power press release via Yahoo Finance (2014-11-10) (T2) <https://finance.yahoo.com/news/ametek-prestolite-power-launches-wireless-142836825.html>
- **Open (see conflicts C11):** the text above classifies WBID Pro as monitoring only. The 2014 release suggests WBID also interacts with chargers. Whether WBID Pro does is not stated on the retrieved pages.
- **Functions performed, with citations** (V = verified this pass, C = carried from seed text, U = user-stated):
  - [[Measure Battery Temperature]] (V): <https://www.prestolitepower.com/products/datadevices/wbid-pro>
  - [[Sense Electrolyte Level]] (V): <https://www.prestolitepower.com/products/datadevices/wbid-pro>
  - [[Accumulate Amp-Hours]] (C): <https://www.prestolitepower.com/products/datadevices/wbid-pro>
  - [[Estimate State of Charge]] (C): <https://www.prestolitepower.com/products/datadevices/wbid-pro>
  - [[Log Battery Events and Usage]] (V): <https://www.prestolitepower.com/products/datadevices/wbid-pro>
  - [[Track Equalization]] (C): <https://www.prestolitepower.com/products/datadevices/wbid-pro>
  - [[Indicate Battery Status Locally]] (V): <https://www.prestolitepower.com/products/datadevices/wbid-pro>
  - [[Transmit Battery Data Wirelessly]] (V): <https://www.prestolitepower.com/products/datadevices/wbid-pro>
  - [[Upload Battery Data to Cloud Portal]] (V): <https://www.prestolitepower.com/products/datadevices/wbid-pro>
- **Design characteristics, with citations:**
  - [[Electrolyte-Immersed Temperature Sensor]] (V): <https://www.prestolitepower.com/products/datadevices/wbid-pro>
  - [[ZigBee 2.4 GHz Interface]] (V): <https://www.prestolitepower.com/products/datadevices/wbid-pro>
  - [[Local LED Indicator]] (V): <https://www.prestolitepower.com/products/datadevices/wbid-pro>
- **Sources used for the mapping above:** Prestolite WBID Pro page <https://www.prestolitepower.com/products/datadevices/wbid-pro>; Seed note (cites the WBID Pro page for these) <https://www.prestolitepower.com/products/datadevices/wbid-pro>
- **Truck parts (round 31):** typical (inferred from the device type, not from a source): mounts on [[Truck Battery Compartment]]; connects to [[Truck Controller and CAN Bus]]. See [[Truck Part Connection Register]].

## Aliases

- WBID Pro
- Wireless Battery Identification Device Pro


## Former ids
