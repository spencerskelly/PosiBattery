---
type: Design
subtype:
id: DES-90935
uid: 20261006202000001skellyspencer
status: Draft
tags:
  - battery-monitoring
  - charger
  - communication
  - data
designOf:
  - "[[Battery-Charger Communication Firmware]]"
  - "[[EnerSys NexSys iON Battery]]"
  - "[[Toyota Lithium-Ion 5-35 Battery Series]]"
  - "[[PosiCharge BMID]]"
  - "[[PosiCharge Battery Rx]]"
  - "[[PosiCharge PosiGuard]]"
  - "[[AMETEK Prestolite Power TruBid]]"
  - "[[AMETEK Prestolite Power WBID]]"
  - "[[Advanced Charging Technologies BATTview]]"
  - "[[EnerSys Wi-iQ]]"
  - "[[HOPPECKE trak collect]]"
  - "[[Power Designers PowerTrac 3]]"
  - "[[Power Designers PowerTrac SP+]]"
  - "[[Stryten inCOMMAND]]"
  - "[[Exide Solition Light Traction Battery]]"
  - "[[Crown V-Force BMID]]"
realizes:
  - "[[Communicate with Charger]]"
dependencyOf:
  - "[[Battery Temperature Reporting to Charger]]"
  - "[[Communicate with Charger]]"
supertypeOf:
  - "[[Battery Identification and Charger Communication Software Design]]"
  - "[[Communicate with Charger]]"
---

# Battery-Charger Data Communication Design

## Definition

Reusable design for exchanging battery state, identity, measurements, limits, charge requests, configuration, or status with a compatible charger over a selected communication interface.

## Notes

- This Design is broader than [[Battery Identification and Charger Communication Software Design]], which is focused on identity and charge-configuration exchange.
- The communication transport is intentionally separate. Products may use [[DC-Cable Power-Line Communication]], [[CAN Interface]], serial, Bluetooth/BLE, ZigBee, proprietary RF, or another interface.
- Candidate exchanged data includes battery identity, nominal voltage, capacity, temperature, state of charge, current, fault state, requested charge limits, charge status, and profile selection depending on product.
- Message schema, directionality, handshake, update rate, authentication, charger ownership, and fallback behavior remain product-specific.

## Former ids
