---
type: Document
subtype:
id: DOC-00110
uid: 20261013180756225skellyspencer
status: Draft
tags:
  - source-document
  - datasheet
  - tier-T1
sourceClass: datasheet
sourceUrl: "https://posicharge.com/wp-content/uploads/2026/01/High-Voltage-Power-Station-Product-Card-1.pdf"
sourceRevision: "PDF metadata creation date 2026-06-24; two pages; no version marking"
describes:
  - "[[PosiCharge High Voltage Power Station]]"
---

# Document - PosiCharge High Voltage Power Station Product Card (2026)

## Definition

PosiCharge two-page product card for the High Voltage Power Station: page 1 gives the headline and key features, page 2 gives the specification table. The AC and DC listings on posicharge.com link this same file.

## Notes

Values are as printed. Page 2 has no extractable text (it is an image), so plain text extraction returns page 1 only; the table below was read from the rendered page image on 2026-10-13. Text-recognition output was checked against the image and not used for any value.

**Page 1 (headline and key features)**

- Headline: 20kW DC Fast Charger for eGSE + EVs, with a second line giving 30kW quick charge via CCS1 and NACS.
- Install: runs on the PosiCharge DC bus or stand-alone.
- Features listed: high-voltage power delivery for compatible eGSE and EVs; backwards compatible with DVS and MVS systems with a required software update; scalable power infrastructure that expands fleet charging without new utility drops by replacing a standard power station with a high-voltage unit; CCS1 or NACS single-port output with a standard 5 m connector; NEMA 3S enclosure for industrial environments; built on proven modular power conversion technology.

**Page 2 (specification table)**

- Input voltage: PosiCharge DC bus; 240 Vac single phase; 208 or 240 Vac three-phase delta (3P + PE); 480/277 Vac three-phase wye (3P + N + PE).
- Input operating range and current: 240 Vac single phase 216 to 252 V, 150 A max, 60 Hz; 208/240 Vac three-phase delta 190 to 252 V, 100 A max, 60 Hz; 480 Vac three-phase wye 432 to 504 V, 45 A max, 60 Hz.
- Output power: 20 kW maximum via PosiCharge DC bus; 30 kW maximum via AC input.
- Output voltage: 250 to 920 Vdc. Efficiency: 95 percent (peak or rated point not stated).
- Charging connector: CCS1 and NACS. Cable length: 5 m standard.
- Charging and data protocols: DIN 70121 and OCPP 1.6J compliant. Network interface: cellular 4G LTE, Wi-Fi. Display: 7 inch color LCD.
- Operational temperature -30 to +50 C; storage temperature -40 to +80 C; relative humidity up to 95 percent non-condensing; altitude 2000 m (6560 ft).
- Enclosure rating NEMA 3S and IP54; impact resistance IK10; weight 140 kg (charger only); mounting wall-mounted or pedestal, both sold separately.
- Certifications: AC configuration cETLus listed to UL 2202, UL 2231-1 and -2, and CSA C22.2 No. 281.1, 281.2 and 346. DC configuration cETLus listing pending.

**Checks by the note author (derived, not stated by the source)**

- The headline (20 kW) and the second line (30 kW) are explained by the output power row: 20 kW applies on the PosiCharge DC bus and 30 kW on AC input. Whether the second line refers to the AC-fed case is an inference (see C81).
- No output current is printed. At 30 kW the current would be about 120 A at 250 Vdc and about 33 A at 920 Vdc; at 20 kW about 80 A at 250 Vdc. These are arithmetic, not ratings.
- Each input rating covers the input power needed for 30 kW at 95 percent efficiency (about 31.6 kW): the maximum input currents give about 36.0 kVA (240 V single phase), about 36.0 kVA (208 V three-phase) and about 37.4 kVA (480 V three-phase). Power factor is not stated.
- The card names an AC configuration and a DC configuration in the certification row; it does not define them.

## Provenance

- **Local artifact:** `Reference Files/High-Voltage-Power-Station-Product-Card-1.pdf` (kept in the repo).
- **Source identity:** PosiCharge (a product line of Ampure), official resources page <https://posicharge.com/product-resources/>.
- **Original web address:** <https://posicharge.com/wp-content/uploads/2026/01/High-Voltage-Power-Station-Product-Card-1.pdf>. The live file could not be fetched during the 2026-10-13 review (the site's robots rules block the fetch tool), so it is not confirmed that the live file equals the repo copy (C210).
- **Document date / revision:** the web address path contains 2026/01, while the PDF metadata creation date is 2026-06-24; which is the publication date is unknown.
- **Evidence tier:** T1 manufacturer document.

## Traceability

- `describes` links the card to the merged product note, which covers both listings that share it.
- Earlier vault summaries of the card record page 1 only; the page 2 values above were not on any note before 2026-10-13.
- Conflicts and open questions: C81, C82, C210 in [[Battery Product Landscape Conflicts and Open Questions]].

## Aliases

- High Voltage Power Station product card

## Former ids
