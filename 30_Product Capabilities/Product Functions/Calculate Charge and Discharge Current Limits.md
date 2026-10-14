---
type: Function
subtype:
id: FUNC-90007
uid: 20261014000000005skellyspencer
status: Draft
tags:
  - battery-protection
  - bms
  - product-function
subtypeOf:
  - "[[Protect Battery from Harm]]"
performedBy:
  - "[[Orion BMS 2]]"
describedBy:
  - "[[BMS Function Definitions]]"
  - "[[External BMS Product Landscape]]"
---

# Calculate Charge and Discharge Current Limits

## Definition

Compute the largest charge and discharge current the battery may take at this moment and make it available to the charger or vehicle.

## Notes

- Neutral definition: the encyclopedia article lists charge and discharge current limits among the secondary data a BMS computes ([[Document - Wikipedia Battery Management System (retrieved 2026-10-13)]]). See BD2 and BD6 in [[BMS Function Definitions]].
- Product evidence: the Orion BMS 2 page says it 'calculates discharge current limit (DCL) and charge current limit (CCL)' ([[Document - Orion BMS 2 Product Page (retrieved 2026-10-13)]]). The NexSys iON manual says current limits depend on temperature ([[Document - EnerSys NexSys iON Operating Manual (Spanish, GLOB-ES-OM-NEX-ION 0323)]]), which is a limit that varies, not a stated computation.
- Related: the charger and truck consume the result: [[Charge Under BMS Control]], [[Command Vehicle Operating Limits over CAN]].
- No Requirement is linked (intentional gap).

## Aliases



## Former ids
