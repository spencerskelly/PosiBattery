---
type: Object
subtype: electrical
id: OBJ-00012
uid: 20261002150858948skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - forklift
  - gse
  - lead-acid
  - lithium
subtypeOf:
  - "[[PosiCharge BMID]]"
describedBy:
  - "[[Battery Product Landscape Conflicts and Open Questions]]"
  - "[[PosiCharge BMID Variants]]"
performs:
  - "[[Measure Battery Voltage]]"
  - "[[Measure Battery Current]]"
  - "[[Sense Electrolyte Level]]"
  - "[[Log Battery Events and Usage]]"
  - "[[Communicate with Charger]]"
  - "[[Transmit Battery Data Wirelessly]]"
  - "[[Communicate Battery State over CAN]]"
  - "[[Upload Battery Data to Cloud Portal]]"
  - "[[Configure Device from Mobile App or PC]]"
hasDesign:
  - "[[Bluetooth Interface]]"
  - "[[CAN Interface]]"
  - "[[RS-232 and RS-485 Serial Interface]]"
  - "[[Acid-Resistant Sealed Housing]]"
  - "[[Mobile App Interface]]"
  - "[[LoRa Interface]]"
madeBy:
  - "[[PosiCharge]]"
---

# PosiCharge PosiGuard

## Definition

PosiCharge commercial battery data and monitoring device for lead-acid and lithium industrial battery fleets.

## Notes

- Manufacturer/product line: PosiCharge / Ampure
- Market evidence checked: 2026-10-02
- Published voltage range: nominal 24–96 V; operating 18–120 V.
- Published measurements include current, voltage, and electrolyte level where applicable.
- Published communications include Serial, CAN, Bluetooth, and optional LoRa.
- PosiCharge describes PosiGuard as capturing battery data at the source and supporting mixed lead-acid/lithium fleets.
- Evidence: https://posicharge.com/products/posiguard/
- **Not re-verified:** the posicharge.com PosiGuard page was not retrieved in this pass.
- **Verification 2026-10-02 (new evidence; conflicts with classification):** PosiCharge's own PosiConnect mobile app (published by Ampure Charging Systems Inc.) is described as managing 'PosiGuard BMID devices' over Bluetooth for configuration, firmware updates and log export, with remote or cloud management through the PosiLink web portal. Source: Apple App Store listing for PosiConnect (T1) <https://apps.apple.com/mx/app/posiconnect/id6748969496>
- **Conflict (C10):** the text above files PosiGuard under Battery Monitoring Device and the BMID under the identification and charge-interface family. PosiCharge's app wording calls PosiGuard a BMID device. The relationship between PosiGuard and the BMID variants is unresolved.
- **Stated by Spencer Skelly, 2026-10-02:** PosiGuard is the next generation of the PosiCharge BMID. It is now filed as a subtype of [[PosiCharge BMID]], matching PosiCharge's own app wording ('PosiGuard BMID devices'). It was previously filed under Battery Monitoring Device; see conflicts C10 (now resolved by this statement).
- **Not stated:** which earlier variant it follows (BMID 3 specifically), whether earlier BMIDs are discontinued, and its launch date.
- **Functions performed, with citations** (V = verified this pass, C = carried from seed text, U = user-stated):
  - [[Measure Battery Voltage]] (V): <https://posicharge.com/products/posiguard/>
  - [[Measure Battery Current]] (V): <https://posicharge.com/products/posiguard/>
  - [[Sense Electrolyte Level]] (V): <https://posicharge.com/products/posiguard/>
  - [[Log Battery Events and Usage]] (V): <https://posicharge.com/products/posiguard/> <https://apps.apple.com/mx/app/posiconnect/id6748969496>
  - [[Communicate with Charger]] (V): <https://posicharge.com/products/posiguard/>
  - [[Transmit Battery Data Wirelessly]] (V): <https://posicharge.com/products/posiguard/>
  - [[Communicate Battery State over CAN]] (V): <https://posicharge.com/products/posiguard/>
  - [[Upload Battery Data to Cloud Portal]] (V): <https://posicharge.com/products/posiguard/>
  - [[Configure Device from Mobile App or PC]] (V): <https://apps.apple.com/mx/app/posiconnect/id6748969496>
- **Design characteristics, with citations:**
  - [[Bluetooth Interface]] (V): <https://posicharge.com/products/posiguard/> <https://apps.apple.com/mx/app/posiconnect/id6748969496>
  - [[CAN Interface]] (V): <https://posicharge.com/products/posiguard/>
  - [[RS-232 and RS-485 Serial Interface]] (V): <https://posicharge.com/products/posiguard/>
  - [[Acid-Resistant Sealed Housing]] (V): <https://posicharge.com/products/posiguard/>
  - [[Mobile App Interface]] (V): <https://apps.apple.com/mx/app/posiconnect/id6748969496>
  - [[LoRa Interface]] (V): <https://posicharge.com/products/posiguard/>
- **Sources used for the mapping above:** PosiGuard product page <https://posicharge.com/products/posiguard/>; PosiConnect app listing <https://apps.apple.com/mx/app/posiconnect/id6748969496>
- PosiGuard's current page says it is designed for both lead-acid and lithium batteries, captures data at the source and connects it to PosiLink, monitors current, voltage and electrolyte level, and works with wired, Bluetooth and CAN communication to the charger. Source: PosiCharge PosiGuard page (T1), retrieved 2026-10-02. <https://posicharge.com/products/posiguard/>
- The same page lists nominal battery voltage 24 to 96 V, operating voltage 18 to 120 V, voltage resolution 30 mV, current resolution 100 mA, operating temperature -25 to 75 C, 4.05 x 1.80 x 1.00 in, IP65 sealed against water and acid, interfaces Serial, CAN, Bluetooth and LoRa, battery-backed clock, 16 MB storage, and UL 583 and EN 1175 safety certifications. Source: PosiCharge PosiGuard page (T1), retrieved 2026-10-02. <https://posicharge.com/products/posiguard/>
- **Verification 2026-10-02:** the seed text above (24-96 V, 18-120 V, Serial, CAN, Bluetooth, LoRa) is now re-verified on the current vendor page.

## Aliases

- PosiGuard

## Former ids
