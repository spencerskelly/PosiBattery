---
type: Object
subtype: circuit
id: OBJ-90028
uid: 20261005222810001skellyspencer
status: Draft
tags:
  - reusable-architecture
  - battery-monitoring
  - current
abstract: true
reuseScope: cross-product
supertypeOf:
  - "[[External Shunt Current Measurement Circuit]]"
  - "[[Hall-Effect Current Measurement Assembly]]"
  - "[[Shuntless Current Measurement Assembly]]"
  - "[[Split-Core Current Measurement Assembly]]"
performs:
  - "[[Measure Battery Current]]"
hasDesign:
  - "[[Current Sensing Design]]"
dependsOn:
  - "[[Control Circuit]]"
---

# Battery Current Measurement Circuit

## Definition

Reusable hardware family for measuring battery charge and discharge current and providing a controller-readable measurement.

## Notes

- This is the implementation family for [[Measure Battery Current]].
- The concrete sensing method remains a product-specific choice.
- [[Control Circuit]] provides acquisition and control infrastructure but is not the sensing element itself.
- [[PosiCharge PosiGuard]] is publicly documented as measuring battery current, so some member of this family is assigned at >=95% confidence; the exact sensor topology is unknown.

## Former ids
