---
type: Function
subtype:
id: FUNC-90002
uid: 20261013113854500skellyspencer
status: Draft
tags:
  - battery-monitoring
  - product-function
  - candidate-from-research
subtypeOf:
  - "[[Sense Battery State]]"
dependencyOf:
  - "[[Capacity-Retention State of Health Estimator]]"
  - "[[Data-Driven State of Health Estimator Firmware]]"
describedBy:
  - "[[SOC and Health Estimation Literature Review]]"
performedBy:
  - "[[Discharge Cycle Segmentation Firmware]]"
realizes:
  - "[[Prevent Battery Abuse and Premature Replacement]]"
---

# Segment Discharge Cycles

## Definition

Identify where each charge or discharge cycle begins and ends in the measured battery current and voltage, and label which cycles are complete, so that per-cycle capacity and per-cycle features can be computed.

## Notes

- **Candidate function from research, not a product claim.** No product source in the vault states that a modeled product does this, so it has no performer yet. Overview of the evidence: [[SOC and Health Estimation Literature Review]].
- Several state-of-health approaches need it: the capacity ratio needs the amp-hours of one complete cycle ([[Capacity-Retention State of Health Estimator]]); the data-driven approaches take features from one discharge resampled to a fixed length (review sources 13 and 15) or a window the length of an average discharge (source 14); see [[Data-Driven State of Health Estimator Firmware]].
- Every source in the review uses laboratory data with a full constant-current discharge. None describes segmentation under partial discharge or opportunity charging, which is the normal forklift duty.
- What counts as a cycle is not settled in the sources; the definitions differ (see C140 in [[Battery Product Landscape Conflicts and Open Questions]]). This Function does not choose one. The cycle-validity rule is a product-specific decision.
- Not to be confused with [[Calculate Battery Abuse Cycles]], which counts abusive-use events.

## Former ids
