---
type: Info
subtype:
id: INFO-90021
uid: 20261013150000005skellyspencer
status: Draft
tags:
  - unlinked-capture
  - tier-T4
  - industry-data
  - vendor-article
describes:
  - "[[Industry Data Register from Downloads Articles]]"
---

# Document - Zhang AMR and AGV the Power Behind Industry 4.0 (2026-09-07)

## Definition

Argues that AMR and AGV batteries are part of the automation data loop and that charging strategy affects productivity.

## Provenance

- **Local artifact:** `(1) AMR & AGV_ The Power Behind the Industrial 4.0 Revolution _ LinkedIn.pdf` in `Downloads`.
- **Author or publisher:** Maggie Zhang, LinkedIn newsletter 'Powering Industrial Mobility'. Author headline: Battery Solutions for AMR, AGV, UGV and Mobile Robotics, custom Li-ion battery packs, OEM/ODM, BMS and CAN. One article in the series names the author's company as RuiDeJin New Energy, a maker of customized lithium packs, so the series is supplier-authored.
- **Date:** 2026-09-07.
- **Original web address:** not captured in the saved copy.
- **Evidence tier:** T4 (third-party blog, vendor marketing or templated post; see [[Landscape Evidence and Modeling Conventions]]). The author or publisher has a commercial interest in the subject unless stated otherwise.
- **Local copy reviewed:** 2026-10-13 (full text read).

## Notes

**Content recorded (as stated by the source, not independently verified unless marked):**
- Cites OTTO Motors' Mauser Packaging Solutions case: previous AGV system about 3 to 4 missions before returning to charge; OTTO 1500 up to 36 missions with opportunity charging. Checked against the OTTO page: see C184.
- Battery data an AMR or AGV may need: SOC, SOH, pack voltage, current, cell voltage, temperature, charging status, fault and protection information, over CAN, RS485, UART or other protocols.
- Example reasoning: a fleet of 50 AMRs that only knows 'low battery' has fewer options than one that knows SOC, health, temperature and charging status.
- Opportunity charging changes the design question from 'how large a battery' to 'how efficiently can the robot use the energy available'; larger packs add weight, space, cost and charge time.
- Define before choosing a battery: payload, hours per day, peak current, opportunity charging, communication; avoid starting from '48 V 100 Ah'.
- Cost warning: shorter cycle life, lower usable capacity, longer charge time, poor SOC accuracy, limited communication, frequent replacement and higher integration cost can outweigh a lower price.

**Checks made:**
- OTTO figures confirmed on the OTTO case-study page; the 6x headline is a missions-per-charge measure (C184).

## Traceability

- Retained under the project goal of keeping industry data in one place for stakeholder review; synthesized in [[Industry Data Register from Downloads Articles]].
- Conflicts and open questions: C184 in [[Battery Product Landscape Conflicts and Open Questions]].

## Aliases


## Former ids
- DOC-00017
