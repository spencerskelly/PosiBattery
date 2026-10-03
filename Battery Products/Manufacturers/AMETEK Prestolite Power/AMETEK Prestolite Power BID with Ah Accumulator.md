---
type: Object
subtype: electrical
id: OBJ-00027
uid: 20261002162520377skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - forklift
  - charge-interface
subtypeOf:
  - "[[AMETEK Prestolite Power BID]]"
describedBy:
  - "[[Document - Prestolite BID and BID with Ah Accumulator Data Sheet 1336 (08-18)]]"
performs:
  - "[[Measure Battery Temperature]]"
  - "[[Accumulate Amp-Hours]]"
  - "[[Identify Battery to Charger]]"
  - "[[Report Battery Temperature to Charger]]"
  - "[[Log Battery Events and Usage]]"
hasDesign:
  - "[[Non-Volatile Event Memory]]"
  - "[[DC-Cable Power-Line Communication]]"
madeBy:
  - "[[AMETEK Prestolite Power]]"
---

# AMETEK Prestolite Power BID with Ah Accumulator

## Definition

AMETEK Prestolite Power BID variant that adds current monitoring to track battery amp-hour throughput.

## Notes

- Manufacturer: AMETEK Prestolite Power
- **Verification 2026-10-02 (verified):** the vendor lists a BID with Amp Hour Accumulator that adds current monitoring to track amp hours, in addition to BID features; the 2018 data sheet says it samples charge and discharge amp hours including fast transients and gives access to discharge-cycle counts based on 80 percent of the BID amp-hour setting. Source: AMETEK Prestolite Power data devices page and BID data sheet (Aug 2018) (T1) <https://www.prestolitepower.com/-/media/ametekprestolite/documentation/bid/bid-ah-accumulator-datasheet-aug-2018.pdf>
- **Not stated in retrieved sources:** current-measurement range, chemistry coverage.
- **Functions performed, with citations** (V = verified this pass, C = carried from seed text, U = user-stated):
  - [[Measure Battery Temperature]] (V): <https://www.prestolitepower.com/-/media/ametekprestolite/documentation/bid/bid-ah-accumulator-datasheet-aug-2018.pdf>
  - [[Accumulate Amp-Hours]] (V): <https://www.prestolitepower.com/products/datadevices> <https://www.prestolitepower.com/-/media/ametekprestolite/documentation/bid/bid-ah-accumulator-datasheet-aug-2018.pdf>
  - [[Identify Battery to Charger]] (V): <https://www.prestolitepower.com/-/media/ametekprestolite/documentation/bid/bid-ah-accumulator-datasheet-aug-2018.pdf>
  - [[Report Battery Temperature to Charger]] (V): <https://www.prestolitepower.com/-/media/ametekprestolite/documentation/bid/bid-ah-accumulator-datasheet-aug-2018.pdf>
- **Design characteristics, with citations:**
  - [[Non-Volatile Event Memory]] (V): <https://www.prestolitepower.com/-/media/ametekprestolite/documentation/bid/bid-ah-accumulator-datasheet-aug-2018.pdf>
- **Sources used for the mapping above:** Prestolite Data Devices page <https://www.prestolitepower.com/products/datadevices>; Prestolite BID with Ah Accumulator data sheet (Aug 2018, dated) <https://www.prestolitepower.com/-/media/ametekprestolite/documentation/bid/bid-ah-accumulator-datasheet-aug-2018.pdf>
- **Functions performed, with citations (round 11 document):**
  - [[Log Battery Events and Usage]] (V): <https://www.prestolitepower.com/-/media/ametekprestolite/documentation/bid/bid-ah-accumulator-datasheet-aug-2018.pdf> (also [[Document - Prestolite BID and BID with Ah Accumulator Data Sheet 1336 (08-18)]])
- **Design characteristics, with citations (round 11 document):**
  - [[DC-Cable Power-Line Communication]] (V): <https://www.prestolitepower.com/-/media/ametekprestolite/documentation/bid/bid-ah-accumulator-datasheet-aug-2018.pdf> (also [[Document - Prestolite BID and BID with Ah Accumulator Data Sheet 1336 (08-18)]])
- **Round 11 document:** Source: [[Document - Prestolite BID and BID with Ah Accumulator Data Sheet 1336 (08-18)]] (T1, local copy; original <https://www.prestolitepower.com/-/media/ametekprestolite/documentation/bid/bid-ah-accumulator-datasheet-aug-2018.pdf>), absorbed 2026-10-02.
| Parameter | Value as stated |
|---|---|
| Accumulator | samples charge and discharge current over 100 times per second; stores every Ah of throughput including fast transient regeneration currents |
| Readout | Ah data and battery average temperature on the Ultra Maxx, PowerStar Plus and Eclipse II front panels |
| Cycle counting | number of discharge cycles from total discharge Ah and 80% of the BID Ah setting; charge/discharge ratio from total charge Ah over total discharge Ah |
| Kits (part numbers) | 197348-001 (12-18 cells), -002 (24), -003 (36), -004 (40) |
| Accumulator functions on | Ultra Maxx, PowerStar Plus, Eclipse II controls |
| Warranty | 1 year |

## Aliases

- BID with Amp Hour Accumulator
- Ah Accumulator BID

## Former ids
