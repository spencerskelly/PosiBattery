---
type: Object
subtype: electrical
id: OBJ-00210
uid: 20261003093855179skellyspencer
status: Draft
tags:
  - accessory
  - battery-market-reference
  - charger-accessory
  - commercial-product
  - scope-oem-option
subtypeOf:
  - "[[Charger Remote Control and Indicator]]"
performs:
  - "[[Indicate Charger Status Locally]]"
hasDesign:
  - "[[Remote Charger Status Stack Light]]"
  - "[[Local LED Indicator]]"
hasPart:
  - "[[LED Status Indicator Element]]"
  - "[[Status Indicator Driver Circuit]]"
offeredBy:
  - "[[Crown Equipment]]"
offeredWith:
  - "[[Crown V-HFM3 Charger]]"
---

# Crown V-HFM3 Tower Light Kit

## Definition

Crown option kit (part 396586-001) with an LED light that shows battery charge status from a distance.

## Notes

**Summary:**
Option kit for the Crown V-HFM3 charger that adds a pole-mounted LED tower light showing battery charge status from a distance.

**Marketed features:**
- LED indication of battery charge status visible from a distance
- Part no. 396586-001
- Includes 11.81 in pole with mounting bracket
- Includes I/O expansion board with internal wiring loom, expansion-board and DE9 mounting standoffs

**Summary and features sources:**
Maker or publisher marketing claims as stated, not independently verified.
- Crown (T1), retrieved 2026-10-04. <https://www.crown.com/content/dam/crown/pdfs/en-us/brochures/products/vhfm3-chargers.pdf>

- Crown's brochure lists the Tower Light Kit, part 396586-001: an LED light indicates battery charge status from a distance, supplied with a pole and mounting bracket, an I/O expansion board with mounting standoff and DE9 mounting standoffs. Source: Crown V-HFM3 brochure (copy in repo) (T1), retrieved 2026-10-03. <https://www.crown.com/content/dam/crown/pdfs/en-us/brochures/products/vhfm3-chargers.pdf>
- **Functions performed, with citations:**
  - [[Indicate Battery Status Locally]] (V): <https://www.crown.com/content/dam/crown/pdfs/en-us/brochures/products/vhfm3-chargers.pdf>
- **Design characteristics, with citations:**
  - [[Local LED Indicator]] (V): <https://www.crown.com/content/dam/crown/pdfs/en-us/brochures/products/vhfm3-chargers.pdf>

- **Architecture realization:** [[Remote Charger Status Stack Light]] is verified by the tower-light implementation. [[LED Status Indicator Element]] is verified by Crown's explicit LED description. [[Status Indicator Driver Circuit]] is supported by the included I/O expansion board; the generic circuit abstraction does not claim Crown's exact schematic.

## Aliases

- 396586-001


## Former ids
