---
type: Object
subtype: firmware
id: OBJ-90085
uid: 20261006193000005skellyspencer
status: Draft
tags:
  - reusable-architecture
  - firmware
  - battery-monitoring
  - electrolyte
  - specific-gravity
reuseScope: cross-product
dependsOn:
  - "[[Specific Gravity Measurement Circuit]]"
  - "[[Control Circuit]]"
partOf:
  - "[[AMETEK Prestolite Power TruBid]]"
performs:
  - "[[Measure Electrolyte Specific Gravity]]"
---

# Specific Gravity Acquisition Firmware

## Definition

Firmware that converts the specific-gravity sensor signal into a usable specific-gravity value and makes it available to higher-level battery or charging functions.

## Notes

- Allocation to [[AMETEK Prestolite Power TruBid]] is an **>=95% engineering-confidence assumption** because TruBID reports and uses a continuously measured specific-gravity value, while the internal firmware partition is not published.
- Possible responsibilities include sensor conversion, calibration, filtering, temperature correction, plausibility checking, compensation, and reporting.
- No temperature-correction algorithm or calibration law is asserted from the current evidence.

## Former ids
