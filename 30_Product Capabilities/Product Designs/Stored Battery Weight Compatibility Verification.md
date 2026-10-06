---
type: Design
subtype:
id: DES-90040
uid: 20261006171500002skellyspencer
status: Draft
tags:
  - battery-monitoring
  - design-characteristic
  - weight
  - identification
subtypeOf:
  - "[[Battery Weight Determination Design]]"
designOf:
  - "[[Raymond iBattery]]"
  - "[[Battery Specification Memory]]"
  - "[[Battery Weight Verification Firmware]]"
dependsOn:
  - "[[DC-Cable Power-Line Communication]]"
---

# Stored Battery Weight Compatibility Verification

## Definition

Determine whether an installed battery satisfies a vehicle weight requirement by reading a stored battery-weight specification and comparing it with the vehicle minimum.

## Notes

- This is the verified realization used by the Raymond battery-monitoring architecture described in Raymond's industrial-vehicle battery-weight patent.
- The patent states that a battery sensor module contains electronic memory with manufacturer specification data, including battery weight, and that the vehicle controller requests the specification data and compares the stored battery weight with the vehicle's minimum required battery weight.
- The battery-side communication path is through a power-line communication circuit on the battery cable.
- This Design represents **stored specification verification**, not physical weighing. It must not be interpreted as evidence for a load cell or strain gauge inside [[Raymond iBattery]].
- Source: Raymond Corp patent CA2733079A1 / family, priority 2010-04-22: <https://patents.google.com/patent/CA2733079A1/en>

## Former ids
