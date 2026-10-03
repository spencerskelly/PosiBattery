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
  - "[[Measure Battery Voltage]]"
  - "[[Measure Battery Current]]"
  - "[[Measure Battery Temperature]]"
  - "[[Sense Electrolyte Level]]"
  - "[[Estimate State of Charge]]"
  - "[[Log Battery Events and Usage]]"
  - "[[Communicate with Charger]]"
  - "[[Transmit Battery Data Wirelessly]]"
  - "[[Upload Battery Data to Cloud Portal]]"
hasDesign:
  - "[[Electrolyte-Immersed Temperature Sensor]]"
  - "[[Cellular Communication Interface]]"
  - "[[Acid-Resistant Sealed Housing]]"
  - "[[Cloud Portal Integration]]"
madeBy:
  - "[[PosiCharge]]"
---

# PosiCharge Battery Rx

## Definition

PosiCharge battery monitor with optional cellular connectivity, described in PosiCharge documents as a smart BMID.

## Notes

- PosiCharge's Battery Rx sheet says it monitors state of charge, water level, voltage and temperature in real time, with current measurement range of plus or minus 1000 A, an electrolyte-immersed temperature sensor rated about -20 F to 165 F, a water-level detector, 7.63 x 2.25 x 1.25 in size, and tolerance of acid immersion and pressure-wash spray. The sheet names AeroVironment, so it likely predates current ownership (dated). Source: PosiCharge Battery Rx sheet (T1), retrieved 2026-10-02. <https://www.posicharge.com/source/PDF/BatteryRx.pdf>
- The ProCore installation manual refers to the PosiCharge Battery Rx (smart BMID) and says PosiNet is accessed through it. Source: PosiCharge ProCore installation manual (T1), retrieved 2026-10-02. <https://3425125.fs1.hubspotusercontent-na1.net/hubfs/3425125/IPC%20Technical%20Documents/2-Manuals/24407-W-76_02%20ProCore%20IM.pdf>
- The SVS 80/200/300 spec sheet lists Battery Rx as an advanced battery monitor with optional cellular connectivity and data, and POSINET as collecting charge data and running usage reports (2019 sheet, dated). Source: PosiCharge SVS spec sheet (T1 (dated)), retrieved 2026-10-02. <https://www.posicharge.com/source/files/PosiCharge_80_200_300-SpecSheet-04302019.pdf>
- **Open (C2, C12, C18):** the manual calls Battery Rx a smart BMID, so it is filed under [[PosiCharge BMID]]. Which of the user-stated variants (BMID 1, BMID 3) it corresponds to is not established. Hyster Battery Tracker and Yale Battery Vision are 'Powered by PosiCharge technology' with similar listed capabilities; whether they are rebrands of this device is not stated.
- **Functions performed, with citations** (V = verified this pass, C = carried from seed text, U = user-stated):
  - [[Measure Battery Voltage]] (V): <https://www.posicharge.com/source/PDF/BatteryRx.pdf>
  - [[Measure Battery Current]] (V): <https://www.posicharge.com/source/PDF/BatteryRx.pdf>
  - [[Measure Battery Temperature]] (V): <https://www.posicharge.com/source/PDF/BatteryRx.pdf>
  - [[Sense Electrolyte Level]] (V): <https://www.posicharge.com/source/PDF/BatteryRx.pdf>
  - [[Estimate State of Charge]] (V): <https://www.posicharge.com/source/PDF/BatteryRx.pdf>
  - [[Log Battery Events and Usage]] (V): <https://www.posicharge.com/source/PDF/BatteryRx.pdf> <https://posicharge.com/products/battery-rx/>
  - [[Communicate with Charger]] (V): <https://www.posicharge.com/source/PDF/BatteryRx.pdf>
  - [[Transmit Battery Data Wirelessly]] (V): <https://www.posicharge.com/source/files/PosiCharge_80_200_300-SpecSheet-04302019.pdf>
  - [[Upload Battery Data to Cloud Portal]] (V): <https://www.posicharge.com/source/files/PosiCharge_80_200_300-SpecSheet-04302019.pdf> <https://posicharge.com/products/battery-rx/>
- **Design characteristics, with citations:**
  - [[Electrolyte-Immersed Temperature Sensor]] (V): <https://www.posicharge.com/source/PDF/BatteryRx.pdf>
  - [[Cellular Communication Interface]] (V): <https://www.posicharge.com/source/PDF/BatteryRx.pdf> <https://www.posicharge.com/source/files/PosiCharge_80_200_300-SpecSheet-04302019.pdf>
  - [[Acid-Resistant Sealed Housing]] (V): <https://www.posicharge.com/source/PDF/BatteryRx.pdf>
  - [[Cloud Portal Integration]] (V): <https://www.posicharge.com/source/files/PosiCharge_80_200_300-SpecSheet-04302019.pdf> <https://posicharge.com/products/battery-rx/>
- **Sources used for the mapping above:** Battery Rx sheet (dated) <https://www.posicharge.com/source/PDF/BatteryRx.pdf>; PosiCharge SVS 80/200/300 spec sheet (2019, dated) <https://www.posicharge.com/source/files/PosiCharge_80_200_300-SpecSheet-04302019.pdf>; PosiCharge Battery Rx page <https://posicharge.com/products/battery-rx/>
- The current Battery Rx page says it stores cumulative battery data for the life of the battery, tracks warranty compliance, monitors 24/7, offers dashboards at dealer, company, location and site levels, and is compatible with all 24 to 96 V batteries. Source: PosiCharge Battery Rx page (T1), retrieved 2026-10-02. <https://posicharge.com/products/battery-rx/>
- The Battery Rx sheet says it installs in 20 minutes, is secured to the battery, communicates with the battery chargers, and has an optional cellular connection to the PosiNet back-office system (dated sheet). Source: PosiCharge Battery Rx sheet (T1 (dated)), retrieved 2026-10-02. <https://www.posicharge.com/source/PDF/BatteryRx.pdf>
- **Public-evidence baseline (added from the vault's baseline note, round 19):**
- Public product and resource listings represent it as a current advanced battery-management tool for monitoring, recording, and reporting battery health to extend useful life and improve fleet productivity. Source: official PosiCharge page for Battery Rx, as summarized in the vault's Public Evidence Register (PUB-002, class P1/P2/P3 per that note) (T1), retrieved 2026-10-03. <https://posicharge.com/products/battery-rx/>
- **Baseline confidence (Battery Rx):** Verified public—listing/family level. **Still needed:** Obtain current controlled product sheet; resolve hardware/software/service architecture, relationship to PosiGuard, supported chemistry/data acquisition, SKU/lifecycle state, and interfaces.

## Aliases

- Battery Rx
- Smart BMID


## Former ids
