---
type: Function
subtype:
id: FUNC-00132
uid: 20261004183008132skellyspencer
status: Draft
tags:
  - accessory-function
  - product-function
subtypeOf:
  - "[[Manage Fleet Use]]"
dependsOn:
  - "[[Impact Sensor]]"
  - "[[Impact-Triggered Vehicle Lockout Design]]"
performedBy:
  - "[[TLD Aircraft Safety Docking]]"
  - "[[Impact Lockout Decision Logic]]"
  - "[[Vehicle Enable Interlock]]"
realizes:
  - "[[Detect and Learn from Truck Impacts]]"
  - "[[Protect Aircraft and Ground Crew During Ground Operations]]"
realizedBy:
  - "[[Impact-Triggered Vehicle Lockout Design]]"
  - "[[Protect Aircraft and Ground Crew During Ground Operations]]"
---

# Lock Out Vehicle After Impact

## Definition

Lock the vehicle after a detected impact until an authorized person inspects and unlocks it.

## Notes

- Added 2026-10-04 from the accessory marketed-features review. Product links only where a source states the behavior; no link means unknown.
- **Customer need (2026-10-04, analyst link, hypothesis):** realizes [[Detect and Learn from Truck Impacts]], [[Protect Aircraft and Ground Crew During Ground Operations]]; chosen as the need whose problem statement the function addresses (see [[Research Change and Decision Tracker]]).
- **Depends on:** [[Impact Sensor]] (analyst inference (necessity), strong); rule and basis in [[Function Design Dependencies]].
- No Requirement is linked (intentional gap).
- **Sources** (product, evidence level, web page):
  - [[TLD Aircraft Safety Docking]] (V): <https://www.aerospecialties.com/product/tld-rbl/>

## Implementation Allocation

The reusable realization is [[Impact-Triggered Vehicle Lockout Design]].

[[Impact Sensor]] provides the detected impact or impact-severity input. [[Impact Lockout Decision Logic]] evaluates that event against the product's lockout policy and latches the locked state. [[Vehicle Enable Interlock]] applies the resulting vehicle-use inhibit.

This is intentionally separate from [[Detect and Record Impacts]]: detecting and logging an impact does not necessarily require disabling the vehicle.

[[TLD Aircraft Safety Docking]] is the verified concrete implementation. The published behavior states that impact strength is measured and the GSE is locked until a manager unlocks it after inspection.

## Aliases


## Former ids
