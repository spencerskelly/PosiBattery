---
type: Design
subtype:
id: DES-90919
uid: 20261006183500001skellyspencer
status: Draft
tags:
  - battery-monitoring
  - design-characteristic
  - can
  - vehicle-control
  - command
subtypeOf:
  - "[[Wired Interface Design]]"
designOf:
  - "[[EnerSys Wi-iQ]]"
  - "[[Vehicle Operating Limit Command Firmware]]"
realizes:
  - "[[Command Vehicle Operating Limits over CAN]]"
dependencyOf:
  - "[[Command Vehicle Operating Limits over CAN]]"
dependsOn:
  - "[[CAN Interface]]"
---

# CAN Vehicle Operating Limit Command

## Definition

Battery-monitoring control behavior that sends a vehicle operating-limit, lift-inhibit, or reduced-operation command over CAN using an OEM-specific CAN protocol.

## Notes

- [[EnerSys Wi-iQ]] is the verified implementation currently represented. The Wi-iQ4 manual states that the optional CAN module supports communication with trucks/AGVs and can transmit OEM-specific parameters used to limit vehicle operation.
- The Design intentionally separates the command behavior from the transport. [[CAN Interface]] provides the CAN communication capability; [[Vehicle Operating Limit Command Firmware]] generates and transmits the control state.
- Exact command identifiers, J1939/CANopen objects, OEM protocol, thresholds, debounce, fault handling, and truck response are not published.
- This Design does not imply that Wi-iQ directly switches traction or lift power. The truck-side controller remains responsible for enforcing the received limit.

## Former ids
