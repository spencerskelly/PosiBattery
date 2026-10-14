---
type: Info
subtype: research
id: INFO-00947
uid: 20261014150724116skellyspencer
status: Draft
tags:
  - research-note
  - traceability
describes:
  - "[[Battery-Connected Product]]"
---

# Unlinked Product Triage Register

## Definition

Review of the 108 concrete products under `10_Products` that performed no function on 2026-10-14, with the reason each stays unlinked or the link made. Created 2026-10-14 (priority 5).

## Notes

- **Outcome:** 15 products linked to existing functions where their note's source states the behavior; 93 remain unlinked. No function or need was created.
- **Linked now (function reasoning is on each product note):**
  - [[Banner Traction Bull Electrolyte Circulation Pump Module]]: [[Circulate Electrolyte]]
  - [[Midac Air-Tech Air-Mixing System]]: [[Circulate Electrolyte]]
  - [[Exide Opus Display]]: [[Inform Users of Battery Condition]]
  - [[Anderson Double Stack Manual Assist Brackets]]: [[Connect Battery to Charger or Vehicle]]
  - [[Exide Element HF Charger]]: [[Charge Battery]]
  - [[ITW GSE DC Charger]]: [[Charge Battery]]
  - [[EnerSys NexSys COMpact Charger]]: [[Charge Battery]]
  - [[Linde Lithium-Ion Charger (9, 17 and 30 kW)]]: [[Charge Battery]], [[Charge Lithium-Ion Battery]]
  - [[Triathlon Lithium-Ion Charger for UniCarriers]]: [[Charge Battery]], [[Charge Lithium-Ion Battery]]
  - [[Stryten AGM220 Onboard Charger]]: [[Charge Battery]], [[Indicate Charger Status Locally]]
  - [[Cat Intelligent Speed and Movement Reduction]]: [[Adapt Speed to Load and Lift Height]]
  - [[Raymond Extreme Environment Protection]]: [[Operate in Wet or Dusty Conditions]]
  - [[Cat Panel Cabin Options]]: [[Shelter Operator from Weather]]
  - [[Raymond Right-Hand Battery Rollout]]: [[Change Battery Quickly]]
  - [[Raymond Secondary Control Handle]]: [[Support Operator View and Positioning]]
- **Still unlinked by reason:**
- **Vehicle listings: models state properties; vehicle behavior sits on the option and accessory notes (33):** [[Cat EP14-20 Electric Counterbalance Forklifts]], [[Cat EP25-55 80 V Electric Counterbalance Forklifts]], [[Cat Electric Lift Trucks (North America Series List)]], [[Charlatte Belt Loaders]], [[Charlatte CBT350 AC Tow Tractor]], [[Charlatte CPB35E Pushback Tractor]], [[Charlatte T137-V3]], [[Crown RM-RMD 6000 Series]], [[Crown SC Series]], [[Hyster J2.2-3.5XN Electric Forklifts]], [[Hyster J2.5-3.0XNL Integrated Lithium-Ion Forklifts]], [[Jungheinrich ETV C16 and C20]], [[Linde 1293 Series (E20BHP and E25BHP)]], [[Linde Ei Series]], [[Linde P250 Electric Baggage Tractor]], [[Mitsubishi EDR Reach Trucks (Americas Listing)]], [[Mitsubishi FB25-55N Electric Pneumatic Forklifts (Americas Listing)]], [[Mitsubishi FBC20Q-FBC40Q Electric Cushion Forklifts]], [[Mitsubishi FG and FD Internal Combustion Forklifts (Americas Listing)]], [[Mitsubishi Warehouse Trucks (Americas Listing)]], [[Oshkosh AeroTech B80E Electric Baggage Tractor]], [[Oshkosh AeroTech Commander 30i Cargo Loader]], [[Oshkosh AeroTech Pushback B350E and B650E]], [[Oshkosh AeroTech Ranger 15E Cargo Loader]], [[Raymond Orderpickers]], [[Rocla ART Automated Reach Truck]], [[Rocla AWT Automated Counterbalance Truck]], [[STILL RX 20 Electric Forklift]], [[TLD NBL-E Belt Loader]], [[TLD RBL Electric Regional Belt Loader]], [[Toyota 7FBCU35-55 Electric Pneumatic Forklifts]], [[UniCarriers Nomad AF30-AF50 LP and Dual-Fuel Forklifts]], [[Yale ERC045-070VG Electric Forklifts]]
- **Batteries: listings state properties, which the vault keeps as metrics, not functions (30):** [[Amaron Brute Hi-Life Battery]], [[BSL Lithium Forklift Battery]], [[Banner Traction Bull Bloc PzF]], [[Banner Traction Bull PzS]], [[Banner Traction Bull PzV Gel]], [[Crown V-Force Lead-Acid Battery]], [[Deka MaintenanceSaver Battery]], [[EnerSys IRONCLAD Battery]], [[Exide Element VRLA Battery]], [[Exide MARATHON Classic Battery]], [[Flux Power S-Series Battery]], [[Godrej Lithium-Ion Forklift Battery]], [[Green Cubes Forklift Battery Retrofit Kit]], [[HOPPECKE trak power Lithium Battery]], [[Leoch PzS Traction Battery]], [[Linde 90 V Lithium-Ion Battery]], [[Midac FORCEblock Battery]], [[Midac MBS Traction Battery]], [[Midac MDLblock Battery]], [[Midac MHE Battery]], [[Midac MLM Battery]], [[Midac MLMx Battery]], [[Midac PzS Traction Battery]], [[Redway Lithium Forklift Batteries]], [[Sonnenschein AF Battery]], [[Sonnenschein EPzV Battery]], [[Sonnenschein GF-V Battery]], [[Sonnenschein GF-Y Battery]], [[Stryten M-Series AGM210 Battery]], [[Triathlon Lithium-Ion Battery for UniCarriers]]
- **Named only: the source does not say what it does (15):** [[Amaron AFS System]], [[Amaron Aqua Filling Plug]], [[Amaron DIY Rx]], [[Banner Traction Bull Battery Controller]], [[Crown Service Request App]], [[Deka Ready Power BDI]], [[Exide BattID]], [[HOPPECKE trak collect premium]], [[HOPPECKE trak monitor 4.0]], [[HOPPECKE trak systemizer powercube]], [[Midac Battery Management (MBM)]], [[Midac MB2 Battery Brain]], [[Philadelphia Scientific iBOS]], [[Raymond Power Source Integrated]], [[Raymond iWAREHOUSE GATEWAY]]
- **Hardware or convenience items with no modeled function (11):** [[Crown V-HFM3 Charger Stand]], [[Flux Power GSE3 Truck Adapter]], [[Linde Smartphone Holder]], [[PosiCharge DIY Fast Charge Kit]], [[Purkeys Trailer Auxiliary Power System]], [[Raymond Accessory Bar]], [[Raymond Auto-Locking Pallet Clamp]], [[Raymond Intelliguide Wire Guidance]], [[Raymond Large Storage Tote]], [[Raymond Slope Sensing]], [[UniCarriers In-Cab Accessories]]
- **Third-party BMS: marketing features that match no vault function (2):** [[Nuvation Energy G5 BMS]], [[REC 2Q BMS]]
- **Owner-named variants of PosiCharge BMID: no per-variant source (the parent BMID carries the functions) (2):** [[PosiCharge BMID 1]], [[PosiCharge BMID 3]]

### Findings

- **Most gaps are source gaps, not modeling gaps.** Batteries and vehicle listings state properties; the named-only items have a name and no description (IB-181, IB-184, IB-185, IB-188, IB-189, IB-190, IB-193).
- **Vehicles carry no function by design.** A truck's behavior is recorded on its option and accessory notes, so listing notes stay unlinked. Adding a vehicle-level function such as moving and lifting loads would link every truck but trace to no customer need.
- **General functions were used where the source is general.** Charge Battery, Inform Users of Battery Condition and Support Operator View and Positioning have no need links of their own; the links raise function coverage but not need coverage.
- **To close more:** a page naming what each named-only item does (see the backlog items above), or an owner decision on a vehicle-level function.

## Aliases

## Former ids
