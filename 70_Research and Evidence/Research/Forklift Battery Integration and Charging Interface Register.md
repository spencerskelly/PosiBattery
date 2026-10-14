---
type: Info
subtype:
id: INFO-00912
uid: 20261014092011796skellyspencer
status: Draft
tags:
  - research
  - register
  - forklift
describes:
  - "[[Vehicle Energy Interface Design]]"
---

# Forklift Battery Integration and Charging Interface Register

## Definition

Per-truck register of how the battery is installed (drop-in cavity or vehicle-integrated) and how the truck is charged (on-vehicle inlet, battery-direct connection, or onboard charger), with the evidence for each value.

## Notes

- **Terms (proposed 2026-10-14):** battery installation = [[Drop-In Battery Cavity]] or [[Vehicle-Integrated Battery]]; charge access = [[Truck Charging Port]] (alias On-Vehicle Charge Inlet), [[Battery-Direct Charge Connection]], or [[Battery Onboard Charger]] (charger built into the truck, mains inlet on the vehicle). A truck can offer more than one.
- **Rule:** a value is recorded only where a page or sheet states it. Where a source is silent the cell says "not found"; no industry default is assumed. Lead-acid trucks are very likely drop-in, but that is not recorded without a source.
- **Result (recounted 2026-10-14, counting cells that link a term):** of 46 rows, 28 have a battery-installation value and 11 have a charge-access value. Most remaining gaps need the OEM spec sheet (IB-201).

| Truck note | Battery installation | Evidence | Charge access | Evidence | Gap |
|---|---|---|---|---|---|
| Cat 2EPC5000-2EP6500 | not found | - | not found | - | 12 years old item; Cat brochures needed (R57) |
| Cat EP14-20 (Europe) | not found (lead-acid or Li option) | - | not found | - | Cat EAME brochure |
| Cat EP25-55 80 V (Europe) | lead-acid default; Li "LIBAT" factory-fit or conversion kit | V; swap-in form inferred from the kit, not stated | charging hatch and socket standard with Li: [[Truck Charging Port]] | V | lead-acid charging not stated |
| Cat Electric Lift Trucks (North America) | not found | - | not found | - | no battery data on the series page |
| Crown FC 5700 | [[Drop-In Battery Cavity]] (lift-out or side removal standard; Li optional) | V (spec sheet); brochure says "Integrated Lithium-Ion System", no swapping (C246) | not found (seat-deck connector options, purpose not stated) | - | charge path |
| Crown RC 5700 | [[Drop-In Battery Cavity]] (DIN compartments B-E, rollers standard) | V | charging not described; 320 SBE battery connector standard | V connector; charge path inferred battery-direct, not linked | how charged and changed |
| Crown SC | [[Drop-In Battery Cavity]] (side extraction, top access) | V | [[Truck Charging Port]] (optional QuickCharge seat-deck connectors) | V (option) | standard charge path |
| Crown RR-RD 5700 | [[Drop-In Battery Cavity]] (RD: both-side removal, rollers) | V for RD; RR not covered | not found | - | RR sheet; charging |
| Crown RM-RMD 6000 | [[Drop-In Battery Cavity]] (either-side removal, rollers) | V | not found | - | charging |
| Doosan Bobcat 7-Series Plus | [[Quick-Change Battery Compartment]] (so drop-in) | V (existing) | not found | - |  |
| Doosan Bobcat NXE | not found (Li option, "low-profile battery") | - | not found | - | NXE brochure |
| Hangcha A | [[Drop-In Battery Cavity]] with optional side change | V | not specified; charger paired with each Li model | - | connector |
| Hangcha XC | [[Quick-Change Battery Compartment]] (roller packs) | V (existing) | charger optional | V | port |
| Heli A3 | not found | - | built-in charger for a 230 V socket: [[Battery Onboard Charger]] | V (existing) | battery installation |
| Heli G | G2 "universal battery system" (unclear) | - | not found | - | Heli G brochure |
| Hyster J1.5-3.0UT(L) | [[Drop-In Battery Cavity]] (lead-acid top extraction; Li box under seat, removable) | V | [[Battery-Direct Charge Connection]] (Li battery-side port); optional side inlet [[Truck Charging Port]] | V | lead-acid charging path |
| Komatsu FB | not found | - | not found | - | Komatsu FB brochure |
| Linde 1293 (E20BHP/E25BHP) | [[Drop-In Battery Cavity]] (vertical battery change) | V (T2 dealer-hosted catalog; line to confirm); Li stated by trade article | not found | - | Linde spec sheet |
| Linde 6-8 t electric | not found | - | not found | - |  |
| Linde E Series | [[Drop-In Battery Cavity]] (vertical and lateral change, 180 degree door) | V (datasheet and Ei item) | not found | - | charging |
| Linde Ei | [[Vehicle-Integrated Battery]] (permanently integrated) | V | optional onboard charger on a standard outlet: [[Battery Onboard Charger]] | V | charge port |
| STILL RX 20 | [[Drop-In Battery Cavity]] (lateral change) | V | [[Battery Onboard Charger]] (optional) | V | charge inlet |
| Mitsubishi FB 3-wheel | not found | - | not found | - | 2012 item has no battery data |
| Mitsubishi FBC | not found | - | not found | - |  |
| Mitsubishi FBC20Q-40Q | not found ("easy battery service access") | - | not found | - | voltage |
| Mitsubishi FBCS | [[Drop-In Battery Cavity]] (compartment dims, roller height) | V (spec fields) | not found | - | connector |
| Mitsubishi FB25-55N (Americas) | not found | - | not found | - |  |
| Raymond 4000 | [[Drop-In Battery Cavity]] (optional right-hand rollout) | V | not found | - | Li charging |
| Raymond 7000 | not found (36 V per 7700 page) | - | not found | - | 7500 page silent |
| Raymond Orderpickers | [[Drop-In Battery Cavity]] (standardized compartment widths) | V (5500 page) | not found | - |  |
| Raymond 8000 (8210) | not found (24 V battery, Li compatible) | - | Delta-Q on-board charger: [[Battery Onboard Charger]] | V (development host, caution) | battery installation |
| STILL RX 60 | [[Drop-In Battery Cavity]] (lateral change) | V (T3 dealer page) | not found | - |  |
| STILL EXH-SF | [[Drop-In Battery Cavity]] (lateral change) | V | optional built-in onboard charger: [[Battery Onboard Charger]] | V | connector |
| Toyota 3-Wheel | [[Drop-In Battery Cavity]] (optional roll-out or slide-out) | V (option) | not found (optional fast charge) | - | charge inlet |
| Toyota 7FBCU35-55 | [[Drop-In Battery Cavity]] (optional slide-out) | V (option; T2 dealer-hosted sheet) | not found | - | charging; lithium |
| Hyster J2.2-3.5XN | [[Drop-In Battery Cavity]] (optional side extraction) | V (option; T3 dealer page) | not found | - | charging; lithium |
| Hyster J2.5-3.0XNL | [[Vehicle-Integrated Battery]] ("integrated", no exchange) | V (T2 dealer-hosted sheet) | [[Truck Charging Port]] (external charge socket) | V (T2) | OEM sheet |
| Yale ERC045-070VG | [[Drop-In Battery Cavity]] (side extraction with rollers, lift-out) | V | not found (battery connectors by option: SB350, SBE320, 2x EBC320 for fast charge) | connector options V; inlet location not stated | where the charger plugs in |
| Toyota Traigo48 | [[Quick-Change Battery Compartment]]; Traigo_i [[Vehicle-Integrated Battery]] | V (existing) | Traigo_i charging port in counterweight: [[Truck Charging Port]] | V (existing) |  |
| UniCarriers MX2 and MXL | [[Drop-In Battery Cavity]] (separate 80 V 775 Ah battery, weights, connector cable) | V (spec fields, T3) | not found; Triathlon Li is a factory option | - | Triathlon integration |
| UniCarriers SCX N2 | not found (older SCX sheet: rollers and side gates) | - | not found | - | N2 sheet |
| Yale ERC050-060VGL | [[Vehicle-Integrated Battery]] | V | optional onboard charger; off-board chargers approved: [[Battery Onboard Charger]] | V (existing) | charge port |
| Yale ERC080VHL | [[Vehicle-Integrated Battery]] | V | not found | - | charge port |
| Jungheinrich ETV C16/C20 | [[Drop-In Battery Cavity]] (sideways change) | V, T3 single listing | not found | - | OEM sheet; charging |
| Mitsubishi FG/FD, UniCarriers Nomad | not applicable (internal combustion) | - | not applicable | - |  |
| Rocla ART/AWT | not found | - | not found | - | AGV data sheets |

## Traceability

- Describes [[Vehicle Energy Interface Design]]; each row's evidence is on the truck note and its Document note.

## Aliases

## Former ids
