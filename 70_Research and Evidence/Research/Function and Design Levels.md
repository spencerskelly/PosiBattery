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
  - [[Charge Battery]] (general): [[Charge Battery Conventionally]], [[Charge Battery Fast]], [[Charge Battery Wirelessly]], [[Charge Battery by Opportunity]], [[Charge Battery from Standard Power Outlet]], [[Charge Lithium-Ion Battery]], [[Charge in Cold Storage]]
  - [[Control Charge Profile]] (general): [[Adapt Charge to Battery Condition]], [[Charge Under BMS Control]], [[Compensate Charge for Battery Temperature]], [[Complete Missed Equalization Automatically]], [[Desulfate Battery During Charge]], [[Diagnose Battery During Charge]], [[Equalize Battery on Schedule]], [[Float Charge Battery]], [[Identify Battery by Voltage]]
  - [[Keep Charging Available and Safe]] (general): [[Continue Charging Through Module Fault]], [[Detect Foreign and Live Objects]], [[Manage Temperature During Fast Charging]]
  - [[Supply Vehicle Energy Without Charging]] (general): [[Change Battery Quickly]], [[Deliver Constant Power Through Shift]], [[Recover Energy by Regeneration]], [[Refuel Truck Power Source in Minutes]], [[Report Fuel Cell State to Truck]]
  - [[Connect Battery Power Path]] (general): [[Adapt Truck to Battery Chemistry]], [[Connect Battery to Charger or Vehicle]], [[Manage Charging Cables]]
- **[[Keep Equipment Working in Its Environment]]** (goal)
  - [[Operate in Harsh Conditions]] (general): [[Operate in Cold Storage]], [[Operate in Wet or Dusty Conditions]], [[Shelter Operator from Weather]]
- **[[Know and Protect Battery Condition]]** (goal)
  - [[Sense Battery State]] (general): [[Accumulate Amp-Hours]], [[Detect Battery Weight]], [[Detect Cell Failure]], [[Detect Voltage Imbalance]], [[Estimate Remaining Run Time]], [[Estimate State of Charge]], [[Estimate State of Health]], [[Measure Battery Current]], [[Measure Battery Temperature]], [[Measure Battery Voltage]], [[Measure Electrolyte Specific Gravity]], [[Sense Electrolyte Level]]
  - [[Inform Users of Battery Condition]] (general): [[Alert on Abnormal Condition]], [[Alert on Low Electrolyte Level]], [[Calculate Battery Abuse Cycles]], [[Display Battery Status to Operator]], [[Indicate Battery Status Locally]], [[Predict Battery Replacement Timing]], [[Track Equalization]]
  - [[Protect Battery from Harm]] (general): [[Command Vehicle Operating Limits over CAN]], [[Protect Battery from Deep Discharge]]
  - [[Maintain Battery Electrolyte]] (general): [[Circulate Electrolyte]], [[Water Battery Cells]]
- **[[Manage Fleet Use and Data]]** (goal)
  - [[Communicate Battery and Vehicle Data]] (general): [[Communicate Battery State over CAN]], [[Communicate with Charger]], [[Configure Device from Mobile App or PC]], [[Export Battery Data to PC]], [[Identify Battery to Charger]], [[Log Battery Events and Usage]], [[Report Battery Temperature to Charger]], [[Transmit Battery Data Wirelessly]], [[Upload Battery Data to Cloud Portal]]
  - [[Manage Fleet Use]] (general): [[Control Charger from Remote Panel]], [[Control Operator Access]], [[Diagnose Vehicle Remotely]], [[Enforce Pre-Shift Checklist]], [[Indicate Charger Status Locally]], [[Lock Out Vehicle After Impact]], [[Manage Chargers Remotely]], [[Record Images of Load Handling]], [[Report Truck Telemetry]]
- **[[Protect People and Equipment Near Vehicles]]** (goal)
  - [[Sense Collision Risk and Events]] (general): [[Detect Pedestrians and Objects Near Truck]], [[Detect and Record Impacts]]
  - [[Limit Vehicle Speed Automatically]] (general): [[Adapt Speed to Load and Lift Height]], [[Limit Truck Speed Automatically]], [[Limit Vehicle Motion by Location Zone]], [[Program Travel, Lift and Tilt Speeds]], [[Reduce Speed When Seat Belt Is Unfastened]], [[Slow Truck in Curves]]
  - [[Warn People of Hazards]] (general): [[Alert Operator of Hazards]], [[Indicate Aircraft Proximity to Operator]], [[Warn Pedestrians of Approaching Truck]]
  - [[Maintain Vehicle Stability and Load Awareness]] (general): [[Cushion Fork Lowering]], [[Cut Lift at Programmed Height]], [[Damp Mast Oscillation]], [[Restrict Lift When Load Exceeds Limit]], [[Sense Load Weight and Lift Height]], [[Stabilize Truck Dynamically]]
  - [[Hold or Stop Vehicle Automatically]] (general): [[Cut Power in an Emergency]], [[Hold Truck on Slope]], [[Inhibit Drive Until Equipment Is Stowed]], [[Reduce Wheel Slip]], [[Slow and Stop Near Aircraft]], [[Stop Truck for Detected Obstacle]], [[Stop Vehicle When Operator Is Out of Position]]
- **[[Support the Operator]]** (goal)
  - [[Support Operator View and Positioning]] (general): [[Assist Lift Positioning]], [[Illuminate Work Area]], [[Show Camera View to Operator]]
  - [[Reduce Operator Effort]] (general): [[Dock Automatically at Aircraft]], [[Follow Operator Automatically]], [[Rotate Operator Workstation]], [[Steer with Electric Power Assist]]
  - [[Inform Operator of Truck Condition]] (general): [[Display Truck Status to Operator]], [[Indicate Maintenance Due]]

**Design classes**

- **[[Battery Integrated Feature Design]]**: [[Battery Onboard Charger]], [[Hibernation Mode]], [[Integrated Battery Heater]], [[Integrated Battery Management System]]
- **[[Electrolyte Level Sensing Design]]**: [[Capacitive Electrolyte Level Probe]], [[Cell-Connector Electrolyte Level Sensing]], [[Electronic In-Cell Electrolyte Probe]], [[Low-Current Electrolyte Level Input]], [[Variable-Length Electrolyte Level Probe]]
- **[[Battery Sensor Mounting Design]]**: [[Battery-Top Mounting]], [[Cable-Mounted Indicator Placement]], [[Harness Ring-Terminal Mounting]], [[Mid-Battery Voltage Tap]], [[Panel-Mount Gauge Form Factor]], [[Wrap-Around Cell Connector Probe]]
- **[[Abnormal Condition Alert Design]]**: [[Local Abnormal Condition Alert]], [[Operator Dashboard Abnormal Alert]], [[Remote Exception Notification]]
- **[[Battery Temperature Measurement Design]]**: [[Ambient Temperature Sensor]], [[BMS Internal Temperature Sensing]], [[Cell-Connector Temperature Sensing]], [[Electrolyte-Immersed Temperature Sensor]], [[External Thermistor Temperature Sensor]], [[Internal Temperature Sensor]]
  - **[[Internal Temperature Sensor]]**: [[Internal Thermistor Temperature Sensor]]
- **[[Charger Operator Interface Design]]**: [[Local Charger Status Indication]], [[Touchscreen Interface]]
  - **[[Local Charger Status Indication]]**: [[Charger Status LED Bar]], [[Remote Charger Status Stack Light]]
- **[[Charger Power Stage Design]]**: [[Dual-Cable and Parallel Charging Configuration]], [[Modular Power Modules]], [[Multi-Voltage Output]], [[Silicon-Carbide Power Stage]]
- **[[Current Sensing Design]]**: [[External Shunt Current Sensing]], [[Hall-Effect Current Sensing]], [[Shuntless Current Sensing]], [[Split-Core Current Sensor]]
- **[[Data Handling Design]]**: [[Cloud Portal Integration]], [[Non-Volatile Event Memory]]
- **[[Enclosure and Mounting Design]]**: [[Acid-Resistant Sealed Housing]], [[Breakaway Connector]], [[Ingress-Protected Drive Components]], [[Onboard Charger Mounting]], [[Outdoor-Rated Charger Enclosure]]
- **[[Fuel Cell Power Design]]**: [[Fuel Cell Hybrid Power Stage]], [[Hydrogen Storage Tank]], [[Onboard Fuel Level Gauge]]
- **[[Low Electrolyte Alert Design]]**: [[Communicated Watering Need Alert]], [[Local Low Electrolyte Alert]]
- **[[Lead-Acid Battery Construction Design]]**: [[Copper Inserted Posts]], [[Extended Watering Interval]], [[Flat Plate Construction]], [[Flexible Bolt-On Intercell Connector]], [[Forced Electrolyte Circulation]], [[Gel Electrolyte]], [[Heavy-Duty Intercell Connectors]], [[Individual Plate Formation]], [[Thin Plate Pure Lead Plates]], [[Tubular Plate Construction]]
- **[[Object and Proximity Sensing Design]]**: [[LiDAR Object Sensor]], [[Magnetic Field Detection Sensor]], [[Pedestrian Detection Camera]], [[Proximity Tag System]], [[Radar Object Sensor]], [[Stereoscopic Vision Sensor]], [[Ultrasonic Distance Sensor]]
- **[[Vehicle Control Device Design]]**: [[Active Stability Actuator]], [[Belt-Worn Remote Control]], [[Electric Mast Thrust Drive]], [[Emergency Cut-Off Switch]], [[Fork Laser Guide]], [[Mast Lift Limit Switch]], [[Programmable Motor Controller]], [[Seat Belt Interlock]]
  - **[[Operator Identification Design]]**: [[Fingerprint Reader]], [[RFID or PIN Access Reader]]
- **[[Vehicle Drive Design]]**: [[AC Drive Motor]], [[Electric Parking Brake]], [[Electric Power Steering]], [[Regenerative Braking]]
- **[[Vehicle Energy Interface Design]]**: [[Quick-Change Battery Compartment]], [[Truck Charging Port]]
- **[[Vehicle State Sensing Design]]**: [[Hydraulic Pressure Load Sensor]], [[Impact Sensor]]
  - **[[Operator Presence Sensing Design]]**: [[Light-Beam Compartment Sensor]], [[Operator Presence Pedal]], [[Operator Sensing Floor Mat]]
- **[[Warning and Display Device Design]]**: 
  - **[[Display Device Design]]**: [[Battery Status Gauge]], [[Integrated LCD Display]], [[Vehicle Operator Display Design]]
    - **[[Vehicle Operator Display Design]]**: [[Battery Discharge Indicator]], [[Operator Touch Display]], [[Vehicle-Mounted Display]]
  - **[[Indicator and Alarm Design]]**: [[Aircraft Proximity Indicator Light]], [[Audible Alarm]], [[Floor-Projected Warning Light]], [[Interactive Warning Vest]], [[Local LED Indicator]]
- **[[Wired Interface Design]]**: [[CAN Interface]], [[CAN-LIN and Battery Bus Interface]], [[DC-Cable Power-Line Communication]], [[Infrared Data Port]], [[RS-232 and RS-485 Serial Interface]], [[USB Data Download]]
- **[[Wireless Interface Design]]**: [[900 MHz Industrial Wireless Interface]], [[Bluetooth Interface]], [[Cellular Communication Interface]], [[Light-Triggered Data Upload]], [[LoRa Interface]], [[Mobile App Interface]], [[NFC Interface]], [[Wi-Fi Interface]], [[ZigBee 2.4 GHz Interface]]

**Derived function to design association (general level)**

| General function | Specific functions | Products (count) | Designs that appear on those products (count of products) |
|---|---|---|---|
| [[Charge Battery]] | 7 | 34 | [[Modular Power Modules]] (10), [[Multi-Voltage Output]] (7), [[Charger Status LED Bar]] (4), [[Touchscreen Interface]] (3), [[USB Data Download]] (3) |
| [[Communicate Battery and Vehicle Data]] | 9 | 41 | [[Local LED Indicator]] (10), [[Cloud Portal Integration]] (8), [[Acid-Resistant Sealed Housing]] (7), [[Cellular Communication Interface]] (6), [[Non-Volatile Event Memory]] (5) |
| [[Connect Battery Power Path]] | 2 | 5 | none yet |
| [[Control Charge Profile]] | 9 | 28 | [[Modular Power Modules]] (8), [[Multi-Voltage Output]] (7), [[Charger Status LED Bar]] (4), [[DC-Cable Power-Line Communication]] (2), [[Touchscreen Interface]] (2) |
| [[Hold or Stop Vehicle Automatically]] | 5 | 20 | [[Electric Parking Brake]] (3), [[Quick-Change Battery Compartment]] (2), [[Ultrasonic Distance Sensor]] (2), [[Programmable Motor Controller]] (1), [[Regenerative Braking]] (1) |
| [[Inform Operator of Truck Condition]] | 2 | 4 | [[Vehicle-Mounted Display]] (3), [[Audible Alarm]] (2), [[AC Drive Motor]] (2), [[Electric Parking Brake]] (1), [[Regenerative Braking]] (1) |
| [[Inform Users of Battery Condition]] | 6 | 32 | [[Local LED Indicator]] (15), [[Cloud Portal Integration]] (7), [[Audible Alarm]] (5), [[Acid-Resistant Sealed Housing]] (5), [[Bluetooth Low Energy Interface]] (4) |
| [[Keep Charging Available and Safe]] | 2 | 5 | [[Modular Power Modules]] (3), [[Dual-Cable and Parallel Charging Configuration]] (2), [[Touchscreen Interface]] (1), [[Charger Status LED Bar]] (1), [[Multi-Voltage Output]] (1) |
| [[Limit Vehicle Speed Automatically]] | 6 | 34 | [[Proximity Tag System]] (4), [[LiDAR Object Sensor]] (4), [[Programmable Motor Controller]] (2), [[Floor-Projected Warning Light]] (2), [[Ingress-Protected Drive Components]] (2) |
| [[Maintain Battery Electrolyte]] | 2 | 12 | [[Forced Electrolyte Circulation]] (5), [[Tubular Plate Construction]] (1) |
| [[Maintain Vehicle Stability and Load Awareness]] | 6 | 20 | [[Electric Parking Brake]] (2), [[Regenerative Braking]] (2), [[Audible Alarm]] (2), [[Vehicle-Mounted Display]] (2), [[Quick-Change Battery Compartment]] (2) |
| [[Manage Fleet Use]] | 4 | 34 | [[RFID or PIN Access Reader]] (6), [[Multi-Voltage Output]] (5), [[Impact Sensor]] (4), [[Modular Power Modules]] (3), [[Charger Status LED Bar]] (3) |
| [[Operate in Harsh Conditions]] | 3 | 14 | [[Ingress-Protected Drive Components]] (4), [[Integrated Battery Heater]] (3), [[Electric Parking Brake]] (2), [[RFID or PIN Access Reader]] (2), [[Regenerative Braking]] (1) |
| [[Protect Battery from Harm]] | 2 | 4 | [[CAN Interface]] (2), [[Audible Alarm]] (2), [[Integrated Battery Management System]] (1), [[Hall-Effect Current Sensing]] (1), [[Bluetooth Low Energy Interface]] (1) |
| [[Reduce Operator Effort]] | 4 | 6 | [[Electric Power Steering]] (2), [[AC Drive Motor]] (1), [[Operator Presence Pedal]] (1), [[Belt-Worn Remote Control]] (1) |
| [[Sense Battery State]] | 12 | 40 | [[Local LED Indicator]] (13), [[Acid-Resistant Sealed Housing]] (8), [[Cloud Portal Integration]] (7), [[Non-Volatile Event Memory]] (5), [[DC-Cable Power-Line Communication]] (5) |
| [[Sense Collision Risk and Events]] | 2 | 37 | [[Impact Sensor]] (5), [[Proximity Tag System]] (5), [[Stereoscopic Vision Sensor]] (4), [[LiDAR Object Sensor]] (4), [[Radar Object Sensor]] (3) |
| [[Supply Vehicle Energy Without Charging]] | 5 | 10 | [[Quick-Change Battery Compartment]] (4), [[Electric Parking Brake]] (2), [[Regenerative Braking]] (2), [[Audible Alarm]] (2), [[Vehicle-Mounted Display]] (2) |
| [[Support Operator View and Positioning]] | 2 | 12 | [[Fork Laser Guide]] (3), [[Vehicle-Mounted Display]] (1), [[Impact Sensor]] (1), [[Radar Object Sensor]] (1), [[Regenerative Braking]] (1) |
| [[Warn People of Hazards]] | 3 | 38 | [[Floor-Projected Warning Light]] (8), [[Proximity Tag System]] (4), [[Audible Alarm]] (3), [[Vehicle-Mounted Display]] (3), [[Stereoscopic Vision Sensor]] (3) |

- **Function navigation status (Step 51, 2026-10-05):** all 129 Function notes are represented by the six goal-level roots and their 20 general-function families. This tree is the preferred behavioral navigation grouping; folder placement remains navigation only and does not replace modeled `hasChild` / `childOf` / `supertypeOf` / `subtypeOf` relationships.

- **Not yet assigned a general parent:** functions none; designs [[Reverse-Polarity Protection]].

## Aliases

- Levels of function and design

## Former ids
