---
type: Design
subtype:
id: DES-90930
uid: 20261006194500001skellyspencer
status: Draft
tags:
  - battery-monitoring
  - communication
  - can
  - data
subtypeOf:
  - "[[Wired Interface Design]]"
designOf:
  - "[[CAN Battery State Communication Firmware]]"
realizes:
  - "[[Communicate Battery State over CAN]]"
dependencyOf:
  - "[[Communicate Battery State over CAN]]"
dependsOn:
  - "[[CAN Interface]]"
---

# CAN Battery State Communication Design

## Definition

Reusable design for packaging battery state, status, measurements, limits, or diagnostics into CAN messages and exchanging them with a vehicle, charger, display, or other controller.

## Notes

- [[CAN Interface]] provides the physical/protocol transport capability; this Design represents the battery-state application behavior carried over that interface.
- Published protocols vary by product. [[EnerSys Wi-iQ]] supports CANopen or J1939, while [[Inventus Smart Battery Monitor SBM-01]] supports J1939, CANopen and NMEA 2000. Other products expose CAN without publishing the application-layer message set.
- Candidate data includes state of charge, voltage, current, temperature, state of health, runtime, alarms, limits, charge requests, and diagnostics depending on product.
- The Design does not assert a common CAN database, PGN/object dictionary, message ID, scaling, update rate, heartbeat, timeout, or node-address scheme.

## Former ids
