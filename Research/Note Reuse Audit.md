---
type: Info
subtype:
id: INFO-00203
uid: 20261003093855193skellyspencer
status: Draft
tags:
  - review
  - conventions
  - quality
describes:
  - "[[Battery-Connected Product]]"
---

# Note Reuse Audit

## Definition

Record of where notes covered the same thing, what was merged or renamed, and the rules that keep one note per thing.

## Notes

- **Rules (owner, 2026-10-03):** (1) one note per thing: one organization note per owner, one product note per product, one metric note per metric; (2) products link to the owner by relationship, and the owner is never a folder; (3) check titles and aliases before creating a note; (4) when notes are merged, the survivor keeps its id and the retired ids go in Former ids; (5) notes that might be the same but are unproven stay separate and are cross-referenced.
- **Folder rule:** `Products/<Type>/<Category>/` where the type is Batteries, Chargers, Forklifts, Battery Accessories, Charger Accessories, Vehicle Accessories, Fleet Software and Platforms, Fuel Cell Power Units or Ground Support Equipment, and the category folders sit under the type (for example `Products/Batteries/Lithium-Ion Batteries`).

| Area | What overlapped | Decision |
|---|---|---|
| Folders | Crown vs Crown Equipment, East Penn vs East Penn Manufacturing, Stryten vs Stryten Energy, Exide vs Exide Technologies, Fronius vs Fronius International were separate folders for the same owner, and owners had folders under both Battery Products and Forklifts | Folders are now product type then category; no owner folders; the owner is the makes, offers or other relationship on the product note |
| Metrics | Certifications, Size and Mass, Voltage, Operating Temperature, Warranty and Price, Power Consumption and Ingress Protection were separate notes for monitors, chargers and batteries | Merged into 7 shared metric notes (original ids in Former ids); the other metric notes renamed 'Metric - ...' with the class kept as a tag |
| Maps | Truck Device Feature Map repeated part of the Function Map and Design Map | Merged; Function Map and Design Map now cover every function and design |
| Comparisons | Battery Monitoring Performance Comparison overlapped Monitor Comparison Matrix | Merged into the matrix; original kept as a section and its id in Former ids |
| Aliases | 'GNB Industrial Power' was an alias of Exide Technologies and also its own note; 'Triathlon' was an alias of two notes; two notes listed an alias twice | Aliases removed or made specific; duplicates dropped |
| Organization notes | Round 5 offered-with lists repeated products that now have notes | Relabeled as superseded and kept as written for items not yet modeled; owners link to products by relationship |
| Kept separate until evidence | Hyster Tracker Telemetry vs Hyster Battery Tracker (C60); Yale Vision Telemetry vs Yale Battery Vision (C60); Triathlon USA vs Triathlon Battery Solutions (C62); eGO!c vs eGO!core (C23); WBID vs WBID Pro; Lester Summit II 650 W vs Delta-Q IC650 (C58) | Not merged because no source says they are the same thing; each pair is cross-referenced in the conflicts register |
| Boundary kept | Alert on Abnormal Condition (battery) vs Alert Operator of Hazards (truck); Log Battery Events and Usage vs Report Truck Telemetry | Different objects of the behavior; kept separate with the boundary stated in each note |

## Aliases

- Reuse audit

## Former ids
