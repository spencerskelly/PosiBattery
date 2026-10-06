---
type: Object
subtype: electrical
id: OBJ-00012
uid: 20261002150858948skellyspencer
status: Draft
productClass: specific-offering
aliases:
  - PosiGuard
tags:
  - battery-market-reference
  - commercial-product
  - forklift
  - gse
  - lead-acid
  - lithium
  - scope-aftermarket
subtypeOf:
  - "[[PosiCharge BMID]]"
describedBy:
  - "[[Battery Product Landscape Conflicts and Open Questions]]"
  - "[[PosiCharge BMID Variants]]"
  - "[[Document - PosiCharge PosiGuard Product Page]]"
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
  - "[[Identify Battery to Charger]]"
hasDesign:
  - "[[Bluetooth Interface]]"
  - "[[CAN Interface]]"
  - "[[RS-232 and RS-485 Serial Interface]]"
  - "[[Acid-Resistant Sealed Housing]]"
  - "[[Mobile App Interface]]"
  - "[[LoRa Interface]]"
  - "[[Battery Identification and Charger Communication Software Design]]"
  - "[[Battery Voltage Measurement Design]]"
  - "[[Current Sensing Design]]"
  - "[[CAN Battery State Communication Design]]"
  - "[[Wireless Battery Data Communication Design]]"
  - "[[Cloud Battery Data Upload Design]]"
  - "[[Battery-Charger Data Communication Design]]"
madeBy:
  - "[[PosiCharge]]"
offeredWith:
  - "[[PosiCharge PosiLink]]"
  - "[[PosiCharge PosiConnect]]"
applies:
  - "[[PosiGuard - Support Local Service Configuration]]"
  - "[[PosiGuard - Support Lead-Acid and Lithium Battery Fleets]]"
satisfies:
  - "[[PosiGuard - Support Lead-Acid and Lithium Battery Fleets]]"
hasPart:
  - "[[Electrolyte Level Acquisition Firmware]]"
  - "[[Electrolyte Level Measurement Circuit]]"
  - "[[Control Circuit]]"
  - "[[Battery Identification and Charger Communication Firmware]]"
  - "[[CAN Communication Circuit]]"
  - "[[Serial Communication Circuit]]"
  - "[[BLE Communication Circuit]]"
  - "[[LoRa Communication Circuit]]"
  - "[[Battery Voltage Measurement Circuit]]"
  - "[[Battery Voltage Acquisition Firmware]]"
  - "[[Battery Current Acquisition Firmware]]"
  - "[[CAN Battery State Communication Firmware]]"
  - "[[Wireless Battery Data Communication Firmware]]"
  - "[[Battery-Charger Communication Firmware]]"
  - "[[Battery Current Measurement Circuit]]"
---

# PosiCharge PosiGuard

## Definition

PosiCharge commercial battery data and monitoring device for lead-acid and lithium industrial battery fleets.

## Notes

**Summary:**
PosiCharge battery data and monitoring device for mixed lead-acid and lithium fleets that connects battery data to PosiLink.

**Marketed features:**
- Lead-acid and lithium support for mixed fleets
- Charger communication by wired, Bluetooth and CAN; optional LoRa
- Monitors current, voltage and electrolyte level; daily usage and misuse
- PosiConnect mobile app: Bluetooth pairing, settings, firmware updates, log export
- IP65, ultra-compact (4.05 x 1.80 x 1.00 in), -25 to 75 C
- 24-96 V nominal; 16 MB memory; UL 583 and EN 1175

**Summary and features sources:**
Maker or publisher marketing claims as stated, not independently verified.
- PosiCharge (T1), retrieved 2026-10-04. <https://posicharge.com/products/posiguard/>
- Apple App Store (vendor listing) (T1), retrieved 2026-10-04. <https://apps.apple.com/mx/app/posiconnect/id6748969496>

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
- **Public-evidence baseline (added from the vault's baseline note, round 19):**
- Battery-edge monitor for lead-acid and lithium batteries that captures battery data and sends it to PosiLink. Public specs list 24–96 V nominal battery voltage; 18–120 V operating range; 30 mV voltage resolution; 100 mA current resolution; serial, CAN, Bluetooth, and LoRa communications; electrolyte-level capability; 16 MB storage; IP65; −25 to 75 °C operating range; UL 583 and EN1175. Source: official PosiCharge page for PosiGuard, as summarized in the vault's Public Evidence Register (PUB-010, class P1/P2/P3 per that note) (T1), retrieved 2026-10-03. <https://posicharge.com/products/posiguard/>
- **Baseline confidence (PosiGuard):** Verified public—product level. **Still needed:** Current SKU/variant/sensor configurations; supported BMS/CAN protocols; LoRa band/gateway requirements; data model/API; cloud/service plan; cybersecurity; firmware/update pathway; connector/wiring diagrams.
- The PosiGuard product card (Downloads/PosiGuard_Product-Card.pdf-2.pdf) lists nominal battery voltage 24 to 96 V, operating voltage '18 - 20 Volts', voltage resolution 30 mV, current resolution 100 mA, operating temperature -25 to 75 C, 4.05 x 1.80 x 1.00 in, IP65, serial, CAN, WiFi, Bluetooth and LoRa interfaces, battery-backed date and time, 16 MB memory, UL 583 and EN1175; features: lead-acid and lithium, current, voltage and electrolyte sensing (some sensors need optional components), mobile app configuration and BMID data download. Source: PosiGuard product card (read round 20) (T1), retrieved 2026-10-03. <https://posicharge.com/wp-content/uploads/2026/01/PosiGuard_Product-Card.pdf-2.pdf>
- **C83 (round 20):** the card's operating voltage reads 18 to 20 V where the web page says 18 to 120 V.
- **GSE parts (round 32):** typical (inferred from the device type, not from a source): mounts on [[GSE Battery Compartment]]. The same device also fits trucks: typical mount [[Truck Battery Compartment]] (see [[Truck Part Connection Register]]). See [[GSE Part Connection Register]].

- **Implementation assumption — battery identification path:** PosiGuard is treated as performing [[Identify Battery to Charger]] with >=95% confidence because it is identified as a BMID-family device and publicly supports charger communication. The exact identification-message implementation is not published.
- **Implementation assumption — communication hardware:** the modeled [[Control Circuit]], [[Battery Identification and Charger Communication Firmware]], [[CAN Communication Circuit]], [[Serial Communication Circuit]], [[BLE Communication Circuit]], and [[LoRa Communication Circuit]] are circuit-level abstractions inferred from the published functions/interfaces. The vendor evidence supports CAN, Serial, Bluetooth, and optional LoRa interfaces, but not the exact transceiver/module topology or part numbers.

- **Implementation assumption — voltage measurement hardware:** [[Battery Voltage Measurement Circuit]], [[Battery Voltage Acquisition Firmware]], and [[Battery Voltage Measurement Design]] are allocated at >=95% confidence from the published 18–120 V operating range, voltage monitoring, and 30 mV resolution. The internal topology is not published, so none of the concrete child circuits is selected for PosiGuard.

- **Implementation assumption — current measurement hardware:** [[Battery Current Measurement Circuit]], [[Battery Current Acquisition Firmware]], and [[Current Sensing Design]] are allocated at >=95% confidence because PosiGuard publicly specifies current monitoring and 100 mA resolution. The exact sensing topology is not published, so resistive, Hall-effect, split-core, and shuntless implementations remain alternatives rather than selected product architecture.

- **Implementation assumption — electrolyte level sensing:** [[Electrolyte Level Measurement Circuit]] and [[Electrolyte Level Acquisition Firmware]] are allocated at **>=95% engineering confidence** because this product publicly monitors electrolyte/water level electronically. The exact probe technology, input circuit, thresholds, and firmware partition are not published, so no specific child [[Electrolyte Level Sensing Design]] is selected from this evidence alone.

## Former ids
