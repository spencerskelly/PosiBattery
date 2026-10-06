---
type: Object
subtype: electrical
id: OBJ-00310
uid: 20261003143453044skellyspencer
status: Draft
tags:
  - accessory
  - battery-market-reference
  - commercial-product
  - posicharge-baseline
  - scope-oem-option
subtypeOf:
  - "[[Charger Remote Control and Indicator]]"
performs:
  - "[[Indicate Charger Status Locally]]"
hasDesign:
  - "[[Remote Charger Status Stack Light]]"
madeBy:
  - "[[PosiCharge]]"
---

# PosiCharge Three-Color Stack Light

## Definition

PosiCharge three-color charger status light (green charged, yellow charging, red not charging or fault).

## Notes

**Summary:**
Three-color stack light for PosiCharge chargers that gives a clear visual of charge status.

**Marketed features:**
- Green = charged
- Yellow = charging
- Red = not charging or fault
- Requires the Accessory Driver Kit (ADK)

**Summary and features sources:**
Maker or publisher marketing claims as stated, not independently verified.
- PosiCharge (T1), retrieved 2026-10-04. <https://posicharge.com/accessories/>

- Public listing describes green=charged, yellow=charging, red=not charging/fault and requires an Accessory Driver Kit. Source: official PosiCharge page for Three-color stack light, as summarized in the vault's Public Evidence Register (PUB-002, class P1/P2/P3 per that note) (T1), retrieved 2026-10-03. <https://posicharge.com/accessories/>
- **Baseline confidence (Three-color stack light):** Verified public—listing level. **Still needed:** Electrical interface; compatible products; mounting options; current SKU; environmental/regulatory rating.
- **Functions performed, with citations:**
  - [[Indicate Battery Status Locally]] (V): <https://posicharge.com/accessories/>

- **Architecture realization:** [[Remote Charger Status Stack Light]] is verified. PosiCharge states that the light requires an Accessory Driver Kit, so the output-driver role is external to the stack-light product; no internal [[Status Indicator Driver Circuit]] is assigned to the light itself.

## Aliases

- stack light

## Former ids
