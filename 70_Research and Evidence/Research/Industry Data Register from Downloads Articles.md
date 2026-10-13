---
type: Info
subtype:
id: INFO-90012
uid: 20261013150100000skellyspencer
status: Draft
tags:
  - industry-data
  - register
  - forklift
  - lithium
  - market
  - vendor-claims
describes: []
describedBy:
  - "[[Document - Zhang 5 Things to Check Before Switching from Lead-Acid to Lithium (2026-08-09)]]"
  - "[[Document - Zhang The Battery Price War Will Not Last Forever (2026-08-18)]]"
  - "[[Document - Zhang Why Lithium Forklifts Are Becoming the New Standard (2026-08-25)]]"
  - "[[Document - Zhang How Lithium-Ion Battery Systems Improve AGV Performance (2026-08-30)]]"
  - "[[Document - Zhang AMR and AGV the Power Behind Industry 4.0 (2026-09-07)]]"
  - "[[Document - Zhang When Does a Smart Battery Become Too Smart (2026-09-21)]]"
  - "[[Document - Zhang How to Maintain a Lithium Forklift Battery (2026-10-05)]]"
  - "[[Document - Zhang Passive vs Active Battery Balancing (2026-10-12)]]"
  - "[[Document - BlitzNXT How to Choose a Forklift Lithium Battery (2026-09-23)]]"
  - "[[Document - BlitzNXT Forklift Battery Charging Best Practices (2026-09-26)]]"
  - "[[Document - BlitzNXT How to Read a Forklift Battery Nameplate (2026-09-29)]]"
  - "[[Document - BlitzNXT How Lithium Forklift Batteries Free Up Floor Space (2026-10-03)]]"
  - "[[Document - BlitzNXT Class I II III Forklifts and Lithium Battery Configuration (2026-10-10)]]"
  - "[[Document - ENEROC Propane to Electric Battery Sizing (2026-09-23)]]"
  - "[[Document - Flux Power Lithium-Ion Forklift Battery Charger Best Practices (2026-07-14)]]"
  - "[[Document - ITW GSE Charging and Energy Management for Electric Airport Operations]]"
  - "[[Document - ITW GSE Scale Electric GSE Charging Without Bottlenecks (2026-04-23)]]"
  - "[[Document - LinkedIn Forklift Market-Report Posts (2026-09 to 2026-10)]]"
  - "[[Document - FridayParts 24V-80V LiFePO4 Forklift Battery Listing (retrieved 2026-10-13)]]"
  - "[[Document - Supply Chain 24-7 ENEROC USA Launches Operations in North America (2026-03-10)]]"
  - "[[Document - ITW GSE EcoGate Page (retrieved 2026-10-13)]]"
  - "[[Document - BloombergNEF Lithium-Ion Battery Pack Prices Fall to 108 USD per kWh (2025-12-09)]]"
  - "[[Document - OTTO Motors Mauser Packaging Solutions Case Study]]"
  - "[[Document - Green Cubes SAFEFlex AGV Opportunity Charging Case Study (2017-06-22)]]"
  - "[[Document - Inside Logistics Rockwell Automation Buys OTTO Motors]]"
---

# Industry Data Register from Downloads Articles

## Definition

One place for the industry data found in the LinkedIn articles, vendor blog posts and manufacturer web pages saved in `Downloads/`: reference values, vendor product data, market figures and company names, each with its source note, evidence tier and checking status. Built 2026-10-13 so stakeholders can review it and so new information has something to be compared against.

## Notes

**Why this exists.** The vault already holds customer-need evidence ([[Demand Evidence Source Register]]) and reference values ([[Generic Reference Values]]). This register keeps industry data that supports neither directly: market sizes, competitor products, charging practice, sizing methods. It is retained because the project goal is to hold industry knowledge in one place, not because the sources are strong.

**How to read the tiers.** Every source here is T4 (vendor marketing, blog or templated post; [[Landscape Evidence and Modeling Conventions]]). A figure marked *verified* was checked against a primary page on 2026-10-13. A figure marked *stated* is the source's own claim. A figure marked *do not use* failed an internal check; it is kept so the failure is visible.

### 1. Checked against primary sources (source notes DOC-00034 to DOC-00036)

| Claim (where it appears) | Primary source | Result |
|---|---|---|
| 2025 global average lithium-ion pack price 108 USD/kWh, China 84 USD/kWh ([[Document - Zhang The Battery Price War Will Not Last Forever (2026-08-18)]]) | [BloombergNEF release, 2025-12-09](https://about.bnef.com/insights/clean-energy/lithium-ion-battery-pack-prices-fall-to-108-per-kilowatt-hour) | *Verified.* Release: 108 USD/kWh, down 8 percent from 2024; China 84 USD/kWh, down 13 percent in real terms; stationary storage 70 USD/kWh. The release gives no forklift or industrial-truck price, so this is not a forklift battery price. BloombergNEF expects a further fall in 2026 |
| OTTO 1500 completes up to 36 missions before charging versus 3 to 4 for the previous AGV system ([[Document - Zhang AMR and AGV the Power Behind Industry 4.0 (2026-09-07)]]) | [OTTO Motors Mauser case study](https://ottomotors.com/resources/case-studies/mauser/) | *Verified with qualifications.* Page says 'up to 36 missions', previous system 3 to 4 missions then 25 to 30 minutes of charging, OTTO returns to charge at about 70 percent battery, headline '6x' defined as missions before charging, not throughput. No date on the page. See C184 |
| LFP AGV system with 98 to 99 percent charge efficiency in a 24/7 case ([[Document - Zhang How Lithium-Ion Battery Systems Improve AGV Performance (2026-08-30)]]) | [Green Cubes case study, posted 2017-06-22](https://greencubes.com/blog/lithium-safeflex-case-study-agv-opportunity-charging/) | *Partly verified.* Page says LFP 'has a charge efficiency of 98-99%' as a general statement; customer unnamed; no voltage or capacity; metric undefined. See C184 |

### 2. Reference statements (single-source unless noted)

| Topic | Statement as made | Source note | Status |
|---|---|---|---|
| Truck classes | OSHA Class I electric rider, II electric narrow aisle, III electric hand or hand/rider; ANSI/ITSDF B56.1 is the safety standard; class does not set battery voltage | [[Document - BlitzNXT Class I II III Forklifts and Lithium Battery Configuration (2026-10-10)]] | stated |
| Voltage by class | Class III 24 V (36 V some); Class II 36 or 48 V; Class I 36, 48, 80 V; 48 V most common for 1.5 to 5 ton counterbalanced; 72 or 80 V heavy duty | same and [[Document - BlitzNXT How to Choose a Forklift Lithium Battery (2026-09-23)]] | stated; same author, one source |
| Ah rating basis | Lead-acid forklift batteries rated at the 6-hour rate; lithium commonly at 0.2 C (5 hours) | [[Document - BlitzNXT How to Read a Forklift Battery Nameplate (2026-09-29)]] | stated; see C182 |
| LFP pack voltage | '48 V' LFP pack nominal 51.2 V, charges to 54 V | How to Choose; Charging Best Practices | stated; 16 cells x 3.2 V = 51.2 V checks |
| LFP BMS limits | Over-charge cut-off typically 3.65 V per cell; over-discharge typically 2.5 V per cell | How to Choose | stated |
| Charge temperature | Charge about 0 to 45 C; suspend below 0 C and above 45 C; operating -20 to 50 C | BlitzNXT posts; consistent with lithium-plating warning in [[Document - Zhang How to Maintain a Lithium Forklift Battery (2026-10-05)]] | stated, two authors agree on the 0 C lower limit |
| Storage | Roughly 50 percent SOC in a cool, dry place if idle for weeks; follow manufacturer range; check periodically | [[Document - BlitzNXT Forklift Battery Charging Best Practices (2026-09-26)]]; Zhang maintenance post | stated, agree |
| Opportunity charging | Plug in for any break of 15 minutes or longer; 15 to 30 minute top-ups | Charging Best Practices; floor-space post | stated |
| Hydrogen | Flooded lead-acid charging gives hydrogen, explosive from 4 percent in air; 29 CFR 1910.178(g) requires designated charging areas | [[Document - BlitzNXT How Lithium Forklift Batteries Free Up Floor Space (2026-10-03)]] | stated; 4 percent is a commonly published limit, not verified here |
| Charging-area standards | 29 CFR 1910.178(g), NFPA 505; UL 2580 for EV batteries; IEC 62619 for industrial lithium cells | BlitzNXT posts | stated |
| Propane to electric | 1 gallon of propane does the work of about 4.85 kWh (OEM data under ISO 23308); metered hours about 65 percent of shift; +15 percent capacity for cold; size to end-of-life capacity | [[Document - ENEROC Propane to Electric Battery Sizing (2026-09-23)]] | stated; conversion table not captured; see C183 |
| Lead-acid and lithium discharge limits | Lead-acid not below 40 percent of rated capacity; LFP 80 percent depth of discharge or 80 to 90 percent usable | ENEROC; How to Choose | stated; conflicts with vault values, see C177 |
| Cost trend | Pack prices at record low; differentiation moving to BMS, SOC and SOH accuracy, remote monitoring, CAN, OTA, traceability | Zhang price-war post | opinion plus verified price (section 1) |
| Charger partners | Flux Power names Stanbury, Delta-Q and PosiCharge as certified charger partners | [[Document - Flux Power Lithium-Ion Forklift Battery Charger Best Practices (2026-07-14)]] | stated by manufacturer; also recorded on [[Flux Power]] |
| GSE charging | ITW GSE offers Power Share, Intelligent Power Management and a 60 kW per outlet CCS2 DC Charger, and describes EcoGate as a design approach, not a product, to share gate power between GPU, PCA and GSE charging | [[Document - ITW GSE EcoGate Page (retrieved 2026-10-13)]]; [[Document - ITW GSE Charging and Energy Management for Electric Airport Operations]] | stated by manufacturer; only the DC Charger has figures |
| BMS data for automation | SOC, SOH, pack and cell voltage, current, temperature, charging status, faults over CAN, RS485 or UART; fleet systems use them for charging and mission decisions | Zhang AMR and AGV posts | stated; supports the SOC and SOH estimation functions |

### 3. Vendor product data: BlitzNXT LiFePO4 forklift batteries

Figures are as stated by the vendor (C178 to C181). Computed columns use only the stated figures.

| Model | Nominal V | Ah | Stated energy, kWh | Ah x V, kWh | Continuous / peak A | Size | Mass | Wh/kg (computed) | Wh/L (computed) |
|---|---|---|---|---|---|---|---|---|---|
| 24 V 230 Ah | 25.6 | 230 | 5.9 'usable' | 5.89 | 115 / 175 | 662 x 650 x 195 mm | about 105 kg | 56 | 70 |
| 48 V 460 Ah | 51.2 | 460 | 23.6 'usable' | 23.55 | 100 / 350 | 32.7 x 22.0 x 16.0 in | about 507 lb (230 kg) | 102 | 125 |
| 48 V 608 Ah | 51.2 | 608 | 31.1 'usable' | 31.13 | 121.6 / 350 | 38.15 x 32.60 x 22.64 in | about 864 lb (392 kg) | 79 | 67 |
| 80 V 460 Ah | 80 | 460 | 36.8 'usable' | 36.80 | 100 / 350 | 39.0 x 24.0 x 16.9 in | about 595 lb (270 kg) | 136 | 142 |
| 36 V 920 Ah | not stated | 920 | not stated | not computed | not stated | not stated | not stated | | |

Other vendor claims: EVE Grade A cells, IP67, 10-year warranty, 3,000+ cycles, REMA 320A and Anderson 350A connectors, built-in charge port and circular level indicator on the 24 V model, 54 V / 200 A charge rating on a 48 V-class pack (model not stated).

These are batteries, which the vault's product scope treats as the thing accessories are added to. Whether to create product notes for them is an open question (section 7).

### 4. Cross-check against the Fleetman chart already in the vault

[[Generic Reference Values]] holds the Fleetman lead-acid chart (42 rows). Comparing it with BlitzNXT's 'drop-in' claims gives (C180): 48 V lead-acid trays weigh 2,088 to 3,288 lb and stand 22.62 to 30.50 in high; 80 V trays weigh 2,920 to 4,960 lb and stand 23.68 to 33.13 in high. BlitzNXT's 48 V 608 Ah (864 lb) is 59 to 74 percent lighter and its 80 V 460 Ah (595 lb) is 80 to 88 percent lighter, against the 30 to 50 percent the same posts say. The two 460 Ah packs are 16.0 and 16.9 in high, below any lead-acid tray height of those voltages. Only the 608 Ah pack (38.15 x 32.60 x 22.64 in) matches a lead-acid tray, the 24-85-21 (38.13 x 32.63 x 22.63 in, 850 Ah, 39.58 kWh, 3,288 lb). The Fleetman figures are steel tray sizes, not truck compartment sizes; ratings are on different bases. Counterweight consequences are not quantified by any source.

### 5. Market figures (as stated; see C172 to C176)

| Market as labeled | 2025 | 2035 | Stated CAGR | Fits 10 years from 2025? | Use |
|---|---|---|---|---|---|
| Forklift lead-acid battery (warehouse automation), three posts, one report id | USD 894 million | USD 1.48 billion | 5.2% ('2027 to 2035') | yes (5.17%); eight years would be 6.5% | do not use as evidence |
| Lithium-ion forklift battery (warehouse automation) | USD 1.3 billion | USD 2.94 billion | 8.5% | yes (8.50%) | do not use as evidence |
| Commercial electric forklift battery | USD 2.76 billion | USD 7.5 billion | 10.5% | yes (10.51%) | do not use as evidence |
| Forklift battery charger | USD 1.26 billion | USD 2.05 billion | about 5.0% | yes (4.99%) | do not use as evidence |
| Forklift battery rental | USD 160.8 billion | USD 322.28 billion | 7.2% | yes (7.20%) | do not use: 58 times the commercial electric battery figure |

The arithmetic is internally consistent (the numbers were generated from a ten-year rate), but publisher, method, scope and base year are not given, and the posts reuse text from automotive-service markets. They show only what the market-report vendors are advertising. Any market size the stakeholders need should come from a named, purchasable or published study.

### 6. Company names appearing in the posts

Lead-acid battery makers listed: Johnson Controls, Exide Technologies, East Penn Manufacturing, EnerSys, GS Yuasa, Crown Battery, Clarios, Hoppecke Batterien, Leoch International, Narada Power. Lithium list adds BYD, Samsung SDI, LG Chem, Panasonic, Toshiba and (in a competitive-strategies post) Tesla and LG Energy Solution. Commercial electric list: EnerSys, Hoppecke, East Penn Manufacturing, Exide Technologies, Hitachi Chemical, GS Yuasa, Systems Sunlight, Saft, Electrovaya, FAAM. Charger list: Proterra, EnerSys, Crown Equipment Corporation, Hyster-Yale, Toyota Material Handling, JLG, Plug Power, East Penn, Ametek, Delta-Q. Proterra, Tesla and Systems Sunlight have no vault note and no vault source shows them supplying forklift batteries or chargers (C175).

### 7. Entities created from this register (2026-10-13)

- Organizations: [[BlitzNXT]], [[ENEROC]], [[OTTO Motors]], [[ITW GSE]].
- Products: [[BlitzNXT LiFePO4 Forklift Battery]] (one line note with a model table, not one note per model, because the evidence is vendor posts and a reseller listing), [[ITW GSE DC Charger]].
- Not created: product notes for ITW GSE Power Share, Intelligent Power Management and EcoGate. ITW's own page says EcoGate is 'a design approach ... not a single product', IPM is hosted in the 3500 PCA, and none of the three has published specifications; they are recorded as offerings in [[ITW GSE]].
- Primary-source notes added for the verification in section 1 and for the new entities: DOC-00031 to DOC-00037.
- Cross-check with the reseller listing: the BlitzNXT pack sizes appear on a FridayParts listing with different voltage labels, cycle life and warranty, and with the truck models each pack is sold for (C185).

### 8. Open questions

- Can the original LinkedIn addresses be recorded? The saved PDFs do not carry them.
- Is there a named market study the stakeholders want used in place of the market-report posts?
- The BlitzNXT truck-fit data (Toyota 7FB and 8FB, Lonking, TCM, Doosan, Hyundai, Mitsubishi, Linde, Jungheinrich) could feed the truck-compartment notes if a data sheet confirms it.

Related: [[Downloads Value Screening Register]], [[Demand Evidence Source Register]], [[Generic Reference Values]], [[Battery Product Landscape Conflicts and Open Questions]], [[Flux Power]]

## Evidence status of the captured posts (2026-10-13 CI fix)

- **Source address verified or matched:** BlitzNXT posts (DOC-00021 to DOC-00025: website posts of the same topics found, dates differ from the saved LinkedIn copies, text not compared), Flux Power guide (DOC-00027, fetched, date matches), ITW GSE Scale Electric post (DOC-00029, fetched, title and date match), ITW GSE charging page (DOC-00028).
- **No public address recoverable:** the eight Zhang LinkedIn posts, the ENEROC LinkedIn article and the eleven market-report posts. A governed Document needs a source address, so these ten are now Info notes (INFO-90017 to INFO-90027, former ids DOC-00013 to DOC-00020, DOC-00026 and DOC-00030) tagged `unlinked-capture`. Their content and tier T4 are unchanged.

## Aliases

- Industry articles register

## Former ids
