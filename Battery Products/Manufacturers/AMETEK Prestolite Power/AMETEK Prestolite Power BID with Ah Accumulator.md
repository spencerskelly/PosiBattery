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
performs:
  - "[[Identify Battery to Charger]]"
  - "[[Report Battery Temperature to Charger]]"
  - "[[Measure Battery Temperature]]"
  - "[[Accumulate Amp-Hours]]"
hasDesign:
  - "[[Non-Volatile Event Memory]]"
---

# AMETEK Prestolite Power BID with Ah Accumulator

## Definition

AMETEK Prestolite Power BID variant that adds current monitoring to track battery amp-hour throughput.

## Notes

- Manufacturer: AMETEK Prestolite Power
- **Verification 2026-10-02 (verified):** the vendor lists a BID with Amp Hour Accumulator that adds current monitoring to track amp hours, in addition to BID features; the 2018 data sheet says it samples charge and discharge amp hours including fast transients and gives access to discharge-cycle counts based on 80 percent of the BID amp-hour setting. Source: AMETEK Prestolite Power data devices page and BID data sheet (Aug 2018) (T1) <https://www.prestolitepower.com/-/media/ametekprestolite/documentation/bid/bid-ah-accumulator-datasheet-aug-2018.pdf>
- **Not stated in retrieved sources:** current-measurement range, chemistry coverage.
- **Functions performed (evidence):** [[Identify Battery to Charger]] (V); [[Report Battery Temperature to Charger]] (V); [[Measure Battery Temperature]] (V); [[Accumulate Amp-Hours]] (V). V = verified this pass, C = carried from seed text, U = user-stated.
- **Design characteristics (evidence):** [[Non-Volatile Event Memory]] (V).

## Aliases

- BID with Amp Hour Accumulator
- Ah Accumulator BID

## Former ids
