---
type: Info
subtype:
id: INFO-00261
uid: 20261003200834303skellyspencer
status: Draft
tags:
  - charge-profile
  - flooded
  - comparison
  - review
describes:
  - "[[Industrial Traction Battery]]"
---

# Flooded Lead-Acid Charge Profile Comparison

## Definition

Charge and discharge rules for flooded lead-acid traction batteries as stated in maker manuals, side by side, with the sources, tiers and conflicts.

## Notes

- **Owner request (2026-10-03):** start adding data on charge and discharge patterns and curves; profile parameters first, then curves; flooded lead-acid first; battery maker charging guides first. Round 35 added Stryten, the ZVEI industry leaflet and the DIN characteristic notation. This note is the profile-parameter layer; curves (voltage against time or capacity) are not added yet.
- **Scope:** flooded lead-acid traction batteries (PzS and PzB style and North American cells). Photovoltaic, cycling-battery and VRLA tables are kept separate because they are other applications.
- **Reading rule:** values come from maker manuals and snippets of them; where a page could not be fetched in full the cell says snippet. A parameter missing in one column was not found, not absent. Metric notes carry values for products that have a note: [[Metric - Charge End Criterion]], [[Metric - Equalizing Charge Rule]], [[Metric - Full-Charge Specific Gravity]], [[Metric - Depth of Discharge Limit]], [[Metric - Charge Temperature Limits]], [[Metric - Float Voltage per Cell]], [[Metric - Charge Rate Taper]], [[Metric - Charge Factor]]. Charger characteristic codes are explained in [[Traction Battery Charging Characteristics (DIN Notation)]].

**Parameters by source**

| Parameter | EnerSys HAWKER Perfect Plus (manual 2024, T1, read in full) | East Penn Deka D-Series and MaxPowr (manuals, T1, snippets) | Stryten M-Series T300, T310, T330 (manuals, T1, snippets) | Exide Industries (T1 snippet; page now 404) | GNB EPzS and HOPPECKE trak basic (T3 ManualsLib mirrors, snippets) | ZVEI leaflet (T2 association, read in full) |
|---|---|---|---|---|---|---|
| Charge method | DC only; procedures after DIN 41773-1 and 41774 permitted; gassing-stage current limits per DIN EN 50272-3 | charger finish rate by cell size (tables not extractable); starting rate must match the plate | starting rate 3 times the finish rate (T310-FP 3 to 5 times), tapering to the finish rate by 85 percent charged; do not charge intermittently (T310-FP) | DC only | DC only; DIN 41773 and 41774 procedures permitted; gassing-stage limits per EN 50272-3 | regimes W, Wa, W0Wa, Wsa, IUIa by charger; see the characteristics note |
| Gassing voltage | n/s | n/s | n/s | n/s | n/s | 2.4 V per cell at 30 C |
| Start conditions | electrolyte below 45 C and at least 10 C; battery out of the closed compartment | n/s | let the battery reach room temperature before charging | below 45 C and at least 10 C | at least 10 C | n/s |
| End of charge | specific gravity and voltage constant for 2 hours | n/s | freshening charge until specific gravity shows no increase for three readings (T310-FP) | 2.65 V per cell, or the charger's dV/dt cut-off | specific gravity and voltage constant for 2 hours | end-of-charge voltage 2.65 V per cell is the DIN reference, real values vary |
| Charge factor | 1.07 with electrolyte circulation | n/s | n/s | n/s | n/s | 1.2 standard vented; about 1.07 with air mix; 1.17 Wsa; 1.1 gel PzV |
| Equalizing | after deep discharge, repeated incomplete charges and IU charges; at most 5 A per 100 Ah | every 1 to 4 weeks; charger set to equalize | once a week; 3 or 4 hours at the finish rate | starting current 3 percent of capacity in amperes; hourly readings | after IU charges; at most 5 A per 100 Ah | equalising charge named as an assignment criterion |
| Temperature | rated 30 C; start below 45 C; upper limit 55 C | n/s | average above 125 F is a condition for action; rise above 25 F (14 C) during charge (T330) | optimal 15 to 35 C; upper limit 55 C | rated 30 C; upper limit 55 C | reference 30 C |
| Full-charge specific gravity | 1.29 kg/l at 30 C (nominal); correction -0.0007 kg/l per C | D-Series 1.280 to 1.295 at 25 C; MaxPowr 1.310 to 1.330 | specific gravity spread of 0.020 or more is a condition for action | 1.275 to 1.285 g/cc at 30 C | correction -0.0007 kg/l per C | n/s |
| Discharge limit | at most 80 percent (1.14 kg/l at 30 C) | MaxPowr: below 1.155 can harm (cut off) | do not discharge the battery (text cut off) | n/s | at most 80 percent (cut off) | reference 80 percent; PzV optimized at 60 percent |
| Float or storage | 2.27 V per cell, or a monthly equalizing charge | n/s | n/s | n/s | GNB: float at 2.23 V per cell | n/s |
| Fast or opportunity charging | circulation helps heavy duty, short charge times, boost and opportunity charging | n/s | rapid charging equipment must be approved by Stryten Application Engineering; fast charge during breaks | n/s | n/s | opportunity charges are partial and cannot replace full charges |

**Staged charge table (East Penn flooded cycling battery, T1, snippets of one sheet; correction in round 35)**

East Penn's 'Flooded Cycling-Battery Charging' sheet gives a staged profile for flooded, maintenance-accessible cycling batteries; it does not say it is for forklift traction, so it is a pattern, not a traction rule.

| Stage | Control | End condition | Limits |
|---|---|---|---|
| Bulk (I1) | constant current, constant power or taper permitted; at most 30 A per 100 Ah (C20) | voltage reaches 2.30 to 2.35 V per cell at 20 C | maximum time 1.3 times the depth of discharge in Ah divided by the average current; stop if exceeded |
| Absorption (V1) | constant terminal voltage 2.30 to 2.35 V per cell at 20 C, adjusted only for battery temperature | current acceptance drops by less than 10 percent, or by less than 0.1 A, over a 1 hour period (text cut off after 'a 1') | equalize once a week, otherwise go to float |
| Equalize | charge until a level or declining voltage is measured, then continue at that rate for 2 additional hours (unit cut off in the snippet) | the 3 to 5 A per 100 Ah (C20) figure that round 34 placed under absorption belongs to this equalize stage's current, as the second snippet of the same sheet shows | |
| Temperature compensation | subtract 0.005 V per cell for each degree above 20 C; add 0.005 V per cell for each degree below | not needed below -20 C if frequent operation there is not expected | |

**Related, other applications**

- East Penn's sealed AGM guideline (8A line): 2.40 to 2.43 V per cell bulk and absorption at 20 C, an optional accelerated finishing stage of 1 to 2 A per 100 Ah and an optional float of 2.25 V per cell; a VRLA pattern, shown for contrast.
- A Deka photovoltaic parameter sheet for flooded motive power: bulk current 20 percent of the 20 h rate, equalize at 2.50 to 2.55 V per cell, temperature coefficient -3 mV per cell per C at 25 C, average battery temperature not above 115 F (46 C); a solar application.
- Discover Battery (deep-cycle and semi-traction maker, T3 learning-center page): equalize flooded batteries when specific gravity varies by 0.015 cell to cell on a fully charged battery, let the voltage rise to 2.65 V per cell, plus or minus 0.05 V, and stop when specific gravity no longer rises; not for AGM or gel. A different product family from forklift traction; its 2.65 V per cell matches the Exide Industries and DIN reference figure. <https://discoverbattery.com/support/learning-center/battery-101/how-to-equalize-charge-a-flooded-battery>

**Conflicts, corrections and gaps**

- **Correction (round 35):** round 34 placed the '3 to 5 A per 100 Ah' figure and the 2-hour continuation under East Penn's absorption stage; a second snippet of the same sheet shows absorption ends on a current-acceptance drop of less than 10 percent or 0.1 A over an hour, and the 3 to 5 A figure belongs with the equalize stage. The table above is corrected; C97 records it.
- Float or storage voltage differs: 2.27 V per cell (EnerSys) against 2.23 V per cell (GNB EPzS); C97.
- The charge-end rule differs in kind: constant specific gravity and voltage for 2 hours (EnerSys, GNB), no rise in specific gravity (Stryten), 2.65 V per cell or dV/dt cut-off (Exide Industries); C97.
- Equalizing frequency differs: after specific events (EnerSys, GNB), every 1 to 4 weeks (East Penn), once a week (Stryten); C97.
- **Temperature coefficient for voltage (round 37):** ZVEI recommends -0.004 V per cell per K from 0 to 40 C with a PzS charge voltage of 2.40 V at 30 C (IUI characteristic; see [[Cold Storage Charging Rules for Traction Batteries (ZVEI)]]), against East Penn's -0.005 V per cell per C at 20 C for flooded cycling batteries and -6 mV in its renewable sheet; reference temperature and application differ; C99.
- Identical text: the EnerSys, GNB and HOPPECKE manuals share the same wording on DC charging, DIN 41773 and 41774, 5 A per 100 Ah equalizing, 55 C and -0.0007 kg/l per C; they follow a common template, so they are not independent confirmations of each other.
- Not found: the EN 62485-3 Table 1 final-current values (paid standard), HOPPECKE's own numeric charging values beyond the template text, East Penn and Stryten finish-rate tables by cell size (not extractable), and charger-side algorithm values.
- **Curves:** no voltage-time or discharge-capacity curves are recorded yet; the ZVEI leaflet's diagrams are shapes, not tabulated points.

## Aliases

- Charge profile comparison

## Former ids
