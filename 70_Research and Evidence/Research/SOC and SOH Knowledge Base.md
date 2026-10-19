---
type: Info
subtype:
id: INFO-90035
uid: 20261013200000001skellyspencer
status: Draft
tags:
  - research
  - soc-soh
  - index
describes:
  - "[[Estimate State of Charge]]"
  - "[[Estimate State of Health]]"
describedBy:
---

# SOC and SOH Knowledge Base

## Definition

Entry point for everything the vault holds on state of charge (SOC) and state of health (SOH): methods, products, specifications, source documents, conflicts and documents still wanted. It supports an engineer building the approach decision matrix; the matrix itself is not built here.

## Notes

### Read in this order

1. [[SOC and SOH Methods Reference]] - SOC methods M1-M8 and SOH methods H1-H6, with source keys S1-S24.
2. [[SOC and SOH Product Landscape]] - gauge ICs, monitors and BMS, forklift packs and displays, test instruments.
3. [[SOC and SOH Specifications and Standards]] - definitions, data-sheet measurement chain, standards table.
4. [[SOC and SOH Decision Criteria]] - candidate approach families, criteria, owner questions.
5. Open items below - conflicts and wanted documents.

### Open items

- Conflicts C190-C195 are in [[Battery Product Landscape Conflicts and Open Questions]]: rest-time definitions, non-comparable accuracy claims, SOH thresholds, gauge limits versus 80 V packs, impedance versus capacity, LFP OCV flatness.
- Documents still wanted (standards, data sheets, patent, reviews, truck CAN specifications) are rows added in round R41 of [[Document Wishlist]]. Add new wanted documents there.
- Owner questions that feed the matrix are listed in [[SOC and SOH Decision Criteria]]: chemistries and voltage range, SOC accuracy target, SOH purpose, estimator location. Question 1 was answered in part on 2026-10-18 (all chemistries, up to 96 VDC; nominal versus maximum not stated); see the update at the end of that note. White paper rows are in round R73 of [[Document Wishlist]]; nine of those papers were added to the repo and absorbed on 2026-10-18 (source keys S25 to S33).

### Related vault items

- Functions: [[Estimate State of Charge]], [[Estimate State of Health]].
- Products: [[PosiCharge BMID]], [[AMETEK Prestolite Power WBID Pro]], [[Power Designers PowerTrac DT3]], [[Philadelphia Scientific eGO!pro]], [[Raymond iBattery]], [[EnerSys Wi-iQ]], [[EnerSys NexSys iON Battery]], [[Flux Power LiFT Pack]], [[EnerSys Truck iQ]].
- Earlier literature note: [[SOC and Health Estimation Literature Review]].

### Source documents (33)

- [[Document - ADI Considerations for Fuel Gauging Lithium Iron Phosphate Batteries]]
- [[Document - ADI MAX17320 Product Page (retrieved 2026-10-13)]]
- [[Document - Battery University BU-903 How to Measure State of Charge (retrieved 2026-10-13)]]
- [[Document - Battery University BU-904 How to Measure Capacity (retrieved 2026-10-13)]]
- [[Document - Berecibar et al. Critical Review of State of Health Estimation Methods of Li-ion Batteries for Real Applications (2016)]]
- [[Document - Bilfinger et al. Why We Need a Standardized State of Health Definition for EV Battery Packs (2025)]]
- [[Document - Cadex Spectro Technology Page (retrieved 2026-10-13)]]
- [[Document - Delta Systems Flux Power SOC Display]]
- [[Document - Electronic Design TI bq34z110 Lead-Acid Gas Gauge IC (2013-05-30)]]
- [[Document - EnerSys Truck iQ Operating Manual (GLOB-EN-OM-TIQ-APAC 0324)]]
- [[Document - Fluke Recommended Battery Tests and Testing Schedule (retrieved 2026-10-13)]]
- [[Document - Flux Power LiFT Pack L-Series L48 Brochure]]
- [[Document - ISO 12405-4:2018 Standard Page (retrieved 2026-10-13)]]
- [[Document - Midtronics Using Conductance Technology to Ensure Battery System Reliability (BATTCON 2003)]]
- [[Document - Orion BMS State of Charge Calculation with Dynamic Drift (retrieved 2026-10-13)]]
- [[Document - Orion BMS Troubleshooting State of Charge Jumps]]
- [[Document - Paizulamu et al. LiFePO4 SOC Estimation under OCV-SOC Curve Error (arXiv 2024)]]
- [[Document - SIST EN IEC 62485-6:2021 Catalog Page (retrieved 2026-10-13)]]
- [[Document - TI BQ34Z100-G1 Data Sheet]]
- [[Document - TI BQ34Z100-G1 Product Page (retrieved 2026-10-13)]]
- [[Document - TWAICE Fleet Operator Page (retrieved 2026-10-13)]]
- [[Document - TWAICE State of Health Encyclopedia Entry (retrieved 2026-10-13)]]
- [[Document - Victron BMV-712 Smart Manual Battery Capacity and Peukert Exponent (retrieved 2026-10-13)]]
- [[Document - Victron SmartShunt Product Page (retrieved 2026-10-13)]]
- [[Document - Khan et al. Flooded Lead Acid SOC Estimation Using Adaptive Unscented Kalman Filter (Energies 2024)]]
- [[Document - Lazzarin and Barbi A System for State-of-Health Diagnosis of Lead-Acid Batteries Integrated with a Battery Charger (2011-2012)]]
- [[Document - Tinnemeyer (Cadex) Multiple Model Impedance Spectroscopy Techniques for Testing Electrochemical Systems (BATTCON 2004)]]
- [[Document - Chang The State of Charge Estimating Methods for Battery A Review (ISRN Applied Mathematics 2013)]]
- [[Document - Xiong et al. Critical Review on the Battery State of Charge Estimation Methods for Electric Vehicles (IEEE Access 2017)]]
- [[Document - Zhang et al. A Critical Review of the State Estimation Methods of Power Batteries for Electric Vehicles (Energies 2025)]]
- [[Document - Li et al. Data-driven health estimation and lifetime prediction of lithium-ion batteries A review (RSER 2019)]]
- [[Document - Noura et al. A Review of Battery State of Health Estimation Methods Hybrid Electric Vehicle Challenges (WEVJ 2020)]]
- [[Document - Gao and Onori Advancing SOC Estimation in LiFePO4 Batteries Enhanced dQ-dV Curve and Short-Pulse Methods (eTransportation 2025)]]

### Search tips

Search the tag `soc-soh` to list every note and document in this set. Search the terms in each note's Aliases (for example fuel gauge, coulomb counting, Impedance Track, Peukert). Source keys S1-S24 are defined in the three reference notes.

## Former ids
