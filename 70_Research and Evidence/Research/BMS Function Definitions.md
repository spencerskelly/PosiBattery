---
type: Info
subtype:
id: INFO-90038
uid: 20261013233000018skellyspencer
status: Draft
tags:
  - research
  - bms
  - definitions
describes:
  - "[[Battery Management System]]"
  - "[[Protect Battery from Harm]]"
  - "[[Balance Cells]]"
  - "[[Disconnect Battery on Limit Violation]]"
describedBy:
  - "[[Document - MathWorks Battery Management System Overview (retrieved 2026-10-13)]]"
  - "[[Document - Wikipedia Battery Management System (retrieved 2026-10-13)]]"
---

# BMS Function Definitions

## Definition

What a battery management system (BMS) does, defined from neutral sources first and compared with what makers state. Use it to name BMS functions consistently; the maker evidence is in [[BMS Product Function and Requirement Driver Map]].

## Notes

### How to read this note

- **Neutral sources used:** an encyclopedia article ([[Document - Wikipedia Battery Management System (retrieved 2026-10-13)]]) and a software-vendor educational page ([[Document - MathWorks Battery Management System Overview (retrieved 2026-10-13)]]). Both are tertiary or promotional. Neither is a normative standard. The normative definitions would come from standards such as IEC 62619, UL 2580, ISO 26262 and UL 60730, which are on the [[Document Wishlist]] and have not been read.
- **Where they agree** the function is treated as defined. **Where only one neutral source or only makers state it**, the row says so.

### Functions

| Id | Function | Neutral definition | Neutral sources | Vault Function | OEM evidence in [[BMS Product Function and Requirement Driver Map]] |
|---|---|---|---|---|---|
| BD1 | Monitor | Measure total, per-cell or tap voltage, temperature, current, coolant flow, cell health and cell balance state | W1, W15 | [[Measure Battery Voltage]], [[Measure Battery Current]], [[Measure Battery Temperature]] | BF1 |
| BD2 | Estimate states | Compute secondary data: state of charge, state of health, state of power, charge and discharge current limits, energy delivered, internal impedance, cycle count | W1, W15 | [[Estimate State of Charge]], [[Estimate State of Health]], [[Accumulate Amp-Hours]]; no Function for state of power or current limits | BF6 |
| BD3 | Protect | Prevent operation outside the safe operating area: over and under charge and discharge, over and under voltage and current, over and under temperature, overpressure (NiMH), ground fault | W1, W15 | [[Protect Battery from Harm]], [[Protect Battery from Deep Discharge]], [[Detect Cell Failure]], [[Disconnect Battery on Limit Violation]] (new) | BF2 |
| BD4 | Balance | Equalize cells by energy dissipation (passive), energy shuffling (active) or reduced charge current | W1, W15 | [[Balance Cells]] (new) | BF3 |
| BD5 | Manage temperature | Passive or active thermal management, by air, liquid or phase-change cooling | W1 | [[Compensate Charge for Battery Temperature]], [[Manage Temperature During Fast Charging]]; no Function for pack heating or cooling | BF11 |
| BD6 | Set limits for charge and discharge | Compute charge and discharge current limits and make them available to the charger or vehicle | W1 | [[Charge Under BMS Control]], [[Command Vehicle Operating Limits over CAN]], [[Communicate Battery State over CAN]] | BF4, BF5 |
| BD7 | Control contactors | Precharge control of contactors; open the power path on a fault | W1 | [[Disconnect Battery on Limit Violation]] (new) | BF2 |
| BD8 | Communicate | Internal cell-level and controller-to-controller links, and external links to a laptop or display; CAN named as common in automotive use | W1 | [[Communicate Battery and Vehicle Data]], [[Communicate with Charger]] | BF4, BF5 |
| BD9 | Report to a display | Report battery state to a display | W1 | [[Display Battery Status to Operator]], [[Indicate Battery Status Locally]] | BF6 |
| BD10 | Authenticate | Named in the definition of a BMS and not explained | W1 | none; no neutral source explains it | none |
| BD11 | Log and diagnose | Not listed in the neutral sources read; stated by makers (event logs, remote diagnosis) | none | [[Log Battery Events and Usage]] | BF9 |

Not listed in the neutral sources and stated only by makers: fault lockout and error codes, sleep and self-test timers, isolation fault detection (only Orion BMS 2 states it), and logging. They are real product behaviour but have no neutral definition yet; see BF7, BF8, BF10 in the BMS map.

### Terms the neutral sources define

- **State of charge:** 'to indicate the charge level of the battery' ([[Document - Wikipedia Battery Management System (retrieved 2026-10-13)]]); 'a normalized quantity that indicates how much charge is left' ([[Document - MathWorks Battery Management System Overview (retrieved 2026-10-13)]]). Neither gives a formula or a reference capacity. See [[SOC and SOH Methods Reference]].
- **State of health:** 'a variously defined measurement of the remaining capacity of the battery as a fraction of the original capacity' ([[Document - Wikipedia Battery Management System (retrieved 2026-10-13)]]); based on internal resistance and capacity, with 'no universal agreement' on the definition ([[Document - MathWorks Battery Management System Overview (retrieved 2026-10-13)]]). See C203.
- **State of power:** 'the amount of power available for a defined time interval' given current power usage, temperature and other conditions ([[Document - Wikipedia Battery Management System (retrieved 2026-10-13)]]); named but not defined by [[Document - MathWorks Battery Management System Overview (retrieved 2026-10-13)]].
- **State of energy:** named by [[Document - MathWorks Battery Management System Overview (retrieved 2026-10-13)]] only; no definition read.

### Topologies

The encyclopedia names centralized, modular (a few controllers, each handling a number of cells) and distributed ([[Document - Wikipedia Battery Management System (retrieved 2026-10-13)]]). The MathWorks page describes the pack hierarchy (cell, parallel assembly, module, pack) and no topologies. No maker source read states its topology; the NexSys iON manual describes power modules with sensors, which is consistent with a modular layout but does not say so ([[Document - EnerSys NexSys iON Operating Manual (Spanish, GLOB-ES-OM-NEX-ION 0323)]]).

### Gaps

- No normative definition read. The functions above are descriptive.
- No Function for state of power, current-limit computation, thermal control, isolation monitoring, authentication or sleep and self-test; these are candidates, created only when a product note performs them.
- Cell-level detail (cutoff values, balancing thresholds) is not in any source read.

## Sources

- **W1** [[Document - Wikipedia Battery Management System (retrieved 2026-10-13)]] <https://en.wikipedia.org/wiki/Battery_management_system>
- **W15** [[Document - MathWorks Battery Management System Overview (retrieved 2026-10-13)]] <https://www.mathworks.com/discovery/battery-management-system.html>
- Maker evidence: [[Document - EnerSys NexSys iON Operating Manual (Spanish, GLOB-ES-OM-NEX-ION 0323)]], [[Document - Orion BMS 2 Specifications (Ewert Energy Systems)]], [[Document - Flux Power SkyBMS Brochure (2023)]]

## Aliases

- BMS functions
- what a BMS does
- BMS definition
- SOC SOH SOP definitions
- cell balancing
- BMS protection

## Former ids
