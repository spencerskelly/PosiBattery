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

- **Owner request (2026-10-03):** start adding data on charge and discharge patterns and curves; profile parameters first, then curves; flooded lead-acid first; battery maker charging guides first. This note is the profile-parameter layer; curves (voltage against time or capacity) are not added yet.
- **Scope:** flooded lead-acid traction batteries (PzS and PzB style and North American cells). Photovoltaic and cycling-battery tables are kept separate because they are other applications. Sealed AGM (East Penn 8A line) is shown only to mark the contrast.
- **Reading rule:** values come from maker manuals and snippets of them; where a page could not be fetched in full the cell says snippet. A parameter missing in one column was not found, not absent. Metric notes carry the values for products that have a note: [[Metric - Charge End Criterion]], [[Metric - Equalizing Charge Rule]], [[Metric - Full-Charge Specific Gravity]], [[Metric - Depth of Discharge Limit]], [[Metric - Charge Temperature Limits]], [[Metric - Float Voltage per Cell]].

**Parameters by source**

| Parameter | EnerSys HAWKER Perfect Plus (owner's manual 2024, T1, read in full) | East Penn Deka D-Series and MaxPowr (installation and operation manuals, T1, snippets) | Exide Industries traction manual (T1, snippet; page now 404) | GNB EPzS manual (T3, ManualsLib mirror, snippet) | HOPPECKE trak basic (T3, ManualsLib mirror, snippet) |
|---|---|---|---|---|---|
| Charge method | direct current only; charging procedures after DIN 41773-1 and 41774 permitted (as printed); current limits in the gassing stage per DIN EN 50272-3 | charger finish rate set per cell size (tables in the manual, not extractable); starting rate must match the battery | DC only | DC only; IU characteristic mentioned | DC only; IU characteristic mentioned |
| Start conditions | electrolyte below 45 C and at least 10 C; vent plugs closed; battery out of the closed compartment | n/s | below 45 C and at least 10 C | at least 10 C | n/s |
| End of charge | specific gravity and voltage constant for 2 hours | n/s | cell voltage reaches 2.65 V per cell, or the charger's dV/dt cut-off | specific gravity and voltage constant for 2 hours | n/s |
| Equalizing | after deep discharge, repeated incomplete charges and IU charges; at most 5 A per 100 Ah | every 1 to 4 weeks; charger set to equalize | starting current 3 percent of capacity in amperes; hourly readings | after IU charges (frequency cut off) | after IU charging |
| Temperature | rated 30 C; start below 45 C; upper limit 55 C | n/s | optimal life 15 to 35 C; upper limit 55 C | rated 30 C; upper limit 55 C | upper limit 55 C |
| Full-charge specific gravity | 1.29 kg/l at 30 C (nominal); correction -0.0007 kg/l per C | D-Series 1.280 to 1.295 at 25 C; MaxPowr 1.310 to 1.330 | 1.275 to 1.285 g/cc at 30 C | n/s | n/s |
| Discharge limit | at most 80 percent of rated capacity (specific gravity 1.14 kg/l at 30 C) | MaxPowr: below 1.155 specific gravity can harm (cut off) | n/s | at most 80 percent (text cut off) | at most 80 percent (text cut off) |
| Float or storage | 2.27 V per cell, or a monthly equalizing charge | n/s | n/s | float at 2.23 V per cell | n/s |
| Electrolyte circulation | optional; charge factor 1.07; for heavy duty, short charge times, boost or opportunity charging | n/s | n/s | n/s | n/s |

**Staged charge table (East Penn flooded cycling battery, T1, snippet)**

East Penn's 'Flooded Cycling-Battery Charging' sheet gives a staged profile for flooded, maintenance-accessible cycling batteries; the sheet does not say it is for forklift traction, so it is shown as a pattern, not as a traction rule.

| Stage | Control | End condition | Limits |
|---|---|---|---|
| Bulk (I1) | constant current, with constant power or taper permitted; at most 30 A per 100 Ah (C20) | voltage reaches 2.30 to 2.35 V per cell at 20 C | maximum time 1.3 times the depth of discharge in Ah divided by the average current; stop if exceeded |
| Absorption (V1) | constant terminal voltage 2.30 to 2.35 V per cell at 20 C, adjusted only for battery temperature | current acceptance falls by 3 to 5 A per 100 Ah (C20); then a level or falling voltage is measured and charging continues for 2 more hours (text cut off) | equalize once a week, otherwise go to float |
| Temperature compensation | subtract 0.005 V per cell for each degree above 20 C; add 0.005 V per cell for each degree below | no compensation needed below -20 C if frequent operation there is not expected | |

**Related, other applications**

- East Penn's sealed AGM guideline (8A line) uses 2.40 to 2.43 V per cell bulk and absorption at 20 C, an optional accelerated finishing stage of 1 to 2 A per 100 Ah and an optional float of 2.25 V per cell; it is a VRLA pattern, shown only for contrast.
- A Deka photovoltaic parameter sheet for flooded motive power gives bulk current of 20 percent of the 20 h rate, equalize at 2.50 to 2.55 V per cell and a temperature coefficient of -3 mV per cell per C at 25 C, with an average battery temperature not above 115 F (46 C); that is a solar application.

**Conflicts and gaps**

- Float or storage voltage differs: 2.27 V per cell (EnerSys) against 2.23 V per cell (GNB EPzS); see C97.
- The charge-end rule differs in kind: a 2 hour constant specific gravity and voltage (EnerSys, GNB) against a 2.65 V per cell or dV/dt cut-off (Exide Industries); see C97.
- Temperature compensation for voltage differs by application: -3 mV per cell per C (Deka photovoltaic) and -5 mV per cell per C above 20 C (East Penn cycling sheet); neither is stated for forklift chargers here.
- Not found yet: Stryten's charging guide, HOPPECKE's numeric operating instructions, the DIN EN 50272-3 gassing-stage current limits table, East Penn finish rates by cell size, and any charger-side algorithm values.
- **Curves:** no voltage-time or discharge-capacity curves are recorded yet; they would be added as approximate digitized points from datasheet charts, labelled as such.

## Aliases

- Charge profile comparison

## Former ids
