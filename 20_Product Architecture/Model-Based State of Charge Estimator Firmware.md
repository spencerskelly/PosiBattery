---
type: Object
subtype: firmware
id: OBJ-90905
uid: 20261013113854507skellyspencer
status: Draft
tags:
  - reusable-architecture
  - firmware
  - battery-monitoring
  - state-of-charge
reuseScope: cross-product
subtypeOf:
  - "[[State of Charge Estimation Firmware]]"
dependsOn:
  - "[[Battery Voltage Acquisition Firmware]]"
  - "[[Battery Current Acquisition Firmware]]"
performs:
  - "[[Estimate State of Charge]]"
  - "[[Declare Estimator Accuracy Basis]]"
describedBy:
  - "[[SOC and Health Estimation Literature Review]]"
  - "[[Document - Margal et al. Comparative Analysis of Battery State of Charge Estimation Methods (2025)]]"
applies:
  - "[[Estimate State of Charge and Health - Declare Accuracy Basis]]"
---

# Model-Based State of Charge Estimator Firmware

## Definition

Candidate SOC-estimation firmware that runs a filter or observer on an equivalent-circuit battery model, using measured voltage and current to correct the SOC estimate continuously, with model parameters that are set per battery type.

## Notes

- **Candidate implementation, not a product claim.** No modeled product is allocated: the vault's product sources do not identify a model-based SOC algorithm.
- Approaches in the evidence: extended Kalman filter on one or two RC branches (review sources 4, 5), adaptive observer (source 5), a robust observer that estimates open-circuit voltage while the battery is loaded (source 7, patent US 8,922,217), and a joint filter on a fractional-order model that also tracks resistance as a health indicator (source 8).
- Inputs: battery voltage and current; temperature is used by some variants and by the parameter tables ([[Battery Temperature Acquisition Firmware]] is not made a dependency here because the sources differ).
- **Commissioning input.** Model parameters (open-circuit voltage curve, resistances, capacitances) come from characterizing the battery type; the sources fit them offline. How a fielded device gets them is not shown.
- Accuracy figures in the sources are not comparable with each other (different cells, profiles and error definitions; see C154 in [[Battery Product Landscape Conflicts and Open Questions]]).
- **Chemistry.** The sources behind this approach tested lithium cells. The approach is written generally, but its parameters (see the commissioning bullet) must be supplied for the chemistry it is applied to. See the chemistry scope in [[SOC and Health Estimation Literature Review]].
- **Allocation (engineering inference, not a source claim).** Embedded: a filter step per sample on the battery-side device; parameter fitting offline. No source measures compute, memory or timing on target hardware.
- Evidence and per-source detail: [[SOC and Health Estimation Literature Review]].

## Former ids
