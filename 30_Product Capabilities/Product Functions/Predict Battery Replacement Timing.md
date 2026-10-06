---
type: Function
subtype:
id: FUNC-00130
uid: 20261004183006130skellyspencer
status: Draft
tags:
  - accessory-function
  - product-function
subtypeOf:
  - "[[Inform Users of Battery Condition]]"
dependsOn:
  - "[[Battery Replacement Timing Prediction Design]]"
performedBy:
  - "[[PosiCharge Battery Rx]]"
  - "[[Philadelphia Scientific eGO!c]]"
  - "[[Power Designers PowerTrac 3]]"
  - "[[Battery Replacement Prediction Firmware]]"
  - "[[Battery Replacement Forecasting Service]]"
  - "[[Energywith withBMS Analytics Service]]"
realizes:
realizedBy:
  - "[[Battery Replacement Timing Prediction Design]]"
  - "[[Prevent Battery Abuse and Premature Replacement]]"
---

# Predict Battery Replacement Timing

## Definition

Estimate when a battery will need replacing, from its usage and degradation history.

## Notes

- Added 2026-10-04 from the accessory marketed-features review. Product links only where a source states the behavior; no link means unknown.
- **Customer need (2026-10-04, analyst link, hypothesis):** realizes [[Prevent Battery Abuse and Premature Replacement]]; chosen as the need whose problem statement the function addresses (see [[Research Change and Decision Tracker]]).
- **Depends on:** [[Battery Replacement Timing Prediction Design]] (implementation review, strong); rule and basis in [[Function Design Dependencies]].
- No Requirement is linked (intentional gap).
- **Sources** (product, evidence level, web page):
  - [[PosiCharge Battery Rx]] (V): <https://www.posicharge.com/source/PDF/BatteryRx.pdf>
  - [[Energywith withBMS BMU]] (V): <https://www.energy-with.com/en/solutions/forklift-battery-monitoring/>
  - [[Philadelphia Scientific eGO!c]] (V): <https://www.ipesearch.co.uk/iOT-technology-for-batteries>
  - [[Power Designers PowerTrac 3]] (V): <https://powerdesignerssibex.com/wp-content/uploads/2024/04/PDS-PT-PT3_PowerTrac-3.pdf>

## Implementation Allocation

The reusable realization is [[Battery Replacement Timing Prediction Design]]. This Function forecasts a future replacement decision; it is therefore modeled separately from [[Estimate State of Health]], which estimates present battery condition.

### Device-resident alternative

[[Device-Resident Replacement Forecasting]] -> [[Battery Replacement Prediction Firmware]]

A battery monitor can project replacement timing from locally retained degradation and usage history.

### Fleet/service alternative

[[Fleet-Service Replacement Forecasting]] -> [[Battery Replacement Forecasting Service]]

A backend can combine uploaded history, maintenance data, degradation trends, and fleet context to produce a replacement forecast.

### Product allocation

[[PosiCharge Battery Rx]], [[Philadelphia Scientific eGO!c]], and [[Power Designers PowerTrac 3]] are allocated only the generic prediction Design because the published material states life-expectancy/replacement prediction without establishing where the model executes.

For Energywith, the source is more specific: the battery-mounted [[Energywith withBMS BMU]] collects and forwards data, while [[Energywith withBMS Analytics Service]] performs degradation/replacement analysis. The BMU therefore no longer directly performs this Function.

## Aliases


## Former ids
