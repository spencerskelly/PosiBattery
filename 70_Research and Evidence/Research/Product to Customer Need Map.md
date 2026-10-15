---
type: Info
subtype:
id: INFO-00275
uid: 20261003215801362skellyspencer
status: Draft
tags:
  - customer-needs
  - product-need-map
  - derived
describedBy:
  - "[[Function-to-Need Gap Register]]"
describes:
  - "[[Battery-Connected Product]]"
---

# Product to Customer Need Map

## Definition

Derived map from each catalog product to the customer needs it serves, and from each need to the people who have it. Route F (strongest): product `performs` a specific Function, a Use Case (subtype why) is `realizedBy` that Function, and the Use Case `participants` lists the Actors. Routes D, O and M are weaker and stated apart so they are never mistaken for a performed function.

## Notes

- **Status: derived and hypothesis.** The map is generated from links already in the vault. Needs are what makers and dealers say their products do, not what customers say they need; a need becomes validated only with customer-side evidence (the ruleset's path from source research to hypothesis to validated need). Evidence and conflicts: C101 to C110, Q20 in [[Battery Product Landscape Conflicts and Open Questions]].
- **Routes.** F = by performed function. D = by design: the product has a design that a function realizing the need depends on (the product may not perform the function; other designs may also be required). O = by option: the vehicle or battery is offered with a product that reaches the need by F, so the need is reached only if the option is bought. M = by metric: the product has a value on a property metric that informs the need (analyst crosswalk, hypothesis; batteries are described by properties, which the vault keeps as metrics, not functions).
- **Regenerated 2026-10-14 (priority 4).** All counts and tables below were recomputed from the vault's links after the traceability, leaf-function and software passes. Rules: universe = every Object note under `10_Products` (README excluded); abstract class and category notes are counted apart; F = the product `performs` a Function that a need is `realizedBy`; D = the product `hasDesign` a Design that a Function realizing the need is `realizedBy` or `dependsOn` (not already F); O = a battery, forklift or GSE vehicle is `offeredWith` a product that reaches the need by F (not already F or D). The M column is carried over unchanged from the 2026-10-03 map and was not recomputed. The earlier generator is not in the repository, so these counts are not strictly comparable with round 40 (C269).
- **Reached (owner decision, round 40): a product counts as reached through route F, D or O. M stays a hypothesis column and is not counted as reached.** Of 509 concrete products (61 abstract class and category notes excluded): 438 are reached; 410 of those perform a realizing function (F); 7 more are added by design (D) and 21 more by option (O). The carried-over metric route adds 0 products that are not counted. 71 concrete products have no route at all.
- **GSE vehicles and batteries (2026-10-14 recount):** Ground Support Equipment 16 products, 5 by F, 10 reached (F + D + O); batteries 87 products, 57 by F, 74 reached. Most remaining gaps are source gaps (listings that state only properties), not modeling gaps.
- **The counts are lower bounds.** A product reaches a need only through links a source states.
- **2026-10-06 voltage-imbalance correction:** [[EnerSys Truck iQ]] no longer reaches [[Prevent Battery Abuse and Premature Replacement]] through [[Detect Voltage Imbalance]] because its source establishes display of the Wi-iQ imbalance result, not detection by Truck iQ itself.
- **2026-10-06 charger-status correction:** [[Crown V-HFM3 Tower Light Kit]] and [[PosiCharge Three-Color Stack Light]] no longer reach [[Know Battery State Before and During the Shift]] through [[Indicate Battery Status Locally]]; they now perform [[Indicate Charger Status Locally]], which currently has no customer-need link.

### Needs

| Need (Use Case, why) | Who has it | Operating segments (analyst crosswalk, hypothesis) | Products reached (F + D + O) | of which by F | Added by metric (M, hypothesis) | Functions | Evidence kinds |
|---|---|---|---|---|---|---|---|
| [[Keep Trucks Working Without Battery Maintenance Labor]] | [[Maintenance Technician]], [[Fleet Operations Manager]] | Material-handling fleets; Battery-room and centralized charging; Mixed-chemistry fleets | 111 | 78 | 5 | 5 | V |
| [[Charge Without a Ventilated Battery Room]] | [[Fleet Operations Manager]], [[Forklift Operator]] | Material-handling fleets; Distributed and opportunity charging; Mixed-chemistry fleets | 59 | 30 | 0 | 2 | V |
| [[Return Trucks to Service Quickly After a Low Charge]] | [[Fleet Operations Manager]], [[Forklift Operator]] | Material-handling fleets; Airport eGSE fleets; Distributed and opportunity charging | 95 | 64 | 4 | 8 | V |
| [[Charge Each Battery Correctly for Its Chemistry and Condition]] | [[Maintenance Technician]], [[Fleet Operations Manager]] | Mixed-chemistry fleets; Battery-room and centralized charging | 83 | 46 | 0 | 9 | V |
| [[Prevent Battery Abuse and Premature Replacement]] | [[Maintenance Technician]], [[Fleet Operations Manager]] | Material-handling fleets; Battery-room and centralized charging; Mixed-chemistry fleets | 85 | 70 | 5 | 15 | V |
| [[Know Battery State Before and During the Shift]] | [[Forklift Operator]], [[Maintenance Technician]] | Material-handling fleets; Airport eGSE fleets | 79 | 68 | 0 | 12 | V |
| [[Document Battery Care for Warranty Compliance]] | [[Fleet Operations Manager]], [[Dealer Service Technician]] | Material-handling fleets; Battery-room and centralized charging | 48 | 39 | 0 | 4 | V |
| [[Monitor and Manage Chargers and Batteries Across Sites]] | [[Fleet Operations Manager]] | Material-handling fleets; Airport eGSE fleets; Battery-room and centralized charging | 62 | 52 | 0 | 6 | V |
| [[Control Who Operates Each Truck]] | [[Fleet Operations Manager]], [[Site Safety Manager]], [[Forklift Operator]], [[Fleet Software Administrator]] | Material-handling fleets | 27 | 22 | 0 | 2 | V |
| [[Detect and Learn from Truck Impacts]] | [[Site Safety Manager]], [[Fleet Operations Manager]] | Material-handling fleets | 23 | 15 | 0 | 3 | V |
| [[Warn the Operator of People and Objects Near the Truck]] | [[Forklift Operator]], [[Site Safety Manager]] | Material-handling fleets; Airport eGSE fleets | 46 | 37 | 0 | 3 | V + G |
| [[Warn Pedestrians of an Approaching Truck]] | [[Pedestrian Near Trucks]], [[Site Safety Manager]] | Material-handling fleets | 63 | 50 | 0 | 2 | V + G |
| [[Prevent Tip-Overs and Overloads]] | [[Forklift Operator]], [[Site Safety Manager]] | Material-handling fleets | 45 | 33 | 0 | 9 | V + G |
| [[Keep Trucks Slow in Hazardous Zones]] | [[Site Safety Manager]], [[Pedestrian Near Trucks]] | Material-handling fleets | 42 | 32 | 0 | 2 | V + G |
| [[Protect Aircraft and Ground Crew During Ground Operations]] | [[GSE Operator]], [[Fleet Operations Manager]] | Airport eGSE fleets | 21 | 9 | 0 | 5 | V |
| [[Keep the Operator Positioned and Able to See the Work]] | [[Forklift Operator]] | Material-handling fleets | 42 | 31 | 0 | 5 | V |
| [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] | [[Fleet Operations Manager]], [[Forklift Operator]] | Material-handling fleets; Airport eGSE fleets | 34 | 22 | 20 | 4 | V |
| [[Stretch Truck Run Time per Charge]] | [[Fleet Operations Manager]] | Material-handling fleets; Distributed and opportunity charging | 11 | 9 | 0 | 2 | V |
| [[Integrate the Battery with Truck and Charger Controls]] | [[Truck OEM Integration Engineer]] | Mixed-chemistry fleets | 58 | 32 | 4 | 7 | V |
| [[Retrofit Safety and Telematics Onto Existing Trucks]] | [[Dealer Sales Representative]], [[Dealer Service Technician]], [[Equipment Installer]] | Material-handling fleets; Mixed-chemistry fleets | 51 | 37 | 0 | 4 | V |
| [[Connect Chargers and Batteries Safely at the Site]] | [[Equipment Installer]], [[Forklift Operator]] | Battery-room and centralized charging; Distributed and opportunity charging; Airport eGSE fleets | 47 | 25 | 0 | 7 | V + manual |
| [[Find and Fix Vehicle Faults Without Downtime]] | [[Maintenance Technician]], [[Dealer Service Technician]], [[Fleet Operations Manager]] | Material-handling fleets; Airport eGSE fleets | 17 | 12 | 0 | 3 | V |
| [[Act on Fleet Data Without Information Overload]] | [[Fleet Operations Manager]], [[Fleet Software Administrator]] | not yet assigned | 35 | 28 | 0 | 3 | V |
| [[Charge Within Site Power Limits and Utility Costs]] | [[Fleet Operations Manager]] | not yet assigned | 11 | 9 | 0 | 1 | V |
| [[Charge Without Anyone Plugging In]] | [[Fleet Operations Manager]], [[Forklift Operator]] | not yet assigned | 19 | 19 | 0 | 5 | V |
| [[Handle Loads Without Damaging Them]] | [[Forklift Operator]], [[Fleet Operations Manager]] | not yet assigned | 3 | 2 | 0 | 1 | analyst |
| [[Keep the Truck Under Control on Slopes, Slippery Floors and in Emergencies]] | [[Forklift Operator]], [[Site Safety Manager]] | not yet assigned | 16 | 11 | 0 | 4 | analyst |
| [[Plan Battery Replacement and Budget Ahead]] | [[Fleet Operations Manager]] | not yet assigned | 48 | 39 | 0 | 4 | V |
| [[Reduce Operator Effort and Fatigue]] | [[Forklift Operator]], [[Fleet Operations Manager]] | not yet assigned | 3 | 3 | 0 | 2 | analyst |
| [[Right-Size the Fleet from Usage Data]] | [[Fleet Operations Manager]] | not yet assigned | 44 | 30 | 0 | 4 | V |

Evidence kinds: V = vendor or dealer statement in product notes; G = government statistics showing the underlying problem exists; manual = a maker's installation or service manual; analyst = need derived by the analyst from customer work, no source states it.

### Roles

| Actor | Evidence status | Needs | Which |
|---|---|---|---|
| [[Vehicle Operator]] | source-stated | 0 | none (supertype or no need linked yet) |
| [[Forklift Operator]] | source-stated | 13 | [[Charge Without a Ventilated Battery Room]], [[Return Trucks to Service Quickly After a Low Charge]], [[Know Battery State Before and During the Shift]], [[Control Who Operates Each Truck]], [[Warn the Operator of People and Objects Near the Truck]], [[Prevent Tip-Overs and Overloads]], [[Keep the Operator Positioned and Able to See the Work]], [[Keep Equipment Working in Cold, Wet and Dusty Conditions]], [[Connect Chargers and Batteries Safely at the Site]], [[Charge Without Anyone Plugging In]], [[Handle Loads Without Damaging Them]], [[Keep the Truck Under Control on Slopes, Slippery Floors and in Emergencies]], [[Reduce Operator Effort and Fatigue]] |
| [[GSE Operator]] | source-stated | 1 | [[Protect Aircraft and Ground Crew During Ground Operations]] |
| [[Pedestrian Near Trucks]] | source-stated | 2 | [[Warn Pedestrians of an Approaching Truck]], [[Keep Trucks Slow in Hazardous Zones]] |
| [[Maintenance Technician]] | source-stated | 5 | [[Keep Trucks Working Without Battery Maintenance Labor]], [[Charge Each Battery Correctly for Its Chemistry and Condition]], [[Prevent Battery Abuse and Premature Replacement]], [[Know Battery State Before and During the Shift]], [[Find and Fix Vehicle Faults Without Downtime]] |
| [[Fleet Operations Manager]] | source-stated | 20 | [[Keep Trucks Working Without Battery Maintenance Labor]], [[Charge Without a Ventilated Battery Room]], [[Return Trucks to Service Quickly After a Low Charge]], [[Charge Each Battery Correctly for Its Chemistry and Condition]], [[Prevent Battery Abuse and Premature Replacement]], [[Document Battery Care for Warranty Compliance]], [[Monitor and Manage Chargers and Batteries Across Sites]], [[Control Who Operates Each Truck]], [[Detect and Learn from Truck Impacts]], [[Protect Aircraft and Ground Crew During Ground Operations]], [[Keep Equipment Working in Cold, Wet and Dusty Conditions]], [[Stretch Truck Run Time per Charge]], [[Find and Fix Vehicle Faults Without Downtime]], [[Act on Fleet Data Without Information Overload]], [[Charge Within Site Power Limits and Utility Costs]], [[Charge Without Anyone Plugging In]], [[Handle Loads Without Damaging Them]], [[Plan Battery Replacement and Budget Ahead]], [[Reduce Operator Effort and Fatigue]], [[Right-Size the Fleet from Usage Data]] |
| [[Site Safety Manager]] | hypothesis | 7 | [[Control Who Operates Each Truck]], [[Detect and Learn from Truck Impacts]], [[Warn the Operator of People and Objects Near the Truck]], [[Warn Pedestrians of an Approaching Truck]], [[Prevent Tip-Overs and Overloads]], [[Keep Trucks Slow in Hazardous Zones]], [[Keep the Truck Under Control on Slopes, Slippery Floors and in Emergencies]] |
| [[Dealer Sales Representative]] | source-implied | 1 | [[Retrofit Safety and Telematics Onto Existing Trucks]] |
| [[Dealer Service Technician]] | source-stated | 3 | [[Document Battery Care for Warranty Compliance]], [[Retrofit Safety and Telematics Onto Existing Trucks]], [[Find and Fix Vehicle Faults Without Downtime]] |
| [[Equipment Installer]] | source-stated | 2 | [[Retrofit Safety and Telematics Onto Existing Trucks]], [[Connect Chargers and Batteries Safely at the Site]] |
| [[Truck OEM Integration Engineer]] | source-implied | 1 | [[Integrate the Battery with Truck and Charger Controls]] |
| [[Fleet Software Administrator]] | see actor note | 2 | [[Control Who Operates Each Truck]], [[Act on Fleet Data Without Information Overload]] |

### Segments and needs (crosswalk to [[PosiCharge Market Segments and Jobs-to-Be-Done]])

The crosswalk is the analyst's reading, not a source statement.

| Segment | Needs | Which |
|---|---|---|
| Material-handling fleets | 18 | [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Warn the Operator of People and Objects Near the Truck]]; [[Prevent Tip-Overs and Overloads]]; [[Detect and Learn from Truck Impacts]]; [[Keep Trucks Slow in Hazardous Zones]]; [[Charge Without a Ventilated Battery Room]]; [[Control Who Operates Each Truck]]; [[Prevent Battery Abuse and Premature Replacement]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Keep the Operator Positioned and Able to See the Work]]; [[Return Trucks to Service Quickly After a Low Charge]]; [[Warn Pedestrians of an Approaching Truck]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Document Battery Care for Warranty Compliance]]; [[Find and Fix Vehicle Faults Without Downtime]]; [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Know Battery State Before and During the Shift]]; [[Stretch Truck Run Time per Charge]] |
| Airport eGSE fleets | 8 | [[Connect Chargers and Batteries Safely at the Site]]; [[Warn the Operator of People and Objects Near the Truck]]; [[Return Trucks to Service Quickly After a Low Charge]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Protect Aircraft and Ground Crew During Ground Operations]]; [[Find and Fix Vehicle Faults Without Downtime]]; [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Know Battery State Before and During the Shift]] |
| Mixed-chemistry fleets | 6 | [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Charge Without a Ventilated Battery Room]]; [[Prevent Battery Abuse and Premature Replacement]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Integrate the Battery with Truck and Charger Controls]] |
| Battery-room and centralized charging | 6 | [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Connect Chargers and Batteries Safely at the Site]]; [[Prevent Battery Abuse and Premature Replacement]]; [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Document Battery Care for Warranty Compliance]] |
| Distributed and opportunity charging | 4 | [[Connect Chargers and Batteries Safely at the Site]]; [[Charge Without a Ventilated Battery Room]]; [[Return Trucks to Service Quickly After a Low Charge]]; [[Stretch Truck Run Time per Charge]] |

Needs added after 2026-10-03 (UC-00050 to UC-00054 and others marked 'not yet assigned' in the Needs table) have no segment assigned; the crosswalk above is unchanged.

### Metric crosswalk (route M)

Which property metrics inform which need. This is the analyst's reading (hypothesis); the metric notes hold the stated values.

| Metric | Need it informs | Products with a value on file |
|---|---|---|
| [[Metric - Watering Interval]] | [[Keep Trucks Working Without Battery Maintenance Labor]] | 9 |
| [[Metric - Charging Gas Emissions]] | [[Charge Without a Ventilated Battery Room]] | 4 |
| [[Metric - Charge Time]] | [[Return Trucks to Service Quickly After a Low Charge]] | 4 |
| [[Metric - Charge Regimes Supported]] | [[Return Trucks to Service Quickly After a Low Charge]] | 10 |
| [[Metric - Charge Temperature Limits]] | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] | 4 |
| [[Metric - Operating Temperature Range]] | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] | 18 |
| [[Metric - Depth of Discharge Limit]] | [[Prevent Battery Abuse and Premature Replacement]] | 2 |
| [[Metric - Equalizing Charge Rule]] | [[Prevent Battery Abuse and Premature Replacement]] | 7 |
| [[Metric - BMS and Communication]] | [[Integrate the Battery with Truck and Charger Controls]] | 10 |
| [[Metric - Wired and Vehicle Interfaces]] | [[Integrate the Battery with Truck and Charger Controls]] | 8 |

### Families

Concrete products only (abstract class and category notes excluded).

| Product family | Products | By F | Reached (F + D + O) | Reached plus M (hypothesis) |
|---|---|---|---|---|
|  | 0 | 0 | 0 | 0 |
| Batteries | 0 | 0 | 0 | 0 |
| Batteries/Flooded Lead-Acid Batteries | 32 | 17 | 28 | 28 |
| Batteries/Lithium-Ion Batteries | 39 | 31 | 36 | 36 |
| Batteries/Valve-Regulated Lead-Acid Batteries | 16 | 9 | 10 | 10 |
| Battery Accessories | 1 | 0 | 0 | 0 |
| Battery Accessories/Battery Management Systems | 9 | 6 | 6 | 6 |
| Battery Accessories/Connector Assemblies | 11 | 11 | 11 | 11 |
| Battery Accessories/Electrolyte Circulation Systems | 8 | 8 | 8 | 8 |
| Battery Accessories/Identification and Charge Interface Devices | 8 | 6 | 7 | 7 |
| Battery Accessories/Monitoring Devices | 34 | 28 | 28 | 28 |
| Battery Accessories/Protection and Disconnect Units | 0 | 0 | 0 | 0 |
| Battery Accessories/Telematics and Connectivity Devices | 2 | 2 | 2 | 2 |
| Battery Accessories/Thermal Management Devices | 0 | 0 | 0 | 0 |
| Battery Accessories/Water Level Monitors | 8 | 8 | 8 | 8 |
| Battery Accessories/Watering Systems | 12 | 10 | 10 | 10 |
| Charger Accessories | 2 | 1 | 1 | 1 |
| Charger Accessories/Cable Management | 1 | 1 | 1 | 1 |
| Charger Accessories/Connector Accessories | 6 | 6 | 6 | 6 |
| Charger Accessories/Remote Controls and Indicators | 3 | 3 | 3 | 3 |
| Charger Accessories/Stands and Mounting | 2 | 1 | 1 | 1 |
| Charger Accessories/Thermal Accessories | 1 | 1 | 1 | 1 |
| Chargers | 6 | 6 | 6 | 6 |
| Chargers/Industrial Modular Chargers | 40 | 38 | 38 | 38 |
| Chargers/Light-Duty Chargers | 3 | 3 | 3 | 3 |
| Chargers/On-board Chargers | 5 | 4 | 4 | 4 |
| Chargers/Wireless Chargers | 10 | 10 | 10 | 10 |
| Fleet Software and Platforms | 13 | 11 | 11 | 11 |
| Fleet Software and Platforms/Battery and Charger Management | 25 | 22 | 22 | 22 |
| Fleet Software and Platforms/Truck Telematics | 24 | 22 | 22 | 22 |
| Forklifts | 7 | 0 | 0 | 0 |
| Forklifts/Class I Electric Rider Trucks | 36 | 24 | 28 | 28 |
| Forklifts/Class II Electric Narrow Aisle Trucks | 5 | 2 | 3 | 3 |
| Forklifts/Class III Electric Hand and Hand-Rider Trucks | 2 | 2 | 2 | 2 |
| Forklifts/Class IV Internal Combustion Cushion Tire Trucks | 0 | 0 | 0 | 0 |
| Forklifts/Class V Internal Combustion Pneumatic Tire Trucks | 0 | 0 | 0 | 0 |
| Forklifts/Class VI Tractors | 0 | 0 | 0 | 0 |
| Forklifts/Class VII Rough Terrain Forklifts | 0 | 0 | 0 | 0 |
| Fuel Cell Power Units/Hydrogen Fuel Cell Units | 2 | 2 | 2 | 2 |
| Ground Support Equipment | 0 | 0 | 0 | 0 |
| Ground Support Equipment/Baggage and Tow Tractors | 6 | 2 | 2 | 2 |
| Ground Support Equipment/Belt Loaders | 5 | 2 | 5 | 5 |
| Ground Support Equipment/Cargo Loaders | 2 | 0 | 2 | 2 |
| Ground Support Equipment/Pushback Tractors | 3 | 1 | 1 | 1 |
| Vehicle Accessories | 0 | 0 | 0 | 0 |
| Vehicle Accessories/Access Control | 3 | 3 | 3 | 3 |
| Vehicle Accessories/Cameras and Recorders | 7 | 7 | 7 | 7 |
| Vehicle Accessories/Cold Storage Packages | 4 | 4 | 4 | 4 |
| Vehicle Accessories/Operator Assist and Stability | 42 | 39 | 39 | 39 |
| Vehicle Accessories/Operator Convenience | 11 | 6 | 6 | 6 |
| Vehicle Accessories/Operator Displays | 5 | 5 | 5 | 5 |
| Vehicle Accessories/Power Source Interfaces | 4 | 2 | 2 | 2 |
| Vehicle Accessories/Proximity and Object Detection | 29 | 29 | 29 | 29 |
| Vehicle Accessories/Warning Lights and Alerts | 15 | 15 | 15 | 15 |

### Per-product route

Generated list. A dash means no product in that route. M is carried over unchanged from the 2026-10-03 map; it was not recomputed.

#### Batteries/Flooded Lead-Acid Batteries

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Amaron Brute Hi-Life Battery]] | - | - | [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Prevent Battery Abuse and Premature Replacement]] | - |
| [[Banner Traction Bull Bloc PzF]] | - | - | - | - |
| [[Banner Traction Bull PzS]] | - | - | [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Prevent Battery Abuse and Premature Replacement]] | - |
| [[Crown V-Force Lead-Acid Battery]] | - | - | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Charge Within Site Power Limits and Utility Costs]]; [[Charge Without a Ventilated Battery Room]]; [[Document Battery Care for Warranty Compliance]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Plan Battery Replacement and Budget Ahead]]; [[Prevent Battery Abuse and Premature Replacement]]; [[Return Trucks to Service Quickly After a Low Charge]] | - |
| [[Deka ChargeMate Battery]] | [[Charge Without a Ventilated Battery Room]] | - | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Return Trucks to Service Quickly After a Low Charge]] | - |
| [[Deka D-Series Battery]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]] | [[Prevent Battery Abuse and Premature Replacement]] |
| [[Deka FastCharge Battery]] | [[Return Trucks to Service Quickly After a Low Charge]] | - | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]] | - |
| [[Deka HydraSaver Battery]] | [[Keep Trucks Working Without Battery Maintenance Labor]] | - | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Charge Without a Ventilated Battery Room]]; [[Return Trucks to Service Quickly After a Low Charge]] | - |
| [[Deka MaintenanceSaver Battery]] | - | - | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Return Trucks to Service Quickly After a Low Charge]] | - |
| [[Deka MaxPowr Battery]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]] | - | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Return Trucks to Service Quickly After a Low Charge]] | [[Prevent Battery Abuse and Premature Replacement]] |
| [[EnerSys IRONCLAD Battery]] | - | - | [[Act on Fleet Data Without Information Overload]]; [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Document Battery Care for Warranty Compliance]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Plan Battery Replacement and Budget Ahead]]; [[Prevent Battery Abuse and Premature Replacement]]; [[Return Trucks to Service Quickly After a Low Charge]]; [[Right-Size the Fleet from Usage Data]] | - |
| [[Exide MARATHON Battery]] | [[Keep Trucks Working Without Battery Maintenance Labor]] | [[Prevent Battery Abuse and Premature Replacement]] | - | - |
| [[Exide MARATHON Classic Battery]] | - | - | [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Prevent Battery Abuse and Premature Replacement]] | - |
| [[Exide MARATHON Excell Battery]] | [[Keep Trucks Working Without Battery Maintenance Labor]] | - | [[Prevent Battery Abuse and Premature Replacement]] | - |
| [[Exide TENSOR Battery]] | [[Return Trucks to Service Quickly After a Low Charge]] | - | [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Prevent Battery Abuse and Premature Replacement]] | - |
| [[GS Yuasa Traction Battery (Europe)]] | [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | - |
| [[HAWKER Perfect Plus Battery]] | [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Prevent Battery Abuse and Premature Replacement]] | - | [[Act on Fleet Data Without Information Overload]]; [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Document Battery Care for Warranty Compliance]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Plan Battery Replacement and Budget Ahead]] | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] |
| [[HOPPECKE trak uplift air Battery]] | [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Prevent Battery Abuse and Premature Replacement]] | - | [[Charge Each Battery Correctly for Its Chemistry and Condition]] | - |
| [[HOPPECKE trak uplift iQ Battery]] | [[Know Battery State Before and During the Shift]] | - | [[Act on Fleet Data Without Information Overload]]; [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Document Battery Care for Warranty Compliance]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Plan Battery Replacement and Budget Ahead]]; [[Prevent Battery Abuse and Premature Replacement]] | - |
| [[Leoch PzS Traction Battery]] | - | - | [[Keep Trucks Working Without Battery Maintenance Labor]] | - |
| [[Midac FORCEblock Battery]] | - | - | - | - |
| [[Midac MBS Traction Battery]] | - | - | - | - |
| [[Midac MDLblock Battery]] | - | - | [[Charge Each Battery Correctly for Its Chemistry and Condition]] | - |
| [[Midac MHE Battery]] | - | - | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Prevent Battery Abuse and Premature Replacement]]; [[Return Trucks to Service Quickly After a Low Charge]] | - |
| [[Midac MLM Battery]] | - | - | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Prevent Battery Abuse and Premature Replacement]]; [[Return Trucks to Service Quickly After a Low Charge]] | - |
| [[Midac MLMx Battery]] | - | - | - | - |
| [[Midac PzS Traction Battery]] | - | - | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Connect Chargers and Batteries Safely at the Site]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Prevent Battery Abuse and Premature Replacement]] | - |
| [[Stryten M-Series F100 Battery]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]] | - | - | [[Return Trucks to Service Quickly After a Low Charge]] |
| [[Stryten M-Series F110 Battery]] | [[Return Trucks to Service Quickly After a Low Charge]] | - | [[Charge Each Battery Correctly for Its Chemistry and Condition]] | [[Prevent Battery Abuse and Premature Replacement]]; [[Return Trucks to Service Quickly After a Low Charge]] |
| [[Stryten M-Series T300 Battery]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Prevent Battery Abuse and Premature Replacement]]; [[Return Trucks to Service Quickly After a Low Charge]] |
| [[Stryten M-Series T310 Battery]] | [[Return Trucks to Service Quickly After a Low Charge]] | - | [[Charge Each Battery Correctly for Its Chemistry and Condition]] | [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Prevent Battery Abuse and Premature Replacement]]; [[Return Trucks to Service Quickly After a Low Charge]] |
| [[Stryten M-Series T330 Battery]] | [[Prevent Battery Abuse and Premature Replacement]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | [[Charge Each Battery Correctly for Its Chemistry and Condition]] | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Prevent Battery Abuse and Premature Replacement]]; [[Return Trucks to Service Quickly After a Low Charge]] |

#### Batteries/Lithium-Ion Batteries

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[BSL Lithium Forklift Battery]] | - | - | - | - |
| [[BlitzNXT LiFePO4 Forklift Battery]] | [[Connect Chargers and Batteries Safely at the Site]] | - | - | - |
| [[Cat Lithium-Ion Battery Option]] | [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |
| [[Chase Technologies Li-ion Retrofit Packs]] | [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |
| [[Crown V-Force Lithium-Ion ESS]] | [[Know Battery State Before and During the Shift]]; [[Prevent Battery Abuse and Premature Replacement]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Return Trucks to Service Quickly After a Low Charge]] | [[Charge Within Site Power Limits and Utility Costs]]; [[Charge Without a Ventilated Battery Room]]; [[Control Who Operates Each Truck]]; [[Find and Fix Vehicle Faults Without Downtime]]; [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Keep Trucks Slow in Hazardous Zones]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Keep the Truck Under Control on Slopes, Slippery Floors and in Emergencies]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Prevent Tip-Overs and Overloads]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Stretch Truck Run Time per Charge]]; [[Warn Pedestrians of an Approaching Truck]] | - |
| [[Deka Ready Power Lithium Battery]] | [[Integrate the Battery with Truck and Charger Controls]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Return Trucks to Service Quickly After a Low Charge]] | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]] | - |
| [[EnerSys NexSys iON Battery]] | [[Integrate the Battery with Truck and Charger Controls]]; [[Prevent Battery Abuse and Premature Replacement]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | - |
| [[Exide GNB Lithium Battery 2.0]] | [[Document Battery Care for Warranty Compliance]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Plan Battery Replacement and Budget Ahead]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | [[Integrate the Battery with Truck and Charger Controls]] |
| [[Exide Solition Light Traction Battery]] | [[Integrate the Battery with Truck and Charger Controls]]; [[Know Battery State Before and During the Shift]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Return Trucks to Service Quickly After a Low Charge]] | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]] | - |
| [[Exide Solition Material Handling Battery]] | [[Document Battery Care for Warranty Compliance]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Plan Battery Replacement and Budget Ahead]] | - | - | - |
| [[Exide Sonnenschein Lithium Battery]] | [[Integrate the Battery with Truck and Charger Controls]]; [[Know Battery State Before and During the Shift]]; [[Prevent Battery Abuse and Premature Replacement]]; [[Return Trucks to Service Quickly After a Low Charge]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]] | [[Act on Fleet Data Without Information Overload]]; [[Charge Without a Ventilated Battery Room]]; [[Document Battery Care for Warranty Compliance]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Plan Battery Replacement and Budget Ahead]] | - |
| [[Flux Power GSE2]] | [[Integrate the Battery with Truck and Charger Controls]] | - | - | - |
| [[Flux Power GSE3]] | [[Integrate the Battery with Truck and Charger Controls]] | - | - | - |
| [[Flux Power GSE4]] | [[Integrate the Battery with Truck and Charger Controls]] | - | - | - |
| [[Flux Power GSE6]] | [[Integrate the Battery with Truck and Charger Controls]] | - | - | - |
| [[Flux Power LiFT Pack]] | [[Integrate the Battery with Truck and Charger Controls]] | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] | - | [[Integrate the Battery with Truck and Charger Controls]]; [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Return Trucks to Service Quickly After a Low Charge]] |
| [[Flux Power S-Series Battery]] | - | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Return Trucks to Service Quickly After a Low Charge]] | [[Act on Fleet Data Without Information Overload]]; [[Document Battery Care for Warranty Compliance]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Plan Battery Replacement and Budget Ahead]] | [[Integrate the Battery with Truck and Charger Controls]] |
| [[Godrej Lithium-Ion Forklift Battery]] | - | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | [[Return Trucks to Service Quickly After a Low Charge]] |
| [[Godrej Multi-Ion Forklift Battery]] | [[Return Trucks to Service Quickly After a Low Charge]] | - | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] |
| [[Green Cubes Forklift Battery Retrofit Kit]] | - | - | - | - |
| [[Green Cubes GSE Lithium Battery]] | [[Integrate the Battery with Truck and Charger Controls]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Return Trucks to Service Quickly After a Low Charge]] | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]] | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] |
| [[Green Cubes SAFEFlex Battery]] | [[Know Battery State Before and During the Shift]]; [[Prevent Battery Abuse and Premature Replacement]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Return Trucks to Service Quickly After a Low Charge]] | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]] | [[Integrate the Battery with Truck and Charger Controls]]; [[Return Trucks to Service Quickly After a Low Charge]] |
| [[Green Cubes SAFEFlex PLUS Battery]] | [[Document Battery Care for Warranty Compliance]]; [[Know Battery State Before and During the Shift]]; [[Plan Battery Replacement and Budget Ahead]]; [[Prevent Battery Abuse and Premature Replacement]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | - |
| [[HOPPECKE trak power Lithium Battery]] | - | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | - |
| [[Hangcha Lithium Iron Phosphate Battery Pack]] | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | [[Control Who Operates Each Truck]]; [[Find and Fix Vehicle Faults Without Downtime]]; [[Handle Loads Without Damaging Them]]; [[Keep the Operator Positioned and Able to See the Work]]; [[Keep the Truck Under Control on Slopes, Slippery Floors and in Emergencies]]; [[Prevent Tip-Overs and Overloads]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Warn Pedestrians of an Approaching Truck]] | - |
| [[Heli Lithium-Ion Battery]] | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] | - | [[Charge Without a Ventilated Battery Room]]; [[Keep the Truck Under Control on Slopes, Slippery Floors and in Emergencies]]; [[Prevent Tip-Overs and Overloads]] | - |
| [[Jungheinrich Lithium-Ion Battery]] | [[Return Trucks to Service Quickly After a Low Charge]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]] | - | [[Return Trucks to Service Quickly After a Low Charge]] |
| [[Linde 90 V Lithium-Ion Battery]] | - | - | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]] | - |
| [[Midac LFPblock Battery]] | [[Monitor and Manage Chargers and Batteries Across Sites]] | - | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]] | - |
| [[Midac Li-Ion Battery]] | [[Integrate the Battery with Truck and Charger Controls]] | - | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]] | - |
| [[ROYPOW LiFePO4 Forklift Batteries]] | [[Connect Chargers and Batteries Safely at the Site]] | - | - | - |
| [[Raymond 8250 Lithium-Ion Battery]] | [[Charge Without a Ventilated Battery Room]]; [[Know Battery State Before and During the Shift]]; [[Prevent Battery Abuse and Premature Replacement]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | [[Control Who Operates Each Truck]]; [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] | [[Keep Trucks Working Without Battery Maintenance Labor]] |
| [[Raymond Energy Essentials Lithium-Ion Battery]] | [[Prevent Battery Abuse and Premature Replacement]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | [[Detect and Learn from Truck Impacts]]; [[Document Battery Care for Warranty Compliance]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Plan Battery Replacement and Budget Ahead]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Right-Size the Fleet from Usage Data]] | - |
| [[Redway Lithium Forklift Batteries]] | - | - | - | - |
| [[Stryten M-Series Li600 Battery]] | [[Integrate the Battery with Truck and Charger Controls]] | - | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Return Trucks to Service Quickly After a Low Charge]] | - |
| [[Stryten M-Series Li610 Battery]] | [[Know Battery State Before and During the Shift]]; [[Prevent Battery Abuse and Premature Replacement]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Return Trucks to Service Quickly After a Low Charge]] | [[Charge Without a Ventilated Battery Room]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Keep Trucks Working Without Battery Maintenance Labor]] | - |
| [[Toyota Lithium-Ion 5-35 Battery Series]] | [[Integrate the Battery with Truck and Charger Controls]]; [[Return Trucks to Service Quickly After a Low Charge]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]] | [[Find and Fix Vehicle Faults Without Downtime]] | - |
| [[Triathlon Lithium-Ion Battery for UniCarriers]] | - | - | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Prevent Tip-Overs and Overloads]] | [[Charge Without a Ventilated Battery Room]]; [[Return Trucks to Service Quickly After a Low Charge]] |
| [[Wiferion etaTRAY Battery Tray]] | [[Charge Without Anyone Plugging In]] | [[Connect Chargers and Batteries Safely at the Site]]; [[Integrate the Battery with Truck and Charger Controls]] | - | - |

#### Batteries/Valve-Regulated Lead-Acid Batteries

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Banner Traction Bull PzV Gel]] | - | - | - | - |
| [[Deka Dominator Battery]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]] | - |
| [[Deka Gel-Mate Battery]] | [[Charge Without a Ventilated Battery Room]] | - | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Return Trucks to Service Quickly After a Low Charge]] | - |
| [[Deka PowrMate Battery]] | [[Charge Without a Ventilated Battery Room]] | - | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Return Trucks to Service Quickly After a Low Charge]] | - |
| [[EnerSys NexSys TPPL Battery]] | [[Return Trucks to Service Quickly After a Low Charge]] | - | [[Act on Fleet Data Without Information Overload]]; [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Charge Without a Ventilated Battery Room]]; [[Connect Chargers and Batteries Safely at the Site]]; [[Document Battery Care for Warranty Compliance]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Plan Battery Replacement and Budget Ahead]]; [[Prevent Battery Abuse and Premature Replacement]] | - |
| [[EnerSys NexSys TPPL Bloc Battery]] | [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |
| [[Exide Element VRLA Battery]] | - | - | - | - |
| [[Exide TENSOR xGEL Battery]] | [[Return Trucks to Service Quickly After a Low Charge]] | - | [[Act on Fleet Data Without Information Overload]]; [[Document Battery Care for Warranty Compliance]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Plan Battery Replacement and Budget Ahead]] | - |
| [[Sonnenschein AF Battery]] | - | - | - | - |
| [[Sonnenschein AS Battery]] | [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |
| [[Sonnenschein EPzV Battery]] | - | - | - | - |
| [[Sonnenschein GF-V Battery]] | - | - | - | - |
| [[Sonnenschein GF-Y Battery]] | - | - | - | - |
| [[Stryten M-Series AGM200 Battery]] | [[Act on Fleet Data Without Information Overload]] | - | - | [[Keep Trucks Working Without Battery Maintenance Labor]] |
| [[Stryten M-Series AGM210 Battery]] | - | - | [[Return Trucks to Service Quickly After a Low Charge]] | - |
| [[Stryten M-Series AGM220 Battery]] | [[Return Trucks to Service Quickly After a Low Charge]] | [[Charge Without a Ventilated Battery Room]] | - | - |

#### Battery Accessories

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Flux Power GSE3 Truck Adapter]] | - | - | - | - |

#### Battery Accessories/Battery Management Systems

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Batrium CellMate-K9]] | [[Know Battery State Before and During the Shift]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | - |
| [[Batrium ShuntMon2]] | [[Know Battery State Before and During the Shift]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | - |
| [[Batrium WatchMonCORE]] | [[Prevent Battery Abuse and Premature Replacement]] | - | - | - |
| [[Flux SkyBMS]] | [[Act on Fleet Data Without Information Overload]]; [[Document Battery Care for Warranty Compliance]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Plan Battery Replacement and Budget Ahead]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | - |
| [[Midac Battery Management (MBM)]] | - | - | - | - |
| [[Nuvation Energy G5 BMS]] | - | - | - | - |
| [[Orion BMS 2]] | [[Integrate the Battery with Truck and Charger Controls]]; [[Know Battery State Before and During the Shift]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | - |
| [[REC 2Q BMS]] | - | - | - | - |
| [[REC Active BMS]] | [[Prevent Battery Abuse and Premature Replacement]] | - | - | - |

#### Battery Accessories/Connector Assemblies

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Anderson A Series Euro Connector]] | [[Connect Chargers and Batteries Safely at the Site]] | - | - | - |
| [[Anderson Double Stack Manual Assist Brackets]] | [[Connect Chargers and Batteries Safely at the Site]] | - | - | - |
| [[Anderson EBC Euro Battery Connector]] | [[Connect Chargers and Batteries Safely at the Site]] | - | - | - |
| [[Anderson IBC Industrial Battery Connector]] | [[Connect Chargers and Batteries Safely at the Site]] | - | - | - |
| [[Anderson SB Connector Series]] | [[Connect Chargers and Batteries Safely at the Site]] | - | - | - |
| [[Anderson SBE SBX SBO Connector Series]] | [[Connect Chargers and Batteries Safely at the Site]] | - | - | - |
| [[Anderson SBE320-SBX350 Charger-Truck Side Bracket Kit]] | [[Connect Chargers and Batteries Safely at the Site]] | - | - | - |
| [[Crown Battery Cables and Connectors]] | [[Connect Chargers and Batteries Safely at the Site]] | - | - | - |
| [[HOPPECKE AGV Battery Exchange System]] | [[Charge Without Anyone Plugging In]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |
| [[Midac End Leads]] | [[Connect Chargers and Batteries Safely at the Site]] | - | - | - |
| [[REMA Euro DIN Battery Connector]] | [[Connect Chargers and Batteries Safely at the Site]] | - | - | - |

#### Battery Accessories/Electrolyte Circulation Systems

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Amaron Electrolyte Circulation System]] | [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | - |
| [[Banner Traction Bull Electrolyte Circulation Pump Module]] | [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | - |
| [[EnerSys Aeromatic Circulation System]] | [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | - |
| [[Exide AIR Electrolyte Agitation System]] | [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | - |
| [[GS Yuasa Air-Mix System]] | [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | - |
| [[HOPPECKE trak air Electrolyte Circulation]] | [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | - |
| [[Midac Air-Tech Air-Mixing System]] | [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | - |
| [[Midac EUW Electrolyte Circulation System]] | [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | - |

#### Battery Accessories/Identification and Charge Interface Devices

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[AMETEK Prestolite Power BID]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | [[Integrate the Battery with Truck and Charger Controls]] |
| [[AMETEK Prestolite Power BID with Ah Accumulator]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Document Battery Care for Warranty Compliance]]; [[Know Battery State Before and During the Shift]]; [[Plan Battery Replacement and Budget Ahead]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | - |
| [[Crown V-Force BMID]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Document Battery Care for Warranty Compliance]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Plan Battery Replacement and Budget Ahead]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | - |
| [[Fronius TagID]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | - |
| [[PosiCharge BMID 1]] | - | - | - | - |
| [[PosiCharge BMID 3]] | - | [[Integrate the Battery with Truck and Charger Controls]] | - | - |
| [[PosiCharge Battery Rx]] | [[Act on Fleet Data Without Information Overload]]; [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Document Battery Care for Warranty Compliance]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Plan Battery Replacement and Budget Ahead]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] |
| [[PosiCharge PosiGuard]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Document Battery Care for Warranty Compliance]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Plan Battery Replacement and Budget Ahead]] | - | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] |

#### Battery Accessories/Monitoring Devices

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[AMETEK Prestolite Power Site Probe]] | [[Document Battery Care for Warranty Compliance]]; [[Know Battery State Before and During the Shift]]; [[Plan Battery Replacement and Budget Ahead]] | - | - | - |
| [[AMETEK Prestolite Power TruBid]] | [[Integrate the Battery with Truck and Charger Controls]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | - |
| [[AMETEK Prestolite Power WBID]] | [[Document Battery Care for Warranty Compliance]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Plan Battery Replacement and Budget Ahead]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | - |
| [[AMETEK Prestolite Power WBID Pro]] | [[Document Battery Care for Warranty Compliance]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Plan Battery Replacement and Budget Ahead]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | - |
| [[Access Control Group CellTrac]] | [[Act on Fleet Data Without Information Overload]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | - |
| [[Access Control Group CellVue]] | [[Know Battery State Before and During the Shift]] | - | - | - |
| [[Advanced Charging Technologies BATTview]] | [[Act on Fleet Data Without Information Overload]]; [[Document Battery Care for Warranty Compliance]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Plan Battery Replacement and Budget Ahead]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] |
| [[Amaron DIY Rx]] | - | - | - | - |
| [[Banner Traction Bull Battery Controller]] | - | - | - | - |
| [[Crown Battery Health Monitor]] | [[Act on Fleet Data Without Information Overload]]; [[Document Battery Care for Warranty Compliance]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Plan Battery Replacement and Budget Ahead]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | - |
| [[Deka Ready Power BDI]] | - | - | - | - |
| [[EnerSys Wi-iQ]] | [[Act on Fleet Data Without Information Overload]]; [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Document Battery Care for Warranty Compliance]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Plan Battery Replacement and Budget Ahead]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] |
| [[EnerSys iQ Mini]] | [[Act on Fleet Data Without Information Overload]]; [[Document Battery Care for Warranty Compliance]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Plan Battery Replacement and Budget Ahead]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | - |
| [[Energywith withBMS BMU]] | [[Act on Fleet Data Without Information Overload]]; [[Document Battery Care for Warranty Compliance]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Plan Battery Replacement and Budget Ahead]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | - |
| [[Exide HC-LC Logger]] | [[Document Battery Care for Warranty Compliance]]; [[Plan Battery Replacement and Budget Ahead]] | - | - | - |
| [[Exide Motion+ EasyMonitor]] | [[Act on Fleet Data Without Information Overload]]; [[Document Battery Care for Warranty Compliance]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Plan Battery Replacement and Budget Ahead]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] |
| [[Exide Opus Display]] | - | - | - | - |
| [[HOPPECKE trak collect]] | [[Act on Fleet Data Without Information Overload]]; [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Document Battery Care for Warranty Compliance]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Plan Battery Replacement and Budget Ahead]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] |
| [[HOPPECKE trak collect premium]] | - | - | - | - |
| [[Hyster Battery Tracker]] | [[Act on Fleet Data Without Information Overload]]; [[Document Battery Care for Warranty Compliance]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Plan Battery Replacement and Budget Ahead]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | - |
| [[Inventus Smart Battery Monitor SBM-01]] | [[Act on Fleet Data Without Information Overload]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Know Battery State Before and During the Shift]] | - | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] |
| [[MIDATRON BMU]] | [[Integrate the Battery with Truck and Charger Controls]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | - |
| [[Midac MB2 Battery Brain]] | - | - | - | - |
| [[Philadelphia Scientific eGO!Mini]] | [[Act on Fleet Data Without Information Overload]]; [[Document Battery Care for Warranty Compliance]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Plan Battery Replacement and Budget Ahead]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | - |
| [[Philadelphia Scientific eGO!c]] | [[Act on Fleet Data Without Information Overload]]; [[Document Battery Care for Warranty Compliance]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Plan Battery Replacement and Budget Ahead]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | - |
| [[Philadelphia Scientific eGO!core]] | [[Act on Fleet Data Without Information Overload]]; [[Document Battery Care for Warranty Compliance]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Plan Battery Replacement and Budget Ahead]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | - |
| [[Philadelphia Scientific eGO!plus]] | [[Act on Fleet Data Without Information Overload]]; [[Document Battery Care for Warranty Compliance]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Plan Battery Replacement and Budget Ahead]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | - |
| [[Philadelphia Scientific eGO!pro]] | [[Act on Fleet Data Without Information Overload]]; [[Document Battery Care for Warranty Compliance]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Plan Battery Replacement and Budget Ahead]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | - |
| [[Power Designers PowerTrac 3]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Document Battery Care for Warranty Compliance]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Plan Battery Replacement and Budget Ahead]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] |
| [[Power Designers PowerTrac DT3]] | [[Act on Fleet Data Without Information Overload]]; [[Document Battery Care for Warranty Compliance]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Plan Battery Replacement and Budget Ahead]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] |
| [[Power Designers PowerTrac Monitor]] | [[Document Battery Care for Warranty Compliance]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Plan Battery Replacement and Budget Ahead]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | - |
| [[Power Designers PowerTrac SP+]] | [[Act on Fleet Data Without Information Overload]]; [[Document Battery Care for Warranty Compliance]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Plan Battery Replacement and Budget Ahead]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] |
| [[Raymond iBattery]] | [[Act on Fleet Data Without Information Overload]]; [[Document Battery Care for Warranty Compliance]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Plan Battery Replacement and Budget Ahead]]; [[Prevent Battery Abuse and Premature Replacement]]; [[Prevent Tip-Overs and Overloads]] | - | - | - |
| [[Yale Battery Vision]] | [[Act on Fleet Data Without Information Overload]]; [[Document Battery Care for Warranty Compliance]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Plan Battery Replacement and Budget Ahead]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | - |

#### Battery Accessories/Telematics and Connectivity Devices

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Exide Retrofitting Communicator]] | [[Know Battery State Before and During the Shift]] | - | - | - |
| [[Philadelphia Scientific eGO!gateway]] | [[Document Battery Care for Warranty Compliance]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Plan Battery Replacement and Budget Ahead]] | - | - | - |

#### Battery Accessories/Water Level Monitors

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Access Control Group SMARTIE]] | [[Keep Trucks Working Without Battery Maintenance Labor]] | - | - | - |
| [[Crown Battery Acid Indicators]] | [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]] | - | - | - |
| [[Flow-Rite Eagle Eye Elite IV]] | [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]] | - | - | - |
| [[Flow-Rite Eagle Eye Essential IV]] | [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]] | - | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] |
| [[GS Yuasa LED Level Indicator]] | [[Keep Trucks Working Without Battery Maintenance Labor]] | - | - | - |
| [[Midac Electrolyte Level Sensor]] | [[Keep Trucks Working Without Battery Maintenance Labor]] | - | - | - |
| [[Philadelphia Scientific Blinky Watering Monitors]] | [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]] | - | - | - |
| [[Philadelphia Scientific SmartBlinky Pro]] | [[Act on Fleet Data Without Information Overload]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]] | - | - | - |

#### Battery Accessories/Watering Systems

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Amaron AFS System]] | - | - | - | - |
| [[Amaron Aqua Filling Plug]] | - | - | - | - |
| [[Banner Traction Bull Filling System]] | [[Keep Trucks Working Without Battery Maintenance Labor]] | - | - | - |
| [[Crown V-Force Single Point Watering System]] | [[Keep Trucks Working Without Battery Maintenance Labor]] | - | - | - |
| [[EnerSys Aquamatic Water Refilling System]] | [[Keep Trucks Working Without Battery Maintenance Labor]] | - | - | - |
| [[Exide Automatic Watering System and Level Sensor]] | [[Keep Trucks Working Without Battery Maintenance Labor]] | - | - | - |
| [[Flow-Rite Maverick Battery Watering System]] | [[Keep Trucks Working Without Battery Maintenance Labor]] | - | - | - |
| [[Leoch PzS Automatic Water Filling System]] | [[Keep Trucks Working Without Battery Maintenance Labor]] | - | - | - |
| [[Midac Aquamatic Watering System]] | [[Keep Trucks Working Without Battery Maintenance Labor]] | - | - | - |
| [[Philadelphia Scientific Stealth Watering System]] | [[Keep Trucks Working Without Battery Maintenance Labor]] | - | - | - |
| [[Philadelphia Scientific Water Injector System]] | [[Keep Trucks Working Without Battery Maintenance Labor]] | - | - | - |
| [[PosiCharge Single-Point Automatic Battery Watering]] | [[Keep Trucks Working Without Battery Maintenance Labor]] | - | - | - |

#### Charger Accessories

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[HOPPECKE trak systemizer powercube]] | - | - | - | - |
| [[HVPS Communications Kit]] | [[Connect Chargers and Batteries Safely at the Site]] | - | - | - |

#### Charger Accessories/Cable Management

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Crown Cable Management Accessories]] | [[Connect Chargers and Batteries Safely at the Site]] | - | - | - |

#### Charger Accessories/Connector Accessories

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Conductix-Wampfler Enduro+ Charging Contacts]] | [[Charge Without Anyone Plugging In]] | - | - | - |
| [[Grenzebach AGV Contact Charging Station]] | [[Charge Without Anyone Plugging In]] | - | - | - |
| [[PosiCharge Modular Charge Cables]] | [[Connect Chargers and Batteries Safely at the Site]] | - | - | - |
| [[Raymond Courier AutoCharge System]] | [[Charge Without Anyone Plugging In]] | - | - | - |
| [[Staubli QCC Quick Charging Connection]] | [[Charge Without Anyone Plugging In]] | - | - | - |
| [[Vahle Charging Contacts]] | [[Charge Without Anyone Plugging In]] | - | - | - |

#### Charger Accessories/Remote Controls and Indicators

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Crown V-HFM3 Tower Light Kit]] | [[Know Battery State Before and During the Shift]] | - | - | - |
| [[Crown V-HFM3 Wired Remote Control Kit]] | [[Monitor and Manage Chargers and Batteries Across Sites]] | - | - | - |
| [[PosiCharge Three-Color Stack Light]] | [[Know Battery State Before and During the Shift]] | - | - | - |

#### Charger Accessories/Stands and Mounting

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Crown V-HFM3 Charger Stand]] | - | - | - | - |
| [[PosiCharge Charger Stand Kit and Cable Handler]] | [[Connect Chargers and Batteries Safely at the Site]] | - | - | - |

#### Charger Accessories/Thermal Accessories

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[PosiCharge Cooling Fan Box]] | [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |

#### Chargers

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[MIDATRON HE Charger]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |
| [[MIDATRON HE-Lion Charger]] | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]] | - | - | - |
| [[MIDATRON HF Charger]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]] | - | - | - |
| [[MIDATRON HF LFPB Charger]] | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]] | - | - | - |
| [[MIDATRON MTB Charger]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]] | - | - | - |
| [[MIDATRON MTT Charger]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]] | - | - | - |

#### Chargers/Industrial Modular Chargers

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[ACT Quantum 2]] | [[Charge Without a Ventilated Battery Room]]; [[Connect Chargers and Batteries Safely at the Site]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] |
| [[ACT Quantum 3]] | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Prevent Battery Abuse and Premature Replacement]] | [[Connect Chargers and Batteries Safely at the Site]] | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] |
| [[ACT Quantum Outdoor]] | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | - |
| [[AMETEK Prestolite Power Eclipse II]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Prevent Battery Abuse and Premature Replacement]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |
| [[AMETEK Prestolite Power ULTRA]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |
| [[Crown Battery EVOLUTION Series]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Return Trucks to Service Quickly After a Low Charge]] | [[Connect Chargers and Batteries Safely at the Site]] | - | - |
| [[Crown V-HFM3 Charger]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Charge Within Site Power Limits and Utility Costs]]; [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Return Trucks to Service Quickly After a Low Charge]] | [[Connect Chargers and Batteries Safely at the Site]] | - | - |
| [[Deka PowerForce Charger]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |
| [[Delta MOOVbase Modular Charging Systems]] | [[Connect Chargers and Batteries Safely at the Site]] | - | - | - |
| [[EnerSys Express Charger]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Connect Chargers and Batteries Safely at the Site]]; [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Prevent Battery Abuse and Premature Replacement]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |
| [[EnerSys IMPAQ Charger]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Connect Chargers and Batteries Safely at the Site]]; [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Prevent Battery Abuse and Premature Replacement]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |
| [[EnerSys NexSys+ Charger]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Charge Without a Ventilated Battery Room]]; [[Connect Chargers and Batteries Safely at the Site]]; [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Prevent Battery Abuse and Premature Replacement]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |
| [[Exide 2100 HP Charger]] | [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |
| [[Exide 2100 Li High Output Charger]] | [[Charge Without a Ventilated Battery Room]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Keep Trucks Working Without Battery Maintenance Labor]] | - | - | - |
| [[Exide Element HF Charger]] | - | - | - | - |
| [[Exide Motion+ Lithium Charger]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]] | - | - | - |
| [[Fronius SelectION]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]] | [[Integrate the Battery with Truck and Charger Controls]] | - | - |
| [[Fronius Selectiva 4.0]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Monitor and Manage Chargers and Batteries Across Sites]] | - | - | - |
| [[Green Cubes SAFEFlex Charger]] | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]] | - | - | - |
| [[HOPPECKE trak charger HF premium]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]] | - | - | - |
| [[ITW GSE DC Charger]] | - | - | - | - |
| [[Linde Lithium-Ion Charger (9, 17 and 30 kW)]] | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]] | - | - | - |
| [[PosiCharge DVS100]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Prevent Battery Abuse and Premature Replacement]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |
| [[PosiCharge DVS150]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Document Battery Care for Warranty Compliance]]; [[Plan Battery Replacement and Budget Ahead]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | - |
| [[PosiCharge DVS300 Series]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |
| [[PosiCharge High Voltage Power Station (AC)]] | [[Return Trucks to Service Quickly After a Low Charge]] | [[Connect Chargers and Batteries Safely at the Site]] | - | - |
| [[PosiCharge High Voltage Power Station (DC)]] | [[Connect Chargers and Batteries Safely at the Site]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |
| [[PosiCharge MVS400 and MVS800]] | [[Connect Chargers and Batteries Safely at the Site]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |
| [[PosiCharge ProCore Edge]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Prevent Battery Abuse and Premature Replacement]]; [[Return Trucks to Service Quickly After a Low Charge]] | [[Integrate the Battery with Truck and Charger Controls]] | - | - |
| [[PosiCharge ProCore Solo]] | [[Prevent Battery Abuse and Premature Replacement]] | - | - | - |
| [[PosiCharge SVS100]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |
| [[PosiCharge SVS200]] | [[Keep Trucks Working Without Battery Maintenance Labor]] | - | - | - |
| [[Power Designers REVOLUTION X]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Prevent Battery Abuse and Premature Replacement]]; [[Return Trucks to Service Quickly After a Low Charge]] | [[Connect Chargers and Batteries Safely at the Site]] | - | - |
| [[Raymond Red Charger]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Return Trucks to Service Quickly After a Low Charge]] | [[Connect Chargers and Batteries Safely at the Site]] | - | - |
| [[Stryten EHF Charger]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]] | - | - | - |
| [[Stryten EHI Charger]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |
| [[Stryten EHY Charger]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]] | - | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] |
| [[Stryten X-3 Charger]] | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Return Trucks to Service Quickly After a Low Charge]] | [[Connect Chargers and Batteries Safely at the Site]] | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] |
| [[Stryten X-7 Charger]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Return Trucks to Service Quickly After a Low Charge]] | [[Connect Chargers and Batteries Safely at the Site]] | - | - |
| [[Triathlon Lithium-Ion Charger for UniCarriers]] | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]] | - | - | - |

#### Chargers/Light-Duty Chargers

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Delta-Q IC650]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]] | [[Integrate the Battery with Truck and Charger Controls]] | - | - |
| [[Exide Motion+ Premium Charger]] | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]] | [[Integrate the Battery with Truck and Charger Controls]] | - | - |
| [[Lester Summit Series II]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Monitor and Manage Chargers and Batteries Across Sites]] | [[Integrate the Battery with Truck and Charger Controls]] | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] |

#### Chargers/On-board Chargers

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Delta MOOVon Onboard Charger and Converters]] | [[Retrofit Safety and Telematics Onto Existing Trucks]] | [[Charge Without a Ventilated Battery Room]] | - | - |
| [[EnerSys NexSys COMpact Charger]] | - | - | - | - |
| [[Heli Built-In Lithium Charger]] | [[Charge Without a Ventilated Battery Room]] | - | - | - |
| [[Hyster Onboard Charging Solution]] | [[Charge Without a Ventilated Battery Room]] | - | - | - |
| [[Stryten AGM220 Onboard Charger]] | [[Know Battery State Before and During the Shift]] | - | - | - |

#### Chargers/Wireless Chargers

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Daihen D-Broad Wireless Charging System]] | [[Charge Without Anyone Plugging In]] | [[Connect Chargers and Batteries Safely at the Site]]; [[Integrate the Battery with Truck and Charger Controls]] | - | - |
| [[Delta MOOVair Wireless Charging Series]] | [[Charge Without Anyone Plugging In]]; [[Integrate the Battery with Truck and Charger Controls]] | [[Connect Chargers and Batteries Safely at the Site]] | - | - |
| [[EnerSys NexSys AIR Wireless Charger]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Charge Without Anyone Plugging In]]; [[Charge Without a Ventilated Battery Room]]; [[Connect Chargers and Batteries Safely at the Site]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Prevent Battery Abuse and Premature Replacement]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |
| [[Lindig L.inductive Charging Offer]] | [[Charge Without Anyone Plugging In]] | [[Connect Chargers and Batteries Safely at the Site]]; [[Integrate the Battery with Truck and Charger Controls]] | - | - |
| [[Resonant Link Wireless Lift Truck Charger]] | [[Charge Without Anyone Plugging In]]; [[Connect Chargers and Batteries Safely at the Site]] | [[Integrate the Battery with Truck and Charger Controls]] | - | - |
| [[WiBotic 1kW Wireless Charging System]] | [[Charge Without Anyone Plugging In]] | [[Connect Chargers and Batteries Safely at the Site]]; [[Integrate the Battery with Truck and Charger Controls]] | - | - |
| [[Wiferion CW1000 Wireless Charging System]] | [[Charge Without Anyone Plugging In]] | [[Connect Chargers and Batteries Safely at the Site]]; [[Integrate the Battery with Truck and Charger Controls]] | - | - |
| [[Wiferion etaLINK 12000 Wireless Charging System]] | [[Charge Without Anyone Plugging In]] | [[Connect Chargers and Batteries Safely at the Site]]; [[Integrate the Battery with Truck and Charger Controls]] | - | - |
| [[Wiferion etaLINK 3000 Wireless Charging System]] | [[Charge Without Anyone Plugging In]] | [[Connect Chargers and Batteries Safely at the Site]]; [[Integrate the Battery with Truck and Charger Controls]] | - | - |
| [[Xnergy Wireless Charging Series]] | [[Charge Without Anyone Plugging In]] | [[Connect Chargers and Batteries Safely at the Site]]; [[Integrate the Battery with Truck and Charger Controls]] | - | - |

#### Fleet Software and Platforms

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Ampcontrol Yard Management for Electric Vehicles]] | [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |
| [[Blue Yonder Warehouse Execution]] | [[Right-Size the Fleet from Usage Data]] | - | - | - |
| [[Crown Service Request App]] | - | - | - | - |
| [[FleetRabbit]] | [[Act on Fleet Data Without Information Overload]]; [[Right-Size the Fleet from Usage Data]] | - | - | - |
| [[Flip Turn Energy Management]] | [[Charge Within Site Power Limits and Utility Costs]] | - | - | - |
| [[MiR Fleet]] | [[Act on Fleet Data Without Information Overload]]; [[Right-Size the Fleet from Usage Data]] | - | - | - |
| [[OTTO Fleet Manager]] | [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Return Trucks to Service Quickly After a Low Charge]]; [[Right-Size the Fleet from Usage Data]] | - | - | - |
| [[Phantom Auto Remote Operation Software]] | - | - | - | - |
| [[PowerFlex X]] | [[Charge Within Site Power Limits and Utility Costs]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |
| [[Seegrid Auto Charge]] | [[Charge Without Anyone Plugging In]] | - | - | - |
| [[Seegrid Fleet Central]] | [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Return Trucks to Service Quickly After a Low Charge]]; [[Right-Size the Fleet from Usage Data]] | - | - | - |
| [[Siemens depotfinity]] | [[Charge Within Site Power Limits and Utility Costs]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |
| [[WiBotic Commander]] | [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |

#### Fleet Software and Platforms/Battery and Charger Management

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[ACT ACTenergy]] | [[Charge Within Site Power Limits and Utility Costs]] | - | - | - |
| [[ACT ACTview]] | [[Monitor and Manage Chargers and Batteries Across Sites]] | - | - | - |
| [[Concentric PowerHIVE]] | [[Charge Without Anyone Plugging In]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |
| [[EnerSys BSI40]] | [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |
| [[EnerSys EZSelect Lite]] | [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |
| [[EnerSys EnSite]] | [[Right-Size the Fleet from Usage Data]] | - | - | - |
| [[EnerSys LifeNetwork iQ]] | [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |
| [[Exide BattID]] | - | - | - | - |
| [[Exide GNB Fleet]] | [[Act on Fleet Data Without Information Overload]]; [[Document Battery Care for Warranty Compliance]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Plan Battery Replacement and Budget Ahead]] | - | - | - |
| [[Fronius Charge & Connect]] | [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]] | - | - | - |
| [[Fronius PV Connect]] | [[Charge Within Site Power Limits and Utility Costs]] | - | - | - |
| [[HOPPECKE trak monitor 4.0]] | - | - | - | - |
| [[Jungheinrich Active Load Management]] | [[Charge Within Site Power Limits and Utility Costs]] | [[Connect Chargers and Batteries Safely at the Site]] | - | - |
| [[Linde connect charger]] | [[Charge Within Site Power Limits and Utility Costs]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]] | [[Connect Chargers and Batteries Safely at the Site]] | - | - |
| [[Midac Mobile App]] | [[Monitor and Manage Chargers and Batteries Across Sites]] | - | - | - |
| [[Midac Service Tool]] | [[Document Battery Care for Warranty Compliance]] | - | - | - |
| [[Philadelphia Scientific iBOS]] | - | - | - | - |
| [[PosiCharge E-Meter]] | [[Document Battery Care for Warranty Compliance]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Plan Battery Replacement and Budget Ahead]] | - | - | - |
| [[PosiCharge PosiConnect]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]] | - | - | - |
| [[PosiCharge PosiLink]] | [[Document Battery Care for Warranty Compliance]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Plan Battery Replacement and Budget Ahead]] | - | - | - |
| [[PosiCharge PosiNet]] | [[Document Battery Care for Warranty Compliance]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Plan Battery Replacement and Budget Ahead]] | - | - | - |
| [[PosiCharge SkyLink]] | [[Monitor and Manage Chargers and Batteries Across Sites]] | - | - | - |
| [[Raymond Energy Asset Manager]] | [[Document Battery Care for Warranty Compliance]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Plan Battery Replacement and Budget Ahead]] | - | - | - |
| [[Stryten inCOMMAND]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Integrate the Battery with Truck and Charger Controls]] | - | - | - |
| [[Toyota Peak Load Management]] | [[Charge Within Site Power Limits and Utility Costs]] | [[Connect Chargers and Batteries Safely at the Site]] | - | - |

#### Fleet Software and Platforms/Truck Telematics

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Adveez Asset and Operations Monitoring System]] | [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Right-Size the Fleet from Usage Data]] | - | - | - |
| [[CLARK SMART Telematics]] | [[Control Who Operates Each Truck]]; [[Detect and Learn from Truck Impacts]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Right-Size the Fleet from Usage Data]] | - | - | - |
| [[Cat VISR]] | [[Control Who Operates Each Truck]]; [[Detect and Learn from Truck Impacts]]; [[Keep Trucks Slow in Hazardous Zones]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Right-Size the Fleet from Usage Data]] | [[Protect Aircraft and Ground Crew During Ground Operations]] | - | - |
| [[Crown InfoLink]] | [[Control Who Operates Each Truck]]; [[Detect and Learn from Truck Impacts]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Right-Size the Fleet from Usage Data]] | - | - | - |
| [[Doosan Lin-Q]] | [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Right-Size the Fleet from Usage Data]] | - | - | - |
| [[ELOKON ELOfleet]] | [[Control Who Operates Each Truck]]; [[Detect and Learn from Truck Impacts]]; [[Keep Trucks Slow in Hazardous Zones]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Right-Size the Fleet from Usage Data]] | [[Protect Aircraft and Ground Crew During Ground Operations]] | - | - |
| [[Hangcha FIMS]] | [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Right-Size the Fleet from Usage Data]] | - | - | - |
| [[Heli Fleet Management System]] | [[Find and Fix Vehicle Faults Without Downtime]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Right-Size the Fleet from Usage Data]] | - | - | - |
| [[Hyster Tracker Telemetry]] | [[Control Who Operates Each Truck]]; [[Detect and Learn from Truck Impacts]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Right-Size the Fleet from Usage Data]] | - | - | - |
| [[Jungheinrich ISM Online]] | [[Control Who Operates Each Truck]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Right-Size the Fleet from Usage Data]] | - | - | - |
| [[Komatsu KOMTRAX]] | [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Right-Size the Fleet from Usage Data]] | - | - | - |
| [[Linde connect]] | [[Control Who Operates Each Truck]]; [[Detect and Learn from Truck Impacts]]; [[Find and Fix Vehicle Faults Without Downtime]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Right-Size the Fleet from Usage Data]] | [[Protect Aircraft and Ground Crew During Ground Operations]] | - | - |
| [[Logisnext Lift Link]] | [[Control Who Operates Each Truck]]; [[Detect and Learn from Truck Impacts]]; [[Keep Trucks Slow in Hazardous Zones]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Right-Size the Fleet from Usage Data]] | [[Protect Aircraft and Ground Crew During Ground Operations]] | - | - |
| [[Oshkosh AeroTech iOPS]] | [[Find and Fix Vehicle Faults Without Downtime]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Right-Size the Fleet from Usage Data]] | - | - | - |
| [[Powerfleet Forklift Gateway]] | [[Control Who Operates Each Truck]]; [[Detect and Learn from Truck Impacts]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Right-Size the Fleet from Usage Data]]; [[Warn the Operator of People and Objects Near the Truck]] | [[Protect Aircraft and Ground Crew During Ground Operations]] | - | - |
| [[Raymond Power Source Integrated]] | - | - | - | - |
| [[Raymond iWAREHOUSE]] | [[Detect and Learn from Truck Impacts]]; [[Plan Battery Replacement and Budget Ahead]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Right-Size the Fleet from Usage Data]] | - | - | - |
| [[Raymond iWAREHOUSE GATEWAY]] | - | - | - | - |
| [[Raymond iWAREHOUSE Real-Time Location System]] | [[Keep Trucks Slow in Hazardous Zones]] | - | - | - |
| [[STILL FleetManager]] | [[Control Who Operates Each Truck]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Right-Size the Fleet from Usage Data]] | - | - | - |
| [[STILL Smart Portal]] | [[Control Who Operates Each Truck]]; [[Detect and Learn from Truck Impacts]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Right-Size the Fleet from Usage Data]] | - | - | - |
| [[STILL neXXt fleet]] | [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Right-Size the Fleet from Usage Data]] | - | - | - |
| [[Toyota MyInsights Telematics]] | [[Detect and Learn from Truck Impacts]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Right-Size the Fleet from Usage Data]] | [[Protect Aircraft and Ground Crew During Ground Operations]] | - | - |
| [[Yale Vision Telemetry]] | [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Right-Size the Fleet from Usage Data]] | - | - | - |

#### Forklifts

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Mitsubishi EDR Reach Trucks (Americas Listing)]] | - | - | - | - |
| [[Mitsubishi FB25-55N Electric Pneumatic Forklifts (Americas Listing)]] | - | - | - | - |
| [[Mitsubishi FG and FD Internal Combustion Forklifts (Americas Listing)]] | - | - | - | - |
| [[Mitsubishi Warehouse Trucks (Americas Listing)]] | - | - | - | - |
| [[Rocla ART Automated Reach Truck]] | - | - | - | - |
| [[Rocla AWT Automated Counterbalance Truck]] | - | - | - | - |
| [[UniCarriers Nomad AF30-AF50 LP and Dual-Fuel Forklifts]] | - | - | - | - |

#### Forklifts/Class I Electric Rider Trucks

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Cat 2EPC5000-2EP6500 Electric Pneumatic Tire Lift Trucks]] | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Keep Trucks Slow in Hazardous Zones]]; [[Keep the Operator Positioned and Able to See the Work]] | - | - | - |
| [[Cat EP14-20 Electric Counterbalance Forklifts]] | - | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Keep the Operator Positioned and Able to See the Work]]; [[Keep the Truck Under Control on Slopes, Slippery Floors and in Emergencies]]; [[Prevent Tip-Overs and Overloads]]; [[Return Trucks to Service Quickly After a Low Charge]] | - |
| [[Cat EP25-55 80 V Electric Counterbalance Forklifts]] | - | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Prevent Tip-Overs and Overloads]]; [[Return Trucks to Service Quickly After a Low Charge]]; [[Warn Pedestrians of an Approaching Truck]] | - |
| [[Cat Electric Lift Trucks (North America Series List)]] | - | - | - | - |
| [[Crown FC 5700 Series]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Keep the Truck Under Control on Slopes, Slippery Floors and in Emergencies]]; [[Prevent Tip-Overs and Overloads]] | - | [[Control Who Operates Each Truck]]; [[Detect and Learn from Truck Impacts]]; [[Know Battery State Before and During the Shift]]; [[Prevent Battery Abuse and Premature Replacement]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Right-Size the Fleet from Usage Data]] | - |
| [[Crown RC 5700 Series]] | [[Control Who Operates Each Truck]]; [[Find and Fix Vehicle Faults Without Downtime]]; [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Keep Trucks Slow in Hazardous Zones]]; [[Keep the Truck Under Control on Slopes, Slippery Floors and in Emergencies]]; [[Know Battery State Before and During the Shift]]; [[Prevent Battery Abuse and Premature Replacement]]; [[Prevent Tip-Overs and Overloads]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Stretch Truck Run Time per Charge]]; [[Warn Pedestrians of an Approaching Truck]] | - | [[Detect and Learn from Truck Impacts]]; [[Right-Size the Fleet from Usage Data]] | - |
| [[Crown SC Series]] | - | - | - | - |
| [[Doosan Bobcat 7-Series Plus Electric Forklifts]] | [[Keep the Operator Positioned and Able to See the Work]]; [[Keep the Truck Under Control on Slopes, Slippery Floors and in Emergencies]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | [[Keep Trucks Slow in Hazardous Zones]]; [[Prevent Tip-Overs and Overloads]] | - |
| [[Doosan Bobcat NXE Series Electric Forklifts]] | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Keep the Truck Under Control on Slopes, Slippery Floors and in Emergencies]]; [[Prevent Tip-Overs and Overloads]] | - | - | - |
| [[Hangcha A Series Electric Forklifts]] | [[Find and Fix Vehicle Faults Without Downtime]]; [[Handle Loads Without Damaging Them]]; [[Return Trucks to Service Quickly After a Low Charge]]; [[Warn Pedestrians of an Approaching Truck]] | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] | - |
| [[Hangcha XC Series Electric Forklifts]] | [[Control Who Operates Each Truck]]; [[Handle Loads Without Damaging Them]]; [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Keep the Operator Positioned and Able to See the Work]]; [[Keep the Truck Under Control on Slopes, Slippery Floors and in Emergencies]]; [[Prevent Tip-Overs and Overloads]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | [[Right-Size the Fleet from Usage Data]] | - |
| [[Heli A3 Series Lithium Forklifts]] | [[Charge Without a Ventilated Battery Room]]; [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] | - | [[Keep the Operator Positioned and Able to See the Work]] | - |
| [[Heli G Series Lithium Forklifts]] | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Keep the Truck Under Control on Slopes, Slippery Floors and in Emergencies]]; [[Prevent Tip-Overs and Overloads]] | - | - | - |
| [[Hyster J1.5-3.0UT(L)]] | [[Stretch Truck Run Time per Charge]] | - | - | - |
| [[Hyster J2.2-3.5XN Electric Forklifts]] | - | - | - | - |
| [[Hyster J2.5-3.0XNL Integrated Lithium-Ion Forklifts]] | - | - | - | - |
| [[Komatsu FB Series Electric Forklifts]] | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Keep Trucks Slow in Hazardous Zones]]; [[Keep the Truck Under Control on Slopes, Slippery Floors and in Emergencies]] | - | [[Find and Fix Vehicle Faults Without Downtime]]; [[Keep the Operator Positioned and Able to See the Work]]; [[Prevent Tip-Overs and Overloads]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Right-Size the Fleet from Usage Data]] | - |
| [[Linde 1293 Series (E20BHP and E25BHP)]] | - | - | - | - |
| [[Linde 6-8 t Electric Counterbalance Forklifts]] | [[Know Battery State Before and During the Shift]] | - | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]] | [[Return Trucks to Service Quickly After a Low Charge]] |
| [[Linde E Series Electric Counterbalance Forklifts]] | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Keep the Truck Under Control on Slopes, Slippery Floors and in Emergencies]] | - | - | - |
| [[Linde Ei Series]] | - | [[Charge Without a Ventilated Battery Room]] | - | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]] |
| [[Mitsubishi FB 3-Wheel Electric Forklifts]] | [[Reduce Operator Effort and Fatigue]] | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - |
| [[Mitsubishi FBC Cushion Tire Electric Forklifts]] | [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Mitsubishi FBC20Q-FBC40Q Electric Cushion Forklifts]] | - | - | - | - |
| [[Mitsubishi FBCS Stand-Up Counterbalanced Forklifts]] | [[Keep the Operator Positioned and Able to See the Work]]; [[Reduce Operator Effort and Fatigue]] | - | - | - |
| [[Raymond 4000 Series Counterbalanced Trucks]] | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Keep the Operator Positioned and Able to See the Work]] | - | [[Keep Trucks Slow in Hazardous Zones]]; [[Prevent Tip-Overs and Overloads]]; [[Return Trucks to Service Quickly After a Low Charge]] | - |
| [[STILL RX 20 Electric Forklift]] | - | [[Charge Without a Ventilated Battery Room]] | - | - |
| [[STILL RX 60 Electric Forklift]] | [[Control Who Operates Each Truck]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] | - | [[Keep the Operator Positioned and Able to See the Work]]; [[Prevent Tip-Overs and Overloads]]; [[Right-Size the Fleet from Usage Data]]; [[Warn Pedestrians of an Approaching Truck]] | - |
| [[Toyota 3-Wheel Electric Forklift]] | [[Find and Fix Vehicle Faults Without Downtime]] | - | [[Detect and Learn from Truck Impacts]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Return Trucks to Service Quickly After a Low Charge]]; [[Right-Size the Fleet from Usage Data]] | - |
| [[Toyota 7FBCU35-55 Electric Pneumatic Forklifts]] | - | - | - | - |
| [[Toyota Traigo48]] | [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |
| [[UniCarriers MX2 and MXL Series]] | [[Prevent Tip-Overs and Overloads]] | - | [[Control Who Operates Each Truck]]; [[Detect and Learn from Truck Impacts]]; [[Keep Trucks Slow in Hazardous Zones]]; [[Keep the Operator Positioned and Able to See the Work]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Right-Size the Fleet from Usage Data]]; [[Warn Pedestrians of an Approaching Truck]] | - |
| [[UniCarriers SCX N2 Stand-Up Counterbalanced Forklifts]] | [[Prevent Tip-Overs and Overloads]] | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Keep the Operator Positioned and Able to See the Work]]; [[Warn Pedestrians of an Approaching Truck]] | - |
| [[Yale ERC045-070VG Electric Forklifts]] | - | - | - | - |
| [[Yale ERC050-060VGL]] | [[Act on Fleet Data Without Information Overload]]; [[Charge Without a Ventilated Battery Room]]; [[Know Battery State Before and During the Shift]] | - | [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Right-Size the Fleet from Usage Data]] | [[Keep Trucks Working Without Battery Maintenance Labor]] |
| [[Yale ERC080VHL]] | [[Stretch Truck Run Time per Charge]] | - | [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Right-Size the Fleet from Usage Data]] | - |

#### Forklifts/Class II Electric Narrow Aisle Trucks

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Crown RM-RMD 6000 Series]] | - | - | - | - |
| [[Crown RR-RD 5700 Series]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Keep the Operator Positioned and Able to See the Work]]; [[Keep the Truck Under Control on Slopes, Slippery Floors and in Emergencies]]; [[Prevent Tip-Overs and Overloads]] | - | - | - |
| [[Jungheinrich ETV C16 and C20]] | - | - | - | - |
| [[Raymond 7000 Series Reach-Fork Trucks]] | [[Stretch Truck Run Time per Charge]] | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Keep Trucks Slow in Hazardous Zones]]; [[Keep the Operator Positioned and Able to See the Work]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - |
| [[Raymond Orderpickers]] | - | - | [[Keep Trucks Slow in Hazardous Zones]]; [[Keep the Operator Positioned and Able to See the Work]]; [[Prevent Tip-Overs and Overloads]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - |

#### Forklifts/Class III Electric Hand and Hand-Rider Trucks

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Raymond 8000 Series Pallet Trucks]] | [[Control Who Operates Each Truck]]; [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] | [[Charge Without a Ventilated Battery Room]] | [[Know Battery State Before and During the Shift]]; [[Prevent Battery Abuse and Premature Replacement]]; [[Return Trucks to Service Quickly After a Low Charge]] | - |
| [[STILL EXH-SF Low Lift Pallet Truck]] | [[Control Who Operates Each Truck]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] | [[Charge Without a Ventilated Battery Room]] | [[Detect and Learn from Truck Impacts]]; [[Prevent Tip-Overs and Overloads]]; [[Right-Size the Fleet from Usage Data]] | - |

#### Fuel Cell Power Units/Hydrogen Fuel Cell Units

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Nuvera PowerEdge]] | [[Return Trucks to Service Quickly After a Low Charge]]; [[Stretch Truck Run Time per Charge]] | - | - | - |
| [[Plug Power GenDrive]] | [[Know Battery State Before and During the Shift]]; [[Return Trucks to Service Quickly After a Low Charge]]; [[Stretch Truck Run Time per Charge]] | - | - | - |

#### Ground Support Equipment/Baggage and Tow Tractors

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Charlatte CBT350 AC Tow Tractor]] | - | - | - | - |
| [[Charlatte T135 Neo 25T]] | [[Stretch Truck Run Time per Charge]] | - | - | - |
| [[Charlatte T137-V3]] | - | - | - | - |
| [[Linde P250 Electric Baggage Tractor]] | - | - | - | - |
| [[Oshkosh AeroTech B80E Electric Baggage Tractor]] | - | - | - | - |
| [[TUG Endurance Baggage Tractor]] | [[Find and Fix Vehicle Faults Without Downtime]]; [[Stretch Truck Run Time per Charge]] | [[Keep the Truck Under Control on Slopes, Slippery Floors and in Emergencies]] | - | - |

#### Ground Support Equipment/Belt Loaders

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Charlatte Belt Loaders]] | - | [[Charge Without a Ventilated Battery Room]] | - | - |
| [[Mallaghan SkyBelt]] | [[Find and Fix Vehicle Faults Without Downtime]] | - | [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Right-Size the Fleet from Usage Data]]; [[Warn the Operator of People and Objects Near the Truck]] | - |
| [[TLD NBL-E Belt Loader]] | - | - | [[Detect and Learn from Truck Impacts]]; [[Keep Trucks Slow in Hazardous Zones]]; [[Protect Aircraft and Ground Crew During Ground Operations]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - |
| [[TLD RBL Electric Regional Belt Loader]] | - | - | [[Detect and Learn from Truck Impacts]]; [[Keep Trucks Slow in Hazardous Zones]]; [[Protect Aircraft and Ground Crew During Ground Operations]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - |
| [[TUG 660 Belt Loader]] | [[Stretch Truck Run Time per Charge]] | - | [[Keep Trucks Slow in Hazardous Zones]]; [[Keep the Operator Positioned and Able to See the Work]]; [[Protect Aircraft and Ground Crew During Ground Operations]]; [[Warn the Operator of People and Objects Near the Truck]] | - |

#### Ground Support Equipment/Cargo Loaders

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Oshkosh AeroTech Commander 30i Cargo Loader]] | - | - | [[Find and Fix Vehicle Faults Without Downtime]]; [[Keep the Operator Positioned and Able to See the Work]]; [[Protect Aircraft and Ground Crew During Ground Operations]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Right-Size the Fleet from Usage Data]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - |
| [[Oshkosh AeroTech Ranger 15E Cargo Loader]] | - | - | [[Protect Aircraft and Ground Crew During Ground Operations]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - |

#### Ground Support Equipment/Pushback Tractors

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Charlatte CPB35E Pushback Tractor]] | - | - | - | - |
| [[Oshkosh AeroTech Pushback B350E and B650E]] | - | - | - | - |
| [[TUG ALPHA 1 Pushback]] | [[Find and Fix Vehicle Faults Without Downtime]]; [[Know Battery State Before and During the Shift]]; [[Prevent Battery Abuse and Premature Replacement]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | - |

#### Vehicle Accessories/Access Control

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Panacea Smart Start]] | [[Control Who Operates Each Truck]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] | - | - | - |
| [[Raymond PIN Code Pad]] | [[Control Who Operates Each Truck]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] | - | - | - |
| [[Toyota PIN Code Access Pad]] | [[Control Who Operates Each Truck]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] | - | - | - |

#### Vehicle Accessories/Cameras and Recorders

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Hangcha Backup Camera Option]] | [[Keep the Operator Positioned and Able to See the Work]] | - | - | - |
| [[Jungheinrich addedVIEW Camera Systems]] | [[Keep the Operator Positioned and Able to See the Work]] | - | - | - |
| [[Panacea Cam-DVR with Impact Sensors]] | [[Detect and Learn from Truck Impacts]]; [[Keep the Operator Positioned and Able to See the Work]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] | [[Protect Aircraft and Ground Crew During Ground Operations]] | - | - |
| [[Raymond Vantage Point System]] | [[Keep the Operator Positioned and Able to See the Work]] | - | - | - |
| [[Toyota 360 Operating Camera]] | [[Keep the Operator Positioned and Able to See the Work]] | - | - | - |
| [[Toyota Carriage-Mounted Camera]] | [[Keep the Operator Positioned and Able to See the Work]] | - | - | - |
| [[Toyota Twistlock Snapshot Camera System]] | [[Detect and Learn from Truck Impacts]] | - | - | - |

#### Vehicle Accessories/Cold Storage Packages

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Mitsubishi Cold Storage Modification]] | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] | - | - | - |
| [[Raymond ThermaKit]] | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] | - | - | - |
| [[Toyota Cold Conditioning Package]] | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] | - | - | - |
| [[UniCarriers Freezer Option]] | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] | - | - | - |

#### Vehicle Accessories/Operator Assist and Stability

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Cat Intelligent Speed and Movement Reduction]] | [[Prevent Tip-Overs and Overloads]] | - | - | - |
| [[Cat Presence Detection System]] | [[Keep the Operator Positioned and Able to See the Work]]; [[Keep the Truck Under Control on Slopes, Slippery Floors and in Emergencies]] | - | - | - |
| [[Crown Capacity Data Monitor]] | [[Prevent Tip-Overs and Overloads]] | - | - | - |
| [[Doosan Bobcat Mast Sway Control]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Prevent Tip-Overs and Overloads]] | - | - | - |
| [[Heli Operator Presence Sensing System]] | [[Keep the Operator Positioned and Able to See the Work]] | - | - | - |
| [[Hyster Dynamic Stability System]] | [[Prevent Tip-Overs and Overloads]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Jungheinrich curveCONTROL]] | [[Prevent Tip-Overs and Overloads]] | - | - | - |
| [[Komatsu Digital Load Scale]] | [[Prevent Tip-Overs and Overloads]] | - | - | - |
| [[Komatsu Operator Presence Sensing System]] | [[Find and Fix Vehicle Faults Without Downtime]]; [[Keep the Operator Positioned and Able to See the Work]] | - | - | - |
| [[Linde Dynamic Mast Control]] | [[Prevent Tip-Overs and Overloads]] | - | - | - |
| [[Linde Load Management Advanced]] | [[Prevent Tip-Overs and Overloads]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Linde Safety Pilot]] | [[Prevent Tip-Overs and Overloads]] | - | - | - |
| [[Linde System Control]] | [[Prevent Tip-Overs and Overloads]] | - | - | - |
| [[Mitsubishi Integrated Presence System]] | [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Oshkosh AeroTech APD Wheel Position Sensor]] | [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Oshkosh AeroTech JetDock]] | [[Protect Aircraft and Ground Crew During Ground Operations]] | - | - | - |
| [[Oshkosh AeroTech Powered Handrail with Distance Sensor]] | [[Protect Aircraft and Ground Crew During Ground Operations]] | - | - | - |
| [[RCT Muirhead Forklift Speed Limiter Kits]] | [[Keep Trucks Slow in Hazardous Zones]] | - | - | - |
| [[Raymond Auto-Locking Pallet Clamp]] | - | - | - | - |
| [[Raymond Fork Tilt Leveling]] | [[Keep the Operator Positioned and Able to See the Work]] | - | - | - |
| [[Raymond Fork-Tip Laser Guide]] | [[Keep the Operator Positioned and Able to See the Work]] | - | - | - |
| [[Raymond Intelliguide Wire Guidance]] | - | - | - | - |
| [[Raymond Intellispeed System]] | [[Prevent Tip-Overs and Overloads]] | - | - | - |
| [[Raymond Load Weight Display]] | [[Prevent Tip-Overs and Overloads]] | - | - | - |
| [[Raymond Mast Lift Limit Switch with Bypass]] | [[Prevent Tip-Overs and Overloads]] | - | - | - |
| [[Raymond Operator Compartment Sensor System]] | [[Keep the Operator Positioned and Able to See the Work]] | - | - | - |
| [[Raymond Slope Sensing]] | - | - | - | - |
| [[Raymond Travel Speed Control]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Prevent Tip-Overs and Overloads]] | - | - | - |
| [[Raymond Zoning and Positioning]] | [[Keep Trucks Slow in Hazardous Zones]] | - | - | - |
| [[Raymond iWAREHOUSE Integrated Tether System]] | [[Keep the Operator Positioned and Able to See the Work]] | - | - | - |
| [[STILL Curve Speed Control]] | [[Prevent Tip-Overs and Overloads]] | - | - | - |
| [[STILL Safety Assist]] | [[Control Who Operates Each Truck]]; [[Keep Trucks Slow in Hazardous Zones]]; [[Prevent Tip-Overs and Overloads]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Warn Pedestrians of an Approaching Truck]] | - | - | - |
| [[STILL Safety Packages]] | [[Keep the Operator Positioned and Able to See the Work]]; [[Prevent Tip-Overs and Overloads]]; [[Warn Pedestrians of an Approaching Truck]] | - | - | - |
| [[TLD ASD+ Assisted Docking]] | [[Protect Aircraft and Ground Crew During Ground Operations]] | - | - | - |
| [[Toyota Acu-Laser]] | [[Keep the Operator Positioned and Able to See the Work]] | - | - | - |
| [[Toyota Assist]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Keep the Operator Positioned and Able to See the Work]]; [[Prevent Tip-Overs and Overloads]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | [[Stretch Truck Run Time per Charge]] | - | - |
| [[Toyota Auto Height Select]] | [[Keep the Operator Positioned and Able to See the Work]] | - | - | - |
| [[Toyota Compartment Sensing System]] | [[Keep the Operator Positioned and Able to See the Work]] | - | - | - |
| [[Toyota Load Weight Sensing]] | [[Prevent Tip-Overs and Overloads]] | - | - | - |
| [[Toyota System of Active Stability]] | [[Prevent Tip-Overs and Overloads]] | - | - | - |
| [[UniCarriers Curve Control]] | [[Prevent Tip-Overs and Overloads]] | - | - | - |
| [[Yale Reliant Portfolio]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Prevent Tip-Overs and Overloads]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |

#### Vehicle Accessories/Operator Convenience

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Cat Panel Cabin Options]] | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] | - | - | - |
| [[Jungheinrich easyPILOT]] | [[Reduce Operator Effort and Fatigue]] | - | - | - |
| [[Linde Rotating Operator Workstation]] | [[Keep the Operator Positioned and Able to See the Work]] | - | - | - |
| [[Linde Smartphone Holder]] | - | - | - | - |
| [[Raymond Accessory Bar]] | - | - | - | - |
| [[Raymond Extreme Environment Protection]] | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] | - | - | - |
| [[Raymond Large Storage Tote]] | - | - | - | - |
| [[Raymond Light and Fan Package]] | [[Keep the Operator Positioned and Able to See the Work]] | - | - | - |
| [[Raymond Secondary Control Handle]] | - | - | - | - |
| [[STILL EasyBelt]] | [[Prevent Tip-Overs and Overloads]] | - | - | - |
| [[UniCarriers In-Cab Accessories]] | - | - | - | - |

#### Vehicle Accessories/Operator Displays

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Crown Gena Operating System]] | [[Find and Fix Vehicle Faults Without Downtime]]; [[Keep the Truck Under Control on Slopes, Slippery Floors and in Emergencies]]; [[Know Battery State Before and During the Shift]] | - | - | - |
| [[Crown InfoLink 7-inch Touch Display]] | [[Control Who Operates Each Truck]]; [[Detect and Learn from Truck Impacts]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[EnerSys Truck iQ]] | [[Act on Fleet Data Without Information Overload]]; [[Know Battery State Before and During the Shift]] | - | - | - |
| [[Linde MT18 Multifunction Display]] | [[Find and Fix Vehicle Faults Without Downtime]]; [[Know Battery State Before and During the Shift]] | - | - | - |
| [[Raymond Height-Tilt Indicator]] | [[Keep the Operator Positioned and Able to See the Work]] | - | - | - |

#### Vehicle Accessories/Power Source Interfaces

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Hyster Power Cellect]] | [[Integrate the Battery with Truck and Charger Controls]]; [[Know Battery State Before and During the Shift]]; [[Prevent Battery Abuse and Premature Replacement]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Right-Size the Fleet from Usage Data]] | - | - | - |
| [[PosiCharge DIY Fast Charge Kit]] | - | - | - | - |
| [[Purkeys Trailer Auxiliary Power System]] | - | - | - | - |
| [[Raymond Right-Hand Battery Rollout]] | [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |

#### Vehicle Accessories/Proximity and Object Detection

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Blaxtair Pedestrian Detection System]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Crown ProximityAssist System]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Doosan Bobcat Pedestrian Detection Camera]] | [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Hyster Pedestrian Awareness Camera]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Hyster Reaction]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Prevent Tip-Overs and Overloads]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[IRIS 860 Sensor Pack]] | [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Jungheinrich Pedestrian Detection System]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Jungheinrich Reverse Area Warning System]] | [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Jungheinrich zoneCONTROL]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Linde Motion Detection]] | [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Linde Safety Guard]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Linde Safety Guard Truck Unit]] | [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | [[Keep Trucks Slow in Hazardous Zones]] | - | - |
| [[Linde Safety Guard Zone Marker]] | [[Keep Trucks Slow in Hazardous Zones]] | - | - | - |
| [[Litum PathAware]] | [[Control Who Operates Each Truck]]; [[Keep Trucks Slow in Hazardous Zones]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Right-Size the Fleet from Usage Data]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Mallaghan Collision Avoidance System]] | [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Oshkosh AeroTech APD Engine Cowling Sensors]] | [[Protect Aircraft and Ground Crew During Ground Operations]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Oshkosh AeroTech APD Forward Radar and Controller]] | [[Protect Aircraft and Ground Crew During Ground Operations]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Oshkosh AeroTech APD Pressure-Sensitive Front Bumper]] | [[Protect Aircraft and Ground Crew During Ground Operations]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Oshkosh AeroTech APD Wing and Fairing Sensors]] | [[Protect Aircraft and Ground Crew During Ground Operations]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Oshkosh AeroTech Aircraft Proximity Detection]] | [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Powerfleet Pedestrian Proximity Detection]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Right-Size the Fleet from Usage Data]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Raymond In-Aisle Detection System]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Raymond iWAREHOUSE Fieldsense]] | [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Raymond iWAREHOUSE ObjectSense]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[TLD Aircraft Safety Docking]] | [[Detect and Learn from Truck Impacts]]; [[Keep Trucks Slow in Hazardous Zones]]; [[Protect Aircraft and Ground Crew During Ground Operations]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Textron Smart Sense]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Keep the Operator Positioned and Able to See the Work]]; [[Protect Aircraft and Ground Crew During Ground Operations]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Toyota Object Detection Radar]] | [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Toyota SEnS Pedestrian Detection]] | [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Toyota SEnS+ Pedestrian and Object Detection]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |

#### Vehicle Accessories/Warning Lights and Alerts

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Cat Safety Lighting Options]] | [[Warn Pedestrians of an Approaching Truck]] | - | - | - |
| [[Larson Explosion-Proof Blue LED Forklift Light]] | [[Warn Pedestrians of an Approaching Truck]] | - | - | - |
| [[Liftow Big Blue Pedestrian Warning Spotlight]] | [[Warn Pedestrians of an Approaching Truck]] | - | - | - |
| [[Liftow Safe-Lite Pedestrian Warning Spotlight]] | [[Warn Pedestrians of an Approaching Truck]] | - | - | - |
| [[Linde BlueSpot]] | [[Warn Pedestrians of an Approaching Truck]] | - | - | - |
| [[Linde Safety Guard Portable Unit]] | [[Warn Pedestrians of an Approaching Truck]] | - | - | - |
| [[Linde Safety Guard Static Unit]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Warn Pedestrians of an Approaching Truck]] | - | - | - |
| [[Oshkosh AeroTech Ramp Visibility Lights]] | [[Keep the Operator Positioned and Able to See the Work]]; [[Warn Pedestrians of an Approaching Truck]] | - | - | - |
| [[Panacea Blue Warning Light]] | [[Warn Pedestrians of an Approaching Truck]] | - | - | - |
| [[Powerfleet Forklift Safety Lights]] | [[Warn Pedestrians of an Approaching Truck]] | - | - | - |
| [[STILL SafetyLight 4Plus]] | [[Warn Pedestrians of an Approaching Truck]] | - | - | - |
| [[STILL Warning Zone Light]] | [[Warn Pedestrians of an Approaching Truck]] | - | - | - |
| [[TVH Forklift Arrow Lights]] | [[Warn Pedestrians of an Approaching Truck]] | - | - | - |
| [[Toyota Forklift Lighting Options]] | [[Keep the Operator Positioned and Able to See the Work]]; [[Warn Pedestrians of an Approaching Truck]] | - | - | - |
| [[UniCarriers Lighting Packages]] | [[Keep the Operator Positioned and Able to See the Work]]; [[Warn Pedestrians of an Approaching Truck]] | - | - | - |

### Products with no route to a need

- **Concrete products with no route (71):**
  - **Batteries/Flooded Lead-Acid Batteries** (4): [[Banner Traction Bull Bloc PzF]], [[Midac FORCEblock Battery]], [[Midac MBS Traction Battery]], [[Midac MLMx Battery]]
  - **Batteries/Lithium-Ion Batteries** (3): [[BSL Lithium Forklift Battery]], [[Green Cubes Forklift Battery Retrofit Kit]], [[Redway Lithium Forklift Batteries]]
  - **Batteries/Valve-Regulated Lead-Acid Batteries** (6): [[Banner Traction Bull PzV Gel]], [[Exide Element VRLA Battery]], [[Sonnenschein AF Battery]], [[Sonnenschein EPzV Battery]], [[Sonnenschein GF-V Battery]], [[Sonnenschein GF-Y Battery]]
  - **Battery Accessories** (1): [[Flux Power GSE3 Truck Adapter]]
  - **Battery Accessories/Battery Management Systems** (3): [[Midac Battery Management (MBM)]], [[Nuvation Energy G5 BMS]], [[REC 2Q BMS]]
  - **Battery Accessories/Identification and Charge Interface Devices** (1): [[PosiCharge BMID 1]]
  - **Battery Accessories/Monitoring Devices** (6): [[Amaron DIY Rx]], [[Banner Traction Bull Battery Controller]], [[Deka Ready Power BDI]], [[Exide Opus Display]], [[HOPPECKE trak collect premium]], [[Midac MB2 Battery Brain]]
  - **Battery Accessories/Watering Systems** (2): [[Amaron AFS System]], [[Amaron Aqua Filling Plug]]
  - **Charger Accessories** (1): [[HOPPECKE trak systemizer powercube]]
  - **Charger Accessories/Stands and Mounting** (1): [[Crown V-HFM3 Charger Stand]]
  - **Chargers/Industrial Modular Chargers** (2): [[Exide Element HF Charger]], [[ITW GSE DC Charger]]
  - **Chargers/On-board Chargers** (1): [[EnerSys NexSys COMpact Charger]]
  - **Fleet Software and Platforms** (2): [[Crown Service Request App]], [[Phantom Auto Remote Operation Software]]
  - **Fleet Software and Platforms/Battery and Charger Management** (3): [[Exide BattID]], [[HOPPECKE trak monitor 4.0]], [[Philadelphia Scientific iBOS]]
  - **Fleet Software and Platforms/Truck Telematics** (2): [[Raymond Power Source Integrated]], [[Raymond iWAREHOUSE GATEWAY]]
  - **Forklifts** (7): [[Mitsubishi EDR Reach Trucks (Americas Listing)]], [[Mitsubishi FB25-55N Electric Pneumatic Forklifts (Americas Listing)]], [[Mitsubishi FG and FD Internal Combustion Forklifts (Americas Listing)]], [[Mitsubishi Warehouse Trucks (Americas Listing)]], [[Rocla ART Automated Reach Truck]], [[Rocla AWT Automated Counterbalance Truck]], [[UniCarriers Nomad AF30-AF50 LP and Dual-Fuel Forklifts]]
  - **Forklifts/Class I Electric Rider Trucks** (8): [[Cat Electric Lift Trucks (North America Series List)]], [[Crown SC Series]], [[Hyster J2.2-3.5XN Electric Forklifts]], [[Hyster J2.5-3.0XNL Integrated Lithium-Ion Forklifts]], [[Linde 1293 Series (E20BHP and E25BHP)]], [[Mitsubishi FBC20Q-FBC40Q Electric Cushion Forklifts]], [[Toyota 7FBCU35-55 Electric Pneumatic Forklifts]], [[Yale ERC045-070VG Electric Forklifts]]
  - **Forklifts/Class II Electric Narrow Aisle Trucks** (2): [[Crown RM-RMD 6000 Series]], [[Jungheinrich ETV C16 and C20]]
  - **Ground Support Equipment/Baggage and Tow Tractors** (4): [[Charlatte CBT350 AC Tow Tractor]], [[Charlatte T137-V3]], [[Linde P250 Electric Baggage Tractor]], [[Oshkosh AeroTech B80E Electric Baggage Tractor]]
  - **Ground Support Equipment/Pushback Tractors** (2): [[Charlatte CPB35E Pushback Tractor]], [[Oshkosh AeroTech Pushback B350E and B650E]]
  - **Vehicle Accessories/Operator Assist and Stability** (3): [[Raymond Auto-Locking Pallet Clamp]], [[Raymond Intelliguide Wire Guidance]], [[Raymond Slope Sensing]]
  - **Vehicle Accessories/Operator Convenience** (5): [[Linde Smartphone Holder]], [[Raymond Accessory Bar]], [[Raymond Large Storage Tote]], [[Raymond Secondary Control Handle]], [[UniCarriers In-Cab Accessories]]
  - **Vehicle Accessories/Power Source Interfaces** (2): [[PosiCharge DIY Fast Charge Kit]], [[Purkeys Trailer Auxiliary Power System]]
- **Abstract class and category notes (61):** not expected to link.
- **Functions performed by products but realizing no need yet (product count):** [[Charge Battery]] (8), [[Sense Battery State]] (3), [[Communicate Battery and Vehicle Data]] (2), [[Protect Battery from Harm]] (2), [[Operate Truck Remotely]] (1), [[Detect Isolation Fault]] (1), [[Inform Users of Battery Condition]] (1), [[Support Operator View and Positioning]] (1)

### Challenges to the current state

- **Vendor claims are not needs.** Every need rests on a maker or dealer sentence. Direction: customer-side sources (IB-129).
- **Counting D and O as reached can overstate.** The owner decided in round 40 that design and option routes count as reached. D says a product has a part a function needs, not that it does the function (other parts may be missing). O says the product can be bought with something that does it, not that every unit has it. The per-product table keeps F, D and O in separate columns so the stronger evidence stays visible. M is a property on file and is not counted.
- **Battery properties stay metrics.** Round 27 retired property functions into metrics; closing battery gaps by adding functions would double-count them, so only device behaviors with a source were linked (BMS, onboard charger, heater, CAN output, electrolyte circulation).
- **Remaining GSE gaps are source gaps.** Several GSE notes rest on distributor lists that state only drawbar pull or battery size. Direction: OEM spec sheets (IB-138, Document Wishlist).
- **Regeneration changed the basis (C269).** The 2026-10-14 regeneration used rules written from the map's own definitions because the earlier generator is not in the repository; counts moved by new links and by the rules, so differences from round 40 are not all new evidence.
- **Role names are partly hypotheses.** Site Safety Manager has no source naming it; Dealer Sales Representative rests on dealer option lists (C106).

### Change history

- 2026-10-14: regenerated counts, needs, roles, families, per-product and no-route tables from the vault links (rules in the Notes); route M carried over. See C269.
- 2026-10-14 (charge-method and vehicle-behavior pass): the need map was regenerated after Function-to-Design links were added. One product, [[Linde Safety Guard Truck Unit]], gained route D to [[Keep Trucks Slow in Hazardous Zones]] through [[Proximity Tag System]]; need row count 41 to 42 products. Totals are unchanged (509 concrete, 438 reached: 410 F, 7 D, 21 O; 71 no route). See C269.
- 2026-10-14 (IB-233 and last six proposals): regenerated again. Battery-side and cold-storage Design links added route D entries for lithium and TPPL batteries, for example Return Trucks to Service Quickly After a Low Charge now lists more battery products and Keep Equipment Working in Cold, Wet and Dusty Conditions lists 34 products (was 31). Totals are unchanged (509 concrete, 438 reached: 410 F, 7 D, 21 O; 71 no route) because those products were already reached. See C269.
- 2026-10-14 (review of unlinked Functions): regenerated a third time. The CAN BMS-Directed Charging link raised the products reaching Integrate the Battery with Truck and Charger Controls from 54 to 58 and added route D entries for four BMS-directed chargers. Totals are unchanged (438 reached of 509). See C269.
- 2026-10-03: first generated map (round 39).
- 2026-10-03: owner decision (Q20): design and option routes count as reached; metric route stays a hypothesis column.
- 2026-10-03: round 40 gap review. Added routes D, O and M; linked 21 product notes to functions, designs or options from cited sources; added function [[Diagnose Vehicle Remotely]] and need [[Find and Fix Vehicle Faults Without Downtime]]; conflicts C107 to C110; backlog IB-136 to IB-140. See [[Research Change and Decision Tracker]].

## Aliases

- Customer need map
- Product need map

## Former ids
