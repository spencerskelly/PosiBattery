---
type: Info
subtype:
id: INFO-00130
uid: 20261002195812522skellyspencer
status: Draft
tags:
  - battery
  - charger
  - comparison
  - monitor
  - performance-metric
describes:
  - "[[Battery Monitoring and Identification Device]]"
  - "[[Industrial Battery Charger]]"
  - "[[Industrial Traction Battery]]"
  - "[[Integrated Battery Heater]]"
---

# Metric - Operating Temperature Range

## Definition

Operating Temperature Range: shared metric used for monitors, chargers, batterys.

## Notes

- **Code and class:** MM02, CM18, BM09 (monitor, charger, battery metrics merged by the note re-use rule). Unit or format: C; C; heater.
- **Definition by class:**
  - monitor (MM02): Operating Temperature Range: Ambient range in which the device operates.
  - charger (CM18): Operating Temperature: Ambient operating range of the charger, with derating noted.
  - battery (BM09): Operating Temperature and Heating: Operating range and heating or cooling provisions.
- **Comparability rules by class:**
  - monitor (MM02): Device operating, sensor, and storage ranges differ; convert F to C (C = (F - 32) / 1.8); say which.
  - charger (CM18): State whether derating applies.
  - battery (BM09): Heater power source differs by vendor (C7).
- **Direction:** wider is better.
- **Values on file (as stated in each product note; n/s means not stated):**
  - [[ACT Quantum 2]]: maximum 50 C (122 F) no derating
  - [[ACT Quantum 3]]: -40 to 50 C
  - [[Advanced Charging Technologies BATTview]]: -25 to 60 C
  - [[EnerSys Wi-iQ]]: -20 to 60 C
  - [[Exide Motion+ EasyMonitor]]: -10 to 60 C
  - [[Flow-Rite Eagle Eye Essential IV]]: -40 to 185 F (-40 to 85 C)
  - [[Godrej Multi-Ion Forklift Battery]]: ambient above 45 C (maker claim)
  - [[Green Cubes GSE Lithium Battery]]: heaters; range not stated
  - [[HOPPECKE trak collect]]: use -30 to 80 C (data sheet); earlier note: use -30 to 80 C; storage -30 to 80 C
  - [[Inventus Smart Battery Monitor SBM-01]]: -30 to 70 C; storage -40 to 80 C
  - [[Lester Summit Series II]]: -25 to 60 C; storage -40 to 85 C
  - [[PosiCharge Battery Rx]]: sensor -20 to 165 F (sheet); earlier note: electrolyte sensor -20 to 165 F (-29 to 74 C)
  - [[PosiCharge PosiGuard]]: -25 to 75 C (sheet); earlier note: -25 to 75 C
  - [[Power Designers PowerTrac 3]]: -25 to 60 C (-13 to 140 F) (sheet)
  - [[Power Designers PowerTrac DT3]]: -25 to 60 C
  - [[Power Designers PowerTrac SP+]]: -25 to 60 C
  - [[Stryten EHY Charger]]: operation -10 to +50 C; storage -20 to +70 C
  - [[Stryten X-3 Charger]]: 0 to 45 C
- **Source rule:** the product note holds the source URL for each value; this note copies the value for comparison.
- **Gaps and to-do:** values come from documents as they are absorbed.

## Aliases

- MM02
- CM18
- BM09
- Operating Temperature Range
- Operating Temperature
- Operating Temperature and Heating


## Former ids
- INFO-00176 (Charger Metric - Operating Temperature)
- INFO-00167 (Battery Metric - Operating Temperature and Heating)
