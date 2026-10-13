---
type: Document
subtype:
id: DOC-00026
uid: 20261013150000014skellyspencer
status: Draft
tags:
  - source-document
  - tier-T4
  - industry-data
  - vendor-article
sourceClass: vendor-article
describes:
  - "[[Industry Data Register from Downloads Articles]]"
  - "[[ENEROC]]"
---

# Document - ENEROC Propane to Electric Battery Sizing (2026-09-23)

## Definition

Method for sizing a lithium battery to replace a propane forklift.

## Provenance

- **Local artifact:** `(3) Propane to Electric_ How to Size the Battery for Your Forklift Fleet _ LinkedIn.pdf` in `Downloads`.
- **Author or publisher:** Max Khabur, Marketing Director, ENEROC USA (LinkedIn article). ENEROC sells lithium forklift batteries, so the article is supplier-authored.
- **Date:** 2026-09-23.
- **Original web address:** not captured in the saved copy.
- **Evidence tier:** T4 (third-party blog, vendor marketing or templated post; see [[Landscape Evidence and Modeling Conventions]]). The author or publisher has a commercial interest in the subject unless stated otherwise.
- **Local copy reviewed:** 2026-10-13 (full text read).

## Notes

**Content recorded (as stated by the source, not independently verified unless marked):**
- Four sizing variables: energy per hour, working hours, battery age, operating conditions.
- Energy per hour from OEM data under ISO 23308; based on advertised OEM specifications one gallon of propane does the same work as about 4.85 kWh of electricity. The conversion table is an image and was not captured as text.
- Working hours: a truck on an 8-hour shift typically records 5 to 6 hours; the method uses 65 percent, so 8 x 0.65 = 5.2 metered hours.
- Size to end-of-life capacity; cold (refrigerated warehouses, open docks, outdoor yards in cold climates) needs another 15 percent capacity.
- Worked example: 5,000 lb, 80 V sit-down truck, 6.3 kWh/h, 70 percent end-of-life capacity: 5.2 x 6.3 = 32.8 kWh per day; 32.8 / 0.70 x 1000 / 80 = 585 Ah, round up to 600 Ah.
- Says lead-acid loses cycle life if regularly discharged below 40 percent of rated capacity, and LFP can be safely discharged to 80 percent depth of discharge (C177).

**Checks made:**
- Arithmetic checks: 5.2 x 6.3 = 32.76; 32.76 / 0.70 x 1000 / 80 = 585 Ah. The example does not apply the 80 percent depth of discharge or the 15 percent cold margin the article itself gives (C183).

## Traceability

- Retained under the project goal of keeping industry data in one place for stakeholder review; synthesized in [[Industry Data Register from Downloads Articles]].
- Conflicts and open questions: C177, C183 in [[Battery Product Landscape Conflicts and Open Questions]].

## Aliases


## Former ids
