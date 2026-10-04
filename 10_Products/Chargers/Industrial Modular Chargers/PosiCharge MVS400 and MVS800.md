---
type: Object
subtype: electrical
id: OBJ-00252
uid: 20261003094918671skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - charger
  - gse
subtypeOf:
  - "[[Industrial Modular Charger]]"
performs:
  - "[[Charge Battery Fast]]"
madeBy:
  - "[[PosiCharge]]"
offeredWith:
  - "[[PosiCharge BMID]]"
---

# PosiCharge MVS400 and MVS800

## Definition

PosiCharge multi-port GSE chargers for 24 to 96 V for tow tugs, baggage tractors and belt loaders.

## Notes

- PosiCharge's MVS sheets say the MVS400 and MVS800 cover 24 to 96 V, share the DVS's power quality and data capabilities, work with BMID, Battery Rx and PosiNet, charge 3 times the equipment on the same power as conventional chargers and need no battery changing. Source: PosiCharge MVS400 and MVS800 sheets (T1), retrieved 2026-10-03. <https://og.mhi.org/media/members/16696/131261342583679925.pdf>
- Airport Technology lists the MVS400 and MVS800 as GSE chargers for tow tugs, baggage tractors and belt loaders. Source: Airport Technology (T2), retrieved 2026-10-03. <https://www.airport-technology.com/contractors/groundequipment/posicharge/>
- **Earlier note (Q10):** the PosiCharge web pages for MVS400 and MVS800 show inconsistent numbers; these sheets give no kW or A values in the retrieved text.
- **Functions performed, with citations:**
  - [[Charge Battery Fast]] (V): <https://og.mhi.org/media/members/16696/131261342583679925.pdf>
- **Public-evidence baseline (added from the vault's baseline note, round 19):**
- Multi-vehicle GSE fast-charge system. Public page lists a 40 kW power server, 24–96 V battery range, 250 A dual-mode / 500 A single-mode output, RS-232, 480/600 VAC input, 0.96 power factor, 90% efficiency, NEMA 3R, BMID recognition, power sharing, and up to eight simultaneous vehicles. Source: official PosiCharge page for MVS400, as summarized in the vault's Public Evidence Register (PUB-008 and PUB-009, class P1/P2/P3 per that note) (T1), retrieved 2026-10-03. <https://posicharge.com/products/mvs400/>
- **Baseline confidence (MVS400):** Verified public—system level. **Still needed:** Obtain topology/configuration guide; explain power-server vs. power-station rating, valid port counts, output allocation, installation architecture, connector choices, and current commercial configuration.
- Multi-vehicle GSE fast-charge system. Public page lists an 80 kW power server, 24–96 V battery range, 250 A dual-mode / 500 A single-mode output, RS-232, 0.96 power factor, 95% listed power-server efficiency, and up to 16 simultaneous vehicles. Source: official PosiCharge page for MVS800, as summarized in the vault's Public Evidence Register (PUB-008 and PUB-009, class P1/P2/P3 per that note) (T1), retrieved 2026-10-03. <https://posicharge.com/products/mvs400/>
- **Baseline confidence (MVS800):** Verified public—system level, with P0 topology conflict. **Still needed:** Resolve whether system supports 8 or 16 vehicles, why associated power-station text states 60 kW, and the valid topology/power-allocation rules.
- The MVS400 sheet (Downloads/MVS-400.pdf) says it is built on the DVS400 platform, supports up to three additional power stations and up to eight vehicles charging at once, with power sharing that prioritizes the lowest state of charge; table: powerserver 40 kW, 480/600 VAC 3-phase, 56/45 A draw, breaker 70/60 A, power factor 0.96, efficiency 90 percent, 915 lb, 60 x 32.4 x 21.9 in; powerstation 60 kW, 24 to 96 V, 250 A dual or 500 A single mode, 304 lb, 30 x 30 x 19 in, RS232. Source: PosiCharge MVS400 sheet (read round 20) (T1), retrieved 2026-10-03. <https://posicharge.com/wp-content/uploads/2026/01/MVS-400.pdf>
- The MVS800 sheet (Downloads/MVS-800.pdf) says one MVS800 charges up to 16 vehicles at once, CE compliant version available, NEMA 3R, installed at the world's largest airports; table: powerserver 80 kW, 480/600 VAC 3-phase, 100/80 A draw, breaker 125/100 A, power factor 0.96, efficiency 95 percent, 1,405 lb, 62 x 42 x 27 in; the powerstation table is identical to the MVS400's (60 kW, 24 to 96 V, 250/500 A, 304 lb). Source: PosiCharge MVS800 sheet (read round 20) (T1), retrieved 2026-10-03. <https://posicharge.com/wp-content/uploads/2026/01/MVS-800.pdf>
- The eGSE catalog says one utility connection can charge up to 16 vehicles and that there are over 3,000 charging locations at airports using MVS technology; it integrates the BMID into vehicle wiring harnesses with no extra interface box. Source: PosiCharge eGSE catalog (T1), retrieved 2026-10-03. <https://posicharge.com/wp-content/uploads/2026/06/eGSE-Catalog.pdf>
- **C78 and C79 updates (round 20):** see the register; the sheets give 16 vehicles for the MVS800 and 8 for the MVS400, and list the powerserver and the powerstation as separate components with separate ratings.

## Aliases

- MVS400
- MVS800

## Former ids
