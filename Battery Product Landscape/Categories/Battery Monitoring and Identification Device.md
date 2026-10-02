---
type: Object
subtype: electrical
id: OBJ-00019
uid: 20261002161409682skellyspencer
status: Draft
tags:
  - battery-landscape
  - category
abstract: true
subtypeOf:
  - "[[Battery-Connected Product]]"
supertypeOf:
  - "[[Battery Monitoring Device]]"
  - "[[Battery Identification and Charge Interface Device]]"
describedBy:
  - "[[Battery Product Landscape Conflicts and Open Questions]]"
  - "[[Battery Product Landscape]]"
---

# Battery Monitoring and Identification Device

## Definition

Battery-mounted device that measures battery condition (for example temperature, voltage, electrolyte level, charge history) and/or identifies the battery to a charger so the charger can choose a profile.

## Notes

- **Locus:** battery-mounted. Evidence covers lead-acid forklift batteries. Chemistry coverage for lithium is not established.
- **Naming warning:** the acronym BMID is used by at least two vendors for products that are not shown to be equivalent. See [[Battery Product Landscape Conflicts and Open Questions]] item C1. Do not merge by name.
- PosiCharge states its BMID is installed on the battery and has two parts: an electrolyte-immersed thermistor that signals the charger to adjust its algorithm, and an electronic device that stores battery identity, charging profile and charge-event history. Source: PosiCharge FAQ (T1), retrieved 2026-10-02. <https://www.posicharge.com/faq/>
- PosiCharge Battery Rx is described as monitoring state of charge, water level, voltage and temperature, with a current range of plus or minus 1000 A, an electrolyte-immersed temperature sensor rated about -20 F to 165 F, a water-level detector, and acid-immersion and pressure-wash tolerance. The sheet refers to AeroVironment, so it likely predates the current ownership; market status unclear. Source: PosiCharge Battery Rx sheet (T1 (possibly dated)), retrieved 2026-10-02. <https://www.posicharge.com/source/PDF/BatteryRx.pdf>
- PosiCharge ProCore Edge supports three charge-start modes (CAN/lithium, BMID, voltage) and communicates with a wireless BMID over Bluetooth; the ProCore manual says a charger charges a battery with a BMID without further configuration and uses default settings without one. Source: PosiCharge ProCore Edge page and ProCore installation manual (T1), retrieved 2026-10-02. <https://www.posicharge.com/procoreedge>
- Crown sells a V-Force Battery Monitoring Identification Device (part 396525-BTM) with dual charge profiles for opportunity or fast charging, battery-event recording, spill-resistant housing and Bluetooth Class 1. Listed price at retrieval: 583.33 USD. Source: Crown parts shop (T1), retrieved 2026-10-02. <https://shop.crown.com/crown/en/Batteries-and-Chargers/Battery-and-Charger-Parts-and-Accessories/Battery-and-Charger-Accessories//p/396525-BTM>
- Crown describes an optional BMID module for its FS3/HFM3 chargers that mounts on top of a lead-acid battery, detects low electrolyte, monitors voltage and temperature, and adjusts charge rate. Source: Crown (regional page) (T1), retrieved 2026-10-02. <https://crown.com/en-vn/batteries-and-chargers/vhfm3-charger.html>
- **Imported products:** the earlier seed branch products now sit under [[Battery Monitoring Device]] and [[Battery Identification and Charge Interface Device]]. Verification status is on each product note; Energywith and Flow-Rite items remain unverified. Competitor comparison: [[BMID Competitor Landscape]].
- **Not stated in retrieved sources:** how a Crown BMID connects to a charger (analog, wireless or other). Do not assume it matches PosiCharge.

## Aliases

- BMID class
- Battery monitor
- Battery ID device

## Former ids
