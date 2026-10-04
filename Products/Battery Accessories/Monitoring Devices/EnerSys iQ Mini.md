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
  - scope-oem-option
subtypeOf:
  - "[[Battery Monitoring Device]]"
describedBy:
  - "[[Document - EnerSys iQ Mini Flyer (GLOB-EN-FLY-IQM 0924)]]"
performs:
  - "[[Measure Battery Temperature]]"
  - "[[Log Battery Events and Usage]]"
  - "[[Indicate Battery Status Locally]]"
  - "[[Transmit Battery Data Wirelessly]]"
  - "[[Upload Battery Data to Cloud Portal]]"
  - "[[Calculate Battery Abuse Cycles]]"
  - "[[Alert on Abnormal Condition]]"
hasDesign:
  - "[[Bluetooth Low Energy Interface]]"
  - "[[Local LED Indicator]]"
  - "[[Cloud Portal Integration]]"
madeBy:
  - "[[EnerSys]]"
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
- **Functions performed, with citations (round 11 document):**
  - [[Calculate Battery Abuse Cycles]] (V): <https://www.enersys.com/496a7c/globalassets/documents/product-documentation/_enersys/glob/legacy/battery-management/iq-mini/glob-en-fly-iqm-0924-apac.pdf> (also [[Document - EnerSys iQ Mini Flyer (GLOB-EN-FLY-IQM 0924)]])
  - [[Alert on Abnormal Condition]] (V): <https://www.enersys.com/496a7c/globalassets/documents/product-documentation/_enersys/glob/legacy/battery-management/iq-mini/glob-en-fly-iqm-0924-apac.pdf> (also [[Document - EnerSys iQ Mini Flyer (GLOB-EN-FLY-IQM 0924)]])
  - [[Log Battery Events and Usage]] (V): <https://www.enersys.com/496a7c/globalassets/documents/product-documentation/_enersys/glob/legacy/battery-management/iq-mini/glob-en-fly-iqm-0924-apac.pdf> (also [[Document - EnerSys iQ Mini Flyer (GLOB-EN-FLY-IQM 0924)]])
- **Round 11 document:** Source: [[Document - EnerSys iQ Mini Flyer (GLOB-EN-FLY-IQM 0924)]] (T1, local copy; original <https://www.enersys.com/496a7c/globalassets/documents/product-documentation/_enersys/glob/legacy/battery-management/iq-mini/glob-en-fly-iqm-0924-apac.pdf>), absorbed 2026-10-02.
| Parameter | Value as stated |
|---|---|
| Part numbers | IQ-MINI-300Q and 300B8 (TPPL); 310Q and 310S (flooded); 301Q (VRLA) |
| Battery types | TPPL, flooded and VRLA |
| Alerts | over-temperature, low electrolyte (footnoted) and over-discharge; shown on the unit, recorded and uploaded |
| Abuse | abuse cycles calculated to approximate the life lost |
| Usage | records work, rest, charge and cool-down time |
| System | battery-mounted iQ Mini devices with iQ Gateway battery data transmitters; online portal |
| Electrical specifications | none given in the flyer |
- **Conflict-visible (C49):** the earlier note carries '12-80 V' from the seed text; the flyer states no voltage range, so the figure stays 'carried, not verified'. The iQ Gateway is a product not yet modeled (see [[Unidentified Products Review]]).

## Aliases

- iQ Mini


## Former ids
