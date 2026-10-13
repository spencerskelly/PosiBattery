---
type: Info
subtype:
id: INFO-90011
uid: 20261013140000000skellyspencer
status: Draft
tags:
  - research
  - downloads
  - screening
  - evidence-gaps
describes: []
---

# Downloads Value Screening Register

## Definition

Screening of every file in `Downloads/` (130 files, 118 distinct after removing 11 duplicate groups) for valuable data not yet in the vault, with the coverage evidence and the recommended action for each gap. Screened 2026-10-13. No Downloads file was changed.

## Notes

**Method.** Each PDF was matched to the vault by file name, title and distinctive specification values (for example the trak collect data sheet values 150 VDC, IP 69K, 340 g, 8 MB ring buffer all appear in the product note). The match is a screening test, not a line-by-line audit of every figure.

**Result in one line.** Product data sheets, brochures and manuals are already reflected in product notes. The 16 estimation papers are fully reviewed in [[SOC and Health Estimation Literature Review]]. The gaps are market and marketing articles, three forum or vendor-blog threads, and one battery-size chart.

### 1. Covered (no action)

| Group | Files | Evidence of coverage |
|---|---|---|
| Monitor, charger and battery product literature | trak collect data sheet and brochure, Wi-iQ, eGO!core, Easy Monitor leaflet, BatteryRX, Battview, PowerTrac SP / 3 / DT3, iQ Mini, Delta-Q IC650, Selectiva 4.0, ProCore Edge (IOMM, IG, spec sheet, Solo), Lester Summit, Revolution series, GNB overview, eGSE catalog, RC 5700 / FC 5700, Quantum Outdoor | 2 to 62 product notes name each product family; trak collect spec table matches the data sheet value for value |
| Estimation papers | 16 distinct papers | [[SOC and Health Estimation Literature Review]], conflicts C158 to C171 |
| Truck, OEM and safety documents | Hyster, Toyota Assist, Raymond, pedestrian camera, CEIL manual, MSDS and SDS, operator training | referenced by one or more notes |
| Duplicates | 11 groups | kept visible per `Downloads/README_Downloads.md` |

### 2. Not referenced by any vault note (gaps)

| File | What it is | Valuable data | Evidence tier | Recommended action |
|---|---|---|---|---|
| `forklift-battery-sizes.pdf` (Fleetman Consulting Inc.) | Lead-acid forklift battery selection chart: voltage, model number, Ah, kWh, steel tray dimensions L x W x H in inches, approximate weight in lb, 12 to 80 V | Reference table of standard battery sizes. Supports envelope, mass and capacity limits for retrofit electronics and the Truck Battery Compartment notes. Consistency check on the first rows: the kWh column is about 1.94 V per cell times Ah (for example 510 Ah at 12 V is listed as 5.94 kWh), so it is a rated-energy figure about 3 percent under 2.0 V per cell; confirm the basis before use | vendor chart (T2) | Ingest as a Reference Data note after verifying the kWh column; cite the file, not a URL |
| `forklift-battery-care-instructions.pdf` and `battery-care-instructions.pdf` (Fleetman) | Watering and charging instructions; recommends a filling system with indicator light; says correct charging needs accurate state-of-charge data from the truck | One qualitative statement supports the SOC-visibility need | vendor guide (T2) | Add one line to the SOC need evidence; low value otherwise |
| `Our forklift batteries ... start to boil while charging ... .pdf` (Reddit r/Warehouseworkers, about 2 months old) | Warehouse worker reports old batteries overheating, boiling and tripping charger over-temperature shutdown; fleet has a watering system fitted | Anecdotal customer voice on charge-temperature faults and maintenance neglect. Supports the Report Battery Temperature to Charger and Alert on Abnormal Condition needs | forum post, one person (T4) | Add to [[Demand Evidence Source Register]] as exported material; the register notes Reddit cannot be fetched, so this file is the only copy |
| `Safety concern about Electric forklift battery position ... .pdf` (Reddit r/forkliftmechanics, about 9 months old) | Buyer asks whether a high-mounted battery on a Toyota Core is at risk from dock-pit levelers; update says a Heli truck has the same position and that low-position batteries probably share an IC propane chassis | Anecdote on battery position and hidden damage. The page shows the user flair `5pencer5kelly`, so this appears to be the project owner's own post, not independent evidence | forum post (T4) | Record in the register with that caveat; do not count as independent demand evidence |
| ITW GSE: `GSE Charging & Energy Management for Airports.pdf`, `Scale Electric GSE Charging Without Bottlenecks.pdf` (April 2026) | Vendor pages on coordinated GSE charging with Power Share, EcoGate, DC Charger and Intelligent Power Management | Names ITW GSE products and the claim that charging bottlenecks come from system design, not fleet size. No specifications | vendor marketing (T3) | Candidate product notes under GSE charging; needs the product pages for specifications first |
| `Lithium-Ion Forklift Battery Chargers_ Best Practices Guide.pdf` (Flux Power, 2026-07-14) | Charger matching and maintenance guide | Voltage and current must match the battery specification; general practice only | vendor blog (T3) | Source-register entry only |
| `Power Shift_ 8 ways smarter batteries ... Supply Chain 24_7.pdf` | Trade-press interview with Stryten Energy (Kevin McCusker): fast charging, BESS, charge-on-the-go | Already listed by title in the Demand Evidence Source Register as "Power Shift" | trade press (T2) | none |
| 24 LinkedIn articles (`(1)` and `(3)` prefixes) | Mostly BlitzNXT-branded vendor content and generic market-report summaries | See section 3 | vendor content (T3 to T4) | Section 3 |

### 3. LinkedIn articles: what is usable

Only one of the 24 is in the Demand Evidence Source Register ("When Does a Smart Battery Become Too Smart", 684 characters of text, effectively empty). The rest are vendor content marketing and templated market-report blurbs. Quantified claims found, with the issue with each:

| Claim in article | Where | Issue |
|---|---|---|
| Lead-acid forklift battery market CAGR 5.2 percent, 2027 to 2035 | three near-identical "Lead-Acid Battery Market" articles | Three titles, one set of numbers; counts as one source, not three. No named publisher or method in the extracted text |
| Lithium-ion forklift battery market to USD 2.94 billion by 2035, CAGR 8.5 percent | "Emerging Opportunities in the Lithium-ion Forklift Battery Market" | Another article in the set gives 10.5 percent CAGR for a "commercial electric forklift battery" market; different scope, not a conflict by itself, but not comparable |
| Battery charger market growth about 5.0 percent; battery rental growth 7.2 percent | charger and rental articles | Same issue: no publisher, no base year in the text |
| Sizing example: 5K lb, 80 V sit-down truck, 5.2 h x 6.3 kWh/h = 32.8 kWh/day, divided by 0.70 end-of-life capacity = 585 Ah | "Propane to Electric" | Worked example is arithmetic only: 32.8 / 0.70 x 1000 / 80 = 585.7 Ah, which checks. The 4.85 kWh per gallon propane equivalent and the 65 percent working-time assumption are unsourced |
| Sizing formula (10 kW x 8 h x 1000) / 48 x 1.2 = about 2,000 Ah | "How to Choose a Forklift Lithium Battery" | The arithmetic gives 2,000 Ah, but a 48 V, 2,000 Ah pack is 96 kWh, which is far above any pack in this vault. A 10 kW average draw for a forklift is also high. Treat the example as illustrative only |
| 48 V LiFePO4 charges to 54 V and runs at 51.2 V nominal | "How to Choose", "Charging Best Practices" | Consistent with 16 cells x 3.2 V = 51.2 V; 16 x 3.375 V = 54 V. Matches LFP behavior; no conflict |
| Lithium battery typically 30 to 50 percent lighter than lead-acid at similar Ah | "How to Read a Nameplate" | Comparison depends on Ah vs kWh basis; unsourced |
| Lead-acid should not be discharged below 40 percent; "safely discharged to 80% DOD" for lithium | "Propane to Electric" | Unsourced; lead-acid guidance elsewhere in the vault uses 20 to 30 percent remaining |
| Passive vs active balancing, smart-battery and AGV articles | five articles | Qualitative; no figures beyond a 98 to 99 percent charge efficiency claim and a 48 V x 100 Ah = 4.8 kWh example |

**Recommendation.** Do not ingest market-size numbers as evidence. Record the articles in the Demand Evidence Source Register as vendor content (T3) so the vault shows they were seen and why they carry no weight. Their only reusable content is the common set of lithium voltage-class and Ah-range statements (24, 36, 48, 72/80 V classes), which should be taken from OEM data sheets instead.

### 4. Image-only or unreadable files

Five PDFs have almost no extractable text: `Battery_state-of-charge_observer.pdf`, `Battery-Care-Maintenance.pdf`, `SA-2014-Forklift-Battery.pdf`, `Forklift-and-Equipment-Batteries-General-Brochure-V2.pdf` and `H4-1.5-3.8t-Lithium-battery-forklift-FLH4002-EN.pdf`. Each is referenced by one vault note, so they are not unseen, but their figures were not checked here. An OCR pass is the only way to confirm nothing is missing. The observer file is the GM patent US 8,922,217, already reviewed as source 7 of the literature review, so it is the lowest priority.

### 5. Open questions for the vault owner

- Should the Fleetman size chart be ingested as a Reference Data note (envelope, mass, kWh per standard model)?
- Should the user's own Reddit post stay in the evidence register, flagged as the project owner's, or be removed from it?

## Aliases

- Downloads screening
