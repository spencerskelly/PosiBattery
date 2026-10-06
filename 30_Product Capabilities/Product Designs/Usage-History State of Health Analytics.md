---
type: Design
subtype:
id: DES-90034
uid: 20261006195500001skellyspencer
status: Draft
tags:
  - battery-monitoring
  - design-characteristic
  - analytics
  - state-of-health
subtypeOf:
  - "[[Data Handling Design]]"
designOf:
  - "[[Raymond iWAREHOUSE]]"
  - "[[Battery State of Health Analytics Service]]"
realizes:
  - "[[Estimate State of Health]]"
dependencyOf:
  - "[[Estimate State of Health]]"
---

# Usage-History State of Health Analytics

## Definition

State-of-health estimation based on accumulated battery usage, maintenance, capacity/efficiency, alert, and operating-history data.

## Notes

- [[Raymond iWAREHOUSE]] is the verified implementation currently represented.
- Raymond states that the iBATTERY / iWAREHOUSE battery cycles detail chart lists contributors to state of health including over- and under-discharge, water level and other critical factors, and separately lists battery capacity/efficiency, temperature, state of charge, current, water level and fault codes among collected data.
- The source supports a **multi-factor usage-history analytics** implementation but does not publish the weighting, formula, thresholds, statistical model, or whether measured capacity is the dominant term.
- This Design does not imply electrochemical impedance, direct internal-resistance measurement, or a laboratory capacity test.

## Former ids
