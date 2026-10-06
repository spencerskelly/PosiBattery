---
type: Object
subtype: electrical
id: OBJ-00068
uid: 20261002191446811skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - charger
  - fast-charge
subtypeOf:
  - "[[Industrial Modular Charger]]"
performs:
  - "[[Equalize Battery on Schedule]]"
  - "[[Charge Battery Fast]]"
  - "[[Compensate Charge for Battery Temperature]]"
madeBy:
  - "[[PosiCharge]]"
offeredWith:
hasDesign:
  - "[[Temperature-Compensated Charge Control Design]]"
  - "[[Communicated Battery Temperature Charge Compensation]]"
hasPart:
  - "[[Temperature Compensation Charge Control Firmware]]"
  - "[[PosiCharge BMID]]"
---

# PosiCharge DVS100

## Definition

PosiCharge dual-port fast charger with BMID, electrolytic thermistor and a dynamic equalization scheduler.

## Notes

- PosiCharge lists the DVS100 as a dual-port charger for 24 to 80 V, 320 A and 20 kW (200 A and 10 kW per port), with charger and battery data management, the Battery Monitor and Identifier Module, an electrolytic thermistor, an easy-service modular cable system and a dynamic equalization scheduler. Source: PosiCharge DVS100 page (T1), retrieved 2026-10-02. <https://www.posicharge.com/dvs100/>
- **Functions performed, with citations** (V = verified this pass):
  - [[Equalize Battery on Schedule]] (V): <https://www.posicharge.com/dvs100/>
  - [[Charge Battery Fast]] (V): <https://www.posicharge.com/dvs100/>
  - [[Compensate Charge for Battery Temperature]] (V): <https://www.posicharge.com/faq/>
- **Public-evidence baseline (added from the vault's baseline note, round 19):**
- A public installation-manual search result describes 2 × 10 kW, 16–120 V DC output, 200 A maximum output, and 480/600 VAC variants. Source: official PosiCharge page for DVS100, as summarized in the vault's Public Evidence Register (PUB-005, class P1/P2/P3 per that note) (T1), retrieved 2026-10-03. <https://posicharge.com/product-resources/>
- **Baseline confidence (DVS100):** Publicly indicated only. **Still needed:** Confirm current product existence with current official page/spec sheet; establish SKU, ratings, certifications, and relationship to DVS150 before relying on these specifications.

- **Architecture realization — temperature-compensated charging:** published behavior supports [[Temperature-Compensated Charge Control Design]] with [[Communicated Battery Temperature Charge Compensation]]. [[Temperature Compensation Charge Control Firmware]] is allocated at **>=95% engineering confidence** because the charger must apply temperature-dependent control while its internal software partition is unpublished. Compensation slope, thresholds, filtering, and fault fallback remain product-specific.

## Aliases

- DVS100


## Former ids
