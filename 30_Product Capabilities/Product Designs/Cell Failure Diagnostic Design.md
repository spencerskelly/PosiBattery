---
type: Design
subtype:
id: DES-90907
uid: 20261006173500001skellyspencer
status: Draft
tags:
  - general-design
  - battery-monitoring
  - diagnostics
  - cell-failure
supertypeOf:
  - "[[Algorithmic Cell Failure Diagnosis]]"
  - "[[Dedicated Threshold Cell Failure Detection]]"
designOf:
  - "[[AMETEK Prestolite Power TruBid]]"
realizes:
  - "[[Detect Cell Failure]]"
dependencyOf:
  - "[[Detect Cell Failure]]"
---

# Cell Failure Diagnostic Design

## Definition

General design class for implementations that determine whether a battery cell-failure condition exists from one or more sensed battery parameters, diagnostic responses, or historical patterns.

## Notes

- This is the reusable realization family for [[Detect Cell Failure]] when a product is known to detect cell failure but its internal diagnostic method is not published.
- [[AMETEK Prestolite Power TruBid]] is assigned at this generic level because published material explicitly identifies a cell-fail alert/detection capability while not disclosing the diagnostic algorithm or circuit.
- [[Algorithmic Cell Failure Diagnosis]] and [[Dedicated Threshold Cell Failure Detection]] are concrete implementation alternatives. Neither is assigned to TruBID without stronger evidence.
- The Design intentionally does **not** depend on [[In-Cell Specific Gravity Probe]], cell-voltage sensing, impedance measurement, or another specific input because the available TruBID evidence does not establish which input drives the diagnosis.

## Evidence boundary

AMETEK/Prestolite material establishes direct specific-gravity measurement and undercharge identification. A Prestolite data-device description separately lists a cell-fail alert. These facts establish the capability but do not establish that specific gravity is the causal cell-failure diagnostic input.

Sources:
- <https://www.prestolitepower.com/aboutus/news/2016/april/100>
- <https://industrialbatterypittsburgh.com/ametek-prestolite-power-battery-motive-power-chargers/data-devices/>

## Former ids
