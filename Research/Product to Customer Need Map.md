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

Derived map from each catalog product to the customer needs it serves, and from each need to the people who have it. Route: product `performs` a specific Function; a Use Case (subtype why) is `realizedBy` that Function; the Use Case `participants` lists the Actors.

## Notes

- **Status: derived and hypothesis.** The map is generated from links already in the vault. Needs are what makers and dealers say their products do, not what customers say they need (rule: a need becomes validated only with customer-side evidence, per the ruleset's path from source research to hypothesis to validated need). Provenance and conflicts: C101 to C106 in [[Battery Product Landscape Conflicts and Open Questions]].
- **Coverage:** 227 of 398 products (excluding the 26 abstract anatomy notes) reach at least one need. 55 do not because they are abstract class or category notes (expected), 96 are concrete products with no function link yet, and 20 have functions that no need realizes yet.
- **The count is a lower bound.** A product reaches a need only through functions a source states for it. A product with no function link may still serve a need.
- **Problem, for whom, one line each:** see the needs table. Role evidence status: source-stated (a vendor document names the role), source-implied (implied by what products do), or hypothesis (no source).

### Needs

| Need (Use Case, why) | Who has it | Operating segments (analyst crosswalk, hypothesis) | Products reaching it | Functions | Evidence kinds |
|---|---|---|---|---|---|
| [[Keep Trucks Working Without Battery Maintenance Labor]] | [[Maintenance Technician]], [[Fleet Operations Manager]] | Material-handling fleets; Battery-room and centralized charging; Mixed-chemistry fleets | 52 | 4 | V |
| [[Charge Without a Ventilated Battery Room]] | [[Fleet Operations Manager]], [[Forklift Operator]] | Material-handling fleets; Distributed and opportunity charging; Mixed-chemistry fleets | 20 | 2 | V |
| [[Return Trucks to Service Quickly After a Low Charge]] | [[Fleet Operations Manager]], [[Forklift Operator]] | Material-handling fleets; Airport eGSE fleets; Distributed and opportunity charging | 26 | 4 | V |
| [[Charge Each Battery Correctly for Its Chemistry and Condition]] | [[Maintenance Technician]], [[Fleet Operations Manager]] | Mixed-chemistry fleets; Battery-room and centralized charging | 27 | 4 | V |
| [[Prevent Battery Abuse and Premature Replacement]] | [[Maintenance Technician]], [[Fleet Operations Manager]] | Material-handling fleets; Battery-room and centralized charging; Mixed-chemistry fleets | 8 | 4 | V |
| [[Know Battery State Before and During the Shift]] | [[Forklift Operator]], [[Maintenance Technician]] | Material-handling fleets; Airport eGSE fleets | 31 | 4 | V |
| [[Document Battery Care for Warranty Compliance]] | [[Fleet Operations Manager]], [[Dealer Service Technician]] | Material-handling fleets; Battery-room and centralized charging | 32 | 3 | V |
| [[Monitor and Manage Chargers and Batteries Across Sites]] | [[Fleet Operations Manager]] | Material-handling fleets; Airport eGSE fleets; Battery-room and centralized charging | 44 | 3 | V |
| [[Control Who Operates Each Truck]] | [[Fleet Operations Manager]], [[Site Safety Manager]], [[Forklift Operator]] | Material-handling fleets | 26 | 3 | V |
| [[Detect and Learn from Truck Impacts]] | [[Site Safety Manager]], [[Fleet Operations Manager]] | Material-handling fleets | 10 | 1 | V |
| [[Warn the Operator of People and Objects Near the Truck]] | [[Forklift Operator]], [[Site Safety Manager]] | Material-handling fleets; Airport eGSE fleets | 32 | 2 | V + G |
| [[Warn Pedestrians of an Approaching Truck]] | [[Pedestrian Near Trucks]], [[Site Safety Manager]] | Material-handling fleets | 37 | 2 | V + G |
| [[Prevent Tip-Overs and Overloads]] | [[Forklift Operator]], [[Site Safety Manager]] | Material-handling fleets | 19 | 4 | V + G |
| [[Keep Trucks Slow in Hazardous Zones]] | [[Site Safety Manager]], [[Pedestrian Near Trucks]] | Material-handling fleets | 23 | 2 | V + G |
| [[Protect Aircraft and Ground Crew During Ground Operations]] | [[GSE Operator]], [[Fleet Operations Manager]] | Airport eGSE fleets | 7 | 3 | V |
| [[Keep the Operator Positioned and Able to See the Work]] | [[Forklift Operator]] | Material-handling fleets | 24 | 3 | V |
| [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] | [[Fleet Operations Manager]], [[Forklift Operator]] | Material-handling fleets; Airport eGSE fleets | 18 | 4 | V |
| [[Stretch Truck Run Time per Charge]] | [[Fleet Operations Manager]] | Material-handling fleets; Distributed and opportunity charging | 6 | 2 | V |
| [[Integrate the Battery with Truck and Charger Controls]] | [[Truck OEM Integration Engineer]] | Mixed-chemistry fleets | 15 | 3 | V |
| [[Retrofit Safety and Telematics Onto Existing Trucks]] | [[Dealer Sales Representative]], [[Dealer Service Technician]], [[Equipment Installer]] | Material-handling fleets; Mixed-chemistry fleets | 28 | 3 | V |
| [[Connect Chargers and Batteries Safely at the Site]] | [[Equipment Installer]], [[Forklift Operator]] | Battery-room and centralized charging; Distributed and opportunity charging; Airport eGSE fleets | 10 | 3 | V + manual |

Evidence kinds: V = vendor or dealer statement in product notes; G = government statistics showing the underlying problem exists; manual = a maker's installation or service manual.

### Roles

| Actor | Evidence status | Needs | Which |
|---|---|---|---|
| [[Vehicle Operator]] | source-stated | 0 | none (supertype or no need linked yet) |
| [[Forklift Operator]] | source-stated | 9 | [[Charge Without a Ventilated Battery Room]], [[Return Trucks to Service Quickly After a Low Charge]], [[Know Battery State Before and During the Shift]], [[Control Who Operates Each Truck]], [[Warn the Operator of People and Objects Near the Truck]], [[Prevent Tip-Overs and Overloads]], [[Keep the Operator Positioned and Able to See the Work]], [[Keep Equipment Working in Cold, Wet and Dusty Conditions]], [[Connect Chargers and Batteries Safely at the Site]] |
| [[GSE Operator]] | source-stated | 1 | [[Protect Aircraft and Ground Crew During Ground Operations]] |
| [[Pedestrian Near Trucks]] | source-stated | 2 | [[Warn Pedestrians of an Approaching Truck]], [[Keep Trucks Slow in Hazardous Zones]] |
| [[Maintenance Technician]] | source-stated | 4 | [[Keep Trucks Working Without Battery Maintenance Labor]], [[Charge Each Battery Correctly for Its Chemistry and Condition]], [[Prevent Battery Abuse and Premature Replacement]], [[Know Battery State Before and During the Shift]] |
| [[Fleet Operations Manager]] | source-stated | 12 | [[Keep Trucks Working Without Battery Maintenance Labor]], [[Charge Without a Ventilated Battery Room]], [[Return Trucks to Service Quickly After a Low Charge]], [[Charge Each Battery Correctly for Its Chemistry and Condition]], [[Prevent Battery Abuse and Premature Replacement]], [[Document Battery Care for Warranty Compliance]], [[Monitor and Manage Chargers and Batteries Across Sites]], [[Control Who Operates Each Truck]], [[Detect and Learn from Truck Impacts]], [[Protect Aircraft and Ground Crew During Ground Operations]], [[Keep Equipment Working in Cold, Wet and Dusty Conditions]], [[Stretch Truck Run Time per Charge]] |
| [[Site Safety Manager]] | hypothesis | 6 | [[Control Who Operates Each Truck]], [[Detect and Learn from Truck Impacts]], [[Warn the Operator of People and Objects Near the Truck]], [[Warn Pedestrians of an Approaching Truck]], [[Prevent Tip-Overs and Overloads]], [[Keep Trucks Slow in Hazardous Zones]] |
| [[Dealer Sales Representative]] | source-implied | 1 | [[Retrofit Safety and Telematics Onto Existing Trucks]] |
| [[Dealer Service Technician]] | source-stated | 2 | [[Document Battery Care for Warranty Compliance]], [[Retrofit Safety and Telematics Onto Existing Trucks]] |
| [[Equipment Installer]] | source-stated | 2 | [[Retrofit Safety and Telematics Onto Existing Trucks]], [[Connect Chargers and Batteries Safely at the Site]] |
| [[Truck OEM Integration Engineer]] | source-implied | 1 | [[Integrate the Battery with Truck and Charger Controls]] |

### Segments and needs (crosswalk to [[PosiCharge Market Segments and Jobs-to-Be-Done]])

The crosswalk is the analyst's reading, not a source statement. It exists so each segment in the earlier analysis can be tied to needs.

| Segment | Needs | Which |
|---|---|---|
| Material-handling fleets | 17 | [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Charge Without a Ventilated Battery Room]]; [[Return Trucks to Service Quickly After a Low Charge]]; [[Prevent Battery Abuse and Premature Replacement]]; [[Know Battery State Before and During the Shift]]; [[Document Battery Care for Warranty Compliance]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Control Who Operates Each Truck]]; [[Detect and Learn from Truck Impacts]]; [[Warn the Operator of People and Objects Near the Truck]]; [[Warn Pedestrians of an Approaching Truck]]; [[Prevent Tip-Overs and Overloads]]; [[Keep Trucks Slow in Hazardous Zones]]; [[Keep the Operator Positioned and Able to See the Work]]; [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Stretch Truck Run Time per Charge]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] |
| Airport eGSE fleets | 7 | [[Return Trucks to Service Quickly After a Low Charge]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Warn the Operator of People and Objects Near the Truck]]; [[Protect Aircraft and Ground Crew During Ground Operations]]; [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Connect Chargers and Batteries Safely at the Site]] |
| Mixed-chemistry fleets | 6 | [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Charge Without a Ventilated Battery Room]]; [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Prevent Battery Abuse and Premature Replacement]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] |
| Battery-room and centralized charging | 6 | [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Prevent Battery Abuse and Premature Replacement]]; [[Document Battery Care for Warranty Compliance]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Connect Chargers and Batteries Safely at the Site]] |
| Distributed and opportunity charging | 4 | [[Charge Without a Ventilated Battery Room]]; [[Return Trucks to Service Quickly After a Low Charge]]; [[Stretch Truck Run Time per Charge]]; [[Connect Chargers and Batteries Safely at the Site]] |

### Families

| Product family | Products | Reaching a need | Distinct needs reached |
|---|---|---|---|
| Batteries | 1 | 0 | 0 |
| Batteries/Flooded Lead-Acid Batteries | 24 | 4 | 2 |
| Batteries/Lithium-Ion Batteries | 27 | 5 | 4 |
| Batteries/Valve-Regulated Lead-Acid Batteries | 11 | 0 | 0 |
| Battery Accessories | 2 | 0 | 0 |
| Battery Accessories/Battery Management Systems | 1 | 0 | 0 |
| Battery Accessories/Connector Assemblies | 4 | 3 | 1 |
| Battery Accessories/Electrolyte Circulation Systems | 4 | 0 | 0 |
| Battery Accessories/Identification and Charge Interface Devices | 10 | 7 | 6 |
| Battery Accessories/Monitoring Devices | 27 | 26 | 7 |
| Battery Accessories/Protection and Disconnect Units | 1 | 0 | 0 |
| Battery Accessories/Telematics and Connectivity Devices | 2 | 1 | 2 |
| Battery Accessories/Thermal Management Devices | 1 | 0 | 0 |
| Battery Accessories/Water Level Monitors | 5 | 4 | 2 |
| Battery Accessories/Watering Systems | 8 | 6 | 1 |
| Battery-Connected Product.md | 1 | 0 | 0 |
| Charger Accessories | 1 | 0 | 0 |
| Charger Accessories/Cable Management | 2 | 1 | 1 |
| Charger Accessories/Connector Accessories | 2 | 0 | 0 |
| Charger Accessories/Remote Controls and Indicators | 4 | 2 | 1 |
| Charger Accessories/Stands and Mounting | 3 | 1 | 1 |
| Charger Accessories/Thermal Accessories | 2 | 0 | 0 |
| Chargers | 1 | 0 | 0 |
| Chargers/Industrial Modular Chargers | 37 | 29 | 8 |
| Chargers/Light-Duty Chargers | 4 | 3 | 4 |
| Chargers/On-board Chargers | 3 | 1 | 1 |
| Chargers/Wireless Chargers | 2 | 1 | 6 |
| Fleet Software and Platforms | 1 | 0 | 0 |
| Fleet Software and Platforms/Battery and Charger Management | 10 | 6 | 4 |
| Fleet Software and Platforms/Truck Telematics | 20 | 19 | 5 |
| Forklifts | 1 | 0 | 0 |
| Forklifts/Class I Electric Rider Trucks | 30 | 19 | 12 |
| Forklifts/Class II Electric Narrow Aisle Trucks | 6 | 2 | 4 |
| Forklifts/Class III Electric Hand and Hand-Rider Trucks | 3 | 2 | 3 |
| Forklifts/Class IV Internal Combustion Cushion Tire Trucks | 1 | 0 | 0 |
| Forklifts/Class V Internal Combustion Pneumatic Tire Trucks | 1 | 0 | 0 |
| Forklifts/Class VI Tractors | 1 | 0 | 0 |
| Forklifts/Class VII Rough Terrain Forklifts | 1 | 0 | 0 |
| Fuel Cell Power Units/Hydrogen Fuel Cell Units | 3 | 2 | 2 |
| Ground Support Equipment | 1 | 0 | 0 |
| Ground Support Equipment/Baggage and Tow Tractors | 7 | 0 | 0 |
| Ground Support Equipment/Belt Loaders | 6 | 0 | 0 |
| Ground Support Equipment/Cargo Loaders | 3 | 0 | 0 |
| Ground Support Equipment/Pushback Tractors | 4 | 0 | 0 |
| Vehicle Accessories | 1 | 0 | 0 |
| Vehicle Accessories/Access Control | 3 | 2 | 2 |
| Vehicle Accessories/Cameras and Recorders | 8 | 6 | 3 |
| Vehicle Accessories/Cold Storage Packages | 3 | 2 | 1 |
| Vehicle Accessories/Operator Assist and Stability | 37 | 29 | 8 |
| Vehicle Accessories/Operator Convenience | 6 | 0 | 0 |
| Vehicle Accessories/Operator Displays | 5 | 3 | 4 |
| Vehicle Accessories/Power Source Interfaces | 3 | 1 | 2 |
| Vehicle Accessories/Proximity and Object Detection | 29 | 28 | 8 |
| Vehicle Accessories/Warning Lights and Alerts | 14 | 12 | 1 |

### Per-product route

Generated list. The needs shown are the union over the product's functions.

#### Batteries/Flooded Lead-Acid Batteries

| Product | Needs reached (through its functions) |
|---|---|
| [[Deka HydraSaver Battery]] | [[Keep Trucks Working Without Battery Maintenance Labor]] |
| [[Exide MARATHON Battery]] | [[Keep Trucks Working Without Battery Maintenance Labor]] |
| [[HAWKER Perfect Plus Battery]] | [[Keep Trucks Working Without Battery Maintenance Labor]] |
| [[HOPPECKE trak uplift iQ Battery]] | [[Know Battery State Before and During the Shift]] |

#### Batteries/Lithium-Ion Batteries

| Product | Needs reached (through its functions) |
|---|---|
| [[EnerSys NexSys iON Battery]] | [[Integrate the Battery with Truck and Charger Controls]]; [[Prevent Battery Abuse and Premature Replacement]] |
| [[Hangcha Lithium Iron Phosphate Battery Pack]] | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] |
| [[Heli Lithium-Ion Battery]] | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] |
| [[Stryten M-Series Li610 Battery]] | [[Know Battery State Before and During the Shift]] |
| [[Toyota Lithium-Ion 5-35 Battery Series]] | [[Integrate the Battery with Truck and Charger Controls]] |

#### Battery Accessories/Connector Assemblies

| Product | Needs reached (through its functions) |
|---|---|
| [[Anderson SB Connector Series]] | [[Connect Chargers and Batteries Safely at the Site]] |
| [[Crown Battery Cables and Connectors]] | [[Connect Chargers and Batteries Safely at the Site]] |
| [[Midac End Leads]] | [[Connect Chargers and Batteries Safely at the Site]] |

#### Battery Accessories/Identification and Charge Interface Devices

| Product | Needs reached (through its functions) |
|---|---|
| [[AMETEK Prestolite Power BID]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]] |
| [[AMETEK Prestolite Power BID with Ah Accumulator]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Document Battery Care for Warranty Compliance]] |
| [[Crown V-Force BMID]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Document Battery Care for Warranty Compliance]]; [[Keep Trucks Working Without Battery Maintenance Labor]] |
| [[Fronius TagID]] | [[Keep Trucks Working Without Battery Maintenance Labor]] |
| [[PosiCharge BMID]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Document Battery Care for Warranty Compliance]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Know Battery State Before and During the Shift]] |
| [[PosiCharge Battery Rx]] | [[Document Battery Care for Warranty Compliance]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]] |
| [[PosiCharge PosiGuard]] | [[Document Battery Care for Warranty Compliance]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Monitor and Manage Chargers and Batteries Across Sites]] |

#### Battery Accessories/Monitoring Devices

| Product | Needs reached (through its functions) |
|---|---|
| [[AMETEK Prestolite Power Site Probe]] | [[Document Battery Care for Warranty Compliance]] |
| [[AMETEK Prestolite Power TruBid]] | [[Integrate the Battery with Truck and Charger Controls]]; [[Know Battery State Before and During the Shift]]; [[Prevent Battery Abuse and Premature Replacement]] |
| [[AMETEK Prestolite Power WBID]] | [[Document Battery Care for Warranty Compliance]]; [[Integrate the Battery with Truck and Charger Controls]] |
| [[AMETEK Prestolite Power WBID Pro]] | [[Document Battery Care for Warranty Compliance]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]] |
| [[Access Control Group CellTrac]] | [[Keep Trucks Working Without Battery Maintenance Labor]] |
| [[Access Control Group CellVue]] | [[Know Battery State Before and During the Shift]] |
| [[Advanced Charging Technologies BATTview]] | [[Document Battery Care for Warranty Compliance]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Monitor and Manage Chargers and Batteries Across Sites]] |
| [[Crown Battery Health Monitor]] | [[Document Battery Care for Warranty Compliance]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Monitor and Manage Chargers and Batteries Across Sites]] |
| [[EnerSys Wi-iQ]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Document Battery Care for Warranty Compliance]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Prevent Battery Abuse and Premature Replacement]] |
| [[EnerSys iQ Mini]] | [[Document Battery Care for Warranty Compliance]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Prevent Battery Abuse and Premature Replacement]] |
| [[Energywith withBMS BMU]] | [[Document Battery Care for Warranty Compliance]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Monitor and Manage Chargers and Batteries Across Sites]] |
| [[Exide Motion+ EasyMonitor]] | [[Document Battery Care for Warranty Compliance]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Prevent Battery Abuse and Premature Replacement]] |
| [[HOPPECKE trak collect]] | [[Document Battery Care for Warranty Compliance]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]] |
| [[Hyster Battery Tracker]] | [[Document Battery Care for Warranty Compliance]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]] |
| [[Inventus Smart Battery Monitor SBM-01]] | [[Integrate the Battery with Truck and Charger Controls]]; [[Know Battery State Before and During the Shift]] |
| [[Philadelphia Scientific eGO!Mini]] | [[Document Battery Care for Warranty Compliance]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]] |
| [[Philadelphia Scientific eGO!c]] | [[Document Battery Care for Warranty Compliance]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]] |
| [[Philadelphia Scientific eGO!core]] | [[Document Battery Care for Warranty Compliance]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Monitor and Manage Chargers and Batteries Across Sites]] |
| [[Philadelphia Scientific eGO!plus]] | [[Document Battery Care for Warranty Compliance]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]] |
| [[Philadelphia Scientific eGO!pro]] | [[Document Battery Care for Warranty Compliance]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]] |
| [[Power Designers PowerTrac 3]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Document Battery Care for Warranty Compliance]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Keep Trucks Working Without Battery Maintenance Labor]] |
| [[Power Designers PowerTrac DT3]] | [[Document Battery Care for Warranty Compliance]]; [[Know Battery State Before and During the Shift]] |
| [[Power Designers PowerTrac Monitor]] | [[Document Battery Care for Warranty Compliance]]; [[Know Battery State Before and During the Shift]] |
| [[Power Designers PowerTrac SP+]] | [[Document Battery Care for Warranty Compliance]]; [[Integrate the Battery with Truck and Charger Controls]]; [[Keep Trucks Working Without Battery Maintenance Labor]] |
| [[Raymond iBattery]] | [[Document Battery Care for Warranty Compliance]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]] |
| [[Yale Battery Vision]] | [[Document Battery Care for Warranty Compliance]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]]; [[Monitor and Manage Chargers and Batteries Across Sites]] |

#### Battery Accessories/Telematics and Connectivity Devices

| Product | Needs reached (through its functions) |
|---|---|
| [[Philadelphia Scientific eGO!gateway]] | [[Document Battery Care for Warranty Compliance]]; [[Monitor and Manage Chargers and Batteries Across Sites]] |

#### Battery Accessories/Water Level Monitors

| Product | Needs reached (through its functions) |
|---|---|
| [[Crown Battery Acid Indicators]] | [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]] |
| [[Flow-Rite Eagle Eye Elite IV]] | [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]] |
| [[Flow-Rite Eagle Eye Essential IV]] | [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]] |
| [[Philadelphia Scientific SmartBlinky Pro]] | [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Know Battery State Before and During the Shift]] |

#### Battery Accessories/Watering Systems

| Product | Needs reached (through its functions) |
|---|---|
| [[Crown V-Force Single Point Watering System]] | [[Keep Trucks Working Without Battery Maintenance Labor]] |
| [[Exide Automatic Watering System and Level Sensor]] | [[Keep Trucks Working Without Battery Maintenance Labor]] |
| [[Midac Aquamatic Watering System]] | [[Keep Trucks Working Without Battery Maintenance Labor]] |
| [[Philadelphia Scientific Stealth Watering System]] | [[Keep Trucks Working Without Battery Maintenance Labor]] |
| [[Philadelphia Scientific Water Injector System]] | [[Keep Trucks Working Without Battery Maintenance Labor]] |
| [[PosiCharge Single-Point Automatic Battery Watering]] | [[Keep Trucks Working Without Battery Maintenance Labor]] |

#### Charger Accessories/Cable Management

| Product | Needs reached (through its functions) |
|---|---|
| [[Crown Cable Management Accessories]] | [[Connect Chargers and Batteries Safely at the Site]] |

#### Charger Accessories/Remote Controls and Indicators

| Product | Needs reached (through its functions) |
|---|---|
| [[Crown V-HFM3 Tower Light Kit]] | [[Know Battery State Before and During the Shift]] |
| [[PosiCharge Three-Color Stack Light]] | [[Know Battery State Before and During the Shift]] |

#### Charger Accessories/Stands and Mounting

| Product | Needs reached (through its functions) |
|---|---|
| [[PosiCharge Charger Stand Kit and Cable Handler]] | [[Connect Chargers and Batteries Safely at the Site]] |

#### Chargers/Industrial Modular Chargers

| Product | Needs reached (through its functions) |
|---|---|
| [[ACT Quantum 2]] | [[Charge Without a Ventilated Battery Room]]; [[Connect Chargers and Batteries Safely at the Site]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Monitor and Manage Chargers and Batteries Across Sites]] |
| [[ACT Quantum 3]] | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Monitor and Manage Chargers and Batteries Across Sites]] |
| [[ACT Quantum Outdoor]] | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Monitor and Manage Chargers and Batteries Across Sites]] |
| [[AMETEK Prestolite Power Eclipse II]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Return Trucks to Service Quickly After a Low Charge]] |
| [[AMETEK Prestolite Power ULTRA]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Return Trucks to Service Quickly After a Low Charge]] |
| [[Crown Battery EVOLUTION Series]] | [[Return Trucks to Service Quickly After a Low Charge]] |
| [[Crown V-HFM3 Charger]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Return Trucks to Service Quickly After a Low Charge]] |
| [[Deka PowerForce Charger]] | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Return Trucks to Service Quickly After a Low Charge]] |
| [[EnerSys Express Charger]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Connect Chargers and Batteries Safely at the Site]]; [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Return Trucks to Service Quickly After a Low Charge]] |
| [[EnerSys IMPAQ Charger]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Connect Chargers and Batteries Safely at the Site]]; [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Return Trucks to Service Quickly After a Low Charge]] |
| [[EnerSys NexSys+ Charger]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Charge Without a Ventilated Battery Room]]; [[Connect Chargers and Batteries Safely at the Site]]; [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Return Trucks to Service Quickly After a Low Charge]] |
| [[Exide Motion+ Lithium Charger]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]] |
| [[Fronius SelectION]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]] |
| [[Fronius Selectiva 4.0]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Monitor and Manage Chargers and Batteries Across Sites]] |
| [[Green Cubes SAFEFlex Charger]] | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]] |
| [[HOPPECKE trak charger HF premium]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]] |
| [[PosiCharge DVS100]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Return Trucks to Service Quickly After a Low Charge]] |
| [[PosiCharge DVS150]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Document Battery Care for Warranty Compliance]] |
| [[PosiCharge DVS300 Series]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Return Trucks to Service Quickly After a Low Charge]] |
| [[PosiCharge High Voltage Power Station (DC)]] | [[Return Trucks to Service Quickly After a Low Charge]] |
| [[PosiCharge MVS400 and MVS800]] | [[Return Trucks to Service Quickly After a Low Charge]] |
| [[PosiCharge ProCore Edge]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Return Trucks to Service Quickly After a Low Charge]] |
| [[PosiCharge SVS100]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Return Trucks to Service Quickly After a Low Charge]] |
| [[PosiCharge SVS200]] | [[Keep Trucks Working Without Battery Maintenance Labor]] |
| [[Power Designers REVOLUTION X]] | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Return Trucks to Service Quickly After a Low Charge]] |
| [[Raymond Red Charger]] | [[Return Trucks to Service Quickly After a Low Charge]] |
| [[Stryten EHI Charger]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Return Trucks to Service Quickly After a Low Charge]] |
| [[Stryten X-3 Charger]] | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Return Trucks to Service Quickly After a Low Charge]] |
| [[Stryten X-7 Charger]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Return Trucks to Service Quickly After a Low Charge]] |

#### Chargers/Light-Duty Chargers

| Product | Needs reached (through its functions) |
|---|---|
| [[Delta-Q IC650]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]] |
| [[Exide Motion+ Premium Charger]] | [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]] |
| [[Lester Summit Series II]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Charge Without a Ventilated Battery Room]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Monitor and Manage Chargers and Batteries Across Sites]] |

#### Chargers/On-board Chargers

| Product | Needs reached (through its functions) |
|---|---|
| [[Heli Built-In Lithium Charger]] | [[Charge Without a Ventilated Battery Room]] |

#### Chargers/Wireless Chargers

| Product | Needs reached (through its functions) |
|---|---|
| [[EnerSys NexSys AIR Wireless Charger]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Charge Without a Ventilated Battery Room]]; [[Connect Chargers and Batteries Safely at the Site]]; [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Keep Trucks Working Without Battery Maintenance Labor]]; [[Return Trucks to Service Quickly After a Low Charge]] |

#### Fleet Software and Platforms/Battery and Charger Management

| Product | Needs reached (through its functions) |
|---|---|
| [[ACT ACTview]] | [[Monitor and Manage Chargers and Batteries Across Sites]] |
| [[PosiCharge E-Meter]] | [[Document Battery Care for Warranty Compliance]] |
| [[PosiCharge PosiLink]] | [[Document Battery Care for Warranty Compliance]]; [[Monitor and Manage Chargers and Batteries Across Sites]] |
| [[PosiCharge PosiNet]] | [[Document Battery Care for Warranty Compliance]]; [[Monitor and Manage Chargers and Batteries Across Sites]] |
| [[PosiCharge SkyLink]] | [[Monitor and Manage Chargers and Batteries Across Sites]] |
| [[Stryten inCOMMAND]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]]; [[Integrate the Battery with Truck and Charger Controls]] |

#### Fleet Software and Platforms/Truck Telematics

| Product | Needs reached (through its functions) |
|---|---|
| [[Adveez Asset and Operations Monitoring System]] | [[Control Who Operates Each Truck]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] |
| [[Crown InfoLink]] | [[Control Who Operates Each Truck]]; [[Detect and Learn from Truck Impacts]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] |
| [[Doosan Lin-Q]] | [[Control Who Operates Each Truck]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] |
| [[Hangcha FIMS]] | [[Control Who Operates Each Truck]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] |
| [[Heli Fleet Management System]] | [[Control Who Operates Each Truck]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] |
| [[Hyster Tracker Telemetry]] | [[Control Who Operates Each Truck]]; [[Detect and Learn from Truck Impacts]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] |
| [[Jungheinrich ISM Online]] | [[Control Who Operates Each Truck]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] |
| [[Komatsu KOMTRAX]] | [[Control Who Operates Each Truck]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] |
| [[Linde connect]] | [[Control Who Operates Each Truck]]; [[Detect and Learn from Truck Impacts]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] |
| [[Logisnext Lift Link]] | [[Control Who Operates Each Truck]]; [[Detect and Learn from Truck Impacts]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] |
| [[Oshkosh AeroTech iOPS]] | [[Control Who Operates Each Truck]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] |
| [[Powerfleet Forklift Gateway]] | [[Control Who Operates Each Truck]]; [[Detect and Learn from Truck Impacts]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] |
| [[Raymond iWAREHOUSE]] | [[Control Who Operates Each Truck]]; [[Detect and Learn from Truck Impacts]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] |
| [[Raymond iWAREHOUSE Real-Time Location System]] | [[Keep Trucks Slow in Hazardous Zones]] |
| [[STILL FleetManager]] | [[Control Who Operates Each Truck]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] |
| [[STILL Smart Portal]] | [[Control Who Operates Each Truck]]; [[Detect and Learn from Truck Impacts]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] |
| [[STILL neXXt fleet]] | [[Control Who Operates Each Truck]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] |
| [[Toyota MyInsights Telematics]] | [[Control Who Operates Each Truck]]; [[Detect and Learn from Truck Impacts]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] |
| [[Yale Vision Telemetry]] | [[Control Who Operates Each Truck]]; [[Monitor and Manage Chargers and Batteries Across Sites]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] |

#### Forklifts/Class I Electric Rider Trucks

| Product | Needs reached (through its functions) |
|---|---|
| [[Cat 2EPC5000-2EP6500 Electric Pneumatic Tire Lift Trucks]] | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Keep Trucks Slow in Hazardous Zones]]; [[Keep the Operator Positioned and Able to See the Work]] |
| [[Crown FC 5700 Series]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Prevent Tip-Overs and Overloads]] |
| [[Crown RC 5700 Series]] | [[Control Who Operates Each Truck]]; [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Keep Trucks Slow in Hazardous Zones]]; [[Prevent Battery Abuse and Premature Replacement]]; [[Prevent Tip-Overs and Overloads]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Stretch Truck Run Time per Charge]]; [[Warn Pedestrians of an Approaching Truck]] |
| [[Doosan Bobcat 7-Series Plus Electric Forklifts]] | [[Keep the Operator Positioned and Able to See the Work]]; [[Return Trucks to Service Quickly After a Low Charge]] |
| [[Doosan Bobcat NXE Series Electric Forklifts]] | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Prevent Tip-Overs and Overloads]] |
| [[Hangcha A Series Electric Forklifts]] | [[Return Trucks to Service Quickly After a Low Charge]]; [[Warn Pedestrians of an Approaching Truck]] |
| [[Hangcha XC Series Electric Forklifts]] | [[Control Who Operates Each Truck]]; [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Keep the Operator Positioned and Able to See the Work]]; [[Prevent Tip-Overs and Overloads]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Return Trucks to Service Quickly After a Low Charge]] |
| [[Heli A3 Series Lithium Forklifts]] | [[Charge Without a Ventilated Battery Room]]; [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] |
| [[Heli G Series Lithium Forklifts]] | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Prevent Tip-Overs and Overloads]] |
| [[Hyster J1.5-3.0UT(L)]] | [[Stretch Truck Run Time per Charge]] |
| [[Komatsu FB Series Electric Forklifts]] | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Keep Trucks Slow in Hazardous Zones]] |
| [[Linde 6-8 t Electric Counterbalance Forklifts]] | [[Know Battery State Before and During the Shift]] |
| [[Linde E Series Electric Counterbalance Forklifts]] | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] |
| [[Mitsubishi FBCS Stand-Up Counterbalanced Forklifts]] | [[Keep the Operator Positioned and Able to See the Work]] |
| [[Raymond 4000 Series Counterbalanced Trucks]] | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Keep the Operator Positioned and Able to See the Work]] |
| [[STILL RX 60 Electric Forklift]] | [[Control Who Operates Each Truck]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] |
| [[Toyota Traigo48]] | [[Return Trucks to Service Quickly After a Low Charge]] |
| [[Yale ERC050-060VGL]] | [[Charge Without a Ventilated Battery Room]]; [[Know Battery State Before and During the Shift]] |
| [[Yale ERC080VHL]] | [[Stretch Truck Run Time per Charge]] |

#### Forklifts/Class II Electric Narrow Aisle Trucks

| Product | Needs reached (through its functions) |
|---|---|
| [[Crown RR-RD 5700 Series]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Keep the Operator Positioned and Able to See the Work]]; [[Prevent Tip-Overs and Overloads]] |
| [[Raymond 7000 Series Reach-Fork Trucks]] | [[Stretch Truck Run Time per Charge]] |

#### Forklifts/Class III Electric Hand and Hand-Rider Trucks

| Product | Needs reached (through its functions) |
|---|---|
| [[Raymond 8000 Series Pallet Trucks]] | [[Control Who Operates Each Truck]]; [[Keep Equipment Working in Cold, Wet and Dusty Conditions]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] |
| [[STILL EXH-SF Low Lift Pallet Truck]] | [[Control Who Operates Each Truck]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] |

#### Fuel Cell Power Units/Hydrogen Fuel Cell Units

| Product | Needs reached (through its functions) |
|---|---|
| [[Nuvera PowerEdge]] | [[Return Trucks to Service Quickly After a Low Charge]]; [[Stretch Truck Run Time per Charge]] |
| [[Plug Power GenDrive]] | [[Return Trucks to Service Quickly After a Low Charge]]; [[Stretch Truck Run Time per Charge]] |

#### Vehicle Accessories/Access Control

| Product | Needs reached (through its functions) |
|---|---|
| [[Panacea Smart Start]] | [[Control Who Operates Each Truck]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] |
| [[Toyota PIN Code Access Pad]] | [[Control Who Operates Each Truck]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] |

#### Vehicle Accessories/Cameras and Recorders

| Product | Needs reached (through its functions) |
|---|---|
| [[Hangcha Backup Camera Option]] | [[Keep the Operator Positioned and Able to See the Work]] |
| [[Jungheinrich addedVIEW Camera Systems]] | [[Keep the Operator Positioned and Able to See the Work]] |
| [[Panacea Cam-DVR with Impact Sensors]] | [[Detect and Learn from Truck Impacts]]; [[Keep the Operator Positioned and Able to See the Work]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] |
| [[Raymond Vantage Point System]] | [[Keep the Operator Positioned and Able to See the Work]] |
| [[Toyota 360 Operating Camera]] | [[Keep the Operator Positioned and Able to See the Work]] |
| [[Toyota Carriage-Mounted Camera]] | [[Keep the Operator Positioned and Able to See the Work]] |

#### Vehicle Accessories/Cold Storage Packages

| Product | Needs reached (through its functions) |
|---|---|
| [[Toyota Cold Conditioning Package]] | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] |
| [[UniCarriers Freezer Option]] | [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] |

#### Vehicle Accessories/Operator Assist and Stability

| Product | Needs reached (through its functions) |
|---|---|
| [[Cat Presence Detection System]] | [[Keep the Operator Positioned and Able to See the Work]] |
| [[Doosan Bobcat Mast Sway Control]] | [[Keep Trucks Slow in Hazardous Zones]] |
| [[Heli Operator Presence Sensing System]] | [[Keep the Operator Positioned and Able to See the Work]] |
| [[Hyster Dynamic Stability System]] | [[Prevent Tip-Overs and Overloads]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] |
| [[Jungheinrich curveCONTROL]] | [[Prevent Tip-Overs and Overloads]] |
| [[Komatsu Operator Presence Sensing System]] | [[Keep the Operator Positioned and Able to See the Work]] |
| [[Linde Load Management Advanced]] | [[Prevent Tip-Overs and Overloads]] |
| [[Linde Safety Pilot]] | [[Prevent Tip-Overs and Overloads]] |
| [[Linde System Control]] | [[Prevent Tip-Overs and Overloads]] |
| [[Mitsubishi Integrated Presence System]] | [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] |
| [[Oshkosh AeroTech APD Wheel Position Sensor]] | [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] |
| [[Oshkosh AeroTech JetDock]] | [[Protect Aircraft and Ground Crew During Ground Operations]] |
| [[Raymond Fork Tilt Leveling]] | [[Keep the Operator Positioned and Able to See the Work]] |
| [[Raymond Fork-Tip Laser Guide]] | [[Keep the Operator Positioned and Able to See the Work]] |
| [[Raymond Operator Compartment Sensor System]] | [[Keep the Operator Positioned and Able to See the Work]] |
| [[Raymond Travel Speed Control]] | [[Keep Trucks Slow in Hazardous Zones]] |
| [[Raymond Zoning and Positioning]] | [[Keep Trucks Slow in Hazardous Zones]] |
| [[Raymond iWAREHOUSE Integrated Tether System]] | [[Keep the Operator Positioned and Able to See the Work]] |
| [[STILL Curve Speed Control]] | [[Prevent Tip-Overs and Overloads]] |
| [[STILL Safety Assist]] | [[Control Who Operates Each Truck]]; [[Keep Trucks Slow in Hazardous Zones]]; [[Prevent Tip-Overs and Overloads]]; [[Retrofit Safety and Telematics Onto Existing Trucks]]; [[Warn Pedestrians of an Approaching Truck]] |
| [[STILL Safety Packages]] | [[Prevent Tip-Overs and Overloads]]; [[Warn Pedestrians of an Approaching Truck]] |
| [[TLD ASD+ Assisted Docking]] | [[Protect Aircraft and Ground Crew During Ground Operations]] |
| [[Toyota Acu-Laser]] | [[Keep the Operator Positioned and Able to See the Work]] |
| [[Toyota Assist]] | [[Keep the Operator Positioned and Able to See the Work]]; [[Prevent Tip-Overs and Overloads]]; [[Warn the Operator of People and Objects Near the Truck]] |
| [[Toyota Auto Height Select]] | [[Keep the Operator Positioned and Able to See the Work]] |
| [[Toyota Compartment Sensing System]] | [[Keep the Operator Positioned and Able to See the Work]] |
| [[Toyota System of Active Stability]] | [[Prevent Tip-Overs and Overloads]] |
| [[UniCarriers Curve Control]] | [[Prevent Tip-Overs and Overloads]] |
| [[Yale Reliant Portfolio]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Prevent Tip-Overs and Overloads]]; [[Warn the Operator of People and Objects Near the Truck]] |

#### Vehicle Accessories/Operator Displays

| Product | Needs reached (through its functions) |
|---|---|
| [[Crown InfoLink 7-inch Touch Display]] | [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] |
| [[EnerSys Truck iQ]] | [[Know Battery State Before and During the Shift]]; [[Prevent Battery Abuse and Premature Replacement]] |
| [[Linde MT18 Multifunction Display]] | [[Know Battery State Before and During the Shift]] |

#### Vehicle Accessories/Power Source Interfaces

| Product | Needs reached (through its functions) |
|---|---|
| [[Hyster Power Cellect]] | [[Integrate the Battery with Truck and Charger Controls]]; [[Prevent Battery Abuse and Premature Replacement]] |

#### Vehicle Accessories/Proximity and Object Detection

| Product | Needs reached (through its functions) |
|---|---|
| [[Blaxtair Pedestrian Detection System]] | [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] |
| [[Crown ProximityAssist System]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] |
| [[Doosan Bobcat Pedestrian Detection Camera]] | [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] |
| [[Hyster Pedestrian Awareness Camera]] | [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] |
| [[Hyster Reaction]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Prevent Tip-Overs and Overloads]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] |
| [[IRIS 860 Sensor Pack]] | [[Warn the Operator of People and Objects Near the Truck]] |
| [[Jungheinrich Pedestrian Detection System]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Warn the Operator of People and Objects Near the Truck]] |
| [[Jungheinrich Reverse Area Warning System]] | [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] |
| [[Jungheinrich zoneCONTROL]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] |
| [[Linde Motion Detection]] | [[Warn the Operator of People and Objects Near the Truck]] |
| [[Linde Safety Guard]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] |
| [[Linde Safety Guard Truck Unit]] | [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] |
| [[Linde Safety Guard Zone Marker]] | [[Keep Trucks Slow in Hazardous Zones]] |
| [[Mallaghan Collision Avoidance System]] | [[Warn the Operator of People and Objects Near the Truck]] |
| [[Oshkosh AeroTech APD Engine Cowling Sensors]] | [[Protect Aircraft and Ground Crew During Ground Operations]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] |
| [[Oshkosh AeroTech APD Forward Radar and Controller]] | [[Protect Aircraft and Ground Crew During Ground Operations]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] |
| [[Oshkosh AeroTech APD Pressure-Sensitive Front Bumper]] | [[Protect Aircraft and Ground Crew During Ground Operations]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] |
| [[Oshkosh AeroTech APD Wing and Fairing Sensors]] | [[Protect Aircraft and Ground Crew During Ground Operations]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] |
| [[Oshkosh AeroTech Aircraft Proximity Detection]] | [[Warn the Operator of People and Objects Near the Truck]] |
| [[Powerfleet Pedestrian Proximity Detection]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Warn the Operator of People and Objects Near the Truck]] |
| [[Raymond In-Aisle Detection System]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Warn the Operator of People and Objects Near the Truck]] |
| [[Raymond iWAREHOUSE Fieldsense]] | [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] |
| [[Raymond iWAREHOUSE ObjectSense]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] |
| [[TLD Aircraft Safety Docking]] | [[Detect and Learn from Truck Impacts]]; [[Keep Trucks Slow in Hazardous Zones]]; [[Retrofit Safety and Telematics Onto Existing Trucks]] |
| [[Textron Smart Sense]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Keep the Operator Positioned and Able to See the Work]]; [[Protect Aircraft and Ground Crew During Ground Operations]]; [[Warn the Operator of People and Objects Near the Truck]] |
| [[Toyota Object Detection Radar]] | [[Warn the Operator of People and Objects Near the Truck]] |
| [[Toyota SEnS Pedestrian Detection]] | [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] |
| [[Toyota SEnS+ Pedestrian and Object Detection]] | [[Keep Trucks Slow in Hazardous Zones]]; [[Warn Pedestrians of an Approaching Truck]]; [[Warn the Operator of People and Objects Near the Truck]] |

#### Vehicle Accessories/Warning Lights and Alerts

| Product | Needs reached (through its functions) |
|---|---|
| [[Cat Safety Lighting Options]] | [[Warn Pedestrians of an Approaching Truck]] |
| [[Larson Explosion-Proof Blue LED Forklift Light]] | [[Warn Pedestrians of an Approaching Truck]] |
| [[Linde BlueSpot]] | [[Warn Pedestrians of an Approaching Truck]] |
| [[Linde Safety Guard Portable Unit]] | [[Warn Pedestrians of an Approaching Truck]] |
| [[Linde Safety Guard Static Unit]] | [[Warn Pedestrians of an Approaching Truck]] |
| [[Oshkosh AeroTech Ramp Visibility Lights]] | [[Warn Pedestrians of an Approaching Truck]] |
| [[Panacea Blue Warning Light]] | [[Warn Pedestrians of an Approaching Truck]] |
| [[Powerfleet Forklift Safety Lights]] | [[Warn Pedestrians of an Approaching Truck]] |
| [[STILL SafetyLight 4Plus]] | [[Warn Pedestrians of an Approaching Truck]] |
| [[STILL Warning Zone Light]] | [[Warn Pedestrians of an Approaching Truck]] |
| [[TVH Forklift Arrow Lights]] | [[Warn Pedestrians of an Approaching Truck]] |
| [[Toyota Forklift Lighting Options]] | [[Warn Pedestrians of an Approaching Truck]] |

### Products with no route to a need

- **Concrete products without a function link (96):**
  - **Batteries/Flooded Lead-Acid Batteries** (18): [[Amaron Brute Hi-Life Battery]], [[Banner Traction Bull Bloc PzF]], [[Banner Traction Bull PzS]], [[Crown V-Force Lead-Acid Battery]], [[Deka ChargeMate Battery]], [[Deka D-Series Battery]], [[Deka FastCharge Battery]], [[Deka MaintenanceSaver Battery]], [[Deka MaxPowr Battery]], [[EnerSys IRONCLAD Battery]], [[HOPPECKE trak uplift air Battery]], [[Leoch PzS Traction Battery]], [[Midac PzS Traction Battery]], [[Stryten M-Series F100 Battery]], [[Stryten M-Series F110 Battery]], [[Stryten M-Series T300 Battery]], [[Stryten M-Series T310 Battery]], [[Stryten M-Series T330 Battery]]
  - **Batteries/Lithium-Ion Batteries** (21): [[Cat Lithium-Ion Battery Option]], [[Crown V-Force Lithium-Ion ESS]], [[Deka Ready Power Lithium Battery]], [[Exide GNB Lithium Battery 2.0]], [[Exide Solition Light Traction Battery]], [[Exide Sonnenschein Lithium Battery]], [[Flux Power GSE Pack]], [[Flux Power LiFT Pack]], [[Flux Power S-Series Battery]], [[Godrej Lithium-Ion Forklift Battery]], [[Godrej Multi-Ion Forklift Battery]], [[Green Cubes GSE Lithium Battery]], [[Green Cubes SAFEFlex Battery]], [[Green Cubes SAFEFlex PLUS Battery]], [[HOPPECKE trak power Lithium Battery]], [[Jungheinrich Lithium-Ion Battery]], [[Linde 90 V Lithium-Ion Battery]], [[Raymond 8250 Lithium-Ion Battery]], [[Raymond Energy Essentials Lithium-Ion Battery]], [[Stryten M-Series Li600 Battery]], [[Triathlon Lithium-Ion Battery for UniCarriers]]
  - **Batteries/Valve-Regulated Lead-Acid Batteries** (10): [[Banner Traction Bull PzV Gel]], [[Deka Dominator Battery]], [[Deka Gel-Mate Battery]], [[Deka PowrMate Battery]], [[EnerSys NexSys TPPL Battery]], [[Exide Element VRLA Battery]], [[Exide TENSOR xGEL Battery]], [[Stryten M-Series AGM200 Battery]], [[Stryten M-Series AGM210 Battery]], [[Stryten M-Series AGM220 Battery]]
  - **Battery Accessories/Identification and Charge Interface Devices** (2): [[PosiCharge BMID 1]], [[PosiCharge BMID 3]]
  - **Battery Accessories/Watering Systems** (1): [[Flow-Rite Maverick Battery Watering System]]
  - **Charger Accessories/Connector Accessories** (1): [[PosiCharge Modular Charge Cables]]
  - **Charger Accessories/Remote Controls and Indicators** (1): [[Crown V-HFM3 Wired Remote Control Kit]]
  - **Charger Accessories/Stands and Mounting** (1): [[Crown V-HFM3 Charger Stand]]
  - **Charger Accessories/Thermal Accessories** (1): [[PosiCharge Cooling Fan Box]]
  - **Chargers/Industrial Modular Chargers** (4): [[Exide Element HF Charger]], [[Linde Lithium-Ion Charger (9, 17 and 30 kW)]], [[PosiCharge High Voltage Power Station (AC)]], [[Triathlon Lithium-Ion Charger for UniCarriers]]
  - **Chargers/On-board Chargers** (1): [[EnerSys NexSys COMpact Charger]]
  - **Fleet Software and Platforms/Battery and Charger Management** (2): [[Fronius Charge & Connect]], [[Philadelphia Scientific iBOS]]
  - **Forklifts/Class I Electric Rider Trucks** (8): [[Cat EP14-20 Electric Counterbalance Forklifts]], [[Cat EP25-55 80 V Electric Counterbalance Forklifts]], [[Crown SC Series]], [[Linde 1293 Series (E20BHP and E25BHP)]], [[Linde Ei Series]], [[Mitsubishi FBC Cushion Tire Electric Forklifts]], [[UniCarriers MX2 and MXL Series]], [[UniCarriers SCX N2 Stand-Up Counterbalanced Forklifts]]
  - **Forklifts/Class II Electric Narrow Aisle Trucks** (3): [[Crown RM-RMD 6000 Series]], [[Jungheinrich ETV C16 and C20]], [[Raymond Orderpickers]]
  - **Ground Support Equipment/Baggage and Tow Tractors** (6): [[Charlatte CBT350 AC Tow Tractor]], [[Charlatte T135 Neo 25T]], [[Charlatte T137-V3]], [[Linde P250 Electric Baggage Tractor]], [[Oshkosh AeroTech B80E Electric Baggage Tractor]], [[TUG Endurance Baggage Tractor]]
  - **Ground Support Equipment/Belt Loaders** (4): [[Charlatte Belt Loaders]], [[TLD NBL-E Belt Loader]], [[TLD RBL Electric Regional Belt Loader]], [[TUG 660 Belt Loader]]
  - **Ground Support Equipment/Cargo Loaders** (2): [[Oshkosh AeroTech Commander 30i Cargo Loader]], [[Oshkosh AeroTech Ranger 15E Cargo Loader]]
  - **Ground Support Equipment/Pushback Tractors** (3): [[Charlatte CPB35E Pushback Tractor]], [[Oshkosh AeroTech Pushback B350E and B650E]], [[TUG ALPHA 1 Pushback]]
  - **Vehicle Accessories/Cameras and Recorders** (1): [[Toyota Twistlock Snapshot Camera System]]
  - **Vehicle Accessories/Operator Assist and Stability** (1): [[Oshkosh AeroTech Powered Handrail with Distance Sensor]]
  - **Vehicle Accessories/Operator Convenience** (2): [[Linde Smartphone Holder]], [[UniCarriers In-Cab Accessories]]
  - **Vehicle Accessories/Operator Displays** (1): [[Crown Gena Operating System]]
  - **Vehicle Accessories/Power Source Interfaces** (1): [[PosiCharge DIY Fast Charge Kit]]
  - **Vehicle Accessories/Warning Lights and Alerts** (1): [[UniCarriers Lighting Packages]]
- **Products whose functions realize no need yet (20):**
  - **Batteries/Flooded Lead-Acid Batteries** (1): [[GS Yuasa Traction Battery (Europe)]]
  - **Battery Accessories/Electrolyte Circulation Systems** (3): [[Exide AIR Electrolyte Agitation System]], [[HOPPECKE trak air Electrolyte Circulation]], [[Midac EUW Electrolyte Circulation System]]
  - **Chargers/Industrial Modular Chargers** (3): [[PosiCharge ProCore Solo]], [[Stryten EHF Charger]], [[Stryten EHY Charger]]
  - **Fleet Software and Platforms/Battery and Charger Management** (1): [[PosiCharge PosiConnect]]
  - **Forklifts/Class I Electric Rider Trucks** (2): [[Mitsubishi FB 3-Wheel Electric Forklifts]], [[Toyota 3-Wheel Electric Forklift]]
  - **Ground Support Equipment/Belt Loaders** (1): [[Mallaghan SkyBelt]]
  - **Vehicle Accessories/Operator Assist and Stability** (6): [[Crown Capacity Data Monitor]], [[Komatsu Digital Load Scale]], [[Linde Dynamic Mast Control]], [[Raymond Load Weight Display]], [[Raymond Mast Lift Limit Switch with Bypass]], [[Toyota Load Weight Sensing]]
  - **Vehicle Accessories/Operator Convenience** (3): [[Jungheinrich easyPILOT]], [[Linde Rotating Operator Workstation]], [[STILL EasyBelt]]
- **Abstract class and category notes (55):** not expected to link; they organize families.
- **Functions performed by products but realizing no need yet (product count):** [[Measure Battery Temperature]] (29), [[Transmit Battery Data Wirelessly]] (22), [[Measure Battery Voltage]] (22), [[Alert on Abnormal Condition]] (19), [[Measure Battery Current]] (15), [[Equalize Battery on Schedule]] (12), [[Charge Battery Conventionally]] (12), [[Accumulate Amp-Hours]] (12), [[Sense Load Weight and Lift Height]] (7), [[Report Battery Temperature to Charger]] (6), [[Program Travel, Lift and Tilt Speeds]] (5), [[Identify Battery by Voltage]] (5), [[Circulate Electrolyte]] (5), [[Hold Truck on Slope]] (4), [[Configure Device from Mobile App or PC]] (4), [[Export Battery Data to PC]] (3), [[Display Truck Status to Operator]] (3), [[Desulfate Battery During Charge]] (3), [[Steer with Electric Power Assist]] (2), [[Estimate State of Health]] (2), [[Diagnose Battery During Charge]] (2), [[Damp Mast Oscillation]] (2), [[Cushion Fork Lowering]] (2), [[Complete Missed Equalization Automatically]] (2), [[Rotate Operator Workstation]] (1), [[Report Fuel Cell State to Truck]] (1), [[Reduce Wheel Slip]] (1), [[Reduce Speed When Seat Belt Is Unfastened]] (1), [[Measure Electrolyte Specific Gravity]] (1), [[Indicate Maintenance Due]] (1), [[Follow Operator Automatically]] (1), [[Float Charge Battery]] (1), [[Detect Foreign and Live Objects]] (1), [[Detect Battery Weight]] (1), [[Cut Power in an Emergency]] (1), [[Cut Lift at Programmed Height]] (1), [[Charge Battery Wirelessly]] (1).

### Challenges to the current state

- **Vendor claims are not needs.** Every need rests on a maker or dealer sentence. Direction: find customer-side sources (IB-129).
- **Safety needs have a government basis; most others do not.** BLS and OSHA figures show the safety problem exists, but they disagree with secondary sources (C101 to C104).
- **Role names are partly hypotheses.** Site Safety Manager has no source naming it; Dealer Sales Representative rests on dealer option lists (C106).
- **GSE is thin.** Only the aircraft-proximity needs reach GSE products; tractors, loaders and pushback units have no function links.
- **Battery makers' products are mostly unrouted.** Most lead-acid and lithium battery notes carry no function links, so battery customers' needs (life, maintenance, run time) are reached mainly through monitors, chargers and trucks.

### Change history

- 2026-10-03: first generated map. Method: Use Case (subtype why) realizedBy specific functions, participants Actors (owner decision on how to model needs). See [[Research Change and Decision Tracker]].

## Aliases

- Customer need map
- Product need map


## Former ids
