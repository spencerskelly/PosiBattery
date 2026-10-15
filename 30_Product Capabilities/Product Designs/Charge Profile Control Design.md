---
type: Design
subtype:
id: DES-00139
uid: 20261014163455383skellyspencer
status: Draft
tags:
  - general-design
  - design-characteristic
supertypeOf:
  - "[[Adaptive Charge Profile Control Design]]"
  - "[[BMS-Directed Charge Control Design]]"
  - "[[Temperature-Compensated Charge Control Design]]"
  - "[[Lead-Acid Desulfation Charge Control Design]]"
  - "[[Voltage-Triggered Ready-State Top-Up]]"
  - "[[Battery-Stored Equalization Schedule]]"
  - "[[Time-Window Charge Current Setting]]"
dependencyOf:
  - "[[Charge Battery Fast]]"
  - "[[Charge Battery by Opportunity]]"
  - "[[Charge Battery Conventionally]]"
  - "[[Charge Lithium-Ion Battery]]"
---

# Charge Profile Control Design

## Definition

General design class: the control logic that sets how a charger varies current and voltage over a charge (profile), whether fixed, temperature-compensated, battery-directed or adaptive.

## Notes

- General-level note: products do not link here directly; they link to the specific designs below (see [[Function and Design Levels]]).
- Added 2026-10-14 so charge-method Functions can depend on a profile control Design together with [[Charger Power Stage Design]]. The four existing control Designs were each already built on the power stage; they had no common parent.

## Aliases


## Former ids
