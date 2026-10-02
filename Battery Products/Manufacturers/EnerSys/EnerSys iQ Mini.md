---
type: Object
subtype: electrical
id: OBJ-00007
uid: 20261002150858943skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - forklift
subtypeOf:
  - "[[Battery Monitoring Device]]"
performs:
  - "[[Measure Battery Temperature]]"
  - "[[Log Battery Events and Usage]]"
  - "[[Indicate Battery Status Locally]]"
  - "[[Transmit Battery Data Wirelessly]]"
  - "[[Upload Battery Data to Cloud Portal]]"
hasDesign:
  - "[[Bluetooth Low Energy Interface]]"
  - "[[Local LED Indicator]]"
  - "[[Cloud Portal Integration]]"
---

# EnerSys iQ Mini

## Definition

Compact EnerSys battery-mounted monitoring device for battery status and usage monitoring.

## Notes

- Manufacturer: EnerSys
- Market evidence checked: 2026-10-02
- Installation locus: battery-mounted according to EnerSys product literature.
- Published applications include forklifts/pallet trucks and floor-care equipment.
- Published communication capability: wireless BLE; EnerSys describes use with iQ Gateway battery data transmitters and an online portal.
- Owner documentation for model 310Q describes monitoring cycles and temperature on 12–80 V flooded batteries and status indication for electrolyte, over-temperature, and communication.
- Evidence:
  - https://www.enersys.com/en/products/monitoring-and-fleet-management/data-logger/enersys/iq-mini/
  - https://www.enersys.com/496a7c/globalassets/documents/product-documentation/_enersys/glob/legacy/battery-management/iq-mini/glob-en-fly-iqm-0924-apac.pdf
- **Verification 2026-10-02 (re-verified):** EnerSys describes iQ Mini as recently launched in November 2024, compatible with TPPL, flooded and VRLA batteries, with colour status indicators on the unit and data uploaded to an online portal; the product page lists forklifts, pallet trucks and floor-care machines, BLE communication, and use with iQ Gateway data transmitters. Source: EnerSys press release and product page (T1) <https://www.enersys.com/en/about-us/news/enersys-to-showcase-advanced-battery-management-at-2024-north-american-issa-show/>
- **Not stated in retrieved sources:** CAN, charger interaction, battery voltage range. The 12-80 V figure in the text above comes from a 310Q owner document that was not re-opened. The press release emphasises floor-care machines, so the forklift emphasis rests on the product page application list.
- **Functions performed, with citations** (V = verified this pass, C = carried from seed text, U = user-stated):
  - [[Measure Battery Temperature]] (C): <https://www.enersys.com/496a7c/globalassets/documents/product-documentation/_enersys/glob/legacy/battery-management/iq-mini/glob-en-fly-iqm-0924-apac.pdf>
  - [[Log Battery Events and Usage]] (C): <https://www.enersys.com/496a7c/globalassets/documents/product-documentation/_enersys/glob/legacy/battery-management/iq-mini/glob-en-fly-iqm-0924-apac.pdf>
  - [[Indicate Battery Status Locally]] (V): <https://www.enersys.com/en/about-us/news/enersys-to-showcase-advanced-battery-management-at-2024-north-american-issa-show/>
  - [[Transmit Battery Data Wirelessly]] (V): <https://www.enersys.com/en-gb/products/monitoring-and-fleet-management/data-logger/enersys/iq-mini/>
  - [[Upload Battery Data to Cloud Portal]] (V): <https://www.enersys.com/en-gb/products/monitoring-and-fleet-management/data-logger/enersys/iq-mini/> <https://www.enersys.com/en/about-us/news/enersys-to-showcase-advanced-battery-management-at-2024-north-american-issa-show/>
- **Design characteristics, with citations:**
  - [[Bluetooth Low Energy Interface]] (V): <https://www.enersys.com/en-gb/products/monitoring-and-fleet-management/data-logger/enersys/iq-mini/>
  - [[Local LED Indicator]] (V): <https://www.enersys.com/en/about-us/news/enersys-to-showcase-advanced-battery-management-at-2024-north-american-issa-show/>
  - [[Cloud Portal Integration]] (V): <https://www.enersys.com/en-gb/products/monitoring-and-fleet-management/data-logger/enersys/iq-mini/> <https://www.enersys.com/en/about-us/news/enersys-to-showcase-advanced-battery-management-at-2024-north-american-issa-show/>
- **Sources used for the mapping above:** EnerSys iQ Mini product page (UK) <https://www.enersys.com/en-gb/products/monitoring-and-fleet-management/data-logger/enersys/iq-mini/>; EnerSys ISSA 2024 release <https://www.enersys.com/en/about-us/news/enersys-to-showcase-advanced-battery-management-at-2024-north-american-issa-show/>; Seed note (cites the iQ Mini flyer, not re-opened) <https://www.enersys.com/496a7c/globalassets/documents/product-documentation/_enersys/glob/legacy/battery-management/iq-mini/glob-en-fly-iqm-0924-apac.pdf>

## Aliases

- iQ Mini

## Former ids
