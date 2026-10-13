---
type: Object
subtype: firmware
id: OBJ-90906
uid: 20261013113854514skellyspencer
status: Draft
tags:
  - reusable-architecture
  - firmware
  - battery-monitoring
  - state-of-health
reuseScope: cross-product
dependsOn:
  - "[[Battery Voltage Acquisition Firmware]]"
  - "[[Battery Current Acquisition Firmware]]"
  - "[[Battery Temperature Acquisition Firmware]]"
  - "[[Segment Discharge Cycles]]"
performs:
  - "[[Estimate State of Health]]"
  - "[[Report State of Health Threshold Crossings]]"
  - "[[Declare Estimator Accuracy Basis]]"
describedBy:
  - "[[SOC and Health Estimation Literature Review]]"
  - "[[Document - Mbagaya et al. Machine Learning Techniques for Battery State of Health Prediction (2025)]]"
  - "[[Document - Giuliano et al. Transformer-Based Transfer Learning for Battery State-of-Health Estimation (2025)]]"
applies:
  - "[[Estimate State of Health - Report Configured Threshold Crossings]]"
  - "[[Estimate State of Charge and Health - Declare Accuracy Basis]]"
---

# Data-Driven State of Health Estimator Firmware

## Definition

Candidate firmware that estimates state of health from a trained model applied to features of one complete discharge cycle (voltage, current and temperature), with the model trained offline.

## Notes

- **Candidate implementation, not a product claim.** No modeled product is allocated.
- Model families in the evidence: random forest and support vector regression on summary statistics (review sources 13, 15), a small 1D convolutional network on a resampled cycle (source 15, 10,169 parameters, claimed about 10 kB at 8-bit), and heavier recurrent or transformer models (sources 13, 14). The sources themselves say the recurrent and transformer models are hard to run on embedded BMS hardware; the small CNN and tree claims are not tested on target hardware.
- Depends on a cycle buffer and the cycle segmentation in [[Segment Discharge Cycles]]. One variant (source 14) also feeds in the previous cycle's capacity from [[Accumulate Amp-Hours]].
- Source 15 shows that a model trained without the operating conditions (temperature, load, cutoff) failed on cells from other protocols, so a record of operating conditions is a further input (see [[Log Battery Events and Usage]]). Source 15 also reports that the critical band (SOH below 70%) was caught only 7.1% of the time; see [[Estimate State of Health - Report Configured Threshold Crossings]].
- Accuracy figures are not comparable across sources (C162, C167, C168 in [[Battery Product Landscape Conflicts and Open Questions]]).
- **Chemistry.** The sources behind this approach tested lithium cells. The approach is written generally, but its parameters (see the commissioning bullet) must be supplied for the chemistry it is applied to. See the chemistry scope in [[SOC and Health Estimation Literature Review]].
- **Allocation (engineering inference, not a source claim).** Embedded for acquisition, cycle segmentation and feature extraction; the model could be embedded only if a small model is shown on target hardware; training offline or in [[Learned State of Health Service]].
- Evidence and per-source detail: [[SOC and Health Estimation Literature Review]].

## Former ids
