---
type: Info
subtype:
id: INFO-00975
uid: 20261017192000000skellyspencer
status: Draft
tags:
  - research
  - lead-acid
  - maintenance
  - battery-life
  - flooded
describes:
  - "[[Industrial Traction Battery]]"
  - "[[Battery Cell Watering Design]]"
  - "[[Lead-Acid Desulfation Charge Control Design]]"
  - "[[Temperature-Compensated Charge Control Design]]"
  - "[[Missed Equalization Recovery Design]]"
  - "[[Battery-Stored Equalization Schedule]]"
  - "[[Equalization Event Tracking Design]]"
describedBy:
  - "[[Document - Battery University BU-804b Sulfation and How to Prevent It (2024-02-08)]]"
  - "[[Document - Battery University BU-804 How to Prolong Lead-acid Batteries (2021-11-02)]]"
  - "[[Document - Battery University How to Store Batteries (retrieved 2026-10-17)]]"
  - "[[Document - ZVEI Leaflet 8e Service Life of Traction Batteries (2014-02)]]"
  - "[[Document - ZVEI Leaflet 13e Discharge Indicators for Lead-Acid Traction Batteries (2011-12)]]"
  - "[[Document - ZVEI Leaflet 10e Opportunity Charging of Lead-Acid Traction Batteries (2011-12)]]"
  - "[[Document - ZVEI Information Sheet 10 Rapid and Intermediate Charging of Drive Batteries (2026-03)]]"
  - "[[Document - ZVEI Leaflet 6e Cleaning of Batteries (2006)]]"
  - "[[Document - MHL News Faust Proper Care Safety and Maintenance of Forklift Batteries (2014-11-21)]]"
  - "[[Document - Cat Lift Trucks Forklift Battery Watering Guide (2026-09-18)]]"
  - "[[Document - Raymond West Tips to Extend the Life of Your Forklift Batteries (2023-01-30)]]"
  - "[[Document - EnerSys Maintenance and Service Instruction Sheet Water Less Perfect Plus Ironclad (EMEA 0724)]]"
---

# Lead-Acid Traction Battery Life Care Methods Register

## Definition

Register of the methods documented for keeping flooded lead-acid traction batteries in good condition for a long service life: what each method is, the rule or figure sources give, how well the claim is evidenced, and which vault products and designs implement it. It adds a life-care view over the charge-parameter work in [[Flooded Lead-Acid Charge Profile Comparison]]. Disagreements are numbered C338 to C346 in [[Battery Product Landscape Conflicts and Open Questions]]; new directions are IB-305 to IB-312 in [[Investigation Backlog]].

## Notes

- **Reading rule:** every source was read through a summarizing fetch tool (second-hand). ZVEI leaflets are industry association text, labelled T2 with a note by vault precedent; Battery University pages are T4. "Analyst reasoning" marks a conclusion no source states. Status is as of 2026-10-17.
- **Scope:** flooded (vented) PzS-style and North American traction batteries in forklifts and similar. Valve-regulated (AGM, gel) is mentioned only where a source separates it; see [[VRLA Charge Profile Comparison (AGM and Gel)]]. Starter, deep-cycle and stationary guidance is flagged where a source mixes it in.
- **Not repeated here:** charge parameters by maker are in [[Flooded Lead-Acid Charge Profile Comparison]]; cold-room rules are in [[Cold Storage Charging Rules for Traction Batteries (ZVEI)]].

### Bottom line (analyst summary)

1. **The sources give rules, not measured life gains.** The only quantified life statements are: a lab baseline of about 1500 cycles for PzS and 900 for PzV to 80 percent capacity (EN 60254-1); a 100 percent depth of discharge cutting life by about one third against the 80 percent operating capacity; PzV at 80 percent depth having two thirds of its indicated life; and one worked example where 45 C instead of 30 C average cut expected life from 60 to 29 months (other inputs also differ, so it is not a clean temperature effect). Nothing read quantifies the life gain from watering, equalizing, cleaning, circulation or desulfation. Any claim of "extends life by X percent" for those methods has no source in the vault (C346, IB-309).
2. **Depth of discharge and temperature have the strongest support.** ZVEI limits discharge to 80 percent and caps temperature at 55 C (flooded) and 45 C (VRLA); makers repeat the temperature limit. These two are also the methods a monitoring device can enforce or log.
3. **Everything else is a procedure with disagreeing details.** Equalizing frequency, watering timing and fill level, opportunity-charge current, cleaning agents and the weekly "14 to 16 hour" charge differ between sources (C338 to C345). Several sources are not independent: the dealer blog repeats a Battery University figure that was written for other battery types (C344).
4. **The newest ZVEI sheet changes the opportunity-charge numbers.** The 2011 leaflet allows up to 1.5 times I5 (0.3 C5) and warns about acid stratification above 80 percent of nominal capacity per day. The March 2026 sheet, now listed under the same number 10, gives 0.2 C for standard lead-acid and a 20 to 80 percent window, covers all chemistries and does not mention the older text (C339). Which one governs is unknown (IB-306).
5. **Desulfation is the least supported method.** Battery University says pulse devices cannot reverse established sulfation and prescribes a corrective charge at 2.50 to 2.66 V per cell for about 24 hours, with warming to 50 to 60 C, which exceeds the 55 C maker limit and the 45 C start limit in the EnerSys sheet (C342). The vault lists four charger products with a desulfation cycle; none publishes its mechanism ([[Lead-Acid Desulfation Charge Control Design]]).
6. **No traction-specific storage rule was found.** The storage thresholds read are for starter batteries (C345, IB-311).

### Methods table

| # | Method | What sources say | Evidence | Vault implementers |
|---|---|---|---|---|
| 1 | Limit depth of discharge to 80 percent of nominal; cut lift at the limit | Deep discharge is above 80 percent (density below 1.13 kg/l at 30 C or 1.97 V per cell open circuit); example cut-offs 1.86 V per cell at 20 A per 100 Ah and 1.79 V per cell at 30 A per 100 Ah; clean cut-off, not stepped current reduction; every deep discharge needs an equalising charge; 100 percent depth costs about one third of life ([[Document - ZVEI Leaflet 13e Discharge Indicators for Lead-Acid Traction Batteries (2011-12)]], [[Document - ZVEI Leaflet 8e Service Life of Traction Batteries (2014-02)]]) | Association leaflet; no maker source on the one-third figure | [[Protect Battery from Deep Discharge]], [[Truck Battery Discharge Interlock]], [[Metric - Depth of Discharge Limit]] |
| 2 | Charge fully with a matched charger; avoid under- and overcharge | Undersized charger sulfates positives; oversized sheds and burns positives ([[Document - MHL News Faust Proper Care Safety and Maintenance of Forklift Batteries (2014-11-21)]]); obsolete chargers cause under- or overcharge (ZVEI 8e); charge factors 1.04 to 1.2 ([[Document - EnerSys Maintenance and Service Instruction Sheet Water Less Perfect Plus Ironclad (EMEA 0724)]]) | Maker-authored trade article, maker sheet | [[Metric - Charge Factor]], [[Metric - Charge End Criterion]] |
| 3 | Equalizing charge | Weekly (Faust; dealer blog for opportunity or fast charging; EnerSys sheet); after deep discharge (ZVEI 13e); regular equalizing needed with opportunity charging to avoid stratification (ZVEI 8e) (C338) | Maker and association rules; no life figure | [[Equalize Battery on Schedule]], [[Track Equalization]], [[Complete Missed Equalization Automatically]], [[Battery-Stored Equalization Schedule]], [[Metric - Equalizing Charge Rule]] |
| 4 | Opportunity charging within a window | 2011: start after about 30 percent depth, up to 1.5 times I5, over 80 percent of Cn per day risks stratification, average temperature rises above 1.2 times Cn between full charges; 2026: 20 to 80 percent state of charge, 0.2 C (C339) | Association leaflets, two editions | [[Charge Battery by Opportunity]], [[Manage Temperature During Fast Charging]] |
| 5 | Keep electrolyte level correct | Water after charge (Cat guide, dealer blog, EnerSys: 20 minutes before end or right after) or during gassing at end of charge (Faust); cover plates before charge; fill to the maker level (1/4 inch below vent well in Faust, max mark in EnerSys); topping-up intervals 2 to 20 weeks (C340, C341) | Maker and truck-maker pages; no life figure | [[Water Battery Cells]], [[Battery Cell Watering Design]], [[Metric - Watering Interval]] |
| 6 | Use distilled or deionized water | pH 5 to 7; no tap water ([[Document - Cat Lift Trucks Forklift Battery Watering Guide (2026-09-18)]]); the EnerSys sheet states no purity | One truck-maker page; no conductivity limit found | none modelled (IB-307) |
| 7 | Keep electrolyte mixed | Opportunity charging without mixing or equalizing causes stratification (ZVEI 8e); circulation recommended for liquid electrolyte (ZVEI 2026); charge factor 1.07 with circulation | Association; maker | [[Forced Electrolyte Circulation]], [[Exide AIR Electrolyte Agitation System]], [[EnerSys Aeromatic Circulation System]] |
| 8 | Control temperature | Rated 30 C, maximum 55 C flooded, 45 C VRLA; EnerSys: start charging below 45 C; temperature-compensated charging recommended | Association and maker agree | [[Compensate Charge for Battery Temperature]], [[Temperature-Compensated Charge Control Design]], [[Metric - Charge Temperature Limits]] |
| 9 | Prevent and treat sulfation | Avoid prolonged low charge and repeated deep discharge; periodic saturation charge; corrective 2.50 to 2.66 V per cell for about 24 hours (C342, C344) | Battery University (T4), ZVEI | [[Desulfate Battery During Charge]], [[Lead-Acid Desulfation Charge Control Design]] |
| 10 | Monitor cells | Monthly hydrometer on every cell after charge (Faust); cell voltage monitoring called essential (EnerSys); insulation at least 50 ohm per volt | Maker | [[Measure Electrolyte Specific Gravity]], [[Document Battery Care for Warranty Compliance]] |
| 11 | Clean | Water only on plastic, no cleaning agents, high-pressure limits (ZVEI 6e); neutralizing cleaner on top monthly (Faust) (C343) | Association; maker-authored article | none modelled |
| 12 | Store charged and cool | Starter-battery thresholds only (C345) | Battery University (T4) | none modelled (IB-311) |

### What the vault does and does not cover (analyst reasoning)

- **Covered by product notes:** watering systems, watering monitors, electrolyte circulation, equalization scheduling and tracking, temperature compensation, desulfation cycles, and the discharge interlock.
- **Not modelled:** water-quality control, cleaning, storage, stratification detection, and any measure of whether a care rule was actually followed. The last matters for the customer needs [[Document Battery Care for Warranty Compliance]], [[Prevent Battery Abuse and Premature Replacement]] and [[Keep Trucks Working Without Battery Maintenance Labor]].

### Hypotheses (analyst reasoning, untested)

- **LH1:** a monitor or charger can best claim value for the two methods with quantified life effects (depth of discharge, temperature) and for proof of compliance, not for life-extension percentages. Test: IB-309, IB-312.
- **LH2:** the "desulfation cycle" in chargers is an extended high-voltage low-current charge similar to the Battery University recipe, not pulse hardware. Test: IB-310.
- **LH3:** field data from PosiCharge BMID or Battery Rx logs could quantify what no source here does (care compliance against battery life). Test: IB-312.

### Question for the owner

Does PosiCharge hold field data linking care practice (equalization compliance, depth of discharge, temperature) to battery life, from BMID or Battery Rx logs or customer warranty claims? It is the only route to a quantified claim, since no source read gives one.

## Open questions

- Which ZVEI sheet governs opportunity charging, and what do IEC TS 61044 and EN 50272-3 specify (IB-305, IB-306)?
- Water purity limits, fill levels and intervals from maker manuals (IB-307).
- Independent evidence of life effect for watering, equalizing and cleaning (IB-309).
- Mechanism of charger desulfation cycles (IB-310).

## Sources

Listed in `describedBy`. Not read: IEC TS 61044:2021, EN 50272-3 / IEC 62485-3 (paid), ZVEI leaflets 11e, 14e, 23e.

## Aliases

- Lead-Acid Care Register

## Former ids
