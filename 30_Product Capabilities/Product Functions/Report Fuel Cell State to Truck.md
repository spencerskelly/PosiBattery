---
type: Function
subtype:
id: FUNC-00060
uid: 20261003090225555skellyspencer
status: Draft
tags:
  - truck-function
  - product-function
subtypeOf:
  - "[[Supply Vehicle Energy Without Charging]]"
performedBy:
  - "[[Plug Power GenDrive]]"
realizes:
  - "[[Know Battery State Before and During the Shift]]"
---

# Report Fuel Cell State to Truck

## Definition

Tell the truck the fuel cell stack and system state and remaining fuel.

## Notes

- **Need served (analyst reasoning, 2026-10-14):** [[Know Battery State Before and During the Shift]]. Plug Power says GenDrive communicates with the truck to monitor stack and system performance and has a fuel level gauge (source: [[Plug Power GenDrive]]). The fuel cell takes the battery's place, so the same question (how much energy is left) applies. Customer work: starting a shift and checking energy.
- Truck-side behavior found in product descriptions. Product links only where a source states the behavior; no link means unknown.
- No Requirement is linked (intentional gap).
- **Sources** (product, evidence level, web page):
  - [[Plug Power GenDrive]] (V): <https://plugpower.com/wp-content/uploads/2014/12/GenDrive-Series-1000-Spec-Sheet.pdf>

## Aliases


## Former ids
