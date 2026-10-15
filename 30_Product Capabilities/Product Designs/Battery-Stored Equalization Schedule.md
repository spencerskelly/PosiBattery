---
type: Design
subtype:
id: DES-00144
uid: 20261014191236334skellyspencer
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
  - "[[Equalize Battery on Schedule]]"
---

# Battery-Stored Equalization Schedule

## Definition

The equalization schedule and limits are held in the battery's monitoring device, and the charger runs equalization when the stored limits say it is due.

## Notes

- Design characteristic found in products, not a decision by us. Added 2026-10-14.
- **Basis:** the PosiCharge DVS and MVS manual says the equalization schedule is stored in the BMID and runs automatically, and that each BMID holds the maximum amp-hours between equalizations, the maximum days between them and the equalization day of the week. Source: [[Document - PosiCharge DVS and MVS GSE Operation and Maintenance Manual (5914769 rev C03)]] (T1).
- **Inference, not stated by the manual:** because the schedule lives on the battery and not in the charger, any charger that reads the BMID can run it, which is what the Function's wording 'even when the battery moves between chargers' asks for. The manual does not say that sentence.
- Covers only the products that carry a BMID; the other 11 performers of [[Equalize Battery on Schedule]] (ACT Quantum, AMETEK Eclipse II, EnerSys, Power Designers and others) state no scheduling mechanism and are not linked to this Design.
- **Sources** (product, evidence level, document):
  - [[PosiCharge DVS300 Series]] (V): [[Document - PosiCharge DVS and MVS GSE Operation and Maintenance Manual (5914769 rev C03)]]
  - [[PosiCharge MVS400 and MVS800]] (V): [[Document - PosiCharge DVS and MVS GSE Operation and Maintenance Manual (5914769 rev C03)]]

## Aliases


## Former ids
