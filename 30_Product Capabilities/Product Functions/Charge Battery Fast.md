---
type: Function
subtype:
id: FUNC-00029
uid: 20261002193402984skellyspencer
status: Draft
tags:
  - charger
  - extra
  - product-function
subtypeOf:
  - "[[Charge Battery]]"
describedBy:
  - "[[Metric - Charge Regimes]]"
performedBy:
  - "[[AMETEK Prestolite Power Eclipse II]]"
  - "[[AMETEK Prestolite Power ULTRA]]"
  - "[[Crown Battery EVOLUTION Series]]"
  - "[[Crown V-HFM3 Charger]]"
  - "[[Deka PowerForce Charger]]"
  - "[[EnerSys Express Charger]]"
  - "[[PosiCharge DVS100]]"
  - "[[PosiCharge DVS300 Series]]"
  - "[[PosiCharge High Voltage Power Station (AC)]]"
  - "[[PosiCharge High Voltage Power Station (DC)]]"
  - "[[PosiCharge MVS400 and MVS800]]"
  - "[[PosiCharge SVS100]]"
  - "[[Power Designers REVOLUTION X]]"
  - "[[Raymond Red Charger]]"
  - "[[Stryten EHI Charger]]"
  - "[[Stryten X-3 Charger]]"
  - "[[Stryten X-7 Charger]]"
  - "[[Raymond Energy Essentials Lithium-Ion Battery]]"
  - "[[Exide Sonnenschein Lithium Battery]]"
  - "[[Godrej Multi-Ion Forklift Battery]]"
  - "[[Stryten M-Series F110 Battery]]"
  - "[[Stryten M-Series T310 Battery]]"
  - "[[Stryten M-Series T330 Battery]]"
  - "[[EnerSys NexSys TPPL Battery]]"
  - "[[Deka FastCharge Battery]]"
  - "[[MIDATRON HE Charger]]"
  - "[[Jungheinrich Lithium-Ion Battery]]"
  - "[[Exide TENSOR Battery]]"
  - "[[Exide 2100 HP Charger]]"
  - "[[Toyota Lithium-Ion 5-35 Battery Series]]"
  - "[[Hangcha Lithium Iron Phosphate Battery Pack]]"
  - "[[Cat Lithium-Ion Battery Option]]"
  - "[[Chase Technologies Li-ion Retrofit Packs]]"
realizes:
  - "[[Return Trucks to Service Quickly After a Low Charge]]"
  - "[[Opportunity-Charge a Vehicle During a Work Break]]"
dependsOn:
  - "[[Charger Power Stage Design]]"
  - "[[Charge Profile Control Design]]"
  - "[[Thin Plate Pure Lead Plates]]"
  - "[[Integrated Battery Management System]]"
  - "[[Heavy-Duty Intercell Connectors]]"
  - "[[Copper Inserted Posts]]"
---

# Charge Battery Fast

## Definition

Charge at rates several times conventional charging, at every opportunity, usually with a monitor or ID device.

## Notes

- **Battery-side links added 2026-10-14 (IB-233):** the battery half is a choice of technology, not a stack. Any one is enough for a battery product: [[Thin Plate Pure Lead Plates]] (EnerSys TPPL), [[Integrated Battery Management System]] (lithium-ion; the BMS sets the charge current), or Deka's fast-charge hardware ([[Heavy-Duty Intercell Connectors]], [[Copper Inserted Posts]], one product). These sit beside the two required charger-side Designs above. Flooded Stryten tubular lines, Exide TENSOR (fast-charge package of charger, air agitation and temperature probe) and Godrej and Chase packs state no Design that sets the rate and are not linked (see [[Function-to-Solution Coverage Register]]).
- **Solution link added 2026-10-14 (analyst reasoning; no source states the split):** depends on [[Charger Power Stage Design]] and [[Charge Profile Control Design]]; both are needed together, as the power stage delivers the current and the profile decides its shape over time. Performers include batteries as well as chargers; the battery side (a chemistry or construction that accepts the rate) has no Design yet (IB-233).
- Charger-side or charger-and-battery behavior found in product descriptions. Links to products are made only where a source states the behavior; no link means unknown.
- No Requirement is linked (intentional gap).
- **Sources** (product, evidence level, web page):
  - [[Deka PowerForce Charger]] (V): <https://www.eastpennmanufacturing.com/?p=6135>
  - [[Stryten X-7 Charger]] (V): <https://www.nacleanenergy.com/energy-storage/unlocking-fleet-versatility-while-simplifying-charging-infrastructure>
  - [[Crown V-HFM3 Charger]] (V): <https://www.crown.com/content/dam/crown/pdfs/en-us/brochures/products/vhfm3-chargers.pdf>
  - [[PosiCharge DVS100]] (V): <https://www.posicharge.com/dvs100/>
  - [[Power Designers REVOLUTION X]] (V): <https://www.carolinahandling.com/-/media/dealers/carolina-handling/literature/battery-chargers/ch-rev-series_overview_01-2017.pdf>
  - [[Raymond Red Charger]] (V): <https://www.carolinahandling.com/products/raymond-red-charger>
  - [[Crown Battery EVOLUTION Series]] (V): <https://crownbattery.com/lp-power-line>
  - [[AMETEK Prestolite Power Eclipse II]] (V): <https://www.fleetowner.com/equipment/news/updated-industrial-battery-charger-1115>
  - [[AMETEK Prestolite Power ULTRA]] (V): <https://www.mhlnews.com/archive/ultra-industrial-battery-chargers>
  - [[Stryten X-3 Charger]] (V): <https://og.mhi.org/media/members/14502/133723547947804003.pdf>
  - [[Stryten EHI Charger]] (V): <https://og.mhi.org/media/members/14502/133723547947804003.pdf>
  - [[EnerSys Express Charger]] (V): <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf> (also [[Document - EnerSys IMPAQ and NexSys+ Charger Product Guide (AMER 0125)]])
  - [[PosiCharge SVS100]] (V): <https://og.mhi.org/media/members/16696/131261341460139117.pdf>
  - [[PosiCharge DVS300 Series]] (V): <https://og.mhi.org/media/members/16696/131261342052642309.pdf>
  - [[PosiCharge MVS400 and MVS800]] (V): <https://og.mhi.org/media/members/16696/131261342583679925.pdf>
  - [[PosiCharge High Voltage Power Station (DC)]] (V): <https://posicharge.com/products/high-voltage-power-station-dc/>
- **Extra (round 30):** documented for 8 of 18 charger maker groups (44 percent), delivered by devices or software (accessory and software notes); rule and caveats in [[Extra Functions Register]].

## Aliases


## Former ids
