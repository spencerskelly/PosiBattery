---
type: Object
subtype: electrical
id: OBJ-00128
uid: 20261002194458532skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - battery
subtypeOf:
  - "[[Valve-Regulated Lead-Acid Traction Battery]]"
describedBy:
  - "[[Document - Stryten M-Series AGM200 Brochure (SE1047, 5-24)]]"
  - "[[Document - Stryten M-Series AGM200 Manual (SE1045, French-Canada)]]"
performs:
  - "[[Alert on Abnormal Condition]]"
hasDesign:
  - "[[Battery Discharge Indicator]]"
madeBy:
  - "[[Stryten Energy]]"
---

# Stryten M-Series AGM200 Battery

## Definition

Stryten AGM battery that never needs watering, for light retail and medium warehouse material handling.

## Notes

- Stryten's lineup sheet says AGM200 valve-regulated lead-acid batteries never need watering and suit light retail and medium warehouse applications. Source: Stryten lineup sheet (09/2024) (T1), retrieved 2026-10-02. <https://og.mhi.org/media/members/14502/133723547947804003.pdf>
- **Functions performed, with citations:**
  - [[Alert on Abnormal Condition]] (V, partial): a discharge alarm sounds an intermittent 80 dB tone at the alarm reference voltage and continuously at 80 percent depth of discharge; the alarm is the only monitoring feature described. <https://www.stryten.com/wp-content/uploads/2024/04/Stryten_M-Series_I-O_Manual_AGM200_SE1045_French-Canada_Final.pdf>
- **Design characteristics, with citations:**
  - [[Battery Discharge Indicator]] (V, partial): audible discharge alarm on the battery; no display. <https://www.stryten.com/wp-content/uploads/2024/04/Stryten_M-Series_I-O_Manual_AGM200_SE1045_French-Canada_Final.pdf>
- Stryten's AGM200 manual (French-Canada edition, SE1045) says every AGM200 must receive an equalizing charge before use, the charger must be a Stryten-approved one, a cooling period after a charge equal to the charge duration is mentioned, and the battery is equipped with an alarm (the rest of the sentence is cut off); the retrieved copy is fragmentary. Source: Stryten AGM200 manual (SE1045), search snippet (T1), retrieved 2026-10-03. <https://www.stryten.com/wp-content/uploads/2024/04/Stryten_M-Series_I-O_Manual_AGM200_SE1045_French-Canada_Final.pdf>

- **Fuller sources found 2026-10-13 (read through a summarizing tool, IB-178):** [[Document - Stryten M-Series AGM200 Brochure (SE1047, 5-24)]] <https://stryten.com/wp-content/uploads/2023/03/Stryten-M-Series-Product-Brochure-AGM200-SE1047.pdf>; [[Document - Stryten M-Series AGM200 Manual (SE1045, French-Canada)]] <https://www.stryten.com/wp-content/uploads/2024/04/Stryten_M-Series_I-O_Manual_AGM200_SE1045_French-Canada_Final.pdf>. The manual text below replaces the fragmentary snippet above; the snippet is kept.
- **Construction (brochure SE1047, 5/24):** AGM valve-regulated lead-acid, medium duty, classes I to III; welded powder-coated steel tray; copper posts; SB and Euro connectors; table of eight models (45B to 105B) at "Ah per positive at 6-hour rate" (45 to 105); a "Plates" column is not defined. <https://stryten.com/wp-content/uploads/2023/03/Stryten-M-Series-Product-Brochure-AGM200-SE1047.pdf>
- **Charging rules (manual SE1045):** Stryten-approved charger only; constant current, constant voltage, constant current with automatic charge control; finishing rate 2 A per 100 Ah; 2.37 V per cell; normally eight hours or less from 80 percent depth of discharge; cool for at least as long as the charge lasted; equalizing charge before first use and every 50 to 100 operating hours (every two weeks if hours unknown); opportunity charging not allowed except approved VGA applications (7-hour charge, 17-hour discharge control per 24 hours). <https://www.stryten.com/wp-content/uploads/2024/04/Stryten_M-Series_I-O_Manual_AGM200_SE1045_French-Canada_Final.pdf>
- **Operating limits:** 15 to 38 C normal range; do not discharge below 1.86 V per cell under load or 2.02 V per cell open circuit (80 percent depth of discharge); no more than 80 percent of rated capacity within six hours; state of charge cannot be read from specific gravity. <https://www.stryten.com/wp-content/uploads/2024/04/Stryten_M-Series_I-O_Manual_AGM200_SE1045_French-Canada_Final.pdf>
- **Warranty conditions:** voided by removing vent caps, by adding monitoring devices without written authorization, or by tampering with monitoring devices. <https://www.stryten.com/wp-content/uploads/2024/04/Stryten_M-Series_I-O_Manual_AGM200_SE1045_French-Canada_Final.pdf>
- **Conflict kept visible:** the brochure says AGM technology removes daily watering and "acid equalization maintenance", while the manual requires equalizing charges (C219).
- **Not stated:** voltage, cycle life, warranty period, dimensions, weight; the manual is the French-Canada edition, so an English manual is still wanted.

## Aliases

- AGM200


## Former ids
