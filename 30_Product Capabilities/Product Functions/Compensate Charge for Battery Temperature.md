---
type: Function
subtype:
id: FUNC-00032
uid: 20261002193402987skellyspencer
status: Draft
tags:
  - charger
  - extra
  - product-function
subtypeOf:
  - "[[Control Charge Profile]]"
describedBy:
  - "[[Metric - Temperature Compensation Source]]"
performedBy:
  - "[[AMETEK Prestolite Power Eclipse II]]"
  - "[[AMETEK Prestolite Power ULTRA]]"
  - "[[Crown V-HFM3 Charger]]"
  - "[[EnerSys Express Charger]]"
  - "[[EnerSys NexSys+ Charger]]"
  - "[[Fronius Selectiva 4.0]]"
  - "[[HOPPECKE trak charger HF premium]]"
  - "[[PosiCharge DVS100]]"
  - "[[PosiCharge DVS150]]"
  - "[[PosiCharge DVS300 Series]]"
  - "[[PosiCharge SVS100]]"
  - "[[Stryten EHI Charger]]"
  - "[[Stryten X-7 Charger]]"
  - "[[Lester Summit Series II]]"
  - "[[EnerSys NexSys AIR Wireless Charger]]"
  - "[[Stryten inCOMMAND]]"
  - "[[Temperature Compensation Charge Control Firmware]]"
realizes:
  - "[[Charge Each Battery Correctly for Its Chemistry and Condition]]"
dependsOn:
  - "[[Temperature-Compensated Charge Control Design]]"
realizedBy:
  - "[[Temperature-Compensated Charge Control Design]]"
  - "[[Charge Each Battery Correctly for Its Chemistry and Condition]]"
---

# Compensate Charge for Battery Temperature

## Definition

Adjust charge current or end point to the battery temperature supplied by a sensor, monitor or ID device.

## Notes

- Charger-side or charger-and-battery behavior found in product descriptions. Links to products are made only where a source states the behavior; no link means unknown.
- No Requirement is linked (intentional gap).
- **Sources** (product, evidence level, web page):
  - [[EnerSys NexSys+ Charger]] (V): <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf>
  - [[HOPPECKE trak charger HF premium]] (V): <https://hoppecke.com/en/stories/show/switch-from-gas-to-electrically-powered-forklift-trucks>
  - [[Crown V-HFM3 Charger]] (V): <https://www.crown.com/en-au/batteries-and-chargers/vhfm3-charger.html>
  - [[PosiCharge DVS100]] (V): <https://www.posicharge.com/faq/>
  - [[AMETEK Prestolite Power Eclipse II]] (V): <https://www.fleetowner.com/equipment/news/updated-industrial-battery-charger-1115>
  - [[AMETEK Prestolite Power ULTRA]] (V): <https://www.mhlnews.com/archive/ultra-industrial-battery-chargers>
  - [[Fronius Selectiva 4.0]] (V): <https://www.fronius.com/en/battery-charging-technology/our-solutions/individual-battery-charging-solutions/battery-sensor-tagid>
  - [[Lester Summit Series II]] (V): <https://www.rjbatt.com.au/media/nufe2twh/summit-series-ii_650w_data-sheet_060223.pdf>
  - [[Stryten EHI Charger]] (V): <https://og.mhi.org/media/members/14502/133723547947804003.pdf>
  - [[EnerSys Express Charger]] (V): <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf> (also [[Document - EnerSys IMPAQ and NexSys+ Charger Product Guide (AMER 0125)]])
  - [[EnerSys NexSys AIR Wireless Charger]] (V): <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf> (also [[Document - EnerSys IMPAQ and NexSys+ Charger Product Guide (AMER 0125)]])
  - [[Stryten X-7 Charger]] (V): <https://stryten.com/?p=173790>
  - [[PosiCharge SVS100]] (V): <https://og.mhi.org/media/members/16696/131261341460139117.pdf>
  - [[PosiCharge DVS300 Series]] (V): <https://og.mhi.org/media/members/16696/131261342052642309.pdf>
  - [[PosiCharge DVS150]] (V): <https://posicharge.com/products/dvs150/>
  - [[Stryten inCOMMAND]] (V): <https://stryten.com/?p=173790>
  - [[Crown V-HFM3 Charger]] (V): <https://www.crown.com/content/dam/crown/pdfs/en-us/brochures/products/vhfm3-chargers.pdf>
- **Extra (round 30):** documented for 8 of 18 charger maker groups (44 percent); the charger-side realization is now [[Temperature-Compensated Charge Control Design]].

## Implementation Allocation

The reusable realization is [[Temperature-Compensated Charge Control Design]] -> [[Temperature Compensation Charge Control Firmware]].

Two implementation paths are modeled:

- [[Direct Temperature Input Charge Compensation]] for chargers that receive temperature from a charger-connected sensor/input.
- [[Communicated Battery Temperature Charge Compensation]] for chargers that receive temperature from a battery monitor, ID device, or BMS through [[Battery Temperature Reporting to Charger]].

The temperature measurement/reporting path provides the input; the charger-side firmware applies the compensation rule; the charger power stage executes the resulting current/voltage commands.

[[Lester Summit Series II]] is the clearest direct-input example because its published data sheet lists a battery-temperature input and optional sensor. Systems using BMID, TagID, Wi-iQ, or similar battery-mounted devices are allocated to the communicated-temperature path only where the product evidence supports that architecture.

## Aliases


## Former ids
