---
type: Info
subtype:
id: INFO-00239
uid: 20261003150838730skellyspencer
status: Draft
tags:
  - coverage
  - scope
  - plan
  - conventions
describes:
  - "[[Battery-Connected Product]]"
---

# Coverage Plan

## Definition

How the catalog decides which makers and products to include, what a finished category means, and the current coverage against reference makers, worldwide.

## Notes

- **Owner decisions this plan implements (2026-10-03):** the neutral market reference drives; the market scope is global; a category is finished when the top makers are covered plus a sample of the rest. The numbers and rules below that turn those decisions into tests are proposals until the owner confirms them (see [[Project Objectives (Draft)]]).

**Proposed rules**

1. **Reference makers.** For each product type, the reference makers are chosen from a cited ranking or list in this note. Forklift OEMs have a credible annual ranking (tier T2). Batteries, chargers, accessories and GSE have no authoritative ranking in what was found, so their reference makers are those named by at least two independent lists, with the lists shown (tier T4 for marketing and report-table lists).
2. **Top makers covered.** A reference maker counts as covered for a type when it has at least one product note of that type, or a dated entry saying a search found none.
3. **Sample of the rest.** For each type and each world region (Americas, Europe, Asia-Pacific, Middle East and Africa), add at least three makers outside the reference list, chosen to differ in business model (OEM-integrated, independent, private label) and, for batteries, in chemistry. The selection reason is written on each organization note. This rule is what keeps the sample from being only what English-language web pages show.
4. **Product finish test (owner decision, 2026-10-03: the minimum differs by product type; the numbers are proposals).** A product note counts toward coverage when it names its maker or offerer, its category, a source file or page with its tier, and at least the number of values below from the category's metric set (or says the source gives none):

| Product type | Proposed minimum values | Which values |
|---|---|---|
| Batteries | 4 | chemistry, nominal voltage range, capacity, cycle life or warranty |
| Chargers | 5 | voltage range, output power and current, input, efficiency, chemistries or charge regimes (certifications where stated) |
| Forklifts and other trucks | 3 | class or type, rated capacity, battery type and voltage; plus the truck-side devices offered, linked, since lifting power matters less than devices (owner) |
| Battery accessories and monitors | 3 | what it measures or does, interfaces, mounting and temperature or enclosure data |
| Charger accessories | 2 | what it does and which chargers it fits |
| Vehicle accessories | 3 | detection or function, response, integration and availability (the truck metrics) |
| Fleet software and platforms | 2 | functions and data interfaces |
| Fuel cell power units | 3 | power, refuel time, fuel storage |
| Ground support equipment vehicles | 3 | vehicle type, drive and battery voltage, capacity |

5. **Region.** Each organization note records headquarters and regions served with a source. Product notes record the standards the source names (UL, CE, GB/T and others) through the certifications metric.
6. **Neutrality.** Every maker is treated alike in the catalog, including PosiCharge and Power Designers: same fields, same evidence rules, no extra depth. Ampure's internal-versus-external classification belongs to the business analysis, not to the catalog.
7. **Priority.** Document and research priority follows coverage need (reference makers with no product notes first), not the owner's company.
8. **Evidence tiers (owner decision, 2026-10-03: dealer and trade press count as decision-grade if labelled by tier).** Tiers are the ones in [[Landscape Evidence and Modeling Conventions]]: T1 manufacturer product page, data sheet, manual or vendor app listing; T2 manufacturer press release or trade press quoting the manufacturer; T3 reseller or parts-catalog listing; T4 third-party blog, training material or vendor marketing; T5 patent. Proposed handling: every value carries its tier; a T3 or T4 value never overrides a T1 or T2 value (both stay visible and a conflict is logged); a value that has only T3 or T4 support is marked 'single lower-tier source' in matrices; a comparison matrix shows the tier next to any value below T2.

**Reference evidence**

- Forklift OEM ranking: Modern Materials Handling 2025 list of top global lift truck suppliers (2024 revenue), through Supply Chain 24/7 (T2). <https://www.supplychain247.com/article/top-20-lift-truck-suppliers-2025>; the 2024 edition adds North American brands per company, for example Toyota with Raymond, Mitsubishi Logisnext with UniCarriers, Mitsubishi, Cat, Jungheinrich in North America and Rocla, and Hyster-Yale with Hyster, Yale, Nuvera and Bolzoni (T2). <https://www.robotics247.com/article/top_20_lift_truck_suppliers_2024>; Statista-derived 2019 list with headquarters countries (T3). <https://xpert.digital/en/top-ten-leading-manufacturers-of-industrial-trucks-in-intralogistics/?amp=1>; a market report puts Asia Pacific at about 39 percent of lift truck revenue in 2023 (T3). <https://gminsights.com/industry-analysis/lift-trucks-market/market-share>
- Battery maker lists (all T4, none is a ranking): A SkyQuest forklift battery companies <https://www.skyquestt.com/report/forklift-battery-market/companies>; B Tritek top 10 industrial battery manufacturers (a maker's own blog) <https://tritekbattery.com/top-10-industrial-battery-manufacturers/>; C Kings Research top 10 <https://www.kingsresearch.com/blog/top-10-forklift-battery-companies>; D 2018 PR Newswire forklift battery report <https://www.prnewswire.com/in/news-releases/forklift-battery-industry-2018-global-market-growth-trend-and-forecast-to-2025-677410213.html>; E 2020 GlobeNewswire forklift battery report <https://www.globenewswire.com/en/news-release/2020/11/27/2135171/28124/en/Worldwide-Forklift-Battery-Industry-to-2025-Featuring-Exide-Technologies-East-Penn-Manufacturing-Enersys-Among-Others.html>; F MarketsandMarkets industrial batteries <https://marketsandmarkets.com/ResearchInsight/industrial-batteries-market.asp>; G Market Reports World table of contents <https://www.marketreportsworld.com/market-reports/toc/forklift-battery-market-14714595>.
- GSE makers: EPRI lists Charlatte, Eagle, JBT, JetPorter, Lektro, TLD America and TUG for electric GSE (T2). <https://restservice.epri.com/publicdownload/000000003002005771/0/Product>
- Chargers, monitors and accessories: no ranking found; the reference list will be the makers that appear in OEM option lists and battery maker charger lines until a source is found.

**Coverage ledger (generated from the vault, 2026-10-03)**

*Forklift OEMs against the 2025 ranking*

| Rank (2025 list, 2024 revenue) | Company as ranked | Vault organization | 2024 revenue | Headquarters stated by a source | Forklift products on file (with subsidiaries and brands) | All product notes on file (with subsidiaries and brands) | Status |
|---|---|---|---|---|---|---|---|
| 1 | Toyota Industries Corporation | [[Toyota Industries Corporation]] | not stated in the retrieved text | Japan (Kariya, Aichi; 2024 list) | 6 | 39 | covered |
| 2 | KION Group | [[KION Group]] | $8.96B | Germany (2019 list) | 6 | 33 | covered |
| 3 | Jungheinrich | [[Jungheinrich]] | $5.60B | Germany (2019 list) | 1 | 9 | covered |
| 4 | Crown Equipment Corp. | [[Crown Equipment]] | not stated in the retrieved text | United States (2019 list) | 5 | 22 | covered |
| 5 | Mitsubishi Logisnext Co. | [[Mitsubishi Logisnext]] | not stated in the retrieved text | Japan (Kyoto; 2024 list) | 1 | 1 | covered |
| 6 | Hyster-Yale | [[Hyster-Yale]] | $4.30B | United States (Cleveland; 2024 list) | 3 | 13 | covered |
| 7 | Anhui Forklift Group | [[Anhui Heli]] | $2.51B | China (the vault note is titled Anhui Heli; see C84) | 2 | 6 | covered |
| 8 | Hangcha Group | [[Hangcha Group]] | $2.29B | China (2019 list) | 2 | 5 | covered |
| also named in other lists | Doosan Industrial Vehicle, Komatsu, Hyundai Heavy Industries | [[Doosan Bobcat]], [[Komatsu]] | - | South Korea (Doosan, 2019 list) | 3 | 9 | covered |

*Battery makers against the lists above*

| Maker | Vault organization | Headquarters named by a list | Lists naming it | Battery product notes on file | All product notes on file | Status |
|---|---|---|---|---|---|---|
| EnerSys | [[EnerSys]] | United States | A, B, C, E, F | 3 | 11 | covered |
| East Penn Manufacturing | [[East Penn Manufacturing]] | United States | A, B, C, D, E, G | 10 | 15 | covered |
| Exide Technologies | [[Exide Technologies]] | United States | A, B, E | 6 | 12 | covered |
| Exide Industries (India) | - | India (D, F) | D, F | 0 | 0 | gap: no org note |
| HOPPECKE | [[HOPPECKE]] | Germany | A, B, C, D | 3 | 6 | covered |
| Crown Battery Manufacturing | - | United States | A, D, E, G (the lists also name 'Crown Equipment Corporation'; see C84) | 0 | 0 | gap: no org note |
| Midac | [[Midac]] | Italy | A, D, G | 1 | 4 | covered |
| Flux Power | [[Flux Power]] | United States | A, C, E | 3 | 3 | covered |
| GS Yuasa | - | Japan | A, B | 0 | 0 | gap: no org note |
| Leoch International | - | China | A, B, F | 0 | 0 | gap: no org note |
| Banner Batteries | - | Austria | A, G | 0 | 0 | gap: no org note |
| Stryten Energy | [[Stryten Energy]] | United States | B only (but 15 or more product notes on file) | 10 | 16 | covered |
| Tianneng, Amara Raja, Godrej, Forsee Power, OneCharge, GB Industrial Battery, Hawker, Clarios, Saft, Hitachi Chemical, Trojan, Navitas, Storage Battery Systems | - | various | one list each | 0 | 0 | single-list names: not yet screened |

*Makers that are the direct maker or offerer of at least one product note, by product type (parent companies are not rolled up here)*

| Product type | Makers with at least one product note | Makers |
|---|---|---|
| Batteries | 18 | [[Anhui Heli]], [[Crown Equipment]], [[East Penn Manufacturing]], [[EnerSys]], [[Exide Technologies]], [[Flux Power]], [[Green Cubes Technology]], [[HOPPECKE]], [[Hangcha Group]], [[Jungheinrich]], [[Linde Material Handling]], [[Logisnext Europe]], [[Midac]], [[Mitsubishi Logisnext Americas]], [[Raymond]], [[Stryten Energy]], [[Toyota Material Handling]], [[Triathlon USA]] |
| Chargers | 19 | [[AMETEK Prestolite Power]], [[Advanced Charging Technologies]], [[Anhui Heli]], [[Crown Battery Manufacturing]], [[Crown Equipment]], [[Delta-Q Technologies]], [[East Penn Manufacturing]], [[EnerSys]], [[Exide Technologies]], [[Fronius International]], [[Green Cubes Technology]], [[HOPPECKE]], [[Lester Electrical]], [[Linde Material Handling]], [[PosiCharge]], [[Power Designers]], [[Raymond]], [[Stryten Energy]], [[Triathlon USA]] |
| Forklifts | 14 | [[Anhui Heli]], [[Crown Equipment]], [[Doosan Bobcat]], [[Hangcha Group]], [[Hyster-Yale]], [[Jungheinrich]], [[Komatsu]], [[Linde Material Handling]], [[Logisnext Europe]], [[Mitsubishi Logisnext]], [[Mitsubishi Logisnext Americas]], [[Raymond]], [[STILL]], [[Toyota Material Handling]] |
| Battery Accessories | 19 | [[AMETEK Prestolite Power]], [[Access Control Group]], [[Advanced Charging Technologies]], [[Anderson Power Products]], [[Crown Equipment]], [[EnerSys]], [[Energywith]], [[Exide Technologies]], [[Flow-Rite]], [[Fronius International]], [[HOPPECKE]], [[Hyster-Yale]], [[Inventus Power]], [[Midac]], [[Philadelphia Scientific]], [[PosiCharge]], [[Power Designers]], [[Raymond]], [[Sunlight Group]] |
| Charger Accessories | 2 | [[Crown Equipment]], [[PosiCharge]] |
| Vehicle Accessories | 25 | [[Anhui Heli]], [[Blaxtair]], [[Crown Equipment]], [[Doosan Bobcat]], [[EnerSys]], [[Hangcha Group]], [[Holt of California]], [[Hyster-Yale]], [[Jungheinrich]], [[Komatsu]], [[Larson Electronics]], [[Linde Material Handling]], [[Logisnext Europe]], [[Mallaghan]], [[Mitsubishi Logisnext Americas]], [[Oshkosh AeroTech]], [[Panacea Aftermarket Co.]], [[PosiCharge]], [[Powerfleet]], [[Raymond]], [[STILL]], [[TLD Group]], [[TVH]], [[Textron GSE]], [[Toyota Material Handling]] |
| Fleet Software and Platforms | 20 | [[Advanced Charging Technologies]], [[Adveez]], [[Anhui Heli]], [[Crown Equipment]], [[Doosan Bobcat]], [[Fronius International]], [[Hangcha Group]], [[Hyster-Yale]], [[Jungheinrich]], [[Komatsu]], [[Linde Material Handling]], [[Mitsubishi Logisnext Americas]], [[Oshkosh AeroTech]], [[Philadelphia Scientific]], [[PosiCharge]], [[Powerfleet]], [[Raymond]], [[STILL]], [[Stryten Energy]], [[Toyota Material Handling]] |
| Fuel Cell Power Units | 2 | [[Nuvera]], [[Plug Power]] |
| Ground Support Equipment | 6 | [[Charlatte Manutention]], [[Linde Material Handling]], [[Mallaghan]], [[Oshkosh AeroTech]], [[TLD Group]], [[Textron GSE]] |

- **Region recorded:** 37 of 73 organization notes carry a region tag; the rest have none, so regional coverage cannot be measured yet. Backlog: record headquarters and regions served with a source on every organization note.
- **What the ledger shows (round 24):** all eight ranked forklift OEMs have at least one electric truck note; Mitsubishi Logisnext is now split into group, Americas and Europe entities; the thin spots are manufacturer-level sources for the Asian makers and Mitsubishi (dealer data, T3), the Asian and Indian battery makers, and the region field on organization notes.

## Aliases

- Coverage rules

## Former ids
