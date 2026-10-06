---
type: Object
subtype: software
id: OBJ-90108
uid: 20261006182000006skellyspencer
status: Draft
tags:
  - reusable-architecture
  - software
  - battery-monitoring
  - analytics
  - replacement
hasDesign:
  - "[[Fleet-Service Replacement Forecasting]]"
dependsOn:
  - "[[Energywith withBMS BMU]]"
performs:
  - "[[Predict Battery Replacement Timing]]"
---

# Energywith withBMS Analytics Service

## Definition

Energywith service-platform analytics role that evaluates BMU data for battery degradation and replacement timing.

## Notes

- Energywith states that the battery-mounted [[Energywith withBMS BMU]] measures battery condition and transfers data through an IoT gateway to a service platform for operating-condition visualization and degradation/replacement analysis.
- This Object captures the published software/service locus without inventing a separate commercial product name.
- The internal forecast algorithm, training data, thresholds, weighting, update cadence, and confidence model are not published.
- Source: <https://www.energy-with.com/en/solutions/forklift-battery-monitoring/>

## Former ids
