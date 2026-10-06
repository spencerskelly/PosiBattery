---
type: Object
subtype: electrical
id: OBJ-00089
uid: 20261002193402945skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - battery
subtypeOf:
  - "[[Lithium-Ion Traction Battery]]"
performs:
  - "[[Communicate with Charger]]"
  - "[[Protect Battery from Deep Discharge]]"
hasDesign:
  - "[[Integrated Battery Management System]]"
  - "[[BMS Discharge Limitation]]"
madeBy:
hasPart:
  - "[[BMS Discharge Protection Logic]]"
  - "[[EnerSys]]"
---

# EnerSys NexSys iON Battery

## Definition

EnerSys lithium-ion battery line for material handling.

## Notes

- EnerSys's guide says NexSys iON batteries feature what it calls the most advanced lithium-ion technology in the material handling industry. Source: EnerSys EMEA motive power guide (T1), retrieved 2026-10-02. <https://enersys.com/4a4c3f/globalassets/documents/product-documentation/_enersys/emea/emea-mp-product-guide-0423.pdf>
- EnerSys says NexSys iON batteries have an integrated battery management system that performs auto-diagnosis, charge and discharge voltage limitation and communication of performance data, provides protection, control and communication to the charger and truck, is designed to meet ISO 26262, supports plug-and-play charging without disconnecting the battery, comes 24 to 80 V and 185 to 1,110 Ah (US standard) with CAN bus communication, and is modular so it can be upsized or downsized. Source: EnerSys releases and NexSys iON product page (T1), retrieved 2026-10-03. <https://www.enersys.com/en/about-us/news/enersys_now_offering_lithium_ion_li_ion_battery_to_global_portfolio_of_power_solutions/>
- **Functions performed, with citations:**
  - [[Communicate with Charger]] (V): <https://www.enersys.com/en/about-us/news/enersys_now_offering_lithium_ion_li_ion_battery_to_global_portfolio_of_power_solutions/>
  - [[Protect Battery from Deep Discharge]] (V): <https://www.enersys.com/en/about-us/news/enersys_now_offering_lithium_ion_li_ion_battery_to_global_portfolio_of_power_solutions/>
- **Design characteristics, with citations:**
  - [[Integrated Battery Management System]] (V): <https://www.enersys.com/en/about-us/news/enersys_now_offering_lithium_ion_li_ion_battery_to_global_portfolio_of_power_solutions/>
- EnerSys says NexSys iON is maintenance free with no long equalize charges, and that its BMS performs voltage limitation on charge and discharge and can integrate with the truck over CAN. Source: MH&L News (2023-07-26) (T2), retrieved 2026-10-03. <https://www.mhlnews.com/new-products/article/21270278/lithium-ion-battery>
- A second trade item says fast- and opportunity-charging NexSys iON batteries are paired with high-output NexSys+ chargers. Source: Inside Logistics (T2), retrieved 2026-10-03. <https://www.insidelogistics.ca/products/80-volt-lithium-ion-battery/>

- **Architecture realization — deep discharge protection:** the integrated BMS and published discharge-voltage limitation support [[BMS Discharge Limitation]] and [[BMS Discharge Protection Logic]]. The exact final enforcement mechanism is not published, so no specific contactor or truck-command path is asserted.

## Aliases

- NexSys iON


## Former ids
