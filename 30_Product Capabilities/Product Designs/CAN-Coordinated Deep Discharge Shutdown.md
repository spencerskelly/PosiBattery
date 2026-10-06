---
type: Design
subtype:
id: DES-90923
uid: 20261006184500004skellyspencer
status: Draft
tags:
  - battery-protection
  - can
  - truck-control
  - deep-discharge
subtypeOf:
  - "[[Deep Discharge Protection Design]]"
designOf:
  - "[[Hyster Power Cellect]]"
  - "[[CAN Deep Discharge Shutdown Logic]]"
dependsOn:
  - "[[CAN Interface]]"
---

# CAN-Coordinated Deep Discharge Shutdown

## Definition

Deep-discharge protection in which battery discharge state is communicated over CAN and the vehicle performs a controlled shutdown or operating restriction.

## Notes

- [[Hyster Power Cellect]] is the verified implementation currently represented. Hyster states that Power Cellect uses CAN between a qualified battery and truck and triggers a controlled shutdown at complete discharge.
- The battery and truck share responsibility: the battery supplies state information, while the truck-side control architecture enforces the shutdown.
- Exact CAN messages, thresholds, sequence timing, fallback behavior, and restart criteria are not published.

## Former ids
