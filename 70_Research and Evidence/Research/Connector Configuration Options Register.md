---
type: Info
subtype: research
id: INFO-00925
uid: 20261014105410670skellyspencer
status: Draft
tags:
  - research-note
  - connector
describedBy:
  - "[[Document - Anderson IBC 320 Summary Sheet (SS-IBC320, 2025-07)]]"
  - "[[Document - Anderson IBC 320 Data Sheet (DS-IBC320 Rev 1)]]"
  - "[[Document - Anderson A Series Euro Connector Data Sheet]]"
  - "[[Document - Anderson SB175 Data Sheet]]"
  - "[[Document - Anderson Double Stack DIN Truck Charger Brackets Page (retrieved 2026-10-14)]]"
  - "[[Document - Mouser Anderson Double Stack Manual Assist Brackets Item]]"
  - "[[Document - TVH Forklift Battery Connectors Page (retrieved 2026-10-14)]]"
  - "[[Document - Crown Parts Shop Battery Connectors Category (retrieved 2026-10-14)]]"
  - "[[Document - Yale ERC045-070VG Specification Sheet]]"
---

# Connector Configuration Options Register

## Definition

The ways each industrial battery connector family can be configured when ordered or serviced, and which connector a truck ships with as standard versus as an option. Configuration is chosen per battery, truck and charger, so the standard fit of a truck can differ from what is installed.

## Notes

- Values are as stated by the source; blank means not stated. Anderson sheets are T1 read second-hand; TVH is T3. Family-level specifications are in [[Industrial Battery Connector Specification Register]]; terms in [[Industrial Battery Connector Glossary and Differences]].
- Conflict: naming of the Anderson Euro families is unresolved (C253).

### Configuration axes by connector family

| Axis | IBC 320 | A Series (A80/A160/A320) | SB 175 | SB 350 / SBE / SBX |
|---|---|---|---|---|
| Housing form | Plug, receptacle, panel-mount receptacle | Male (code 4) or female (code 5) | Genderless; black keyless or colour keyed | Genderless; colour keyed |
| Size / rating | 320 class only found; 250-320 A (EN1175), 290-460 A (UL) by wire size | 80, 160, 320 class; A320 about 450 A UL on 120 mm2 | 280 A UL wire-to-wire on 1/0 | SB350 450 A on 4/0, 500 A on 350 mcm (C251); SBE/SBX per-pole current conflict (C250) |
| Power contact size | 50, 70, 95, 120 mm2 or 1/0-4/0 AWG | 10-35, 16-50, 50-120 mm2 | 10 AWG to 1/0 (1/0, 1, 2, 4, 6 AWG contacts) | 4/0 to 350 mcm (SB350) |
| Contact style | Modular tool-less cartridges | Crimp, per-contact tooling | Wire or busbar | Wire or busbar |
| Voltage identification | Keying 24, 36, 48, 72, 80, 96 V (DIN VDE 0623-589) | Keys 24-96 V; grey, green, yellow | Colour keys yellow, orange, red, gray, blue; no voltage mapping stated | Colour keys; per-truck use conflicts (C252) |
| Wet / dry / universal coding | Seven pins: grey wet, green dry, yellow universal, blue Type II dry, red Type II wet | Grey wet, green dry, yellow universal (vehicle side only) | | |
| Auxiliary / signal | Air Tube, 4 Aux (purple), 10 Aux (orange, gold-plated) | Config codes A-F, lower and upper aux | 3-pole gray kit 902 | SBE/SBX up to 8 aux; air tubes |
| Handle / latch | Latching (plug only, 45 lb defeat) or non-latching | Low or high profile | Handles 995G1, 995G3 | Handles, latches, manual release brackets |
| Sealing | IP23; IP68 with seal kit | IP23 | Boots IP64 (test pending); dust cover | |
| Sensing | NTC contact temperature kit | | | |
| Mounting | Panel-mount option; cable-diameter kits | Latch plates, battery brackets | Release brackets 924G1, 923G1; reducing bushings | Side bracket kits |
| Packaging | | Kit or bulk | Housings and contacts sold separately | Contacts and housings sold separately (Crown shop) |

### Fast-charge and parallel add-ons

- [[Anderson Double Stack Manual Assist Brackets]] (SKU 994G6 for A320/E320; SBE320/SBX350 versions) hold two connector sets in parallel for higher charging current. No rating stated.
- Yale option BAFBC (fast charge) uses dual cabling ending in two female EBC320 connectors (A32503-0009) and needs a site survey ([[Dual-Cable and Parallel Charging Configuration]]).

### Truck standard versus optional connector

| Truck | Standard as stated | Option as stated | Source |
|---|---|---|---|
| [[Yale ERC045-070VG Electric Forklifts]] | BCSSBC: gray SB350 (36 V, 6320G1), blue SB350 (48 V, 6321G1), black SBE320 (80 V, E6363G1) | BAFBC fast charge: dual cabling to two female EBC320; Li-ion and TPPL with Yale Power Key | [[Document - Yale ERC045-070VG Specification Sheet]] |
| [[Toyota 7FBCU35-55 Electric Pneumatic Forklifts]] | Gray SB350 | Optional battery connector colours | Vault note |
| [[Toyota 3-Wheel Electric Forklift]] | | Optional fast charge | Vault note |
| [[Crown RC 5700 Series]] | 320 SBE | | Vault note |
| [[Crown FC 5700 Series]] | SB350 | Seat-deck connector options | Vault note |
| [[Crown SC Series]] | SB350 | QuickCharge, 1-2 seat-deck connectors | Vault note |
| [[Hyster J1.5-3.0UT(L)]] | Lithium battery-side port DIN 160/320 A | Side inlet | Vault note |
| [[UniCarriers SCX N2 Stand-Up Counterbalanced Forklifts]] | SB-350 gray (older sheet) | | Vault note |

### Reading across the tables

- The standard connector is fixed by order code per truck; the table shows the connectors that were stated, not all possible fits.
- Any connector on a battery must match the charger and truck by family, size and key; mismatch (for example same-colour SBE320 with SBX350) prevents mating.
- Parts-level options (contacts, housings, handles, boots) are sold separately per Crown's shop and TVH.

## Aliases

- Connector Options

## Former ids
