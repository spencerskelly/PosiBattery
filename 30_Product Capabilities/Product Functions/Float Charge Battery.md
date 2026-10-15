---
type: Function
subtype:
id: FUNC-00108
uid: 20261003163422025skellyspencer
status: Draft
tags:
  - extra
  - product-function
  - truck-function
subtypeOf:
  - "[[Control Charge Profile]]"
performedBy:
  - "[[PosiCharge ProCore Solo]]"
realizes:
  - "[[Prevent Battery Abuse and Premature Replacement]]"
dependsOn:
  - "[[Voltage-Triggered Ready-State Top-Up]]"
---

# Float Charge Battery

## Definition

Hold the battery at full charge with a float charge.

## Notes

- **Solution link added 2026-10-14 (owner statement, U):** depends on [[Voltage-Triggered Ready-State Top-Up]]. The owner describes a voltage threshold that restarts charging to a ready-state voltage, not a continuous constant-voltage float (C274).
- **Need served (analyst reasoning, 2026-10-14):** [[Prevent Battery Abuse and Premature Replacement]]. Analyst reasoning: a battery left idle between uses is held full instead of self-discharging; the PosiCharge sheet lists the float mode but states no customer problem. Customer work: parking a truck or spare battery between shifts.
- Behavior found in product descriptions. Product links only where a source states the behavior.
- No Requirement is linked (intentional gap).
- **Sources** (product, evidence level, web page):
  - [[PosiCharge ProCore Solo]] (V): <https://posicharge.com/wp-content/uploads/2026/02/5x7_ProCore-Solo-1.pdf>
- **Extra (round 30):** documented for 1 of 18 charger maker groups (6 percent), delivered by devices or software (accessory and software notes); rule and caveats in [[Extra Functions Register]].

## Aliases


## Former ids
