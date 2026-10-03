---
type: Object
subtype: electrical
id: OBJ-00070
uid: 20261002191446813skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - charger
  - opportunity-charge
subtypeOf:
  - "[[Industrial Modular Charger]]"
performs:
  - "[[Charge Battery by Opportunity]]"
  - "[[Charge Lithium-Ion Battery]]"
  - "[[Identify Battery by Voltage]]"
  - "[[Charge Under BMS Control]]"
hasDesign:
  - "[[Multi-Voltage Output]]"
  - "[[Charger Status LED Bar]]"
madeBy:
  - "[[PosiCharge]]"
offeredWith:
  - "[[PosiCharge BMID]]"
  - "[[PosiCharge PosiLink]]"
---

# PosiCharge ProCore Edge

## Definition

PosiCharge opportunity charger with automatic modes for CAN/lithium, BMID and voltage-only operation.

## Notes

- PosiCharge says ProCore Edge covers 24 to 96 V, has CAN/Lithium, BMID and Voltage automatic modes, charges sealed, flooded and thin plate lead and lithium chemistries, communicates with wireless BMIDs over Bluetooth, and has an LED status bar and phone control. Source: PosiCharge ProCore Edge page (T1), retrieved 2026-10-02. <https://www.posicharge.com/procoreedge>
- **Functions performed, with citations** (V = verified this pass):
  - [[Charge Battery by Opportunity]] (V): <https://www.posicharge.com/procoreedge>
  - [[Charge Lithium-Ion Battery]] (V): <https://www.posicharge.com/procoreedge>
  - [[Identify Battery by Voltage]] (V): <https://www.posicharge.com/procoreedge>
  - [[Charge Under BMS Control]] (V): <https://www.posicharge.com/procoreedge>
- **Design characteristics, with citations:**
  - [[Multi-Voltage Output]] (V): <https://www.posicharge.com/procoreedge>
  - [[Charger Status LED Bar]] (V): <https://www.posicharge.com/procoreedge>
- **Public-evidence baseline (added from the vault's baseline note, round 19):**
- Opportunity charger platform for forklift batteries. Public pages list 24/36/48 V variants at 6–30 kW and 48/72/80/96 V variants at 9–30 kW; 96 V is listed for lithium-ion applications only. Public capabilities include automatic multi-chemistry charging, Bluetooth diagnostics, LED status, modular/scalable power, wall/pole/free-standing installation options, and PosiLink-connected fleet tools. Resource listings reference installation, service, spare-parts, anti-arc, BMID III-B dongle, PilotTerm software-loading, and iOS updater documentation. Source: official PosiCharge page for ProCore Edge, as summarized in the vault's Public Evidence Register (PUB-003, class P1/P2/P3 per that note) (T1), retrieved 2026-10-03. <https://posicharge.com/products/procore-edge/>
- **Baseline confidence (ProCore Edge):** Verified public—family level. **Still needed:** Current SKU/option master; certification and regional configuration matrix; chemistry/BMS/connector/BMID interoperability; active firmware and software versions; installation and service policy.
- The current ProCore Edge sheet (Downloads/ProCore-Edge-Spec-Sheet-Updated.pdf) lists 440/480 V and 600 V versions at 6 to 30 kW and a 380/400 V version at 6 to 15 kW; chemistries lead acid, Li-ion, Ni-MH and sodium-ion with automatic selection; Bluetooth app; LED stack light bar; three replaceable parts; a 5-year warranty; 24/36/48 V output tables (for example 6 kW at 128/128/104 A to 30 kW at 640/640/521 A) and 48/72/80/96 V tables (9 to 30 kW; 96 V lithium-ion only); the sheet calls it the only UL-approved charger that can be de-rated for smaller breakers and the only HF charger supporting 48 to 96 V in one module (vendor claims). Source: ProCore Edge spec sheet (read round 20) (T1), retrieved 2026-10-03. <https://posicharge.com/wp-content/uploads/2026/06/ProCore-Edge-Spec-Sheet-Updated.pdf>

## Aliases

- ProCore Edge


## Former ids
