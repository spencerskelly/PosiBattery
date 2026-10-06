---
type: Object
subtype: circuit
id: OBJ-90096
uid: 20261006171500005skellyspencer
status: Draft
tags:
  - reusable-architecture
  - communication
  - wired
  - power-line
reuseScope: cross-product
subtypeOf:
  - "[[Wired Communication Circuit]]"
hasDesign:
  - "[[DC-Cable Power-Line Communication]]"
partOf:
  - "[[Raymond iBattery]]"
dependencyOf:
  - "[[Battery Weight Verification Firmware]]"
---

# Power-Line Communication Circuit

## Definition

Wired communication circuit that exchanges battery data with a vehicle or charger over the battery power cable without a separate data connector.

## Notes

- Raymond's battery sensor module patent explicitly identifies a power-line communication circuit used for bidirectional communication with the vehicle controller and charging equipment.
- The modulation, coupling network, carrier frequency, transceiver IC, isolation, and protocol are not disclosed in the retrieved source and are therefore left open.
- This Object is a concrete hardware realization of [[DC-Cable Power-Line Communication]].
- Source: <https://patents.google.com/patent/CA2733079A1/en>

## Former ids
