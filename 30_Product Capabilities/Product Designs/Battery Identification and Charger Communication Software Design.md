---
type: Design
subtype:
id: DES-90001
uid: 20261005212400018skellyspencer
status: Draft
tags:
  - product-design
  - communication
  - software
designOf:
  - "[[Battery Identification and Charger Communication Firmware]]"
appliesTo:
  - "[[PosiCharge BMID]]"
  - "[[PosiCharge PosiGuard]]"
dependsOn:
  - "[[Control Circuit]]"
  - "[[Communication Interface Circuit]]"
realizes:
  - "[[Identify Battery to Charger]]"
---

# Battery Identification and Charger Communication Software Design

## Definition

Software design that retrieves battery identity and charge-configuration information and provides it to a compatible charger through a selected wired or wireless communication interface.

## Notes

- Primary realization for [[Identify Battery to Charger]].
- The design is interface-agnostic at this level. A product or variant can select CAN, serial, BLE, LoRa, Wi-Fi, custom RF, or another supported concrete communication implementation.
- [[Wired Interface Design]] and [[Wireless Interface Design]] are solution families; their descendants model the physical communication method.
- **PosiCharge BMID assumption:** applying this software design to the BMID family is a >=95% engineering inference from the documented combination of stored identity/profile/history plus charger communication. No source currently states the internal firmware architecture.
- **PosiCharge PosiGuard assumption:** applying the same software-design concept to PosiGuard is a >=95% inference because PosiGuard is identified as a BMID-family device and publicly documents serial, CAN, Bluetooth, and optional LoRa communications. The exact charger-identification message path is not published.

## Former ids
