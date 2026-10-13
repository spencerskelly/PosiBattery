---
type: Document
subtype:
id: DOC-00038
uid: 20261013160000100skellyspencer
status: Draft
tags:
  - source-document
  - article
  - peer-reviewed
  - industry-data
sourceClass: article
sourceUrl: "https://doi.org/10.3390/wevj16110594"
accessed: 2026-10-13
describes:
  - "[[Data-Driven State of Health Estimator Firmware]]"
supports:
  - "[[Estimate State of Health - Report Configured Threshold Crossings]]"
  - "[[Estimate State of Charge and Health - Declare Accuracy Basis]]"
  - "[[Report State of Health Threshold Crossings]]"
  - "[[Declare Estimator Accuracy Basis]]"
referencedBy:
  - "[[Estimate State of Health - Report Configured Threshold Crossings]]"
  - "[[Estimate State of Charge and Health - Declare Accuracy Basis]]"
---

# Document - Mbagaya et al. Machine Learning Techniques for Battery State of Health Prediction (2025)

## Definition

Peer-reviewed comparative review and simulation of machine-learning SOH estimators (World Electric Vehicle Journal 2025, 16, 594, MDPI, open access).

## Provenance

- **Source address:** https://doi.org/10.3390/wevj16110594 (DOI link taken from the journal record cited in [[SOC and Health Estimation Literature Review]]; the link was not fetched in this session, the reviewed copy is the PDF in `Downloads`).
- **Reviewed copy:** local PDF `Machine_Learning_Techniques_for_Battery_State_of_H.pdf` in `Downloads`, read in full during the literature review.
- **Evidence tier:** not covered by T1 to T5 in [[Landscape Evidence and Modeling Conventions]] (journal or conference paper). Treated as peer-reviewed research evidence; its figures come from laboratory data, not from a product.

## What this Document supports

- **Accuracy basis ([[Estimate State of Charge and Health - Declare Accuracy Basis]]):** the paper reports its errors for one test cell (B0005), one chemistry, 25 C, fixed protocols, and states those limits itself. That is the kind of basis a declared accuracy would need to carry. The paper does not itself define such a requirement.
- **Threshold convention ([[Estimate State of Health - Report Configured Threshold Crossings]]):** the tested cells run to end of life at 70% of nominal capacity, so a threshold on SOH is part of how the data set is defined. The paper does not evaluate detection of a threshold crossing. The evidence for missed crossings is source 15 of the literature review, which has no public address and is therefore not a curated Document (open item).
- Not supported: any forklift or lead-acid claim; the paper is lithium-ion laboratory data only.

## Former ids
