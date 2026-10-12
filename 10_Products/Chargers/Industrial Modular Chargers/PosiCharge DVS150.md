---
type: Object
subtype: electrical
id: OBJ-00299
uid: 20261003143453033skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - posicharge-baseline
  - charger
subtypeOf:
  - "[[Industrial Modular Charger]]"
performs:
  - "[[Equalize Battery on Schedule]]"
  - "[[Compensate Charge for Battery Temperature]]"
  - "[[Log Battery Events and Usage]]"
hasDesign:
  - "[[Electrolyte-Immersed Temperature Sensor]]"
  - "[[Temperature-Compensated Charge Control Design]]"
  - "[[Direct Temperature Input Charge Compensation]]"
madeBy:
  - "[[PosiCharge]]"
hasPart:
  - "[[Temperature Compensation Charge Control Firmware]]"
---

# PosiCharge DVS150

## Definition

PosiCharge dual-port fast charger for 24 to 80 V material handling batteries.

## Notes

- Dual-port MHE fast charger for 24–80 V batteries. Public page lists 15 kW per port, 300 A per port, 480/600 VAC input, up to 92% efficiency, 0.98 power factor, NEMA 1 enclosure, 13 ft output cable, and 250 logged charge events. Listed controls/protections include BMID, real-time clock, equalization scheduling, electrolyte-immersed thermistor, thermal foldback/shutdown, and 5 ms shutdown response. Source: official PosiCharge page for DVS150, as summarized in the vault's Public Evidence Register (PUB-004, class P1/P2/P3 per that note) (T1), retrieved 2026-10-03. <https://posicharge.com/products/dvs150/>
- **Baseline confidence (DVS150):** Verified public—product level. **Still needed:** Current commercial model/ordering codes; chemistry and capacity envelope; output connector options; exact certifications; BMID/communications interfaces; relationship to DVS100.
- **Functions performed, with citations:**
  - [[Equalize Battery on Schedule]] (V): <https://posicharge.com/products/dvs150/>
  - [[Compensate Charge for Battery Temperature]] (V): <https://posicharge.com/products/dvs150/>
  - [[Log Battery Events and Usage]] (V): <https://posicharge.com/products/dvs150/>
- **Design characteristics, with citations:**
  - [[Electrolyte-Immersed Temperature Sensor]] (V): <https://posicharge.com/products/dvs150/>
- The public DVS150 page lists equalization scheduling, an electrolyte-immersed thermistor and thermal foldback or shutdown among its controls and protections. Source: PosiCharge DVS150 page (T1), retrieved 2026-10-03. <https://posicharge.com/products/dvs150/>

- **Architecture realization — temperature-compensated charging:** published behavior supports [[Temperature-Compensated Charge Control Design]] with [[Direct Temperature Input Charge Compensation]]. [[Temperature Compensation Charge Control Firmware]] is allocated at **>=95% engineering confidence** because the charger must apply temperature-dependent control while its internal software partition is unpublished. Compensation slope, thresholds, filtering, and fault fallback remain product-specific.

## Aliases

- DVS150

## Former ids
