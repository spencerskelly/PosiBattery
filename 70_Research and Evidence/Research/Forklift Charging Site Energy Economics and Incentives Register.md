---
type: Info
subtype:
id: INFO-00962
uid: 20261017170010000skellyspencer
status: Draft
tags:
  - research
  - site-energy
  - incentive
  - business-case
  - forklift
  - north-america
describes:
  - "[[Industrial Battery Charger]]"
describedBy:
  - "[[Document - Wu et al Energy Consumption Analysis of High-Voltage Lithium Electric Forklifts (Applied Sciences 2025)]]"
  - "[[Document - SRP E-Tech Program Factsheet FY27 (2026-05)]]"
  - "[[Document - Southwest Iowa REC Commercial Electric Forklifts Rebate C15 (2021)]]"
  - "[[Document - Apache Electric Vehicles How Much Electricity Does a Forklift Use in a Year (blog)]]"
  - "[[Document - Connexus Energy Electric Forklift Rebates (2026)]]"
  - "[[Document - Mass Save Electric Forklifts and Chargers Rebate Page (2026)]]"
  - "[[Document - Burlington Electric Department Electric Forklifts Rebate Page (retrieved 2026-10-17)]]"
  - "[[Document - ANL ESD 08-3 Full Fuel-Cycle Comparison of Forklift Propulsion Systems]]"
  - "[[Document - SRP E-Tech Forklift Program Flyer (program year 2022-23)]]"
  - "[[Document - IRS Instructions for Form 8911 Alternative Fuel Vehicle Refueling Property Credit (2025-12)]]"
---

# Forklift Charging Site Energy Economics and Incentives Register

## Definition

Register of what a forklift charging site pays for energy and what outside money offsets it: annual energy per truck, utility rebates for trucks and chargers, the federal refueling credit, and demand-charge exposure. Evidence sits on the Document notes; disagreements are numbered C310 onward in [[Battery Product Landscape Conflicts and Open Questions]]. It complements the credit view in [[Forklift Clean Fuel Credit Business Case]] and the qualitative research in [[Cost Driver 08 Utilities and Energy]].

## Notes

- **Reading rule:** sources are second-hand through a summarizing fetch tool; vendor blogs are T4 and interested parties; utility and government publications sit outside T1 to T5. Calculations are the analyst's and labeled. Status as of 2026-10-17. It does not recommend a product investment.

### Annual energy per truck (the missing input, bounded)

| Source | Basis | Per truck per year |
|---|---|---|
| [[Document - ANL ESD 08-3 Full Fuel-Cycle Comparison of Forklift Propulsion Systems]] | 7.5 kWh per hour purchased (5,000 lb truck, EPRI 2001) x 500 to 3,500 hours | 3.75 to 26.25 MWh (analyst product) |
| [[Document - ANL ESD 08-3 Full Fuel-Cycle Comparison of Forklift Propulsion Systems]] | Same source: average 1.5 shifts x 5 days x 52 weeks x about 6 hours | about 17.6 MWh (analyst) |
| [[Document - Apache Electric Vehicles How Much Electricity Does a Forklift Use in a Year (blog)]] (T4, interested) | By shift pattern, 250 days | 6.5 to 8 MWh (one shift); 13 to 16 (two); 19 to 25+ (three); headline 10 to 20 MWh |
| [[Document - Wu et al Energy Consumption Analysis of High-Voltage Lithium Electric Forklifts (Applied Sciences 2025)]] | 1.11 kWh per hour measured, 3-ton lithium prototype, battery side | not annualized; about 1.1 to 2.2 MWh at 1,000 to 2,000 hours (analyst) |
| [[Document - CARB Standardized Regulatory Impact Assessment, Appendix B-2 (zero-emission forklifts)]] (added 2026-10-18) | 7.5 kWh per operating hour x 1,848 hours a year, both regulator assumptions from CARB's LSI Inventory Model | 13.86 MWh (analyst product; an assumption, not a measurement) |

Working range used for illustrations (analyst reasoning): 5 to 20 MWh per truck per year, central 10 MWh. Sources disagree by a factor of 2 to 7 on hourly energy because they measure different things (wall versus battery, old versus new trucks, class and duty) (C310). **No measurement from PosiCharge or customer data is on file** (IB-258).

### Utility rebates seen (one-time, per unit)

| Program | Forklift | Charger | Conditions | Period | Source |
|---|---|---|---|---|---|
| Mass Save (MA utilities) | $6,000 | $550 high-frequency | Forklift replaces propane; charger efficiency 90 percent or more, input above 2 kW, new or replacing SCR or ferroresonant | Purchase in 2026 | [[Document - Mass Save Electric Forklifts and Chargers Rebate Page (2026)]] |
| SRP (AZ) FY27 | $2,000 replacing ICE; $800 expansion; $300 Class 3 | $180 high-frequency | Eligible price plans listed | 2026-05-01 to 2027-04-30 | [[Document - SRP E-Tech Program Factsheet FY27 (2026-05)]] |
| SRP (AZ) 2022-23 | up to $2,000; $500 additional | up to $150 | Charger at least 89 percent efficient, network-enabled and demand-response capable, 24 to 48 V | Expired | [[Document - SRP E-Tech Forklift Program Flyer (program year 2022-23)]] |
| Burlington Electric (VT) | $6,000 new | none stated | At least 3,000 lb; one per account | Through 2026-12-31 | [[Document - Burlington Electric Department Electric Forklifts Rebate Page (retrieved 2026-10-17)]] |
| Connexus Energy (MN co-op) | $2,000; $500 retention | $75 per shift of use | At least 40 hours a week; 50 percent of cost cap; $30,000 per member per year | Apply by 2026-12-15 | [[Document - Connexus Energy Electric Forklift Rebates (2026)]] |
| Southwest Iowa REC | $1,000 (Class 1 or 2) | none | Expired | 2021 | [[Document - Southwest Iowa REC Commercial Electric Forklifts Rebate C15 (2021)]] |

Patterns (analyst reasoning): trucks replacing propane draw $2,000 to $6,000 in 2026; charger rebates are small ($150 to $550) but carry specification gates (efficiency 89 to 90 percent or more, high frequency, network-enabled demand response). A charger that meets those gates is eligible in every program above that pays for chargers (C312). Coverage is a handful of utilities; a national list was not found (IB-271).

### Federal refueling property credit (30C)

The IRS says the credit cannot be claimed for property placed in service after 2026-06-30 ([[Document - IRS Instructions for Form 8911 Alternative Fuel Vehicle Refueling Property Credit (2025-12)]]). It was 6 percent of cost (30 percent with prevailing wage and apprenticeship), up to $100,000 per item, only in eligible census tracts. As of today it is unavailable for new installs. Whether forklift chargers ever qualified was not shown (IB-270).

### Demand charges and rate design

- **Level:** a commentary puts the U.S. average demand charge near $9 per kW and a Northeast example near $15 per kW per month (author estimates, a vendor of charging energy management; interested).
- **Rate design:** utilities use waivers and special EV rates that the same author says are often phased out as volume grows. SCE's TOU-EV-8 and TOU-EV-9 rates say demand charges are currently not applicable pending Commission action, but the fact sheet does not say whether forklifts qualify and gives no dollar rates.
- **Illustration (hypothetical inputs, analyst calculation):** 20 chargers of 8 kW with an 0.8 coincidence factor give a 128 kW peak, or $13,800 to $23,000 a year at $9 to $15 per kW. Halving the peak by load management saves $6,900 to $11,500 a year, or $350 to $580 per charger. Compare Eaton's reported $40,000 a year saving at one site (vendor claim already in [[Cost Driver 08 Utilities and Energy]]). The inputs are assumptions; the actual tariff and the site's measured peak decide the result.

### Putting it beside the credit (illustration only)

At an energy price of $0.14 per kWh (the vendor blog's example), a 10 MWh truck costs $1,400 a year in energy. California credits at the $72.61 mid-2026 price are about $333 a year at EER 2.4 and $626 at EER 3.8 for 10 MWh, or 24 and 45 percent of that energy cost ([[Forklift Clean Fuel Credit Business Case]]). A $2,000 to $6,000 one-time rebate equals 6 to 18 years of the lighter-class credit. Treat these as orders of magnitude.

### Gaps

- Measured annual kWh per truck by class (IB-258); the California regulatory impact assessment (SRIA) tables and the EPRI 2015 forklift study were blocked or truncated in the fetch tool and are on the wishlist.
- A national list of utility forklift and charger programs (IB-271).
- Actual commercial tariffs with demand charges for forklift sites and whether EV tariffs allow forklifts (IB-272).
- Whether forklift chargers qualified for 30C (IB-270).

### Sources

- Energy: [[Document - ANL ESD 08-3 Full Fuel-Cycle Comparison of Forklift Propulsion Systems]], [[Document - Apache Electric Vehicles How Much Electricity Does a Forklift Use in a Year (blog)]], [[Document - Wu et al Energy Consumption Analysis of High-Voltage Lithium Electric Forklifts (Applied Sciences 2025)]], [[Document - Apache Electric Vehicles How Much Electricity Does a Forklift Use in a Year (blog)]].
- Incentives: [[Document - Mass Save Electric Forklifts and Chargers Rebate Page (2026)]], [[Document - SRP E-Tech Program Factsheet FY27 (2026-05)]], [[Document - SRP E-Tech Forklift Program Flyer (program year 2022-23)]], [[Document - Burlington Electric Department Electric Forklifts Rebate Page (retrieved 2026-10-17)]], [[Document - Connexus Energy Electric Forklift Rebates (2026)]], [[Document - Southwest Iowa REC Commercial Electric Forklifts Rebate C15 (2021)]], [[Document - IRS Instructions for Form 8911 Alternative Fuel Vehicle Refueling Property Credit (2025-12)]].
- Demand charges (commentary, not yet absorbed as notes): Power Magazine, "The Demand Charge Dilemma at EV Charging Stations", 2023-12-19, <https://www.powermag.com/the-demand-charge-dilemma-at-ev-charging-stations/>; SCE TOU-EV-7/8/9 fact sheet, <https://www.sce.com/sites/default/files/custom-files/PDF_Files/TOU-EV-7_8_9-Rate_Fact_Sheet_082026_A11y.pdf>; Atlas Public Policy commercial demand charge analysis, <https://atlaspolicy.com/?p=8712>.

## Aliases

- Site energy economics register

## Former ids
