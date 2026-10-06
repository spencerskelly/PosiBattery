---
type: Object
subtype: firmware
id: OBJ-90150
uid: 20261006232000004skellyspencer
status: Draft
tags:
  - reusable-architecture
  - firmware
  - charger
  - adaptive-charging
reuseScope: cross-product
hasDesign:
  - "[[Adaptive Charge Profile Control Design]]"
dependsOn:
  - "[[Control Circuit]]"
performs:
partOf:
  - "[[Fronius Selectiva 4.0]]"
  - "[[EnerSys IMPAQ Charger]]"
  - "[[Adapt Charge to Battery Condition]]"
---

# Adaptive Charge Profile Control Firmware

## Definition

Charger-control firmware that evaluates battery-condition inputs and updates charge-profile commands during the charging session.

## Notes

- Candidate responsibilities include battery-state evaluation, profile-phase control, current/voltage command generation, adaptive transitions, limit enforcement, fault fallback, and charge-completion decisions.
- The physical power conversion is provided by the charger power stage rather than this firmware Object.
- Internal software partitioning is generally unpublished and should be treated as an engineering abstraction unless a source identifies it directly.

## Former ids
