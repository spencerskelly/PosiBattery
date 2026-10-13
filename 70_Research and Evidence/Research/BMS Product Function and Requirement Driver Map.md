---
type: Info
subtype:
id: INFO-90037
uid: 20261013231000001skellyspencer
status: Draft
tags:
  - research
  - bms
  - requirements-drivers
  - evidence
describes:
  - "[[Battery Management System]]"
  - "[[Integrated Battery Management System]]"
describedBy:
  - "[[Document - EnerSys UL Listing Release for NexSys iON (2022-03-08)]]"
  - "[[Document - ROYPOW UL 2580 Certification Release (2025-04-14)]]"
  - "[[Document - OEM Off-Highway Inside Battery Certification Standards UL vs SGS vs TUV (ENEROC USA)]]"
  - "[[Document - EnerSys NexSys iON Operating Manual (Spanish, GLOB-ES-OM-NEX-ION 0323)]]"
  - "[[Document - MH&L Lithium Batteries for Material Handling (Green Cubes, 2024-04-23)]]"
  - "[[Document - Orion BMS 2 Specifications (Ewert Energy Systems)]]"
  - "[[Document - ATEC IEC 62619 Compliance Standards Page (retrieved 2026-10-13)]]"
  - "[[Document - Flux Power SkyBMS Brochure (2023)]]"
  - "[[Document - UL What Is UL 2580 Understanding EV Battery Safety Requirements (retrieved 2026-10-13)]]"
---

# BMS Product Function and Requirement Driver Map

## Definition

What battery management systems (BMS) on the market do, which of those functions each product states, and what drives them: standards, charger and truck interfaces, and customer needs already in the vault. It extends the category note [[Battery Management System]] and the metric [[Metric - BMS and Communication]].

## Notes

### Scope and limits

- **Products covered:** lithium-ion traction batteries with an integrated BMS (vault products and sources B2, B5, B6, B8), one standalone BMS family (Orion BMS 2, B3) and one fleet telemetry platform that carries 'BMS' in its name (Flux SkyBMS, B1). Orion BMS 2 and Flux SkyBMS have no product note yet.
- **Requirements:** none is written for the BMS. The standards that drive it were not read in full (UL 2580 and IEC 62619 are paid; the IEC preview could not be fetched), and the vault has no PosiCharge BMS product that a requirement would apply to. The drivers below are candidates, not Requirements. See the question at the end.
- Pages were read through a summarising fetch. Wording not stated in a source is marked 'not stated'.

### Functions the sources state, by product

| Id | BMS function | What the sources say | Products stating it | Sources |
|---|---|---|---|---|
| BF1 | Measure cell and pack voltage, current, temperature | NexSys iON power modules carry sensors for cell temperature and voltage; Orion BMS 2 measures cell voltage from 0.5 V to 5 V at 0.1 mV resolution; Green Cubes says individual cell monitoring | [[EnerSys NexSys iON Battery]], [[Green Cubes SAFEFlex Battery]]; Orion BMS 2 (no note) | B2, B3, B8 |
| BF2 | Enforce limits and disconnect | NexSys iON: a safe-disconnect system acts when voltage, current or temperature limits are exceeded, the BMS controls the main contactors, and current limits depend on temperature; Orion: enforces minimum and maximum cell voltage, maximum current and temperature limits | [[EnerSys NexSys iON Battery]]; Orion BMS 2 (no note); [[Hyster Power Cellect]] opens the charge contactor on an unsafe cell (vault metric note) | B2, B3 |
| BF3 | Balance cells | NexSys iON balances cells during use, thresholds not stated; Orion: 200 mA passive balancing; the vault records internal balancing for Green Cubes SAFEFlex | [[EnerSys NexSys iON Battery]], [[Green Cubes SAFEFlex Battery]]; Orion BMS 2 (no note) | B2, B3 |
| BF4 | Control charging with the charger | NexSys iON: charge starts once CAN communication with the charger is established, the optimal current depends on state of charge and temperature, charging stops on a fault and the charger wakes a switched-off battery; Orion: one digital output controls a charger and two enable charge and discharge | [[EnerSys NexSys iON Battery]], [[Stryten M-Series Li610 Battery]]; Orion BMS 2 (no note); charger side: [[Charge Under BMS Control]] | B2, B3 |
| BF5 | Communicate with the truck | NexSys iON's display interface supports CANopen and BMS CAN protocols and a wireless app; Orion: two CAN 2.0B interfaces, 125 to 1000 kbps, and cited CANopen and J1939 compatibility | [[EnerSys NexSys iON Battery]], [[Flux Power LiFT Pack]]; Orion BMS 2 (no note) | B2, B3 |
| BF6 | Estimate and show state of charge | NexSys iON: orange and red LED and buzzer warnings and an LED bar at set levels; Orion: calculates state of charge and 'pack health' (method not stated) | [[EnerSys NexSys iON Battery]], [[Stryten M-Series Li610 Battery]]; Orion BMS 2 (no note). Method choice: [[SOC and SOH Knowledge Base]] | B2, B3 |
| BF7 | Lock out and report faults | NexSys iON: lockout after deep discharge until a technician restores it, error codes with actions, and a lockout shown as error 401 | [[EnerSys NexSys iON Battery]] | B2 |
| BF8 | Sleep and self-test | NexSys iON deactivates when current stays below 1 A for 4 h (under 25 kWh), 24 h (25 to 53 kWh) or 48 h (over 53 kWh) and needs charging or a manual cycle after three days continuously active so safety functions can self-test | [[EnerSys NexSys iON Battery]] | B2 |
| BF9 | Log data and report remotely | Flux SkyBMS: one month of debug data kept locally, Wi-Fi, cellular and Bluetooth, remote diagnosis and custom alerts; Green Cubes: distributed BMS intelligence, data logging and Wi-Fi | [[Green Cubes SAFEFlex Battery]]; Flux SkyBMS (no note) | B1, B8 |
| BF10 | Detect isolation faults | Orion BMS 2 has an isolation fault detection circuit | Orion BMS 2 (no note) | B3 |
| BF11 | Operate within a temperature range | NexSys iON charging range 0 to 55 C; the vault records 0 to 45 C charge and heaters for Flux LiFT Pack | [[EnerSys NexSys iON Battery]], [[Flux Power LiFT Pack]] | B2 |

Detail not stated in any source read: cell-level cutoff values, balancing thresholds, the state-of-charge method, and the CAN message set for any product.

### What drives these functions

| Id | Driver | Kind | What the sources say | What is missing |
|---|---|---|---|---|
| RD1 | UL 2580, batteries for electric vehicles | Standard (product safety) | UL lists ride-on forklifts and ground support equipment in scope; tests are electrical (overcharge, short circuit, isolation resistance), mechanical, environmental and thermal runaway; 'Functional safety and BMS considerations are included within the overall evaluation approach' (B4). EnerSys NexSys iON and ROYPOW report listings (B5, B6). | Clause text; which BMS behaviours are required. See C201. |
| RD2 | IEC 62619, industrial lithium cells and batteries | Standard (product safety) | A test-lab page says it covers industrial applications including forklifts but not road vehicles, and that newer revisions have stricter BMS integration requirements (B9). | The standard itself; a vendor summary is not evidence of the clause. |
| RD3 | EN IEC 62485-6:2021, safe operation of lithium-ion traction batteries | Standard (operation) | Catalogue page only; BMS clause and inspection clause numbers noted in [[SOC and SOH Specifications and Standards]]. | Full text (on the [[Document Wishlist]]). |
| RD4 | Functional safety standards claimed by makers | Standard (design process) | EnerSys: BMS 'designed to meet' ISO 26262 (B5). ROYPOW: separate UL 60730 functional safety assessment of the BMS (B6). Orion lists ISO 7637 load dump and EN 50498 EMC, and names no functional safety standard (B3). | Whether either is required for a forklift; see C201. |
| RD5 | Charger to battery interface | Interface | The charger acts as a slave to the BMS over CAN (see [[Charge Under BMS Control]] and [[BMS-Directed Charge Control Design]]); NexSys iON charges only after CAN is established (B2). | The message set and the CiA 419 profile (page could not be fetched; backlog item IB-040). |
| RD6 | Truck to battery interface | Interface | CANopen and J1939 named by a maker and a vendor guide (B2, B3, and the Polinovel guide cited in [[Battery Management System]]). | Truck-maker message specifications (on the wishlist). |
| RD7 | Customer needs already in the vault | Need hypotheses | [[Charge Each Battery Correctly for Its Chemistry and Condition]], [[Prevent Battery Abuse and Premature Replacement]], [[Integrate the Battery with Truck and Charger Controls]], [[Keep Trucks Working Without Battery Maintenance Labor]]. All are vendor-stated; none has customer-side evidence. | Customer evidence; see [[Fleet Manager and Admin Digital Access Evidence]] for the data-use side. |

### Gaps

- **Product notes:** Orion BMS 2 (and other standalone BMS makers such as REC, Batrium, Elithion and Daly), Flux SkyBMS, ROYPOW forklift batteries and Hoppecke, Toyota and Jungheinrich BMS data sheets have no note or no BMS function detail.
- **Requirements:** none written; the vault's eight Requirements cover BMID, PosiGuard and the state-of-charge estimator.
- **Functions:** the vault has no Function for cell balancing, isolation fault detection, contactor control, or sleep and self-test. They are candidates; none is created here because no product note would perform them yet.
- **Conflicts:** C200 to C202 in [[Battery Product Landscape Conflicts and Open Questions]].

### Question for the owner

Is the aim to specify a BMS PosiCharge would offer or build, or to specify what PosiCharge chargers and the BMID must do when they meet other makers' BMS? The first needs requirements on the BMS itself; the second needs interface requirements on the charger, drawn from RD5 and RD6.

## Sources

- **B1** [[Document - Flux Power SkyBMS Brochure (2023)]] <https://www.fluxpower.com/hubfs/Flux%20Power%20SkyBMS.pdf> (T1)
- **B2** [[Document - EnerSys NexSys iON Operating Manual (Spanish, GLOB-ES-OM-NEX-ION 0323)]] <https://www.enersys.com/4a2ec0/globalassets/documents/product-documentation/nexsys/ion/glob/glob-es-om-nex-ion-0323.pdf> (T1)
- **B3** [[Document - Orion BMS 2 Specifications (Ewert Energy Systems)]] <https://www.orionbms.com/downloads/documents/orionbms2_specifications.pdf> (T1)
- **B4** [[Document - UL What Is UL 2580 Understanding EV Battery Safety Requirements (retrieved 2026-10-13)]] <https://www.ul.com/insights/what-ul-2580-understanding-ev-battery-safety-requirements> (T1)
- **B5** [[Document - EnerSys UL Listing Release for NexSys iON (2022-03-08)]] <https://www.enersys.com/en/about-us/news/enersys-is-taking-safety-to-the-next-level-with-ithium-ion-li-ion-underwriter-laboratories-ul-listing/> (T1)
- **B6** [[Document - ROYPOW UL 2580 Certification Release (2025-04-14)]] <https://www.roypow.com/news/roypow-achieves-ul2580-certification-across-all-lithium-forklift-battery-voltage-platforms/> (T1)
- **B7** [[Document - OEM Off-Highway Inside Battery Certification Standards UL vs SGS vs TUV (ENEROC USA)]] <https://www.oemoffhighway.com/electronics/power-systems/batteries-capacitors/article/22969425/eneroc-usa-forklift-battery-certification-standards-ul-vs-sgs-vs-tv> (T4)
- **B8** [[Document - MH&L Lithium Batteries for Material Handling (Green Cubes, 2024-04-23)]] <https://www.mhlnews.com/new-products/article/55020384/lithium-batteries-for-material-handling> (T2)
- **B9** [[Document - ATEC IEC 62619 Compliance Standards Page (retrieved 2026-10-13)]] <https://www.atecorp.com/compliance-standards/iec/62619> (T4)

## Aliases

- BMS landscape
- battery management system products
- BMS functions
- BMS requirements
- BMS standards
- UL 2580
- IEC 62619

## Former ids
