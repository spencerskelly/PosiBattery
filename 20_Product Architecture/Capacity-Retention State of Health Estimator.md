---
type: Object
subtype: firmware
id: OBJ-90087
uid: 20261006195500003skellyspencer
status: Draft
tags:
  - reusable-architecture
  - firmware
  - battery-monitoring
  - analytics
  - state-of-health
reuseScope: cross-product
performs:
  - "[[Estimate State of Health]]"
---

# Capacity-Retention State of Health Estimator

## Definition

Candidate firmware implementation that estimates state of health from available battery capacity relative to an initial or rated capacity baseline.

## Notes

- **Candidate implementation, not a product claim.**
- A typical implementation can estimate usable discharge capacity over one or more sufficiently complete cycles, normalize it to an initial/rated capacity, and report SOH as a percentage or health class.
- Inputs can include accumulated amp-hours, state of charge, current, voltage, temperature, charge/discharge endpoints, and stored baseline capacity.
- Calibration rules, cycle-validity criteria, temperature normalization, aging baseline, and confidence limits are product-specific.
- No current commercial product is allocated in this vault because the available sources do not prove that a modeled product calculates SOH this way.

## Former ids
