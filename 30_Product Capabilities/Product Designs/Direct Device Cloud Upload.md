---
type: Design
subtype:
id: DES-90933
uid: 20261006200500002skellyspencer
status: Draft
tags:
  - battery-monitoring
  - cloud
  - upload
  - direct-connect
subtypeOf:
  - "[[Cloud Battery Data Upload Design]]"
designOf:
  - "[[Cloud Battery Data Upload Service]]"
---

# Direct Device Cloud Upload

## Definition

Cloud upload architecture in which the battery monitor, charger, or field device connects directly to a hosted service without a separately modeled local aggregation gateway.

## Notes

- The connection may use cellular, Wi-Fi, Ethernet, or another WAN-capable path.
- A product is assigned only when the available evidence establishes a direct field-device-to-cloud path.
- This Design does not imply a specific cloud API or transport protocol.

## Former ids
