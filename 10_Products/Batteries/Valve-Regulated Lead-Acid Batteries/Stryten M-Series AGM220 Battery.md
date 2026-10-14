---
type: Object
subtype: electrical
id: OBJ-00129
uid: 20261002194458533skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - battery
  - onboard-charger
subtypeOf:
  - "[[Valve-Regulated Lead-Acid Traction Battery]]"
describedBy:
  - "[[Document - Stryten M-Series Lineup Sheet (09-2024)]]"
  - "[[Document - Stryten M-Series AGM220 Manual (SE1041, 2023-04)]]"
  - "[[Document - Stryten M-Series AGM220 Brochure (SE1043)]]"
  - "[[Document - Stryten Marathon Pow'r Pak LD Page (retrieved 2026-10-13)]]"
performs:
  - "[[Charge Battery by Opportunity]]"
hasDesign:
  - "[[Battery Onboard Charger]]"
integratesWith:
  - "[[Stryten AGM220 Onboard Charger]]"
madeBy:
  - "[[Stryten Energy]]"
offeredWith:
  - "[[Stryten M-Series AGM210 Battery]]"
---

# Stryten M-Series AGM220 Battery

## Definition

Stryten integrated AGM battery and charger system for 24 V walkie pallet trucks.

## Notes

- Stryten says AGM220 is an integrated valve-regulated lead-acid battery and charging system for 24 V electric walkie pallet trucks with capacity up to 4,500 lb, housing a smart high-frequency charger with auto stop/start and four 6 V AGM210 batteries. Source: Stryten lineup sheet (09/2024) (T1), retrieved 2026-10-02. <https://og.mhi.org/media/members/14502/133723547947804003.pdf>
- **Design characteristics, with citations:**
  - [[Battery Onboard Charger]] (V): <https://og.mhi.org/media/members/14502/133723547947804003.pdf>
- Stryten's AGM220 installation and operating instructions say all AGM VRLA batteries must be given an equalizing charge before use, the onboard charger is matched to the battery's voltage and ampere-hour capacity, a Stryten-approved high-frequency charger with a CC-CV-CC profile and automatic charge termination is used, and the constant-voltage portion of the curve is set at 2.37 volts per cell; the product brochure says charging begins with constant current until the appropriate gassing voltage, then the charge adjusts to constant voltage, opportunity charging is advised between 30 and 70 percent state of charge, and temperature compensation is optional on the PalletPro systems. Source: Stryten AGM220 manual (SE1041) and brochure (SE1043), search snippets (T1), retrieved 2026-10-03. <https://www.stryten.com/wp-content/uploads/2023/03/Stryten-M-Series-I-O-Manual-AGM220-SE1041-April-2023.pdf>
- **Design characteristics, with citations (round 40, gap review 2026-10-03):**
  - [[Battery Onboard Charger]] (V): <https://www.stryten.com/wp-content/uploads/2023/03/Stryten-M-Series-I-O-Manual-AGM220-SE1041-April-2023.pdf>

- **Update 2026-10-13:** brochure SE1043 gives 24 V from four 6 V AGM210, 184 Ah at C/6, 365 lb, 12-month warranty, models M90004S24MARG / M90004S24MARTM / M90004S24MARX, I-E-I profile with 25 A start rate, opportunity charging at 30% to 70% depth of discharge (minimum half hour plus cool-down). The AGM220 was formerly the Marathon Pow'r Pak LD per Stryten's page; the 'PalletPro' name appears once in the brochure undefined (IB-186). Sources: <https://www.stryten.com/wp-content/uploads/2023/03/Stryten_M-SeriesProductBrochure_AGM220_SE1043_FINAL.pdf>; <https://stryten.com/marathon-powr-pak-ld/>. See [[Stryten AGM220 Onboard Charger]].

- **Functions performed, with citations (2026-10-13):**
  - [[Charge Battery by Opportunity]] (V): <https://www.stryten.com/wp-content/uploads/2023/03/Stryten_M-SeriesProductBrochure_AGM220_SE1043_FINAL.pdf>

## Aliases

- AGM220
- Marathon Pow'r Pak LD (former name)


## Former ids
