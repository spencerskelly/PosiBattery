---
type: Object
subtype: component
id: OBJ-90065
uid: 20261006155500006skellyspencer
status: Draft
tags:
  - reusable-architecture
  - local-status
  - gauge
reuseScope: cross-product
hasDesign:
  - "[[Battery Status Gauge]]"
partOf:
  - "[[Inventus Smart Battery Monitor SBM-01]]"
  - "[[Access Control Group CellVue]]"
performs:
  - "[[Display Battery Status to Operator]]"
  - "[[Indicate Battery Status Locally]]"
---

# Battery Status Gauge Display Element

## Definition

Technology-neutral local display element used by a battery-status gauge.

## Notes

- [[Access Control Group CellVue]] is described publicly as a real-time battery gauge.
- [[Inventus Smart Battery Monitor SBM-01]] is a 52 mm panel monitor that displays battery-supplied SOC, SOH, runtime, voltage and fault information.
- The source does not disclose whether its visible element is LCD, LED, analog, segmented, graphical, or otherwise; this component deliberately preserves that uncertainty.
- The commercial CellVue product remains the system-level Object; this note captures the reusable display-element role within such a gauge.

## Former ids
