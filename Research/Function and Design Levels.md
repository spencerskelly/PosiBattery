---
type: Info
subtype:
id: INFO-00220
uid: 20261003101711548skellyspencer
status: Draft
tags:
  - conventions
  - hierarchy
  - functions
  - designs
describes:
  - "[[Battery-Connected Product]]"
---

# Function and Design Levels

## Definition

How functions and designs are generalized into levels, which relationships connect the levels, and where function and design meet.

## Notes

- **Function levels:** goal (what the product family is for) -> general function (a family of behaviors) -> specific function (what a product note links to). Goal to general uses `hasChild` (one owner); general to specific uses `subtypeOf` (is-a). Products link only to specific functions; the general levels are rolled up.
- **Design levels:** general design class (classes can nest) -> specific design. Specific designs use `subtypeOf` to their class; products link only to specific designs.
- **Where function and design meet (Q16, resolved 2026-10-03):** a function depends on the designs it needs, written as `dependsOn` on the Function (inverse `dependencyOf` on the Design). Example from the owner: showing state of charge depends on a display; a low water level alert depends on a water level sensor. The rule and each dependency's basis are in [[Function Design Dependencies]]. The derived table below is the evidence side: which designs actually appear on products that perform each general function.
- **Rules for generalizing:** (1) create a general note only when at least two siblings share it; (2) name general functions as a verb phrase for the family and general designs as '<Topic> Design'; (3) a note has one general parent; if a specific note fits two, keep the stronger fit and say so in its body; (4) general notes carry no product links and no requirements; (5) when a new specific note is created, assign its general parent in the same step; (6) when a function needs a design, add the dependency and its basis to the register in the same step.
- **Round 18 changes:** 'Warning and Display Device Design' now has two classes (display devices; indicators and alarms); new classes for operator identification, operator presence sensing and vehicle state sensing; 'Stop Vehicle When Operator Leaves Seat' became 'Stop Vehicle When Operator Is Out of Position' (seat, compartment or tether).

**Function tree**

- **[[Deliver Energy to Vehicles]]** (goal)
  - [[Charge Battery]] (general): [[Charge Battery Conventionally]], [[Charge Battery Fast]], [[Charge Battery Wirelessly]], [[Charge Battery by Opportunity]], [[Charge Lithium-Ion Battery]], [[Charge in Cold Storage]]
  - [[Control Charge Profile]] (general): [[Charge Under BMS Control]], [[Compensate Charge for Battery Temperature]], [[Complete Missed Equalization Automatically]], [[Desulfate Battery During Charge]], [[Diagnose Battery During Charge]], [[Equalize Battery on Schedule]], [[Identify Battery by Voltage]]
  - [[Keep Charging Available and Safe]] (general): [[Continue Charging Through Module Fault]], [[Detect Foreign and Live Objects]]
  - [[Supply Vehicle Energy Without Charging]] (general): [[Deliver Constant Power Through Shift]], [[Recover Energy by Regeneration]], [[Refuel Truck Power Source in Minutes]], [[Report Fuel Cell State to Truck]]
  - [[Connect Battery Power Path]] (general): [[Connect Battery to Charger or Vehicle]], [[Manage Charging Cables]]
- **[[Know and Protect Battery Condition]]** (goal)
  - [[Sense Battery State]] (general): [[Accumulate Amp-Hours]], [[Detect Battery Weight]], [[Detect Cell Failure]], [[Detect Voltage Imbalance]], [[Estimate Remaining Run Time]], [[Estimate State of Charge]], [[Estimate State of Health]], [[Measure Battery Current]], [[Measure Battery Temperature]], [[Measure Battery Voltage]], [[Measure Electrolyte Specific Gravity]], [[Sense Electrolyte Level]]
  - [[Inform Users of Battery Condition]] (general): [[Alert on Abnormal Condition]], [[Alert on Low Electrolyte Level]], [[Calculate Battery Abuse Cycles]], [[Display Battery Status to Operator]], [[Indicate Battery Status Locally]], [[Track Equalization]]
  - [[Protect Battery from Harm]] (general): [[Command Vehicle Operating Limits over CAN]], [[Protect Battery from Deep Discharge]]
  - [[Maintain Battery Electrolyte]] (general): [[Circulate Electrolyte]], [[Water Battery Cells]]
- **[[Manage Fleet Use and Data]]** (goal)
  - [[Communicate Battery and Vehicle Data]] (general): [[Communicate Battery State over CAN]], [[Communicate with Charger]], [[Configure Device from Mobile App or PC]], [[Export Battery Data to PC]], [[Identify Battery to Charger]], [[Log Battery Events and Usage]], [[Report Battery Temperature to Charger]], [[Transmit Battery Data Wirelessly]], [[Upload Battery Data to Cloud Portal]]
  - [[Manage Fleet Use]] (general): [[Control Operator Access]], [[Manage Chargers Remotely]], [[Report Truck Telemetry]]
- **[[Protect People and Equipment Near Vehicles]]** (goal)
  - [[Sense Collision Risk and Events]] (general): [[Detect Pedestrians and Objects Near Truck]], [[Detect and Record Impacts]]
  - [[Limit Vehicle Motion Automatically]] (general): [[Limit Truck Speed Automatically]], [[Limit Vehicle Motion by Location Zone]], [[Slow Truck in Curves]], [[Slow and Stop Near Aircraft]], [[Stop Vehicle When Operator Is Out of Position]]
  - [[Warn People of Hazards]] (general): [[Alert Operator of Hazards]], [[Indicate Aircraft Proximity to Operator]], [[Warn Pedestrians of Approaching Truck]]
  - [[Maintain Vehicle Stability and Load Awareness]] (general): [[Restrict Lift When Load Exceeds Limit]], [[Sense Load Weight and Lift Height]], [[Stabilize Truck Dynamically]]
  - [[Support Operator View and Positioning]] (general): [[Assist Lift Positioning]], [[Show Camera View to Operator]]

**Design classes**

- **[[Battery Integrated Feature Design]]**: [[Battery Onboard Charger]], [[Hibernation Mode]], [[Integrated Battery Heater]], [[Integrated Battery Management System]]
- **[[Battery Sensor Element Design]]**: [[Capacitive Electrolyte Level Probe]], [[Electrolyte-Immersed Temperature Sensor]]
- **[[Battery Sensor Mounting Design]]**: [[Battery-Top Mounting]], [[Cable-Mounted Indicator Placement]], [[Harness Ring-Terminal Mounting]], [[Mid-Battery Voltage Tap]], [[Panel-Mount Gauge Form Factor]], [[Wrap-Around Cell Connector Probe]]
- **[[Charger Operator Interface Design]]**: [[Charger Status LED Bar]], [[Touchscreen Interface]]
- **[[Charger Power Stage Design]]**: [[Dual-Cable and Parallel Charging Configuration]], [[Modular Power Modules]], [[Multi-Voltage Output]], [[Silicon-Carbide Power Stage]]
- **[[Current Sensing Design]]**: [[External Shunt Current Sensing]], [[Hall-Effect Current Sensing]], [[Shuntless Current Sensing]], [[Split-Core Current Sensor]]
- **[[Data Handling Design]]**: [[Cloud Portal Integration]], [[Non-Volatile Event Memory]]
- **[[Enclosure and Mounting Design]]**: [[Acid-Resistant Sealed Housing]], [[Breakaway Connector]], [[Onboard Charger Mounting]], [[Outdoor-Rated Charger Enclosure]]
- **[[Fuel Cell Power Design]]**: [[Fuel Cell Hybrid Power Stage]], [[Hydrogen Storage Tank]], [[Onboard Fuel Level Gauge]]
- **[[Lead-Acid Battery Construction Design]]**: [[Extended Watering Interval]], [[Forced Electrolyte Circulation]], [[Gel Electrolyte]], [[Thin Plate Pure Lead Plates]], [[Tubular Plate Construction]]
- **[[Object and Proximity Sensing Design]]**: [[LiDAR Object Sensor]], [[Magnetic Field Detection Sensor]], [[Pedestrian Detection Camera]], [[Proximity Tag System]], [[Radar Object Sensor]], [[Stereoscopic Vision Sensor]], [[Ultrasonic Distance Sensor]]
- **[[Vehicle Control Device Design]]**: [[Active Stability Actuator]], [[Fork Laser Guide]], [[Regenerative Braking]]
  - **[[Operator Identification Design]]**: [[Fingerprint Reader]], [[RFID or PIN Access Reader]]
- **[[Vehicle State Sensing Design]]**: [[Hydraulic Pressure Load Sensor]], [[Impact Sensor]]
  - **[[Operator Presence Sensing Design]]**: [[Light-Beam Compartment Sensor]], [[Operator Sensing Floor Mat]]
- **[[Warning and Display Device Design]]**: 
  - **[[Display Device Design]]**: [[Integrated LCD Display]], [[Operator Touch Display]], [[Vehicle-Mounted Display]]
  - **[[Indicator and Alarm Design]]**: [[Aircraft Proximity Indicator Light]], [[Audible Alarm]], [[Floor-Projected Warning Light]], [[Interactive Warning Vest]], [[Local LED Indicator]]
- **[[Wired Interface Design]]**: [[CAN Interface]], [[CAN-LIN and Battery Bus Interface]], [[DC-Cable Power-Line Communication]], [[Infrared Data Port]], [[RS-232 and RS-485 Serial Interface]], [[USB Data Download]]
- **[[Wireless Interface Design]]**: [[900 MHz Industrial Wireless Interface]], [[Bluetooth Interface]], [[Cellular Communication Interface]], [[Light-Triggered Data Upload]], [[LoRa Interface]], [[Mobile App Interface]], [[NFC Interface]], [[Wi-Fi Interface]], [[ZigBee 2.4 GHz Interface]]

**Derived function to design association (general level)**

| General function | Specific functions | Products (count) | Designs that appear on those products (count of products) |
|---|---|---|---|
| [[Charge Battery]] | 6 | 30 | [[Modular Power Modules]] (10), [[Multi-Voltage Output]] (7), [[Charger Status LED Bar]] (4), [[Touchscreen Interface]] (3), [[USB Data Download]] (3) |
| [[Communicate Battery and Vehicle Data]] | 9 | 33 | [[Local LED Indicator]] (10), [[Cloud Portal Integration]] (8), [[Acid-Resistant Sealed Housing]] (7), [[Non-Volatile Event Memory]] (5), [[DC-Cable Power-Line Communication]] (5) |
| [[Connect Battery Power Path]] | 2 | 4 | none yet |
| [[Control Charge Profile]] | 7 | 25 | [[Modular Power Modules]] (8), [[Multi-Voltage Output]] (7), [[Charger Status LED Bar]] (4), [[DC-Cable Power-Line Communication]] (2), [[Touchscreen Interface]] (2) |
| [[Inform Users of Battery Condition]] | 6 | 28 | [[Local LED Indicator]] (14), [[Cloud Portal Integration]] (7), [[Audible Alarm]] (5), [[Acid-Resistant Sealed Housing]] (5), [[Bluetooth Low Energy Interface]] (4) |
| [[Keep Charging Available and Safe]] | 2 | 5 | [[Modular Power Modules]] (3), [[Dual-Cable and Parallel Charging Configuration]] (2), [[Touchscreen Interface]] (1), [[Charger Status LED Bar]] (1), [[Multi-Voltage Output]] (1) |
| [[Limit Vehicle Motion Automatically]] | 5 | 16 | [[LiDAR Object Sensor]] (4), [[Proximity Tag System]] (3), [[Floor-Projected Warning Light]] (1), [[Operator Touch Display]] (1), [[Interactive Warning Vest]] (1) |
| [[Maintain Battery Electrolyte]] | 2 | 8 | [[Forced Electrolyte Circulation]] (3) |
| [[Maintain Vehicle Stability and Load Awareness]] | 3 | 9 | [[Proximity Tag System]] (2), [[Fork Laser Guide]] (1), [[Radar Object Sensor]] (1), [[Regenerative Braking]] (1), [[Active Stability Actuator]] (1) |
| [[Manage Fleet Use]] | 3 | 17 | [[Multi-Voltage Output]] (5), [[Modular Power Modules]] (3), [[Charger Status LED Bar]] (3), [[Impact Sensor]] (3), [[Touchscreen Interface]] (2) |
| [[Protect Battery from Harm]] | 2 | 2 | [[CAN Interface]] (2), [[Hall-Effect Current Sensing]] (1), [[Bluetooth Low Energy Interface]] (1), [[ZigBee 2.4 GHz Interface]] (1), [[Local LED Indicator]] (1) |
| [[Sense Battery State]] | 12 | 39 | [[Local LED Indicator]] (13), [[Acid-Resistant Sealed Housing]] (8), [[Cloud Portal Integration]] (7), [[Non-Volatile Event Memory]] (5), [[DC-Cable Power-Line Communication]] (5) |
| [[Sense Collision Risk and Events]] | 2 | 23 | [[Impact Sensor]] (4), [[LiDAR Object Sensor]] (4), [[Proximity Tag System]] (3), [[Stereoscopic Vision Sensor]] (2), [[RFID or PIN Access Reader]] (1) |
| [[Supply Vehicle Energy Without Charging]] | 4 | 5 | [[Hydrogen Storage Tank]] (2), [[Fuel Cell Hybrid Power Stage]] (2), [[Operator Touch Display]] (1), [[Regenerative Braking]] (1), [[Onboard Fuel Level Gauge]] (1) |
| [[Support Operator View and Positioning]] | 2 | 7 | [[Fork Laser Guide]] (2), [[Impact Sensor]] (1), [[Radar Object Sensor]] (1), [[Regenerative Braking]] (1) |
| [[Warn People of Hazards]] | 3 | 15 | [[Floor-Projected Warning Light]] (4), [[LiDAR Object Sensor]] (3), [[Stereoscopic Vision Sensor]] (2), [[Proximity Tag System]] (2), [[Vehicle-Mounted Display]] (1) |

- **Not yet assigned a general parent:** functions none; designs [[Reverse-Polarity Protection]].

## Aliases

- Levels of function and design

## Former ids
