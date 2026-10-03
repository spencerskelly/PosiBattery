---
type: Info
subtype:
id: INFO-00202
uid: 20261003090225596skellyspencer
status: Draft
tags:
  - research
  - review
  - forklift
  - gaps
describes:
  - "[[Powered Industrial Truck]]"
  - "[[Fuel Cell Power Unit]]"
---

# ICE and Fuel Cell Feature Gap Review

## Definition

Review of features that internal combustion and fuel-cell trucks offer that battery-electric trucks may lack, each with the electric-side status and evidence.

## Notes

- **Owner request (2026-10-03):** stay with electric trucks but note features on internal combustion and fuel-cell trucks that may be missing from electric.
- **Result:** the fuel-cell advantages found are fast refueling, constant voltage, cold performance and no battery room; lithium-ion trucks close most of them by vendor claim but not refueling time. Two features run the other way (energy-source flexibility, regeneration).
- **Not yet researched:** internal combustion specific devices (engine and transmission diagnostics, fuel level and hours sensors, LPG tank monitoring, exhaust). Only the telematics standard-level difference is sourced so far. See [[Investigation Backlog]].

| Feature | Seen on | Electric-side evidence | Status | Evidence |
|---|---|---|---|---|
| Refuel in about 2 to 3 minutes | fuel cell (GenDrive, Nuvera) | Electric trucks recharge or swap batteries; Plug Power gives 15 minutes (battery change station) or 20-30 minutes per shift; lithium opportunity charging removes swaps but no truck-level minute figure was found (Jungheinrich: 50% in 40 minutes) | partly closed by lithium-ion opportunity charging; not matched in minutes | <https://www.plugpower.com/applications/material-handling/>; <https://www.plugpower.com/faq-from-potential-gendrive-customers>; [[Jungheinrich Lithium-Ion Battery]] |
| Constant voltage and power through the shift (no droop) | fuel cell (GenDrive, Nuvera) | Lead-acid droops as it depletes; makers claim consistent power for lithium-ion (Yale ERC080VHL, Hyster lithium-ion option) | closed for lithium-ion by vendor claim | <https://plugpower.com/wp-content/uploads/2014/12/GenDrive-Series-1000-Spec-Sheet.pdf>; [[Yale ERC080VHL]]; [[Hyster J1.5-3.0UT(L)]] |
| Performance at -22 F in freezers | fuel cell (GenDrive) | Batteries lose capacity in the cold; cold storage profiles and heaters exist (EnerSys cold storage profile, Green Cubes GSE heaters) but no truck-level figure was found | addressed by heaters and profiles; no equal stated temperature figure | <https://plugpower.com/wp-content/uploads/2014/12/GenDrive-Series-1000-Spec-Sheet.pdf>; [[EnerSys NexSys+ Charger]]; [[Green Cubes GSE Lithium Battery]] |
| No battery room or battery handling | fuel cell (GenDrive); lithium-ion also removes it | Lithium-ion has no gassing and no ventilated charging room (Linde Ei); fuel cell needs hydrogen storage and dispensers instead | lithium-ion matches; both swap one infrastructure for another | <https://www.plugpower.com/applications/material-handling/>; [[Linde Ei Series]] |
| Power unit tells the truck its state and remaining fuel | fuel cell (GenDrive fuel gauge, stack monitoring) | Battery side: CAN BMS to truck (Power Cellect), Wi-iQ, Truck iQ display; no single standard | present but fragmented | [[Plug Power GenDrive]]; [[Hyster Power Cellect]]; [[EnerSys Truck iQ]] |
| Remote monitoring and automated controls on the power unit | fuel cell (Nuvera PowerEdge) | Lithium-ion packs with telemetry (Flux SkyBMS, Stryten inCOMMAND); lead-acid relies on add-on monitors | present on lithium; add-on for lead-acid | <https://www.liftandaccess.com/news/hybrid-fuel-cell-forklifts-introduced>; [[Stryten M-Series Li610 Battery]] |
| Base telematics standard on the truck | internal combustion (Yale Series N ICE, Hyster A Series) | Toyota pre-installs MyInsights on its 3-wheel electric; Hyster and Yale electric standard level not stated | not shown for Hyster and Yale electric trucks | [[Hyster Tracker Telemetry]]; [[Yale Vision Telemetry]]; [[Toyota MyInsights Telematics]] |
| Energy-source flexibility on one truck (lead-acid, TPPL, lithium-ion) | electric only (Hyster Power Cellect) | Not available on internal combustion or fuel-cell trucks; a gap the other way | electric advantage | [[Hyster Power Cellect]] |
| Regenerative braking and lowering | electric only | Internal combustion and fuel-cell trucks lack it unless hybrid; Nuvera PowerEdge keeps a buffer battery | electric advantage | [[Raymond 7000 Series Reach-Fork Trucks]]; [[Toyota SEnS+ Pedestrian and Object Detection]] |

## Aliases

- Feature gap review

## Former ids
