---
type: Info
subtype:
id: INFO-00976
uid: 20261017194600000skellyspencer
status: Draft
tags:
  - research
  - business-analysis
  - installed-base
  - opportunity
  - recurring-revenue
describes:
  - "[[PosiCharge SkyLink]]"
  - "[[PosiCharge PosiLink]]"
  - "[[PosiCharge E-Meter]]"
  - "[[PosiCharge Battery Rx]]"
  - "[[PosiCharge PosiGuard]]"
  - "[[PosiCharge BMID]]"
  - "[[PosiCharge DVS300 Series]]"
  - "[[PosiCharge MVS400 and MVS800]]"
  - "[[PosiCharge ProCore Edge]]"
  - "[[PosiCharge Single-Point Automatic Battery Watering]]"
describedBy:
  - "[[Document - C and S Companies Port of Portland eGSE EER Tier 2 Pathway Report (2022-01)]]"
---

# Installed Base Monetization Opportunity Register

## Definition

Ranked list of low-cost add-ons that would earn revenue from PosiCharge chargers, battery monitors and cloud platforms already installed at customer sites, each tied to a customer need, the capability that already exists, the evidence for its value and what blocks a decision. Owner request 2026-10-17. Analyst ranking, not a roadmap commitment. Disagreements are C348 in [[Battery Product Landscape Conflicts and Open Questions]]; directions are IB-318 to IB-324 in [[Investigation Backlog]].

## Notes

- **Reading rule:** capabilities come from the public PosiCharge pages and sheets already on the product notes (second-hand reads). Value figures come from vault registers and are labeled analyst calculations or illustrations; none is PosiCharge field data. No internal installed-base, connectivity or pricing data is in the vault (KB-010).
- **Scope:** add-ons that reuse hardware already in the field and are mainly software, data, service or existing accessories. Status as of 2026-10-17.
- **Test applied to each item:** a customer need already in the vault, a capability PosiCharge already shows publicly, a source for the money involved, and the cost driver of delivering it.

### Bottom line (analyst summary)

1. **The cheapest money is in data PosiCharge already collects.** [[PosiCharge SkyLink]] already records charge sessions, energy and vehicle-level activity by BMID, with remote support, billing support and over-the-air firmware ([[PosiCharge SkyLink]]). [[PosiCharge PosiLink]] already tracks battery usage against recommended practice for warranty compliance, and lists facility power limits, time-of-use and scheduled charging as "coming soon". The top three opportunities are reports and controls on top of that data, not new hardware.
2. **First pick: clean fuel credit reporting from charger data.** Customers in California, Oregon, Washington, New Mexico, British Columbia and Canada can be paid per MWh of forklift charging. California values are about $33 to $63 per MWh, and Oregon about $56 per MWh for forklifts ([[Forklift Clean Fuel Credit Business Case]]). At an illustrative 5 to 20 MWh per truck-year, that is roughly $170 to $1,250 per truck-year in California that customers do not collect today unless they meter and report. The vault already holds the data requirements (output-side unadjusted energy, records tagged by truck and lift class). Aggregators (3Degrees, 7Gen) and meter vendors already sell this, so PosiCharge would partner or compete.
3. **Second: site power and time-of-use control on installed chargers.** [[PosiCharge MVS400 and MVS800]] already do peer load management and site-set time windows, [[PosiCharge DVS300 Series]] has time windows, and PosiLink lists energy management as coming. Six competitors already sell this to forklift fleets. The illustrated saving is $350 to $580 per charger-year at $9 to $15 per kW demand charges; the site tariff decides the real figure.
4. **Third: battery health and care-compliance subscription.** [[PosiCharge Battery Rx]] states rotation recommendations, life-expectancy estimates and warranty-compliance tracking. The two care rules with quantified life effects (depth of discharge and temperature; [[Lead-Acid Traction Battery Life Care Methods Register]]) are exactly what a BMID logs. Competitors (EnerSys, Exide GNB Fleet, Philadelphia Scientific, and Ampure's own [[Power Designers PowerTrac 3]]) already sell it.
5. **Everything depends on one unknown: how much of the installed base is connected.** Items 1 to 4 need data off the site. Battery Rx cellular is optional, BMID data is read over Bluetooth, and no source says which chargers report to SkyLink or which modem they carry (IB-292, C329). The first business action is an installed-base census (IB-318), not a build.
6. **Do not build these twice.** PosiLink, SkyLink and Power Designers' PowerCharge.NET and energy-demand software overlap ([[Ampure Industrial Portfolio Overlap and Synergy Map]]). Each opportunity below names the internal capability to check first, as the gap assessment rule requires ([[PosiCharge Capability Gap Assessment]]).

### Ranked opportunities

| Rank | Add-on | Customer need it serves | What already exists | Money involved (evidence) | Cost driver to deliver | Blocking unknowns |
|---|---|---|---|---|---|---|
| 1 | **Clean fuel credit data and reporting service** (monthly per-site energy reports by truck and lift class in each program's format; partner with an aggregator or file for the customer) | [[Report Metered Forklift Charging Energy for LCFS Credits]], [[Report Metered Forklift Charging Energy for Oregon, Washington or New Mexico Credits]] | SkyLink charge-session energy and vehicle activity by BMID; E-Meter energy capture; requirements [[Charging Energy Reporting - Provide Unadjusted Energy Data at the Output or Forklift Side]] and [[Charging Energy Reporting - Tag Charging Records with Forklift Identifier, Lift Capacity Class and Model Year]] | California $33.29 per MWh (under 12,000 lb) and $62.62 (12,000 lb and over); Oregon about $56 per MWh for forklifts; both analyst calculations from regulator inputs. Oregon also lists electric ground support equipment (EER 3.2, extraction to be checked) and BC lists GSE at EER 2.5, so airport chargers may qualify where California does not (C348) | Report engineering; meter accuracy evidence (California asks 5 percent, Guidance 25-01); truck-to-BMID-to-lift-class mapping; third-party verification from the 2026 California data year | Charger energy measurement accuracy; share of customers in credit states; aggregator fee (IB-262); whether customers already sell credits through a utility or aggregator |
| 2 | **Site power cap and time-of-use charging** (turn on and sell what MVS and DVS300 already do; add a PosiLink schedule) | [[Charge Within Site Power Limits and Utility Costs]], [[Limit Site Charging Power at Peak]] | MVS peer load management and time windows; DVS300 time windows; PosiLink energy management "coming soon" | Illustration $350 to $580 per charger-year at $9 to $15 per kW; one vendor claim of $40,000 a year at a site ([[Forklift Charging Site Energy Economics and Incentives Register]]); some utility charger rebates required network-enabled, demand-response-capable chargers (SRP 2022-23, expired) | Software and commissioning; per-site tariff analysis | Tariffs at customer sites; whether installed DVS and SVS units can receive the setting remotely; Power Designers energy-demand software overlap |
| 3 | **Battery health and care-compliance subscription** (monthly report: deep-discharge count, over-temperature time, missed equalization, low water, replacement forecast) | [[Document Battery Care for Warranty Compliance]], [[Prevent Battery Abuse and Premature Replacement]], [[Plan Battery Replacement and Budget Ahead]] | Battery Rx (rotation, life expectancy, warranty-compliance tracking stated); PosiGuard and BMID logging; DVS and MVS battery-stored equalization schedule; PosiLink exceptions reporting | Life effect evidence: 100 percent depth of discharge costs about one third of life against 80 percent (ZVEI); no battery price or subscription price is in the vault | Analytics and report; data collection path for Bluetooth-only BMIDs | Connected share; battery replacement price to state the saving; who pays (fleet, dealer or battery maker) |
| 4 | **Fleet right-sizing assessment from installed data** (E-Meter-style report from SkyLink history: charger utilization, idle batteries, charge-window fit) | [[Right-Size the Fleet from Usage Data]], [[Monitor and Manage Chargers and Batteries Across Sites]] | E-Meter analysis (energy, battery health, charger performance, lost productivity, billing discrepancies); SkyLink session data | No price source; value is pull-through of chargers, lithium conversions and item 2 | Analyst time per report; mostly a sales tool | Whether SkyLink history is long enough per site |
| 5 | **Watering automation retrofit on installed lead-acid fleets** | [[Keep Trucks Working Without Battery Maintenance Labor]] (the need with first-hand customer evidence) | [[PosiCharge Single-Point Automatic Battery Watering]], [[PosiCharge SVS200]] charger-controlled watering; Battery Rx water-level sensing to find the batteries that need it | No labor-cost source in the vault for watering; ZVEI and maker rules make watering mandatory but give no life figure ([[Lead-Acid Traction Battery Life Care Methods Register]]) | Existing SKU; installation labor | Which installed chargers can drive watering; lead-acid share of the installed base |
| 6 | **Fire alarm and ventilation interlock kit** for sites converting to lithium (charger stops on alarm or ventilation loss; paperwork for the insurer) | [[Get Charging Areas Approved by the Fire Authority and Insurer]] | Need and Function [[Start and Stop Charge from an External Control]] are modeled; no PosiCharge product is shown performing it | One insurer sheet asks for it (If P&C 2024); no code requires it ([[Lithium Forklift Charging Area Fire and Safety Code Register]]) | Small hardware kit if chargers have an enable input; documentation | Whether installed chargers have a usable input; US insurer demand |
| 7 | **Lithium-ready upgrade for installed chargers** (charge profiles and BMS-directed CAN charging on the installed DVS, SVS and MVS base, as ProCore Edge already does) | [[Charge Each Battery Correctly for Its Chemistry and Condition]], [[Integrate the Battery with Truck and Charger Controls]] | ProCore Edge performs [[Charge Lithium-Ion Battery]] and [[Charge Under BMS Control]] | Defensive: OEMs now bundle their own battery and charger ([[OEM In-House Lithium Battery and Charger Offers Register]]); keeping the charger socket when a fleet converts | Moderate: per-battery-brand BMS validation and firmware; not low-cost | Which installed models can take the firmware; battery makers' approval of third-party chargers |

### What not to pursue now (analyst reasoning)

- **EU battery passport services:** the duty sits on battery makers, and PosiCharge's EU sales are unknown ([[EU Battery Passport and Battery Regulation Register]]).
- **Selling NFPA 855 compliance:** no source applies NFPA 855 to forklift charging.
- **Desulfation as a paid feature:** the least supported care method ([[Lead-Acid Traction Battery Life Care Methods Register]]).

### Hypotheses (analyst reasoning, untested)

- **MH1:** items 1 to 3 share one data pipeline (session energy, battery identity, events). Built once, each extra report has low marginal cost. Test: IB-318, IB-319.
- **MH2:** the credit service has the fastest customer pull because it pays the customer cash instead of asking for a budget. Test: IB-320 (customer interviews in credit states).
- **MH3:** connectivity, not features, is the constraint; a connectivity upgrade (gateway or modem refresh) may itself be the first sale. Test: IB-318, IB-292.

### Questions for the owner

What share of the installed base reports to SkyLink or PosiLink today, and in which states and provinces? That single number sizes items 1 to 4 and decides whether a connectivity upgrade comes first.

## Open questions

- Installed-base census: units by model, connected or not, location (IB-318).
- Charger energy measurement accuracy and measuring point (IB-319).
- Customer interest and current credit arrangements in credit states (IB-320).
- Tariffs and demand charges at customer sites (IB-321, extends IB-272).
- Power Designers and PowerCharge.NET capability overlap for load management and battery analytics (IB-322).
- Enable input on installed chargers (IB-323).
- eGSE credit eligibility by program and per-unit energy (IB-324, C348).

## Sources

Registers and product notes linked above; new source [[Document - C and S Companies Port of Portland eGSE EER Tier 2 Pathway Report (2022-01)]] and the existing [[Document - 3Degrees Revenue Streams from Electric Forklifts Under Clean Fuel Standards (2025-09-25)]] (eGSE eligibility statements).

## Aliases

- Installed Base Opportunities

## Former ids
