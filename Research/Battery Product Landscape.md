---
type: Info
subtype:
id: INFO-00070
uid: 20261002161409690skellyspencer
status: Draft
tags:
  - battery-landscape
  - evidence-register
describes:
  - "[[Battery-Connected Product]]"
  - "[[Battery Management System]]"
  - "[[Battery Monitoring and Identification Device]]"
  - "[[Battery Connector Assembly]]"
  - "[[Electrolyte Circulation System]]"
  - "[[Battery Watering System]]"
  - "[[Battery Thermal Management Device]]"
  - "[[Battery Protection and Disconnect Unit]]"
  - "[[Industrial Battery Charger]]"
  - "[[Battery Telematics and Connectivity Device]]"
  - "[[Battery-Installed Device]]"
---

# Battery Product Landscape

## Definition

Scope, method, evidence tiers and backlog for the first-pass survey of product categories connected to batteries.

## Notes

- **Purpose:** first-pass, broad survey of product categories connected to batteries, industrial forklift (MHE) and ground support equipment (GSE) first, before narrowing to competitors of PosiCharge BMID products and then widening again.
- **Method and limits:** web search only, on 2026-10-02. Evidence below comes from search-result excerpts, not from full datasheet or manual reads. No vendor datasheet, standard or manual has been opened. A datasheet-level pass is pending for any category before it is relied on.
- **Scope axes (working, not governed):** locus (battery-integrated, battery-mounted, vehicle-mounted, charger-side, site infrastructure, cloud); chemistry (flooded lead-acid, sealed lead-acid, lithium-ion, other); voltage class (about 24 to 96 V for MHE per connector and charger sources; higher classes for EV); application (forklift, GSE, other).
- **Evidence tiers and conventions:** see [[Landscape Evidence and Modeling Conventions]].
- **Categories found (hypotheses until reviewed):** [[Battery Management System]], [[Battery Monitoring and Identification Device]], [[Battery Connector Assembly]], [[Electrolyte Circulation System]], [[Battery Watering System]], [[Battery Thermal Management Device]], [[Battery Protection and Disconnect Unit]], [[Industrial Battery Charger]], [[Battery Telematics and Connectivity Device]]. Root: [[Battery-Connected Product]].
- **Observed charge-start modes (PosiCharge only):** ID device (BMID), CAN from a lithium BMS, voltage-only default. See [[Industrial Battery Charger]].
- **Not yet researched:** battery changers and extractors, wash stations, ventilation and hydrogen detection, battery rooms, cooling devices, balancing hardware, on-board chargers, DC-DC converters, lead-acid desulfation or equalization hardware, GSE-specific equipment, and non-industrial applications.
- **Relationship to the ChatGPT seed branch:** the 11 products, 5 families and market-reference note from `chatgpt/battery-installed-reference-foundation` were brought into this structure on 2026-10-02, keeping their `uid` values and OBJ ids. The market-reference note moved from INFO-00001 to INFO-00072 to follow the vault rule of highest id plus one; INFO-00001 is recorded under its former ids. The seed branch's navigation files and architecture-alignment note were not carried over. Competitor comparison: [[BMID Competitor Landscape]].
- **Round 2 2026-10-02:** monitoring-device survey extended to 19 more products; reusable functions and design characteristics now have their own notes in `Product Functions` and `Product Designs`, mapped by evidence level. See [[Function Map]], [[Design Map]], [[Monitor Comparison Matrix]]. General-purpose monitors (marine, RV, solar, automotive) are deferred.
- **Round 3 2026-10-02:** added citations (a web page per link) to every function and design mapping, 6 more products (Power Designers PowerTrac Monitor, Exide Motion+ EasyMonitor, ACT BATTview, eGO!plus, eGO!core, eGO!gateway), 2 functions and 8 designs, and re-verified seed claims for PosiGuard and eGO!pro.
- **Round 4 2026-10-02:** started the `Organizations` folder: 11 organization notes and a relationship register for industrial battery makers, truck OEMs and white-label or rebrand evidence. Candidate makers not yet researched are listed in the register.
- **Round 5 2026-10-02:** researched what battery makers and truck OEMs offer with their batteries; added Stryten Energy, Midac, Triathlon Battery Solutions, Jungheinrich and Sunlight Group, an offered-with list on every organization note, and the matrix [[Products Offered or Promoted with Industrial Batteries]]. Wi-iQ re-mapped as identifying the battery to EnerSys chargers.
- **Round 8 2026-10-02:** catalog review; 38 battery lines and four battery families added; charger and battery features mapped; see [[Catalog Review 2026-10-02]] and [[Offerings by Organization]].
- **Round 9 2026-10-02:** note standard and exemplars, specs added from three documents, Stryten lineup completed, multi-link explanations, decisions Q11 and Q12 recorded. See [[Note Standard (Example)]].
- **Round 10 2026-10-02:** performance metric dictionary (42 metrics in the Performance Metrics folder) and three comparison matrices; the documents mentioned for this round had not arrived, so no document-based values were added. See [[Monitor Comparison Matrix]], [[Charger Comparison Matrix]], [[Battery Comparison Matrix]].
- **Round 11 2026-10-02:** eight datasheets absorbed as Document notes in `Source Documents`; differences from earlier sources logged (C43 to C51); charger and monitor specs, 7 functions and 1 design added; metrics CM16 to CM18 added; [[Document Wishlist]] and [[Unidentified Products Review]] created.
- **Round 12 2026-10-02:** link audit and rebuilt Document Wishlist (owner flagged four bad links and home-page links); corrections: Deka Dominator is gel (C53), PowerForce is not Deka-only (C54); Stryten brochures give lead-acid battery to charger pairings; Delta-Q IC650, Exide Motion+ Premium Charger and the Sunlight eGO! PRO page added; conflicts C52 to C59. See [[Link Audit]].
- **Round 13 2026-10-03:** forklift survey: seven ITA classes, ten truck makers, 21 model families, and the batteries, chargers, telematics and programs sold with them; first truck-maker supplier relationship (Triathlon to UniCarriers); Document Wishlist reordered. See [[Forklift Offerings Matrix]].
- **Round 14 2026-10-03:** truck-side devices modeled (17 functions, 16 designs, 15 products, 6 truck metrics); Q13 and Q14 resolved; ICE and fuel-cell feature gap review; Truck Device Comparison Matrix and Truck Device Feature Map; conflicts C66 to C68.
- **Round 15 2026-10-03:** product folders regrouped by type then category under `Products`; metric, map and comparison notes de-duplicated; accessory categories and 14 seeded accessory and software notes; Document Wishlist in the owner's column format. See [[Note Reuse Audit]].
- **Round 16 2026-10-03:** GSE: 4 vehicle categories, 15 vehicle families from 8 makers, 3 aircraft-proximity systems plus 2 telematics systems, 3 PosiCharge GSE chargers, 3 functions, 2 designs, conflicts C69 to C72. See [[Ground Support Equipment]].
- **Round 17 2026-10-03:** accessories sweep (20 accessory notes, 7 organizations), function and design levels (19 general functions, 4 goals, 15 general designs), conflicts C73 to C75, Q16, wishlist URL column now direct files only. See [[Function and Design Levels]].
- **Round 18 2026-10-03:** Q16 resolved (functions `dependsOn` designs, 28 dependencies in [[Function Design Dependencies]]); naming rule and `check-names.py`; truck OEM accessories: 23 notes for Crown, Toyota, Raymond and Hyster; new function and design classes; conflict C76.
- **Round 19 2026-10-03:** unformatted analysis notes repaired and filed (see [[Note Reuse Audit]]); 14 new PosiCharge product and accessory notes; conflicts C77 to C79; wishlist links repaired.
- **Round 20 2026-10-03:** uploaded documents read and absorbed; conflicts C66, C77 to C79 resolved or narrowed, C80 to C83 raised; [[External Context and Provenance]] and [[Project Objectives (Draft)]] added.
- **Round 21 2026-10-03:** owner scope decisions recorded (neutral reference, global, top makers plus a sample); [[Coverage Plan]] with a generated coverage ledger added; [[Project Objectives (Draft)]] revised; conflict C84.
- **Round 22 2026-10-03:** truck OEM accessory sweep for Linde, Jungheinrich and Mitsubishi Logisnext (17 notes, 5 functions, 2 designs, a new goal and general function, 4 dependencies); per-type minimums and tier handling added to the [[Coverage Plan]]; conflicts C85 to C87.
- **Round 23 2026-10-03:** truck makers sweep: STILL, Cat, Hangcha, Heli, Doosan Bobcat, Komatsu (21 accessory notes, 13 truck notes, 3 battery notes, 1 charger, CATL); conflicts C88 to C90; C84 updated.
- **Round 24 2026-10-03:** Mitsubishi Logisnext focus: group split into three entity notes, 4 truck notes, 5 option notes, EnerSys partnership, brand coverage table in the [[Coverage Plan]]; conflicts C91 to C93.
- **Round 25 2026-10-03:** feature capture for the unlinked products (50 products linked; 56 of 321 still unlinked); see [[Feature Capture Log]].
- **Round 26 2026-10-03:** sources found for unlinked products; 48 of 323 still without a feature link ([[Feature Capture Log]]).
- **Round 27 2026-10-03:** feature vocabulary and dependency review applied; 52 of 323 products still without a feature link ([[Feature Capture Log]]).
- **Round 28 2026-10-03:** dependency strength column and check script; battery maker gaps: 5 organizations and 9 battery notes; conflicts C94 and C95 ([[Coverage Plan]]).

## Aliases

- Battery landscape survey


## Former ids
