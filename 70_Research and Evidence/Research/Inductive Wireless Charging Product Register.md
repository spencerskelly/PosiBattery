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
| [[Delta MOOVair Wireless Charging Series]] | 1-30 kW | 1 kW: 24/36/48 V (to 41.7/27.7/20.8 A); 30 kW voltage not stated | 1 kW: 0-20 mm, 20 mm; 30 kW: 20-150 mm | 92-93% (1 kW); 95% (30 kW) | IP65 (1 kW); FCC CE MET | T1/T2 |
| [[Wiferion etaLINK 3000 Wireless Charging System]] | 3 kW (6 / 9 kW in series) | not stated (etaTRAY 24-48 V, 60-180 A) | not stated | not stated | IP65; CAN | T1 |
| [[Wiferion CW1000 Wireless Charging System]] | 1 kW (1,250 W continuous) | 15, 24, 32, 48, 60 V; up to 42 A | 5-30 mm; +/-30 mm | up to 93% | IP65/IP68 stationary, IP54 mobile | T1 |
| [[WiBotic 1kW Wireless Charging System]] | 1 kW (earlier 150-300 W) | 0-60 V; 0-35 A | not stated | not stated | 110 V supply | T2 |
| [[Xnergy Wireless Charging Series]] | PH 1.5 kW; BE 3-9 kW (T4) | not stated | wider gap, no figure | not stated | FCC UL CE (PH) | T2/T4 |
| [[Daihen D-Broad Wireless Charging System]] | up to 4 kW (T4) | not stated | up to 40 mm (T4) | not stated | WiTricity magnetic resonance | T2/T4 |

### Names found only in a supplier-copied list (T4), not yet verified

- B&PLUS (600 W), CaPow Genesis (500 W, in-motion charging), Buzzard by Multipowr (1.5-8.4 kW). Source: <https://www.agvnetwork.com/wireless-charging-for-agv-and-autonomous-mobile-robots>.

### Observations

- Only two products reach forklift-class power with a stated voltage: NexSys AIR (80 V, 120 A, 10 kW; 80 V x 120 A = 9.6 kW) and Delta's 30 kW model (voltage not stated). The rest are 0.3-4 kW AGV and AMR products, mostly 24-60 V.
- NexSys AIR is described on the maker page as for AGVs; the manual lists 24-80 V and lead-acid and lithium chemistries. No source found shows it fitted to a counterbalance or reach truck.
- Hands-free voltage correction: the earlier note that wireless voltages stop at 48 V was wrong; the NexSys AIR manual lists an 80 V converter.
- AGV Network states most AGV suppliers use non-resonant coupling (efficient, distance sensitive) and that its data was copied from vendors (T4).
- Efficiency is stated at 92-95% by Delta and Wiferion; EnerSys' manual gives none, and the vault's brochure row says 94% or more.
- No wireless standard for industrial trucks was found; Delta's 1 kW sheet lists UL/EN 62368-1, FCC and EN 62311.

## Aliases

- Inductive Product Register

## Former ids
