---
type: Info
subtype:
id: INFO-00137
uid: 20261002195812529skellyspencer
status: Draft
tags:
  - performance-metric
  - monitor
  - comparison
describes:
  - "[[Battery Monitoring and Identification Device]]"
  - "[[Communicate Battery State over CAN]]"
  - "[[CAN Interface]]"
  - "[[RS-232 and RS-485 Serial Interface]]"
  - "[[Infrared Data Port]]"
---

# Monitor Metric - Wired and Vehicle Interfaces

## Definition

Wired and Vehicle Interfaces: CAN, serial or proprietary bus interfaces.

## Notes

- **Code and class:** MM09; monitor metric. Unit or format: protocol.
- **Comparability rule:** Name the protocol (CANopen, J1939, battery bus); optional modules count as options.
- **Direction:** n/a.
- **Values on file (as stated in each product note; n/s means not stated):**
  - [[EnerSys Wi-iQ]]: CAN optional: CANopen CiA 418 or J1939
  - [[HOPPECKE trak collect]]: HOPPECKE Battery Bus 60 baud (CAN-LIN per news, C39)
  - [[Inventus Smart Battery Monitor SBM-01]]: CAN, auto baud 125 kbps to 1 Mbps
  - [[PosiCharge PosiGuard]]: Serial; CAN
  - [[Power Designers PowerTrac SP+]]: IR port; RS-232 and RS-485 options
- **Source rule:** the product note holds the source URL for each value; this note copies the value for comparison. If they differ, the product note wins and this note is fixed.
- **Gaps and to-do:** 5 product(s) have a value; document-based values to be added as documents are supplied.

## Aliases

- MM09
- Wired and Vehicle Interfaces

## Former ids
