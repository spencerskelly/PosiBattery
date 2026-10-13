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

**Result in one line.** Product data sheets, brochures and manuals are already reflected in product notes. The 16 estimation papers are fully reviewed in [[SOC and Health Estimation Literature Review]]. The Fleetman size chart and care instructions, the two Reddit threads and the ITW GSE pages are already in [[Generic Reference Values]] or the [[Demand Evidence Source Register]]; the first pass of this screening matched on file names and wrongly listed them as gaps (corrected 2026-10-13 by content search). The only true gaps are the LinkedIn market and marketing articles, which carry no evidential weight, and the Flux Power charger guide.

### 1. Covered (no action)

| Group | Files | Evidence of coverage |
|---|---|---|
| Monitor, charger and battery product literature | trak collect data sheet and brochure, Wi-iQ, eGO!core, Easy Monitor leaflet, BatteryRX, Battview, PowerTrac SP / 3 / DT3, iQ Mini, Delta-Q IC650, Selectiva 4.0, ProCore Edge (IOMM, IG, spec sheet, Solo), Lester Summit, Revolution series, GNB overview, eGSE catalog, RC 5700 / FC 5700, Quantum Outdoor | 2 to 62 product notes name each product family; trak collect spec table matches the data sheet value for value |
| Estimation papers | 16 distinct papers | [[SOC and Health Estimation Literature Review]], conflicts C158 to C171 |
| Truck, OEM and safety documents | Hyster, Toyota Assist, Raymond, pedestrian camera, CEIL manual, MSDS and SDS, operator training | referenced by one or more notes |
| Duplicates | 11 groups | kept visible per `Downloads/README_Downloads.md` |

### 2. Referenced by content, not by file name (no action)

| File | Where it is already in the vault |
|---|---|
| `forklift-battery-sizes.pdf` (Fleetman selection chart) | [[Generic Reference Values]], section "Lead-acid forklift battery size, capacity and weight", all 42 rows. Re-check done here: every row has kWh = Ah x cells x 1.94 V per cell, Ah = (plates - 1) / 2 x Ah per plate from the model code, and voltage = 2 x cells; no row breaks these rules |
| `forklift-battery-care-instructions.pdf`, `battery-care-instructions.pdf` (Fleetman) | [[Generic Reference Values]] (discharge floor, recharge trigger, cycle definition) |
| Reddit r/Warehouseworkers boiling-battery thread; Reddit r/forkliftmechanics battery-position thread | [[Demand Evidence Source Register]] and [[Demand Evidence Conflict Log]]. The second thread shows the flair `5pencer5kelly`, so it appears to be the project owner's own post; confirm it is flagged as non-independent there |
| ITW GSE pages (Power Share, EcoGate) | [[Demand Evidence Source Register]] |
| Stryten "Power Shift" interview | [[Demand Evidence Source Register]] |

### 2b. Real gaps

| File | What it is | Recommended action |
|---|---|---|
| `Lithium-Ion Forklift Battery Chargers_ Best Practices Guide.pdf` (Flux Power, 2026-07-14) | Vendor blog: charger must match battery voltage and current; maintenance routine. No specifications | Source-register entry only, vendor content (T3) |
| 24 LinkedIn articles | BlitzNXT-branded vendor content and templated market-report blurbs; no vault note mentions BlitzNXT | Section 3 |

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

### 5. Open question for the vault owner

- Should the LinkedIn articles be added to the Demand Evidence Source Register as vendor content (T3) with the caveats in section 3, or left out entirely?

## Aliases

- Downloads screening
