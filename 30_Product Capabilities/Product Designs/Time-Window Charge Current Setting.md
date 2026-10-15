---
type: Design
subtype:
id: DES-00145
uid: 20261014194007786skellyspencer
status: Draft
tags:
  - charger
  - control
  - design-characteristic
subtypeOf:
  - "[[Charge Profile Control Design]]"
designOf:
  - "[[PosiCharge DVS300 Series]]"
  - "[[PosiCharge MVS400 and MVS800]]"
dependencyOf:
  - "[[Reduce Charge Current in Site-Set Time Windows]]"
---

# Time-Window Charge Current Setting

## Definition

A charge current limit and a start and end time are stored in the charger's configuration, and the charger applies the lower current whenever a charge runs inside that window.

## Notes

- Design characteristic found in products, not a decision by us. Added 2026-10-14.
- **Basis:** [[Document - PosiCharge DVS and MVS GSE Operation and Maintenance Manual (5914769 rev C03)]] section 4.7 (T1). The manual does not say whether the window repeats daily or by weekday, or how it interacts with the BMID's own current limits; not assumed here.
- **Sources** (product, evidence level, document):
  - [[PosiCharge DVS300 Series]] (V): [[Document - PosiCharge DVS and MVS GSE Operation and Maintenance Manual (5914769 rev C03)]]
  - [[PosiCharge MVS400 and MVS800]] (V): [[Document - PosiCharge DVS and MVS GSE Operation and Maintenance Manual (5914769 rev C03)]]

## Aliases


## Former ids
