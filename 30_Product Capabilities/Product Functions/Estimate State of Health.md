---
type: Function
subtype:
id: FUNC-00008
uid: 20261002164202354skellyspencer
status: Draft
tags:
  - battery-monitoring
  - extra
  - product-function
subtypeOf:
  - "[[Sense Battery State]]"
performedBy:
performedBy:
  - "[[Raymond iWAREHOUSE]]"
  - "[[Battery State of Health Analytics Service]]"
  - "[[Capacity-Retention State of Health Estimator]]"
  - "[[Resistance-Trend State of Health Estimator]]"
dependsOn:
  - "[[Usage-History State of Health Analytics]]"
realizedBy:
  - "[[Usage-History State of Health Analytics]]"
---

# Estimate State of Health

## Definition

Estimate the battery's state of health.

## Notes

- The current product-backed SOH implementation in the modeled vault is Raymond iWAREHOUSE usage-history analytics.
- [[Inventus Smart Battery Monitor SBM-01]] was removed as a performer on 2026-10-06 because Inventus states that the monitor receives battery-system information and displays SOH rather than calculating it locally.
- [[Raymond iBattery]] was removed as the estimator itself: Raymond's published SOH chart and cycle-contributor analytics reside in the iWAREHOUSE software layer, while the battery module supplies the underlying measurements/history.
- Product links are made only where a source states the behavior; no link means unknown, not absent. Overview: [[Function Map]].
- No Requirement is linked: nothing here is a committed requirement, so model-health will show these Functions without satisfied Requirements. That gap is intentional.
- **Sources** (product, evidence level, web page):
  - [[Raymond iWAREHOUSE]] (V): <https://www.raymondcorp.com/-/media/raymond/literature/iwarehouse/ibatterysellsheetsipl1030_0513.pdf> <https://prod-cms-iwarehouseknows.raymondcorp.com/products/battery-monitoring>
- **Extra (round 30):** documented for one Raymond battery-management ecosystem; the verified implementation is [[Usage-History State of Health Analytics]] in iWAREHOUSE. Rule and caveats remain in [[Extra Functions Register]].

## Implementation Allocation

The only current product-backed implementation is [[Usage-History State of Health Analytics]] -> [[Battery State of Health Analytics Service]] within [[Raymond iWAREHOUSE]].

### Verified usage-history analytics path

Raymond's iBATTERY/iWAREHOUSE material identifies contributors to battery SOH including over- and under-discharge, water level and other critical factors, and identifies collected data including battery capacity/efficiency, current, temperature, SOC, water level and fault codes. This supports a multi-factor historical analytics implementation without exposing the actual formula or weighting.

[[Raymond iBattery]] supplies battery-side data to this analytics path but no longer directly performs the estimation Function.

### Candidate capacity-retention path

[[Capacity-Retention State of Health Estimator]] is an unallocated engineering option that estimates SOH from usable capacity relative to an initial/rated capacity baseline. It could use current integration, valid full/partial cycles, temperature normalization and stored baseline capacity.

### Candidate resistance-trend path

[[Resistance-Trend State of Health Estimator]] is an unallocated engineering option that estimates SOH from increasing internal resistance, impedance or voltage response under load. It does **not** imply electrochemical impedance spectroscopy unless dedicated excitation/measurement hardware is added.

### Inventus display boundary

Inventus defines battery SOH as battery capacity relative to initial capacity and states that PROformance batteries communicate SOH. [[Inventus Smart Battery Monitor SBM-01]] receives battery information over CAN and displays that SOH value. Because no PROformance battery product note currently exists in this vault, the underlying Inventus battery/BMS estimator is not added as a performer here.

## Aliases


## Former ids
