---
type: Use Case
subtype: what
id: UC-00042
uid: 20261005111800004skellyspencer
status: Draft
tags:
  - operational-use-case
  - bmid-product-use-case
participants:
  - "[[Truck OEM Integration Engineer]]"
  - "[[Dealer Service Technician]]"
  - "[[PosiCharge BMID]]"
realizedBy:
  - "[[Communicate with Charger]]"
  - "[[Communicate Battery State over CAN]]"
  - "[[Transmit Battery Data Wirelessly]]"
  - "[[Upload Battery Data to Cloud Portal]]"
givesRiseTo:
  - "[[Integrate the Battery with Truck and Charger Controls]]"
---

# Integrate a BMID with Charger Vehicle and Fleet Systems

## Definition

An integration engineer or qualified technician connects a supported BMID variant to the external charger, vehicle, or fleet-data interfaces required by the intended application.

## Notes

- Primary product family: [[PosiCharge BMID]].
- Integration is interface-specific and variant-specific; this use case does not generalize CAN, Bluetooth, cellular, LoRa, or cloud connectivity across all BMID generations.
- Charger, vehicle, battery BMS, and fleet/cloud systems remain external context.
- Completion: the intended supported external interface is connected and the required data exchange can occur.
- Product requirements created later must distinguish information exchange from control authority.

## Traceability

- Source need: [[Integrate the Battery with Truck and Charger Controls]].
- Related product functions: [[Communicate with Charger]], [[Communicate Battery State over CAN]], [[Transmit Battery Data Wirelessly]], [[Upload Battery Data to Cloud Portal]].

## Former ids
