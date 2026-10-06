---
type: Object
subtype: electrical
id: OBJ-00028
uid: 20261002162520378skellyspencer
status: Draft
tags:
  - battery-market-reference
  - charge-interface
  - commercial-product
  - forklift
  - lead-acid
  - scope-oem-option
subtypeOf:
  - "[[Battery Identification and Charge Interface Device]]"
performs:
  - "[[Measure Battery Voltage]]"
  - "[[Measure Battery Temperature]]"
  - "[[Sense Electrolyte Level]]"
  - "[[Log Battery Events and Usage]]"
  - "[[Identify Battery to Charger]]"
  - "[[Configure Device from Mobile App or PC]]"
  - "[[Alert on Low Electrolyte Level]]"
  - "[[Report Battery Temperature to Charger]]"
  - "[[Communicate with Charger]]"
hasDesign:
  - "[[Communicated Watering Need Alert]]"
  - "[[Bluetooth Class 1 Interface]]"
  - "[[Battery-Top Mounting]]"
  - "[[Acid-Resistant Sealed Housing]]"
hasPart:
  - "[[Low Electrolyte Alert Logic]]"
offeredBy:
  - "[[Crown Equipment]]"
offeredWith:
  - "[[Crown V-HFM3 Charger]]"
---

# Crown V-Force BMID

## Definition

Crown battery monitoring and identification device for lead-acid forklift batteries, sold as a charger accessory and as a part.

## Notes

**Summary:**
Crown V-Force battery monitoring and identification device that sits on a lead-acid battery to record events and optimize charging.

**Marketed features:**
- Dual profile configuration for opportunity or fast charging
- Records battery events including temperature and charge/discharge cycles
- Adjusts charge rate by voltage and temperature; automatic temperature compensation
- Low electrolyte detection and watering-need communication
- Rugged case resists impact, water and electrolyte; Bluetooth Class 1 to laptop/tablet
- Part no. 396525-BT

**Summary and features sources:**
Maker or publisher marketing claims as stated, not independently verified.
- Crown (T1), retrieved 2026-10-04. <https://shop.crown.com/crown/en/Batteries-and-Chargers/Battery-and-Charger-Parts-and-Accessories/Battery-and-Charger-Accessories//p/396525-BTM>
- Crown (T1), retrieved 2026-10-04. <https://www.crown.com/content/dam/crown/pdfs/en-us/brochures/products/vhfm3-chargers.pdf>

- Manufacturer: Crown Equipment Corporation. Not the same product as the PosiCharge BMID despite the shared acronym (conflicts C1).
- **Verification 2026-10-02 (verified (vendor shop)):** part 396525-BTM: dual-profile configuration for opportunity or fast charging, records battery events including temperature and charge and discharge cycles, rugged spill-resistant case, Bluetooth Class 1 for connecting to a laptop or tablet; listed at 583.33 USD with 365-day warranty on the retrieval date. Source: Crown parts shop (T1) <https://shop.crown.com/crown/en/Batteries-and-Chargers/Battery-and-Charger-Parts-and-Accessories/Battery-and-Charger-Accessories//p/396525-BTM>
- **Verification 2026-10-02 (verified (regional page)):** an optional BMID module for FS3 and HFM3 chargers mounts on top of a lead-acid battery, detects low electrolyte, monitors voltage and temperature, and adjusts charge rate. Source: Crown charger page (Vietnam site) (T1) <https://crown.com/en-vn/batteries-and-chargers/vhfm3-charger.html>
- **Not stated in retrieved sources:** how the BMID communicates with the charger (wired, wireless or other), voltage range, lithium support, whether it works with non-Crown chargers. Do not assume it matches PosiCharge behavior.
- **Functions performed, with citations** (V = verified this pass, C = carried from seed text, U = user-stated):
  - [[Measure Battery Voltage]] (V): <https://crown.com/en-vn/batteries-and-chargers/vhfm3-charger.html>
  - [[Measure Battery Temperature]] (V): <https://shop.crown.com/crown/en/Batteries-and-Chargers/Battery-and-Charger-Parts-and-Accessories/Battery-and-Charger-Accessories//p/396525-BTM> <https://crown.com/en-vn/batteries-and-chargers/vhfm3-charger.html>
  - [[Sense Electrolyte Level]] (V): <https://crown.com/en-vn/batteries-and-chargers/vhfm3-charger.html>
  - [[Log Battery Events and Usage]] (V): <https://shop.crown.com/crown/en/Batteries-and-Chargers/Battery-and-Charger-Parts-and-Accessories/Battery-and-Charger-Accessories//p/396525-BTM>
  - [[Identify Battery to Charger]] (V): <https://shop.crown.com/crown/en/Batteries-and-Chargers/Battery-and-Charger-Parts-and-Accessories/Battery-and-Charger-Accessories//p/396525-BTM>
  - [[Configure Device from Mobile App or PC]] (V): <https://shop.crown.com/crown/en/Batteries-and-Chargers/Battery-and-Charger-Parts-and-Accessories/Battery-and-Charger-Accessories//p/396525-BTM>
  - [[Alert on Low Electrolyte Level]] (V): <https://www.crown.com/content/dam/crown/pdfs/en-us/brochures/products/vhfm3-chargers.pdf>
  - [[Report Battery Temperature to Charger]] (V): <https://www.crown.com/content/dam/crown/pdfs/en-us/brochures/products/vhfm3-chargers.pdf>
  - [[Communicate with Charger]] (V): <https://www.crown.com/content/dam/crown/pdfs/en-us/brochures/products/vhfm3-chargers.pdf>
- **Design characteristics, with citations:**
  - [[Communicated Watering Need Alert]] (V): <https://www.crown.com/content/dam/crown/pdfs/en-us/brochures/products/vhfm3-chargers.pdf>
  - [[Bluetooth Class 1 Interface]] (V): <https://shop.crown.com/crown/en/Batteries-and-Chargers/Battery-and-Charger-Parts-and-Accessories/Battery-and-Charger-Accessories//p/396525-BTM>
  - [[Battery-Top Mounting]] (V): <https://crown.com/en-vn/batteries-and-chargers/vhfm3-charger.html>
  - [[Acid-Resistant Sealed Housing]] (V): <https://shop.crown.com/crown/en/Batteries-and-Chargers/Battery-and-Charger-Parts-and-Accessories/Battery-and-Charger-Accessories//p/396525-BTM>
- **Sources used for the mapping above:** Crown parts shop <https://shop.crown.com/crown/en/Batteries-and-Chargers/Battery-and-Charger-Parts-and-Accessories/Battery-and-Charger-Accessories//p/396525-BTM>; Crown charger options page (Vietnam site) <https://crown.com/en-vn/batteries-and-chargers/vhfm3-charger.html>
- The V-HFM3 brochure lists the BMID as part number 396525-BT, mounting on top of the battery to monitor battery health, control and optimize charging, detect low electrolyte and communicate watering needs, adjusting charge rate on voltage and temperature, with automatic temperature compensation and electrolyte level monitoring during the charge. Source: Crown V-HFM3 brochure (PF20000, 08-18) (T1), retrieved 2026-10-02. <https://www.crown.com/content/dam/crown/pdfs/en-us/brochures/products/vhfm3-chargers.pdf>
- **Conflict-visible (C38):** the brochure part number is 396525-BT; the Crown parts shop listing used 396525-BTM. Not established whether these are the same part or a variant.
- Crown says the optional BMID module mounts on top of a lead-acid battery, records all battery events including temperature and charge and discharge cycles, detects low electrolyte level and communicates the need to water. Source: Crown batteries and chargers page (T1), retrieved 2026-10-03. <https://www.crown.com/en-ca/batteries-and-chargers/>
- **Implementation assumption — low electrolyte alert logic:** [[Low Electrolyte Alert Logic]] is allocated at **>=95% engineering confidence** because the BMID detects low electrolyte and communicates watering need. Crown does not publish the internal decision logic or transport used for that watering alert, so [[Communicated Watering Need Alert]] is verified while the logic implementation remains an explicit assumption.
- **Truck parts (round 31):** typical (inferred from the device type, not from a source): mounts on [[Truck Battery Compartment]]. See [[Truck Part Connection Register]].

## Aliases

- Crown BMID
- V-Force Battery Monitoring Identification Device


## Former ids
