---
type: Object
subtype: firmware
id: OBJ-90109
uid: 20261006183500002skellyspencer
status: Draft
tags:
  - reusable-architecture
  - firmware
  - battery-monitoring
  - can
  - vehicle-control
reuseScope: cross-product
hasDesign:
  - "[[CAN Vehicle Operating Limit Command]]"
dependsOn:
  - "[[Control Circuit]]"
  - "[[CAN Communication Circuit]]"
performs:
  - "[[Command Vehicle Operating Limits over CAN]]"
partOf:
  - "[[EnerSys Wi-iQ]]"
---

# Vehicle Operating Limit Command Firmware

## Definition

Firmware that converts a battery-protection or operating-limit state into an OEM-specific CAN command or status message for the vehicle controller.

## Notes

- Allocation to [[EnerSys Wi-iQ]] is a **>=95% engineering-confidence implementation assumption** because the product explicitly sends OEM-specific operating-limit parameters over its optional CAN interface, while the internal firmware partition is not published.
- Candidate responsibilities include command-state generation, message packing, protocol selection, timeout/heartbeat handling, state persistence, and safe clearing of the operating limit.
- The exact battery condition that triggers a limit is product/OEM specific and is not asserted here.
- The truck-side receiving controller is not modeled as a product-specific part or Connection because the published Wi-iQ evidence does not identify a specific truck endpoint.

## Former ids
