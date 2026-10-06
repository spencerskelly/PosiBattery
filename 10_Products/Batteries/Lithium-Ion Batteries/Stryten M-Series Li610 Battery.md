---
type: Object
subtype: electrical
id: OBJ-00112
uid: 20261002193402968skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - battery
  - hibernation
subtypeOf:
  - "[[Lithium-Ion Traction Battery]]"
performs:
  - "[[Estimate State of Charge]]"
  - "[[Measure Battery Temperature]]"
  - "[[Measure Battery Voltage]]"
  - "[[Measure Battery Current]]"
hasDesign:
  - "[[Hibernation Mode]]"
  - "[[Integrated Battery Management System]]"
  - "[[BMS Internal Temperature Sensing]]"
hasPart:
  - "[[BMS Temperature Sensor Network]]"
madeBy:
  - "[[Stryten Energy]]"
offeredWith:
  - "[[Stryten X-7 Charger]]"
  - "[[Stryten X-3 Charger]]"
  - "[[Stryten inCOMMAND]]"
---

# Stryten M-Series Li610 Battery

## Definition

Stryten LFP battery for Class I forklifts with an onboard display and hibernation mode, launched in April 2026.

## Notes

- Stryten says Li610 shows state of charge, temperature, voltage and current on an onboard display, has automated hibernation, is made in the US, is compatible with X-3 and X-7 chargers, and integrates with inCOMMAND; UL2580 certification is being pursued. Source: Business Wire (2026-04-13) (T2), retrieved 2026-10-02. <https://www.businesswire.com/news/home/20260413514429/en/Stryten-Energy-Launches-New-MSeries-Li610-LithiumIon-Battery-at-MODEX>
- **Evidence upgrade (2026-10-05):** Stryten's current Li610 product page and 2026 Installation and Operation Manual identify the Li610 as an LFP battery that reports battery temperature and uses a BMS communicating with the charger. Sources (T1): <https://www.stryten.com/motive-power-solutions/m-series-li610/>; <https://www.stryten.com/wp-content/uploads/2026/04/M-Series-Li610-Installation-Operational-Manual-SE2070_Final.pdf>
- **Temperature implementation assumption:** [[BMS Internal Temperature Sensing]] and [[BMS Temperature Sensor Network]] are allocated at **>=95% engineering confidence** because the product has an onboard BMS and reports battery temperature. The public documentation does not identify the sensor technology, number of sensors, or exact placement.
- **Functions performed, with citations** (V = verified this pass):
  - [[Estimate State of Charge]] (V): <https://www.businesswire.com/news/home/20260413514429/en/Stryten-Energy-Launches-New-MSeries-Li610-LithiumIon-Battery-at-MODEX>
  - [[Measure Battery Temperature]] (V): <https://www.businesswire.com/news/home/20260413514429/en/Stryten-Energy-Launches-New-MSeries-Li610-LithiumIon-Battery-at-MODEX>
  - [[Measure Battery Voltage]] (V): <https://www.businesswire.com/news/home/20260413514429/en/Stryten-Energy-Launches-New-MSeries-Li610-LithiumIon-Battery-at-MODEX>
  - [[Measure Battery Current]] (V): <https://www.businesswire.com/news/home/20260413514429/en/Stryten-Energy-Launches-New-MSeries-Li610-LithiumIon-Battery-at-MODEX>
- **Design characteristics, with citations:**
  - [[Hibernation Mode]] (V): <https://www.businesswire.com/news/home/20260413514429/en/Stryten-Energy-Launches-New-MSeries-Li610-LithiumIon-Battery-at-MODEX>
  - [[Integrated Battery Management System]] (V): <https://www.stryten.com/wp-content/uploads/2026/04/M-Series-Li610-Installation-Operational-Manual-SE2070_Final.pdf>
  - [[BMS Internal Temperature Sensing]] (A, >=95%): <https://www.stryten.com/motive-power-solutions/m-series-li610/>
- **Related products and how they differ (offeredWith):**
  - [[Stryten X-7 Charger]]: no difference stated in the sources.
  - [[Stryten X-3 Charger]]: no difference stated in the sources.

## Aliases

- Li610


## Former ids
