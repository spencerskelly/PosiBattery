---
type: Use Case
subtype: why
id: UC-00019
uid: 20261003215631083skellyspencer
status: Draft
tags:
  - customer-need
  - need-hypothesis
  - vendor-stated
realizedBy:
  - "[[Communicate Battery State over CAN]]"
  - "[[Command Vehicle Operating Limits over CAN]]"
  - "[[Communicate with Charger]]"
participants:
  - "[[Truck OEM Integration Engineer]]"
---

# Integrate the Battery with Truck and Charger Controls

## Definition

Customer need: Integrate the Battery with Truck and Charger Controls. The problem behind it: A battery that cannot tell the truck and charger its state and limits cannot be protected or used to full value.

## Notes

- **Evidence status: need hypothesis.** The statements below are what makers and dealers say their products do for customers. No customer, user or buyer source in the vault confirms that customers hold this need or rank it. Per the ruleset, source research becomes a validated need only after customer-side evidence.
- **Problem solved (analyst wording):** A battery that cannot tell the truck and charger its state and limits cannot be protected or used to full value.
- **Who has the problem:** [[Truck OEM Integration Engineer]].
- **Operating segments (analyst crosswalk to [[PosiCharge Market Segments and Jobs-to-Be-Done]], hypothesis):** Mixed-chemistry fleets.
- **Realized by (specific functions; products link to these):** [[Communicate Battery State over CAN]], [[Command Vehicle Operating Limits over CAN]], [[Communicate with Charger]].
- **Products reaching this need through those functions:** 15. Largest families: Battery Accessories/Monitoring Devices (8), Battery Accessories/Identification and Charge Interface Devices (3), Batteries/Lithium-Ion Batteries (2), Fleet Software and Platforms/Battery and Charger Management (1), Vehicle Accessories/Power Source Interfaces (1). Per-product list in [[Product to Customer Need Map]].
- **Vendor-stated evidence (by product):**
  - [[EnerSys NexSys iON Battery]]: EnerSys says NexSys iON batteries have an integrated battery management system that performs auto-diagnosis, charge and discharge voltage limitation and communication of performance data, provides protection, control and communication to the charger and truck, is designed to meet ISO 26262, supports plug-and-play charging without disconnecting the battery, comes 24 to 80 V and 185 to 1,110 Ah (US standard) with CAN bus communication, and is modular so it can be upsized or downsized. Source: EnerSys releases and NexSys iON product page (T1), retrieved 2026-10-03. <https://www.enersys.com/en/about-us/news/enersys_now_offering_lithium_ion_li_ion_battery_to_global_portfolio_of_power_solutions/>
  - [[HOPPECKE trak collect]]: HOPPECKE says trak | collect highlights incorrect treatment such as deep discharge or temperature warning, and that remaining driving time data helps OEMs optimize drive mode. Source: HOPPECKE news on improved battery management (T1), retrieved 2026-10-02. <https://www.hoppecke.com/uk/news/improved-battery-management-with-trak-collect/>
- **Gaps:** no customer-side source; each function in the list is realized by only the products that state it, so the product count is a lower bound; no Requirement is linked (the vault leaves requirements as an intentional gap).

## Aliases


## Former ids
