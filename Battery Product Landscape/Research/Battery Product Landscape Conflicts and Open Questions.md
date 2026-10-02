---
type: Info
subtype:
id: INFO-00071
uid: 20261002161409691skellyspencer
status: Draft
tags:
  - battery-landscape
  - conflicts
  - open-questions
describes:
  - "[[Battery Monitoring and Identification Device]]"
  - "[[Battery Connector Assembly]]"
  - "[[Battery Thermal Management Device]]"
  - "[[Industrial Battery Charger]]"
---

# Battery Product Landscape Conflicts and Open Questions

## Definition

Register of conflicting, ambiguous or unverified evidence and open modeling questions found while building the landscape survey.

## Notes

- Each item states what differs, the sources, and what would resolve it. Nothing here is resolved. Items stay visible until a primary source or a user decision settles them.
- **C1 - BMID acronym used by two vendors.** PosiCharge expands it as Battery Monitor and Identifier (FAQ) or Smart Battery Monitor and Identification Device (spec sheets). Crown expands it as Battery Monitoring Identification Device. Crown describes it as a lead-acid battery-top module that detects low electrolyte and adjusts charge rate; PosiCharge describes it as holding identity, profile and event history with an immersed thermistor. No source shows they are interchangeable or compatible. Resolve with: both vendors' datasheets; keep as separate Objects. Sources: PosiCharge FAQ <https://www.posicharge.com/faq/>; Crown <https://shop.crown.com/crown/en/Batteries-and-Chargers/Battery-and-Charger-Parts-and-Accessories/Battery-and-Charger-Accessories//p/396525-BTM>.
- **C2 - What a PosiCharge BMID physically includes.** The FAQ says the BMID has two parts, an immersed thermistor and an electronic device. Charger spec sheets list a Smart BMID and an Electrolyte Immersed Thermistor as separate features. The ProCore manual calls Battery Rx a smart BMID, and ProCore Edge refers to a wireless BMID over Bluetooth. This suggests several BMID hardware variants, but no source lists them. Resolve with: PosiCharge BMID and Battery Rx datasheets and part numbers. Sources: <https://www.posicharge.com/faq/>; <https://www.posicharge.com/source/PDF/2500series.pdf>; <https://www.posicharge.com/procoreedge>.
- **C3 - Age of PosiCharge documents.** The Battery Rx sheet names AeroVironment and the 2500 Series sheet mentions approvals 'in process'. Both likely predate current product lines. Treat their specifications as possibly obsolete until current documents confirm. Source: <https://www.posicharge.com/source/PDF/BatteryRx.pdf>.
- **C4 - Connector color and voltage coding.** One reseller says any color connector can be used on any forklift battery, then says not to mix colors and that a battery will not accept a charger set to a different voltage. Anderson and TVH describe color or coding pins as the mechanism that prevents a voltage mismatch. The reseller wording is ambiguous or inaccurate. Resolve with: Anderson's voltage and color chart and the REMA datasheet. Sources: <https://intellaparts.ca/c/battery-connectors/battery-connectors.html>; <https://www.mouser.lt/pdfDocs/AG-MHCS.pdf>; <https://www.tvh.com/en-us/parts/parts-for/forklifts/electrical-parts/forklift-battery-connectors>.
- **C5 - DIN coding-pin meaning.** TVH describes coding pins as preventing voltage mismatch. A REMA listing describes pin color as distinguishing dry, wet and universal batteries. These may both be true on different pin attributes (position vs color), but no source says so. Resolve with: DIN 43589-1 and REMA datasheet. Sources: TVH and Akkusys links in [[Battery Connector Assembly]].
- **C6 - Cold-weather figures are not comparable.** Toyota: cold-store version used down to -30 C. BSLBATT: heating 'up to -40 C'. ROYPOW: rated -40 C, charging in place typically to -30 C. Stromcore: tested idle at -40 F (equal to -40 C) for up to 14 hours. These describe operating, storage and charging limits inconsistently. Resolve with: per-vendor datasheets that separate operating, storage and charge limits. Sources: links in [[Battery Thermal Management Device]].
- **C7 - Heater power source varies.** BSLBATT describes a heater designed to run during overnight in-truck charging. Stromcore describes a heater drawing about 2 percent of battery capacity. ROYPOW says buyers should ask whether it runs off the charger or the cells. No retrieved source gives a per-product answer. Resolve with: datasheets and manuals.
- **C8 - Superlative claim.** Green Cubes states it is the only manufacturer of both Li-ion batteries and chargers for material handling equipment. HOPPECKE markets its own batteries and chargers, but the retrieved HOPPECKE evidence is lead-acid, so this is not a direct contradiction. Not tested. Source: <https://www.groundhandlinginternational.com/content/news/green-cubes-announces-patent-award-for-bms>.
- **C9 - Protection hardware applicability.** Sources for contactors, pre-charge and pyro fuses are automotive or high-voltage EV. Applicability to 24 to 96 V MHE and GSE batteries is unverified. Do not carry these into MHE or GSE models without an MHE or GSE source.
- **Q1 - Scope.** Installed-only (as in the seed branch) or all battery-connected products with locus recorded per product? This survey used the second.
- **Q2 - Category subtype.** Categories use Object subtype by dominant discipline (electrical or mechanical) and the root uses part. Subtype for abstract families is provisional.
- **Q3 - One product, several families.** Battery Rx is monitor, identifier and telematics. Multiple subtypeOf or one primary family?
- **Q4 - Schema gaps.** The schema has no first-class type for manufacturer, market, or evidence tier, and `derivedFrom` is Requirement-only. This survey records those as note text. An amendment is a release-owner decision, not made here.
- **Q5 - Evidence tiers.** Proposed tiers in [[Battery Product Landscape]] need approval or replacement.

## Aliases

- Landscape conflicts register

## Former ids
