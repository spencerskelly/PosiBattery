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
---

# State of Charge Estimation Design

## Definition

Software/algorithm design for estimating battery state of charge from measured battery state and stored battery configuration.

## Notes

This is the selected reusable realization family for [[Estimate State of Charge]].

Concrete algorithm alternatives include:
- [[Voltage-Based State of Charge Estimation]];
- [[Coulomb Counting State of Charge Estimation]];
- [[Hybrid State of Charge Estimation]].

The generic Design does not select an algorithm. Product-specific assignment of a child Design requires evidence or an explicit engineering decision.

## Former ids
