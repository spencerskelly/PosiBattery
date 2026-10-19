---
type: Info
subtype:
id: INFO-90064
uid: 20261018200000100skellyspencer
status: Draft
tags:
  - research
  - market-sizing
  - installed-base
describes:
  - "[[Battery-Connected Product]]"
describedBy:
  - "[[Document - ITA United States Factory Shipments Table (2000 to 2025, 2026 Directory)]]"
  - "[[Document - Modern Materials Handling End-of-Life Management Have a Plan (2018-12-10)]]"
  - "[[Document - CHG-MERIDIAN Material Handling Equipment Useful Life and Lease Terms]]"
---

# US Installed Base Model

## Definition

A stock-from-flow estimate of United States industrial trucks in service at the end of 2025: add up the ITA United States factory shipments of the last L years, for each class group. It exists because no public source gives a US truck count by class (C359). It is a model on public inputs, not a count, and every assumption is listed below. Built 2026-10-18.

## Notes

### Bottom line

1. **About 1.9 million trucks at a base life of 8 years, with a range of 1.2 to 2.7 million** for lives of 5 to 12 years (derived). Of the base case, about 0.67 million are electric riders (Classes 1 and 2), 0.59 million motorized hand trucks (Class 3) and 0.62 million internal combustion.
2. **The class mix hardly changes with the assumed life:** electric rider 35 to 36%, Class 3 31 to 32%, internal combustion 32 to 34% of the stock (derived).
3. **The model reproduces the one old public count.** The same method gives 1.09 million at the end of 2009 for a 7-year life and 1.22 million for 8 years, against 'over 1 million' in the 2009 NIST paper ([[Document - NIST PerMIS 2009 Forklift Safety White Paper]]). The model does not prove either figure; it shows they are mutually consistent for a life of about 7 to 8 years.
4. **The vault's earlier 2 to 3.5 million is too high.** It used 200,000 to 350,000 sales a year; the upper figure matches North American retail orders (348,000 in 2021, covering US, Canada, Mexico and government), not US factory shipments, which peaked at 298,059 in 2023 and averaged 229,860 in 2016 to 2025 ([[Fleet Energy and Cost Evidence Register]]; C359).

### Inputs

| Input | Value | Basis | Source |
|---|---|---|---|
| Annual shipments by class group, 2000 to 2025 | e.g. 2025: 88,461 electric rider; 79,081 Class 3; 63,855 internal combustion | ITA United States factory shipments | [[Document - ITA United States Factory Shipments Table (2000 to 2025, 2026 Directory)]] [P] |
| Operating hours a year | 1,848 | CARB survey-based assumption for affected California forklifts | [[Document - CARB Standardized Regulatory Impact Assessment, Appendix B-2 (zero-emission forklifts)]] [P] |
| Useful life in hours | Counterbalanced 10,000 to 20,000, replacement target about 15,000; reach 10,000 to 15,000; pallet trucks 8,000 to 12,000 | A lessor's planning ranges | [[Document - CHG-MERIDIAN Material Handling Equipment Useful Life and Lease Terms]] [V] |
| Useful life in years | 5 to 7 (Toyota), 8 to 10 (UniCarriers, intensive users); IC 8 and electric 10 chosen by some customers | Trade press quoting two truck makers | [[Document - Modern Materials Handling End-of-Life Management Have a Plan (2018-12-10)]] [S] |
| Hours converted to years at 1,848 a year | 10,000 h = 5.4 y; 15,000 h = 8.1 y; 20,000 h = 10.8 y | Derived | the two rows above |
| **Life used** | **Low 5, base 8, high 10 years, 12 as a stretch case** | Chosen to span the rows above | |

### Result (stock at end of 2025, trucks; derived)

| Life L (years) | Total | Electric rider (Cl. 1+2) | Motorized hand (Cl. 3) | Internal combustion |
|---|---|---|---|---|
| 5 | 1,228,669 | 445,264 | 388,964 | 394,441 |
| 8 (base) | 1,879,138 | 672,136 | 586,541 | 620,461 |
| 10 | 2,298,601 | 813,925 | 715,717 | 768,959 |
| 12 | 2,682,026 | 936,510 | 825,442 | 920,074 |

For other lives: 6 years 1,424,993; 7 years 1,647,442; 9 years 2,091,140; 11 years 2,497,047 (total). Check at end of 2009: 5 years 782,833; 6 years 948,255; 7 years 1,088,742; 8 years 1,220,350; 10 years 1,556,251.

### What the model leaves out

- **Imports and exports.** The ITA file does not say whether exports are counted or whether imported trucks are excluded. US factory shipments fell 22% from 2023 to 2025 while WITS Americas stayed flat (C358); if imports replaced them, this model understates the US stock.
- **Hours-based retirement.** Trucks retire at hours, not at an age; high-use trucks retire sooner and light-use trucks last longer. A single life is a simplification; the 60 to 70% lease share (one trade-press statement) suggests many trucks leave first owners early but stay in service as used units, which the model counts once.
- **Used trucks and re-export.** Not modeled.
- **Class 3 life.** The lessor gives 8,000 to 12,000 hours for pallet trucks, shorter than the riders; the model applies one life to all classes, which overstates Class 3 stock at a given L.
- **ITA membership changes.** The ITA page warns annual figures are not strictly comparable.
- **Canada, Mexico and other regions** are not covered; there is no equivalent shipment history for them in the vault.

### How to use it

For the electric rider stock (the base for traction battery and charger demand), use 0.67 to 0.81 million (L of 8 to 10) and say it is a model. Replacement flows follow: at L of 8, about one eighth of the stock, or roughly 84,000 electric riders, retire in a year (derived), compared with 88,461 shipped in 2025. Chemistry mix, battery age and charger age are not in this model.

## Traceability

- Feeds: [[Market Definition and Scope]] section 5, [[Regional Market Size Model]].

## Aliases

- US stock model
- installed base model

## Former ids
