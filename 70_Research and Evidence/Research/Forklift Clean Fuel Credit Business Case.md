---
type: Info
subtype:
id: INFO-00961
uid: 20261017143001000skellyspencer
status: Draft
tags:
  - research
  - business-case
  - forklift
  - clean-fuel-program
  - credit-price
  - north-america
describes:
  - "[[Industrial Battery Charger]]"
describedBy:
  - "[[Document - Washington Ecology Clean Fuel Standard Report for Calendar Year 2024 (publication 26-14-043)]]"
  - "[[Document - 17 CCR 95484 Cornell LII Page (retrieved 2026-10-17)]]"
  - "[[Document - PG&E EV Fleet Low Carbon Fuel Standard Flyer (undated)]]"
  - "[[Document - FuSE CARB's 2025 LCFS Regulation Amendments Electricity Credit Generation (2024-11-14)]]"
  - "[[Document - CCarbon Oregon CFP Remains Balanced Amid Evolving Renewable Diesel Dynamics (2026-05-08)]]"
  - "[[Document - CARB 2026 California Average Grid Electricity Carbon Intensity Update]]"
  - "[[Document - 7Gen CFR Credit Price in 2026 (2026-06-11)]]"
  - "[[Document - W-Carbon Low Carbon Fuel Credits Refresh (2025-05-16)]]"
  - "[[Document - CARB Weekly LCFS Credit Transfer Activity Reports Page (retrieved 2026-10-17)]]"
  - "[[Document - Oregon DEQ Forklift Methodology Meeting Deck (2023-05-30)]]"
  - "[[Document - 17 CCR 95486.1 Cornell LII Page (retrieved 2026-10-17)]]"
---

# Forklift Clean Fuel Credit Business Case

## Definition

Business case note on whether clean fuel credits for forklift charging justify charger-side data and metering features: credit prices, credit yield per MWh, market evidence and the gaps that block a decision. Evidence sits on the Document notes; disagreements are numbered C296 onward in [[Battery Product Landscape Conflicts and Open Questions]].

## Notes

- **Reading rule:** sources are second-hand through a summarizing fetch tool; trade, vendor and utility sources are T4 and interested parties; agency sources sit outside T1 to T5. Calculations are the analyst's and are labeled. Status as of 2026-10-17.
- **Question:** do clean fuel credits give forklift owners enough money to justify charger-side data and metering features? This note gathers prices, per-MWh yields and market evidence, and lists what is missing. It does not recommend a product investment.

### Bottom line (analyst summary)

1. **California credit value is about $25 to $68 per MWh of charging energy,** depending on which forklift EER applies ($25.40 at 1.9, $36.55 at 2.4, $67.80 at 3.8) at the $72.61 per tonne weekly average in mid-2026 and assuming the benchmark and grid CI below. The adopted EER is unconfirmed, and it moves the result by a factor of 2.7 (C296).
2. **Charger efficiency changes the reportable energy by up to 11.8 percent** when the meter is upstream of the charger (95 percent versus the 85 percent default), worth about $3.65 per MWh at EER 2.4 (analyst calculation).
3. **No source gives annual kWh per forklift,** so revenue per truck cannot be computed from sources. The one worked example found (PG&E, $1,360 a year) cannot be reconciled with CARB's current factors (C297). Real kWh data from PosiLink or E-Meter would close this (IB-258).
4. **Prices differ a lot by program and are mostly stale:** California $72.61 in mid-2026 (CARB), Washington $45.92 average for 2024 (Ecology), Oregon $47.98 in April 2025 (newsletter), and a vendor claim of Canadian credits above $400 each in early 2026. Oregon and Washington 2026 prices were not obtained.
5. **Forklifts are a material share of credits where counted:** Oregon had more than 3,500 registered electric forklifts in May 2023, producing over a third of electricity credits ([[Document - Oregon DEQ Forklift Methodology Meeting Deck (2023-05-30)]]).

### Table 1: credit prices found

| Program | Price | Date | Source |
|---|---|---|---|
| California LCFS | $72.61 per metric ton (all non-zero transfers); $74.35 Type 1 | Weekly log to 2026-07-19 | [[Document - CARB Weekly LCFS Credit Transfer Activity Reports Page (retrieved 2026-10-17)]] |
| California LCFS | about $64 | April 2025 monthly average | [[Document - W-Carbon Low Carbon Fuel Credits Refresh (2025-05-16)]] (T4) |
| Oregon CFP | $47.98 | April 2025 monthly average | [[Document - W-Carbon Low Carbon Fuel Credits Refresh (2025-05-16)]] (T4) |
| Washington CFS | $45.92 volume-weighted average; monthly $23.88 to $89.89 | Calendar 2024 | [[Document - Washington Ecology Clean Fuel Standard Report for Calendar Year 2024 (publication 26-14-043)]] |
| Washington CFS | $28.86 | April 2025 monthly average | [[Document - W-Carbon Low Carbon Fuel Credits Refresh (2025-05-16)]] (T4) |
| Canada CFR | above $400 per credit (vendor claim; per-tonne basis unclear) | Early 2026 | [[Document - 7Gen CFR Credit Price in 2026 (2026-06-11)]] (T4, interested) |
| New Mexico CTFP | $100 per credit (a projection used in revenue tables) | 2027 estimate | [[Document - New Mexico CTFP Roads to Revenue with Fleet Electrification (2026-07)]] |
| British Columbia | Not found | - | [[Document - Xpansiv British Columbia LCFS Market Page (retrieved 2026-10-17)]] |
| Oregon credit bank | about 0.61 million tonnes at end of 2025 (a surplus of credits) | Q4 2025 | [[Document - CCarbon Oregon CFP Remains Balanced Amid Evolving Renewable Diesel Dynamics (2026-05-08)]] (T4) |

### Calculation: California credits per MWh of charging energy (analyst calculation)

Credits (tonnes) = (benchmark x EER - grid CI) x 3.6 MJ per kWh x 1,000 kWh per MWh / 1,000,000. Inputs: benchmark 85.38 gCO2e/MJ for 2026 ([[Document - 17 CCR 95484 Cornell LII Page (retrieved 2026-10-17)]]; probably before the 2025 amendments, C298); grid CI 65.07 gCO2e/MJ for 2026 ([[Document - CARB 2026 California Average Grid Electricity Carbon Intensity Update]]); price $72.61 per tonne ([[Document - CARB Weekly LCFS Credit Transfer Activity Reports Page (retrieved 2026-10-17)]]). It assumes forklift charging uses the annual-average grid CI and that the benchmark applies unchanged.

| Forklift EER | Credits per MWh (t) | Value per MWh at $72.61 | Value per MWh per $10 of price |
|---|---|---|---|
| 3.8 (Cornell table; probably before the 2025 amendments) | 0.934 | 67.80 | 9.34 |
| 2.4 (FuSE; unverified) | 0.503 | 36.55 | 5.03 |
| 1.9 (proposal in a 2024 comment letter; unverified) | 0.350 | 25.40 | 3.50 |

With the benchmark cut 9 percent (77.70 gCO2e/MJ, an illustrative sensitivity because the 2025 amendments include a one-time 9 percent cut per [[Document - FuSE CARB's 2025 LCFS Regulation Amendments Electricity Credit Generation (2024-11-14)]]), EER 2.4 gives 0.437 t per MWh, or $31.73 per MWh.

### Table 2: effect of charger efficiency at EER 2.4 (meter upstream of the charger)

Reportable energy = metered energy x charger efficiency ([[Document - CARB LCFS Guidance 25-01 Forklift Fueling Reporting (2025-10)]]). Vault charger efficiencies run 90 to 97 percent ([[Metric - Peak Efficiency]]); which efficiency CARB means is open (C287).

| Efficiency used | Credits per MWh metered (t) | Value per MWh metered at $72.61 |
|---|---|---|
| 85 percent (CARB default) | 0.428 | 31.07 |
| 90 percent | 0.453 | 32.90 |
| 95 percent | 0.478 | 34.73 |

### Market evidence found

- **California:** CARB counts more than 89,000 spark-ignited forklifts statewide across all fleets (see [[California Forklift Electrification Regulations Register]]); the electric share is unknown.
- **Oregon:** more than 3,500 electric forklifts registered by May 2023; forklift credits over a third of electricity credits [[Document - Oregon DEQ Forklift Methodology Meeting Deck (2023-05-30)]].
- **Vendors already sell the data layer:** Smart Charging Technologies sells meters at the charger output, panel or forklift ([[Document - Smart Charging Technologies Letter to Oregon DEQ on Forklift Metering Options (2023-05-15)]], T4); 3Degrees and 7Gen sell credit-generation services ([[Document - 3Degrees Revenue Streams from Electric Forklifts Under Clean Fuel Standards (2025-09-25)]], [[Document - 7Gen CFR Credit Price in 2026 (2026-06-11)]], T4). A charger maker would compete with, or partner with, these.
- **Utility role:** PG&E tells fleets they may generate credits and offers help with a dedicated meter ([[Document - PG&E EV Fleet Low Carbon Fuel Standard Flyer (undated)]]).

### Gaps that block a business decision

- **Annual kWh per forklift** and the share of customers that claim credits: needs PosiCharge fleet data and customer interviews (IB-258, IB-252).
- **Adopted California forklift EER** and the 2026 benchmark in force (C296, C298; IB-242).
- **Oregon and Washington 2026 prices and EER values** (IB-259).
- **Aggregator fees:** what vendors keep from each credit (IB-262).
- **Competing and partner offers** at the charger or panel level (IB-263).

### Implications (analyst reasoning, hypotheses only)

- **H11:** the credit is worth tens of dollars per MWh in California at current prices. For a truck charged with 10 MWh a year (an illustrative figure, not sourced), that is a few hundred dollars a year; the actual figure depends on the real kWh. Whether this changes a purchase decision depends on fleet size and on how much customers value avoiding manual meter work. This is not a demonstrated willingness to pay.
- **H12:** the most robust product value is accurate, auditable energy data (identity of the measuring point, no hidden adjustment), because it serves California, Oregon and the New Mexico metered-kWh rule at once (REQ-00058).
- **H13:** efficiency disclosure is worth a few dollars per MWh in California; this is small compared with the data and verification effort, so it is a secondary lever.

### Sources

- Prices: [[Document - CARB Weekly LCFS Credit Transfer Activity Reports Page (retrieved 2026-10-17)]]; [[Document - Washington Ecology Clean Fuel Standard Report for Calendar Year 2024 (publication 26-14-043)]]; [[Document - W-Carbon Low Carbon Fuel Credits Refresh (2025-05-16)]]; [[Document - 7Gen CFR Credit Price in 2026 (2026-06-11)]]; [[Document - New Mexico CTFP Roads to Revenue with Fleet Electrification (2026-07)]]; [[Document - CCarbon Oregon CFP Remains Balanced Amid Evolving Renewable Diesel Dynamics (2026-05-08)]].
- Factors: [[Document - CARB 2026 California Average Grid Electricity Carbon Intensity Update]]; [[Document - 17 CCR 95484 Cornell LII Page (retrieved 2026-10-17)]]; [[Document - 17 CCR 95486.1 Cornell LII Page (retrieved 2026-10-17)]]; [[Document - FuSE CARB's 2025 LCFS Regulation Amendments Electricity Credit Generation (2024-11-14)]]; [[Document - Smart Charging Technologies Comment Letter on Electric Forklift EER (2024-05-09)]].
- Market: [[Document - Oregon DEQ Forklift Methodology Meeting Deck (2023-05-30)]]; [[Document - Smart Charging Technologies Letter to Oregon DEQ on Forklift Metering Options (2023-05-15)]]; [[Document - PG&E EV Fleet Low Carbon Fuel Standard Flyer (undated)]].

## Aliases

- Forklift credit business case

## Former ids
