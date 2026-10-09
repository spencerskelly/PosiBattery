---
type: Function
subtype:
id: FUNC-00042
uid: 20261002211134433skellyspencer
status: Draft
tags:
  - charger
  - extra
  - product-function
subtypeOf:
  - "[[Control Charge Profile]]"
performedBy:
  - "[[Power Designers PowerTrac 3]]"
  - "[[Missed Equalization Recovery Firmware]]"
  - "[[Power Designers REVOLUTION X]]"
dependsOn:
  - "[[Missed Equalization Recovery Design]]"
realizedBy:
  - "[[Missed Equalization Recovery Design]]"
  - "[[Power Designers REVOLUTION X]]"
---

# Complete Missed Equalization Automatically

## Definition

Complete an equalization that was missed, automatically, during the next charge cycle and until finished.

## Notes

- Found in the documents absorbed in round 11. Product links only where a source states the behavior; no link means unknown.
- No Requirement is linked (intentional gap).
- **Sources** (product, evidence level, web page):
  - [[Power Designers REVOLUTION X]] (V): <https://powerdesignerssibex.com/wp-content/uploads/2024/04/PDS-PT-PT3_PowerTrac-3.pdf> (also [[Document - Power Designers PowerTrac 3 Specification (PDS-PT3 11-2025)]])
  - [[Power Designers PowerTrac 3]] (V): <https://powerdesignerssibex.com/wp-content/uploads/2024/04/PDS-PT-PT3_PowerTrac-3.pdf> (also [[Document - Power Designers PowerTrac 3 Specification (PDS-PT3 11-2025)]])
- **Extra (round 30):** documented for 0 of 21 battery maker groups (0 percent); the reusable realization is now [[Missed Equalization Recovery Design]].

## Implementation Allocation

The reusable realization is [[Missed Equalization Recovery Design]] -> [[Missed Equalization Recovery Firmware]].

[[Equalization Event Tracking Design]] provides the state/history needed to determine whether a required equalization was actually completed. The recovery firmware preserves a pending equalization obligation and carries it into a later eligible charging session until completion is confirmed.

This is distinct from [[Equalize Battery on Schedule]]: a normal schedule says when equalization should occur; this Function specifically recovers an equalization that was missed.

[[Power Designers PowerTrac 3]] and [[Power Designers REVOLUTION X]] are the verified implementations currently represented. The exact software partition, persistence mechanism, retry rules, and completion criteria are not published.

## Aliases


## Former ids
