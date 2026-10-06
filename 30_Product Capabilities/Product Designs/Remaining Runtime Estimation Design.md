---
type: Design
subtype:
id: DES-90035
uid: 20261006201500001skellyspencer
status: Draft
tags:
  - general-design
  - design-characteristic
  - battery-monitoring
  - analytics
  - runtime
subtypeOf:
  - "[[Data Handling Design]]"
realizes:
  - "[[Estimate Remaining Run Time]]"
dependencyOf:
  - "[[Estimate Remaining Run Time]]"
designOf:
  - "[[Remaining Runtime Estimation Software]]"
  - "[[HOPPECKE trak collect]]"
  - "[[Linde 6-8 t Electric Counterbalance Forklifts]]"
---

# Remaining Runtime Estimation Design

## Definition

Software/algorithm design for estimating how much useful operating time remains before the battery reaches a limiting state.

## Notes

- [[HOPPECKE trak collect]] and [[Linde 6-8 t Electric Counterbalance Forklifts]] are the current product-backed implementations.
- HOPPECKE explicitly publishes remaining driving time as processed battery information; Linde explicitly states that its energy-management system calculates projected remaining operating time.
- The sources do not disclose the exact algorithm.
- Plausible inputs include available energy or SOC, recent current/power consumption, battery capacity, temperature, duty cycle, vehicle operating state, and stored history, but no particular input set is asserted for either product.
- Possible algorithm classes include recent-average-load projection, filtered consumption-rate estimation, duty-cycle models, or adaptive/model-based prediction. These remain implementation options until a product source identifies one.

## Former ids
