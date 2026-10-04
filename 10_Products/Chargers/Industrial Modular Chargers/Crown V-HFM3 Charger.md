---
type: Object
subtype: electrical
id: OBJ-00067
uid: 20261002191446810skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - charger
subtypeOf:
  - "[[Industrial Modular Charger]]"
performs:
  - "[[Charge Battery Conventionally]]"
  - "[[Charge Battery by Opportunity]]"
  - "[[Charge Battery Fast]]"
  - "[[Charge Lithium-Ion Battery]]"
  - "[[Identify Battery by Voltage]]"
  - "[[Manage Chargers Remotely]]"
  - "[[Compensate Charge for Battery Temperature]]"
hasDesign:
  - "[[Multi-Voltage Output]]"
  - "[[Modular Power Modules]]"
  - "[[Charger Status LED Bar]]"
offeredBy:
  - "[[Crown Equipment]]"
offeredWith:
  - "[[Crown V-Force BMID]]"
  - "[[Crown V-Force Lithium-Ion ESS]]"
  - "[[Crown V-Force Lead-Acid Battery]]"
  - "[[Crown V-HFM3 Wired Remote Control Kit]]"
  - "[[Crown V-HFM3 Tower Light Kit]]"
  - "[[Crown V-HFM3 Charger Stand]]"
  - "[[Crown Cable Management Accessories]]"
  - "[[Crown Battery Cables and Connectors]]"
---

# Crown V-HFM3 Charger

## Definition

Crown V-Force modular charger for lead-acid and lithium-ion batteries that identifies the battery by voltage and has an optional BMID.

## Notes

- **Identity:** modular high-frequency charger series offered by [[Crown Equipment]] under the V-Force name; family [[Industrial Battery Charger]]. The brochure says 'Distributed by Crown Equipment Corporation'; who builds it is not stated (C41).
- **Specifications (as stated in the V-HFM3 brochure, copyright 2018):**
| Parameter | Value as stated |
|---|---|
| Battery voltages | 24, 36, 48, 72, 80, 96 V |
| Input (three phase) | FS3: 208-240, 380-480, 480-600 Vac; FS4 and FS6: 380-480, 480-600 Vac |
| Modules | FS3: one to three; FS4 and FS6: two to six |
| Efficiency | up to 97% (Crown claim) |
| Max charging current | FS3: 300 A (24/36 V), 255 A (48 V), 150 A (72/80 V), 127.5 A (96 V); FS4: 400, 400, 300, 255 A; FS6: 600, 510, 300, 255 A |
| Size | FS3 12 x 9.5 x 14.5 in (305 x 240 x 365 mm); FS4 and FS6 12 x 18.5 x 14.5 in (305 x 470 x 365 mm) |
| Weight | FS3 up to 37.4 lb (17 kg) with three modules; FS4 and FS6 up to 71.5 lb (32.5 kg) with six modules |
| Marks | UL Listed, cUL Listed, CEC-BC compliant |
| Charge profiles | conventional, opportunity, fast, V-Force lithium-ion |
| Connectivity | built-in web interface; Wi-Fi, Ethernet and USB |
| Options | BMID 396525-BT; wired remote control kit 396587-001; tower light kit 396586-001; charger stand; pogo stick |
- **Spec source:** [Crown V-HFM3 brochure PF20000 08-18](https://www.crown.com/content/dam/crown/pdfs/en-us/brochures/products/vhfm3-chargers.pdf).
- **Features (functions and designs, each with its citation):** see the citation lines in the source history below.
- **Related products and how they differ:**
  - [[Crown V-Force BMID]]: optional; the charger already identifies a battery by voltage without a monitoring device, and the BMID adds temperature compensation, electrolyte level monitoring and watering indication.
  - [[Crown V-Force Lithium-Ion ESS]]: lithium battery system that includes a V-Force charger; uses the V-Force lithium profile.
  - [[Crown V-Force Lead-Acid Battery]]: uses the conventional, opportunity or fast lead-acid profiles.
- **Differences and conflicts:** the brochure lists models FS3, FS4 and FS6 while Crown's Australia page lists FS4 (conventional or opportunity, lead-acid and lithium) and FS6 (fast, lead-acid) (C37); the brochure is dated 2018 while the launch release is dated 2019-06-18; BMID part number BT versus BTM (C38).
- **Gaps and to-do:** manufacturer (C41); price; whether the charger talks CAN to the V-Force lithium BMS; FS3 availability.
- **Source history (earlier bullets kept as written):**
- Crown says the V-HFM3 supports 24, 36, 48, 72, 80 and 96 V batteries, 208 to 600 V input, and conventional, opportunity, fast and V-Force lithium-ion profiles. Source: Crown V-HFM3 brochure (T1), retrieved 2026-10-02. <https://www.crown.com/content/dam/crown/pdfs/en-us/brochures/products/vhfm3-chargers.pdf>
- Crown says automatic voltage sensing identifies a battery on connection and applies the correct profile from 24 to 96 V without a monitoring device, and claims 97 percent efficiency. Source: Crown release (2019-06-18) (T1), retrieved 2026-10-02. <https://news.crown.com/blog/2019/crown-equipment-adds-forklift-power-source-versatility-and-efficiency-to-chargers/>
- The FS4 model covers conventional or opportunity charging for lead-acid and lithium-ion; the FS6 covers fast charging for lead-acid; the optional BMID mounts on top of a lead-acid battery, monitors voltage and temperature and adjusts charge rate. Source: Crown V-HFM3 page (Australia) (T1), retrieved 2026-10-02. <https://www.crown.com/en-au/batteries-and-chargers/vhfm3-charger.html>
- **Unknown:** who manufactures the V-HFM3 hardware.
- **Functions performed, with citations** (V = verified this pass):
  - [[Charge Battery Conventionally]] (V): <https://www.crown.com/content/dam/crown/pdfs/en-us/brochures/products/vhfm3-chargers.pdf>
  - [[Charge Battery by Opportunity]] (V): <https://www.crown.com/content/dam/crown/pdfs/en-us/brochures/products/vhfm3-chargers.pdf>
  - [[Charge Battery Fast]] (V): <https://www.crown.com/content/dam/crown/pdfs/en-us/brochures/products/vhfm3-chargers.pdf>
  - [[Charge Lithium-Ion Battery]] (V): <https://www.crown.com/content/dam/crown/pdfs/en-us/brochures/products/vhfm3-chargers.pdf>
  - [[Identify Battery by Voltage]] (V): <https://news.crown.com/blog/2019/crown-equipment-adds-forklift-power-source-versatility-and-efficiency-to-chargers/>
  - [[Manage Chargers Remotely]] (V): <https://www.crown.com/en-au/batteries-and-chargers/vhfm3-charger.html>
  - [[Compensate Charge for Battery Temperature]] (V): <https://www.crown.com/en-au/batteries-and-chargers/vhfm3-charger.html>
- **Design characteristics, with citations:**
  - [[Multi-Voltage Output]] (V): <https://www.crown.com/content/dam/crown/pdfs/en-us/brochures/products/vhfm3-chargers.pdf>
  - [[Modular Power Modules]] (V): <https://www.crown.com/content/dam/crown/pdfs/en-us/brochures/products/vhfm3-chargers.pdf>
  - [[Charger Status LED Bar]] (V): <https://www.crown.com/en-au/batteries-and-chargers/vhfm3-charger.html>
- Crown's V-HFM3 brochure lists charge profile options of Conventional, Opportunity, Fast and V-Force Lithium-Ion; the charger identifies a battery on connection and applies the correct charging profile from 24 to 96 V without a monitoring device; with the V-Force BMID it adds automatic temperature compensation and electrolyte level monitoring during the charge, and its indicators show charging status, cooling time and equalizing and watering needs. Source: Crown V-HFM3 brochure (T1), retrieved 2026-10-03. <https://www.crown.com/content/dam/crown/pdfs/en-us/brochures/products/vhfm3-chargers.pdf>
- **Functions performed, with citations:**
  - [[Compensate Charge for Battery Temperature]] (V): <https://www.crown.com/content/dam/crown/pdfs/en-us/brochures/products/vhfm3-chargers.pdf>

## Aliases

- V-HFM3
- V-Force V-HFM3


## Former ids
