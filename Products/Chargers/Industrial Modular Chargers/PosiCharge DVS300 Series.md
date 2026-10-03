---
type: Object
subtype: electrical
id: OBJ-00251
uid: 20261003094918670skellyspencer
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
  - "[[Compensate Charge for Battery Temperature]]"
madeBy:
  - "[[PosiCharge]]"
offeredWith:
  - "[[PosiCharge BMID]]"
---

# PosiCharge DVS300 Series

## Definition

PosiCharge outdoor GSE chargers (DVS300, DVS330, DVS400) for 24 to 96 V that charge one vehicle up to 500 A or two vehicles at 250 A each.

## Notes

- PosiCharge's DVS sheet says DVS300 is the stand-alone industrial charger, DVS covers 24 to 96 V across the 300, 330 and 400 models, controls battery temperature during charging, works with BMID, Battery Rx and PosiNet, and lets operators charge the same number of vehicles with a third of the power of conventional chargers. Source: PosiCharge DVS 300/330/400 sheet (T1), retrieved 2026-10-03. <https://og.mhi.org/media/members/16696/131261342052642309.pdf>
- Airport Technology says one vehicle can be charged with up to 500 A or two vehicles simultaneously at 250 A. Source: Airport Technology (T2), retrieved 2026-10-03. <https://www.airport-technology.com/contractors/groundequipment/posicharge/>
- **Functions performed, with citations:**
  - [[Charge Battery Fast]] (V): <https://og.mhi.org/media/members/16696/131261342052642309.pdf>
  - [[Compensate Charge for Battery Temperature]] (V): <https://og.mhi.org/media/members/16696/131261342052642309.pdf>
- **Public-evidence baseline (added from the vault's baseline note, round 19):**
- Outdoor fast-charge family for airport GSE. Official page lists 30/33/40 kW variants, 24–96 V battery range, 250 A dual-vehicle output or up to 500 A single-vehicle output, 480/600 VAC three-phase input, 0.96 power factor, 90% efficiency, NEMA 3R enclosure, BMID recognition, anti-arcing disconnect, thermal protection/shutdown, jet-bridge/other-device power sharing, and RS-232. Resource content includes a China GBT interface-board manual. Source: official PosiCharge page for DVS300/330/400, as summarized in the vault's Public Evidence Register (PUB-007, class P1/P2/P3 per that note) (T1), retrieved 2026-10-03. <https://posicharge.com/products/dvs300-330-400/>
- **Baseline confidence (DVS300/330/400):** Verified public—family level. **Still needed:** Resolve 300/330/400 configuration mapping; confirm current/output limits, power-sharing conditions, GBT board scope, eGSE/OEM compatibility, connectors, certifications, current BMID generation/protocol, and geographic availability.
- The current DVS sheet (Downloads/DVS-300-400.pdf) says DVS300 and DVS400 are stand-alone chargers for one vehicle up to 500 A or two at 250 A each, with an integrated AC-to-DC power server, CAN for lithium batteries, BMID support, up to 3 times the equipment throughput of conventional chargers, NEMA 3R, Euro and Burton connectors; table: DVS300 30 kW, 480/600 VAC 3-phase, 40/32 A draw, breaker 50/40 A, power factor 0.96, efficiency 90 percent, 24 to 96 V, 250 A dual or 500 A single mode, 905 lb, 60 x 32.4 x 21.9 in, RS232; DVS400 40 kW, same draw as DVS300 (40/32 A, see C80), breaker 70/60 A, 915 lb. Source: PosiCharge DVS 300/400 sheet (read round 20) (T1), retrieved 2026-10-03. <https://posicharge.com/wp-content/uploads/2026/01/DVS-300-400.pdf>
- The same sheet file has pages for a DVS330 and a DVS330 IP55 (stand-alone, same 500 A or 2 x 250 A, GBT CAN add-on kit, Euro or Burton connectors); the eGSE catalog also lists a DVS330 II and an MVS330 (names only in the retrieved text). Source: PosiCharge DVS sheet and eGSE catalog (T1), retrieved 2026-10-03. <https://posicharge.com/wp-content/uploads/2026/06/eGSE-Catalog.pdf>

## Aliases

- DVS300
- DVS330
- DVS400

## Former ids
