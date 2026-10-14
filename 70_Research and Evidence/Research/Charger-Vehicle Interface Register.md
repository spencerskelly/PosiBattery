---
type: Info
subtype: research
id: INFO-00921
uid: 20261014103229601skellyspencer
status: Draft
tags:
  - research-note
  - connector
  - hands-free
describedBy:
  - "[[Document - Anderson Material Handling Connector Catalog (AG-MHCS)]]"
  - "[[Document - Anderson Euro Battery Connector Page (retrieved 2026-10-14)]]"
  - "[[Document - Electronic Design EN 1175 Connector Article]]"
  - "[[Document - Vahle Charging Contacts Catalog (Cat 10a)]]"
  - "[[Document - Wiferion Products Page (retrieved 2026-10-14)]]"
  - "[[Document - Conductix-Wampfler Enduro Plus Charging Contacts Page (retrieved 2026-10-14)]]"
describes:
  - "[[Vehicle Energy Interface Design]]"
---

# Charger-Vehicle Interface Register

## Definition

Register of how energy gets from charger to vehicle or battery: two axes, where the charger connects (truck inlet, battery connector, onboard charger) and how the connection is made (by hand, automatic contact, inductive, automated connector, or automated battery swap), with the connector families and ratings found.

## Notes

- **Axes:** where = [[Truck Charging Port]], [[Battery-Direct Charge Connection]], [[Battery Onboard Charger]]; how = [[Manual Plug-In Charging]], [[Conductive Auto-Contact Charging]], [[Inductive Wireless Charging]], [[Automated Connector Charging]], [[Automated Battery Swap]]. A truck-level register is [[Forklift Battery Integration and Charging Interface Register]].
- **Rule:** values are as stated by the source; blanks mean not stated. Maker marketing claims are not independently verified.

### Plug-in connector families

| Family | Maker | Current | Voltage | Aux contacts | Standard / note | Evidence |
|---|---|---|---|---|---|---|
| DIN A | Anderson | up to 350 A | 600 V | not stated | DIN | AG-MHCS catalog (T1) |
| DIN E | Anderson | 80-320 A nominal | 150 V (IEC) | 4 on 80/160/320 | key colours grey wet, green dry, yellow universal | AG-MHCS catalog (T1) |
| SB | Anderson | up to 450 A | 600 V (UL) | up to 20 | 10,000 cycles; voltage coding 12-120 V | AG-MHCS catalog (T1) |
| SBS | Anderson | up to 110 A | 600 V (UL) | 5 to 20 | 10,000 cycles | AG-MHCS catalog (T1) |
| SBE / SBX | Anderson | up to 550 A | 600 V (UL) | up to 20 | 10,000 cycles; SBE320 and SBX350 used by Crown and Yale | AG-MHCS catalog (T1) |
| EBC 80/160/320 | Anderson | up to 450 A | not stated | up to 4 | EN 1175:2020, DIN 43589-1; legacy | EBC page (T1) |
| IBC | Anderson | not stated | not stated | up to 10 | EN 1175; IP68 kit, latching handle | Anderson pages, Electronic Design (T1/T2) |
| REMA Euro DIN 80/160/320 | REMA | 320 A seen | not stated | not stated | DIN 43589, EN 1175-1; pin colours | Akkusys listing (T2) |
| EBC320 DIN female x2 (Yale fast charge) | Anderson | not stated | not stated | not stated | Yale option BAFBC | Yale sheet (T1) |

### Hands-free methods

| Method | Product | Rating | Tolerance | Cycles / other | Evidence |
|---|---|---|---|---|---|
| Conductive auto-contact | [[Vahle Charging Contacts]] | 50-600 A, up to 60 VDC (custom 230/400 V) | large, no figure | pilot contacts | Vahle catalog (T1) |
| Conductive auto-contact | [[Conductix-Wampfler Enduro+ Charging Contacts]] | 100-600 A, 12-60 V DC | +/-15 mm X and Y | optional CAN pilots; dry interior | Conductix page (T1) |
| Automated connector | [[Staubli QCC Quick Charging Connection]] | up to 1,500 V DC, 1,440 A peak, 670 A continuous | angular and positional, no figure | over 100,000 cycles (trade item); IP55; SAE J3105/3 | Staubli page (T1), trade item (T2) |
| Inductive | [[Wiferion etaLINK 3000 Wireless Charging System]] | 3 kW (6 kW series) | not stated | CAN, IP65 | Wiferion page (T1) |
| Inductive | [[EnerSys NexSys AIR Wireless Charger]] | 7-10 kW; 24/36/48/80 V (80 V: 120 A) | 20-50 mm gap, +/-20 mm | efficiency 94% or more (brochure); none in manual | EnerSys manual (T1) |
| Conductive auto-contact | [[Raymond Courier AutoCharge System]] | station 120 V in, 150 A max | two vehicle plates; drive-thru | opportunity, partial, full modes | Raymond sell sheet (T1) |
| Conductive auto-contact | [[Grenzebach AGV Contact Charging Station]] | 48 V DC, 80 A, contacts to 200 A | not stated | 93% efficiency | Grenzebach data sheet (T1) |
| Inductive | [[Delta MOOVair Wireless Charging Series]] | 1 kW (24/36/48 V, 41.7/27.7/20.8 A); 30 kW | 1 kW: 0-20 mm gap, 20 mm lateral; 30 kW: 20-150 mm gap | 93-95% efficiency; CAN | Delta data sheet and article (T1/T2) |
| Battery swap | [[Concentric PowerHIVE]] | about 2 min per swap | n/a | 250,000+ swaps | trade item (T2) |
| Battery swap | [[HOPPECKE AGV Battery Exchange System]] | n/a | n/a | 18 batteries, 13 chargers, 6 trucks | HOPPECKE story (T1) |

### Observations

- The contact products found publish standard ratings up to 60 V DC, while many counterbalance trucks in the truck register run 80 V; no source found shows 80 V or 96 V automatic contact charging for forklifts (IB-206). Raymond's AutoCharge and Grenzebach are 48 V-class AGV/automated-truck systems; Vahle offers custom 230/400 V.
- Wireless: EnerSys' NexSys AIR manual lists an 80 V, 10 kW converter (120 A); Delta 1 kW, Wiferion CW1000 and WiBotic stop at 48-60 V; Delta 30 kW and etaLINK give no voltage. Product comparison: [[Inductive Wireless Charging Product Register]].
- Standards: SAE J3105 (pin-and-socket, pantograph, rail) targets transit buses at 250-1000 V DC; EN 50696:2021 covers automated connection devices up to 1,500 V DC and does not mention industrial trucks. Neither is shown to apply to 24-96 V truck batteries, so no hands-free standard for forklifts has been found (IB-206).
- EN 1175 Annex A covers connectors for energy sources; no charging-specific connector standard was named by the article (IB-206).
- Jungheinrich's case study shows a site removing battery changing stations in favour of on-the-spot lithium charging, the opposite direction from [[Automated Battery Swap]].

## Aliases

## Former ids
