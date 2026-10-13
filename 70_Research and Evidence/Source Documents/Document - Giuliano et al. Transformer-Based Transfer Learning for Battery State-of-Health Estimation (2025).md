---
type: Document
subtype:
id: DOC-00039
uid: 20261013160000101skellyspencer
status: Draft
tags:
  - source-document
  - article
  - peer-reviewed
  - industry-data
sourceClass: article
sourceUrl: "https://doi.org/10.3390/en18205439"
accessed: 2026-10-13
describes:
  - "[[Data-Driven State of Health Estimator Firmware]]"
supports:
  - "[[Estimate State of Health - Report Configured Threshold Crossings]]"
  - "[[Report State of Health Threshold Crossings]]"
referencedBy:
  - "[[Estimate State of Health - Report Configured Threshold Crossings]]"
---

# Document - Giuliano et al. Transformer-Based Transfer Learning for Battery State-of-Health Estimation (2025)

## Definition

Peer-reviewed study of transformer, LSTM and ANN SOH estimators with transfer learning between two cell data sets (Energies 2025, 18, 5439, MDPI, open access).

## Provenance

- **Source address:** https://doi.org/10.3390/en18205439 (DOI link taken from the journal record cited in [[SOC and Health Estimation Literature Review]]; the link was not fetched in this session, the reviewed copy is the PDF in `Downloads`).
- **Reviewed copy:** local PDF `Transformer-Based_Transfer_Learning_for_Battery_St.pdf` in `Downloads`, read in full during the literature review.
- **Evidence tier:** not covered by T1 to T5 in [[Landscape Evidence and Modeling Conventions]] (journal or conference paper). Treated as peer-reviewed research evidence; its figures come from laboratory data, not from a product.

## What this Document supports

- **Threshold convention ([[Estimate State of Health - Report Configured Threshold Crossings]]):** SOH is tracked as a capacity ratio over the life of the cell and the review records an 80% end-of-life convention among the sources. The paper reports average errors (RMSE) over whole-life curves, not detection of a configured threshold, which is the gap the Requirement addresses.
- Smoothing is applied across the whole predicted curve after the fact, so the reported errors are not those of a live estimate at a threshold.
- Not supported: any forklift or lead-acid claim.

## Former ids
