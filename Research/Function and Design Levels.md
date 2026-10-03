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
- **Design levels:** general design class -> specific design. Specific designs use `subtypeOf` to their class; products link only to specific designs.
- **Where function and design meet:** the schema has no Function-to-Design relationship (`realizedBy` is Use Case to Function or Design; `hasChild` is one-owner nesting; `includes` is membership). Today the join is the product: an Object `performs` functions and has designs. The table below derives the co-occurrence at the general level; it is evidence of association, not an assertion that a design realizes a function (Q16).
- **Rules for generalizing:** (1) create a general note only when at least two siblings share it; (2) name general functions as a verb phrase for the family and general designs as '<Topic> Design'; (3) a note has one general parent; if a specific note fits two, keep the stronger fit and say so in its body; (4) general notes carry no product links and no requirements; (5) when a new specific note is created, assign its general parent in the same step.
- **Open question (Q16):** how to tie a function to the designs that realize it. Options: keep deriving from products (current); list designs on a general function with `includes` (membership, a design may sit under several functions); add a provisional relationship such as `realizedByDesign`; or use the provisional `tracesTo`. Recommendation: keep deriving until the number of products makes the derived table unwieldy, then add the provisional relationship in the overlay schema.

**Function tree**

- **[[Protect People and Equipment Near Vehicles]]** (goal)
  - [[Sense Collision Risk and Events]] (general): [[Detect Pedestrians and Objects Near Truck]], [[Detect and Record Impacts]]
  - [[Limit Vehicle Motion Automatically]] (general): [[Limit Truck Speed Automatically]], [[Slow Truck in Curves]], [[Slow and Stop Near Aircraft]], [[Stop Vehicle When Operator Leaves Seat]]
  - [[Warn People of Hazards]] (general): [[Alert Operator of Hazards]], [[Warn Pedestrians of Approaching Truck]], [[Indicate Aircraft Proximity to Operator]]
  - [[Maintain Vehicle Stability and Load Awareness]] (general): [[Stabilize Truck Dynamically]], [[Sense Load Weight and Lift Height]]
  - [[Support Operator View and Positioning]] (general): [[Show Camera View to Operator]], [[Assist Lift Positioning]]
- **[[Know and Protect Battery Condition]]** (goal)
  - [[Sense Battery State]] (general): [[Measure Battery Voltage]], [[Measure Battery Current]], [[Measure Battery Temperature]], [[Sense Electrolyte Level]], [[Measure Electrolyte Specific Gravity]], [[Estimate State of Charge]], [[Estimate State of Health]], [[Estimate Remaining Run Time]], [[Accumulate Amp-Hours]], [[Detect Cell Failure]], [[Detect Voltage Imbalance]], [[Detect Battery Weight]]
  - [[Inform Users of Battery Condition]] (general): [[Indicate Battery Status Locally]], [[Display Battery Status to Operator]], [[Alert on Abnormal Condition]], [[Calculate Battery Abuse Cycles]], [[Track Equalization]]
  - [[Protect Battery from Harm]] (general): [[Protect Battery from Deep Discharge]], [[Command Vehicle Operating Limits over CAN]]
  - [[Maintain Battery Electrolyte]] (general): [[Water Battery Cells]], [[Circulate Electrolyte]]
- **[[Deliver Energy to Vehicles]]** (goal)
  - [[Charge Battery]] (general): [[Charge Battery Conventionally]], [[Charge Battery by Opportunity]], [[Charge Battery Fast]], [[Charge Lithium-Ion Battery]], [[Charge Battery Wirelessly]], [[Charge in Cold Storage]]
  - [[Control Charge Profile]] (general): [[Identify Battery by Voltage]], [[Compensate Charge for Battery Temperature]], [[Equalize Battery on Schedule]], [[Complete Missed Equalization Automatically]], [[Desulfate Battery During Charge]], [[Diagnose Battery During Charge]], [[Charge Under BMS Control]]
  - [[Keep Charging Available and Safe]] (general): [[Continue Charging Through Module Fault]], [[Detect Foreign and Live Objects]]
  - [[Supply Vehicle Energy Without Charging]] (general): [[Refuel Truck Power Source in Minutes]], [[Deliver Constant Power Through Shift]], [[Report Fuel Cell State to Truck]], [[Recover Energy by Regeneration]]
  - [[Connect Battery Power Path]] (general): [[Connect Battery to Charger or Vehicle]], [[Manage Charging Cables]]
- **[[Manage Fleet Use and Data]]** (goal)
  - [[Communicate Battery and Vehicle Data]] (general): [[Log Battery Events and Usage]], [[Transmit Battery Data Wirelessly]], [[Communicate Battery State over CAN]], [[Identify Battery to Charger]], [[Report Battery Temperature to Charger]], [[Communicate with Charger]], [[Export Battery Data to PC]], [[Upload Battery Data to Cloud Portal]], [[Configure Device from Mobile App or PC]]
  - [[Manage Fleet Use]] (general): [[Report Truck Telemetry]], [[Control Operator Access]], [[Manage Chargers Remotely]]

**Design classes**

- **[[Object and Proximity Sensing Design]]**: [[LiDAR Object Sensor]], [[Radar Object Sensor]], [[Stereoscopic Vision Sensor]], [[Pedestrian Detection Camera]], [[Ultrasonic Distance Sensor]], [[Proximity Tag System]]
- **[[Wireless Interface Design]]**: [[900 MHz Industrial Wireless Interface]], [[Bluetooth Interface]], [[Cellular Communication Interface]], [[LoRa Interface]], [[NFC Interface]], [[Wi-Fi Interface]], [[ZigBee 2.4 GHz Interface]], [[Mobile App Interface]], [[Light-Triggered Data Upload]]
- **[[Wired Interface Design]]**: [[CAN Interface]], [[CAN-LIN and Battery Bus Interface]], [[RS-232 and RS-485 Serial Interface]], [[Infrared Data Port]], [[DC-Cable Power-Line Communication]], [[USB Data Download]]
- **[[Data Handling Design]]**: [[Non-Volatile Event Memory]], [[Cloud Portal Integration]]
- **[[Current Sensing Design]]**: [[External Shunt Current Sensing]], [[Shuntless Current Sensing]], [[Hall-Effect Current Sensing]], [[Split-Core Current Sensor]]
- **[[Battery Sensor Mounting Design]]**: [[Battery-Top Mounting]], [[Harness Ring-Terminal Mounting]], [[Wrap-Around Cell Connector Probe]], [[Mid-Battery Voltage Tap]], [[Cable-Mounted Indicator Placement]], [[Panel-Mount Gauge Form Factor]]
- **[[Battery Sensor Element Design]]**: [[Electrolyte-Immersed Temperature Sensor]], [[Capacitive Electrolyte Level Probe]]
- **[[Charger Power Stage Design]]**: [[Modular Power Modules]], [[Silicon-Carbide Power Stage]], [[Multi-Voltage Output]], [[Dual-Cable and Parallel Charging Configuration]]
- **[[Charger Operator Interface Design]]**: [[Touchscreen Interface]], [[Charger Status LED Bar]]
- **[[Lead-Acid Battery Construction Design]]**: [[Tubular Plate Construction]], [[Thin Plate Pure Lead Plates]], [[Gel Electrolyte]], [[Extended Watering Interval]], [[Forced Electrolyte Circulation]]
- **[[Battery Integrated Feature Design]]**: [[Integrated Battery Management System]], [[Integrated Battery Heater]], [[Hibernation Mode]], [[Battery Onboard Charger]]
- **[[Enclosure and Mounting Design]]**: [[Acid-Resistant Sealed Housing]], [[Outdoor-Rated Charger Enclosure]], [[Onboard Charger Mounting]], [[Breakaway Connector]]
- **[[Warning and Display Device Design]]**: [[Floor-Projected Warning Light]], [[Interactive Warning Vest]], [[Aircraft Proximity Indicator Light]], [[Audible Alarm]], [[Local LED Indicator]], [[Integrated LCD Display]], [[Operator Touch Display]], [[Vehicle-Mounted Display]]
- **[[Vehicle Control Device Design]]**: [[RFID or PIN Access Reader]], [[Impact Sensor]], [[Active Stability Actuator]], [[Regenerative Braking]], [[Fork Laser Guide]]
- **[[Fuel Cell Power Design]]**: [[Fuel Cell Hybrid Power Stage]], [[Hydrogen Storage Tank]], [[Onboard Fuel Level Gauge]]

**Derived function to design association (general level)**

| General function | Specific functions | Products (count) | Designs that appear on those products (count of products) |
|---|---|---|---|
| [[Sense Collision Risk and Events]] | 2 | 13 | [[Impact Sensor]] (2), [[LiDAR Object Sensor]] (2), [[Proximity Tag System]] (2), [[RFID or PIN Access Reader]] (1), [[Fork Laser Guide]] (1) |
| [[Limit Vehicle Motion Automatically]] | 4 | 6 | [[LiDAR Object Sensor]] (2), [[Proximity Tag System]] (2), [[Floor-Projected Warning Light]] (1), [[Operator Touch Display]] (1), [[Interactive Warning Vest]] (1) |
| [[Warn People of Hazards]] | 3 | 8 | [[Floor-Projected Warning Light]] (2), [[LiDAR Object Sensor]] (2), [[Proximity Tag System]] (2), [[Operator Touch Display]] (1), [[Pedestrian Detection Camera]] (1) |
| [[Maintain Vehicle Stability and Load Awareness]] | 2 | 4 | [[Fork Laser Guide]] (1), [[Radar Object Sensor]] (1), [[Regenerative Braking]] (1), [[Active Stability Actuator]] (1), [[Proximity Tag System]] (1) |
| [[Support Operator View and Positioning]] | 2 | 1 | [[Fork Laser Guide]] (1), [[Radar Object Sensor]] (1), [[Regenerative Braking]] (1) |
| [[Sense Battery State]] | 12 | 37 | [[Local LED Indicator]] (12), [[Acid-Resistant Sealed Housing]] (8), [[Cloud Portal Integration]] (7), [[Non-Volatile Event Memory]] (5), [[DC-Cable Power-Line Communication]] (5) |
| [[Inform Users of Battery Condition]] | 5 | 27 | [[Local LED Indicator]] (13), [[Cloud Portal Integration]] (7), [[Acid-Resistant Sealed Housing]] (5), [[Bluetooth Low Energy Interface]] (4), [[Audible Alarm]] (4) |
| [[Protect Battery from Harm]] | 2 | 2 | [[CAN Interface]] (2), [[Hall-Effect Current Sensing]] (1), [[Bluetooth Low Energy Interface]] (1), [[ZigBee 2.4 GHz Interface]] (1), [[Local LED Indicator]] (1) |
| [[Charge Battery]] | 6 | 30 | [[Modular Power Modules]] (10), [[Multi-Voltage Output]] (7), [[Charger Status LED Bar]] (4), [[Touchscreen Interface]] (3), [[USB Data Download]] (3) |
| [[Control Charge Profile]] | 7 | 25 | [[Modular Power Modules]] (8), [[Multi-Voltage Output]] (7), [[Charger Status LED Bar]] (4), [[DC-Cable Power-Line Communication]] (2), [[Touchscreen Interface]] (2) |
| [[Keep Charging Available and Safe]] | 2 | 5 | [[Modular Power Modules]] (3), [[Dual-Cable and Parallel Charging Configuration]] (2), [[Touchscreen Interface]] (1), [[Charger Status LED Bar]] (1), [[Multi-Voltage Output]] (1) |
| [[Supply Vehicle Energy Without Charging]] | 4 | 5 | [[Hydrogen Storage Tank]] (2), [[Fuel Cell Hybrid Power Stage]] (2), [[Operator Touch Display]] (1), [[Regenerative Braking]] (1), [[Onboard Fuel Level Gauge]] (1) |
| [[Communicate Battery and Vehicle Data]] | 9 | 33 | [[Local LED Indicator]] (10), [[Cloud Portal Integration]] (8), [[Acid-Resistant Sealed Housing]] (7), [[Non-Volatile Event Memory]] (5), [[DC-Cable Power-Line Communication]] (5) |
| [[Manage Fleet Use]] | 3 | 13 | [[Multi-Voltage Output]] (5), [[Modular Power Modules]] (3), [[Charger Status LED Bar]] (3), [[Touchscreen Interface]] (2), [[Impact Sensor]] (2) |
| [[Maintain Battery Electrolyte]] | 2 | 0 | none yet |
| [[Connect Battery Power Path]] | 2 | 0 | none yet |

- **Not yet assigned a general parent:** functions none; designs [[Reverse-Polarity Protection]].

## Aliases

- Levels of function and design

## Former ids
