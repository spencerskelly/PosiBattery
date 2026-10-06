---
type: Design
subtype:
id: DES-90936
uid: 20261006203500001skellyspencer
status: Draft
tags:
  - battery-monitoring
  - charger
  - communication
  - temperature
designOf:
  - "[[Battery-Charger Communication Firmware]]"
  - "[[PosiCharge BMID]]"
  - "[[EnerSys Wi-iQ]]"
  - "[[HOPPECKE trak collect]]"
  - "[[Fronius TagID]]"
  - "[[AMETEK Prestolite Power BID]]"
  - "[[AMETEK Prestolite Power BID with Ah Accumulator]]"
  - "[[Crown V-Force BMID]]"
realizes:
  - "[[Report Battery Temperature to Charger]]"
dependencyOf:
  - "[[Report Battery Temperature to Charger]]"
dependsOn:
  - "[[Battery Temperature Measurement Design]]"
  - "[[Battery-Charger Data Communication Design]]"
---

# Battery Temperature Reporting to Charger

## Definition

Reusable design for obtaining a battery-temperature value and communicating it to a compatible charger so the charger can adjust charging behavior.

## Notes

- This Design separates **temperature measurement** from **temperature communication**.
- [[Battery Temperature Measurement Design]] provides the controller-readable temperature value.
- [[Battery-Charger Data Communication Design]] provides the charger message/session behavior used to deliver that value.
- The temperature sensor location can be electrolyte-immersed, external, internal, or otherwise product-specific.
- Transport can be PLC, CAN, serial, wireless, or another charger link.
- The Design does not imply that the battery itself performs temperature compensation; it only provides temperature information to the charger.
- Message encoding, units, scaling, update rate, invalid-sensor handling, fallback behavior, and charger response remain product-specific.

## Former ids
