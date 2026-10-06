---
type: Design
subtype:
id: DES-90934
uid: 20261006200500003skellyspencer
status: Draft
tags:
  - battery-monitoring
  - cloud
  - upload
  - gateway
subtypeOf:
  - "[[Cloud Battery Data Upload Design]]"
designOf:
  - "[[Battery Data Gateway Upload Service]]"
  - "[[Philadelphia Scientific eGO!gateway]]"
---

# Gateway-Mediated Cloud Upload

## Definition

Cloud upload architecture in which a local gateway collects battery data from one or more field devices and forwards it to a hosted portal or service.

## Notes

- [[Philadelphia Scientific eGO!gateway]] is the clearest verified example currently represented: it receives eGO! monitor data over Bluetooth and uploads it to batterymanagement.net over cellular.
- Other ecosystems may use a gateway, truck telematics unit, site collector, or similar intermediary, but those are allocated only when the source establishes the path.
- The gateway may buffer, transform, aggregate, or retry data, but those behaviors are not assumed unless evidenced.

## Former ids
