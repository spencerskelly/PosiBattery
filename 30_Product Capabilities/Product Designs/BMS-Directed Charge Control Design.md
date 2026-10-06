---
type: Design
subtype:
id: DES-90954
uid: 20261006233500001skellyspencer
status: Draft
tags:
  - charger
  - bms
  - lithium
  - control
supertypeOf:
  - "[[CAN BMS-Directed Charging]]"
designOf:
  - "[[BMS-Directed Charge Control Firmware]]"
realizes:
  - "[[Charge Under BMS Control]]"
dependencyOf:
  - "[[Charge Under BMS Control]]"
dependsOn:
  - "[[Integrated Battery Management System]]"
  - "[[Charger Power Stage Design]]"
---

# BMS-Directed Charge Control Design

## Definition

Reusable charger-control design in which an external battery management system provides charge permission, voltage/current limits, targets, or stop conditions that govern charger output.

## Notes

- The BMS remains the source of battery-specific charge limits or permission, while the charger enforces those commands within its own safety and hardware limits.
- [[BMS-Directed Charge Control Firmware]] handles message/session validation, limit application, timeout behavior, and fallback.
- [[CAN BMS-Directed Charging]] captures the common implementation in which BMS commands are exchanged over CAN.
- The transport is not assumed to be CAN for every product; some architectures may use another wired or proprietary link.
- The charger power stage remains separate from the supervisory charge-control behavior.
- Exact command set, arbitration, heartbeat, timeout, fail-safe response, authentication, scaling, and charger/BMS ownership rules remain product-specific.

## Former ids
