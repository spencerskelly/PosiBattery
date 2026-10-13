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

**Result in one line.** Product data sheets, brochures and manuals are already reflected in product notes. The 16 estimation papers are fully reviewed in [[SOC and Health Estimation Literature Review]]. The Fleetman size chart and care instructions, the two Reddit threads and the ITW GSE pages were first listed as gaps because the screen matched on file names; a content search showed the Fleetman files, the Reddit threads and the ITW product names were already in [[Generic Reference Values]] or the [[Demand Evidence Source Register]] (the ITW pages themselves had no source note). The real gaps were the 25 LinkedIn and vendor articles and the Flux Power charger guide. At the project owner's request (retain industry data, not only customer needs) they were read in full, checked where a primary source exists, and recorded in [[Industry Data Register from Downloads Articles]] with 18 source notes and conflicts C172 to C184.

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

### 2b. Gaps now closed (2026-10-13)

| File group | Where recorded |
|---|---|
| 8 Zhang 'Powering Industrial Mobility' articles | [[Industry Data Register from Downloads Articles]] and DOC-00013 to DOC-00020 |
| 5 BlitzNXT articles | same, DOC-00021 to DOC-00025 |
| ENEROC propane-to-electric sizing | same, DOC-00026 |
| Flux Power charger guide | same, DOC-00027; also linked from [[Flux Power]] |
| 2 ITW GSE pages | same, DOC-00028 and DOC-00029 |
| 11 market-report posts | same, DOC-00030 (one note, eleven rows) |

### 3. LinkedIn articles: outcome

The first version of this section recommended leaving the market and marketing articles out. That recommendation is withdrawn: the project goal is to retain industry data for stakeholder review, so the articles are kept, with their tier and every failed check visible. Findings are in [[Industry Data Register from Downloads Articles]]: market-size figures are templated and unusable as evidence (C172 to C176); BlitzNXT product claims conflict with each other and with the Fleetman chart (C178 to C182); the BloombergNEF price was verified; the OTTO and Green Cubes claims were verified only with qualifications (C184).

### 4. Image-only or unreadable files

Five PDFs have almost no extractable text: `Battery_state-of-charge_observer.pdf`, `Battery-Care-Maintenance.pdf`, `SA-2014-Forklift-Battery.pdf`, `Forklift-and-Equipment-Batteries-General-Brochure-V2.pdf` and `H4-1.5-3.8t-Lithium-battery-forklift-FLH4002-EN.pdf`. Each is referenced by one vault note, so they are not unseen, but their figures were not checked here. An OCR pass is the only way to confirm nothing is missing. The observer file is the GM patent US 8,922,217, already reviewed as source 7 of the literature review, so it is the lowest priority.

### 5. Open items

- The five image-only PDFs (section 4) still need OCR.
- Questions on Organization and product notes for BlitzNXT, ENEROC, OTTO Motors and ITW GSE products are in section 7 of [[Industry Data Register from Downloads Articles]].

## Aliases

- Downloads screening
