---
type: Function
subtype:
id: FUNC-00145
uid: 20261014132849733skellyspencer
status: Draft
tags:
  - software
  - product-function
  - fleet-software
subtypeOf:
  - "[[Keep Charging Available and Safe]]"
performedBy:
  - "[[Siemens depotfinity]]"
  - "[[PowerFlex X]]"
  - "[[Flip Turn Energy Management]]"
  - "[[Linde connect charger]]"
  - "[[Jungheinrich Active Load Management]]"
  - "[[Toyota Peak Load Management]]"
  - "[[Fronius PV Connect]]"
  - "[[ACT ACTenergy]]"
  - "[[Crown V-HFM3 Charger]]"
realizes:
  - "[[Charge Within Site Power Limits and Utility Costs]]"
---

# Balance Charging Power Across Site Capacity

## Definition

Share a limited site power supply among chargers, limit peak demand and shift charging to cheaper hours.

## Notes

- **Update 2026-10-14 (IB-221):** forklift-charger performers added from sources that state the behavior: [[Linde connect charger]] (power limits, time slots, priority), [[Jungheinrich Active Load Management]] (group power limit, priority by state of charge), [[Toyota Peak Load Management]] (shared power budget by priority), [[Fronius PV Connect]] (load balancing around PV output), [[ACT ACTenergy]] (shift from peak periods) and the charger [[Crown V-HFM3 Charger]] (Demand Response Management). All come from truck or charger makers' own systems; none is an OCPP or EV-fleet platform. Register: [[Forklift Charger Load Management Register]].
- Stated: depotfinity (load-managed depot, dynamic load management), PowerFlex X (Adaptive Load Management), Flip Turn (site, circuit and port limits, time-of-use shifting). Links are made only where a source states the behavior.
- No Requirement is linked.

## Aliases


## Former ids
