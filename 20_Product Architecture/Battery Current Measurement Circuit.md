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
hasDesign:
  - "[[Current Sensing Design]]"
dependsOn:
  - "[[Control Circuit]]"
partOf:
  - "[[AMETEK Prestolite Power BID with Ah Accumulator]]"
  - "[[Access Control Group CellTrac]]"
  - "[[EnerSys Wi-iQ]]"
  - "[[Exide Motion+ EasyMonitor]]"
  - "[[HOPPECKE trak collect]]"
  - "[[Power Designers PowerTrac DT3]]"
  - "[[Power Designers PowerTrac SP+]]"
  - "[[PosiCharge PosiGuard]]"
dependencyOf:
  - "[[Battery Current Acquisition Firmware]]"
performs:
  - "[[Measure Battery Current]]"
supertypeOf:
  - "[[Resistive Current Measurement Circuit]]"
  - "[[Magnetic Current Measurement Assembly]]"
  - "[[Clamp-On Current Measurement Assembly]]"
---

# Battery Current Measurement Circuit

## Definition

Reusable hardware family for measuring battery charge and discharge current and providing a controller-readable measurement.

## Notes

- This is the implementation family for [[Measure Battery Current]].
- The concrete sensing method remains a product-specific choice.
- [[Control Circuit]] provides acquisition and control infrastructure but is not the sensing element itself.
- [[PosiCharge PosiGuard]] is publicly documented as measuring battery current, so some member of this family is assigned at >=95% confidence; the exact sensor topology is unknown.
- The products added for amp-hour accumulation are allocated this generic circuit role at **>=95% engineering confidence** because they explicitly combine electronic current sensing/monitoring with accumulated Ah values; product-specific sensing Designs remain authoritative where known.

## Former ids
