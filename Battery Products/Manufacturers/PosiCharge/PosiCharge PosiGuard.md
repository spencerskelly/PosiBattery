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
  - "[[Configure Device from Mobile App or PC]]"
  - "[[Log Battery Events and Usage]]"
  - "[[Measure Battery Voltage]]"
  - "[[Measure Battery Current]]"
  - "[[Sense Electrolyte Level]]"
  - "[[Communicate Battery State over CAN]]"
  - "[[Transmit Battery Data Wirelessly]]"
hasDesign:
  - "[[Bluetooth Interface]]"
  - "[[CAN Interface]]"
  - "[[RS-232 and RS-485 Serial Interface]]"
  - "[[Mobile App Interface]]"
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
- **Functions performed (evidence):** [[Configure Device from Mobile App or PC]] (V); [[Log Battery Events and Usage]] (V); [[Measure Battery Voltage]] (C); [[Measure Battery Current]] (C); [[Sense Electrolyte Level]] (C); [[Communicate Battery State over CAN]] (C); [[Transmit Battery Data Wirelessly]] (C). V = verified this pass, C = carried from seed text, U = user-stated.
- **Design characteristics (evidence):** [[Bluetooth Interface]] (V); [[CAN Interface]] (C); [[RS-232 and RS-485 Serial Interface]] (C); [[Mobile App Interface]] (V).

## Aliases

- PosiGuard

## Former ids
