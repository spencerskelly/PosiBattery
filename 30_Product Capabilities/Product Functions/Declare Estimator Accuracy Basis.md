---
type: Function
subtype:
id: FUNC-90004
uid: 20261013161000002skellyspencer
status: Draft
tags:
  - battery-monitoring
  - product-function
  - candidate-from-research
subtypeOf:
  - "[[Sense Battery State]]"
performedBy:
  - "[[Model-Based State of Charge Estimator Firmware]]"
  - "[[Data-Driven State of Health Estimator Firmware]]"
satisfies:
  - "[[Estimate State of Charge and Health - Declare Accuracy Basis]]"
describedBy:
  - "[[SOC and Health Estimation Literature Review]]"
supportedBy:
  - "[[Document - Mbagaya et al. Machine Learning Techniques for Battery State of Health Prediction (2025)]]"
  - "[[Document - Margal et al. Comparative Analysis of Battery State of Charge Estimation Methods (2025)]]"
realizes:
  - "[[Know Battery State Before and During the Shift]]"
---

# Declare Estimator Accuracy Basis

## Definition

Attach to each state-of-charge or state-of-health estimate the battery chemistry, duty cycle, test conditions and error definition under which the estimator's accuracy was established.

## Notes

- **Candidate function from research, not a product claim.** No product source in the vault states that a modeled product does this. It exists so that [[Estimate State of Charge and Health - Declare Accuracy Basis]] has a satisfier.
- The declaration is documentation or configuration that travels with the estimator; it does not require runtime computation. How it is carried is not decided.
- Scope is limited to the two estimator candidates that have curated evidence; other estimators can be added when they have a source Document.
- Evidence overview: [[SOC and Health Estimation Literature Review]].

## Former ids
