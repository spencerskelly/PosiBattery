---
type: Info
subtype:
id: INFO-00139
uid: 20261002195812531skellyspencer
status: Draft
tags:
  - charger
  - comparison
  - monitor
  - performance-metric
describes:
  - "[[Battery Monitoring and Identification Device]]"
  - "[[Industrial Battery Charger]]"
---

# Metric - Power Consumption

## Definition

Power Consumption: shared metric used for monitors, chargers.

## Notes

- **Code and class:** MM11, CM16 (monitor, charger metrics merged by the note re-use rule). Unit or format: W or mA at V; W.
- **Definition by class:**
  - monitor (MM11): Power Consumption: Supply power or current.
  - charger (CM16): Standby Power Consumption: Power drawn while the charger is idle.
- **Comparability rules by class:**
  - monitor (MM11): Quote voltage and whether the radio is transmitting.
  - charger (CM16): Compare only with the same measurement conditions; the EnerSys figure is a portfolio statement.
- **Direction:** lower is better.
- **Values on file (as stated in each product note; n/s means not stated):**
  - [[EnerSys Express Charger]]: under 10 W (portfolio statement)
  - [[EnerSys IMPAQ Charger]]: under 10 W (portfolio statement)
  - [[EnerSys NexSys AIR Wireless Charger]]: under 10 W (portfolio statement)
  - [[EnerSys NexSys+ Charger]]: under 10 W (portfolio statement)
  - [[EnerSys Wi-iQ]]: 1 W
  - [[Flow-Rite Eagle Eye Essential IV]]: 0.015 A
  - [[HOPPECKE trak collect]]: 7.5 mA at 150 V to 70 mA at 17 V
  - [[Inventus Smart Battery Monitor SBM-01]]: 1.4 W typical
  - [[Philadelphia Scientific eGO!plus]]: 20-24 mA transmitting; 10-13 mA idle (24-80 V)
  - [[Philadelphia Scientific eGO!pro]]: conflict (C22): US 2 W initial Bluetooth, 1.2 W nominal; UK 200-24 mA and 100-13 mA
  - [[Power Designers PowerTrac 3]]: 1/2 W nominal (sheet)
  - [[Power Designers PowerTrac DT3]]: 0.5 W nominal
- **Source rule:** the product note holds the source URL for each value; this note copies the value for comparison.
- **Gaps and to-do:** values come from documents as they are absorbed.

## Aliases

- MM11
- CM16
- Power Consumption
- Standby Power Consumption


## Former ids
- INFO-00174 (Charger Metric - Standby Power Consumption)
