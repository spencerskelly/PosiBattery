---
type: Design
subtype:
id: DES-90029
uid: 20261006183500002skellyspencer
status: Draft
tags:
  - battery-monitoring
  - design-characteristic
  - voltage
  - imbalance
subtypeOf:
  - "[[Voltage Imbalance Detection Design]]"
dependsOn:
  - "[[Mid-Battery Differential Voltage Measurement]]"
designOf:
  - "[[EnerSys Wi-iQ]]"
  - "[[Exide Motion+ EasyMonitor]]"
  - "[[Voltage Imbalance Evaluation Firmware]]"
  - "[[Voltage Imbalance Comparator Circuit]]"
---

# Midpoint Voltage Symmetry Detection

## Definition

Voltage-imbalance detection that compares overall battery voltage with a midpoint or balance-tap measurement to determine whether the two battery halves are electrically symmetric.

## Notes

- [[EnerSys Wi-iQ]] explicitly measures overall and half-battery voltage and uses a balance wire.
- [[Exide Motion+ EasyMonitor]] explicitly uses a middle-voltage tap to detect imbalance / voltage symmetry.
- This Design does not define the threshold, filtering, hysteresis, persistence time, or whether the final comparison is implemented in firmware or dedicated analog circuitry.

## Former ids
