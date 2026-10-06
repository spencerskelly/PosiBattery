---
type: Design
subtype:
id: DES-90022
uid: 20261006170500001skellyspencer
status: Draft
tags:
  - general-design
  - design-characteristic
  - operator-interface
  - vehicle
subtypeOf:
  - "[[Display Device Design]]"
supertypeOf:
  - "[[Vehicle-Mounted Display]]"
  - "[[Operator Touch Display]]"
  - "[[Battery Discharge Indicator]]"
realizes:
  - "[[Display Truck Status to Operator]]"
  - "[[Display Battery Status to Operator]]"
dependencyOf:
  - "[[Display Battery Status to Operator]]"
  - "[[Display Truck Status to Operator]]"
designOf:
  - "[[Vehicle Operator Display Assembly]]"
---

# Vehicle Operator Display Design

## Definition

General design family for displaying battery state, vehicle state, diagnostics, warnings, or other operating information to an operator on a vehicle-side display.

## Notes

- This family narrows [[Display Device Design]] to operator-facing vehicle displays and separates them from battery-mounted LCDs and gauges.
- Specific implementations include a general [[Vehicle-Mounted Display]], an interactive [[Operator Touch Display]], and a dedicated [[Battery Discharge Indicator]].
- Products link to the applicable specific child Design rather than directly to this general class.

## Former ids
