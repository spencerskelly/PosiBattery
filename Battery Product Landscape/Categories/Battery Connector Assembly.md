---
type: Object
subtype: electrical
id: OBJ-00020
uid: 20261002161409683skellyspencer
status: Draft
tags:
  - battery-landscape
  - category
abstract: true
subtypeOf:
  - "[[Battery-Connected Product]]"
describedBy:
  - "[[Battery Product Landscape Conflicts and Open Questions]]"
  - "[[Battery Product Landscape]]"
---

# Battery Connector Assembly

## Definition

Power connector set (receptacle, plug, housing, contacts, coding and optional auxiliary contacts) used to connect an industrial battery to a vehicle or a charger.

## Notes

- **Locus:** the same connector family appears on three sides: battery, vehicle and charger. Treat the connector definition as one reusable Object and record where it is used as a contextual occurrence (Local Model) rather than creating separate definitions per side. This is a modeling proposal, not an approved decision.
- **Families seen:** DIN-style (80, 160 and 320 sizes) and Anderson SB-style (SB, SBX, SBE, SBS). Regional standards named by the manufacturer: DIN 43589-1 and EN 1175-1 in Europe; UL/CSA with Anderson's voltage color chart in North America.
- Anderson's material-handling connector guide names DIN, SB, SBX and SBE products, says DIN 80, 160 and 320 have two power contacts with DIN 320 UL-rated to 350 A, and says its E-series DIN and SBE products meet battery-acid resistance. Source: Anderson Power Products guide (hosted by Mouser) (T1), retrieved 2026-10-02. <https://www.mouser.lt/pdfDocs/AG-MHCS.pdf>
- An electric forklift typically needs three connectors, one each for battery, charger and truck. DIN connectors are gendered (battery female; truck and charger male) and use coding pins to prevent a voltage mismatch. Source: TVH parts catalog (T3), retrieved 2026-10-02. <https://www.tvh.com/en-us/parts/parts-for/forklifts/electrical-parts/forklift-battery-connectors>
- A reseller says REMA connectors in the SB style are genderless, that 175 A is typical for walkies and pallet jacks and 350 A for stand-up and sit-down trucks, and that SB is an Anderson brand name. Source: Intella Parts (T3), retrieved 2026-10-02. <https://intellaparts.ca/c/battery-connectors/battery-connectors.html>
- A REMA DIN listing describes optional accessories: an air plug for electrolyte circulation, a pilot contact set and an auxiliary contact set, and coding-pin colors that distinguish dry, wet and universal batteries. Source: Akkusys shop (REMA listing) (T3), retrieved 2026-10-02. <https://akkusys.shop/en/batteries-by-application/forklifts/accessories/2249/rema-plug-euro-din-160a-50mm2-coding-pin-grey-main-contact-strain-relief>
- PosiCharge states it uses SBX or Euro connectors between battery and charger. Source: PosiCharge FAQ (T1), retrieved 2026-10-02. <https://www.posicharge.com/faq/>
- **Open:** coding-pin and color semantics differ between sources; see conflicts note item C4 and C5. No REMA or DIN primary datasheet has been opened.
- **Derived (not source-asserted):** pilot and auxiliary contacts in the connector may carry charger-to-battery signaling. Sources only list them as accessories; their use is not established.

## Aliases

- Battery plug and receptacle
- Charging connector assembly
- Forklift battery connector

## Former ids
