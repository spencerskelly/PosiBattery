---
type: Function
subtype:
id: FUNC-00124
uid: 20261004183000124skellyspencer
status: Draft
tags:
  - accessory-function
  - product-function
subtypeOf:
  - "[[Manage Fleet Use]]"
dependsOn:
  - "[[Charger Operator Interface Design]]"
  - "[[Wired Remote Charger Control Design]]"
performedBy:
  - "[[Crown V-HFM3 Wired Remote Control Kit]]"
  - "[[Wired Remote Charger Control Assembly]]"
  - "[[Remote Charger Control Panel]]"
  - "[[Remote Charger I-O Expansion Board]]"
realizes:
  - "[[Monitor and Manage Chargers and Batteries Across Sites]]"
realizedBy:
  - "[[Wired Remote Charger Control Design]]"
  - "[[Monitor and Manage Chargers and Batteries Across Sites]]"
---

# Control Charger from Remote Panel

## Definition

Let a person start, stop or check a charger from a remote control panel or wired remote instead of at the charger itself.

## Notes

- Added 2026-10-04 from the accessory marketed-features review. Product links only where a source states the behavior; no link means unknown.
- **Customer need (2026-10-04, analyst link, hypothesis):** realizes [[Monitor and Manage Chargers and Batteries Across Sites]]; chosen as the need whose problem statement the function addresses (see [[Research Change and Decision Tracker]]).
- **Depends on:** [[Charger Operator Interface Design]] (analyst inference (necessity), weak); rule and basis in [[Function Design Dependencies]].
- No Requirement is linked (intentional gap).
- **Sources** (product, evidence level, web page):
  - [[Crown V-HFM3 Wired Remote Control Kit]] (V): <https://www.crown.com/content/dam/crown/pdfs/en-us/brochures/products/vhfm3-chargers.pdf>

## Implementation Allocation

The reusable realization is [[Wired Remote Charger Control Design]].

[[Wired Remote Charger Control Assembly]] contains the remote operator panel and charger-side interface electronics. [[Remote Charger Control Panel]] provides operator input/status away from the charger enclosure, while [[Remote Charger I-O Expansion Board]] connects those remote controls to charger-side signals.

This is intentionally separate from [[Remote Charger Management Design]]: a wired remote panel is local physical control, not cloud/network management.

[[Crown V-HFM3 Wired Remote Control Kit]] provides unusually direct implementation evidence because Crown explicitly lists the wired remote, detachable cable, I/O expansion board, internal wiring loom, and DE9 mounting hardware.

## Aliases


## Former ids
