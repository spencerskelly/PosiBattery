---
type: Document
subtype:
id: DOC-00615
uid: 20261018180000009skellyspencer
status: Draft
tags:
  - source-document
  - article
  - soc-soh
sourceClass: article
sourceUrl: "https://pangea.stanford.edu/ERE/pdf/OnoriPDF/Journals/115.pdf"
accessed: 2026-10-18
describes:
  - "[[SOC and SOH Methods Reference]]"
---

# Document - Gao and Onori Advancing SOC Estimation in LiFePO4 Batteries Enhanced dQ-dV Curve and Short-Pulse Methods (eTransportation 2025)

## Definition

Stanford paper on LFP SOC from the dQ/dV curve using short current pulses and an unscented Kalman filter, addressing the flat LFP OCV (C195).

## Provenance

- **Source address:** https://pangea.stanford.edu/ERE/pdf/OnoriPDF/Journals/115.pdf
- **Repo file:** Downloads/115.pdf (14 pages), added by the owner on 2026-10-18. Text was extracted from the file and the passages below were read; this is a first-hand read of the file, but not every section was read in full.
- **Evidence tier:** not covered by T1 to T5 in [[Landscape Evidence and Modeling Conventions]] (paper, standard or catalogue record).
- **Source key in the SOC and SOH notes:** S33.

## Notes

- Test article: one 26650 cylindrical LFP cell, 2.5 Ah, 3.3 V nominal, 2.0 to 3.65 V limits, at a controlled 25 C. Cell level only; no pack, no voltage near 96 V.
- Result as stated: with 0.2C to 0.5C pulses, RMSE below 0.08 (that is 8 percent of SOC) with convergence in 180 to 540 s; a 0.5C pulse gave RMSE 0.0256. Convergence failed at 1C and 2C and in mid-to-high SOC (about 0.5 to 0.9).
- The reference curves were built offline across five C-rates, so a design needs cell characterization per model; the authors list embedded hardware-in-the-loop validation as future work.
- Relevance: a candidate answer to the LFP flat-curve problem in C195, with the limits above.

Content recorded from this source is in [[SOC and SOH Methods Reference]].

## Former ids
