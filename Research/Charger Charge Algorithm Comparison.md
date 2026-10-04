---
type: Info
subtype:
id: INFO-00268
uid: 20261003203338373skellyspencer
status: Draft
tags:
  - charge-profile
  - charger
  - comparison
  - review
describes:
  - "[[Battery-Connected Product]]"
---

# Charger Charge Algorithm Comparison

## Definition

What charger makers say about how their chargers shape the charge: profile names, stages, adaptation and equalizing, side by side, with the sources and what is not published.

## Notes

- **Owner request (2026-10-03):** charger-side algorithms for Crown, EnerSys, Fronius, Delta-Q and PosiCharge, following the flooded battery guides ([[Flooded Lead-Acid Charge Profile Comparison]]). Characteristic codes are explained in [[Traction Battery Charging Characteristics (DIN Notation)]].
- **Main finding:** none of the five makers publishes numeric stage thresholds (voltage per cell, current, termination) in the material retrieved; they publish names, stage structure and adaptation methods. Numbers sit in battery maker guides (flooded rules in the other note) and in per-battery profile lists (Delta-Q keeps one).
- **Reading rule:** a cell says what the source states; n/s means not stated in the retrieved text. Metric notes carry the values for products on file: [[Metric - Charge Profile Types Offered]], [[Metric - Charge Adaptation Method]], [[Metric - Equalize Scheduling]]; efficiency in [[Metric - Peak Efficiency]].

**Algorithms by maker**

| Maker and charger | Profiles or characteristics named | Stage structure | Adaptation | Equalizing and refresh | Chemistries | Sources |
|---|---|---|---|---|---|---|
| Fronius Selectiva 4.0 | Ri characteristic; special characteristic for opportunity and fast charging; refresh; deep discharge; calendar function | not published as stages; 'every charge has an individual characteristic curve' | effective internal resistance Ri, which depends on age, temperature and state of charge | refresh characteristic raises the performance of a weak battery; equalizing n/s | lead-acid, lead crystal and CSM (as printed in the brochure) | Fronius Ri page and Selectiva 4.0 brochure (T1) |
| EnerSys IMPAQ and NexSys+ | P21 STDWL, P22 HDUTY, P19 FAST, P07 OPP, P25 LOWCHG, P29 NXSTND, P30 NXFAST, P31 NXBLOC; letter types IEI, gel IEI, O, IEIE | IUI (constant current, constant voltage, constant current) on standard profiles; IEIE adds a second constant-voltage stage; finish current 5 percent on OPP; NXFAST rate 0.18 to 0.40 C5 | HDUTY diagnoses the battery through continuous current loops; capacity, temperature and equalize values set or taken from a programmed Wi-iQ | weekly equalize can be programmed; refresh or maintenance charging; opportunity needs cooling time after the equalize | TPPL, flooded, gel | EnerSys IMPAQ and NexSys+ owner's manuals (T1) |
| Delta-Q IC650 (and QuiQ) | one algorithm per battery model; up to 25 field-programmable; 16 lead-acid and 2 lithium preloaded (reseller) | Bulk (maximum current, exit at a conservative target voltage), Absorption (constant voltage, current tapers), Finish (constant-current finish sized to the battery) for lead-acid | temperature-compensated algorithms need the charger sensor; optional CAN for lithium | equalization and float have FAQ articles (not read) | wet, AGM, gel, lithium | Delta-Q support articles (T1), IC650 datasheet (in repo), reseller (T3) |
| Crown V-HFM3 | Conventional, Opportunity, Fast, V-Force Lithium-Ion | n/s | identifies the battery on connection and applies the profile for 24 to 96 V; BMID adds temperature compensation and electrolyte level monitoring | indicators for equalizing and watering needs | lead-acid and lithium-ion | Crown V-HFM3 brochure (T1, in repo) |
| PosiCharge ProCore Edge | PosiCharge proprietary algorithms | n/s | BMID mode or voltage mode; automatic chemistry selection | EQ once a week, an extended low-current charge after a regular charge to 100 percent; EQ button | lead-acid, lithium-ion, Ni-MH, sodium-ion (maker claim) | ProCore Edge IOMM and spec sheet (T1, in repo) |

**Efficiency figures are on different bases (C98)**

- Fronius: overall efficiency up to 84 percent, as device efficiency 93 percent times charging efficiency 90 percent. EnerSys IMPAQ: up to 94 percent (basis not stated). Crown V-HFM3: up to 97 percent (basis not stated). They are not comparable until the basis is known: [[Metric - Peak Efficiency]].

**Gaps**

- Numeric stage thresholds per profile (for example the voltage at which STDWL changes stage, or the Delta-Q bulk exit voltage) are not in the retrieved sources; the EnerSys profile description tables and the Delta-Q Charge Profile List may hold them but were retrieved only as fragments.
- Not read: Delta-Q FAQ articles on equalization and float, Crown's charger manual, the Fronius Selectiva manual, EnerSys' full profile table, ACT, Exide, Stryten and HOPPECKE charger algorithms.
- **Curves:** no charge curves recorded yet; Fronius and EnerSys documents describe curve shapes without tabulated points.

## Aliases

- Charger algorithms

## Former ids
