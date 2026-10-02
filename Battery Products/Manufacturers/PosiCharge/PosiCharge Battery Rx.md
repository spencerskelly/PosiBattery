---
type: Object
subtype: electrical
id: OBJ-00032
uid: 20261002164202400skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - forklift
  - lead-acid
  - stated-in-posicharge-docs
subtypeOf:
  - "[[PosiCharge BMID]]"
describedBy:
  - "[[Battery Product Landscape Conflicts and Open Questions]]"
performs:
  - "[[Estimate State of Charge]]"
  - "[[Sense Electrolyte Level]]"
  - "[[Measure Battery Voltage]]"
  - "[[Measure Battery Temperature]]"
  - "[[Measure Battery Current]]"
  - "[[Transmit Battery Data Wirelessly]]"
  - "[[Upload Battery Data to Cloud Portal]]"
hasDesign:
  - "[[Electrolyte-Immersed Temperature Sensor]]"
  - "[[Acid-Resistant Sealed Housing]]"
  - "[[Cellular Communication Interface]]"
  - "[[Cloud Portal Integration]]"
---

# PosiCharge Battery Rx

## Definition

PosiCharge battery monitor with optional cellular connectivity, described in PosiCharge documents as a smart BMID.

## Notes

- PosiCharge's Battery Rx sheet says it monitors state of charge, water level, voltage and temperature in real time, with current measurement range of plus or minus 1000 A, an electrolyte-immersed temperature sensor rated about -20 F to 165 F, a water-level detector, 7.63 x 2.25 x 1.25 in size, and tolerance of acid immersion and pressure-wash spray. The sheet names AeroVironment, so it likely predates current ownership (dated). Source: PosiCharge Battery Rx sheet (T1), retrieved 2026-10-02. <https://www.posicharge.com/source/PDF/BatteryRx.pdf>
- The ProCore installation manual refers to the PosiCharge Battery Rx (smart BMID) and says PosiNet is accessed through it. Source: PosiCharge ProCore installation manual (T1), retrieved 2026-10-02. <https://3425125.fs1.hubspotusercontent-na1.net/hubfs/3425125/IPC%20Technical%20Documents/2-Manuals/24407-W-76_02%20ProCore%20IM.pdf>
- The SVS 80/200/300 spec sheet lists Battery Rx as an advanced battery monitor with optional cellular connectivity and data, and POSINET as collecting charge data and running usage reports (2019 sheet, dated). Source: PosiCharge SVS spec sheet (T1 (dated)), retrieved 2026-10-02. <https://www.posicharge.com/source/files/PosiCharge_80_200_300-SpecSheet-04302019.pdf>
- **Open (C2, C12, C18):** the manual calls Battery Rx a smart BMID, so it is filed under [[PosiCharge BMID]]. Which of the user-stated variants (BMID 1, BMID 3) it corresponds to is not established. Hyster Battery Tracker and Yale Battery Vision are 'Powered by PosiCharge technology' with similar listed capabilities; whether they are rebrands of this device is not stated.
- **Functions performed (evidence):** [[Estimate State of Charge]] (V); [[Sense Electrolyte Level]] (V); [[Measure Battery Voltage]] (V); [[Measure Battery Temperature]] (V); [[Measure Battery Current]] (V); [[Transmit Battery Data Wirelessly]] (V); [[Upload Battery Data to Cloud Portal]] (V). V = verified this pass, C = carried from seed text, U = user-stated.
- **Design characteristics (evidence):** [[Electrolyte-Immersed Temperature Sensor]] (V); [[Acid-Resistant Sealed Housing]] (V); [[Cellular Communication Interface]] (V); [[Cloud Portal Integration]] (V).

## Aliases

- Battery Rx
- Smart BMID

## Former ids
