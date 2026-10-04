---
type: Info
subtype:
id: INFO-00271
uid: 20261003220208402skellyspencer
status: Draft
tags:
  - charge-profile
  - vrla
  - agm
  - gel
  - comparison
  - review
describes:
  - "[[Industrial Traction Battery]]"
---

# VRLA Charge Profile Comparison (AGM and Gel)

## Definition

Charge rules for valve-regulated lead-acid (AGM and gel) batteries as stated by makers and an industry association, side by side, with the sources, tiers, applications and conflicts.

## Notes

- **Owner request (2026-10-03):** valve-regulated (AGM and gel) charge profiles, after the flooded ones ([[Flooded Lead-Acid Charge Profile Comparison]]). Parameters first, curves later; characteristic codes are in [[Traction Battery Charging Characteristics (DIN Notation)]]; low-temperature and cold-store rules are in [[Cold Storage Charging Rules for Traction Batteries (ZVEI)]].
- **Scope and honest limit:** motive power AGM and gel products on file are the Stryten AGM200, AGM210 and AGM220 and the EnerSys NexSys TPPL (a thin-plate pure lead, absorbed-electrolyte design). Most numeric VRLA charge data found comes from non-traction lines (East Penn's 8A deep-cycle AGM, Sonnenschein stationary gel, Discover), so those columns are patterns for contrast, not traction rules.
- **Reading rule:** values come from maker documents or snippets of them; applications are named in each column. n/s means not stated in the retrieved text. Metric notes carry values for products on file: [[Metric - Constant Voltage Setpoint]], [[Metric - Opportunity Charging Window]], [[Metric - Charge Factor]], [[Metric - Charge Temperature Limits]].

**Parameters by source**

| Parameter | Stryten AGM220 (motive, onboard charger; T1 snippets) | EnerSys NexSys TPPL (motive; T1/T2) | East Penn 8A line AGM staged guideline (deep-cycle, T1 snippet) | ZVEI traction leaflets, PzV gel (association, T2, read in full) | Sonnenschein gel (Exide group; stationary and rail, T1 snippets) | Discover (deep-cycle and semi-traction; T3) |
|---|---|---|---|---|---|---|
| Profile type | CC-CV-CC with automatic termination, high-frequency charger | profiles P29 NXSTND, P30 NXFAST and P31 NXBLOC (see [[Charger Charge Algorithm Comparison]]) | bulk (I1), absorption (V1), optional accelerated finish (I2), optional float (V2) | IUIa only; a charge-factor control is not permitted because of recombination | IU (constant current then constant voltage), or I charging with limited current | bulk, absorption, float; 'balance' algorithms |
| Bulk current | n/s | NXFAST rate 0.18 to 0.40 C5 | at most 30 A per 100 Ah (C20) | main charge about 12 to 14 A per 100 Ah in the leaflet's diagram | rail: 10 to 35 A per 100 Ah indicative; solar: at least 10 A per 100 Ah C10 | n/s |
| Bulk end or absorption voltage | constant voltage 2.37 V per cell | n/s | 2.40 to 2.43 V per cell at 20 C; bulk time at most 1.2 times depth of discharge in Ah divided by average current | gel PzV temperature-corrected voltage 2.35 V per cell at 30 C | 2.40 V per cell | gel at most 2.35 V per cell, AGM at most 2.45 V per cell, at 25 C |
| End of charge | automatic charge control (criterion n/s) | n/s | current acceptance falls by less than 0.10 A over 1 hour (maximum 12 h), or I2 reached (maximum 6 h); stop if current rises above 8 A after dropping below 6 A | final current 1.0 to 1.4 A per 100 Ah in the diagram; last phase time set from the main charge time | n/s | n/s |
| Finishing stage | constant current in a CC-CV-CC curve | n/s | optional accelerated finish 1 to 2 A per 100 Ah (C20) for 1 to 4 hours by Ah returned (under 25 percent of C20: 1 h; 25 to 50 percent: 2 h; over 50 percent: 4 h) | final constant-current phase of IUIa | n/s | n/s |
| Float | n/s | n/s | optional, 2.25 V per cell at 20 C, generally unneeded if there is no load when idle and no idle period over 3 months | n/s | n/s | gel at most 2.25, AGM at most 2.27 V per cell at 25 C |
| Equalize | an equalizing charge before first use | n/s | not required on VRLA as part of a daily setup (East Penn renewable sheet, a different document from the staged guideline) | n/s | n/s | 'balance' charge; not equalize |
| Charge factor | n/s | low charging factor, up to 30 percent energy saving against standard (trade report) | n/s | 1.1 for energy estimates | n/s | n/s |
| Temperature compensation | optional on PalletPro systems | charging inhibited above 60 C | subtract 0.005 V per cell for each degree above 20 C | PzV: 2.35 V + [-0.004 V per cell per K x (temperature - 30 C)], 0 to 40 C; constant 2.47 V per cell at 0 to -10 C (as printed) | none needed between 15 and 35 C; outside that range adjust by the maker's figures | 0.005 V per cell per degree from 25 C |
| Depth of discharge | do not discharge (limit cut off) | keep above 40 percent charge | n/s | optimized life at 60 percent at most; 80 percent possible per the maker | n/s | n/s |
| Opportunity charging | between 30 and 70 percent state of charge | 40 to 80 percent in 1 h, 98 percent in 2 h (Fast) | n/s | partial charges, not a replacement for full charges | n/s | n/s |

**Related East Penn tables (other applications)**

- East Penn photovoltaic bulletin (2007, dealer-hosted): absorption 2.35 to 2.40 V per cell for gel, 2.30 to 2.35 for AGM and 2.40 to 2.45 for flooded; float 2.25 to 2.30, 2.25 to 2.30 and 2.30 to 2.35; equalize 2.40 to 2.45, 2.35 to 2.40 and 2.50 to 2.55; bulk 30 percent of the 20 h rate; voltages at 25 C. A newer East Penn renewable sheet gives a VRLA temperature coefficient of -3 mV per cell per C and states that an equalize is not required on VRLA as part of a daily setup.
- East Penn 8A24DT and 8AGC2 datasheets: charge voltage at 20 C of 2.40 to 2.43 V per cell for cycle use and 2.25 to 2.30 V per cell for float.

**Conflicts and gaps**

- **Temperature coefficient differs (C99):** -0.004 V per cell per K (ZVEI, reference 30 C, PzS and PzV), -0.005 V per cell per C (East Penn 8A staged guideline at 20 C; Discover at 25 C), -3 mV per cell per C (East Penn renewable VRLA at 25 C) and -6 mV for flooded in the same sheet; reference temperature and application differ, so they are not interchangeable.
- Absorption voltage differs with design, reference temperature and application: 2.35 (ZVEI PzV, 30 C), 2.37 (Stryten AGM220 constant voltage), 2.40 to 2.43 (East Penn AGM 8A, 20 C), up to 2.45 (Discover AGM, 25 C).
- Stryten AGM200 and AGM210 numeric rules were not found (the AGM200 manual came back fragmentary in French); HOPPECKE and Exide PzV traction instructions with numbers were not found beyond the stationary and rail Sonnenschein documents.
- **Curves:** none recorded yet; the staged tables above are the closest thing to a profile shape.

## Aliases

- VRLA charge profiles
- AGM and gel charge profiles

## Former ids
