---
type: Info
subtype:
id: INFO-00963
uid: 20261017175000000skellyspencer
status: Draft
tags:
  - research
  - regulation
  - fire-code
  - lithium
  - charging-area
  - insurer
  - north-america
  - forklift
describes:
  - "[[Industrial Battery Charger]]"
describedBy:
  - "[[Document - California Fire Code 2025 Section 309 Powered Industrial Trucks (gocodebook, retrieved 2026-10-17)]]"
  - "[[Document - California Fire Code 2025 Section 322 Powered Micromobility Devices (gocodebook, retrieved 2026-10-17)]]"
  - "[[Document - If P&C Hazard Info Sheet Lithium-Ion Stacker Trucks (2024-06)]]"
  - "[[Document - HDI Risk Engineering Guideline Battery Charging (2016)]]"
  - "[[Document - OSHA Instruction STD 1-11.4 Battery Charging Stations for Fork Lifts (1978)]]"
  - "[[Document - 1910.178 Powered Industrial Trucks Course Slides (ETTA OSH Division, undated)]]"
  - "[[Document - SafetyFolio OSHA Requirements for Battery Charging Areas in Small Warehouses (2026)]]"
  - "[[Document - MHI Blog Navigating Third-Party Safety Standards for Lithium Batteries in Lift Trucks (2024-10-08)]]"
  - "[[Document - Energy-Storage.news NFPA 855 2026 Edition Updates (2026-04-29)]]"
  - "[[Document - Meyer Fire Whats New in NFPA 855 2026 Edition (2025-09-17)]]"
  - "[[Document - ANSI Webstore NFPA 505-2024 Listing (retrieved 2026-10-17)]]"
  - "[[Document - ANSI Webstore UL 583 Ed 11-2022 Listing (retrieved 2026-10-17)]]"
  - "[[Document - ANSI Webstore UL 1564 Ed 5-2024 Listing (retrieved 2026-10-17)]]"
  - "[[Document - ANSI Webstore UL 3100 Ed 1-2018 Listing (retrieved 2026-10-17)]]"
  - "[[Document - Electrical Contractor Magazine Whats Classified as an Electric Vehicle (2015-05-06)]]"
supportedBy:
  - "[[Document - SafetyFolio OSHA Requirements for Battery Charging Areas in Small Warehouses (2026)]]"
---

# Lithium Forklift Charging Area Fire and Safety Code Register

## Definition

Register of the fire, electrical and safety rules, standards and insurer guidance that bear on where and how lithium-ion (and other) forklift batteries may be charged, what each source actually says, where sources disagree, and what that could mean for chargers. It checks the 2026-10-04 backlog row on fire-code and AHJ treatment of lithium charging areas ([[Knowledge Base Backlog]]). Disagreements are numbered C314 to C322 in [[Battery Product Landscape Conflicts and Open Questions]]; new directions are IB-273 to IB-283 in [[Investigation Backlog]].

## Notes

- **Reading rule:** every source was read through a summarizing fetch tool (second-hand). Code text came from a third-party reproduction (gocodebook), not the official publication. Two primary sources could not be read: the NFPA 855 page and the ICC Digital Codes IFC 2024 chapter 3 (fetch permission for both was not answered in time, so they were not retrieved). "Analyst reasoning" marks a conclusion no source states. Status is as of 2026-10-17.
- **Scope of this pass:** only the fire-code row of the 2026-10-04 backlog list was researched. The other unverified rows (EU battery passport, cyber rules, tariffs, cellular sunsets, AMR charging, WMS integration) are untouched.
- **Chemistry caution:** almost every rule found for "battery charging areas" predates lithium forklift batteries and is written around gassing lead-acid batteries. Where a source does not name a chemistry, the register says so and does not assume lithium is covered or exempt.

### Bottom line (analyst summary)

1. **The backlog premise is not supported as written.** The row says NFPA 855 treatment of lithium charging areas can block or delay deployments and may justify charger safety features. No source read states that NFPA 855 applies to forklift battery charging, and its scope text is unread (C314, IB-273). The adopted code text read for forklift charging (2025 California Fire Code section 309) says nothing about lithium. No source read documents a real site that was delayed or blocked.
2. **What does exist is insurer guidance specific to lithium trucks.** One insurer sheet (If P&C, 2024-06) asks for 10 m separation or EI60 fire separation with detection and sprinklers, chargers that cut power on a fire alarm or ventilation failure, a truck BMS that talks to the charger, and the truck maker's own charger ([[Document - If P&C Hazard Info Sheet Lithium-Ion Stacker Trucks (2024-06)]]). This is a loss-prevention sheet from one insurer, not a code, and its US relevance is unknown. It is the most charger-relevant evidence found.
3. **The adopted charging-area rules read are chemistry-agnostic and gas-oriented.** California section 309 asks for approved chargers, 3 ft clear of combustible storage, no charging in areas open to the public, ventilation against flammable gas, and a rated extinguisher within 20 ft. Whether an authority applies the ventilation clause to a lithium-only room is unknown (C318).
4. **OSHA is also lead-acid-worded.** 29 CFR 1910.178(g) is described by secondary sources in terms of gassing batteries and electrolyte; a 1978 directive treats "charging-only" areas separately; a 2026 secondary article says no lithium-specific OSHA standard exists as of mid-2025 (C319). The standard text itself is unread.
5. **Section 322 is a trap.** A search hit for "IFC 2024 322.4 Battery charging areas" is the powered micromobility section (e-bikes, scooters); its aspirating-detection and 18 in spacing rules do not govern forklift charging (C322, [[Document - California Fire Code 2025 Section 322 Powered Micromobility Devices (gocodebook, retrieved 2026-10-17)]]).
6. **Standards editions are slippery.** UL 1564 (chargers) has a 5th edition dated 2024-02-13 although a 2024 panelist said UL no longer maintains it (C316); UL 583 (electric trucks) is listed as an 11th edition 2022 with a 2025 publication date and no stated lithium coverage (C317).
7. **A vault need is exposed.** [[Charge Without a Ventilated Battery Room]] rests on vendors saying lithium charging releases no gas; the insurer sheet and the code text both still ask for ventilation in a charging area (C318). The need stays a hypothesis; its text is not edited.

### Check of the 2026-10-04 backlog statements

| Backlog statement | Result | Basis |
|---|---|---|
| NFPA 855 (2026 edition) treatment of lithium charging areas may block or delay deployments | Not supported: no source ties NFPA 855 to forklift charging; scope text unread; no blocked site found (C314) | [[Document - Energy-Storage.news NFPA 855 2026 Edition Updates (2026-04-29)]]; [[Document - Meyer Fire Whats New in NFPA 855 2026 Edition (2025-09-17)]]; both silent on forklifts |
| Site approval may justify charger safety features | Partly supported by one insurer sheet (interlocks, BMS link); unsupported by any code read | [[Document - If P&C Hazard Info Sheet Lithium-Ion Stacker Trucks (2024-06)]]; [[Document - California Fire Code 2025 Section 309 Powered Industrial Trucks (gocodebook, retrieved 2026-10-17)]] |
| NFPA 855 2026 edition is the relevant edition and applies from 2026 | Edition exists and was published ahead of schedule per one source; adoption is local and many places enforce earlier editions per the other (C315) | [[Document - Meyer Fire Whats New in NFPA 855 2026 Edition (2025-09-17)]]; [[Document - Energy-Storage.news NFPA 855 2026 Edition Updates (2026-04-29)]] |

### Code and guidance map

| Source | Kind | Edition or date read | Forklift charging content found | Names lithium? | Doc |
|---|---|---|---|---|---|
| California Fire Code section 309 | Adopted state code (effective 2026-01-01 per the page) | 2025 | Approved chargers; 3 ft from combustibles; not in public areas; ventilation vs flammable gas; extinguisher within 20 ft | No | [[Document - California Fire Code 2025 Section 309 Powered Industrial Trucks (gocodebook, retrieved 2026-10-17)]] |
| California Fire Code section 322 | Adopted state code | 2025 | Powered micromobility only; not forklifts | Yes (micromobility) | [[Document - California Fire Code 2025 Section 322 Powered Micromobility Devices (gocodebook, retrieved 2026-10-17)]] |
| IFC 2024 section 309 | Model code | 2024 | Not read (ICC page unreadable) | Unknown | IB-274 |
| NFPA 505 | Fire safety standard for powered industrial trucks | 2024 | Listing only: electric and ICE trucks, areas of use, recharging, extinguishers | Not in listing | [[Document - ANSI Webstore NFPA 505-2024 Listing (retrieved 2026-10-17)]] |
| NFPA 855 | Stationary energy storage standard | 2026 | Silent on forklifts and mobile equipment in both articles | n/a | [[Document - Energy-Storage.news NFPA 855 2026 Edition Updates (2026-04-29)]]; [[Document - Meyer Fire Whats New in NFPA 855 2026 Edition (2025-09-17)]] |
| 29 CFR 1910.178(g) | Federal rule | Text unread | Designated areas, ventilation for gassing, protect chargers, battery handling, no smoking (secondary) | No | [[Document - 1910.178 Powered Industrial Trucks Course Slides (ETTA OSH Division, undated)]]; [[Document - SafetyFolio OSHA Requirements for Battery Charging Areas in Small Warehouses (2026)]] |
| OSHA STD 1-11.4 | Enforcement directive | 1978-10-30 | Charging-only areas judged under (g)(1) and (g)(8) to (g)(12), not (g)(2) | No | [[Document - OSHA Instruction STD 1-11.4 Battery Charging Stations for Fork Lifts (1978)]] |
| UL 1564 | Listing standard, industrial battery chargers | Ed. 5, 2024-02-13 | Scope: chargers up to 600 V for industrial storage batteries for motive equipment | Not stated | [[Document - ANSI Webstore UL 1564 Ed 5-2024 Listing (retrieved 2026-10-17)]] |
| UL 583 | Listing standard, electric battery-powered industrial trucks | Ed. 11-2022, listed 2025-08-07 | Fire, shock and explosion risk of trucks and their power sources | Not stated | [[Document - ANSI Webstore UL 583 Ed 11-2022 Listing (retrieved 2026-10-17)]] |
| UL 3100 | Outline for AGVs | Ed. 1-2018 (historical; Ed. 2-2020 revises it) | Covers the charging device and lead-acid or lithium-ion batteries of AGVs | Yes | [[Document - ANSI Webstore UL 3100 Ed 1-2018 Listing (retrieved 2026-10-17)]] |
| NEC Article 625 | Electrical code | Edition not stated (article dated 2015) | Industrial trucks are not "electric vehicles" for Article 625 | n/a | [[Document - Electrical Contractor Magazine Whats Classified as an Electric Vehicle (2015-05-06)]] |
| If P&C hazard sheet | Insurer guidance | 2024-06 | Lithium stacker truck charging siting, detection, interlocks, BMS link | Yes | [[Document - If P&C Hazard Info Sheet Lithium-Ion Stacker Trucks (2024-06)]] |
| HDI guideline | Insurer guidance | 2016 | Charging room wall, ventilation, clearance, detection (lead-acid) | No | [[Document - HDI Risk Engineering Guideline Battery Charging (2016)]] |
| UL 2580 | Lithium battery listing | Not read | Described as the "umbrella" scheme for lithium forklift batteries by one panelist | Yes | [[Document - MHI Blog Navigating Third-Party Safety Standards for Lithium Batteries in Lift Trucks (2024-10-08)]] |

### Distances and separations by source (C321)

The numbers differ because they answer different questions; none is a general rule.

| Source | Value | What it separates |
|---|---|---|
| California Fire Code 309.3 | 3 ft | Combustible storage from chargers |
| HDI 2016 | 2.50 m (or a tall non-combustible wall); 1 m battery to charger; 90-minute wall to adjacent areas | Charging points from combustibles; hydrogen ignition; room from neighbors |
| If P&C 2024-06 | 10 m; or EI60 separation when attached | Li-ion charging area from buildings and storage |

### Implications for chargers (analyst reasoning, hypotheses only)

- **FH1:** insurers, more than codes, may be what shapes lithium charging-area layout. One sheet; no US insurer read. Test: IB-278.
- **FH2:** an external interlock on a charger (stop on site fire alarm or ventilation fault) would help a site meet the If P&C expectations. No charger product in the vault states a fire-alarm input; [[Start and Stop Charge from an External Control]] (Fronius only) does not say what its control is (C275). Candidate requirement REQ-00076.
- **FH3:** BMS-to-charger communication is already marketed by five charger makers ([[Charge Under BMS Control]]), so REQ-00077 is a market baseline rather than a gap. Whether an insurer or authority checks for it is unknown.
- **FH4:** a charger that states its listing standard and edition (REQ-00078) could shorten an approval conversation. This is reasoning only; the vault has [[Metric - Certifications and Standards]] but no source says approvals turn on it. One panelist says OSHA expects UL certification of warehouse chargers ([[Document - MHI Blog Navigating Third-Party Safety Standards for Lithium Batteries in Lift Trucks (2024-10-08)]]); no OSHA text was read to confirm that.
- **FH5:** if lithium charging does not need a ventilated room (vendor claim) yet insurers and code ask for ventilation anyway, the "no battery room" selling point may be weaker than the vault's need note assumes (C318).

### Requirement and Use Case model (added 2026-10-17)

Per the 2026-10-17 owner decision (regulatory content as Requirement notes, Use Cases for where and what), without product closure checks for external obligations (tag `regulatory-driver`).

- **External obligations, code (Requirement, subtype standard):** REQ-00064 [[CFC 309 - Chargers Shall Be of an Approved Type]]; REQ-00065 [[CFC 309 - Combustible Storage Shall Stay 3 Feet From Chargers]]; REQ-00066 [[CFC 309 - Battery Charging Is Not Allowed in Areas Open to the Public]]; REQ-00067 [[CFC 309 - Charging Areas Shall Be Ventilated Against Flammable Gas Buildup]]; REQ-00068 [[CFC 309 - Charging Areas Need a Rated Extinguisher Within 20 Feet]].
- **External obligations, OSHA (Requirement, subtype standard; second-hand):** REQ-00069 [[OSHA 1910.178(g)(1) - Charging Installations Shall Be in Designated Areas]]; REQ-00070 [[OSHA STD 1-11.4 - Charging-Only Areas Are Judged Under (g)(1) and (g)(8) to (g)(12)]].
- **External expectations, insurer (Requirement, subtype stakeholder; not law):** REQ-00071 [[If P&C - Li-Ion Truck Charging Rooms Need Fire Separation, Detection and Sprinklers]]; REQ-00072 [[If P&C - Li-Ion Truck Charging Keeps 10 m From Buildings and Storage]]; REQ-00073 [[If P&C - Charging Areas Need Ventilation and Charger Cut-Off on Alarm or Ventilation Failure]]; REQ-00074 [[If P&C - Truck BMS Shall Talk to the Charger and the OEM Charger Is Used]]; REQ-00075 [[If P&C - Mark the Area, Provide Emergency Shut-Off and Clear Space Above Chargers]].
- **Derived product requirements (analyst-proposed, Draft; hypotheses FH2 to FH4):** REQ-00076 [[Fire and Insurer Review - Charger Shall Accept an External Interlock and Stop Charging When It Trips]]; REQ-00077 [[Fire and Insurer Review - Charger Shall Take Charge Permission and Limits From the Lithium Battery BMS]]; REQ-00078 [[Fire and Insurer Review - Charger Shall State the Listing Standard and Edition It Is Certified To]].
- **Need (Use Case, subtype why; hypothesis):** [[Get Charging Areas Approved by the Fire Authority and Insurer]].
- **Where (Use Case, subtype where):** [[Forklift Charging Area Under Fire Code and Insurer Review]]; related existing contexts [[Centralized Battery Room and Charging Area]] and [[Distributed and Opportunity Charging Area]].
- **What customers do (Use Case, subtype what; analyst hypothesis):** [[Obtain Fire Authority and Insurer Approval for a Charging Area]].
- **Decision for the owner:** the gate carve-out is keyed to the tag `regulatory-driver`, which these notes use. Insurer guidance is not regulation, so the tag is a stretch; the notes also carry `insurer-guidance` and `non-binding`. Say if a neutral tag such as `external-driver` should replace it in the gate scripts.

### What would change this picture

- NFPA 855 scope text shows it excludes (or includes) mobile-equipment battery charging (IB-273).
- IFC 2024 section 309 or NFPA 505-2024 turns out to contain lithium-specific charging rules (IB-274, IB-275).
- A US insurer (for example FM Global) publishes lithium forklift charging requirements (IB-278).
- A fire marshal letter or approval record shows how an authority treats a lithium charging room (IB-279).
- OSHA or the ITSDF publishes a lithium-specific position (IB-280).

### Open questions

Tracked as C314 to C322 and IB-273 to IB-283: NFPA 855 scope; the 2026 threshold wording; UL 1564 and UL 583 status; whether ventilation is expected for lithium-only rooms; OSHA coverage of lithium; NEC Article 625 for forklift chargers; and which authority and insurer practice actually governs US sites. The question for the owner at the end of the pass is whether PosiCharge sells into the EU, because the If and HDI sheets use European units and fire classes.

### Sources

- Codes and regulation: [[Document - California Fire Code 2025 Section 309 Powered Industrial Trucks (gocodebook, retrieved 2026-10-17)]]; [[Document - California Fire Code 2025 Section 322 Powered Micromobility Devices (gocodebook, retrieved 2026-10-17)]]; [[Document - OSHA Instruction STD 1-11.4 Battery Charging Stations for Fork Lifts (1978)]]; [[Document - 1910.178 Powered Industrial Trucks Course Slides (ETTA OSH Division, undated)]].
- Standards listings: [[Document - ANSI Webstore NFPA 505-2024 Listing (retrieved 2026-10-17)]]; [[Document - ANSI Webstore UL 583 Ed 11-2022 Listing (retrieved 2026-10-17)]]; [[Document - ANSI Webstore UL 1564 Ed 5-2024 Listing (retrieved 2026-10-17)]]; [[Document - ANSI Webstore UL 3100 Ed 1-2018 Listing (retrieved 2026-10-17)]].
- Insurers: [[Document - If P&C Hazard Info Sheet Lithium-Ion Stacker Trucks (2024-06)]]; [[Document - HDI Risk Engineering Guideline Battery Charging (2016)]].
- Trade and consulting: [[Document - MHI Blog Navigating Third-Party Safety Standards for Lithium Batteries in Lift Trucks (2024-10-08)]]; [[Document - Energy-Storage.news NFPA 855 2026 Edition Updates (2026-04-29)]]; [[Document - Meyer Fire Whats New in NFPA 855 2026 Edition (2025-09-17)]]; [[Document - SafetyFolio OSHA Requirements for Battery Charging Areas in Small Warehouses (2026)]]; [[Document - Electrical Contractor Magazine Whats Classified as an Electric Vehicle (2015-05-06)]].
- Leads read but not made into Document notes (forum or listing pages, lower value):
  - Meyer Fire forum thread on forklifts and gem carts in mechanical rooms: commenters cite NFPA 505 through NFPA 1 sections 10.17 and 34.6 and point to IFC section 309; one commenter doubts electric carts are in NFPA 505 scope; adopted code in that thread was IFC 2015. <https://meyerfire.com/daily/gem-carts-forklifts-allowed-in-mech-rooms>
  - Mike Holt forum thread on a forklift charging station feeder: one poster cites Article 625.42 (continuous load), another cites the 625.2 industrial truck exclusion; unresolved. <https://forums.mikeholt.com/threads/feeder-calculation-for-fork-lift-charging-station.133744>
  - Standards Council of Canada notice of intent for a joint ANSI/CAN/UL 583 new edition (posted 2021-02-01, scope updated 2022-02-01); the page does not mention lithium. <https://scc-ccn.ca/standards/notices-of-intent/underwriters-laboratories-inc-ul/standard-safety-electric-battery>
  - OSHA interlinking page for 1910.178(g)(2): lists directive STD 1-11.4 and a 1976 letter on "adequate ventilation" only, no standard text. <https://www.osha.gov/laws-regs/interlinking/standards/1910.178(g)(2)/all>
  - EnerSys press release, UL 2580 Listing for NexSys iON lithium batteries used in forklifts, AGVs and AMRs (2022-03-08). <https://www.enersys.com/en/about-us/news/enersys-is-taking-safety-to-the-next-level-with-ithium-ion-li-ion-underwriter-laboratories-ul-listing/>
  - ROYPOW press release, UL 2580 certification for lithium forklift batteries, with the BMS assessed separately for functional safety under UL 60730 (2025-04-14); the release does not say who requires UL 2580. <https://www.roypow.com/news/roypow-achieves-ul2580-certification-across-all-lithium-forklift-battery-voltage-platforms/>
  - NFPA 505-2024 product page (scope list: hazardous locations, dual-fuel trucks, conversions, maintenance, fuel recharging, marking, extinguishers; lithium not mentioned). <https://www.fire-police-ems.com/NFPA505-2024.shtml>
  - Not readable by the tools: NFPA 855 page <https://www.nfpa.org/codes-and-standards/nfpa-855-standard-development/855> (permission not answered), ICC IFC 2024 chapter 3 <https://codes.iccsafe.org/content/IFC2024P1/chapter-3-general-requirements> (permission not answered), IFC 2024 section 322.4 page (returned site shell only), Building Code Forum thread on battery charging and storage (robots block) <https://www.thebuildingcodeforum.com/forum/threads/battery-charging-and-storage.38140/latest>, up.codes (robots block).

## Aliases

- Fire code register
- Lithium charging area code register

## Former ids
