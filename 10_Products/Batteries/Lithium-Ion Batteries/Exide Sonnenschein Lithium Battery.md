---
type: Object
subtype: electrical
id: OBJ-00094
uid: 20261002193402950skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - battery
subtypeOf:
  - "[[Lithium-Ion Traction Battery]]"
describedBy:
  - "[[Document - Exide Sonnenschein Lithium Brochure]]"
  - "[[Document - Exide Sonnenschein Lithium Battery and GNB Fleet Sheet (MXSLITEPDF00820)]]"
performs:
  - "[[Balance Cells]]"
  - "[[Estimate State of Charge]]"
  - "[[Protect Battery from Deep Discharge]]"
  - "[[Sense Battery State]]"
  - "[[Charge Battery Fast]]"
  - "[[Charge Battery by Opportunity]]"
  - "[[Communicate with Charger]]"
hasDesign:
  - "[[Integrated Battery Management System]]"
madeBy:
  - "[[Exide Technologies]]"
offeredWith:
  - "[[Exide GNB Fleet]]"
  - "[[Exide Retrofitting Communicator]]"
  - "[[Exide Opus Display]]"
  - "[[Exide HC-LC Logger]]"
---

# Exide Sonnenschein Lithium Battery

## Definition

Exide Sonnenschein-branded lithium battery for material handling.

## Notes

- Exide's overview lists Sonnenschein Lithium material handling batteries for most motive power applications with an integrated monitoring system and GNB Fleet. Source: GNB motive power overview (T1), retrieved 2026-10-02. <https://www.exidegroup.com/eu/sites/default/files/2021-08/GNB_MP_Overview_EN_web.pdf>

- **Official sources found 2026-10-13 (read through a summarizing tool, IB-175):** [[Document - Exide Sonnenschein Lithium Brochure]] <https://exidegroup.com/en/document/sonnenschein-lithium-brochure>; [[Document - Exide Sonnenschein Lithium Battery and GNB Fleet Sheet (MXSLITEPDF00820)]] <https://exidegroup.com/es/sites/default/files/2020-11/GNB_MP_Sonnenschein_Lithium_MHB_GNB_Fleet_EN.pdf> (page <https://exidegroup.com/en/document/sonnenschein-lithium-material-handling-battery-product-sheet>).
- **Classes (nominal V; capacity; energy):** 24 V class 25.6 V, 80 to 440 Ah, 2.0 to 11.3 kWh; 36 V class 38.4 V, 80 to 440 Ah, 3.1 to 16.9 kWh; 48 V class 51.2 V, 110 to 552 Ah, 5.6 to 28.3 kWh; 80 V class 76.8 V, 110 to 966 Ah, 8.4 to 74.2 kWh. Voltage x capacity matches the energy in every class (checked). The nominal voltages are multiples of 3.2 V, which is typical of iron phosphate cells; that is an analyst inference, since Exide states only "lithium-ion". Source: Exide Sonnenschein Lithium brochure (T1), retrieved 2026-10-13. <https://exidegroup.com/en/document/sonnenschein-lithium-brochure>
- **Discharge and charge:** 80 V 966 Ah model 1,960 A constant and 2,940 A peak discharge; 110 Ah model 220 A and 420 A. Ah charge efficiency over 98 percent (basis not stated); fast and opportunity charging claimed with no times; the truck sheet shows a "2100HP" charger with full recharge in up to one hour (naming unexplained, IB-175). <https://exidegroup.com/en/document/sonnenschein-lithium-brochure>; <https://exidegroup.com/es/sites/default/files/2020-11/GNB_MP_Sonnenschein_Lithium_MHB_GNB_Fleet_EN.pdf>
- **Not stated:** cycle life count, warranty, CAN, chemistry subtype, product certifications (only plant ISO certificates), weights.
- **Functions performed, with citations:**
  - [[Balance Cells]] (V): controlled cell balancing, method not stated. <https://exidegroup.com/en/document/sonnenschein-lithium-brochure>
  - [[Estimate State of Charge]] (V): state-of-charge calculation in the BMS. <https://exidegroup.com/en/document/sonnenschein-lithium-brochure>
  - [[Protect Battery from Deep Discharge]] (V): deep discharge protection. <https://exidegroup.com/es/sites/default/files/2020-11/GNB_MP_Sonnenschein_Lithium_MHB_GNB_Fleet_EN.pdf>
  - [[Sense Battery State]] (V): BMS monitors voltage, current and temperature. <https://exidegroup.com/en/document/sonnenschein-lithium-brochure>
  - [[Charge Battery Fast]] (V, claim): "ultra-fast" charging, no times. <https://exidegroup.com/en/document/sonnenschein-lithium-brochure>
  - [[Charge Battery by Opportunity]] (V): fast charge and opportunity charge. <https://exidegroup.com/en/document/sonnenschein-lithium-brochure>
  - [[Communicate with Charger]] (V): the BMS controls the GNB Lithium Charger; communication flow includes the High Output Charger. <https://exidegroup.com/en/document/sonnenschein-lithium-brochure>
- **Design characteristics, with citations:**
  - [[Integrated Battery Management System]] (V): BMS with internal communication bus between modules, thermal management if required, optional vehicle integration. <https://exidegroup.com/en/document/sonnenschein-lithium-brochure>
- **Offered with:** [[Exide GNB Fleet]], [[Exide Retrofitting Communicator]], [[Exide Opus Display]], [[Exide HC-LC Logger]] (all V, one brochure each, IB-176).
- **Not linked, and why:** [[Active Cell Balancing]] and [[Passive Cell Balancing]] (method not stated); [[Communicate Battery State over CAN]] (CAN not mentioned); a named GNB Lithium Charger and the 2100HP charger (no note yet; the organization note lists "GNB 2100" and naming is unconfirmed, IB-175).

## Aliases

- Sonnenschein Lithium


## Former ids
