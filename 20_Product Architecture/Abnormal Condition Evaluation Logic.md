---
type: Object
subtype: software
id: OBJ-90073
uid: 20261006175500005skellyspencer
status: Draft
tags:
  - reusable-architecture
  - battery-monitoring
  - alert
  - software
abstract: true
reuseScope: cross-product
hasDesign:
  - "[[Abnormal Condition Alert Design]]"
partOf:
  - "[[EnerSys Wi-iQ]]"
  - "[[EnerSys iQ Mini]]"
  - "[[Philadelphia Scientific eGO!Mini]]"
  - "[[Philadelphia Scientific eGO!pro]]"
performs:
  - "[[Alert on Abnormal Condition]]"
---

# Abnormal Condition Evaluation Logic

## Definition

Reusable logic that evaluates measurements, states, timers, histories, or diagnostic flags and determines when an abnormal condition should become an alert.

## Notes

- Typical responsibilities can include threshold comparison, hysteresis, time qualification, debounce, persistence, fault classification, severity, suppression, escalation and alert clearing.
- The inputs are product-specific and may come from voltage, current, temperature, electrolyte, state-of-charge, imbalance, equalization, communication or diagnostic functions.
- Allocation to [[EnerSys Wi-iQ]], [[EnerSys iQ Mini]], [[Philadelphia Scientific eGO!Mini]], and [[Philadelphia Scientific eGO!pro]] is **>=95% engineering confidence** because each explicitly evaluates one or more abnormal battery conditions, while the internal firmware/software partition is not published.
- Product allocation requires evidence or an explicit engineering-confidence assumption because public literature rarely exposes the internal firmware/software partition.

## Former ids
