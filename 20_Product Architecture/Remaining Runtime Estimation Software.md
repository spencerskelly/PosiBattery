---
type: Object
subtype: software
id: OBJ-90089
uid: 20261006201500002skellyspencer
status: Draft
tags:
  - reusable-architecture
  - software
  - battery-monitoring
  - analytics
  - runtime
reuseScope: cross-product
hasDesign:
  - "[[Remaining Runtime Estimation Design]]"
partOf:
  - "[[HOPPECKE trak collect]]"
  - "[[Linde 6-8 t Electric Counterbalance Forklifts]]"
performs:
  - "[[Estimate Remaining Run Time]]"
---

# Remaining Runtime Estimation Software

## Definition

Reusable software role that converts battery energy/state information and operating demand into an estimate of remaining useful operating time.

## Notes

- Allocation to [[HOPPECKE trak collect]] is **>=95% engineering confidence** because HOPPECKE explicitly publishes processed remaining-driving-time data and the device contains a DSP, measurement inputs, memory, and stored processed battery data.
- Allocation to [[Linde 6-8 t Electric Counterbalance Forklifts]] is **>=95% engineering confidence** because Linde explicitly states that the truck's energy-management system calculates projected remaining operating time.
- Exact inputs, filtering, update rate, capacity model, end-of-discharge criterion, and prediction algorithm are not published.
- This Object intentionally does not assume that the estimator uses SOC alone; runtime can be derived from energy, current/power history, duty cycle, capacity, or a combination.

## Former ids
