---
type: Object
subtype: electrical
id: OBJ-00300
uid: 20261003143453034skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - posicharge-baseline
  - charger
productCategory: charger
subtypeOf:
  - "[[Industrial Modular Charger]]"
describedBy:
  - "[[Document - PosiCharge High Voltage Power Station Product Card (2026)]]"
  - "[[Document - PosiCharge High Voltage Power Station (AC) Page (retrieved 2026-10-13)]]"
performs:
  - "[[Charge Battery Fast]]"
hasDesign:
  - "[[Cellular Communication Interface]]"
  - "[[Modular Power Modules]]"
  - "[[Outdoor-Rated Charger Enclosure]]"
  - "[[Wi-Fi Interface]]"
madeBy:
  - "[[PosiCharge]]"
integratesWith:
  - "[[PosiCharge DVS100]]"
  - "[[PosiCharge DVS150]]"
  - "[[PosiCharge DVS300 Series]]"
  - "[[PosiCharge MVS400 and MVS800]]"
---

# PosiCharge High Voltage Power Station (AC)

## Definition

PosiCharge High Voltage Power Station listed under material handling charging (AC); shares a spec sheet file with the DC listing.

## Notes

- Listed as a current eGSE product; resource library lists an AC spec sheet. Source: official PosiCharge page for High Voltage Power Station—AC, as summarized in the vault's Public Evidence Register (PUB-001 and PUB-002, class P1/P2/P3 per that note) (T1), retrieved 2026-10-03. <https://posicharge.com/products/high-voltage-power-station-ac/>
- **Baseline confidence (High Voltage Power Station—AC):** Verified public—listing level. **Still needed:** Obtain and extract controlled/current spec sheet; define ratings, topology, interfaces, application, certification, and commercial status. **Update 2026-10-13:** ratings, input options, interfaces, application and certification are now recorded below from the card's page 2 and the AC page; still open: commercial status and availability, part numbers, warranty, the DC configuration's listing, the DC bus topology, which DVS and MVS models qualify, and any back-end behind OCPP.
- The resource listing links this product to the same card as the DC listing, and the card describes a DC fast charger (20 kW, CCS1 and NACS, NEMA 3S). Source: High Voltage Power Station product card (T1), retrieved 2026-10-03. <https://posicharge.com/wp-content/uploads/2026/01/High-Voltage-Power-Station-Product-Card-1.pdf>
- **Conflict (C82):** an AC-named listing with a DC card; no separate AC sheet found. **Update 2026-10-13:** the AC listing has its own page with a specification tab ([[Document - PosiCharge High Voltage Power Station (AC) Page (retrieved 2026-10-13)]]), and the card's table names an AC configuration (cETLus listed) and a DC configuration (listing pending); the original statement above is kept and C82 is updated.
- **Specifications (card page 2, read from the page image on 2026-10-13; T1):** input is the PosiCharge DC bus, 240 Vac single phase (216 to 252 V, 150 A max), 208 or 240 Vac three-phase delta (190 to 252 V, 100 A max) or 480/277 Vac three-phase wye (432 to 504 V, 45 A max), 60 Hz; output power is 20 kW maximum via the PosiCharge DC bus and 30 kW maximum via AC input; output voltage 250 to 920 Vdc; efficiency 95 percent; CCS1 and NACS connector, 5 m cable standard; DIN 70121 and OCPP 1.6J compliant; cellular 4G LTE and Wi-Fi; 7 inch color LCD; operation -30 to +50 C, storage -40 to +80 C, humidity up to 95 percent non-condensing, altitude 2000 m; NEMA 3S and IP54, impact IK10; 140 kg (charger only); wall-mounted or pedestal, both sold separately; AC configuration cETLus listed to UL 2202, UL 2231-1 and -2 and CSA C22.2 No. 281.1, 281.2 and 346, DC configuration listing pending. Page 2 has no extractable text, so earlier plain-text reads saw page 1 only. Source: [[Document - PosiCharge High Voltage Power Station Product Card (2026)]] (T1), <https://posicharge.com/wp-content/uploads/2026/01/High-Voltage-Power-Station-Product-Card-1.pdf>
- **AC listing page (retrieved 2026-10-13; T1; read through a fetch tool that returns a summary):** the title says High Voltage Power Station (AC) and the sub-heading says 20kW DC Fast Charger for eGSE + EVs; the specification tab matches the card except the protocol row, where the page was reported as DIN 70121 with no OCPP (C210). Source: [[Document - PosiCharge High Voltage Power Station (AC) Page (retrieved 2026-10-13)]] (T1), <https://posicharge.com/products/high-voltage-power-station-ac/>
- **Derived checks (note author, not source statements):** no output current is printed; at 30 kW the current would be about 120 A at 250 Vdc and about 33 A at 920 Vdc. The 20 kW and 30 kW figures are explained by the output power row (DC bus versus AC input), which accounts for the headline and second line (C81); whether the second line refers to the AC-fed case is an inference.
- **Functions performed, with citations** (V = verified this pass):
  - [[Charge Battery Fast]] (V): the card calls it a DC fast charger and gives 30 kW quick charge; it does not state a multiple of conventional charging rate or opportunity use, which the function's definition mentions. <https://posicharge.com/wp-content/uploads/2026/01/High-Voltage-Power-Station-Product-Card-1.pdf>
- **Design characteristics, with citations** (V = verified this pass; each link carries a note where the source covers only part of the design's definition):
  - [[Outdoor-Rated Charger Enclosure]] (V): NEMA 3S, IP54, IK10, operation -30 to +50 C. <https://posicharge.com/wp-content/uploads/2026/01/High-Voltage-Power-Station-Product-Card-1.pdf>
  - [[Modular Power Modules]] (V, partial): the card says it is built on proven modular power conversion technology. It gives no module count, no parallel-module description and no statement that charging continues after a module fails, which this design's definition includes; the link states modular construction only. <https://posicharge.com/wp-content/uploads/2026/01/High-Voltage-Power-Station-Product-Card-1.pdf>
  - [[Wi-Fi Interface]] (V, partial): the network row lists Wi-Fi. The design is defined as a Wi-Fi link for uploading data and sending commands; the card does not say what the link carries. <https://posicharge.com/wp-content/uploads/2026/01/High-Voltage-Power-Station-Product-Card-1.pdf>
  - [[Cellular Communication Interface]] (V, partial): the network row lists cellular 4G LTE. The design is defined as a cellular modem for sending data from the battery device; here it is on the charger, and the card does not say what it carries. <https://posicharge.com/wp-content/uploads/2026/01/High-Voltage-Power-Station-Product-Card-1.pdf>
- **Integrates with (T1):** the card says it is backwards compatible with DVS and MVS systems with a required software update, and that it runs on the PosiCharge DC bus. It names no models, so the links go to every vault note named for those families: [[PosiCharge DVS100]], [[PosiCharge DVS150]], [[PosiCharge DVS300 Series]] and [[PosiCharge MVS400 and MVS800]]. Whether each model qualifies, and which software version is required, is open (IB-159). <https://posicharge.com/wp-content/uploads/2026/01/High-Voltage-Power-Station-Product-Card-1.pdf>
- **Not linked, and why:** [[Manage Chargers Remotely]] and [[Remote Charger Management Design]] (the card lists OCPP 1.6J and cellular or Wi-Fi but states no portal or remote management; OCPP is a protocol between a charger and a central system per [[Document - Wikipedia Open Charge Point Protocol (retrieved 2026-10-13)]], which is about the protocol and not this product; IB-157); [[Charge Under BMS Control]] and [[Identify Battery to Charger]] (DIN 70121 is listed, but the card does not describe BMS-directed charging or battery identification); [[Indicate Charger Status Locally]] (the role of the 7 inch LCD is not stated; touch is not stated, so [[Touchscreen Interface]] is not linked); [[Multi-Voltage Output]] (the card gives one output range of 250 to 920 Vdc, not several fixed battery voltages); [[Silicon-Carbide Power Stage]] (not stated).
- **Sibling listing:** [[PosiCharge High Voltage Power Station (DC)]] is built on the same card and the same page content. The card's certification row separates an AC configuration from a DC configuration, which suggests the AC and DC names refer to the input source (AC input or the PosiCharge DC bus) and not to the output, which is DC in both; this is an analyst inference, not a source statement. The schema has no variant link, so the two notes are tied by the shared source document and by this paragraph (IB-156). The DC note was changed only by the inverse link to the shared card. **Owner correction 2026-10-13:** the two listings stay separate notes because the DC variant includes a kit that the AC variant does not (kit not yet identified, IB-162); the reading above, that AC and DC only name the input source, is therefore not confirmed and may be wrong. **Owner statement 2026-10-13 (U):** the DC variant's kit is a communication kit that balances energy transfer with other stations; the AC variant does not need it because it does not share power, so [[Share Power Between Charging Stations]] is not linked to this note. This supports AC as a stand-alone unit, but it still does not show that AC and DC name only the input source; the earlier reading is kept above, unconfirmed (IB-162, IB-163).

## Aliases


## Former ids
