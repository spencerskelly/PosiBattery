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
performs:
  - "[[Measure Battery Temperature]]"
  - "[[Identify Battery to Charger]]"
  - "[[Report Battery Temperature to Charger]]"
hasDesign:
  - "[[Non-Volatile Event Memory]]"
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

## Aliases

- Prestolite BID
- Battery Identification Device (BID)

## Former ids
