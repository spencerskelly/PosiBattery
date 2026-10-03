---
type: Object
subtype: electrical
id: OBJ-00053
uid: 20261002165629063skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - forklift
  - gse
  - fleet-management
subtypeOf:
  - "[[Battery Monitoring Device]]"
  - "[[Battery Identification and Charge Interface Device]]"
describedBy:
  - "[[Document - ACT Battview Sheet (2023)]]"
  - "[[Document - ACT Quantum 3 Sheet (2024)]]"
  - "[[Document - ACT Quantum Charger Sheet (2023)]]"
performs:
  - "[[Measure Battery Voltage]]"
  - "[[Measure Battery Current]]"
  - "[[Measure Battery Temperature]]"
  - "[[Sense Electrolyte Level]]"
  - "[[Log Battery Events and Usage]]"
  - "[[Track Equalization]]"
  - "[[Alert on Abnormal Condition]]"
  - "[[Communicate with Charger]]"
  - "[[Transmit Battery Data Wirelessly]]"
  - "[[Upload Battery Data to Cloud Portal]]"
hasDesign:
  - "[[Wi-Fi Interface]]"
  - "[[DC-Cable Power-Line Communication]]"
madeBy:
  - "[[Advanced Charging Technologies]]"
offeredWith:
  - "[[ACT Quantum 2]]"
  - "[[ACT Quantum 3]]"
  - "[[ACT Quantum Outdoor]]"
  - "[[ACT ACTview]]"
---

# Advanced Charging Technologies BATTview

## Definition

ACT battery monitor that exchanges data with ACT Quantum chargers and reports to the ACTview cloud platform.

## Notes

- The spec sheet lists nominal battery voltage 12 to 80 V, operating voltage 12 to 110 V, voltage resolution plus or minus 30 mV, current resolution plus or minus 1 A minimum, temperature resolution plus or minus 1.0 F, and operating temperature -25 to 60 C; it reports hours, Ah, charge, use and idle periods, and alerts for weekly missed equalization, charge, temperature and usage, potential weak cells, missed finish, deep discharge, potential sulfated battery and water level; it needs no calibration, uses Wi-Fi, and communicates in real time between Quantum chargers and ACTview. Source: ACT Battview spec sheet (T1), retrieved 2026-10-02. <https://og.mhi.org/media/members/41607/133717592244521430.pdf>
- A trade report says data integration between BATTview units and Quantum chargers improves charge-cycle communications, equalization scheduling and tracking of charge termination conditions. Source: DC Velocity (T2), retrieved 2026-10-02. <https://dcvelocity.com/articles/31570-advanced-charging-technologies-improves-battview-battery-monitors>
- A GSE trade article says ACT's Quantum GSE outdoor charger communicates with BATTview and uploads data to the ACTintelligent cloud platform. Source: Airside International (T2), retrieved 2026-10-02. <https://www.airsideint.com/issue-article/act-moves-into-the-gse-battery-charging-business/>
- ACT's products are sold and serviced exclusively through the Deka (East Penn) battery dealer network. Source: MMH company profile (T2), retrieved 2026-10-02. <https://www.mmh.com/company/advanced_charging_technologies>
- **Not stated in retrieved sources:** how BATTview attaches to the battery, whether it identifies the battery to the charger, whether it supports lithium (the Quantum charger lists lithium-ion support).
- **Functions performed, with citations** (V = verified this pass, C = carried from seed text, U = user-stated):
  - [[Measure Battery Voltage]] (V): <https://og.mhi.org/media/members/41607/133717592244521430.pdf>
  - [[Measure Battery Current]] (V): <https://og.mhi.org/media/members/41607/133717592244521430.pdf>
  - [[Measure Battery Temperature]] (V): <https://og.mhi.org/media/members/41607/133717592244521430.pdf>
  - [[Sense Electrolyte Level]] (V): <https://og.mhi.org/media/members/41607/133717592244521430.pdf>
  - [[Log Battery Events and Usage]] (V): <https://og.mhi.org/media/members/41607/133717592244521430.pdf>
  - [[Track Equalization]] (V): <https://og.mhi.org/media/members/41607/133717592244521430.pdf> <https://dcvelocity.com/articles/31570-advanced-charging-technologies-improves-battview-battery-monitors>
  - [[Alert on Abnormal Condition]] (V): <https://og.mhi.org/media/members/41607/133717592244521430.pdf>
  - [[Communicate with Charger]] (V): <https://og.mhi.org/media/members/41607/133717592244521430.pdf> <https://dcvelocity.com/articles/31570-advanced-charging-technologies-improves-battview-battery-monitors> <https://www.airsideint.com/issue-article/act-moves-into-the-gse-battery-charging-business/>
  - [[Transmit Battery Data Wirelessly]] (V): <https://og.mhi.org/media/members/41607/133717592244521430.pdf>
  - [[Upload Battery Data to Cloud Portal]] (V): <https://og.mhi.org/media/members/41607/133717592244521430.pdf> <https://www.airsideint.com/issue-article/act-moves-into-the-gse-battery-charging-business/>
- **Design characteristics, with citations:**
  - [[Wi-Fi Interface]] (V): <https://og.mhi.org/media/members/41607/133717592244521430.pdf>
- **Sources used for the mapping above:** ACT Battview spec sheet (MHI member site) <https://og.mhi.org/media/members/41607/133717592244521430.pdf>; DC Velocity on BATTview-Quantum integration <https://dcvelocity.com/articles/31570-advanced-charging-technologies-improves-battview-battery-monitors>; Airside International on ACT GSE charger and BATTview <https://www.airsideint.com/issue-article/act-moves-into-the-gse-battery-charging-business/>
- **Related products and how they differ (offeredWith):**
  - [[ACT Quantum 2]]: all three Quantum chargers appear with Battview on their sheets; they differ in voltage range, efficiency and enclosure.
  - [[ACT Quantum 3]]: Quantum 3 covers 24 to 120 V and over 96.4 percent peak efficiency versus 24 to 96 V and over 94 percent.
  - [[ACT Quantum Outdoor]]: outdoor model with a NEMA 3R enclosure, also sold as Quantum GSE.
- **Design characteristics, with citations (round 11 document):**
  - [[DC-Cable Power-Line Communication]] (V): <https://og.mhi.org/media/members/41607/133717592244521430.pdf> (also [[Document - ACT Battview Sheet (2023)]])
- **Round 11 document:** Source: [[Document - ACT Battview Sheet (2023)]] (T1, local copy; original <https://og.mhi.org/media/members/41607/133717592244521430.pdf>), absorbed 2026-10-02.
| Parameter | Value as stated |
|---|---|
| Nominal and operating voltage | 12 to 80 V nominal; 12 to 110 V operating |
| Resolution | voltage +/-30 mV; current +/-1 A minimum; temperature +/-1.0 F |
| Operating temperature | -25 to 60 C |
| Communication | Wi-Fi; PLC optional |
| Time backup | coin-type lithium cell |
| Protection and enclosure | reverse polarity; sealed, splash proof, UL 94V-5 |
| Size | 5.5 x 1.75 x 1.0 in (140 x 44 x 25 mm) |
| Data | daily operation; hours, Ah, EBUs and percentages; charge, use and idle periods; fleet and site utilization |
| Alerts | weekly missed equalization; charge, temperature and usage notifications; potential weak cells; missed finish; deep discharge; potential sulfated battery; water level |
| Other | no calibration needed; '10x faster Wi-Fi speed' and 'easier to install' versus earlier model (claims) |
- **Conflict-visible (C51):** the sheet's Quantum blurb says 'Industry's highest charge efficiency (>94% peak)' while the Quantum 3 sheet says 96.4%; different generations, vendor superlative.

## Aliases

- BATTview
- Battview


## Former ids
