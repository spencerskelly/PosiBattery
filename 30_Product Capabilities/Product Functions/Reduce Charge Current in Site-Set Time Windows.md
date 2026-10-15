---
type: Function
subtype:
id: FUNC-00154
uid: 20261014194007771skellyspencer
status: Draft
tags:
  - charger
  - product-function
subtypeOf:
  - "[[Keep Charging Available and Safe]]"
performedBy:
  - "[[PosiCharge DVS300 Series]]"
  - "[[PosiCharge MVS400 and MVS800]]"
realizes:
  - "[[Charge Within Site Power Limits and Utility Costs]]"
dependsOn:
  - "[[Time-Window Charge Current Setting]]"
---

# Reduce Charge Current in Site-Set Time Windows

## Definition

Let the site set time windows in which the charger lowers its charge current, so energy use is lower in those hours.

## Notes

- Added 2026-10-14 from the owner's account that reduced charging is 'windows of reduced energy usage' and that 'windows are set by the site owners' (U). The owner has not said what the site owners are reacting to.
- **Manual (V):** [[Document - PosiCharge DVS and MVS GSE Operation and Maintenance Manual (5914769 rev C03)]] section 4.7: the user sets a charge current and a time window; if the charger is charging inside the window, the current is reduced to that value and held there while the charge stays inside the window. Set from the Charger Configuration menu, which needs an access code. The manual gives no reason.
- **Need (analyst link, hypothesis):** realizes [[Charge Within Site Power Limits and Utility Costs]] because lower current in set hours is a way to lower site draw; whether sites use it for utility rates, a demand limit or something else is not stated (C278, IB-241).
- Difference from [[Balance Charging Power Across Site Capacity]]: that Function shares power by live site or peer measurement; this one is a fixed local schedule set by a person. No claim is made that either replaces the other.
- No Requirement is linked (intentional gap).
- **Sources** (product, evidence level, document):
  - [[PosiCharge DVS300 Series]] (V): [[Document - PosiCharge DVS and MVS GSE Operation and Maintenance Manual (5914769 rev C03)]], section 4.7
  - [[PosiCharge MVS400 and MVS800]] (V): [[Document - PosiCharge DVS and MVS GSE Operation and Maintenance Manual (5914769 rev C03)]], section 4.7

## Aliases


## Former ids
