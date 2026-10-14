---
type: Info
subtype:
id: INFO-90047
uid: 20261014010000001skellyspencer
status: Draft
tags:
  - research
  - bms
  - external-product
  - design-options
describes:
  - "[[Battery Management System]]"
  - "[[Battery Management System Design]]"
  - "[[Standalone Battery Management System]]"
  - "[[Master and Cell Monitor BMS Topology]]"
  - "[[Passive Cell Balancing]]"
  - "[[Active Cell Balancing]]"
  - "[[BMS Maker]]"
  - "[[Calculate Charge and Discharge Current Limits]]"
  - "[[Detect Isolation Fault]]"
describedBy:
  - "[[Document - REC BMS Product Page (retrieved 2026-10-13)]]"
  - "[[Document - Batrium BMS Product Guide (undated)]]"
  - "[[Document - Orion BMS 2 Product Page (retrieved 2026-10-13)]]"
  - "[[Document - Nuvation Energy UL 1973 Recognized BMS Page (retrieved 2026-10-13)]]"
  - "[[Document - Orion BMS 2 Specifications (Ewert Energy Systems)]]"
  - "[[Document - Flux Power SkyBMS Brochure (2023)]]"
---

# External BMS Product Landscape

## Definition

Battery management systems made by others, compared by the functions and designs their makers state. PosiCharge has no BMS (owner decision 2026-10-13), so these products serve two purposes: they define what a BMS does and how it can be built ([[BMS Function Definitions]]), and they are the counterpart that PosiCharge chargers and the BMID meet at the CAN interface ([[Interface and Protocol Layer Reference]]).

## Notes

### Scope and limits

- **Coverage:** five standalone BMS makers or product lines with a note each (Orion BMS 2, REC 2Q and Active, Batrium, Nuvation G5) and Flux SkyBMS, which is integrated. The integrated BMS of forklift battery makers stay in their battery notes (see [[Integrated Battery Management System]]) because their sources do not describe the BMS as a product.
- **Not covered yet:** Elithion Lithiumate (page could not be fetched), Daly, ROYPOW, Flux's other BMS, Nuvation's cell interface products, and any BMS whose maker publishes only through a dealer.
- **Fit to forklifts is unevidenced.** None of the standalone pages read mentions forklifts, UL 2580 or industrial trucks. Nuvation's context is stationary storage. These products show BMS functions and designs; they are not evidence of what forklift battery makers use inside their packs.
- Pages were read through a summarising fetch; 'not stated' means the summary found nothing on that page.

### Products compared

| Product | Maker | Cells | Balancing | States and limits | Outputs and links | Safety or approvals stated | Sources |
|---|---|---|---|---|---|---|---|
| [[Orion BMS 2]] | [[Ewert Energy Systems]] | up to 180 in series (24 to 180 in 12-cell steps) | passive; 200 mA (sheet) | SOC, charge and discharge current limits; cell voltage 0.5 to 5 V at 0.1 mV (sheet) | two CAN 2.0B; OBD2; J1772 and CHAdeMO hardware; drives certain contactors; isolation fault detection (sheet) | ISO 7637 and EN 50498 listed (sheet); no certification on the page | [[Document - Orion BMS 2 Product Page (retrieved 2026-10-13)]], [[Document - Orion BMS 2 Specifications (Ewert Energy Systems)]] |
| [[REC 2Q BMS]] | [[REC (BMS maker)]] | 4 to 16; master-slave up to 240 | not stated | not stated | integrated CAN; programmable relays and digital outputs in master-slave | not stated | [[Document - REC BMS Product Page (retrieved 2026-10-13)]] |
| [[REC Active BMS]] | [[REC (BMS maker)]] | 4, 12 V systems | active, bi-directional | not stated | not stated | not stated | [[Document - REC BMS Product Page (retrieved 2026-10-13)]] |
| [[Batrium WatchMonCORE]] | [[Batrium]] | 1 to 250 through cell monitors | by cell monitors; 28 Ah per day per cell | 4-stage SOC display | configurable relay 30 VDC 5 A; USB; CAN, Modbus, RS485 not mentioned | not stated | [[Document - Batrium BMS Product Guide (undated)]] |
| [[Batrium CellMate-K9]] | [[Batrium]] | 3s to 16s | optional fan and 25 W heatsink | cell voltage 0.5 to 5.5 V at 1 mV | daisy chain | not stated | [[Document - Batrium BMS Product Guide (undated)]] |
| [[Batrium ShuntMon2]] | [[Batrium]] | not applicable | not applicable | voltage, current, temperature, SOC from Ah counting; plus or minus 1.0% current | isolated serial | not stated | [[Document - Batrium BMS Product Guide (undated)]] |
| [[Nuvation Energy G5 BMS]] | [[Nuvation Energy]] | not stated | not stated | not stated | not stated | UL 1973 Recognized, CE conformant (maker claims) | [[Document - Nuvation Energy UL 1973 Recognized BMS Page (retrieved 2026-10-13)]] |
| [[Flux SkyBMS]] | [[Flux Power]] | not stated | not stated | not stated | Wi-Fi, cellular, Bluetooth; local debug data | not stated | [[Document - Flux Power SkyBMS Brochure (2023)]] |

### Which functions the products state

| Vault Function | Products stating it |
|---|---|
| [[Measure Battery Voltage]] | Orion BMS 2, Batrium CellMate-K9, Batrium ShuntMon2 |
| [[Measure Battery Current]], [[Measure Battery Temperature]], [[Accumulate Amp-Hours]] | Batrium ShuntMon2 |
| [[Balance Cells]] | Orion BMS 2 (passive), REC Active BMS (active), Batrium CellMate-K9 |
| [[Estimate State of Charge]] | Orion BMS 2, Batrium ShuntMon2 |
| [[Calculate Charge and Discharge Current Limits]] | Orion BMS 2 only |
| [[Detect Isolation Fault]] | Orion BMS 2 only |
| [[Disconnect Battery on Limit Violation]] | Orion BMS 2 (contactor drive), Batrium WatchMonCORE (relay and logic) |
| [[Communicate Battery State over CAN]] | Orion BMS 2; REC 2Q BMS states CAN but not the content, so it is not linked |
| [[Log Battery Events and Usage]], [[Transmit Battery Data Wirelessly]], [[Alert on Abnormal Condition]] | Flux SkyBMS |

No product states state of health, a named thermal control function, authentication or sleep and self-test. The Orion pages give 'pack health' without a method.

### Design choices a BMS owner has to make

Each row is a decision with the options the products show and what the sources leave open. It is a checklist for defining a BMS, not a recommendation.

| Decision | Options seen | Evidence | Left open by the sources |
|---|---|---|---|
| Packaging | Built into the pack ([[Integrated Battery Management System]]) or sold separately ([[Standalone Battery Management System]]) | Forklift battery makers integrate; the products above are standalone | Which is better for a charger-facing interface: no source compares |
| Topology | One unit, or master with cell monitors ([[Master and Cell Monitor BMS Topology]]) | REC master-slave; Batrium supervisor and monitors | The link between units; scaling limits beyond the makers' cell counts |
| Balancing | [[Passive Cell Balancing]] or [[Active Cell Balancing]] | Orion passive at 200 mA; REC Active; Batrium bypass up to 2 A | Balancing current for REC; any comparison of heat, cost or balance time |
| State estimation | Ah counting at a shunt (Batrium ShuntMon2) or a calculated SOC with unstated method (Orion) | See [[SOC and SOH Knowledge Base]] | Accuracy, drift handling, SOH |
| Limits to the charger | Compute and publish charge and discharge current limits (Orion), or drive a charger by an output or pilot lines (Orion J1772, CHAdeMO) | Orion product page | The CAN message set; CiA 418 or J1939 mapping (C204, C206) |
| Power path | Contactors driven by the BMS (Orion), relay for an external breaker (Batrium) | Product pages | Precharge, welded contactor detection, fail-safe state |
| Isolation | Isolation fault detection circuit (Orion) | Orion sheet | Threshold; the UL 2580 clause |
| Functional safety | ISO 26262 (EnerSys claim), UL 60730 (ROYPOW claim) | [[BMS Product Function and Requirement Driver Map]] | Whether any is required for a forklift (C201) |

### Gaps

- No standalone BMS datasheet was read in full except the Orion BMS 2 sheet recorded earlier; the REC, Batrium and Nuvation pages are overview material.
- No BMS home-page balancing or protection thresholds were found for REC.
- The Orion BMS 2 page read first was the Original model by mistake (identical wording in the summary: 180 cells, passive balancing); see C206.
- Standards are unread (UL 2580, IEC 62619, CiA 418 and 419).
- Conflicts: C206 to C208 in [[Battery Product Landscape Conflicts and Open Questions]].

## Sources

- [[Document - Orion BMS 2 Product Page (retrieved 2026-10-13)]] <https://www.orionbms.com/products/orion-bms-standard/>
- [[Document - Orion BMS 2 Specifications (Ewert Energy Systems)]] <https://www.orionbms.com/downloads/documents/orionbms2_specifications.pdf>
- [[Document - REC BMS Product Page (retrieved 2026-10-13)]] <https://www.rec-bms.com/>
- [[Document - Batrium BMS Product Guide (undated)]] <https://wiki.batrium.com/documents/batrium_bms_product_guide.pdf>
- [[Document - Nuvation Energy UL 1973 Recognized BMS Page (retrieved 2026-10-13)]] <https://www.nuvation.com/battery-management-systems/ul-1973-recognized/>
- [[Document - Flux Power SkyBMS Brochure (2023)]]

## Aliases

- external BMS
- standalone BMS
- BMS products
- BMS design options
- Orion REC Batrium Nuvation

## Former ids
