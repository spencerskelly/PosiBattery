---
type: Info
subtype:
id: INFO-90024
uid: 20261013150000008skellyspencer
status: Draft
tags:
  - unlinked-capture
  - tier-T4
  - industry-data
  - vendor-article
describes:
  - "[[Industry Data Register from Downloads Articles]]"
---

# Document - Zhang Passive vs Active Battery Balancing (2026-10-12)

## Definition

Compares passive and active cell balancing for AGV, AMR and UGV packs.

## Provenance

- **Local artifact:** `(1) Passive vs. Active Battery Balancing_ How to Choose the Right Strategy for Mobile Robots _ LinkedIn.pdf` in `Downloads`.
- **Author or publisher:** Maggie Zhang, LinkedIn newsletter 'Powering Industrial Mobility'. Author headline: Battery Solutions for AMR, AGV, UGV and Mobile Robotics, custom Li-ion battery packs, OEM/ODM, BMS and CAN. One article in the series names the author's company as RuiDeJin New Energy, a maker of customized lithium packs, so the series is supplier-authored.
- **Date:** 2026-10-12.
- **Original web address:** not captured in the saved copy.
- **Evidence tier:** T4 (third-party blog, vendor marketing or templated post; see [[Landscape Evidence and Modeling Conventions]]). The author or publisher has a commercial interest in the subject unless stated otherwise.
- **Local copy reviewed:** 2026-10-13 (full text read).

## Notes

**Content recorded (as stated by the source, not independently verified unless marked):**
- Passive balancing dissipates excess energy from higher-SOC cells in resistors as heat; simple, low cost, low current, no energy recovery. Active balancing moves energy between cells with capacitors, inductors or DC-DC converters; more complex and costly, performance depends on balancing current, transfer efficiency and control strategy.
- The first cell to reach a protection limit stops the whole pack, so imbalance reduces usable energy; balancing does not restore lost capacity or repair a damaged cell.
- Choose from the operating profile: AGVs with predictable charging and matched cells often do well with passive balancing; AMRs with short charge windows may justify evaluating active balancing; UGVs need temperature and discharge management alongside balancing.
- Five questions: time between charging opportunities, how much imbalance must be corrected, required balancing current, chemistry and conditions, and lifetime cost. Active balancing cannot compensate for an undersized pack, excess consumption or a degraded cell.

**Checks made:**
- Qualitative; no figures. Consistent with general BMS practice; no primary source cited.

## Traceability

- Retained under the project goal of keeping industry data in one place for stakeholder review; synthesized in [[Industry Data Register from Downloads Articles]].

## Aliases


## Former ids
- DOC-00020
