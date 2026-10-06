---
type: Function
subtype:
id: FUNC-00054
uid: 20261003090225549skellyspencer
status: Draft
tags:
  - extra
  - product-function
  - truck-function
subtypeOf:
  - "[[Protect Battery from Harm]]"
performedBy:
  - "[[EnerSys NexSys iON Battery]]"
  - "[[Crown RC 5700 Series]]"
  - "[[Hyster Power Cellect]]"
  - "[[BMS Discharge Protection Logic]]"
  - "[[Battery Discharge Interlock Logic]]"
  - "[[CAN Deep Discharge Shutdown Logic]]"
realizes:
dependsOn:
  - "[[Deep Discharge Protection Design]]"
realizedBy:
  - "[[Deep Discharge Protection Design]]"
  - "[[Prevent Battery Abuse and Premature Replacement]]"
---

# Protect Battery from Deep Discharge

## Definition

Limit or stop truck operation when the battery reaches full discharge to protect it.

## Notes

- Truck-side behavior found in product descriptions. Product links only where a source states the behavior; no link means unknown.
- No Requirement is linked (intentional gap).
- **Sources** (product, evidence level, web page):
  - [[Hyster Power Cellect]] (V): <https://www.inddist.com/new-products/material-handling-storage/product/22885612/hyster-power-cellect-provides-forklift-battery-freedom>
  - [[Crown RC 5700 Series]] (V): <https://www.crown.com/content/dam/crown/pdfs/en-uk/specs/forklift-rc5700-spec-GB.pdf>
  - [[EnerSys NexSys iON Battery]] (V): <https://www.enersys.com/en/about-us/news/enersys_now_offering_lithium_ion_li_ion_battery_to_global_portfolio_of_power_solutions/>
- **Extra (round 30):** documented for 2 of 10 truck maker groups (20 percent); the reusable realization family is now [[Deep Discharge Protection Design]]. Rule and caveats remain in [[Extra Functions Register]].

## Implementation Allocation

The reusable realization is [[Deep Discharge Protection Design]], with three distinct architectures represented in current products.

### Battery-resident BMS protection

[[BMS Discharge Limitation]] -> [[BMS Discharge Protection Logic]]

[[EnerSys NexSys iON Battery]] explicitly uses an integrated BMS that performs discharge-voltage limitation. The public source establishes the protection locus but not whether the final enforcement uses internal contactors, a current-limit request to the truck, or both.

### Truck-side discharge interlock

[[Truck Battery Discharge Interlock]] -> [[Battery Discharge Interlock Logic]]

[[Crown RC 5700 Series]] explicitly provides a battery-discharge indicator with lift interrupt and re-key. The internal truck controller/software partition is not published, so the reusable interlock logic is allocated at **>=95% engineering confidence**.

### CAN-coordinated shutdown

[[CAN-Coordinated Deep Discharge Shutdown]] -> [[CAN Deep Discharge Shutdown Logic]]

[[Hyster Power Cellect]] explicitly uses CAN between a qualified battery and truck and performs a controlled shutdown at complete discharge. The software partition between the Power Cellect package and truck controller is not disclosed.

These architectures all protect against deep discharge, but they differ materially in where the decision is made and where enforcement occurs. They are therefore modeled as sibling Designs rather than as one implementation.

## Aliases


## Former ids
