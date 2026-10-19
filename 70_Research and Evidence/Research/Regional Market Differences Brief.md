---
type: Info
subtype:
id: INFO-90059
uid: 20261018191500001skellyspencer
status: Draft
tags:
  - research
  - regional-comparison
  - decision-support
  - regulation
describes:
  - "[[Battery-Connected Product]]"
describedBy:
  - "[[Regional Market Size Model]]"
  - "[[Document - PSR Show Report Movimat 2024 Brazil (2024-11)]]"
  - "[[Document - Thomson Reuters Mexico Approves Tariff Hikes on Imports from China and Other Non-Treaty Countries (2025-12-15)]]"
  - "[[Document - China Forklift Market 2024 Sales per CCMA via machinery.yieh.com (2025)]]"
  - "[[Document - EU Ecodesign Regulation 2019-1782 External Power Supplies Scope and Exclusions]]"
  - "[[Document - Canada Clean Fuel Regulations SOR-2022-140 Full Text (consolidated to 2026-09-30)]]"
  - "[[Document - ZVEI Leaflet 14 Ventilation of Battery Charging Rooms for Lead Traction Batteries (2020-05)]]"
  - "[[Document - ZVEI Leaflet 11e Charger Assignments for Traction Batteries in Vented (PzS) and Valve Regulated (PzV) Design (2004-04)]]"
  - "[[Document - ZVEI Leaflet 23e Definition of Different Life Time Terms for Batteries (2013-08)]]"
---

# Regional Market Differences Brief

## Definition

Product-team brief that puts the regional evidence in the vault side by side: what moves demand for electric and lithium forklift batteries and chargers (mandates, credits, incentives), what the rules say about the charger and the charging room, how the technology mix and truck voltages differ, which dates are coming, and what is not known. It is written for someone deciding where to put engineering and sales effort. It adds no new market sizing; each cell points to the note or document that holds the evidence. Public sources only; no PosiCharge internal data.

## Notes

### How to read this

- **Confidence tags:** **[P]** the primary text was read from a file in the repo; **[S]** second-hand through a summarizing fetch tool (government or association page); **[V]** vendor, consultancy or other interested party; **[A]** analyst reasoning, no source says it; **[?]** not researched, which is not the same as "does not exist".
- **Owner's market priority (2026-10-18):** North America, then South America, Asia, Europe, rest of world.
- **Evidence depth by region against that priority:**

| Priority | Region | Depth in the vault | Main gap |
|---|---|---|---|
| 1 | US and Canada | Deep: clean fuel programs, fire code, CARB and EPRI primary texts | OSHA numbers (IB-333); measured fleet data (IB-258) |
| 1 | Mexico | Thin: one tariff summary [S]; no forklift market, battery or charger rule data | IB-334 |
| 2 | South America (Brazil) | Thin: one trade-show recap, claims only [V] | IB-335 |
| 3 | Asia | WITS regional class tables 2023 to 2025; China 2024 sales via trade press; no India, Japan or Southeast Asia detail | IB-336 |
| 4 | Europe | Battery regulation text read [P]; ZVEI/DIN ventilation [P]; no market, incentive or chemistry-mix data | IB-332 |
| 5 | Rest of world | WITS totals only (Africa 29,486; Oceania 33,440 in 2025) | IB-337 |

- **Sizing:** see [[Market Definition and Scope]] for what each statistic counts, and [[Regional Market Size Model]]: Asia 50.8% of 2025 shipments, Europe 28.3%, Americas 18.2%; the Americas row mixes North and South America (IB-339).
- **Challenge to the order:** WITS 2025 shipments put Asia at 1,210,288 of 2,381,417 (51%), Europe 673,663 (28%), Americas 434,540 (18%). Volume does not rank the regions this way; the order holds only if it reflects where PosiCharge sells or can sell. Asia's volume is dominated by Chinese domestic makers (CCMA: 805,000 domestic sales of 1,285,500 in 2024), so addressable share is a separate question (IB-336).
- **Regions covered:** California, Oregon, Washington, New Mexico, British Columbia, Canada (federal), the EU with Germany as the only country-level evidence, and US federal. Thinly researched: Mexico, Brazil, China. Not researched: other US states with clean fuel bills, UK, India, Japan, Southeast Asia, Africa, Oceania.
- **Open dependency:** no vault note says which regions PosiCharge sells into (IB-281). The brief therefore covers every region with evidence and says which decisions each one informs.

### Bottom line

1. **The demand drivers are regional and mostly credit-based, not mandate-based.** California's forklift mandate is enforced only against state and local government fleets; for private fleets it is paused pending EPA authorization [S] ([[California Forklift Electrification Regulations Register]]). The money for most customers comes from clean fuel credit programs and utility rebates, and the programs differ in who may claim, how kWh is measured, and which trucks qualify.
2. **The metering rules are the part of the credit schemes that touch a charger.** Oregon accepts direct metering only, forbids adjusting the data, and lets the charger itself be the registered equipment; California takes upstream-metered kWh within 5 percent and applies an efficiency factor (85 percent default); Washington is unclear [S] ([[Western State Clean Fuel Programs for Forklift Electricity Register]]). A charger-side energy record that is accurate enough, exportable and attributable to a truck is the common denominator [A].
3. **Truck size decides eligibility in two programs.** British Columbia covers forklifts over 6,800 kg and rough-terrain forklifts only, EER 3.9 [P, first-hand bulletin]; California splits at 12,000 lb (EER 2.4 below, 3.8 at or above); Oregon has no split [S]. Most warehouse trucks in the 3,000 to 12,000 lb range at 36 to 80 V (EPRI [P]) fall outside the BC scheme [A].
4. **The EU rules in the vault are about the battery as a product, not about credits.** The batteries regulation puts a battery passport on each industrial battery above 2 kWh from 2027-02-18 and a performance-and-durability declaration from 2024-08-18 [P]; its state-of-health data duty (Art. 14) names stationary storage, light-transport and electric-vehicle batteries and not forklift traction batteries on my reading [P, C351]. No EU forklift credit or incentive scheme is in the vault [?] (IB-332).
5. **The EU gives a quantified ventilation method for lead charging rooms; the US texts read give wording only.** DIN EN 62485-3 as explained in a ZVEI leaflet: Q = 0.055 m3/Ah x cells x gassing current, default 40 percent of maximum charge current, charging only if forced ventilation is effective [P]. California Fire Code section 309 asks for ventilation against flammable gas without a formula in the text read [S]; OSHA text is unread (IB-333).
6. **The technology mix is a modeling assumption in California and unknown elsewhere in the vault.** CARB assumes about 7 to 10 percent of new industrial batteries lithium (c. 2022) and 35 percent of new battery-electric forklifts by 2026 [P, assumption]; roughly 70,000 lead-acid forklifts are in operation in the state [P]. The vault has no lead-acid versus lithium split for Europe, Canada or the rest of the US.
7. **Cellular and data platform lifetimes differ by region.** US 3G is gone; AT&T is retiring NB-IoT; a leaked T-Mobile LTE date near 2028 is unconfirmed; Canadian 3G retirements run 2025 to 2026; Vodafone Germany ends 2G in September 2028 [S, V] ([[Cellular Network Lifetime and IoT Modem Migration Register]]).
8. **Most credit and incentive money per truck is small beside the truck.** California credit about $33 to $63 per MWh at the mid-2026 price (analyst calculation), 13.9 MWh a truck from regulator assumptions, so about $460 to $870 a year, against a $2,000 to $6,000 one-time utility rebate for a truck [A, S] ([[Forklift Clean Fuel Credit Business Case]], [[Forklift Charging Site Energy Economics and Incentives Register]]). The regulator's own impact assessment says about $1,200 a year (C352).

### Matrix 1: what moves demand

| Jurisdiction | Mandate | Credit program and forklift coverage | Who reports, how measured | Credit value found | Other money | Evidence |
|---|---|---|---|---|---|---|
| California | Zero-emission forklift rule: enforced against state and local government fleets since 2026-01-01, phase-out 2028 to 2038; private fleets and sellers paused until EPA authorization or a finding it is not needed [S] | LCFS; forklifts covered; EER 2.4 (under 12,000 lb), 3.8 (12,000 lb and over) [S] | Facility owner since 2025-07-01; metered kWh within 5 percent from Q1 2026 reports; upstream meters adjusted by charger efficiency, 85 percent default; third-party verification from 2027 for 2026 data [S] | $72.61 per tonne, weekly log to 2026-07-19 [S]; $33 to $63 per MWh (analyst calculation); regulator assumption $0.67 per operating hour in 2026 (C352) [P] | CORE voucher: forklifts and refrigeration units share $5M of a $35M baseline for FY2025-26 and FY2026-27 [S]; Title 20 charger efficiency for large chargers [S] | [[California Forklift Electrification Regulations Register]]; [[Document - CARB LCFS Guidance 25-01 Forklift Fueling Reporting (2025-10)]]; [[Document - CARB ZEF Government Fleets Overview Fact Sheet (2026-01)]]; [[Document - CARB Standardized Regulatory Impact Assessment, Appendix B-2 (zero-emission forklifts)]] |
| Oregon | none found in the vault [?] | Clean Fuels Program; forklifts covered; no size split | Forklift owner or operator as credit generator; direct metering only since Q4 2023 report, data not adjustable except subtracting another party's claim; charger may be the registered equipment when its tracking is documented; estimation method caps use at 30 percent depth of discharge and two shifts a day [S] | $47.98 (April 2025 monthly, vendor [V]); $80.51 (DEQ 2025 cost report [S]); more than 3,500 registered electric forklifts in May 2023 giving over a third of electricity credits [S] | none read | [[Western State Clean Fuel Programs for Forklift Electricity Register]]; [[Document - Oregon DEQ Forklift Transition Guidance (2023)]]; [[Document - Oregon DEQ 2025 Annual Costs and Benefits of the Clean Fuels Program]] |
| Washington | none found [?] | Clean Fuel Standard; forklifts covered | Fleet owner is reporting entity and credit generator (operator by written contract); metering not stated in the rule section read (C293) [S] | $45.92 volume-weighted average for 2024; monthly $23.88 to $89.89 [S] | none read | [[Western State Clean Fuel Programs for Forklift Electricity Register]]; [[Document - Washington Ecology Clean Fuel Standard Report for Calendar Year 2024 (publication 26-14-043)]] |
| New Mexico | none found [?] | Clean Transportation Fuel Program; forklifts listed as special equipment by a state document; rule text unread | Fleets that own chargers are "first in line"; metered quarterly kWh; reporting from 2026-04-01; third-party verification from 2028-09-15 [S] | not found | none read | [[Western State Clean Fuel Programs for Forklift Electricity Register]] |
| British Columbia | none found [?] | LCFS covers forklifts from the 2024 compliance period, but only over 6,800 kg and rough-terrain; electricity EER 3.9; the province says forklift volumes "remain relatively small" [P] | Not stated in the bulletin; a vendor page says the entity named on the utility bill is the generator [V] | not found | none read | [[Document - BC Information Bulletin RLCF-022 Prescribed Purposes Other Than Transportation (updated 2026-09-21)]]; [[Document - BC Low Carbon Fuel Requirements Summary 2010-2025 (RLCF-007, updated 2026-06-29)]]; [[Document - Xpansiv British Columbia LCFS Market Page (retrieved 2026-10-17)]] |
| Canada (federal) | none found [?] | Clean Fuel Regulations: a charging-site host creates credits for electricity supplied to an electric vehicle of a class listed in a Specifications document; forklifts are not named in the regulation text [P]; vendor FAQ lists electric forklifts as an opportunity [V] | Charging-site host; kWh as measured by charging stations (accuracy by reference to a NIST document) [S] | CAD 133.20 volume-weighted average, 2023-06-30 to 2024-05-31 [S]; "above $400" vendor claim, basis unclear [V] | none read | [[Document - Canada Clean Fuel Regulations SOR-2022-140 Full Text (consolidated to 2026-09-30)]]; [[Document - Canada Clean Fuel Regulations Section 101 Charging Site Host Credits (Justice Laws)]]; [[Document - Canada Clean Fuel Regulations Credit Market Report (2024-06-26)]] |
| EU (Germany evidence only) | none for forklifts found [?] | none found [?] | not applicable | not applicable | not researched [?] (IB-332) | [[EU Battery Passport and Battery Regulation Register]] |
| US federal | EPA authorization pending for the California rule (CARB had not asked in notices read) [S] | none | not applicable | not applicable | Refueling property credit 30C unavailable for property placed in service after 2026-06-30 [S]; federal battery charger efficiency standard for chargers made on or after 2018-06-13 [S] | [[Forklift Charging Site Energy Economics and Incentives Register]]; [[Energy Programs and Incentives Register]] |
| Other US states | Hawaii enacted, awaiting implementation; Illinois, Massachusetts, Minnesota, New Jersey, New York, Pennsylvania, Vermont have 2026 bills; whether any covers forklifts is not stated [V] | | | | Utility rebates seen: Mass Save $6,000 per truck and $550 per charger; SRP (Arizona) $2,000 per truck replacing combustion and $180 per charger; Burlington Electric $6,000; Connexus $2,000 [S] | [[North American Clean Fuel Programs Register]]; [[Forklift Charging Site Energy Economics and Incentives Register]] |

### Matrix 2: rules that touch the charger and the battery room

| Topic | United States (as read) | EU and Germany (as read) | Difference that matters |
|---|---|---|---|
| Charging-room ventilation, lead batteries | California Fire Code 309: approved chargers, 3 ft clear of combustible storage, no charging in areas open to the public, ventilation against flammable gas, extinguisher within 20 ft; no formula in the text read [S]. OSHA 29 CFR 1910.178(g) text unread (C319) | DIN EN 62485-3 via ZVEI leaflet 14 (May 2020): Q = 0.055 m3/Ah x cells x Igas; Igas from the charger maker or at least 40 percent of maximum charge current; natural ventilation needs room volume at least 2.5 times Q and 0.1 m/s through openings of 28 cm2 h/m3 x Q; forced ventilation must be proven effective before charging; 0.5 m ignition-free distance from cell openings [P] | The EU method needs a charger-declared gassing current and a verified ventilation signal; the US wording as read does not [A] |
| Charging-room rules, lithium | Fire code text read is chemistry-agnostic; no lithium-specific OSHA standard per a 2026 secondary article (C319); CARB staff say they know of no extra fire or life-safety rules for lithium charging [P] (C353) | Not in the vault [?]; the one insurer sheet (10 m separation or EI60, detection, charger cut-off on alarm or ventilation failure, truck BMS talking to the charger) has unknown jurisdiction in the vault [S] (C353) | Regulator and insurer disagree in tone, and no region has a read lithium-specific code (C314, C318) |
| Charger characteristics notation | Not read for the US [?] | W, U, I characteristics with a and 0 suffixes; DIN 41772/41773/41774; tolerances plus or minus 2 percent current, 1 percent voltage (I), 0.05 V per cell (W); reference end-of-charge 2.65 V per cell; charging factor 1.2 [P] | EU buyers and battery makers speak this notation; a US-first charger spec sheet may need the translation [A] ([[Traction Battery Charging Characteristics (DIN Notation)]]) |
| Charger efficiency | Federal standard for chargers made on or after 2018-06-13; California Title 20 for large chargers above 2 kW [S]; utility rebates require 89 to 90 percent efficiency and network or demand-response capability [S] | Ecodesign Regulation 2019/1782 covers external power supplies up to 250 W and excludes battery chargers without power supply function; traction chargers not mentioned, so no EU forklift-charger efficiency duty found [S] ([[Document - EU Ecodesign Regulation 2019-1782 External Power Supplies Scope and Exclusions]]); absence not proven | Efficiency and connectivity gates are a US utility-rebate feature; EU equivalent unknown |
| Battery regulation | none comparable found [?] | Regulation (EU) 2023/1542: performance document from 2024-08-18 (capacity fade, power fade, internal resistance increase, lifetime in cycles and years, with test conditions); passport and QR code from 2027-02-18; Art. 14 state-of-health data in the BMS for stationary, LMT and EV batteries only; passport use data include cycles, events, temperature and state of charge [P] | EU creates a data duty on the battery's market operator; whether a battery-mounted monitor is its source is open (C337, C351) |
| Lifetime and health vocabulary | 80 percent capacity as end of life appears in many second-hand statements (C192, C349) | ZVEI 23e: design life, endurance, service life, each with its own conditions; regulation: "expected lifetime in cycles and calendar years under reference conditions" [P] | The words differ; marketing a state-of-health number across regions needs a stated definition ([[SOC and SOH Specifications and Standards]]) |
| Cold storage | not read | ZVEI leaflet 21e: capacity falls about 0.6 percent per degree below 30 C; charge voltage coefficient -0.004 V per cell per K; regulated IUI chargers with temperature control [S] | Same physics everywhere; the leaflet is the only quantified source in the vault ([[Cold Storage Charging Rules for Traction Batteries (ZVEI)]]) |

### Matrix 3: market and technology mix

| Measure | Value | Region | Basis |
|---|---|---|---|
| World industrial truck shipments 2025 | 2,381,417; electric classes 79.5 percent (derived) | World | [[Market Size and Volume Register]] (WITS) [S] |
| Shipments 2025 by region | Asia 1,210,288; Europe 673,663; Americas 434,540; Africa 29,486; Oceania 33,440 | World regions | same |
| Americas Class 1 plus Class 2 shipments 2025 | 136,911 (derived) | Americas | same |
| Electric share of North American retail orders | about 71 percent in 2024 | North America | ITA via Flux Power 10-K [S] |
| Affected forklifts in California | about 95,000 LSI forklifts in about 11,000 fleets by 2026; about 70,000 lead-acid forklifts in operation | California | CARB impact assessment [P] |
| Lithium share of new industrial batteries | 7 to 10 percent (c. 2022); modeled 35 percent of new battery-electric forklifts in 2026, 61 percent in 2030 | California | CARB impact assessment [P], assumption (C354) |
| Lithium share of full-electric sales | about 32 percent in 2024; expected above 70 percent by 2034 | World | [[Market Size and Volume Register]] (Interact) [V] |
| Typical voltage by class | Class 1: 36, 48 or 80 V; Class 2: 24, 36 or 48 V; Class 3: 12 or 24 V | US (EPRI) | [[Document - EPRI Electric Forklifts Brochure (April 2015, ID 3002005805)]] [P] |
| Hours and energy per truck | 1,848 hours a year; 7.5 kWh per hour; about 13.9 MWh a year (derived) | California | CARB impact assessment [P], assumptions not measurements |
| Price gap, 5,001 to 6,000 lb truck (2021 dollars) | propane $47,292; lead-acid electric $64,844; lithium electric $78,326 | California | CARB impact assessment [P] |
| Electricity price | statewide weighted $0.18 per kWh (2021 dollars); large fleet $0.16; small fleet $0.22 | California | CARB impact assessment [P] |
| Europe lead-acid versus lithium split, energy per truck, prices | not in the vault | Europe | [?] (IB-332) |
| China forklift sales 2024 | 1,285,500 (domestic 805,000; exports 480,500); electric 946,300 (73.61%); lithium share not stated; exceeds the WITS total for all Asia (1,059,429) | China | [[Document - China Forklift Market 2024 Sales per CCMA via machinery.yieh.com (2025)]] [S], trade press (C355) |
| Class 1+2 shipments 2025 and change since 2023 | Asia 275,888 (+22.1%); Europe 171,241 (-6.0%); Americas 136,911 (+16.0%) | World regions | [[Regional Market Size Model]] (WITS) [S] |
| Regional lithium penetration targets | Europe 50% by 2025; US not before 2032; China above 73% by 2034 | World regions | Interact via [[Market Size and Volume Register]] [V] |
| Brazil electric share | Heli claims two of three machines it sells are electric; no market-wide figure | Brazil | [[Document - PSR Show Report Movimat 2024 Brazil (2024-11)]] [V] |
| Mexico import tariffs on non-treaty countries | up to 35% on most goods, machinery 25-35%, from 2026-01-01; trucks and batteries unconfirmed | Mexico | [[Document - Thomson Reuters Mexico Approves Tariff Hikes on Imports from China and Other Non-Treaty Countries (2025-12-15)]] [S] |

### Matrix 4: connectivity lifetime

| Region | Documented | Source tier |
|---|---|---|
| US | 3G shutdowns past (AT&T 2022, Verizon end of 2022, T-Mobile July 2022); AT&T retiring NB-IoT for LTE-M; AT&T has announced no LTE turn-down date in the FAQ read; leaked T-Mobile LTE phase-out around 2028 unconfirmed (C331) | [S], [V] |
| Canada | Rogers began retiring 3G on 2025-08-07; Telus Manitoba 3G ends 2025-12-31 and 2026-03-31 (one vendor blog) | [V] |
| Germany | Vodafone ends 2G for most users in September 2028, some critical IoT until end of 2030 | [V] |
| PosiCharge device modems | not stated in any source (C329); internal data needed | gap |

All from [[Cellular Network Lifetime and IoT Modem Migration Register]].

### Calendar of dated events

| Date | Event | Region | Tier |
|---|---|---|---|
| 2018-06-13 | Federal battery charger standard applies to chargers manufactured from this date | US | [S] |
| 2024 compliance period | BC LCFS starts covering forklifts | BC | [P] |
| 2024-08-18 | EU performance and durability document and Art. 14 data duty start to apply | EU | [P] |
| 2025-07-01 | Facility owner becomes first reporting entity for forklift electricity | California | [S] |
| 2026-01-01 | Zero-emission forklift rule compliance begins for state and local government fleets | California | [S] |
| 2026-02-18 | Date the regulation gives for the delegated act on minimum performance values; adoption not checked (IB-330) | EU | [P] |
| 2026-04-01 | Clean fuel reporting begins | New Mexico | [S] |
| 2026-06-30 | Last in-service date for refueling property credit 30C | US | [S] |
| 2026-08-18 | Date the regulation gives for the implementing act on passport access rights; the register records a draft expected October or November 2026 (IB-330) | EU | [P], [S] |
| Q1 2026 reports | Metered kWh required for forklift credits; estimates no longer accepted | California | [S] |
| 2027 | Third-party verification of 2026 data | California | [S] |
| 2027-02-18 | Battery passport and QR code required for industrial batteries above 2 kWh | EU | [P] |
| 2027-08-18 | Minimum performance values for industrial batteries above 2 kWh, or 18 months after the delegated act, whichever is later | EU | [P] |
| 2028 to 2038 | Phase-out schedule for state and local government fleets | California | [S] |
| 2028-09-15 | Third-party verification | New Mexico | [S] |
| September 2028 | Vodafone Germany 2G ends for most users | Germany | [V] |
| about 2028 | Leaked T-Mobile LTE phase-out, unconfirmed | US | [V] |

### Where regions differ in a way that changes a product decision

Each row is analyst reasoning ([A]) built on the evidence cited above; none is a recommendation.

| Difference | Why it could change a decision | What would settle it |
|---|---|---|
| Metering rule: Oregon direct and unadjusted, California within 5 percent plus efficiency factor, Washington unclear, BC and Canada unstated | A charger-side kWh record is only sellable as a credit-grade meter if it meets the strictest rule it will be sold under; a configurable meter location and efficiency factor would serve California and Oregon | Meter accuracy of PosiCharge chargers (internal); Washington and New Mexico rule text; whether regulators accept charger-reported kWh outside Oregon |
| Reporting party: facility owner (California), forklift owner or operator (Oregon, Washington) | The data must be shareable with whoever holds the credit, and a multi-state customer cannot assume one answer (C295) | Customer interviews; contract practice between site owner and truck owner |
| Eligibility by truck size | BC excludes most warehouse trucks; California gives a lower credit under 12,000 lb | Truck population by lift capacity per region |
| Ventilation method: formula and interlock (EU) versus wording (US) | A charger that declares gassing current and exposes a "ventilation effective" input would fit the EU method directly; the US value is unproven | OSHA and NFPA 505 text (IB-333); German statutory basis (IB-332) |
| Data duty: EU passport use data versus US energy credit data | The same logged variables (cycles, temperature, state of charge, kWh) feed both; only the EU case is a legal record, and only if the battery maker chooses the device | The battery maker's choice of data source; the access-rights act (IB-330) |
| Chemistry mix | If lead-acid remains dominant near term (CARB staff view, a stated opinion), lead-acid charging, water and equalization functions stay relevant in California; the EU mix is unknown | Region-specific lead-acid versus lithium shares (IB-332) |
| Cellular lifetime | Different sunset dates by region argue for a modem choice that covers the longest-lived markets | Device inventory (internal); carrier announcements |
| Terminology: service life, endurance, design life versus capacity-based SOH | State of health claims are not comparable across regions or vendors (C191, C192) | Adopt a stated definition in product material |

### What a product leader would still ask for

- **Which regions are our markets?** The owner gave an order (North America, South America, Asia, Europe, rest of world) but not whether PosiCharge sells in each (IB-281).
- **Truck-level data.** Measured kWh per truck, hours, voltage and lift class from PosiLink or E-Meter, per region, would replace the regulators' assumptions (IB-258).
- **A rule-by-rule check of the strictest case.** Oregon's metering rule and the EU ventilation interlock are the two most demanding items read; whether current PosiCharge products meet them is internal knowledge.
- **EU market facts.** Incentives, charger efficiency rules, chemistry mix and the legal basis of the ventilation standard are missing (IB-332).
- **The US ventilation numbers.** To compare with the EU formula (IB-333).
- **Competitor positions by region.** Not covered here; see [[Forklift Offerings Matrix]] and [[BMID Competitor Landscape]].

## Sources

Evidence sits in the registers named in each table and on these Document notes added or read first-hand in rounds R75 to R77: [[Document - EUR-Lex Regulation 2023-1542 Full Text as Published 2023-07-28 (Articles 3, 10, 13, 14, 77, 78 and Annexes IV, VII, XIII read)]], [[Document - ZVEI Leaflet 14 Ventilation of Battery Charging Rooms for Lead Traction Batteries (2020-05)]], [[Document - ZVEI Leaflet 11e Charger Assignments for Traction Batteries in Vented (PzS) and Valve Regulated (PzV) Design (2004-04)]], [[Document - ZVEI Leaflet 23e Definition of Different Life Time Terms for Batteries (2013-08)]], [[Document - Canada Clean Fuel Regulations SOR-2022-140 Full Text (consolidated to 2026-09-30)]], [[Document - CARB Standardized Regulatory Impact Assessment, Appendix B-2 (zero-emission forklifts)]], [[Document - CARB Final Statement of Reasons, Zero-Emission Forklifts]], [[Document - EPRI Electric Forklifts Brochure (April 2015, ID 3002005805)]], [[Document - BC Information Bulletin RLCF-022 Prescribed Purposes Other Than Transportation (updated 2026-09-21)]], [[Document - BC Low Carbon Fuel Requirements Summary 2010-2025 (RLCF-007, updated 2026-06-29)]]. Conflicts: C295, C314, C318, C319, C329, C331, C333, C337, C349, C351 to C354 in [[Battery Product Landscape Conflicts and Open Questions]].

## Aliases

- regional comparison
- region differences
- CPO regional brief
- market differences by region

## Former ids
