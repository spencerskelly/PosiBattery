---
type: Object
subtype: electrical
id: OBJ-00111
uid: 20261002193402967skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - battery
  - canbus
  - hibernation
subtypeOf:
  - "[[Lithium-Ion Traction Battery]]"
performs:
  - "[[Communicate Battery State over CAN]]"
hasDesign:
  - "[[CAN Interface]]"
  - "[[Hibernation Mode]]"
  - "[[CAN Battery State Communication Design]]"
madeBy:
  - "[[Stryten Energy]]"
offeredWith:
  - "[[Stryten X-7 Charger]]"
  - "[[Stryten X-3 Charger]]"
---

# Stryten M-Series Li600 Battery

## Definition

Stryten LFP battery for Class I, II and III trucks with CANbus, remote monitoring and hibernation.

## Notes

- The release says Li600 is LFP, fully compatible with X-3 and X-7 chargers, with configurable CANbus protocol, remote monitoring, color touchscreen diagnostics, auto hibernation, and designed to meet UL2580 with certification in process. Source: Food Logistics (T2), retrieved 2026-10-02. <https://www.foodlogistics.com/sustainability/carbon-footprint/news/22891172/stryten-energy-lithium-batteries-for-cold-chain>
- **Design characteristics, with citations:**
  - [[CAN Interface]] (V): <https://www.foodlogistics.com/sustainability/carbon-footprint/news/22891172/stryten-energy-lithium-batteries-for-cold-chain>
  - [[Hibernation Mode]] (V): <https://www.foodlogistics.com/sustainability/carbon-footprint/news/22891172/stryten-energy-lithium-batteries-for-cold-chain>
- **Related products and how they differ (offeredWith):**
  - [[Stryten X-7 Charger]]: no difference stated in the sources.
  - [[Stryten X-3 Charger]]: no difference stated in the sources.
- **Functions performed, with citations (round 40, gap review 2026-10-03):**
  - [[Communicate Battery State over CAN]] (V): <https://www.foodlogistics.com/sustainability/carbon-footprint/news/22891172/stryten-energy-lithium-batteries-for-cold-chain>

- **Architecture realization — CAN battery state communication:** the product is allocated [[CAN Battery State Communication Design]] because published evidence establishes battery-state exchange over CAN or a CAN-based vehicle/battery interface. Message identifiers, signal maps, update rates, and protocol details remain product-specific.

## Aliases

- Li600


## Former ids
