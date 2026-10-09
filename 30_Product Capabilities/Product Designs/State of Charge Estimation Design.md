---
type: Design
subtype:
id: DES-90007
uid: 20261005222800001skellyspencer
status: Draft
tags:
  - product-design
  - battery-monitoring
  - software
supertypeOf:
  - "[[Battery-Monitor State of Charge Estimation]]"
  - "[[Integrated BMS State of Charge Estimation]]"
realizes:
  - "[[Estimate State of Charge]]"
designOf:
  - "[[State of Charge Estimation Firmware]]"
supportedBy:
  - "[[Document - PosiCharge GSE BMID Page]]"
dependsOn:
  - "[[Battery Voltage Measurement Design]]"
  - "[[Document - PosiCharge GSE BMID Page]]"
---

# State of Charge Estimation Design

## Definition

Software/algorithm design for estimating battery state of charge from measured battery state and stored battery configuration.

## Notes

This is the selected reusable realization family for [[Estimate State of Charge]]. Products with an unknown algorithm should link to the implementation firmware/Object rather than owning this general Design class.

Product-backed implementation loci currently include:
- [[Battery-Monitor State of Charge Estimation]];
- [[Integrated BMS State of Charge Estimation]].

Algorithm alternatives are represented as candidate firmware Objects rather than unbacked specific Designs:
- [[Voltage-Based State of Charge Estimator Firmware]];
- [[Coulomb Counting State of Charge Estimator Firmware]];
- [[Hybrid State of Charge Estimator Firmware]].

The generic Design does not select an algorithm.

## Former ids
