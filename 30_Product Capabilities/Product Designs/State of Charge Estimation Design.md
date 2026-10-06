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
  - "[[Voltage-Based State of Charge Estimation]]"
  - "[[Coulomb Counting State of Charge Estimation]]"
  - "[[Hybrid State of Charge Estimation]]"
realizes:
  - "[[Estimate State of Charge]]"
designOf:
  - "[[State of Charge Estimation Firmware]]"
supportedBy:
  - "[[Document - PosiCharge GSE BMID Page]]"
dependsOn:
  - "[[Battery Voltage Measurement Design]]"
---

# State of Charge Estimation Design

## Definition

Software/algorithm design for estimating battery state of charge from measured battery state and stored battery configuration.

## Notes

This is the selected reusable realization family for [[Estimate State of Charge]]. Products with an unknown algorithm should link to the implementation firmware/Object rather than owning this general Design class.

Concrete algorithm alternatives include:
- [[Voltage-Based State of Charge Estimation]];
- [[Coulomb Counting State of Charge Estimation]];
- [[Hybrid State of Charge Estimation]].

The generic Design does not select an algorithm. Product-specific assignment of a child Design requires evidence or an explicit engineering decision.

## Former ids
