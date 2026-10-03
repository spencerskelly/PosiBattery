---
type: Object
subtype: electrical
id: OBJ-00010
uid: 20261002150858946skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - forklift
  - charge-interface
subtypeOf:
  - "[[Battery Identification and Charge Interface Device]]"
supertypeOf:
  - "[[AMETEK Prestolite Power BID with Ah Accumulator]]"
describedBy:
  - "[[Document - Prestolite BID and BID with Ah Accumulator Data Sheet 1336 (08-18)]]"
performs:
  - "[[Measure Battery Temperature]]"
  - "[[Identify Battery to Charger]]"
  - "[[Report Battery Temperature to Charger]]"
hasDesign:
  - "[[Non-Volatile Event Memory]]"
  - "[[DC-Cable Power-Line Communication]]"
madeBy:
  - "[[AMETEK Prestolite Power]]"
offeredWith:
  - "[[AMETEK Prestolite Power Eclipse II]]"
  - "[[AMETEK Prestolite Power ULTRA]]"
---

# AMETEK Prestolite Power BID

## Definition

AMETEK Prestolite Power Battery Identification Device that provides a compatible forklift charger with battery identity, configuration, and temperature information.

## Notes

- Manufacturer: AMETEK Prestolite Power
- Market evidence checked: 2026-10-02
- Installation locus: battery device used with motive-power batteries.
- Published charger data includes battery ID, battery type, amp-hour capacity, number of cells, charge start rate, and continuous temperature updates.
- The charger uses this information for a battery-specific temperature-compensated charge profile.
- Evidence: https://www.prestolitepower.com/products/datadevices/bid
- **Verification 2026-10-02 (re-verified):** the BID provides the charger with battery ID, battery type, Ah capacity, cell count and start rate, and updates battery temperature throughout the charge so any BID-capable controlled charger can run a temperature-compensated profile. Source: AMETEK Prestolite Power BID page (T1) <https://www.prestolitepower.com/products/datadevices/bid>
- **Variant:** a BID with Amp Hour Accumulator exists; see [[AMETEK Prestolite Power BID with Ah Accumulator]].
- **Not stated in retrieved sources:** how temperature is sensed, chemistry coverage, and the physical interface to the charger.
- **Functions performed, with citations** (V = verified this pass, C = carried from seed text, U = user-stated):
  - [[Measure Battery Temperature]] (V): <https://www.prestolitepower.com/products/datadevices/bid>
  - [[Identify Battery to Charger]] (V): <https://www.prestolitepower.com/products/datadevices/bid>
  - [[Report Battery Temperature to Charger]] (V): <https://www.prestolitepower.com/products/datadevices/bid>
- **Design characteristics, with citations:**
  - [[Non-Volatile Event Memory]] (V): <https://www.prestolitepower.com/-/media/ametekprestolite/documentation/bid/bid-ah-accumulator-datasheet-aug-2018.pdf>
- **Sources used for the mapping above:** Prestolite BID page <https://www.prestolitepower.com/products/datadevices/bid>; Prestolite BID with Ah Accumulator data sheet (Aug 2018, dated) <https://www.prestolitepower.com/-/media/ametekprestolite/documentation/bid/bid-ah-accumulator-datasheet-aug-2018.pdf>
- **Related products and how they differ (offeredWith):**
  - [[AMETEK Prestolite Power Eclipse II]]: on the Eclipse II the BID is optional and holds capacity, voltage and battery type.
  - [[AMETEK Prestolite Power ULTRA]]: on the ULTRA opportunity and fast models a BID is required to monitor battery temperature.
- **Design characteristics, with citations (round 11 document):**
  - [[DC-Cable Power-Line Communication]] (V): <https://www.prestolitepower.com/-/media/ametekprestolite/documentation/bid/bid-ah-accumulator-datasheet-aug-2018.pdf> (also [[Document - Prestolite BID and BID with Ah Accumulator Data Sheet 1336 (08-18)]])
- **Round 11 document:** Source: [[Document - Prestolite BID and BID with Ah Accumulator Data Sheet 1336 (08-18)]] (T1, local copy; original <https://www.prestolitepower.com/-/media/ametekprestolite/documentation/bid/bid-ah-accumulator-datasheet-aug-2018.pdf>), absorbed 2026-10-02.
| Parameter | Value as stated |
|---|---|
| Stored and programmable data | identification numbers, voltages, amp-hour sizes, start rates, construction types; battery voltage, temperature and amp-hour usage readable on demand |
| Temperature compensation | optimum temperature-compensated profile from 32 to 158 F (0 to 70 C) with a controlled-output charger |
| Communication | through the standard charging cables and connectors; no special wiring or SBX connectors |
| Memory | non-volatile; rugged construction, wide operating temperature |
| Kits (part numbers) | 194304-001 (12-18 cells), -002 (24 cells), -003 (36 cells), -004 (40 cells) |
| Charger controls | BID functions on AC2000 (Ferro), UC2000 (Ultra Charge, Ultra Maxx), SCR2000 (PowerStar, PowerStar Plus), EC2000 (Eclipse II) |
| Warranty | 1 year |
| Recommendation | strongly suggested on all opportunity or fast charge applications |
- **Gap closed:** earlier notes said how the BID reaches the charger was not stated; it is power line communication over the charging cables (see [[DC-Cable Power-Line Communication]]). How temperature is sensed is still not stated (battery average temperature).

## Aliases

- Prestolite BID
- Battery Identification Device (BID)


## Former ids
