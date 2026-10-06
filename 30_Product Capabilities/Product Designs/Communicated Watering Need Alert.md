---
type: Design
subtype:
id: DES-90018
uid: 20261006152500003skellyspencer
status: Draft
tags:
  - battery-monitoring
  - design-characteristic
  - electrolyte
  - alert
  - communication
subtypeOf:
  - "[[Low Electrolyte Alert Design]]"
designOf:
  - "[[Crown V-Force BMID]]"
---

# Communicated Watering Need Alert

## Definition

Low-electrolyte alert communicated from a battery-mounted monitor to another device or system rather than relying only on a local battery indicator.

## Notes

- Crown states that [[Crown V-Force BMID]] detects low electrolyte and communicates the need to water.
- The retrieved Crown sources do not establish the transport mechanism or which charger-side display or indicator presents the message, so no CAN, Bluetooth, PLC, or local-output technology is inferred.
- This Design captures the verified alert-delivery behavior without asserting the internal communication implementation.

## Former ids
