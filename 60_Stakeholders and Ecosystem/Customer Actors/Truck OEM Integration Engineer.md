---
type: Actor
subtype:
id: ACT-00011
uid: 20261003215631064skellyspencer
status: Draft
tags:
  - customer-role
  - actor
  - role-source-implied
---

# Truck OEM Integration Engineer

## Definition

An engineer at a truck or equipment maker who fits a battery, charger interface and monitoring into a vehicle design.

## Notes

- **Evidence status: source-implied.** Role is implied by OEM-integration language; no source describes the engineer's own requirements.
- **Role in the customer organization:** Needs batteries that report state and accept limits over the truck's data bus.
- **Relation to the product (analyst classification, hypothesis):** buyer (of integration-ready batteries and components).
- **Needs this role takes part in:** see the Use Case notes that list this Actor as a participant (query `participants` in [[README_Customer Needs|Customer Needs]]); the product to need route is in [[Product to Customer Need Map]].
- **Evidence:**
  - [[EnerSys NexSys iON Battery]]: EnerSys says NexSys iON batteries have an integrated battery management system that performs auto-diagnosis, charge and discharge voltage limitation and communication of performance data, provides protection, control and communication to the charger and truck, is designed to meet ISO 26262, supports plug-and-play charging without disconnecting the battery, comes 24 to 80 V and 185 to 1,110 Ah (US standard) with CAN bus communication, and is modular so it can be upsized or downsized. Source: EnerSys releases and NexSys iON product page (T1), retrieved 2026-10-03. <https://www.enersys.com/en/about-us/news/enersys_now_offering_lithium_ion_li_ion_battery_to_global_portfolio_of_power_solutions/>
  - [[HOPPECKE trak collect]]: HOPPECKE says trak | collect highlights incorrect treatment such as deep discharge or temperature warning, and that remaining driving time data helps OEMs optimize drive mode. Source: HOPPECKE news on improved battery management (T1), retrieved 2026-10-02. <https://www.hoppecke.com/uk/news/improved-battery-management-with-trak-collect/>

## Aliases


## Former ids
