---
type: Object
subtype: electrical
id: OBJ-00250
uid: 20261003094918669skellyspencer
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
hasDesign:
  - "[[Temperature-Compensated Charge Control Design]]"
  - "[[Communicated Battery Temperature Charge Compensation]]"
hasPart:
  - "[[Temperature Compensation Charge Control Firmware]]"
  - "[[PosiCharge BMID]]"
---

# PosiCharge SVS100

## Definition

PosiCharge compact outdoor GSE fast and opportunity charger for 24 to 80 V electric GSE not under extremely heavy use.

## Notes

- PosiCharge's SVS100 sheet says it is a compact charger for electric airport GSE needing fast or opportunity charging, for FBO operators and non-hub airports, ideal for electric belt loaders and baggage tractors not under extremely heavy use, covering 24 to 80 V, using battery voltage and temperature sensors to control charging, with BMID, Battery Rx and PosiNet and CEC certification. Source: PosiCharge SVS100 sheet (T1), retrieved 2026-10-03. <https://og.mhi.org/media/members/16696/131261341460139117.pdf>
- Airport Technology says the SVS100 is a compact charger for light-duty fast-charging in small cargo warehouses, GA and FBO airports and regional jet operations. Source: Airport Technology (T2), retrieved 2026-10-03. <https://www.airport-technology.com/contractors/groundequipment/posicharge/>
- **Functions performed, with citations:**
  - [[Charge Battery Fast]] (V): <https://og.mhi.org/media/members/16696/131261341460139117.pdf>
  - [[Compensate Charge for Battery Temperature]] (V): <https://og.mhi.org/media/members/16696/131261341460139117.pdf>
- **Public-evidence baseline (added from the vault's baseline note, round 19):**
- Single-port outdoor GSE charger. Public content lists 24–80 V batteries, BMID recognition of voltage/state of charge/temperature, automatic start/stop, anti-arcing disconnect, thermal shutdown, high-frequency IGBT conversion, NEMA 3R enclosure, and Euro/Burton connector/cable options. Source: official PosiCharge page for SVS100, as summarized in the vault's Public Evidence Register (PUB-006, class P1/P2/P3 per that note) (T1), retrieved 2026-10-03. <https://posicharge.com/products/svs100/>
- **Baseline confidence (SVS100):** Verified public, with P0 rating conflict. **Still needed:** Resolve whether rated power is 10 kW, 40 kW, or configuration-dependent; obtain current controlled spec sheet, part-number structure, approved eGSE applications, certifications, and accessory/interface list.
- The current SVS100 sheet (in repo as Downloads/SVS-100.pdf) says it delivers up to 10 kW single-port for small electric belt loaders, carts and people movers; table: 10 kW, 480 or 600 VAC 3-phase, full-load draw 15 or 12 A, breaker 20 or 15 A, power factor 0.98, efficiency 91 percent, battery 24 to 80 V, maximum output 250 A, 388 lb, 39.4 x 22 x 19.3 in; works with all PosiCharge BMIDs, automatic start and stop, anti-arcing disconnect, auto-thermal shutdown, Euro and Burton output connectors; the footer says PosiCharge is a product line of Ampure. Source: PosiCharge SVS100 sheet (read round 20) (T1), retrieved 2026-10-03. <https://posicharge.com/wp-content/uploads/2026/01/SVS-100.pdf>
- **C77 update (round 20):** the sheet states 10 kW in both its text and its table; the 40 kW table on the PosiCharge web page was not rechecked.

- **Architecture realization — temperature-compensated charging:** published behavior supports [[Temperature-Compensated Charge Control Design]] with [[Communicated Battery Temperature Charge Compensation]]. [[Temperature Compensation Charge Control Firmware]] is allocated at **>=95% engineering confidence** because the charger must apply temperature-dependent control while its internal software partition is unpublished. Compensation slope, thresholds, filtering, and fault fallback remain product-specific.

## Aliases

- SVS100

## Former ids
