---
type: Object
subtype: electrical
id: OBJ-00120
uid: 20261002193402976skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - battery
  - gse
abstract: true
productClass: product-family
reuseScope: product-family
subtypeOf:
  - "[[Lithium-Ion Traction Battery]]"
supertypeOf:
  - "[[Flux Power GSE2]]"
  - "[[Flux Power GSE3]]"
  - "[[Flux Power GSE4]]"
  - "[[Flux Power GSE6]]"
describedBy:
  - "[[Document - Flux Power GSE Battery Pack V.2 Brochure (2021)]]"
  - "[[Document - Flux Power GSE3 Product Brochure (SA-808, 2023-12-18)]]"
performs:
  - "[[Sense Battery State]]"
hasDesign:
  - "[[Integrated Battery Management System]]"
  - "[[CAN Interface]]"
  - "[[Integrated Battery Heater]]"
madeBy:
  - "[[Flux Power]]"
offeredWith:
  - "[[Flux SkyBMS]]"
---

# Flux Power GSE Pack

## Definition

Flux lithium pack family for airport ground support equipment: 72 V, 300 to 600 Ah in the 2016 report; 80 V (76.8 V) GSE2, GSE3, GSE4 and GSE6 in the 2021 brochure; GSE3 in 2023 (C212).

## Notes

- A fiscal 2016 report says Flux designed a 72 V lithium pack for GSE with modular capability from 300 to 600 Ah. Source: EE Power (T2 (dated)), retrieved 2026-10-02. <https://eepower.com/news/flux-power-reports-operational-and-financial-results/>

- **2021 brochure (Document - Flux Power GSE Battery Pack V.2 Brochure (2021)):** family GSE2, GSE3, GSE4, GSE6; 80 V (76.8 V) nominal, up to 400 V on request; 210 to 630 Ah; 16.8 to 50.4 kWh; weights 535 to 1,753 lb; max continuous charge current 200 to 350 A; charge 0 to 55 C, discharge -20 to 55 C; BMS 2.0 with cell monitoring; isolated external CANbus. Source: Flux Power GSE pack brochure (T1, read through a summarizing tool), retrieved 2026-10-13. <https://www.fluxpower.com/hubfs/GSE%20Battery%20Pack%20V.2%20-%20Brochure.pdf>
- **2023 GSE3 sheet (Document - Flux Power GSE3 Product Brochure (SA-808, 2023-12-18)):** 80 V (76.8 V), 315 Ah, 24.2 kWh, LiFePO4, 150 A max continuous charge current, -30 to 45 C, IP56, integral BMS, SkyBMS Telematics, optional heaters, 3,500 cycles at 80 percent depth of discharge (maker claim). Source: Flux Power GSE3 brochure (T1, read through a summarizing tool), retrieved 2026-10-13. <https://www.fluxpower.com/hubfs/GSE3%20Product%20Brochure.pdf>
- **Conflicts kept visible:** the 2016 report (72 V, 300 to 600 Ah) disagrees with both brochures (C212); the two brochures disagree on the GSE3's energy (25.2 against 24.2 kWh), charge current (300 against 150 A) and temperature range (C213). The older values stay in the note and in the metric notes. Which source is current is not established (IB-165).
- **Family and variants (owner decision 2026-10-13, U):** this note is the family; the models are variant notes under it: [[Flux Power GSE2]], [[Flux Power GSE3]], [[Flux Power GSE4]], [[Flux Power GSE6]]. Shared functions, designs and the SkyBMS link stay here; model dimensions, weights and charge current sit on the variants (IB-167 decided).
- **Functions performed, with citations:**
  - [[Sense Battery State]] (V, partial): individual cell monitoring in BMS 2.0. <https://www.fluxpower.com/hubfs/GSE%20Battery%20Pack%20V.2%20-%20Brochure.pdf>
- **Design characteristics, with citations:**
  - [[Integrated Battery Management System]] (V): BMS 2.0 (2021) and integral BMS (2023). <https://www.fluxpower.com/hubfs/GSE%20Battery%20Pack%20V.2%20-%20Brochure.pdf>; <https://www.fluxpower.com/hubfs/GSE3%20Product%20Brochure.pdf>
  - [[CAN Interface]] (V, partial): isolated external CANbus for GSE integration (2021 brochure only; the 2023 sheet lists no protocol). <https://www.fluxpower.com/hubfs/GSE%20Battery%20Pack%20V.2%20-%20Brochure.pdf>
  - [[Integrated Battery Heater]] (V, partial): integrated heaters are an option on the GSE3 (2023 sheet only). <https://www.fluxpower.com/hubfs/GSE3%20Product%20Brochure.pdf>
- **Offered with:** [[Flux SkyBMS]] (V, partial): the 2023 sheet lists "SkyBMS Telematics" for the GSE3. <https://www.fluxpower.com/hubfs/GSE3%20Product%20Brochure.pdf>
- **Not linked, and why:** [[Communicate Battery State over CAN]] (the brochure names a CANbus for integration but not battery-state messages); [[Log Battery Events and Usage]] and [[Transmit Battery Data Wirelessly]] (performed by SkyBMS, not stated for the pack itself); [[Protect Battery from Harm]] (sleep mode and automatic shutoffs are named, but no protection limit is stated).

## Aliases

- GSE Pack


## Former ids
