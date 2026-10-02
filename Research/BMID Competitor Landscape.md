---
type: Info
subtype:
id: INFO-00073
uid: 20261002162520382skellyspencer
status: Draft
tags:
  - battery-landscape
  - competitors
  - bmid
describes:
  - "[[PosiCharge BMID]]"
  - "[[Battery Identification and Charge Interface Device]]"
  - "[[Battery Monitoring Device]]"
---

# BMID Competitor Landscape

## Definition

Working comparison of battery-installed identification and monitoring products against the PosiCharge BMID family, with only evidence-backed facts and explicit unknowns.

## Notes

- **Method:** web search on 2026-10-02; vendor pages where retrieved, otherwise trade press. Unknown means no retrieved source states it, not that the product lacks it. No datasheet was opened except Prestolite BID Ah Accumulator.
- **Reading guide:** closest functional matches to the PosiCharge BMID are the products that identify the battery to a charger and report temperature: [[Crown V-Force BMID]], [[AMETEK Prestolite Power BID]] and [[Fronius TagID]]. EnerSys, Philadelphia Scientific and WBID Pro are monitoring and data products with no retrieved evidence of charger interaction.

| Product | Maker | Mount / locus | Charger link (evidence) | Wireless | CAN | Sensors stated | Chemistry stated | Status evidence |
|---|---|---|---|---|---|---|---|---|
| PosiCharge BMID family (BMID 1, BMID 3, Battery Rx, PosiGuard) | PosiCharge | on battery | sends temperature to charger; stores identity and profile (FAQ) | BLE option on BMID 3 (user); Bluetooth on PosiGuard app | BMID 3 CAN option (user) | immersed thermistor; level on Battery Rx | lead-acid (FAQ context); lithium GSE rule C17 | current per user |
| Crown V-Force BMID | Crown | battery top | adjusts charge rate for Crown chargers; method unknown | Bluetooth Class 1 (configuration) | n/s | voltage, temperature, low electrolyte | lead-acid | listed for sale |
| AMETEK Prestolite BID / BID with Ah Accumulator | AMETEK Prestolite | on battery | provides ID, type, Ah, cells, start rate, temperature to charger | none stated | none stated | temperature; Ah (Accumulator) | n/s | current page |
| AMETEK Prestolite WBID Pro | AMETEK Prestolite | battery-mounted | n/s for Pro (obsolete WBID: over DC cable, 2014) | ZigBee | n/s | level, electrolyte and ambient temperature | n/s | current page |
| AMETEK Prestolite TruBid | AMETEK Prestolite | battery top, probe in cell | works with charger to end charge; wireless download to charger | wireless to charger | n/s | electrolyte temperature, specific gravity | lead-acid | trade press; status unclear |
| Power Designers PowerTrac 3 | Power Designers | on battery | REVOLUTION charger recognizes battery voltage and Ah capacity | wireless, band n/s | n/s | voltage, temperature, current, electrolyte level | n/s | vendor page 2024 |
| Power Designers PowerTrac SP+ | Power Designers | on battery | RS-485 PowerCharge interface option | wireless n/s; IR | n/s | voltage, current (ext. shunt), temperature, level option | any, 12-84 V | data sheet 2014 |
| EnerSys Wi-iQ4 (Wi-iQ3 lineage) | EnerSys | on battery harness | Wi-iQ3 brochure: wireless to EnerSys modular charger (generation caveat, C16) | Zigbee, BLE | optional (CANopen, J1939) | voltage incl. half-battery | flooded, VRLA, TPPL | manual 05/2024 |
| EnerSys iQ Mini | EnerSys | on battery | none stated | BLE | none stated | not detailed | flooded, VRLA, TPPL | launched 2024 |
| HOPPECKE trak collect | HOPPECKE | permanently on battery | communicates with charger; temperature-controlled charging | n/s (LIN, battery bus) | n/s | voltage, current, temperature, electrolyte level | lead-acid | vendor page |
| Fronius TagID / TagID+ | Fronius | on battery | charger adjusts to battery temperature (Selectiva 4.0) | n/s | n/s | temperature; level on TagID+ | wet and gel lead-acid | 2022 launch |
| Crown Battery Health Monitor | Crown | on battery | none stated | Bluetooth to InfoLink | n/s | temperature, water level, Ah | lead-acid | trade press |
| Raymond iBattery | Raymond | on battery | none stated | via iWarehouse | n/s | temperature, water level, voltage, SOC, weight | lead-acid | 2010 launch; current page caution |
| Hyster Battery Tracker / Yale Battery Vision | Hyster-Yale | stays with battery | none stated | cellular | n/s | SOC, water, voltage, current, temperature | n/s | trade press; powered by PosiCharge |
| Philadelphia Scientific eGO! range | Philadelphia Scientific | battery top | none stated | cloud upload / USB | n/s | LED alerts; data | lead-acid | trade press, undated |
| Access Control Group CellTrac | Access Control Group | n/s | none stated | n/s | n/s | voltage, Ah, temperature, water level | n/s | undated; status unclear |

- **Previously listed as candidates, now modeled:** [[HOPPECKE trak collect]] and [[Hyster Battery Tracker]] (an OEM channel for PosiCharge technology, conflicts C18). Wider function and design comparison: [[Battery Monitoring Function Map]], [[Battery Monitoring Design Map]], [[Battery Monitoring Performance Comparison]].
- **Lithium side not covered:** products that identify or interface lithium batteries (BMS-to-charger CAN) are in [[Battery Management System]]. Whether a BMID-class device competes with a BMS for lithium customers is open.
- **Not covered:** Zivan, Delta-Q, Lester, Exide, Jungheinrich, Linde, Toyota device-level products, Midtronics, Asian vendors, and general-purpose battery monitors (marine, RV, solar). Japanese BTRC-R100 and BTRC-Z100 lead-acid monitors appear in a catalog with no maker identified.
- **Refresh 2026-10-02:** table rebuilt with 17 rows. Wi-iQ charger link corrected (C16); PowerTrac, TruBid, HOPPECKE and others added. The earlier version said no charger interaction was stated for Wi-iQ.

## Aliases

- BMID competitors

## Former ids
