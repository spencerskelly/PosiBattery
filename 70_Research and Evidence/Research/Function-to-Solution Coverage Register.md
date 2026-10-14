---
type: Info
subtype: research
id: INFO-00948
uid: 20261014153541371skellyspencer
status: Draft
tags:
  - research-note
  - traceability
  - solutions
describes:
  - "[[Battery-Connected Product]]"
---

# Function-to-Solution Coverage Register

## Definition

Review of whether each Function in the vault has an identified solution (a Design that realizes it, and the Products that carry that Design), which alternative solutions exist, and which solutions serve more than one Function. Created 2026-10-14. The vault chain is Function, Design, Product: a Function `dependsOn` a Design, a Product is `designOf` that Design.

## Notes

### Counts

- **Functions:** 156. **74 have a linked solution** (a Design on the Function or on an ancestor Function); **82 do not**: 20 are goal or family functions with no performer (expected) and 62 have performers but no Design.
- **Designs:** 226. **174 are tied to a Function** (directly or through a parent Design); 52 are not, and 43 of those are carried by 108 products.
- Only 73 Designs link to a Function directly; the rest rely on a parent Design that does.

### Alternative solutions

- **The Design layer already holds the alternatives.** 43 general Designs have two or more child Designs that are different ways to do the same job. Largest by products carrying them:

| General Design | Child Designs | Products | Children (products carrying each) |
|---|---|---|---|
| [[Vehicle Energy Interface Design]] | 10 | 54 | [[Drop-In Battery Cavity]] (21); [[Inductive Wireless Charging]] (11); [[Manual Plug-In Charging]] (6); [[Truck Charging Port]] (6); [[Vehicle-Integrated Battery]] (5); [[Conductive Auto-Contact Charging]] (4) |
| [[Battery Integrated Feature Design]] | 4 | 37 | [[Integrated Battery Management System]] (18); [[Battery Onboard Charger]] (14); [[Integrated Battery Heater]] (7); [[Hibernation Mode]] (2) |
| [[Indicator and Alarm Design]] | 5 | 36 | [[Local LED Indicator]] (20); [[Floor-Projected Warning Light]] (10); [[Audible Alarm]] (9); [[Interactive Warning Vest]] (2); [[Aircraft Proximity Indicator Light]] (1) |
| [[Wireless Interface Design]] | 11 | 32 | [[Bluetooth Interface]] (8); [[Cellular Communication Interface]] (7); [[Mobile App Interface]] (7); [[Wi-Fi Interface]] (6); [[Wireless Battery Data Communication Design]] (6); [[ZigBee 2.4 GHz Interface]] (3) |
| [[Lead-Acid Battery Construction Design]] | 10 | 32 | [[Tubular Plate Construction]] (12); [[Forced Electrolyte Circulation]] (7); [[Gel Electrolyte]] (7); [[Extended Watering Interval]] (5); [[Thin Plate Pure Lead Plates]] (2); [[Copper Inserted Posts]] (1) |
| [[Data Handling Design]] | 9 | 30 | [[Current Integration Amp-Hour Accumulation]] (10); [[Non-Volatile Event Memory]] (10); [[Cloud Portal Integration]] (8); [[Equalization Event Tracking Design]] (7); [[Battery Abuse Cycle Analytics]] (5); [[Battery Event and Usage Logging Design]] (4) |
| [[Wired Interface Design]] | 8 | 29 | [[CAN Interface]] (12); [[DC-Cable Power-Line Communication]] (9); [[CAN Battery State Communication Design]] (8); [[USB Data Download]] (5); [[RS-232 and RS-485 Serial Interface]] (3); [[CAN Vehicle Operating Limit Command]] (2) |
| [[Battery Temperature Measurement Design]] | 6 | 21 | [[Electrolyte-Immersed Temperature Sensor]] (7); [[BMS Internal Temperature Sensing]] (4); [[External Thermistor Temperature Sensor]] (4); [[Internal Temperature Sensor]] (4); [[Ambient Temperature Sensor]] (2); [[Cell-Connector Temperature Sensing]] (2) |
| [[Object and Proximity Sensing Design]] | 7 | 21 | [[Proximity Tag System]] (5); [[LiDAR Object Sensor]] (4); [[Stereoscopic Vision Sensor]] (4); [[Radar Object Sensor]] (3); [[Ultrasonic Distance Sensor]] (3); [[Pedestrian Detection Camera]] (2) |
| [[Charger Power Stage Design]] | 4 | 20 | [[Modular Power Modules]] (12); [[Multi-Voltage Output]] (8); [[Dual-Cable and Parallel Charging Configuration]] (5); [[Silicon-Carbide Power Stage]] (2) |
| [[Enclosure and Mounting Design]] | 5 | 19 | [[Acid-Resistant Sealed Housing]] (8); [[Ingress-Protected Drive Components]] (4); [[Onboard Charger Mounting]] (3); [[Outdoor-Rated Charger Enclosure]] (3); [[Breakaway Connector]] (1) |
| [[Vehicle Operator Display Design]] | 3 | 19 | [[Vehicle-Mounted Display]] (10); [[Operator Touch Display]] (7); [[Battery Discharge Indicator]] (5) |
| [[Vehicle Control Device Design]] | 11 | 17 | [[Operator Access Authorization Design]] (4); [[Fork Laser Guide]] (3); [[Pre-Shift Checklist Enforcement Design]] (3); [[Programmable Motor Controller]] (2); [[Active Stability Actuator]] (1); [[Belt-Worn Remote Control]] (1) |
| [[Abnormal Condition Alert Design]] | 3 | 15 | [[Remote Exception Notification]] (8); [[Local Abnormal Condition Alert]] (5); [[Operator Dashboard Abnormal Alert]] (3) |
| [[Vehicle Drive Design]] | 4 | 14 | [[Regenerative Braking]] (6); [[AC Drive Motor]] (5); [[Electric Parking Brake]] (4); [[Electric Power Steering]] (2) |
| [[Battery Sensor Mounting Design]] | 7 | 12 | [[Battery-Top Mounting]] (4); [[Mid-Battery Voltage Tap]] (4); [[In-Cell Specific Gravity Probe]] (2); [[Wrap-Around Cell Connector Probe]] (2); [[Cable-Mounted Indicator Placement]] (1); [[Harness Ring-Terminal Mounting]] (1) |
| [[Electrolyte Level Sensing Design]] | 5 | 11 | [[Capacitive Electrolyte Level Probe]] (3); [[Cell-Connector Electrolyte Level Sensing]] (2); [[Electronic In-Cell Electrolyte Probe]] (2); [[Low-Current Electrolyte Level Input]] (2); [[Variable-Length Electrolyte Level Probe]] (2) |
| [[Battery Cell Watering Design]] | 3 | 10 | [[Float-Valve Single-Point Watering]] (5); [[Charger-Controlled Automatic Watering]] (3); [[Injector Level-Sensing Watering]] (2) |
| [[Current Sensing Design]] | 4 | 10 | [[Hall-Effect Current Sensing]] (4); [[Shuntless Current Sensing]] (3); [[External Shunt Current Sensing]] (2); [[Split-Core Current Sensor]] (2) |
| [[Device Configuration and Service Design]] | 2 | 10 | [[Mobile App Interface]] (7); [[PC Service Tool Interface]] (3) |

- **At Function level there is one true pair of alternatives:** [[Circulate Electrolyte]] is linked to [[Air Injection Electrolyte Circulation]] and [[Forced Electrolyte Circulation]]. The other 14 Functions with two Designs are layered (a sensing or interface Design plus a specific control Design), not alternatives: for example [[Upload Battery Data to Cloud Portal]] uses a cloud upload Design on top of a wireless interface Design.
- **Alternatives that Functions do not yet point to.** For [[Connect Battery to Charger or Vehicle]] the vault has [[Manual Plug-In Charging]], [[Truck Charging Port]] and [[Automated Connector Charging]]; for charging without a person, [[Inductive Wireless Charging]], [[Conductive Auto-Contact Charging]] and [[Automated Battery Swap]]. The Functions are not linked to them, so the comparison cannot be traversed from the Function.

### Solutions that implement more than one Function

| Design | Products carrying it | Functions it supports |
|---|---|---|
| [[Vehicle State Sensing Design]] | 0 | [[Adapt Speed to Load and Lift Height]]; [[Inhibit Drive Until Equipment Is Stowed]]; [[Restrict Lift When Load Exceeds Limit]]; [[Sense Load Weight and Lift Height]] |
| [[Wireless Interface Design]] | 1 | [[Diagnose Vehicle Remotely]]; [[Report Truck Telemetry]]; [[Transmit Battery Data Wirelessly]]; [[Upload Battery Data to Cloud Portal]] |
| [[Object and Proximity Sensing Design]] | 0 | [[Detect Pedestrians and Objects Near Truck]]; [[Slow and Stop Near Aircraft]]; [[Stop Truck for Detected Obstacle]] |
| [[CAN Interface]] | 12 | [[Command Vehicle Operating Limits over CAN]]; [[Communicate Battery State over CAN]] |
| [[Data Handling Design]] | 0 | [[Log Battery Events and Usage]]; [[Predict Battery Replacement Timing]] |
| [[Display Device Design]] | 0 | [[Enforce Pre-Shift Checklist]]; [[Show Camera View to Operator]] |
| [[Electrolyte Level Sensing Design]] | 1 | [[Alert on Low Electrolyte Level]]; [[Sense Electrolyte Level]] |
| [[Impact Sensor]] | 7 | [[Detect and Record Impacts]]; [[Lock Out Vehicle After Impact]] |
| [[Vehicle Operator Display Design]] | 1 | [[Display Battery Status to Operator]]; [[Display Truck Status to Operator]] |
| [[Warning and Display Device Design]] | 0 | [[Alert Operator of Hazards]]; [[Indicate Battery Status Locally]] |

- These are shared enabling Designs (a wireless link, a vehicle-state sensor, a display, a data store). The most reused Designs are not these but ones with no Function link: [[Drop-In Battery Cavity]], [[Local LED Indicator]], [[Floor-Projected Warning Light]].
- **Products that bundle many Functions** are monitors, battery ID devices and smart chargers; the top 15:

| Product | Functions performed | Designs |
|---|---|---|
| [[EnerSys Wi-iQ]] | 18 | 25 |
| [[HOPPECKE trak collect]] | 16 | 20 |
| [[Crown RC 5700 Series]] | 13 | 8 |
| [[PosiCharge Battery Rx]] | 12 | 8 |
| [[Power Designers PowerTrac 3]] | 12 | 12 |
| [[EnerSys NexSys AIR Wireless Charger]] | 12 | 2 |
| [[Exide Motion+ EasyMonitor]] | 11 | 9 |
| [[Hyster Battery Tracker]] | 11 | 4 |
| [[PosiCharge PosiGuard]] | 10 | 14 |
| [[Advanced Charging Technologies BATTview]] | 10 | 4 |
| [[Power Designers PowerTrac SP+]] | 10 | 11 |
| [[Philadelphia Scientific eGO!pro]] | 10 | 10 |
| [[EnerSys NexSys+ Charger]] | 10 | 6 |
| [[Crown V-Force BMID]] | 9 | 8 |
| [[Power Designers PowerTrac DT3]] | 9 | 10 |

- A product with many Functions and few Designs means the Designs are coarse or missing; a product with many Designs and few Functions means the Functions are not modeled.

### Functions with performers but no solution (62)

[[Charge Battery by Opportunity]] (34), [[Charge Battery Fast]] (33), [[Limit Truck Speed Automatically]] (26), [[Charge Lithium-Ion Battery]] (22), [[Charge Battery Conventionally]] (21), [[Slow Truck in Curves]] (16), [[Connect Battery to Charger or Vehicle]] (13), [[Equalize Battery on Schedule]] (13), [[Charge Battery Wirelessly]] (11), [[Operate in Cold Storage]] (10), [[Stabilize Truck Dynamically]] (10), [[Assist Lift Positioning]] (9), [[Balance Charging Power Across Site Capacity]] (9), [[Limit Vehicle Motion by Location Zone]] (9), [[Balance Cells]] (8), [[Charge Battery]] (8), [[Start and Stop Charge Automatically]] (8), [[Operate in Wet or Dusty Conditions]] (7), [[Schedule Charging Around Vehicle Readiness]] (6), [[Charge Battery by Automatic Contact]] (5), [[Charge Wirelessly Despite Misalignment]] (5), [[Dispatch Vehicles to Tasks]] (5), [[Hold Truck on Slope]] (5), [[Identify Battery by Voltage]] (5), [[Illuminate Work Area]] (5), [[Charge in Cold Storage]] (4), [[Deliver Constant Power Through Shift]] (4), [[Disconnect Battery on Limit Violation]] (4), [[Sense Battery State]] (4), [[Guide Battery Selection and Rotation]] (3), [[Share Power Between Charging Stations]] (3), [[Shelter Operator from Weather]] (3), [[Show Battery and Charger State in Fleet Software]] (3), [[Communicate Battery and Vehicle Data]] (2), [[Cushion Fork Lowering]] (2), [[Damp Mast Oscillation]] (2), [[Declare Estimator Accuracy Basis]] (2), [[Detect Foreign and Live Objects]] (2), [[Diagnose Battery During Charge]] (2), [[Dock Automatically at Aircraft]] (2), [[Exchange Battery Automatically]] (2), [[Exchange Charge Control Data Between Pads]] (2), [[Exchange Vehicle and Order Data with Warehouse System]] (2), [[Indicate Maintenance Due]] (2), [[Manage Charging Cables]] (2), [[Protect Battery from Harm]] (2), [[Calculate Charge and Discharge Current Limits]] (1), [[Charge Several Batteries from One Unit]] (1), [[Convert Traction Battery Voltage for Onboard Systems]] (1), [[Detect Isolation Fault]] (1), [[Float Charge Battery]] (1), [[Follow Vehicle Charge Setpoints over CANopen]] (1), [[Inform Users of Battery Condition]] (1), [[Manage Temperature During Fast Charging]] (1), [[Operate Truck Remotely]] (1), [[Reduce Wheel Slip]] (1), [[Report Fuel Cell State to Truck]] (1), [[Rotate Operator Workstation]] (1), [[Scale Charge Power by Module Count]] (1), [[Segment Discharge Cycles]] (1), [[Size Battery and Charger Fleet]] (1), [[Support Operator View and Positioning]] (1).

- **Charge-method functions** (Charge Battery Fast, by Opportunity, Conventionally, Lithium-Ion) have 21 to 34 performers and no Design: the solution is a combination of a power stage and a charge control profile, not a single Design. This needs an owner decision on how to model a combination.
- **Software functions** (Dispatch Vehicles to Tasks, Schedule Charging Around Vehicle Readiness, Balance Charging Power Across Site Capacity, Show Battery and Charger State in Fleet Software, Exchange Vehicle and Order Data with Warehouse System, Size Battery and Charger Fleet, Operate Truck Remotely) have no Design family at all; the Design layer has no software designs. A candidate family would be fleet software designs such as scheduler, load balancer, dispatcher and data gateway.
- **Vehicle behavior functions** (Limit Truck Speed Automatically with 26 performers, Slow Truck in Curves 16, Stabilize Truck Dynamically 10) rely on option notes, not Designs.

### Proposed Function-to-Design links (not applied)

Proposals come from matching Design names to Functions and from how many of a Function's performers carry the Design; performer overlap alone gave false matches (for example Drop-In Battery Cavity against Hold Truck on Slope), so only name-plausible pairs are listed. Each link is an engineering judgment that the owner should confirm.

| Design | Function | Confidence | Basis |
|---|---|---|---|
| Inductive Wireless Charging | Charge Battery Wirelessly; Charge Wirelessly Despite Misalignment; Detect Foreign and Live Objects; Exchange Charge Control Data Between Pads | high | 11 of 11 performers have it (misalignment 5 of 5, objects 2 of 2, pad data 2 of 2) |
| Conductive Auto-Contact Charging | Charge Battery by Automatic Contact | high | 4 of 5 performers |
| Automated Battery Swap | Exchange Battery Automatically | high | 2 of 2 performers |
| Manual Plug-In Charging | Connect Battery to Charger or Vehicle | high | 6 of 13 performers; alternatives are Truck Charging Port and Automated Connector Charging |
| Active Cell Balancing; Passive Cell Balancing | Balance Cells | high | alternatives; 2 and 1 products; Integrated Battery Management System also appears on 4 of 8 performers |
| Electric Parking Brake | Hold Truck on Slope | high | 3 of 5 performers |
| Fork Laser Guide | Assist Lift Positioning | high | 3 of 9 performers, name matches |
| Ingress-Protected Drive Components | Operate in Wet or Dusty Conditions | medium | 4 of 7 performers |
| Proximity Tag System | Limit Vehicle Motion by Location Zone | medium | 4 of 9 performers |
| Integrated Battery Heater | Operate in Cold Storage | medium | 3 of 10 performers |
| Multi-Voltage Output | Identify Battery by Voltage | medium | 4 of 5 performers |
| Modular Power Modules | Scale Charge Power by Module Count; Charge Several Batteries from One Unit | medium | 1 performer each |
| Fuel Cell Hybrid Power Stage; Hydrogen Storage Tank | Deliver Constant Power Through Shift | medium | 2 of 4 performers |
| Standalone Battery Management System | Disconnect Battery on Limit Violation | medium | 2 of 4 performers |
| Object and Proximity Sensing Design (LiDAR, radar, stereo vision) | Limit Truck Speed Automatically | medium | LiDAR 4 of 26 performers; the design is already linked to three other functions |

### Gaps

- Designs without a Function are mostly construction properties of batteries ([[Tubular Plate Construction]], [[Gel Electrolyte]]) and packaging; they may belong with metrics, not Functions.
- Product-level solutions for Functions rest on each product note's source; the Design links carry the same sources as the product notes.

## Aliases

## Former ids
