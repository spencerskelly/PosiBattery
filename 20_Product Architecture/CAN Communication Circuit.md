---
type: Object
subtype: circuit
id: OBJ-90006
uid: 20261005212400006skellyspencer
status: Draft
tags:
  - reusable-architecture
  - communication
  - can
reuseScope: cross-product
subtypeOf:
  - "[[Wired Communication Circuit]]"
hasPart:
  - "[[CAN Transceiver]]"
hasDesign:
  - "[[CAN Interface]]"
partOf:
  - "[[Inventus Smart Battery Monitor SBM-01]]"
  - "[[Hyster Power Cellect]]"
  - "[[PosiCharge PosiGuard]]"
---

# CAN Communication Circuit

## Definition

CAN physical-layer communication circuit between a controller and an external CAN network.

## Notes

- A typical implementation includes a CAN transceiver plus controller CAN peripheral, termination/protection as required, and the product connector.
- The controller peripheral and exact protocol are not asserted here.
- Allocation to [[Hyster Power Cellect]] is an **>=95% engineering-confidence abstraction** from Hyster's explicit CAN link between the qualified battery and truck; the exact transceiver/controller placement inside the option package is not published.
- [[Inventus Smart Battery Monitor SBM-01]] explicitly supports J1939, CANopen and NMEA 2000 with an integrated 120 ohm termination resistor; [[CAN Communication Circuit]] is therefore allocated at **>=95% engineering confidence** while the exact transceiver IC/controller implementation remains unpublished.

## Former ids
