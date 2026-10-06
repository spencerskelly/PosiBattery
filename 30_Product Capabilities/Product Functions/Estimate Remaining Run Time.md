---
type: Function
subtype:
id: FUNC-00009
uid: 20261002164202355skellyspencer
status: Draft
tags:
  - battery-monitoring
  - extra
  - product-function
subtypeOf:
  - "[[Sense Battery State]]"
performedBy:
  - "[[Remaining Runtime Estimation Software]]"
  - "[[HOPPECKE trak collect]]"
  - "[[Linde 6-8 t Electric Counterbalance Forklifts]]"
dependsOn:
  - "[[Remaining Runtime Estimation Design]]"
realizedBy:
  - "[[Remaining Runtime Estimation Design]]"
realizes:
  - "[[Know Battery State Before and During the Shift]]"
  - "[[Start a Shift and Confirm Vehicle Energy Readiness]]"
---

# Estimate Remaining Run Time

## Definition

Estimate the working time remaining at the present usage.

## Notes

- Verified calculation is currently assigned to [[HOPPECKE trak collect]] and the Linde truck energy-management system.
- [[EnerSys Truck iQ]] and [[Inventus Smart Battery Monitor SBM-01]] were removed as estimators on 2026-10-06 because their sources establish that they read/report battery-system values, not that they calculate remaining runtime locally.
- Product links are made only where a source states the behavior; no link means unknown, not absent. Overview: [[Function Map]].
- No Requirement is linked: nothing here is a committed requirement, so model-health will show these Functions without satisfied Requirements. That gap is intentional.
- **Sources** (product, evidence level, web page):
  - [[HOPPECKE trak collect]] (V): <https://www.hoppecke.com/uk/news/improved-battery-management-with-trak-collect/>
  - [[Linde 6-8 t Electric Counterbalance Forklifts]] (V): <https://expoproduction.thelogisticsworld.com/wp-content/themes/theme-summitexpo/directorio/assets/fichas/d0631ac8-a3f8-4b21-8640-bf6f41154ae8.pdf>
- **Extra (round 30):** documented in one battery-monitor ecosystem and one truck energy-management implementation; the reusable realization is [[Remaining Runtime Estimation Design]]. Rule and caveats remain in [[Extra Functions Register]].

## Implementation Allocation

The reusable realization is [[Remaining Runtime Estimation Design]], implemented by [[Remaining Runtime Estimation Software]].

### Verified calculation paths

- **[[HOPPECKE trak collect]]:** HOPPECKE publishes remaining-driving-time information as processed battery data. The device measures battery voltage, current, temperature and electrolyte state, stores processed data, and contains a DSP. [[Remaining Runtime Estimation Software]] is therefore allocated at **>=95% engineering confidence**; the exact prediction algorithm is not published.
- **[[Linde 6-8 t Electric Counterbalance Forklifts]]:** Linde states that its energy-management system automatically calculates projected remaining operating time. The software realization is verified at the system level; the exact inputs and algorithm are not published.

### Presentation-only endpoints

- **[[EnerSys Truck iQ]]:** reads Wi-iQ battery data over BLE and **shows** remaining work time. It remains a performer of [[Display Battery Status to Operator]], not this estimation Function.
- **[[Inventus Smart Battery Monitor SBM-01]]:** receives battery-system data over CAN and displays runtime remaining. The underlying battery/BMS estimator is outside the currently modeled product set, so SBM-01 remains a display endpoint.

### Algorithm boundary

Potential implementations include recent-average power/current projection, filtered consumption-rate estimation, duty-cycle prediction, or model-based/adaptive runtime prediction. No one of these is assigned to a current product without stronger evidence.

## Aliases


## Former ids
