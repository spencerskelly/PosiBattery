---
type: Function
subtype:
id: FUNC-90001
uid: 20261006161000003skellyspencer
status: Draft
tags:
  - charger
  - accessory-function
  - product-function
subtypeOf:
  - "[[Manage Fleet Use]]"
dependsOn:
  - "[[Local Charger Status Indication]]"
performedBy:
  - "[[Charger Status LED Bar Assembly]]"
  - "[[LED Status Indicator Element]]"
  - "[[Status Indicator Driver Circuit]]"
  - "[[ACT Quantum 2]]"
  - "[[ACT Quantum Outdoor]]"
  - "[[Crown V-HFM3 Charger]]"
  - "[[PosiCharge ProCore Edge]]"
  - "[[Crown V-HFM3 Tower Light Kit]]"
  - "[[PosiCharge Three-Color Stack Light]]"
realizedBy:
  - "[[Local Charger Status Indication]]"
---

# Indicate Charger Status Locally

## Definition

Show charger or charge-process status locally at the charger or on a nearby charger-connected status light.

## Notes

- Created to resolve the earlier scope conflict where charger tower/stack lights were linked to [[Indicate Battery Status Locally]].
- Integrated charger LED bars are represented by [[Charger Status LED Bar]].
- Remote visual indicators are represented by [[Remote Charger Status Stack Light]].
- No Requirement or customer-need link is assigned yet; the function is retained as verified product behavior.
- **Sources** are carried on the performing product and Design notes.

## Implementation Allocation

- **Integrated charger LED bar:** [[Charger Status LED Bar]] -> [[Charger Status LED Bar Assembly]] -> [[LED Status Indicator Element]].
- **Remote stack/tower light:** [[Remote Charger Status Stack Light]] -> commercial tower/stack-light Objects. [[Crown V-HFM3 Tower Light Kit]] includes an I/O expansion board; [[PosiCharge Three-Color Stack Light]] requires a separate Accessory Driver Kit.
- [[Status Indicator Driver Circuit]] represents the reusable output-driver role where it is inside the modeled product or assembly. It is not assigned as an internal part of the PosiCharge stack light because PosiCharge explicitly places that role in a separate driver kit.

## Aliases

## Former ids
