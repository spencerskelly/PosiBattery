---
type: Object
subtype: electrical
id: OBJ-00013
uid: 20261002150858949skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - forklift
  - gse
  - charge-interface
abstract: true
subtypeOf:
  - "[[Battery Identification and Charge Interface Device]]"
supertypeOf:
  - "[[PosiCharge BMID 1]]"
  - "[[PosiCharge BMID 3]]"
  - "[[PosiCharge Battery Rx]]"
  - "[[PosiCharge PosiGuard]]"
describedBy:
  - "[[BMID Competitor Landscape]]"
  - "[[Battery Product Landscape Conflicts and Open Questions]]"
  - "[[PosiCharge BMID Variants]]"
  - "[[PosiCharge]]"
performs:
  - "[[Measure Battery Voltage]]"
  - "[[Measure Battery Temperature]]"
  - "[[Estimate State of Charge]]"
  - "[[Log Battery Events and Usage]]"
  - "[[Identify Battery to Charger]]"
  - "[[Report Battery Temperature to Charger]]"
  - "[[Communicate with Charger]]"
  - "[[Transmit Battery Data Wirelessly]]"
hasDesign:
  - "[[Electrolyte-Immersed Temperature Sensor]]"
  - "[[Bluetooth Interface]]"
---

# PosiCharge BMID

## Definition

PosiCharge Battery Monitor and Identifier installed on a battery to identify battery characteristics and communicate battery condition to compatible PosiCharge charging systems.

## Notes

- Manufacturer/product line: PosiCharge / Ampure
- Market evidence checked: 2026-10-02
- PosiCharge FAQ explicitly states the BMID is installed on the battery and includes an electrolyte-immersed thermistor for battery-temperature monitoring.
- Current PosiCharge charger pages describe BMID recognition of battery voltage, state of charge, and temperature and use in both MHE and GSE fast-charge systems.
- Evidence:
  - https://posicharge.com/faq/
  - https://posicharge.com/products/svs100/
  - https://posicharge.com/products/mvs400/
- **Verification 2026-10-02 (re-verified):** PosiCharge states the BMID is installed on the battery with two parts, an electrolyte-immersed thermistor and an electronic device that stores identity, charging profile and charge-event history, and that it communicates battery temperature to the PosiCharge charger. Source: PosiCharge FAQ (T1) <https://www.posicharge.com/faq/>
- **Variants stated by the user (not found in public documents):** BMID 1 and BMID 3. See [[PosiCharge BMID Variants]]. This note is now treated as the family; public-document names (Battery Rx, wireless BMID, Smart BMID) are not yet mapped to variants (conflicts C2, C12).
- **Functions performed, with citations** (V = verified this pass, C = carried from seed text, U = user-stated):
  - [[Measure Battery Voltage]] (V): <https://www.posicharge.com/airport-ground-support-equipment/>
  - [[Measure Battery Temperature]] (V): <https://www.posicharge.com/faq/> <https://www.posicharge.com/airport-ground-support-equipment/>
  - [[Estimate State of Charge]] (V): <https://www.posicharge.com/airport-ground-support-equipment/>
  - [[Log Battery Events and Usage]] (V): <https://www.posicharge.com/faq/>
  - [[Identify Battery to Charger]] (V): <https://www.posicharge.com/faq/>
  - [[Report Battery Temperature to Charger]] (V): <https://www.posicharge.com/faq/>
  - [[Communicate with Charger]] (V): <https://www.posicharge.com/procoreedge>
  - [[Transmit Battery Data Wirelessly]] (V): <https://www.posicharge.com/procoreedge>
- **Design characteristics, with citations:**
  - [[Electrolyte-Immersed Temperature Sensor]] (V): <https://www.posicharge.com/faq/>
  - [[Bluetooth Interface]] (V): <https://www.posicharge.com/procoreedge>
- **Sources used for the mapping above:** PosiCharge FAQ <https://www.posicharge.com/faq/>; PosiCharge ground support equipment page <https://www.posicharge.com/airport-ground-support-equipment/>; PosiCharge ProCore Edge page (wireless BMID) <https://www.posicharge.com/procoreedge>
- PosiCharge's GSE charger page lists as a key feature that the Smart Battery Monitor and Identification Device (BMID) instantly recognizes voltage, state of charge and temperature. Source: PosiCharge ground support equipment page (T1), retrieved 2026-10-02. <https://www.posicharge.com/airport-ground-support-equipment/>
- PosiCharge's ProCore Edge page says the charger has CAN/Lithium, BMID and Voltage automatic modes, and communicates with wireless BMIDs through Bluetooth. Source: PosiCharge ProCore Edge page (T1), retrieved 2026-10-02. <https://www.posicharge.com/procoreedge>

## Aliases

- BMID
- Battery Monitor and Identifier
- Smart Battery Monitor and Identification Device

## Former ids
