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
- **Result:** 50 products received feature links; products still without any function or design link: 56 of 321 (was 106 of 321 at the start of the pass).

| Product type | Products | Features captured in round 25 | Still without a feature link |
|---|---|---|---|
| Forklifts | 36 | 18 | 15 |
| Batteries | 49 | 10 | 12 |
| Ground Support Equipment | 15 | 2 | 13 |
| Vehicle Accessories | 89 | 8 | 5 |
| Chargers | 42 | 5 | 3 |
| Charger Accessories | 8 | 3 | 4 |
| Fleet Software and Platforms | 28 | 4 | 2 |
| Battery Accessories | 52 | 0 | 2 |
| Fuel Cell Power Units | 2 | 0 | 0 |

**Products still without a feature link, with the reason**

| Product | Type | Reason |
|---|---|---|
| [[Cat EP14-20 Electric Counterbalance Forklifts]] | Forklifts | source lists the truck family or its options without built-in features, or the features sit in accessory notes linked by offeredWith |
| [[Charlatte CBT350 AC Tow Tractor]] | Ground Support Equipment | source lists the vehicle and its optional devices; the devices have their own notes linked by offeredWith |
| [[Charlatte CPB35E Pushback Tractor]] | Ground Support Equipment | source lists the vehicle and its optional devices; the devices have their own notes linked by offeredWith |
| [[Charlatte T135 Neo 25T]] | Ground Support Equipment | source lists the vehicle and its optional devices; the devices have their own notes linked by offeredWith |
| [[Charlatte T137-V3]] | Ground Support Equipment | source lists the vehicle and its optional devices; the devices have their own notes linked by offeredWith |
| [[Crown FC 5700 Series]] | Forklifts | features are InfoLink and InfoPoint; linked to [[Crown InfoLink]] by offeredWith, no separate feature stated |
| [[Crown RC 5700 Series]] | Forklifts | features are InfoLink and InfoPoint; linked to [[Crown InfoLink]] by offeredWith, no separate feature stated |
| [[Crown RM-RMD 6000 Series]] | Forklifts | source lists the truck family or its options without built-in features, or the features sit in accessory notes linked by offeredWith |
| [[Crown RR-RD 5700 Series]] | Forklifts | source lists the truck family or its options without built-in features, or the features sit in accessory notes linked by offeredWith |
| [[Crown SC Series]] | Forklifts | source lists the truck family or its options without built-in features, or the features sit in accessory notes linked by offeredWith |
| [[Crown V-HFM3 Charger Stand]] | Charger Accessories | source names the accessory without describing what it does |
| [[Crown V-HFM3 Wired Remote Control Kit]] | Charger Accessories | source names the accessory without describing what it does |
| [[Deka MaxPowr Battery]] | Batteries | properties only (chemistry, voltage, capacity, warranty, charge regimes) belong in the metric notes, not in functions |
| [[EnerSys IRONCLAD Battery]] | Batteries | properties only (chemistry, voltage, capacity, warranty, charge regimes) belong in the metric notes, not in functions |
| [[EnerSys NexSys iON Battery]] | Batteries | properties only (chemistry, voltage, capacity, warranty, charge regimes) belong in the metric notes, not in functions |
| [[Exide Sonnenschein Lithium Battery]] | Batteries | properties only (chemistry, voltage, capacity, warranty, charge regimes) belong in the metric notes, not in functions |
| [[Flow-Rite Maverick Battery Watering System]] | Battery Accessories | no feature stated in any source yet |
| [[Flux Power GSE Pack]] | Batteries | properties only (chemistry, voltage, capacity, warranty, charge regimes) belong in the metric notes, not in functions |
| [[Flux Power LiFT Pack]] | Batteries | properties only (chemistry, voltage, capacity, warranty, charge regimes) belong in the metric notes, not in functions |
| [[Fronius Charge & Connect]] | Fleet Software and Platforms | source does not state a function this vault models (iBOS modules; Charge & Connect transport) |
| [[Green Cubes SAFEFlex PLUS Battery]] | Batteries | properties only (chemistry, voltage, capacity, warranty, charge regimes) belong in the metric notes, not in functions |
| [[Jungheinrich ETV C16 and C20]] | Forklifts | source lists the truck family or its options without built-in features, or the features sit in accessory notes linked by offeredWith |
| [[Linde 1293 Series (E20BHP and E25BHP)]] | Forklifts | source lists the truck family or its options without built-in features, or the features sit in accessory notes linked by offeredWith |
| [[Linde 90 V Lithium-Ion Battery]] | Batteries | properties only (chemistry, voltage, capacity, warranty, charge regimes) belong in the metric notes, not in functions |
| [[Linde E Series Electric Counterbalance Forklifts]] | Forklifts | source lists the truck family or its options without built-in features, or the features sit in accessory notes linked by offeredWith |
| [[Linde Lithium-Ion Charger (9, 17 and 30 kW)]] | Chargers | source gives ratings only, or contents not described (maker unknown, or the DC card conflicts with the AC listing, C82) |
| [[Linde P250 Electric Baggage Tractor]] | Ground Support Equipment | source lists the vehicle and its optional devices; the devices have their own notes linked by offeredWith |
| [[Linde Smartphone Holder]] | Vehicle Accessories | convenience item or contents not described in the source |
| [[Oshkosh AeroTech B80E Electric Baggage Tractor]] | Ground Support Equipment | source lists the vehicle and its optional devices; the devices have their own notes linked by offeredWith |
| [[Oshkosh AeroTech Commander 30i Cargo Loader]] | Ground Support Equipment | source lists the vehicle and its optional devices; the devices have their own notes linked by offeredWith |
| [[Oshkosh AeroTech Pushback B350E and B650E]] | Ground Support Equipment | source lists the vehicle and its optional devices; the devices have their own notes linked by offeredWith |
| [[Oshkosh AeroTech Ranger 15E Cargo Loader]] | Ground Support Equipment | source lists the vehicle and its optional devices; the devices have their own notes linked by offeredWith |
| [[Philadelphia Scientific iBOS]] | Fleet Software and Platforms | source does not state a function this vault models (iBOS modules; Charge & Connect transport) |
| [[PosiCharge BMID 1]] | Battery Accessories | no feature stated in any source yet |
| [[PosiCharge Cooling Fan Box]] | Charger Accessories | source names the accessory without describing what it does |
| [[PosiCharge DIY Fast Charge Kit]] | Vehicle Accessories | convenience item or contents not described in the source |
| [[PosiCharge High Voltage Power Station (AC)]] | Chargers | source gives ratings only, or contents not described (maker unknown, or the DC card conflicts with the AC listing, C82) |
| [[PosiCharge Modular Charge Cables]] | Charger Accessories | source names the accessory without describing what it does |
| [[Raymond 4000 Series Counterbalanced Trucks]] | Forklifts | source lists the truck family or its options without built-in features, or the features sit in accessory notes linked by offeredWith |
| [[Raymond 8000 Series Pallet Trucks]] | Forklifts | source lists the truck family or its options without built-in features, or the features sit in accessory notes linked by offeredWith |
| [[Raymond Energy Essentials Lithium-Ion Battery]] | Batteries | properties only (chemistry, voltage, capacity, warranty, charge regimes) belong in the metric notes, not in functions |
| [[Raymond Orderpickers]] | Forklifts | source lists the truck family or its options without built-in features, or the features sit in accessory notes linked by offeredWith |
| [[Stryten M-Series AGM210 Battery]] | Batteries | properties only (chemistry, voltage, capacity, warranty, charge regimes) belong in the metric notes, not in functions |
| [[Stryten M-Series F110 Battery]] | Batteries | properties only (chemistry, voltage, capacity, warranty, charge regimes) belong in the metric notes, not in functions |
| [[Stryten M-Series T300 Battery]] | Batteries | properties only (chemistry, voltage, capacity, warranty, charge regimes) belong in the metric notes, not in functions |
| [[TLD NBL-E Belt Loader]] | Ground Support Equipment | source lists the vehicle and its optional devices; the devices have their own notes linked by offeredWith |
| [[TUG 660 Belt Loader]] | Ground Support Equipment | source lists the vehicle and its optional devices; the devices have their own notes linked by offeredWith |
| [[TUG ALPHA 1 Pushback]] | Ground Support Equipment | source lists the vehicle and its optional devices; the devices have their own notes linked by offeredWith |
| [[TUG Endurance Baggage Tractor]] | Ground Support Equipment | source lists the vehicle and its optional devices; the devices have their own notes linked by offeredWith |
| [[Toyota Twistlock Snapshot Camera System]] | Vehicle Accessories | convenience item or contents not described in the source |
| [[Triathlon Lithium-Ion Charger for UniCarriers]] | Chargers | source gives ratings only, or contents not described (maker unknown, or the DC card conflicts with the AC listing, C82) |
| [[UniCarriers In-Cab Accessories]] | Vehicle Accessories | convenience item or contents not described in the source |
| [[UniCarriers Lighting Packages]] | Vehicle Accessories | convenience item or contents not described in the source |
| [[UniCarriers MX2 and MXL Series]] | Forklifts | source lists the truck family or its options without built-in features, or the features sit in accessory notes linked by offeredWith |
| [[UniCarriers SCX N2 Stand-Up Counterbalanced Forklifts]] | Forklifts | source lists the truck family or its options without built-in features, or the features sit in accessory notes linked by offeredWith |
| [[Yale ERC050-060VGL]] | Forklifts | source lists the truck family or its options without built-in features, or the features sit in accessory notes linked by offeredWith |

## Aliases

- Feature capture

## Former ids
