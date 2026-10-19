---
type: Document
subtype:
id: DOC-00608
uid: 20261018180000002skellyspencer
status: Draft
tags:
  - source-document
  - article
  - soc-soh
sourceClass: article
sourceUrl: "https://journal.sobraep.org.br/index.php/rep/article/download/398/358"
accessed: 2026-10-18
describes:
  - "[[SOC and SOH Methods Reference]]"
---

# Document - Lazzarin and Barbi A System for State-of-Health Diagnosis of Lead-Acid Batteries Integrated with a Battery Charger (2011-2012)

## Definition

Eletronica de Potencia 17(1) paper on a 1.5 kW lead-acid charger with an integrated per-battery impedance test for state of health, built for a UPS string.

## Provenance

- **Source address:** https://journal.sobraep.org.br/index.php/rep/article/download/398/358
- **Repo file:** Downloads/rvol17no1p12.pdf (8 pages), added by the owner on 2026-10-18. Text was extracted from the file and the passages below were read; this is a first-hand read of the file, but not every section was read in full.
- **Evidence tier:** not covered by T1 to T5 in [[Landscape Evidence and Modeling Conventions]] (paper, standard or catalogue record).
- **Source key in the SOC and SOH notes:** S26.

## Notes

- Prototype: 16 batteries of 12 V, 36 Ah in series (192 V DC link), charger up to 8 A, recharge current 4.5 A; pack reached the equalization voltage 235 V and ended at the float voltage 216 V. The 192 V bank is above the owner's 96 V scope; only the per-battery 12 V measurement idea carries over.
- Method: 4 A, 60 Hz ac injected into the series string, voltage drop measured per 12 V battery; the reference is the average of at least twenty measurements taken when the pack is new, under the same charge conditions. Measurements are stored with temperature and dc voltage as a history.
- Threshold used: a normalized impedance module above 130 percent of the reference marks the battery inadequate, citing literature that a 30 percent impedance rise corresponds to capacity of about 80 percent of initial. These are cited from other papers, not measured here.
- Stated limits: impedance varies with capacity, temperature, charge level and frequency, so tests should run at close to 100 percent charge; fifty measurements over three months are preliminary and a full life cycle of three to four years is needed to confirm the diagnosis.
- Relevance: shows an SOH measurement placed inside the charger, which is the owner's question 4 (estimator in charger). Application is stationary UPS, not traction duty.

Content recorded from this source is in [[SOC and SOH Methods Reference]].

## Former ids
