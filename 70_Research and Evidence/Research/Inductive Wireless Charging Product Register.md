---
type: Info
subtype: research
id: INFO-00931
uid: 20261014110037015skellyspencer
status: Draft
tags:
  - research-note
  - wireless
  - hands-free
describedBy:
  - "[[Document - EnerSys NexSys AIR Product Page (retrieved 2026-10-14)]]"
  - "[[Document - EnerSys NexSys AIR Owner's Manual (0624)]]"
  - "[[Document - Wiferion CW1000 Page (retrieved 2026-10-14)]]"
  - "[[Document - AGV Network Wireless Charging Suppliers Article]]"
  - "[[Document - WiBotic 1kW Wireless Charging Article (2024-04-30)]]"
  - "[[Document - WiBotic Larger AMR Battery Charging Article]]"
  - "[[Document - Xnergy PH Series Certification Release (2026-06-09)]]"
  - "[[Document - MHL News Daihen D-Broad Item]]"
  - "[[Document - Delta MOOVair01 48V Data Sheet (Rev 3.1)]]"
  - "[[Document - Delta 30 kW Wireless Charging Article (2024-03-21)]]"
  - "[[Document - Wiferion Products Page (retrieved 2026-10-14)]]"
  - "[[Document - ACT Resonant Link Wireless Release (2025-02-10)]]"
  - "[[Document - ACT News Page (retrieved 2026-10-14)]]"
  - "[[Document - TMHNA Investment in ACT Release (2025-10-22)]]"
  - "[[Document - MHL News Resonant Link Wireless Lift Truck Charger (2023-04-19)]]"
  - "[[Document - Electrify News Resonant Link Article (2024-03-30)]]"
  - "[[Document - Resonant Link MODEX 2024 Release (2024-03-11)]]"
  - "[[Document - Auto Innovations Delta Neumaier Inductive Charging Article]]"
  - "[[Document - Delta EMEA Wireless Charging Systems Page (retrieved 2026-10-14)]]"
  - "[[Document - Warehouse News Wiferion etaLINK 12000 Article (2020-02-17)]]"
  - "[[Document - EV Infrastructure News Electreon InductEV Article (2026-03-10)]]"
---

# Inductive Wireless Charging Product Register

## Definition

Inductive charging products found for industrial vehicles (forklifts, AGVs, AMRs) with the ratings each maker states, the design they realise ([[Inductive Wireless Charging]]), and the gaps between sources.

## Notes

- Values as stated by the source; blank means not stated. Only products with a source in the vault are listed; names found only in a supplier-copied list (T4) are in the last section.
- Context: [[Charger-Vehicle Interface Register]].

### Products

| Product | Power | Voltage / current | Air gap; tolerance | Efficiency | Protection / other | Evidence |
|---|---|---|---|---|---|---|
| [[EnerSys NexSys AIR Wireless Charger]] | 7-10 kW | 24 V 7 kW 250 A; 36 V 10 kW 250 A; 48 V 10 kW 200 A; 80 V 10 kW 120 A | 20-50 mm; +/-20 mm | not stated | IP23 / IP54; FOD; CE UKCA MET FCC | T1 manual |
| [[Delta MOOVair Wireless Charging Series]] - MOOVair 01 | 1 kW | 24/36/48 V; 41.7/27.7/20.8 A | 0-20 mm; up to 20 mm | 92-93% | IP65; FCC CE MET | T1 |
| [[Delta MOOVair Wireless Charging Series]] - MOOVair 03 | 3.3 kW | 24 V 132 A; 48 V 66 A | 10-30 mm; not stated | over 92% | IP65/IP67 | T1 |
| [[Delta MOOVair Wireless Charging Series]] - MOOVair 10 | 10 kW | 36 V 280 A; 48 V 200 A | up to 185 mm; not stated | over 92% | IP21/IP69; deployed on Linde E16 (article) | T1/T2 |
| [[Delta MOOVair Wireless Charging Series]] - MOOVair 30 | 30 kW | 100 V (72-120 V) 300 A, lithium-ion | 105-155 mm; +/-50 mm | over 95% | IP21/IP69; deployed on Linde P180 (article) | T1/T2 |
| [[Wiferion etaLINK 3000 Wireless Charging System]] | 3 kW (6 / 9 kW in series) | not stated (etaTRAY 24-48 V, 60-180 A) | not stated | not stated | IP65; CAN | T1 |
| [[Wiferion CW1000 Wireless Charging System]] | 1 kW (1,250 W continuous) | 15, 24, 32, 48, 60 V; up to 42 A | 5-30 mm; +/-30 mm | up to 93% | IP65/IP68 stationary, IP54 mobile | T1 |
| [[WiBotic 1kW Wireless Charging System]] | 1 kW (earlier 150-300 W) | 0-60 V; 0-35 A | not stated | not stated | 110 V supply | T2 |
| [[Xnergy Wireless Charging Series]] | PH 1.5 kW; BE 3-9 kW (T4) | not stated | wider gap, no figure | not stated | FCC UL CE (PH) | T2/T4 |
| [[Daihen D-Broad Wireless Charging System]] | up to 4 kW (T4) | not stated | up to 40 mm (T4) | not stated | WiTricity magnetic resonance | T2/T4 |
| [[Resonant Link Wireless Lift Truck Charger]] | 19.2 kW (ACT integrating) | 400 A; voltage not stated (about 48 V by arithmetic); 91% at 48 V per ACT | 10 in gap; +/-6 in | 90% (2023); 91% at 48 V (2025) | FOD; SAE J2954 and UL 2750 claimed by ACT | T1/T2 |
| [[Wiferion etaLINK 12000 Wireless Charging System]] | 12 kW | not stated | not stated | 93% | CAN | T2 |

### Names found only in a supplier-copied list (T4), not yet verified

- B&PLUS (600 W), CaPow Genesis (500 W, in-motion charging), Buzzard by Multipowr (1.5-8.4 kW). Source: <https://www.agvnetwork.com/wireless-charging-for-agv-and-autonomous-mobile-robots>.

### Observations

- Products at forklift-class power: NexSys AIR (80 V, 120 A, 10 kW; 80 V x 120 A = 9.6 kW), Delta MOOVair 30 (80 V stated in a deployment article) and MOOVair 10 (10 kW), Resonant Link (19.2 kW, 400 A, voltage not stated), Wiferion etaLINK 12000 (12 kW, voltage not stated). The rest are 0.3-4 kW AGV and AMR products, mostly 24-60 V.
- NexSys AIR is described on the maker page as for AGVs; the manual lists 24-80 V and lead-acid and lithium chemistries. No source found shows it fitted to a counterbalance or reach truck.
- Hands-free voltage correction: the earlier note that wireless voltages stop at 48 V was wrong; the NexSys AIR manual lists an 80 V converter.
- AGV Network states most AGV suppliers use non-resonant coupling (efficient, distance sensitive) and that its data was copied from vendors (T4).
- Efficiency is stated at 92-95% by Delta and Wiferion; EnerSys' manual gives none, and the vault's brochure row says 94% or more.
- No wireless standard for industrial trucks was found; Delta's 1 kW sheet lists UL/EN 62368-1, FCC and EN 62311.

### Announced or recently acquired (2025-2026)

- ACT integrating Resonant Link (announced 2025-02-10); no product name, price or launch date found; neither the ACT news page (no 2026 items) nor the Toyota investment release (2025-10-22) mentions it again. Who acquired Resonant Link is not stated in the release (C261).
- Delta: 3.3 kW and 10 kW models were "expected later" in a 2024 article; MOOVair 10 now appears in a 2026 deployment article.
- Out of scope: Electreon announced acquiring InductEV on 2026-03-10 (heavy-duty transit and freight, no kW stated; industrial trucks not named). Source: <https://www.evinfrastructurenews.com/ev-technology/electreon-acquires-us-based-inductev-to-expand-wireless-ev-charging> (T2).
- Not found: any announced OEM-factory wireless option from Toyota, Raymond, Crown, Hyster, Yale or Linde Material Handling.

## Aliases

- Inductive Product Register

## Former ids
