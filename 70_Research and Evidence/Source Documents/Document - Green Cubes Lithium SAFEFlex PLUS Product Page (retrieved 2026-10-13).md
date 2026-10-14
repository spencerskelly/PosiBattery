---
type: Document
subtype:
id: DOC-00115
uid: 20261013192440932skellyspencer
status: Draft
tags:
  - source-document
  - tier-T1
sourceClass: web-page
sourceUrl: "https://greencubes.com/product/safeflexplus/"
accessed: 2026-10-13
describes:
  - "[[Green Cubes SAFEFlex PLUS Battery]]"
---

# Document - Green Cubes Lithium SAFEFlex PLUS Product Page (retrieved 2026-10-13)

## Definition

Official Green Cubes product page for Lithium SAFEFlex PLUS: voltage classes, ratings, temperature, BMS, communications and certifications.

## Notes

**How it was read.** Through a fetch tool that returns a model-written summary, not the raw text, on 2026-10-13. The tool itself said the table layout was garbled and that some column assignments were inferred, so per-class values below are unverified until the raw file is read (IB-168).

- Lithium iron phosphate; 4,000 cycles; drop-in replacement for lead-acid, fits standard battery compartments, meets truck battery weight requirements.
- Classes (nominal V; operating V; capacity; energy): 24 V class 25.6 V, 24 to 28.8 V, 420 to 630 Ah, 11 to 16 kWh; 36 V class 38.4 V, 36 to 43.2 V, 525 to 945 Ah, 20 to 36 kWh; 48 V class 51.2 V, 48 to 57.6 V, 525 to 840 Ah, 26 to 43 kWh; 80 V class 83.2 V, 78 to 93.6 V, 315 to 735 Ah, 26 to 61 kWh. Arithmetic check: nominal voltage x capacity matches the stated energy in all four classes.
- Current ratings: peak discharge 600 A (24 V) and 1,200 A (36 V); continuous discharge 250 A with an SB 175 connector or 320 A with others (24 V), 320 A (36 V); further values (300 A for 315 Ah, 320 A for 420 Ah and up; continuous charge 320 A, or 240 A for 315 Ah) sit in a column the summary could not assign (C216). Since 315 Ah appears only in the 80 V range, those values most likely belong to the 80 V class (analyst inference).
- Operating temperature with heater -20 to +54 C (24 V), +55 C (36 V), +50 C (48 V), +53 C (80 V); without heater 0 C to the same upper limits. Storage 0 to +35 C, 70 percent RH or less. IP 2X. Powder-coated steel tray.
- BMS: modular, individual cell monitoring, distributed intelligence and data logging; modes Active (charging, discharging, idle) and Disabled (sleeping, ship or storage); recoverable short-circuit protection; cell over and under voltage and temperature, module overcurrent and overvoltage; manual service disconnect (listed with the 48 V and 80 V column).
- Communications: CAN bus, USB, Wi-Fi; separate CAN buses for truck and charger; all interfaces galvanically isolated; over-the-air firmware upgrades; multiple charger and vehicle protocols. Charge ports or single-point connection.
- Certifications listed: UL 2580:2020 (MH66684); ISO 13849-1:2023 and 13849-2:2012 (MH66684); UN 38.3 Rev 7; Type EE rating.
- Not stated: dimensions, weight, warranty, price, heater specification beyond temperature ranges. Links two datasheets (see [[Document - Green Cubes SAFEFlex PLUS Datasheet (2026.03.18)]] and [[Document - Green Cubes SAFEFlex PLUS Datasheet (refresh, copyright 2025)]]).

## Provenance

- **Source identity:** Green Cubes Technology, official manufacturer site.
- **Original web address:** <https://greencubes.com/product/safeflexplus/>.
- **Access date:** 2026-10-13. **Revision:** none shown on the page
- **Evidence tier:** T1 official vendor document (values second-hand through the fetch tool's summary).

## Traceability

- `describes` links the document to [[Green Cubes SAFEFlex PLUS Battery]]. Disagreements among these sources are logged in C214, C215 and C216.

## Aliases

## Former ids
