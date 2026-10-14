---
type: Info
subtype:
id: INFO-00244
uid: 20261003163422054skellyspencer
status: Draft
tags:
  - review
  - features
  - coverage
describes:
  - "[[Battery-Connected Product]]"
---

# Feature Capture Log

## Definition

Record of the pass that turned features stated in product notes into function and design links, what was captured, and why some products still have no feature link.

## Notes

- **Owner request (2026-10-03):** capture the missing features from the unlinked products, all types, in order of most unlinked.
- **Method:** (1) read only the sourced text already in each product note; (2) reuse an existing function or design where one fits and create a new one only for a feature a source states, with a general parent; (3) cite the source URL beside each link; (4) add a dependency when a function plainly needs a design; (5) do not copy a feature onto a vehicle when an accessory note already carries it (the two are linked by offeredWith).
- **Principle used:** battery properties such as chemistry, voltage, capacity, warranty and charge regimes are metrics ([[Metric - Charge Regimes Supported]], [[Metric - Nominal Voltage Range]]), so they are not duplicated as functions; behaviors and devices are functions and designs.
- **Result after round 25:** 50 products received feature links; 56 of 321 remained unlinked (106 at the start).
- **Round 26:** sources found for 12 of them (in-repo Crown and KION documents, web pages); 48 of 323 remained unlinked.
- **Round 27 (review of the vocabulary and dependencies):** three property functions were retired and their values moved to metrics: Eliminate Battery Watering (FUNC-00107, 5 products); Avoid Battery Changeover During Shifts (FUNC-00104, 3 products); Charge Without Gas Emissions (FUNC-00106, 4 products). Three dependencies contradicted by sources were withdrawn, two links were fixed, and the overloaded general function was split into [[Limit Vehicle Speed Automatically]] and [[Hold or Stop Vehicle Automatically]]. Products still without any function or design link: 52 of 323.
- **2026-10-04 (accessory function review):** 9 functions added (FUNC-00124 to FUNC-00132) and 91 product-to-function links on accessory notes, from the marketed-features lists. Accessories still without a function link: 6 of 159 (IB-152, IB-153).

| Product type | Products | Still without a feature link |
|---|---|---|
| Forklifts | 36 | 9 |
| Batteries | 50 | 14 |
| Ground Support Equipment | 15 | 13 |
| Vehicle Accessories | 90 | 5 |
| Chargers | 42 | 3 |
| Charger Accessories | 8 | 4 |
| Fleet Software and Platforms | 28 | 2 |
| Battery Accessories | 52 | 2 |
| Fuel Cell Power Units | 2 | 0 |

**Products still without a feature link, with the reason**

| Product | Type | Reason |
|---|---|---|
| [[Cat EP14-20 Electric Counterbalance Forklifts]] | Forklifts | source lists the truck family or its options without built-in features, or the features sit in accessory notes linked by offeredWith |
| [[Charlatte CBT350 AC Tow Tractor]] | Ground Support Equipment | source lists the vehicle and its optional devices; the devices have their own notes linked by offeredWith; GSE maker pages not searched |
| [[Charlatte CPB35E Pushback Tractor]] | Ground Support Equipment | source lists the vehicle and its optional devices; the devices have their own notes linked by offeredWith; GSE maker pages not searched |
| [[Charlatte T135 Neo 25T]] | Ground Support Equipment | source lists the vehicle and its optional devices; the devices have their own notes linked by offeredWith; GSE maker pages not searched |
| [[Charlatte T137-V3]] | Ground Support Equipment | source lists the vehicle and its optional devices; the devices have their own notes linked by offeredWith; GSE maker pages not searched |
| [[Crown RM-RMD 6000 Series]] | Forklifts | no source found with features (Crown range page only); searched in round 26 |
| [[Crown SC Series]] | Forklifts | no source found with features (Crown range page only); searched in round 26 |
| [[Crown V-HFM3 Charger Stand]] | Charger Accessories | source names the accessory without describing what it does; PosiCharge accessory pages not retrievable |
| [[Crown V-HFM3 Wired Remote Control Kit]] | Charger Accessories | source names the accessory without describing what it does; PosiCharge accessory pages not retrievable |
| [[Deka MaxPowr Battery]] | Batteries | properties only (chemistry, voltage, capacity, warranty, charge regimes) belong in the metric notes; Flux and Green Cubes feature pages not found in round 26 |
| [[EnerSys IRONCLAD Battery]] | Batteries | properties only (chemistry, voltage, capacity, warranty, charge regimes) belong in the metric notes; Flux and Green Cubes feature pages not found in round 26 |
| [[Exide Sonnenschein Lithium Battery]] | Batteries | properties only (chemistry, voltage, capacity, warranty, charge regimes) belong in the metric notes; Flux and Green Cubes feature pages not found in round 26 |
| [[Flow-Rite Maverick Battery Watering System]] | Battery Accessories | no feature stated in any source yet |
| [[Flux Power GSE Pack]] | Batteries | properties only (chemistry, voltage, capacity, warranty, charge regimes) belong in the metric notes; Flux and Green Cubes feature pages not found in round 26 |
| [[Flux Power LiFT Pack]] | Batteries | properties only (chemistry, voltage, capacity, warranty, charge regimes) belong in the metric notes; Flux and Green Cubes feature pages not found in round 26 |
| [[Fronius Charge & Connect]] | Fleet Software and Platforms | source does not state a function this vault models (iBOS modules; Charge & Connect transport) |
| [[Green Cubes SAFEFlex PLUS Battery]] | Batteries | properties only (chemistry, voltage, capacity, warranty, charge regimes) belong in the metric notes; Flux and Green Cubes feature pages not found in round 26 |
| [[Jungheinrich ETV C16 and C20]] | Forklifts | no features found in sources (searched in round 26) |
| [[Linde 1293 Series (E20BHP and E25BHP)]] | Forklifts | source lists the truck and its lithium option without built-in features beyond those already linked |
| [[Linde 90 V Lithium-Ion Battery]] | Batteries | properties only (chemistry, voltage, capacity, warranty, charge regimes) belong in the metric notes; Flux and Green Cubes feature pages not found in round 26 |
| [[Linde Ei Series]] | Forklifts | its only feature was a property; moved to metric values in round 27 (Watering Interval, Charge Regimes Supported, Charging Gas Emissions) |
| [[Linde Lithium-Ion Charger (9, 17 and 30 kW)]] | Chargers | source gives ratings only, or contents not described (maker unknown, or the DC card conflicts with the AC listing, C82) |
| [[Linde P250 Electric Baggage Tractor]] | Ground Support Equipment | source lists the vehicle and its optional devices; the devices have their own notes linked by offeredWith; GSE maker pages not searched |
| [[Linde Smartphone Holder]] | Vehicle Accessories | convenience item or contents not described in the source |
| [[Oshkosh AeroTech B80E Electric Baggage Tractor]] | Ground Support Equipment | source lists the vehicle and its optional devices; the devices have their own notes linked by offeredWith; GSE maker pages not searched |
| [[Oshkosh AeroTech Commander 30i Cargo Loader]] | Ground Support Equipment | source lists the vehicle and its optional devices; the devices have their own notes linked by offeredWith; GSE maker pages not searched |
| [[Oshkosh AeroTech Pushback B350E and B650E]] | Ground Support Equipment | source lists the vehicle and its optional devices; the devices have their own notes linked by offeredWith; GSE maker pages not searched |
| [[Oshkosh AeroTech Ranger 15E Cargo Loader]] | Ground Support Equipment | source lists the vehicle and its optional devices; the devices have their own notes linked by offeredWith; GSE maker pages not searched |
| [[Philadelphia Scientific iBOS]] | Fleet Software and Platforms | source does not state a function this vault models (iBOS modules; Charge & Connect transport) |
| [[PosiCharge BMID 1]] | Battery Accessories | no feature stated in any source yet |
| [[PosiCharge Cooling Fan Box]] | Charger Accessories | source names the accessory without describing what it does; PosiCharge accessory pages not retrievable |
| [[PosiCharge DIY Fast Charge Kit]] | Vehicle Accessories | convenience item or contents not described in the source |
| [[PosiCharge High Voltage Power Station (AC)]] | Chargers | source gives ratings only, or contents not described (maker unknown, or the DC card conflicts with the AC listing, C82) |
| [[PosiCharge Modular Charge Cables]] | Charger Accessories | source names the accessory without describing what it does; PosiCharge accessory pages not retrievable |
| [[Raymond 8250 Lithium-Ion Battery]] | Batteries | its only feature was a property; moved to metric values in round 27 (Watering Interval, Charge Regimes Supported, Charging Gas Emissions) |
| [[Raymond Energy Essentials Lithium-Ion Battery]] | Batteries | properties only (chemistry, voltage, capacity, warranty, charge regimes) belong in the metric notes; Flux and Green Cubes feature pages not found in round 26 |
| [[Raymond Orderpickers]] | Forklifts | source lists the truck family or its options without built-in features, or the features sit in accessory notes linked by offeredWith |
| [[Stryten M-Series AGM200 Battery]] | Batteries | its only feature was a property; moved to metric values in round 27 (Watering Interval, Charge Regimes Supported, Charging Gas Emissions) |
| [[Stryten M-Series AGM210 Battery]] | Batteries | properties only (chemistry, voltage, capacity, warranty, charge regimes) belong in the metric notes; Flux and Green Cubes feature pages not found in round 26 |
| [[Stryten M-Series F110 Battery]] | Batteries | properties only (chemistry, voltage, capacity, warranty, charge regimes) belong in the metric notes; Flux and Green Cubes feature pages not found in round 26 |
| [[Stryten M-Series T300 Battery]] | Batteries | properties only (chemistry, voltage, capacity, warranty, charge regimes) belong in the metric notes; Flux and Green Cubes feature pages not found in round 26 |
| [[TLD NBL-E Belt Loader]] | Ground Support Equipment | source lists the vehicle and its optional devices; the devices have their own notes linked by offeredWith; GSE maker pages not searched |
| [[TUG 660 Belt Loader]] | Ground Support Equipment | source lists the vehicle and its optional devices; the devices have their own notes linked by offeredWith; GSE maker pages not searched |
| [[TUG ALPHA 1 Pushback]] | Ground Support Equipment | source lists the vehicle and its optional devices; the devices have their own notes linked by offeredWith; GSE maker pages not searched |
| [[TUG Endurance Baggage Tractor]] | Ground Support Equipment | source lists the vehicle and its optional devices; the devices have their own notes linked by offeredWith; GSE maker pages not searched |
| [[Toyota Twistlock Snapshot Camera System]] | Vehicle Accessories | convenience item or contents not described in the source |
| [[Triathlon Lithium-Ion Battery for UniCarriers]] | Batteries | its only feature was a property; moved to metric values in round 27 (Watering Interval, Charge Regimes Supported, Charging Gas Emissions) |
| [[Triathlon Lithium-Ion Charger for UniCarriers]] | Chargers | source gives ratings only, or contents not described (maker unknown, or the DC card conflicts with the AC listing, C82) |
| [[UniCarriers In-Cab Accessories]] | Vehicle Accessories | convenience item or contents not described in the source |
| [[UniCarriers Lighting Packages]] | Vehicle Accessories | convenience item or contents not described in the source |
| [[UniCarriers MX2 and MXL Series]] | Forklifts | source lists the truck family or its options without built-in features, or the features sit in accessory notes linked by offeredWith |
| [[UniCarriers SCX N2 Stand-Up Counterbalanced Forklifts]] | Forklifts | source lists the truck family or its options without built-in features, or the features sit in accessory notes linked by offeredWith |

## Aliases

- Feature capture

## Former ids
