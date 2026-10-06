---
type: Design
subtype:
id: DES-90958
uid: 20261006234000003skellyspencer
status: Draft
tags:
  - charger
  - temperature
  - communication
subtypeOf:
  - "[[Temperature-Compensated Charge Control Design]]"
dependsOn:
  - "[[Battery Temperature Reporting to Charger]]"
---

# Communicated Battery Temperature Charge Compensation

## Definition

Temperature-compensated charging in which a charger receives battery temperature from a battery monitor, identification device, or BMS over a communication link and uses it to adjust the charge profile.

## Notes

- This path reuses [[Battery Temperature Reporting to Charger]] for the battery-side measurement and communication behavior.
- Examples include systems using BMID, TagID, Wi-iQ, or other battery-mounted monitors that report temperature to a compatible charger.
- The transport can be PLC, CAN, serial, wireless, or another charger link.
- Exact message format, compensation algorithm, update cadence, invalid-data handling, and fallback remain product-specific.

## Former ids
