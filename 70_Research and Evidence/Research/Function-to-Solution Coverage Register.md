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

- **Functions:** 156. **99 have a linked solution** (a Design on the Function or on an ancestor Function); **57 do not**: 20 are goal or family functions with no performer (expected) and 37 have performers but no Design. (Before the 2026-10-14 charge-method and vehicle-behavior pass: 91 and 65.)
- **Designs:** 241 (three added in the charge-method and vehicle-behavior pass). **197 are tied to a Function** (directly or through a parent Design); 44 are not. (The 39-of-49 products figure from the first count was not recomputed.)
- Only 88 Designs link to a Function directly; the rest rely on a parent Design that does.

### Alternative solutions

- **The Design layer already holds the alternatives.** 45 general Designs have two or more child Designs that are different ways to do the same job. Largest by products carrying them:

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
| [[Fleet Software Design]] | 7 | 14 | [[Charge Scheduling and Prioritization Design]] (6); [[Vehicle Task Dispatch Design]] (5); [[Fleet State Dashboard Design]] (3); [[Warehouse System Data Interface Design]] (2); [[Fleet Sizing Analytics Design]] (1); [[Remote Vehicle Operation Link Design]] (1) |
| [[Battery Sensor Mounting Design]] | 7 | 12 | [[Battery-Top Mounting]] (4); [[Mid-Battery Voltage Tap]] (4); [[In-Cell Specific Gravity Probe]] (2); [[Wrap-Around Cell Connector Probe]] (2); [[Cable-Mounted Indicator Placement]] (1); [[Harness Ring-Terminal Mounting]] (1) |
| [[Electrolyte Level Sensing Design]] | 5 | 11 | [[Capacitive Electrolyte Level Probe]] (3); [[Cell-Connector Electrolyte Level Sensing]] (2); [[Electronic In-Cell Electrolyte Probe]] (2); [[Low-Current Electrolyte Level Input]] (2); [[Variable-Length Electrolyte Level Probe]] (2) |
| [[Battery Cell Watering Design]] | 3 | 10 | [[Float-Valve Single-Point Watering]] (5); [[Charger-Controlled Automatic Watering]] (3); [[Injector Level-Sensing Watering]] (2) |
| [[Current Sensing Design]] | 4 | 10 | [[Hall-Effect Current Sensing]] (4); [[Shuntless Current Sensing]] (3); [[External Shunt Current Sensing]] (2); [[Split-Core Current Sensor]] (2) |

- **At Function level there were first counted one true pair of alternatives (superseded, C270):** [[Circulate Electrolyte]] is linked to [[Air Injection Electrolyte Circulation]] and [[Forced Electrolyte Circulation]]. The other 14 Functions with two Designs are layered (a sensing or interface Design plus a specific control Design), not alternatives: for example [[Upload Battery Data to Cloud Portal]] uses a cloud upload Design on top of a wireless interface Design.
- **Alternatives that Functions do not yet point to.** For [[Connect Battery to Charger or Vehicle]] the vault has [[Manual Plug-In Charging]], [[Truck Charging Port]] and [[Automated Connector Charging]]; for charging without a person, [[Inductive Wireless Charging]], [[Conductive Auto-Contact Charging]] and [[Automated Battery Swap]]. The Functions are not linked to them, so the comparison cannot be traversed from the Function.

### Solutions that implement more than one Function

| Design | Products carrying it | Functions it supports |
|---|---|---|
| [[Inductive Wireless Charging]] | 11 | [[Charge Battery Wirelessly]]; [[Charge Wirelessly Despite Misalignment]]; [[Detect Foreign and Live Objects]]; [[Exchange Charge Control Data Between Pads]] |
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

### Functions with performers but no solution (37)

[[Equalize Battery on Schedule]] (13), [[Operate in Cold Storage]] (10), [[Charge Battery]] (8), [[Start and Stop Charge Automatically]] (8), [[Operate in Wet or Dusty Conditions]] (7), [[Identify Battery by Voltage]] (5), [[Illuminate Work Area]] (5), [[Charge in Cold Storage]] (4), [[Deliver Constant Power Through Shift]] (4), [[Disconnect Battery on Limit Violation]] (4), [[Sense Battery State]] (4), [[Guide Battery Selection and Rotation]] (3), [[Share Power Between Charging Stations]] (3), [[Shelter Operator from Weather]] (3), [[Communicate Battery and Vehicle Data]] (2), [[Cushion Fork Lowering]] (2), [[Damp Mast Oscillation]] (2), [[Declare Estimator Accuracy Basis]] (2), [[Diagnose Battery During Charge]] (2), [[Dock Automatically at Aircraft]] (2), [[Indicate Maintenance Due]] (2), [[Manage Charging Cables]] (2), [[Protect Battery from Harm]] (2), [[Calculate Charge and Discharge Current Limits]] (1), [[Charge Several Batteries from One Unit]] (1), [[Convert Traction Battery Voltage for Onboard Systems]] (1), [[Detect Isolation Fault]] (1), [[Float Charge Battery]] (1), [[Follow Vehicle Charge Setpoints over CANopen]] (1), [[Inform Users of Battery Condition]] (1), [[Manage Temperature During Fast Charging]] (1), [[Reduce Wheel Slip]] (1), [[Report Fuel Cell State to Truck]] (1), [[Rotate Operator Workstation]] (1), [[Scale Charge Power by Module Count]] (1), [[Segment Discharge Cycles]] (1), [[Support Operator View and Positioning]] (1).

- **Charge-method functions** (Charge Battery Fast, by Opportunity, Conventionally, Lithium-Ion) were linked on 2026-10-14 to two required Designs, [[Charger Power Stage Design]] and the new [[Charge Profile Control Design]] (parent of the four existing profile control Designs). This is analyst reasoning: no source states that a fast or opportunity charge needs both. The third part, a battery that accepts the rate, has no Design (IB-233).
- **Software functions** were modeled on 2026-10-14 under [[Fleet Software Design]]: charge scheduling, site power load management (four alternatives: platform control over a charger network, charger-group peer management, solar-matched charging, time-of-use shifting), task dispatch, warehouse data interface, fleet state dashboard, fleet sizing analytics and remote operation link. Report Truck Hours and Usage was already covered through its parent.
- **Vehicle behavior functions** were reviewed on 2026-10-14. The four speed-limit Functions are siblings under [[Limit Vehicle Speed Automatically]] split by trigger, not alternatives for one job: objects and people ([[Limit Truck Speed Automatically]] to [[Object and Proximity Sensing Design]]), zones ([[Limit Vehicle Motion by Location Zone]] to [[Proximity Tag System]]), curves ([[Slow Truck in Curves]] to the new [[Steering-Angle Curve Speed Control]]) and load or lift height ([[Adapt Speed to Load and Lift Height]], already linked). [[Stabilize Truck Dynamically]] has a true alternative pair: [[Active Stability Actuator]] (axle lock) and the new [[Stability-Limit Function Intervention]] (function limiting). Only 3 of 16 curve performers and 2 of 10 stability performers state a mechanism (C271).

### Applied 2026-10-14 (owner approved)

Seven high-confidence links, nine Function-to-Design pairs: Inductive Wireless Charging to four wireless-charging functions; Conductive Auto-Contact Charging, Automated Battery Swap, Manual Plug-In Charging, Electric Parking Brake and Fork Laser Guide each to one function; Active Cell Balancing and Passive Cell Balancing (alternatives) to Balance Cells. Each Function note says so.

Seven further pairs came from the software Design family above (owner: model all aspects).

### Applied 2026-10-14 (charge-method and vehicle-behavior pass, owner "y")

Three new Designs ([[Charge Profile Control Design]], [[Steering-Angle Curve Speed Control]], [[Stability-Limit Function Intervention]]) and 14 Function-to-Design pairs: four charge-method Functions to two Designs each; Slow Truck in Curves; Stabilize Truck Dynamically (three: axle lock, function limiting, steering-angle speed control); Limit Vehicle Motion by Location Zone to Proximity Tag System; Limit Truck Speed Automatically to Object and Proximity Sensing Design. The last two came from the proposed list below and are now removed from it. Function-level alternative pairs are now Circulate Electrolyte, Balance Cells and Stabilize Truck Dynamically (C270).

### Still proposed (not applied)

Proposals come from matching Design names to Functions and from how many of a Function's performers carry the Design; performer overlap alone gave false matches (for example Drop-In Battery Cavity against Hold Truck on Slope), so only name-plausible pairs are listed. Each link is an engineering judgment that the owner should confirm.

| Design | Function | Confidence | Basis |
|---|---|---|---|
| Ingress-Protected Drive Components | Operate in Wet or Dusty Conditions | medium | 4 of 7 performers |
| Integrated Battery Heater | Operate in Cold Storage | medium | 3 of 10 performers |
| Multi-Voltage Output | Identify Battery by Voltage | medium | 4 of 5 performers |
| Modular Power Modules | Scale Charge Power by Module Count; Charge Several Batteries from One Unit | medium | 1 performer each |
| Fuel Cell Hybrid Power Stage; Hydrogen Storage Tank | Deliver Constant Power Through Shift | medium | 2 of 4 performers |
| Standalone Battery Management System | Disconnect Battery on Limit Violation | medium | 2 of 4 performers |

### Gaps

- Designs without a Function are mostly construction properties of batteries ([[Tubular Plate Construction]], [[Gel Electrolyte]]) and packaging; they may belong with metrics, not Functions.
- Product-level solutions for Functions rest on each product note's source; the Design links carry the same sources as the product notes.

## Aliases

## Former ids
