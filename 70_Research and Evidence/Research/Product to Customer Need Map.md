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
describes:
  - "[[Battery-Connected Product]]"
---

# Product to Customer Need Map

## Definition

Derived map from each catalog product to the customer needs it serves, and from each need to the people who have it. Route F (strongest): product `performs` a specific Function, a Use Case (subtype why) is `realizedBy` that Function, and the Use Case `participants` lists the Actors. Routes D, O and M are weaker and stated apart so they are never mistaken for a performed function.

## Notes

- **Status: derived and hypothesis.** The map is generated from links already in the vault. Needs are what makers and dealers say their products do, not what customers say they need; a need becomes validated only with customer-side evidence (the ruleset's path from source research to hypothesis to validated need). Evidence and conflicts: C101 to C110, Q20 in [[Battery Product Landscape Conflicts and Open Questions]].
- **Routes.** F = by performed function. D = by design: the product has a design that a function realizing the need depends on (the product may not perform the function; other designs may also be required). O = by option: the vehicle or battery is offered with a product that reaches the need by F, so the need is reached only if the option is bought. M = by metric: the product has a value on a property metric that informs the need (analyst crosswalk, hypothesis; batteries are described by properties, which the vault keeps as metrics, not functions).
- **Reached (owner decision, round 40): a product counts as reached through route F, D or O. M stays a hypothesis column and is not counted as reached.** Of 398 products (excluding abstract anatomy notes): 272 are reached; 238 of those perform a realizing function (F); 12 more are added by design (D) and 22 more by option (O). The metric route adds 11 products that are not counted. 55 of the 115 with no route are abstract class or category notes (expected); 60 are concrete products with no route at all.
- **GSE vehicles and batteries (round 40 gap review):** GSE vehicles 5 of 21 by F, 10 reached (F + D + O), 10 with M; batteries 14 of 63 by F, 35 reached, 44 with M. The F counts moved because round 40 added sourced links; most remaining gaps are source gaps (listings that state only properties), not modeling gaps.
- **The counts are lower bounds.** A product reaches a need only through links a source states.

### Needs

| Need (Use Case, why) | Who has it | Operating segments (analyst crosswalk, hypothesis) | Products reached (F + D + O) | of which by F | Added by metric (M, hypothesis) | Functions | Evidence kinds |
|---|---|---|---|---|---|---|---|
| [[Keep Trucks Working Without Battery Maintenance Labor]] | [[Maintenance Technician]], [[Fleet Operations Manager]] | Material-handling fleets; Battery-room and centralized charging; Mixed-chemistry fleets | 71 | 52 | 5 | 4 | V |
| [[Charge Without a Ventilated Battery Room]] | [[Fleet Operations Manager]], [[Forklift Operator]] | Material-handling fleets; Distributed and opportunity charging; Mixed-chemistry fleets | 41 | 22 | 2 | 2 | V |
| [[Return Trucks to Service Quickly After a Low Charge]] | [[Fleet Operations Manager]], [[Forklift Operator]] | Material-handling fleets; Airport eGSE fleets; Distributed and opportunity charging | 42 | 26 | 11 | 4 | V |
| [[Charge Each Battery Correctly for Its Chemistry and Condition]] | [[Maintenance Technician]], [[Fleet Operations Manager]] | Mixed-chemistry fleets; Battery-room and centralized charging | 47 | 27 | 0 | 4 | V |
| [[Prevent Battery Abuse and Premature Replacement]] | [[Maintenance Technician]], [[Fleet Operations Manager]] | Material-handling fleets; Battery-room and centralized charging; Mixed-chemistry fleets | 11 | 8 | 6 | 4 | V |
| [[Know Battery State Before and During the Shift]] | [[Forklift Operator]], [[Maintenance Technician]] | Material-handling fleets; Airport eGSE fleets | 35 | 32 | 0 | 4 | V |
| [[Document Battery Care for Warranty Compliance]] | [[Fleet Operations Manager]], [[Dealer Service Technician]] | Material-handling fleets; Battery-room and centralized charging | 35 | 32 | 0 | 3 | V |
| [[Monitor and Manage Chargers and Batteries Across Sites]] | [[Fleet Operations Manager]] | Material-handling fleets; Airport eGSE fleets; Battery-room and centralized charging | 59 | 44 | 0 | 3 | V |
| [[Control Who Operates Each Truck]] | [[Fleet Operations Manager]], [[Site Safety Manager]], [[Forklift Operator]] | Material-handling fleets | 37 | 26 | 0 | 3 | V |
| [[Detect and Learn from Truck Impacts]] | [[Site Safety Manager]], [[Fleet Operations Manager]] | Material-handling fleets | 17 | 10 | 0 | 1 | V |
| [[Warn the Operator of People and Objects Near the Truck]] | [[Forklift Operator]], [[Site Safety Manager]] | Material-handling fleets; Airport eGSE fleets | 39 | 32 | 0 | 2 | V + G |
| [[Warn Pedestrians of an Approaching Truck]] | [[Pedestrian Near Trucks]], [[Site Safety Manager]] | Material-handling fleets | 45 | 37 | 0 | 2 | V + G |
| [[Prevent Tip-Overs and Overloads]] | [[Forklift Operator]], [[Site Safety Manager]] | Material-handling fleets | 25 | 19 | 0 | 4 | V + G |
| [[Keep Trucks Slow in Hazardous Zones]] | [[Site Safety Manager]], [[Pedestrian Near Trucks]] | Material-handling fleets | 30 | 23 | 0 | 2 | V + G |
| [[Protect Aircraft and Ground Crew During Ground Operations]] | [[GSE Operator]], [[Fleet Operations Manager]] | Airport eGSE fleets | 11 | 7 | 0 | 3 | V |
| [[Keep the Operator Positioned and Able to See the Work]] | [[Forklift Operator]] | Material-handling fleets | 29 | 24 | 0 | 3 | V |
| [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] | [[Fleet Operations Manager]], [[Forklift Operator]] | Material-handling fleets; Airport eGSE fleets | 23 | 18 | 22 | 4 | V |
| [[Stretch Truck Run Time per Charge]] | [[Fleet Operations Manager]] | Material-handling fleets; Distributed and opportunity charging | 11 | 9 | 0 | 2 | V |
| [[Integrate the Battery with Truck and Charger Controls]] | [[Truck OEM Integration Engineer]] | Mixed-chemistry fleets | 26 | 18 | 5 | 3 | V |
| [[Retrofit Safety and Telematics Onto Existing Trucks]] | [[Dealer Sales Representative]], [[Dealer Service Technician]], [[Equipment Installer]] | Material-handling fleets; Mixed-chemistry fleets | 41 | 28 | 0 | 3 | V |
| [[Connect Chargers and Batteries Safely at the Site]] | [[Equipment Installer]], [[Forklift Operator]] | Battery-room and centralized charging; Distributed and opportunity charging; Airport eGSE fleets | 19 | 10 | 0 | 3 | V + manual |
| [[Find and Fix Vehicle Faults Without Downtime]] | [[Maintenance Technician]], [[Dealer Service Technician]], [[Fleet Operations Manager]] | Material-handling fleets; Airport eGSE fleets | 36 | 24 | 0 | 4 | V |

Evidence kinds: V = vendor or dealer statement in product notes; G = government statistics showing the underlying problem exists; manual = a maker's installation or service manual.

### Roles

| Actor | Evidence status | Needs | Which |
|---|---|---|---|
| [[Vehicle Operator]] | source-stated | 0 | none (supertype or no need linked yet) |
| [[Forklift Operator]] | source-stated | 9 | [[Connect Chargers and Batteries Safely at the Site]], [[Warn the Operator of People and Objects Near the Truck]], [[Prevent Tip-Overs and Overloads]], [[Charge Without a Ventilated Battery Room]], [[Control Who Operates Each Truck]], [[Keep the Operator Positioned and Able to See the Work]], [[Return Trucks to Service Quickly After a Low Charge]], [[Keep Equipment Working in Cold, Wet and Dusty Conditions]], [[Know Battery State Before and During the Shift]] |
| [[GSE Operator]] | source-stated | 1 | [[Protect Aircraft and Ground Crew During Ground Operations]] |
| [[Pedestrian Near Trucks]] | source-stated | 2 | [[Keep Trucks Slow in Hazardous Zones]], [[Warn Pedestrians of an Approaching Truck]] |
| [[Maintenance Technician]] | source-stated | 5 | [[Keep Trucks Working Without Battery Maintenance Labor]], [[Prevent Battery Abuse and Premature Replacement]], [[Charge Each Battery Correctly for Its Chemistry and Condition]], [[Find and Fix Vehicle Faults Without Downtime]], [[Know Battery State Before and During the Shift]] |
| [[Fleet Operations Manager]] | source-stated | 13 | [[Keep Trucks Working Without Battery Maintenance Labor]], [[Detect and Learn from Truck Impacts]], [[Charge Without a Ventilated Battery Room]], [[Control Who Operates Each Truck]], [[Prevent Battery Abuse and Premature Replacement]], [[Charge Each Battery Correctly for Its Chemistry and Condition]], [[Return Trucks to Service Quickly After a Low Charge]], [[Monitor and Manage Chargers and Batteries Across Sites]], [[Protect Aircraft and Ground Crew During Ground Operations]], [[Document Battery Care for Warranty Compliance]], [[Find and Fix Vehicle Faults Without Downtime]], [[Keep Equipment Working in Cold, Wet and Dusty Conditions]], [[Stretch Truck Run Time per Charge]] |
| [[Site Safety Manager]] | hypothesis | 6 | [[Warn the Operator of People and Objects Near the Truck]], [[Prevent Tip-Overs and Overloads]], [[Detect and Learn from Truck Impacts]], [[Keep Trucks Slow in Hazardous Zones]], [[Control Who Operates Each Truck]], [[Warn Pedestrians of an Approaching Truck]] |
| [[Dealer Sales Representative]] | source-implied | 1 | [[Retrofit Safety and Telematics Onto Existing Trucks]] |
| [[Dealer Service Technician]] | source-stated | 3 | [[Retrofit Safety and Telematics Onto Existing Trucks]], [[Document Battery Care for Warranty Compliance]], [[Find and Fix Vehicle Faults Without Downtime]] |
| [[Equipment Installer]] | source-stated | 2 | [[Connect Chargers and Batteries Safely at the Site]], [[Retrofit Safety and Telematics Onto Existing Trucks]] |
| [[Truck OEM Integration Engineer]] | source-implied | 1 | [[Integrate the Battery with Truck and Charger Controls]] |

### Segments and needs (crosswalk to [[PosiCharge Market Segments and Jobs-to-Be-Done]])

The crosswalk is the analyst's reading, not a source statement.

| Segment | Needs | Which |
|---|---|---|
| Material-handling fleets | 18 | [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Warn the Operator of People and Objects Near the Truck]]; [[Prevent Tip-Overs and Overloads]]; [[Detect and Learn from Truck Impacts]]; [[Keep Trucks Slow in Hazardous Zones]]; [[Charge Without a Ventilated Battery Room]]; [[Control Who Operates Each Truck]]; [[Prevent Battery Abuse and Premature Replacement]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Keep the Operator Positioned and Able to See the Work]]; [[Return Trucks to Service Quickly After a Low Charge]]; [[Warn Pedestrians of an Approaching Truck]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Document Battery Care for Warranty Compliance]]; [[Find and Fix Vehicle Faults Without Downtime]]; [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Know Battery State Before and During the Shift]]; [[Stretch Truck Run Time per Charge]] |
| Airport eGSE fleets | 8 | [[Connect Chargers and Batteries Safely at the Site]]; [[Warn the Operator of People and Objects Near the Truck]]; [[Return Trucks to Service Quickly After a Low Charge]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Protect Aircraft and Ground Crew During Ground Operations]]; [[Find and Fix Vehicle Faults Without Downtime]]; [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Know Battery State Before and During the Shift]] |
| Mixed-chemistry fleets | 6 | [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Charge Without a Ventilated Battery Room]]; [[Prevent Battery Abuse and Premature Replacement]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Integrate the Battery with Truck and Charger Controls]] |
| Battery-room and centralized charging | 6 | [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Connect Chargers and Batteries Safely at the Site]]; [[Prevent Battery Abuse and Premature Replacement]]; [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Document Battery Care for Warranty Compliance]] |
| Distributed and opportunity charging | 4 | [[Connect Chargers and Batteries Safely at the Site]]; [[Charge Without a Ventilated Battery Room]]; [[Return Trucks to Service Quickly After a Low Charge]]; [[Stretch Truck Run Time per Charge]] |

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

| Product family | Products | By F | Reached (F + D + O) | Reached plus M (hypothesis) |
|---|---|---|---|---|
| Batteries | 1 | 0 | 0 | 0 |
| Batteries/Flooded Lead-Acid Batteries | 24 | 4 | 12 | 17 |
| Batteries/Lithium-Ion Batteries | 27 | 8 | 18 | 21 |
| Batteries/Valve-Regulated Lead-Acid Batteries | 11 | 2 | 5 | 6 |
| Battery Accessories | 2 | 0 | 0 | 0 |
| Battery Accessories/Battery Management Systems | 1 | 0 | 0 | 0 |
| Battery Accessories/Connector Assemblies | 4 | 3 | 3 | 3 |
| Battery Accessories/Electrolyte Circulation Systems | 4 | 0 | 0 | 0 |
| Battery Accessories/Identification and Charge Interface Devices | 10 | 7 | 8 | 8 |
| Battery Accessories/Monitoring Devices | 27 | 26 | 26 | 26 |
| Battery Accessories/Protection and Disconnect Units | 1 | 0 | 0 | 0 |
| Battery Accessories/Telematics and Connectivity Devices | 2 | 1 | 1 | 1 |
| Battery Accessories/Thermal Management Devices | 1 | 0 | 0 | 0 |
| Battery Accessories/Water Level Monitors | 5 | 4 | 4 | 4 |
| Battery Accessories/Watering Systems | 8 | 6 | 6 | 6 |
| Battery-Connected Product.md | 1 | 0 | 0 | 0 |
| Charger Accessories | 1 | 0 | 0 | 0 |
| Charger Accessories/Cable Management | 2 | 1 | 1 | 1 |
| Charger Accessories/Connector Accessories | 2 | 0 | 0 | 0 |
| Charger Accessories/Remote Controls and Indicators | 4 | 2 | 2 | 2 |
| Charger Accessories/Stands and Mounting | 3 | 1 | 1 | 1 |
| Charger Accessories/Thermal Accessories | 2 | 0 | 0 | 0 |
| Chargers | 1 | 0 | 0 | 0 |
| Chargers/Industrial Modular Chargers | 37 | 29 | 29 | 30 |
| Chargers/Light-Duty Chargers | 4 | 3 | 3 | 3 |
| Chargers/On-board Chargers | 3 | 1 | 1 | 1 |
| Chargers/Wireless Chargers | 2 | 1 | 1 | 1 |
| Fleet Software and Platforms | 1 | 0 | 0 | 0 |
| Fleet Software and Platforms/Battery and Charger Management | 10 | 6 | 6 | 6 |
| Fleet Software and Platforms/Truck Telematics | 20 | 19 | 19 | 19 |
| Forklifts | 1 | 0 | 0 | 0 |
| Forklifts/Class I Electric Rider Trucks | 30 | 20 | 26 | 27 |
| Forklifts/Class II Electric Narrow Aisle Trucks | 6 | 2 | 3 | 3 |
| Forklifts/Class III Electric Hand and Hand-Rider Trucks | 3 | 2 | 2 | 2 |
| Forklifts/Class IV Internal Combustion Cushion Tire Trucks | 1 | 0 | 0 | 0 |
| Forklifts/Class V Internal Combustion Pneumatic Tire Trucks | 1 | 0 | 0 | 0 |
| Forklifts/Class VI Tractors | 1 | 0 | 0 | 0 |
| Forklifts/Class VII Rough Terrain Forklifts | 1 | 0 | 0 | 0 |
| Fuel Cell Power Units/Hydrogen Fuel Cell Units | 3 | 2 | 2 | 2 |
| Ground Support Equipment | 1 | 0 | 0 | 0 |
| Ground Support Equipment/Baggage and Tow Tractors | 7 | 2 | 2 | 2 |
| Ground Support Equipment/Belt Loaders | 6 | 2 | 5 | 5 |
| Ground Support Equipment/Cargo Loaders | 3 | 0 | 2 | 2 |
| Ground Support Equipment/Pushback Tractors | 4 | 1 | 1 | 1 |
| Vehicle Accessories | 1 | 0 | 0 | 0 |
| Vehicle Accessories/Access Control | 3 | 2 | 2 | 2 |
| Vehicle Accessories/Cameras and Recorders | 8 | 6 | 6 | 6 |
| Vehicle Accessories/Cold Storage Packages | 3 | 2 | 2 | 2 |
| Vehicle Accessories/Operator Assist and Stability | 37 | 29 | 29 | 29 |
| Vehicle Accessories/Operator Convenience | 6 | 0 | 0 | 0 |
| Vehicle Accessories/Operator Displays | 5 | 3 | 3 | 3 |
| Vehicle Accessories/Power Source Interfaces | 3 | 1 | 1 | 1 |
| Vehicle Accessories/Proximity and Object Detection | 29 | 28 | 28 | 28 |
| Vehicle Accessories/Warning Lights and Alerts | 14 | 12 | 12 | 12 |

### Per-product route

Generated list. A dash means no product in that route.

#### Batteries/Flooded Lead-Acid Batteries

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Crown V-Force Lead-Acid Battery]] | - | - | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Return Trucks to Service Quickly After a Low Charge]] | - |
| [[Deka ChargeMate Battery]] | - | [[Charge Without a Ventilated Battery Room]] | [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Return Trucks to Service Quickly After a Low Charge]] | - |
| [[Deka D-Series Battery]] | - | - | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Return Trucks to Service Quickly After a Low Charge]] | [[Prevent Battery Abuse and Premature Replacement]] |
| [[Deka FastCharge Battery]] | - | - | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Return Trucks to Service Quickly After a Low Charge]] | - |
| [[Deka HydraSaver Battery]] | [[Keep Trucks Working Without Battery Maintenance Labor]] | - | [[Charge Without a Ventilated Battery Room]]; [[Return Trucks to Service Quickly After a Low Charge]] | - |
| [[Deka MaintenanceSaver Battery]] | - | - | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Return Trucks to Service Quickly After a Low Charge]] | - |
| [[Deka MaxPowr Battery]] | - | - | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Return Trucks to Service Quickly After a Low Charge]] | [[Prevent Battery Abuse and Premature Replacement]] |
| [[Exide MARATHON Battery]] | [[Keep Trucks Working Without Battery Maintenance Labor]] | - | - | - |
| [[HAWKER Perfect Plus Battery]] | [[Keep Trucks Working Without Battery Maintenance Labor]] | - | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Document Battery Care for Warranty Compliance]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Know Battery State Before and During the Shift]]; [[Prevent Battery Abuse and Premature Replacement]] | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] |
| [[HOPPECKE trak uplift air Battery]] | - | - | [[Charge Each Battery Correctly for Its Chemistry and Condition]] | - |
| [[HOPPECKE trak uplift iQ Battery]] | [[Know Battery State Before and During the Shift]] | - | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Document Battery Care for Warranty Compliance]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Monitor and Manage Chargers and Batteries Across Sites]] | - |
| [[Midac PzS Traction Battery]] | - | - | [[Connect Chargers and Batteries Safely at the Site]]; [[Keep Trucks Working Without Battery Maintenance Labor]] | - |
| [[Stryten M-Series F100 Battery]] | - | - | - | [[Return Trucks to Service Quickly After a Low Charge]] |
| [[Stryten M-Series F110 Battery]] | - | - | - | [[Prevent Battery Abuse and Premature Replacement]]; [[Return Trucks to Service Quickly After a Low Charge]] |
| [[Stryten M-Series T300 Battery]] | - | - | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Prevent Battery Abuse and Premature Replacement]]; [[Return Trucks to Service Quickly After a Low Charge]] |
| [[Stryten M-Series T310 Battery]] | - | - | - | [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Prevent Battery Abuse and Premature Replacement]]; [[Return Trucks to Service Quickly After a Low Charge]] |
| [[Stryten M-Series T330 Battery]] | - | - | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Prevent Battery Abuse and Premature Replacement]]; [[Return Trucks to Service Quickly After a Low Charge]] |

#### Batteries/Lithium-Ion Batteries

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Crown V-Force Lithium-Ion ESS]] | - | [[Charge Each Battery Correctly for Its Chemistry and Condition]] | [[Charge Without a Ventilated Battery Room]]; [[Control Who Operates Each Truck]]; [[Find and Fix Vehicle Faults Without Downtime]]; [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Keep Trucks Slow in Hazardous Zones]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Prevent Battery Abuse and Premature Replacement]]; [[Prevent Tip-Overs and Overloads]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Return Trucks to Service Quickly After a Low Charge]]; [[Stretch Truck Run Time per Charge]]; [[Warn Pedestrians of an Approaching Truck]] | - |
| [[Deka Ready Power Lithium Battery]] | - | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Integrate the Battery with Truck and Charger Controls]] | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Return Trucks to Service Quickly After a Low Charge]] | - |
| [[EnerSys NexSys iON Battery]] | [[Integrate the Battery with Truck and Charger Controls]]; [[Prevent Battery Abuse and Premature Replacement]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]] | - | - |
| [[Exide GNB Lithium Battery 2.0]] | - | [[Charge Each Battery Correctly for Its Chemistry and Condition]] | - | [[Integrate the Battery with Truck and Charger Controls]] |
| [[Exide Solition Light Traction Battery]] | [[Integrate the Battery with Truck and Charger Controls]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]] | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]] | - |
| [[Flux Power LiFT Pack]] | - | - | - | [[Integrate the Battery with Truck and Charger Controls]]; [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Return Trucks to Service Quickly After a Low Charge]] |
| [[Flux Power S-Series Battery]] | - | [[Charge Each Battery Correctly for Its Chemistry and Condition]] | - | [[Integrate the Battery with Truck and Charger Controls]] |
| [[Godrej Lithium-Ion Forklift Battery]] | - | [[Charge Each Battery Correctly for Its Chemistry and Condition]] | - | [[Return Trucks to Service Quickly After a Low Charge]] |
| [[Godrej Multi-Ion Forklift Battery]] | - | - | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] |
| [[Green Cubes GSE Lithium Battery]] | [[Integrate the Battery with Truck and Charger Controls]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]] | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]] | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] |
| [[Green Cubes SAFEFlex Battery]] | - | [[Charge Each Battery Correctly for Its Chemistry and Condition]] | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]] | [[Integrate the Battery with Truck and Charger Controls]]; [[Return Trucks to Service Quickly After a Low Charge]] |
| [[HOPPECKE trak power Lithium Battery]] | - | [[Charge Each Battery Correctly for Its Chemistry and Condition]] | - | - |
| [[Hangcha Lithium Iron Phosphate Battery Pack]] | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] | - | [[Control Who Operates Each Truck]]; [[Find and Fix Vehicle Faults Without Downtime]]; [[Keep the Operator Positioned and Able to See the Work]]; [[Prevent Tip-Overs and Overloads]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Return Trucks to Service Quickly After a Low Charge]]; [[Warn Pedestrians of an Approaching Truck]] | - |
| [[Heli Lithium-Ion Battery]] | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] | - | [[Charge Without a Ventilated Battery Room]]; [[Prevent Tip-Overs and Overloads]] | - |
| [[Jungheinrich Lithium-Ion Battery]] | - | [[Charge Each Battery Correctly for Its Chemistry and Condition]] | - | [[Return Trucks to Service Quickly After a Low Charge]] |
| [[Linde 90 V Lithium-Ion Battery]] | - | - | [[Know Battery State Before and During the Shift]] | - |
| [[Raymond 8250 Lithium-Ion Battery]] | - | - | [[Control Who Operates Each Truck]]; [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] | [[Keep Trucks Working Without Battery Maintenance Labor]] |
| [[Stryten M-Series Li600 Battery]] | [[Integrate the Battery with Truck and Charger Controls]] | - | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Return Trucks to Service Quickly After a Low Charge]] | - |
| [[Stryten M-Series Li610 Battery]] | [[Know Battery State Before and During the Shift]] | - | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Charge Without a Ventilated Battery Room]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Return Trucks to Service Quickly After a Low Charge]] | - |
| [[Toyota Lithium-Ion 5-35 Battery Series]] | [[Integrate the Battery with Truck and Charger Controls]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]] | [[Find and Fix Vehicle Faults Without Downtime]] | - |
| [[Triathlon Lithium-Ion Battery for UniCarriers]] | - | - | - | [[Charge Without a Ventilated Battery Room]]; [[Return Trucks to Service Quickly After a Low Charge]] |

#### Batteries/Valve-Regulated Lead-Acid Batteries

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Deka Dominator Battery]] | - | - | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Return Trucks to Service Quickly After a Low Charge]] | - |
| [[Deka Gel-Mate Battery]] | [[Charge Without a Ventilated Battery Room]] | - | [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Return Trucks to Service Quickly After a Low Charge]] | - |
| [[Deka PowrMate Battery]] | [[Charge Without a Ventilated Battery Room]] | - | [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Return Trucks to Service Quickly After a Low Charge]] | - |
| [[EnerSys NexSys TPPL Battery]] | - | - | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Charge Without a Ventilated Battery Room]]; [[Connect Chargers and Batteries Safely at the Site]]; [[Document Battery Care for Warranty Compliance]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Prevent Battery Abuse and Premature Replacement]]; [[Return Trucks to Service Quickly After a Low Charge]] | - |
| [[Stryten M-Series AGM200 Battery]] | - | - | - | [[Keep Trucks Working Without Battery Maintenance Labor]] |
| [[Stryten M-Series AGM220 Battery]] | - | [[Charge Without a Ventilated Battery Room]] | - | - |

#### Battery Accessories/Connector Assemblies

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Anderson SB Connector Series]] | [[Connect Chargers and Batteries Safely at the Site]] | - | - | - |
| [[Crown Battery Cables and Connectors]] | [[Connect Chargers and Batteries Safely at the Site]] | - | - | - |
| [[Midac End Leads]] | [[Connect Chargers and Batteries Safely at the Site]] | - | - | - |

#### Battery Accessories/Identification and Charge Interface Devices

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[AMETEK Prestolite Power BID]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]] | - | - | [[Integrate the Battery with Truck and Charger Controls]] |
| [[AMETEK Prestolite Power BID with Ah Accumulator]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Document Battery Care for Warranty Compliance]] | - | - | - |
| [[Crown V-Force BMID]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Document Battery Care for Warranty Compliance]]; [[Keep Trucks Working Without Battery Maintenance Labor]] | - | - | - |
| [[Fronius TagID]] | [[Keep Trucks Working Without Battery Maintenance Labor]] | - | - | - |
| [[PosiCharge BMID]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Document Battery Care for Warranty Compliance]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Know Battery State Before and During the Shift]] | - | - | - |
| [[PosiCharge BMID 3]] | - | [[Integrate the Battery with Truck and Charger Controls]] | - | - |
| [[PosiCharge Battery Rx]] | [[Document Battery Care for Warranty Compliance]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]] | - | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] |
| [[PosiCharge PosiGuard]] | [[Document Battery Care for Warranty Compliance]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Monitor and Manage Chargers and Batteries Across Sites]] | - | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] |

#### Battery Accessories/Monitoring Devices

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[AMETEK Prestolite Power Site Probe]] | [[Document Battery Care for Warranty Compliance]] | - | - | - |
| [[AMETEK Prestolite Power TruBid]] | [[Integrate the Battery with Truck and Charger Controls]]; [[Know Battery State Before and During the Shift]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | - |
| [[AMETEK Prestolite Power WBID]] | [[Document Battery Care for Warranty Compliance]]; [[Integrate the Battery with Truck and Charger Controls]] | - | - | - |
| [[AMETEK Prestolite Power WBID Pro]] | [[Document Battery Care for Warranty Compliance]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]] | - | - | - |
| [[Access Control Group CellTrac]] | [[Keep Trucks Working Without Battery Maintenance Labor]] | - | - | - |
| [[Access Control Group CellVue]] | [[Know Battery State Before and During the Shift]] | - | - | - |
| [[Advanced Charging Technologies BATTview]] | [[Document Battery Care for Warranty Compliance]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Monitor and Manage Chargers and Batteries Across Sites]] | - | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] |
| [[Crown Battery Health Monitor]] | [[Document Battery Care for Warranty Compliance]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Monitor and Manage Chargers and Batteries Across Sites]] | - | - | - |
| [[EnerSys Wi-iQ]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Document Battery Care for Warranty Compliance]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] |
| [[EnerSys iQ Mini]] | [[Document Battery Care for Warranty Compliance]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | - |
| [[Energywith withBMS BMU]] | [[Document Battery Care for Warranty Compliance]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Monitor and Manage Chargers and Batteries Across Sites]] | - | - | - |
| [[Exide Motion+ EasyMonitor]] | [[Document Battery Care for Warranty Compliance]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] |
| [[HOPPECKE trak collect]] | [[Document Battery Care for Warranty Compliance]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]] | - | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] |
| [[Hyster Battery Tracker]] | [[Document Battery Care for Warranty Compliance]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]] | - | - | - |
| [[Inventus Smart Battery Monitor SBM-01]] | [[Integrate the Battery with Truck and Charger Controls]]; [[Know Battery State Before and During the Shift]] | - | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] |
| [[Philadelphia Scientific eGO!Mini]] | [[Document Battery Care for Warranty Compliance]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]] | - | - | - |
| [[Philadelphia Scientific eGO!c]] | [[Document Battery Care for Warranty Compliance]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]] | - | - | - |
| [[Philadelphia Scientific eGO!core]] | [[Document Battery Care for Warranty Compliance]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Monitor and Manage Chargers and Batteries Across Sites]] | - | - | - |
| [[Philadelphia Scientific eGO!plus]] | [[Document Battery Care for Warranty Compliance]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]] | - | - | - |
| [[Philadelphia Scientific eGO!pro]] | [[Document Battery Care for Warranty Compliance]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]] | - | - | - |
| [[Power Designers PowerTrac 3]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Document Battery Care for Warranty Compliance]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Keep Trucks Working Without Battery Maintenance Labor]] | - | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] |
| [[Power Designers PowerTrac DT3]] | [[Document Battery Care for Warranty Compliance]]; [[Know Battery State Before and During the Shift]] | - | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] |
| [[Power Designers PowerTrac Monitor]] | [[Document Battery Care for Warranty Compliance]]; [[Know Battery State Before and During the Shift]] | - | - | - |
| [[Power Designers PowerTrac SP+]] | [[Document Battery Care for Warranty Compliance]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Keep Trucks Working Without Battery Maintenance Labor]] | - | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] |
| [[Raymond iBattery]] | [[Document Battery Care for Warranty Compliance]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]] | - | - | - |
| [[Yale Battery Vision]] | [[Document Battery Care for Warranty Compliance]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]] | - | - | - |

#### Battery Accessories/Telematics and Connectivity Devices

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Philadelphia Scientific eGO!gateway]] | [[Document Battery Care for Warranty Compliance]]; [[Monitor and Manage Chargers and Batteries Across Sites]] | - | - | - |

#### Battery Accessories/Water Level Monitors

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Crown Battery Acid Indicators]] | [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]] | - | - | - |
| [[Flow-Rite Eagle Eye Elite IV]] | [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]] | - | - | - |
| [[Flow-Rite Eagle Eye Essential IV]] | [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]] | - | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] |
| [[Philadelphia Scientific SmartBlinky Pro]] | [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]] | - | - | - |

#### Battery Accessories/Watering Systems

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Crown V-Force Single Point Watering System]] | [[Keep Trucks Working Without Battery Maintenance Labor]] | - | - | - |
| [[Exide Automatic Watering System and Level Sensor]] | [[Keep Trucks Working Without Battery Maintenance Labor]] | - | - | - |
| [[Midac Aquamatic Watering System]] | [[Keep Trucks Working Without Battery Maintenance Labor]] | - | - | - |
| [[Philadelphia Scientific Stealth Watering System]] | [[Keep Trucks Working Without Battery Maintenance Labor]] | - | - | - |
| [[Philadelphia Scientific Water Injector System]] | [[Keep Trucks Working Without Battery Maintenance Labor]] | - | - | - |
| [[PosiCharge Single-Point Automatic Battery Watering]] | [[Keep Trucks Working Without Battery Maintenance Labor]] | - | - | - |

#### Charger Accessories/Cable Management

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Crown Cable Management Accessories]] | [[Connect Chargers and Batteries Safely at the Site]] | - | - | - |

#### Charger Accessories/Remote Controls and Indicators

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Crown V-HFM3 Tower Light Kit]] | [[Know Battery State Before and During the Shift]] | - | - | - |
| [[PosiCharge Three-Color Stack Light]] | [[Know Battery State Before and During the Shift]] | - | - | - |

#### Charger Accessories/Stands and Mounting

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[PosiCharge Charger Stand Kit and Cable Handler]] | [[Connect Chargers and Batteries Safely at the Site]] | - | - | - |

#### Chargers/Industrial Modular Chargers

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[ACT Quantum 2]] | [[Charge Without a Ventilated Battery Room]]; [[Connect Chargers and Batteries Safely at the Site]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Monitor and Manage Chargers and Batteries Across Sites]] | - | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] |
| [[ACT Quantum 3]] | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Monitor and Manage Chargers and Batteries Across Sites]] | [[Connect Chargers and Batteries Safely at the Site]] | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] |
| [[ACT Quantum Outdoor]] | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Monitor and Manage Chargers and Batteries Across Sites]] | - | - | - |
| [[AMETEK Prestolite Power Eclipse II]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |
| [[AMETEK Prestolite Power ULTRA]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |
| [[Crown Battery EVOLUTION Series]] | [[Return Trucks to Service Quickly After a Low Charge]] | [[Connect Chargers and Batteries Safely at the Site]] | - | - |
| [[Crown V-HFM3 Charger]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Return Trucks to Service Quickly After a Low Charge]] | [[Connect Chargers and Batteries Safely at the Site]] | - | - |
| [[Deka PowerForce Charger]] | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |
| [[EnerSys Express Charger]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Connect Chargers and Batteries Safely at the Site]]; [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |
| [[EnerSys IMPAQ Charger]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Connect Chargers and Batteries Safely at the Site]]; [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |
| [[EnerSys NexSys+ Charger]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Charge Without a Ventilated Battery Room]]; [[Connect Chargers and Batteries Safely at the Site]]; [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |
| [[Exide Motion+ Lithium Charger]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]] | - | - | - |
| [[Fronius SelectION]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]] | - | - | - |
| [[Fronius Selectiva 4.0]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Monitor and Manage Chargers and Batteries Across Sites]] | - | - | - |
| [[Green Cubes SAFEFlex Charger]] | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]] | - | - | - |
| [[HOPPECKE trak charger HF premium]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]] | - | - | - |
| [[PosiCharge DVS100]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |
| [[PosiCharge DVS150]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Document Battery Care for Warranty Compliance]] | - | - | - |
| [[PosiCharge DVS300 Series]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |
| [[PosiCharge High Voltage Power Station (DC)]] | [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |
| [[PosiCharge MVS400 and MVS800]] | [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |
| [[PosiCharge ProCore Edge]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |
| [[PosiCharge SVS100]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |
| [[PosiCharge SVS200]] | [[Keep Trucks Working Without Battery Maintenance Labor]] | - | - | - |
| [[Power Designers REVOLUTION X]] | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Return Trucks to Service Quickly After a Low Charge]] | [[Connect Chargers and Batteries Safely at the Site]] | - | - |
| [[Raymond Red Charger]] | [[Return Trucks to Service Quickly After a Low Charge]] | [[Connect Chargers and Batteries Safely at the Site]] | - | - |
| [[Stryten EHI Charger]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |
| [[Stryten EHY Charger]] | - | - | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] |
| [[Stryten X-3 Charger]] | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Return Trucks to Service Quickly After a Low Charge]] | [[Connect Chargers and Batteries Safely at the Site]] | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] |
| [[Stryten X-7 Charger]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Return Trucks to Service Quickly After a Low Charge]] | [[Connect Chargers and Batteries Safely at the Site]] | - | - |

#### Chargers/Light-Duty Chargers

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Delta-Q IC650]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]] | - | - | - |
| [[Exide Motion+ Premium Charger]] | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]] | [[Integrate the Battery with Truck and Charger Controls]] | - | - |
| [[Lester Summit Series II]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Monitor and Manage Chargers and Batteries Across Sites]] | - | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] |

#### Chargers/On-board Chargers

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Heli Built-In Lithium Charger]] | [[Charge Without a Ventilated Battery Room]] | - | - | - |

#### Chargers/Wireless Chargers

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[EnerSys NexSys AIR Wireless Charger]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Charge Without a Ventilated Battery Room]]; [[Connect Chargers and Batteries Safely at the Site]]; [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |

#### Fleet Software and Platforms/Battery and Charger Management

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[ACT ACTview]] | [[Monitor and Manage Chargers and Batteries Across Sites]] | - | - | - |
| [[PosiCharge E-Meter]] | [[Document Battery Care for Warranty Compliance]] | - | - | - |
| [[PosiCharge PosiLink]] | [[Document Battery Care for Warranty Compliance]]; [[Monitor and Manage Chargers and Batteries Across Sites]] | - | - | - |
| [[PosiCharge PosiNet]] | [[Document Battery Care for Warranty Compliance]]; [[Monitor and Manage Chargers and Batteries Across Sites]] | - | - | - |
| [[PosiCharge SkyLink]] | [[Monitor and Manage Chargers and Batteries Across Sites]] | - | - | - |
| [[Stryten inCOMMAND]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Integrate the Battery with Truck and Charger Controls]] | - | - | - |

#### Fleet Software and Platforms/Truck Telematics

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Adveez Asset and Operations Monitoring System]] | [[Control Who Operates Each Truck]]; [[Find and Fix Vehicle Faults Without Downtime]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] | - | - | - |
| [[Crown InfoLink]] | [[Control Who Operates Each Truck]]; [[Detect and Learn from Truck Impacts]]; [[Find and Fix Vehicle Faults Without Downtime]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] | - | - | - |
| [[Doosan Lin-Q]] | [[Control Who Operates Each Truck]]; [[Find and Fix Vehicle Faults Without Downtime]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] | - | - | - |
| [[Hangcha FIMS]] | [[Control Who Operates Each Truck]]; [[Find and Fix Vehicle Faults Without Downtime]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] | - | - | - |
| [[Heli Fleet Management System]] | [[Control Who Operates Each Truck]]; [[Find and Fix Vehicle Faults Without Downtime]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] | - | - | - |
| [[Hyster Tracker Telemetry]] | [[Control Who Operates Each Truck]]; [[Detect and Learn from Truck Impacts]]; [[Find and Fix Vehicle Faults Without Downtime]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] | - | - | - |
| [[Jungheinrich ISM Online]] | [[Control Who Operates Each Truck]]; [[Find and Fix Vehicle Faults Without Downtime]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] | - | - | - |
| [[Komatsu KOMTRAX]] | [[Control Who Operates Each Truck]]; [[Find and Fix Vehicle Faults Without Downtime]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] | - | - | - |
| [[Linde connect]] | [[Control Who Operates Each Truck]]; [[Detect and Learn from Truck Impacts]]; [[Find and Fix Vehicle Faults Without Downtime]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] | - | - | - |
| [[Logisnext Lift Link]] | [[Control Who Operates Each Truck]]; [[Detect and Learn from Truck Impacts]]; [[Find and Fix Vehicle Faults Without Downtime]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] | - | - | - |
| [[Oshkosh AeroTech iOPS]] | [[Control Who Operates Each Truck]]; [[Find and Fix Vehicle Faults Without Downtime]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] | - | - | - |
| [[Powerfleet Forklift Gateway]] | [[Control Who Operates Each Truck]]; [[Detect and Learn from Truck Impacts]]; [[Find and Fix Vehicle Faults Without Downtime]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] | - | - | - |
| [[Raymond iWAREHOUSE]] | [[Control Who Operates Each Truck]]; [[Detect and Learn from Truck Impacts]]; [[Find and Fix Vehicle Faults Without Downtime]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] | - | - | - |
| [[Raymond iWAREHOUSE Real-Time Location System]] | [[Keep Trucks Slow in Hazardous Zones]] | - | - | - |
| [[STILL FleetManager]] | [[Control Who Operates Each Truck]]; [[Find and Fix Vehicle Faults Without Downtime]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] | - | - | - |
| [[STILL Smart Portal]] | [[Control Who Operates Each Truck]]; [[Detect and Learn from Truck Impacts]]; [[Find and Fix Vehicle Faults Without Downtime]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] | - | - | - |
| [[STILL neXXt fleet]] | [[Control Who Operates Each Truck]]; [[Find and Fix Vehicle Faults Without Downtime]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] | - | - | - |
| [[Toyota MyInsights Telematics]] | [[Control Who Operates Each Truck]]; [[Detect and Learn from Truck Impacts]]; [[Find and Fix Vehicle Faults Without Downtime]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] | - | - | - |
| [[Yale Vision Telemetry]] | [[Control Who Operates Each Truck]]; [[Find and Fix Vehicle Faults Without Downtime]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] | - | - | - |

#### Forklifts/Class I Electric Rider Trucks

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Cat 2EPC5000-2EP6500 Electric Pneumatic Tire Lift Trucks]] | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Keep Trucks Slow in Hazardous Zones]]; [[Keep the Operator Positioned and Able to See the Work]] | - | - | - |
| [[Cat EP14-20 Electric Counterbalance Forklifts]] | - | - | [[Keep the Operator Positioned and Able to See the Work]] | - |
| [[Cat EP25-55 80 V Electric Counterbalance Forklifts]] | - | - | [[Warn Pedestrians of an Approaching Truck]] | - |
| [[Crown FC 5700 Series]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Prevent Tip-Overs and Overloads]] | - | [[Control Who Operates Each Truck]]; [[Detect and Learn from Truck Impacts]]; [[Find and Fix Vehicle Faults Without Downtime]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] | - |
| [[Crown RC 5700 Series]] | [[Control Who Operates Each Truck]]; [[Find and Fix Vehicle Faults Without Downtime]]; [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Keep Trucks Slow in Hazardous Zones]]; [[Prevent Battery Abuse and Premature Replacement]]; [[Prevent Tip-Overs and Overloads]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Stretch Truck Run Time per Charge]]; [[Warn Pedestrians of an Approaching Truck]] | - | [[Detect and Learn from Truck Impacts]]; [[Monitor and Manage Chargers and Batteries Across Sites]] | - |
| [[Doosan Bobcat 7-Series Plus Electric Forklifts]] | [[Keep the Operator Positioned and Able to See the Work]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | [[Keep Trucks Slow in Hazardous Zones]] | - |
| [[Doosan Bobcat NXE Series Electric Forklifts]] | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Prevent Tip-Overs and Overloads]] | - | - | - |
| [[Hangcha A Series Electric Forklifts]] | [[Find and Fix Vehicle Faults Without Downtime]]; [[Return Trucks to Service Quickly After a Low Charge]]; [[Warn Pedestrians of an Approaching Truck]] | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] | - |
| [[Hangcha XC Series Electric Forklifts]] | [[Control Who Operates Each Truck]]; [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Keep the Operator Positioned and Able to See the Work]]; [[Prevent Tip-Overs and Overloads]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Return Trucks to Service Quickly After a Low Charge]] | - | [[Find and Fix Vehicle Faults Without Downtime]]; [[Monitor and Manage Chargers and Batteries Across Sites]] | - |
| [[Heli A3 Series Lithium Forklifts]] | [[Charge Without a Ventilated Battery Room]]; [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] | - | [[Keep the Operator Positioned and Able to See the Work]] | - |
| [[Heli G Series Lithium Forklifts]] | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Prevent Tip-Overs and Overloads]] | - | - | - |
| [[Hyster J1.5-3.0UT(L)]] | [[Stretch Truck Run Time per Charge]] | - | - | - |
| [[Komatsu FB Series Electric Forklifts]] | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Keep Trucks Slow in Hazardous Zones]] | - | [[Control Who Operates Each Truck]]; [[Find and Fix Vehicle Faults Without Downtime]]; [[Keep the Operator Positioned and Able to See the Work]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] | - |
| [[Linde 6-8 t Electric Counterbalance Forklifts]] | [[Know Battery State Before and During the Shift]] | - | - | [[Return Trucks to Service Quickly After a Low Charge]] |
| [[Linde E Series Electric Counterbalance Forklifts]] | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] | - | - | - |
| [[Linde Ei Series]] | - | - | - | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]] |
| [[Mitsubishi FB 3-Wheel Electric Forklifts]] | - | - | [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - |
| [[Mitsubishi FBC Cushion Tire Electric Forklifts]] | - | - | [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - |
| [[Mitsubishi FBCS Stand-Up Counterbalanced Forklifts]] | [[Keep the Operator Positioned and Able to See the Work]] | - | - | - |
| [[Raymond 4000 Series Counterbalanced Trucks]] | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Keep the Operator Positioned and Able to See the Work]] | - | [[Keep Trucks Slow in Hazardous Zones]] | - |
| [[STILL RX 60 Electric Forklift]] | [[Control Who Operates Each Truck]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] | - | [[Find and Fix Vehicle Faults Without Downtime]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Prevent Tip-Overs and Overloads]]; [[Warn Pedestrians of an Approaching Truck]] | - |
| [[Toyota 3-Wheel Electric Forklift]] | [[Find and Fix Vehicle Faults Without Downtime]] | - | [[Control Who Operates Each Truck]]; [[Detect and Learn from Truck Impacts]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] | - |
| [[Toyota Traigo48]] | [[Return Trucks to Service Quickly After a Low Charge]] | - | - | - |
| [[UniCarriers MX2 and MXL Series]] | - | - | [[Control Who Operates Each Truck]]; [[Detect and Learn from Truck Impacts]]; [[Find and Fix Vehicle Faults Without Downtime]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Prevent Tip-Overs and Overloads]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] | - |
| [[UniCarriers SCX N2 Stand-Up Counterbalanced Forklifts]] | - | - | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] | - |
| [[Yale ERC050-060VGL]] | [[Charge Without a Ventilated Battery Room]]; [[Know Battery State Before and During the Shift]] | - | [[Control Who Operates Each Truck]]; [[Find and Fix Vehicle Faults Without Downtime]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] | [[Keep Trucks Working Without Battery Maintenance Labor]] |
| [[Yale ERC080VHL]] | [[Stretch Truck Run Time per Charge]] | - | [[Control Who Operates Each Truck]]; [[Find and Fix Vehicle Faults Without Downtime]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] | - |

#### Forklifts/Class II Electric Narrow Aisle Trucks

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Crown RR-RD 5700 Series]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Keep the Operator Positioned and Able to See the Work]]; [[Prevent Tip-Overs and Overloads]] | - | - | - |
| [[Raymond 7000 Series Reach-Fork Trucks]] | [[Stretch Truck Run Time per Charge]] | - | - | - |
| [[Raymond Orderpickers]] | - | - | [[Keep Trucks Slow in Hazardous Zones]]; [[Warn the Operator of People and Objects Near the Truck]] | - |

#### Forklifts/Class III Electric Hand and Hand-Rider Trucks

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Raymond 8000 Series Pallet Trucks]] | [[Control Who Operates Each Truck]]; [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] | - | - | - |
| [[STILL EXH-SF Low Lift Pallet Truck]] | [[Control Who Operates Each Truck]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] | - | [[Detect and Learn from Truck Impacts]]; [[Find and Fix Vehicle Faults Without Downtime]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Prevent Tip-Overs and Overloads]] | - |

#### Fuel Cell Power Units/Hydrogen Fuel Cell Units

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Nuvera PowerEdge]] | [[Return Trucks to Service Quickly After a Low Charge]]; [[Stretch Truck Run Time per Charge]] | - | - | - |
| [[Plug Power GenDrive]] | [[Return Trucks to Service Quickly After a Low Charge]]; [[Stretch Truck Run Time per Charge]] | - | - | - |

#### Ground Support Equipment/Baggage and Tow Tractors

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Charlatte T135 Neo 25T]] | [[Stretch Truck Run Time per Charge]] | - | - | - |
| [[TUG Endurance Baggage Tractor]] | [[Find and Fix Vehicle Faults Without Downtime]]; [[Stretch Truck Run Time per Charge]] | - | - | - |

#### Ground Support Equipment/Belt Loaders

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Charlatte Belt Loaders]] | - | [[Charge Without a Ventilated Battery Room]] | - | - |
| [[Mallaghan SkyBelt]] | [[Find and Fix Vehicle Faults Without Downtime]] | - | [[Control Who Operates Each Truck]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Warn the Operator of People and Objects Near the Truck]] | - |
| [[TLD NBL-E Belt Loader]] | - | - | [[Detect and Learn from Truck Impacts]]; [[Keep Trucks Slow in Hazardous Zones]]; [[Protect Aircraft and Ground Crew During Ground Operations]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] | - |
| [[TLD RBL Electric Regional Belt Loader]] | - | - | [[Detect and Learn from Truck Impacts]]; [[Keep Trucks Slow in Hazardous Zones]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] | - |
| [[TUG 660 Belt Loader]] | [[Stretch Truck Run Time per Charge]] | - | [[Keep Trucks Slow in Hazardous Zones]]; [[Keep the Operator Positioned and Able to See the Work]]; [[Protect Aircraft and Ground Crew During Ground Operations]]; [[Warn the Operator of People and Objects Near the Truck]] | - |

#### Ground Support Equipment/Cargo Loaders

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Oshkosh AeroTech Commander 30i Cargo Loader]] | - | - | [[Control Who Operates Each Truck]]; [[Find and Fix Vehicle Faults Without Downtime]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Protect Aircraft and Ground Crew During Ground Operations]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - |
| [[Oshkosh AeroTech Ranger 15E Cargo Loader]] | - | - | [[Protect Aircraft and Ground Crew During Ground Operations]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - |

#### Ground Support Equipment/Pushback Tractors

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[TUG ALPHA 1 Pushback]] | [[Find and Fix Vehicle Faults Without Downtime]]; [[Know Battery State Before and During the Shift]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]] | - | - |

#### Vehicle Accessories/Access Control

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Panacea Smart Start]] | [[Control Who Operates Each Truck]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] | - | - | - |
| [[Toyota PIN Code Access Pad]] | [[Control Who Operates Each Truck]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] | - | - | - |

#### Vehicle Accessories/Cameras and Recorders

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Hangcha Backup Camera Option]] | [[Keep the Operator Positioned and Able to See the Work]] | - | - | - |
| [[Jungheinrich addedVIEW Camera Systems]] | [[Keep the Operator Positioned and Able to See the Work]] | - | - | - |
| [[Panacea Cam-DVR with Impact Sensors]] | [[Detect and Learn from Truck Impacts]]; [[Keep the Operator Positioned and Able to See the Work]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] | - | - | - |
| [[Raymond Vantage Point System]] | [[Keep the Operator Positioned and Able to See the Work]] | - | - | - |
| [[Toyota 360 Operating Camera]] | [[Keep the Operator Positioned and Able to See the Work]] | - | - | - |
| [[Toyota Carriage-Mounted Camera]] | [[Keep the Operator Positioned and Able to See the Work]] | - | - | - |

#### Vehicle Accessories/Cold Storage Packages

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Toyota Cold Conditioning Package]] | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] | - | - | - |
| [[UniCarriers Freezer Option]] | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] | - | - | - |

#### Vehicle Accessories/Operator Assist and Stability

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Cat Presence Detection System]] | [[Keep the Operator Positioned and Able to See the Work]] | - | - | - |
| [[Doosan Bobcat Mast Sway Control]] | [[Keep Trucks Slow in Hazardous Zones]] | - | - | - |
| [[Heli Operator Presence Sensing System]] | [[Keep the Operator Positioned and Able to See the Work]] | - | - | - |
| [[Hyster Dynamic Stability System]] | [[Prevent Tip-Overs and Overloads]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Jungheinrich curveCONTROL]] | [[Prevent Tip-Overs and Overloads]] | - | - | - |
| [[Komatsu Operator Presence Sensing System]] | [[Keep the Operator Positioned and Able to See the Work]] | - | - | - |
| [[Linde Load Management Advanced]] | [[Prevent Tip-Overs and Overloads]] | - | - | - |
| [[Linde Safety Pilot]] | [[Prevent Tip-Overs and Overloads]] | - | - | - |
| [[Linde System Control]] | [[Prevent Tip-Overs and Overloads]] | - | - | - |
| [[Mitsubishi Integrated Presence System]] | [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Oshkosh AeroTech APD Wheel Position Sensor]] | [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Oshkosh AeroTech JetDock]] | [[Protect Aircraft and Ground Crew During Ground Operations]] | - | - | - |
| [[Raymond Fork Tilt Leveling]] | [[Keep the Operator Positioned and Able to See the Work]] | - | - | - |
| [[Raymond Fork-Tip Laser Guide]] | [[Keep the Operator Positioned and Able to See the Work]] | - | - | - |
| [[Raymond Operator Compartment Sensor System]] | [[Keep the Operator Positioned and Able to See the Work]] | - | - | - |
| [[Raymond Travel Speed Control]] | [[Keep Trucks Slow in Hazardous Zones]] | - | - | - |
| [[Raymond Zoning and Positioning]] | [[Keep Trucks Slow in Hazardous Zones]] | - | - | - |
| [[Raymond iWAREHOUSE Integrated Tether System]] | [[Keep the Operator Positioned and Able to See the Work]] | - | - | - |
| [[STILL Curve Speed Control]] | [[Prevent Tip-Overs and Overloads]] | - | - | - |
| [[STILL Safety Assist]] | [[Control Who Operates Each Truck]]; [[Keep Trucks Slow in Hazardous Zones]]; [[Prevent Tip-Overs and Overloads]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Warn Pedestrians of an Approaching Truck]] | - | - | - |
| [[STILL Safety Packages]] | [[Prevent Tip-Overs and Overloads]]; [[Warn Pedestrians of an Approaching Truck]] | - | - | - |
| [[TLD ASD+ Assisted Docking]] | [[Protect Aircraft and Ground Crew During Ground Operations]] | - | - | - |
| [[Toyota Acu-Laser]] | [[Keep the Operator Positioned and Able to See the Work]] | - | - | - |
| [[Toyota Assist]] | [[Keep the Operator Positioned and Able to See the Work]]; [[Prevent Tip-Overs and Overloads]]; [[Warn the Operator of People and Objects Near the Truck]] | [[Stretch Truck Run Time per Charge]] | - | - |
| [[Toyota Auto Height Select]] | [[Keep the Operator Positioned and Able to See the Work]] | - | - | - |
| [[Toyota Compartment Sensing System]] | [[Keep the Operator Positioned and Able to See the Work]] | - | - | - |
| [[Toyota System of Active Stability]] | [[Prevent Tip-Overs and Overloads]] | - | - | - |
| [[UniCarriers Curve Control]] | [[Prevent Tip-Overs and Overloads]] | - | - | - |
| [[Yale Reliant Portfolio]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Prevent Tip-Overs and Overloads]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |

#### Vehicle Accessories/Operator Displays

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Crown InfoLink 7-inch Touch Display]] | [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[EnerSys Truck iQ]] | [[Know Battery State Before and During the Shift]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | - |
| [[Linde MT18 Multifunction Display]] | [[Know Battery State Before and During the Shift]] | - | - | - |

#### Vehicle Accessories/Power Source Interfaces

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Hyster Power Cellect]] | [[Integrate the Battery with Truck and Charger Controls]]; [[Prevent Battery Abuse and Premature Replacement]] | - | - | - |

#### Vehicle Accessories/Proximity and Object Detection

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Blaxtair Pedestrian Detection System]] | [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Crown ProximityAssist System]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Doosan Bobcat Pedestrian Detection Camera]] | [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Hyster Pedestrian Awareness Camera]] | [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Hyster Reaction]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Prevent Tip-Overs and Overloads]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[IRIS 860 Sensor Pack]] | [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Jungheinrich Pedestrian Detection System]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Jungheinrich Reverse Area Warning System]] | [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Jungheinrich zoneCONTROL]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Linde Motion Detection]] | [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Linde Safety Guard]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Linde Safety Guard Truck Unit]] | [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Linde Safety Guard Zone Marker]] | [[Keep Trucks Slow in Hazardous Zones]] | - | - | - |
| [[Mallaghan Collision Avoidance System]] | [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Oshkosh AeroTech APD Engine Cowling Sensors]] | [[Protect Aircraft and Ground Crew During Ground Operations]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Oshkosh AeroTech APD Forward Radar and Controller]] | [[Protect Aircraft and Ground Crew During Ground Operations]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Oshkosh AeroTech APD Pressure-Sensitive Front Bumper]] | [[Protect Aircraft and Ground Crew During Ground Operations]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Oshkosh AeroTech APD Wing and Fairing Sensors]] | [[Protect Aircraft and Ground Crew During Ground Operations]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Oshkosh AeroTech Aircraft Proximity Detection]] | [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Powerfleet Pedestrian Proximity Detection]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Raymond In-Aisle Detection System]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Raymond iWAREHOUSE Fieldsense]] | [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Raymond iWAREHOUSE ObjectSense]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[TLD Aircraft Safety Docking]] | [[Detect and Learn from Truck Impacts]]; [[Keep Trucks Slow in Hazardous Zones]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] | - | - | - |
| [[Textron Smart Sense]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Keep the Operator Positioned and Able to See the Work]]; [[Protect Aircraft and Ground Crew During Ground Operations]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Toyota Object Detection Radar]] | [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Toyota SEnS Pedestrian Detection]] | [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |
| [[Toyota SEnS+ Pedestrian and Object Detection]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] | - | - | - |

#### Vehicle Accessories/Warning Lights and Alerts

| Product | By function (F) | By design (D) | By option (O) | By metric (M) |
|---|---|---|---|---|
| [[Cat Safety Lighting Options]] | [[Warn Pedestrians of an Approaching Truck]] | - | - | - |
| [[Larson Explosion-Proof Blue LED Forklift Light]] | [[Warn Pedestrians of an Approaching Truck]] | - | - | - |
| [[Linde BlueSpot]] | [[Warn Pedestrians of an Approaching Truck]] | - | - | - |
| [[Linde Safety Guard Portable Unit]] | [[Warn Pedestrians of an Approaching Truck]] | - | - | - |
| [[Linde Safety Guard Static Unit]] | [[Warn Pedestrians of an Approaching Truck]] | - | - | - |
| [[Oshkosh AeroTech Ramp Visibility Lights]] | [[Warn Pedestrians of an Approaching Truck]] | - | - | - |
| [[Panacea Blue Warning Light]] | [[Warn Pedestrians of an Approaching Truck]] | - | - | - |
| [[Powerfleet Forklift Safety Lights]] | [[Warn Pedestrians of an Approaching Truck]] | - | - | - |
| [[STILL SafetyLight 4Plus]] | [[Warn Pedestrians of an Approaching Truck]] | - | - | - |
| [[STILL Warning Zone Light]] | [[Warn Pedestrians of an Approaching Truck]] | - | - | - |
| [[TVH Forklift Arrow Lights]] | [[Warn Pedestrians of an Approaching Truck]] | - | - | - |
| [[Toyota Forklift Lighting Options]] | [[Warn Pedestrians of an Approaching Truck]] | - | - | - |

### Products with no route to a need

- **Concrete products with no route (60):**
  - **Batteries/Flooded Lead-Acid Batteries** (6): [[Amaron Brute Hi-Life Battery]], [[Banner Traction Bull Bloc PzF]], [[Banner Traction Bull PzS]], [[EnerSys IRONCLAD Battery]], [[GS Yuasa Traction Battery (Europe)]], [[Leoch PzS Traction Battery]]
  - **Batteries/Lithium-Ion Batteries** (5): [[Cat Lithium-Ion Battery Option]], [[Exide Sonnenschein Lithium Battery]], [[Flux Power GSE Pack]], [[Green Cubes SAFEFlex PLUS Battery]], [[Raymond Energy Essentials Lithium-Ion Battery]]
  - **Batteries/Valve-Regulated Lead-Acid Batteries** (4): [[Banner Traction Bull PzV Gel]], [[Exide Element VRLA Battery]], [[Exide TENSOR xGEL Battery]], [[Stryten M-Series AGM210 Battery]]
  - **Battery Accessories/Electrolyte Circulation Systems** (3): [[Exide AIR Electrolyte Agitation System]], [[HOPPECKE trak air Electrolyte Circulation]], [[Midac EUW Electrolyte Circulation System]]
  - **Battery Accessories/Identification and Charge Interface Devices** (1): [[PosiCharge BMID 1]]
  - **Battery Accessories/Watering Systems** (1): [[Flow-Rite Maverick Battery Watering System]]
  - **Charger Accessories/Connector Accessories** (1): [[PosiCharge Modular Charge Cables]]
  - **Charger Accessories/Remote Controls and Indicators** (1): [[Crown V-HFM3 Wired Remote Control Kit]]
  - **Charger Accessories/Stands and Mounting** (1): [[Crown V-HFM3 Charger Stand]]
  - **Charger Accessories/Thermal Accessories** (1): [[PosiCharge Cooling Fan Box]]
  - **Chargers/Industrial Modular Chargers** (6): [[Exide Element HF Charger]], [[Linde Lithium-Ion Charger (9, 17 and 30 kW)]], [[PosiCharge High Voltage Power Station (AC)]], [[PosiCharge ProCore Solo]], [[Stryten EHF Charger]], [[Triathlon Lithium-Ion Charger for UniCarriers]]
  - **Chargers/On-board Chargers** (1): [[EnerSys NexSys COMpact Charger]]
  - **Fleet Software and Platforms/Battery and Charger Management** (3): [[Fronius Charge & Connect]], [[Philadelphia Scientific iBOS]], [[PosiCharge PosiConnect]]
  - **Forklifts/Class I Electric Rider Trucks** (2): [[Crown SC Series]], [[Linde 1293 Series (E20BHP and E25BHP)]]
  - **Forklifts/Class II Electric Narrow Aisle Trucks** (2): [[Crown RM-RMD 6000 Series]], [[Jungheinrich ETV C16 and C20]]
  - **Ground Support Equipment/Baggage and Tow Tractors** (4): [[Charlatte CBT350 AC Tow Tractor]], [[Charlatte T137-V3]], [[Linde P250 Electric Baggage Tractor]], [[Oshkosh AeroTech B80E Electric Baggage Tractor]]
  - **Ground Support Equipment/Pushback Tractors** (2): [[Charlatte CPB35E Pushback Tractor]], [[Oshkosh AeroTech Pushback B350E and B650E]]
  - **Vehicle Accessories/Cameras and Recorders** (1): [[Toyota Twistlock Snapshot Camera System]]
  - **Vehicle Accessories/Operator Assist and Stability** (7): [[Crown Capacity Data Monitor]], [[Komatsu Digital Load Scale]], [[Linde Dynamic Mast Control]], [[Oshkosh AeroTech Powered Handrail with Distance Sensor]], [[Raymond Load Weight Display]], [[Raymond Mast Lift Limit Switch with Bypass]], [[Toyota Load Weight Sensing]]
  - **Vehicle Accessories/Operator Convenience** (5): [[Jungheinrich easyPILOT]], [[Linde Rotating Operator Workstation]], [[Linde Smartphone Holder]], [[STILL EasyBelt]], [[UniCarriers In-Cab Accessories]]
  - **Vehicle Accessories/Operator Displays** (1): [[Crown Gena Operating System]]
  - **Vehicle Accessories/Power Source Interfaces** (1): [[PosiCharge DIY Fast Charge Kit]]
  - **Vehicle Accessories/Warning Lights and Alerts** (1): [[UniCarriers Lighting Packages]]
- **Abstract class and category notes (55):** not expected to link.
- **Functions performed by products but realizing no need yet (product count):** [[Measure Battery Temperature]] (31), [[Measure Battery Voltage]] (24), [[Transmit Battery Data Wirelessly]] (22), [[Alert on Abnormal Condition]] (19), [[Measure Battery Current]] (17), [[Equalize Battery on Schedule]] (12), [[Charge Battery Conventionally]] (12), [[Accumulate Amp-Hours]] (12), [[Sense Load Weight and Lift Height]] (7), [[Report Battery Temperature to Charger]] (6), [[Circulate Electrolyte]] (6), [[Program Travel, Lift and Tilt Speeds]] (5), [[Identify Battery by Voltage]] (5), [[Hold Truck on Slope]] (4), [[Configure Device from Mobile App or PC]] (4), [[Export Battery Data to PC]] (3), [[Desulfate Battery During Charge]] (3), [[Steer with Electric Power Assist]] (2), [[Estimate State of Health]] (2), [[Diagnose Battery During Charge]] (2), [[Damp Mast Oscillation]] (2), [[Cushion Fork Lowering]] (2), [[Complete Missed Equalization Automatically]] (2), [[Rotate Operator Workstation]] (1), [[Report Fuel Cell State to Truck]] (1), [[Reduce Wheel Slip]] (1), [[Reduce Speed When Seat Belt Is Unfastened]] (1), [[Measure Electrolyte Specific Gravity]] (1), [[Follow Operator Automatically]] (1), [[Float Charge Battery]] (1), [[Detect Foreign and Live Objects]] (1), [[Detect Battery Weight]] (1), [[Cut Power in an Emergency]] (1), [[Cut Lift at Programmed Height]] (1), [[Charge Battery Wirelessly]] (1).

### Challenges to the current state

- **Vendor claims are not needs.** Every need rests on a maker or dealer sentence. Direction: customer-side sources (IB-129).
- **Counting D and O as reached can overstate.** The owner decided in round 40 that design and option routes count as reached. D says a product has a part a function needs, not that it does the function (other parts may be missing). O says the product can be bought with something that does it, not that every unit has it. The per-product table keeps F, D and O in separate columns so the stronger evidence stays visible. M is a property on file and is not counted.
- **Battery properties stay metrics.** Round 27 retired property functions into metrics; closing battery gaps by adding functions would double-count them, so only device behaviors with a source were linked (BMS, onboard charger, heater, CAN output, electrolyte circulation).
- **Remaining GSE gaps are source gaps.** Several GSE notes rest on distributor lists that state only drawbar pull or battery size. Direction: OEM spec sheets (IB-138, Document Wishlist).
- **Role names are partly hypotheses.** Site Safety Manager has no source naming it; Dealer Sales Representative rests on dealer option lists (C106).

### Change history

- 2026-10-03: first generated map (round 39).
- 2026-10-03: owner decision (Q20): design and option routes count as reached; metric route stays a hypothesis column.
- 2026-10-03: round 40 gap review. Added routes D, O and M; linked 21 product notes to functions, designs or options from cited sources; added function [[Diagnose Vehicle Remotely]] and need [[Find and Fix Vehicle Faults Without Downtime]]; conflicts C107 to C110; backlog IB-136 to IB-140. See [[Research Change and Decision Tracker]].

## Aliases

- Customer need map
- Product need map


## Former ids
