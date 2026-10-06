---
type: Function
subtype:
id: FUNC-00122
uid: 20261003203338369skellyspencer
status: Draft
tags:
  - charger-function
  - product-function
subtypeOf:
  - "[[Control Charge Profile]]"
performedBy:
  - "[[EnerSys IMPAQ Charger]]"
  - "[[Fronius Selectiva 4.0]]"
  - "[[Adaptive Charge Profile Control Firmware]]"
realizes:
dependsOn:
  - "[[Adaptive Charge Profile Control Design]]"
realizedBy:
  - "[[Adaptive Charge Profile Control Design]]"
  - "[[Charge Each Battery Correctly for Its Chemistry and Condition]]"
---

# Adapt Charge to Battery Condition

## Definition

Change the charging current or characteristic during the charge according to what the charger measures or learns about the battery, such as internal resistance, temperature or state of charge.

## Notes

- Behavior found in product descriptions. Product links only where a source states the behavior.
- No Requirement is linked (intentional gap).
- **Sources** (product, evidence level, web page):
  - [[Fronius Selectiva 4.0]] (V): <https://www.fronius.com/en/perfect-charging/our-solutions/technologies/ri-charging-process>
  - [[EnerSys IMPAQ Charger]] (V): <https://integration.enersys.com/49bcd9/globalassets/documents/product-documentation/impaq/emea/emea-en-om-impaq-1022.pdf>

## Implementation Allocation

The reusable realization is [[Adaptive Charge Profile Control Design]] -> [[Adaptive Charge Profile Control Firmware]].

[[Charger Power Stage Design]] remains the electrical-output implementation underneath the controller; the adaptive firmware decides how the requested charge profile changes based on battery condition.

Two evidence-specific strategies are currently modeled:

- [[Ri-Based Adaptive Charging]] for [[Fronius Selectiva 4.0]], where Fronius explicitly states that effective internal resistance, affected by age, temperature, and state of charge, is used to adapt the charging characteristic.
- [[Diagnostic-Loop Adaptive Charging]] for [[EnerSys IMPAQ Charger]], where EnerSys describes a heavy-duty profile that diagnoses battery status or capacity through continuous current loops.

The proprietary control laws and firmware partitioning remain unpublished.

## Aliases


## Former ids
