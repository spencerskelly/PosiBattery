---
type: Info
subtype:
id: INFO-00253
uid: 20261003195011094skellyspencer
status: Draft
tags:
  - review
  - features
  - truck-parts
describes:
  - "[[Battery-Connected Product]]"
---

# Truck Part Connection Register

## Definition

Which of 12 generic truck parts each truck-side and battery accessory mounts on, connects to, or acts on, with stated mappings kept apart from typical ones.

## Notes

- **Owner request (2026-10-03):** map the accessories to the parts of the truck they are connected to; 'connected' means all three of where it mounts, what it electrically or data-connects to, and what part it controls or acts on, recorded separately; stated first, then typical, kept visibly separate; about 12 subsystems. Parts: [[Industrial Truck Anatomy]].
- **Scope:** 159 truck-side and battery accessory, device and software notes (GSE devices are excluded).
- **Stated** (the source names the part): 14 rows on 13 accessories. **Typical** (inferred from the device class and, for 'acts on', from the functions it performs; not from any source): 150 accessories carry at least one typical row. 9 accessories are left unmapped.
- **Reading rule:** a typical row says where this kind of device usually goes or what it usually acts on. It is analyst inference and must not be read as a fact about that product. Rows marked alternative mean the mounting point varies by model and is not stated.
- **Not written as links:** the symmetric `interfaces` field would carry stated pairs but has no place for connection type or basis, and the `interfaces` field order is not wired into the build; the pairs stay here and as a line on each accessory note until the owner confirms the field.
- **Battery-side devices:** monitors, watering and connector devices sit on the battery, which sits in the truck's battery compartment; they are mapped to Truck Battery Compartment as typical unless a source names the compartment.

**Function-level 'acts on' map (typical)**

| Function | Parts it acts on (typical, function-level) |
|---|---|
| [[Limit Truck Speed Automatically]] | [[Truck Drive and Brakes]] |
| [[Slow Truck in Curves]] | [[Truck Drive and Brakes]] |
| [[Adapt Speed to Load and Lift Height]] | [[Truck Drive and Brakes]], [[Truck Hydraulics]] |
| [[Reduce Speed When Seat Belt Is Unfastened]] | [[Truck Drive and Brakes]] |
| [[Program Travel, Lift and Tilt Speeds]] | [[Truck Drive and Brakes]], [[Truck Hydraulics]] |
| [[Limit Vehicle Motion by Location Zone]] | [[Truck Drive and Brakes]] |
| [[Stop Vehicle When Operator Is Out of Position]] | [[Truck Drive and Brakes]] |
| [[Hold Truck on Slope]] | [[Truck Drive and Brakes]] |
| [[Reduce Wheel Slip]] | [[Truck Drive and Brakes]], [[Truck Wheels]] |
| [[Cut Power in an Emergency]] | [[Truck Controller and CAN Bus]] |
| [[Restrict Lift When Load Exceeds Limit]] | [[Truck Hydraulics]] |
| [[Cut Lift at Programmed Height]] | [[Truck Hydraulics]], [[Truck Mast]] |
| [[Damp Mast Oscillation]] | [[Truck Mast]] |
| [[Stabilize Truck Dynamically]] | [[Truck Hydraulics]], [[Truck Drive and Brakes]] |
| [[Assist Lift Positioning]] | [[Truck Forks]], [[Truck Mast]] |
| [[Sense Load Weight and Lift Height]] | [[Truck Forks]], [[Truck Mast]] |
| [[Control Operator Access]] | [[Truck Controller and CAN Bus]] |
| [[Enforce Pre-Shift Checklist]] | [[Truck Controller and CAN Bus]], [[Truck Controls and Display]] |
| [[Detect and Record Impacts]] | [[Truck Controller and CAN Bus]] |
| [[Report Truck Telemetry]] | [[Truck Controller and CAN Bus]] |
| [[Show Camera View to Operator]] | [[Truck Controls and Display]] |
| [[Alert Operator of Hazards]] | [[Truck Controls and Display]] |
| [[Alert on Abnormal Condition]] | [[Truck Controls and Display]] |
| [[Display Battery Status to Operator]] | [[Truck Controls and Display]] |
| [[Display Truck Status to Operator]] | [[Truck Controls and Display]] |
| [[Warn Pedestrians of Approaching Truck]] | [[Truck Lighting]] |
| [[Rotate Operator Workstation]] | [[Truck Operator Compartment]] |
| [[Steer with Electric Power Assist]] | [[Truck Drive and Brakes]] |

**Accessories by part**

**[[Truck Mast]]**

- *mounts on, stated:* [[Toyota Carriage-Mounted Camera]] (a camera mounted on the carriage)
- *mounts on, typical:* [[Crown Capacity Data Monitor]], [[Doosan Bobcat Mast Sway Control]], [[Heli Operator Presence Sensing System]], [[Hyster Dynamic Stability System]], [[Jungheinrich curveCONTROL]], [[Komatsu Digital Load Scale]], [[Komatsu Operator Presence Sensing System]], [[Linde Dynamic Mast Control]], [[Linde Load Management Advanced]], [[Linde Safety Pilot]], [[Linde System Control]], [[Mitsubishi Integrated Presence System]], [[Raymond Fork Tilt Leveling]], [[Raymond Fork-Tip Laser Guide]], [[Raymond Load Weight Display]], [[Raymond Mast Lift Limit Switch with Bypass]], [[Raymond Travel Speed Control]], [[Raymond iWAREHOUSE Integrated Tether System]], [[STILL Curve Speed Control]], [[STILL Safety Assist]], [[STILL Safety Packages]], [[Toyota Acu-Laser]], [[Toyota Assist]], [[Toyota Auto Height Select]], [[Toyota Compartment Sensing System]], [[Toyota Load Weight Sensing]], [[Toyota System of Active Stability]], [[UniCarriers Curve Control]], [[Yale Reliant Portfolio]]
- *acts on, stated:* [[Doosan Bobcat Mast Sway Control]] (stabilizes the mast at height); [[Linde Dynamic Mast Control]] (reduces mast swing and deflection)
- *acts on, typical:* [[Crown Capacity Data Monitor]], [[Komatsu Digital Load Scale]], [[Linde Load Management Advanced]], [[Linde Safety Pilot]], [[Raymond Fork-Tip Laser Guide]], [[Raymond Mast Lift Limit Switch with Bypass]], [[Raymond Vantage Point System]], [[Toyota Acu-Laser]], [[Toyota Assist]], [[Toyota Auto Height Select]], [[Toyota Carriage-Mounted Camera]], [[Toyota Load Weight Sensing]]

**[[Truck Forks]]**

- *mounts on, stated:* [[Raymond Vantage Point System]] (camera mounted under the truck's forks)
- *mounts on, typical:* [[Hangcha Backup Camera Option]], [[Jungheinrich addedVIEW Camera Systems]], [[Panacea Cam-DVR with Impact Sensors]], [[Toyota 360 Operating Camera]], [[Toyota Twistlock Snapshot Camera System]]
- *acts on, stated:* [[Raymond Fork Tilt Leveling]] (positions the forks perpendicular to the mast); [[Raymond Load Weight Display]] (measures the load weight on the forks)
- *acts on, typical:* [[Crown Capacity Data Monitor]], [[Komatsu Digital Load Scale]], [[Linde Load Management Advanced]], [[Linde Safety Pilot]], [[Raymond Fork-Tip Laser Guide]], [[Raymond Vantage Point System]], [[Toyota Acu-Laser]], [[Toyota Assist]], [[Toyota Auto Height Select]], [[Toyota Carriage-Mounted Camera]], [[Toyota Load Weight Sensing]]

**[[Truck Overhead Guard]]**

- *mounts on, stated:* [[Toyota Forklift Lighting Options]] (blue spotlights mount on the overhead guard)
- *mounts on, typical:* [[Blaxtair Pedestrian Detection System]] (alt.), [[Cat Safety Lighting Options]] (alt.), [[Crown ProximityAssist System]] (alt.), [[Doosan Bobcat Pedestrian Detection Camera]] (alt.), [[Hyster Pedestrian Awareness Camera]] (alt.), [[Hyster Reaction]] (alt.), [[IRIS 860 Sensor Pack]] (alt.), [[Larson Explosion-Proof Blue LED Forklift Light]] (alt.), [[Linde BlueSpot]] (alt.), [[Linde Safety Guard]] (alt.), [[Linde Safety Guard Portable Unit]] (alt.), [[Linde Safety Guard Static Unit]] (alt.), [[Panacea Blue Warning Light]] (alt.), [[Powerfleet Forklift Safety Lights]] (alt.), [[Raymond In-Aisle Detection System]] (alt.), [[Raymond iWAREHOUSE Fieldsense]] (alt.), [[Raymond iWAREHOUSE ObjectSense]] (alt.), [[STILL SafetyLight 4Plus]] (alt.), [[STILL Warning Zone Light]] (alt.), [[TVH Forklift Arrow Lights]] (alt.), [[Toyota SEnS Pedestrian Detection]] (alt.), [[UniCarriers Lighting Packages]] (alt.)

**[[Truck Operator Compartment]]**

- *mounts on, stated:* [[Linde Rotating Operator Workstation]] (a rotating driver's workstation or cabin)
- *mounts on, typical:* [[Cat Presence Detection System]], [[Jungheinrich easyPILOT]], [[Linde Smartphone Holder]], [[Raymond Operator Compartment Sensor System]], [[STILL EasyBelt]], [[UniCarriers In-Cab Accessories]]

**[[Truck Controls and Display]]**

- *mounts on, stated:* [[EnerSys Truck iQ]] (a truck-mounted touchscreen)
- *mounts on, typical:* [[Crown Gena Operating System]], [[Crown InfoLink 7-inch Touch Display]], [[Linde MT18 Multifunction Display]], [[Panacea Smart Start]], [[Toyota PIN Code Access Pad]]
- *connects to, stated:* [[Jungheinrich addedVIEW Camera Systems]] (cameras with a central assistance display); [[Raymond Load Weight Display]] (load weight is communicated via the truck display)
- *connects to, typical:* [[Hangcha Backup Camera Option]], [[Panacea Cam-DVR with Impact Sensors]], [[Raymond Vantage Point System]], [[Toyota 360 Operating Camera]], [[Toyota Carriage-Mounted Camera]], [[Toyota Twistlock Snapshot Camera System]]
- *acts on, typical:* [[Blaxtair Pedestrian Detection System]], [[Crown InfoLink]], [[Crown InfoLink 7-inch Touch Display]], [[Crown ProximityAssist System]], [[Doosan Bobcat Pedestrian Detection Camera]], [[EnerSys Truck iQ]], [[Hangcha Backup Camera Option]], [[Hyster Dynamic Stability System]], [[Hyster Pedestrian Awareness Camera]], [[Hyster Reaction]], [[Hyster Tracker Telemetry]], [[Jungheinrich ISM Online]], [[Jungheinrich Reverse Area Warning System]], [[Jungheinrich addedVIEW Camera Systems]], [[Jungheinrich zoneCONTROL]], [[Linde MT18 Multifunction Display]], [[Linde Safety Guard Truck Unit]], [[Logisnext Lift Link]], [[Mitsubishi Integrated Presence System]], [[Panacea Cam-DVR with Impact Sensors]], [[Powerfleet Forklift Gateway]], [[Raymond Vantage Point System]], [[Raymond iWAREHOUSE Fieldsense]], [[Raymond iWAREHOUSE ObjectSense]], [[Toyota 360 Operating Camera]], [[Toyota Assist]], [[Toyota Carriage-Mounted Camera]], [[Toyota SEnS Pedestrian Detection]], [[Toyota SEnS+ Pedestrian and Object Detection]]

**[[Truck Battery Compartment]]**

- *mounts on, stated:* [[PosiCharge E-Meter]] (goes in the battery compartment)
- *mounts on, typical:* [[AMETEK Prestolite Power BID]], [[AMETEK Prestolite Power BID with Ah Accumulator]], [[AMETEK Prestolite Power Site Probe]], [[AMETEK Prestolite Power TruBid]], [[AMETEK Prestolite Power WBID]], [[AMETEK Prestolite Power WBID Pro]], [[Access Control Group CellTrac]], [[Access Control Group CellVue]], [[Anderson SB Connector Series]], [[Crown Battery Acid Indicators]], [[Crown Battery Cables and Connectors]], [[Crown Battery Health Monitor]], [[Crown V-Force BMID]], [[Crown V-Force Single Point Watering System]], [[EnerSys iQ Mini]], [[Energywith withBMS BMU]], [[Exide AIR Electrolyte Agitation System]], [[Exide Automatic Watering System and Level Sensor]], [[Exide Motion+ EasyMonitor]], [[Flow-Rite Eagle Eye Elite IV]], [[Flow-Rite Eagle Eye Essential IV]], [[Flow-Rite Maverick Battery Watering System]], [[Fronius TagID]], [[HOPPECKE trak air Electrolyte Circulation]], [[HOPPECKE trak collect]], [[Hyster Battery Tracker]], [[Hyster Power Cellect]], [[Inventus Smart Battery Monitor SBM-01]], [[Midac Aquamatic Watering System]], [[Midac EUW Electrolyte Circulation System]], [[Midac End Leads]], [[Philadelphia Scientific SmartBlinky Pro]], [[Philadelphia Scientific Stealth Watering System]], [[Philadelphia Scientific Water Injector System]], [[Philadelphia Scientific eGO!Mini]], [[Philadelphia Scientific eGO!c]], [[Philadelphia Scientific eGO!core]], [[Philadelphia Scientific eGO!gateway]], [[Philadelphia Scientific eGO!plus]], [[Philadelphia Scientific eGO!pro]], [[PosiCharge BMID 1]], [[PosiCharge BMID 3]], [[PosiCharge Battery Rx]], [[PosiCharge DIY Fast Charge Kit]], [[PosiCharge Single-Point Automatic Battery Watering]], [[Power Designers PowerTrac 3]], [[Power Designers PowerTrac DT3]], [[Power Designers PowerTrac Monitor]], [[Raymond iBattery]], [[Yale Battery Vision]]
- *connects to, typical:* [[Anderson SB Connector Series]], [[Crown Battery Cables and Connectors]], [[Hyster Power Cellect]], [[Midac End Leads]], [[PosiCharge DIY Fast Charge Kit]]

**[[Truck Controller and CAN Bus]]**

- *mounts on, typical:* [[Crown InfoLink]], [[Doosan Lin-Q]], [[Hangcha FIMS]], [[Heli Fleet Management System]], [[Hyster Tracker Telemetry]], [[Jungheinrich ISM Online]], [[Komatsu KOMTRAX]], [[Linde connect]], [[Logisnext Lift Link]], [[Powerfleet Forklift Gateway]], [[Raymond iWAREHOUSE]], [[Raymond iWAREHOUSE Real-Time Location System]], [[STILL FleetManager]], [[STILL Smart Portal]], [[STILL neXXt fleet]], [[Toyota MyInsights Telematics]], [[Yale Vision Telemetry]]
- *connects to, stated:* [[HOPPECKE trak collect]] (links to the vehicle over LIN and battery bus)
- *connects to, typical:* [[AMETEK Prestolite Power BID]], [[AMETEK Prestolite Power WBID Pro]], [[Access Control Group CellTrac]], [[Blaxtair Pedestrian Detection System]], [[Cat Presence Detection System]], [[Crown Capacity Data Monitor]], [[Crown Gena Operating System]], [[Crown InfoLink]], [[Crown InfoLink 7-inch Touch Display]], [[Crown ProximityAssist System]], [[Doosan Bobcat Mast Sway Control]], [[Doosan Bobcat Pedestrian Detection Camera]], [[Doosan Lin-Q]], [[EnerSys Truck iQ]], [[EnerSys iQ Mini]], [[Exide Motion+ EasyMonitor]], [[Flow-Rite Eagle Eye Essential IV]], [[Hangcha FIMS]], [[Heli Fleet Management System]], [[Heli Operator Presence Sensing System]], [[Hyster Dynamic Stability System]], [[Hyster Pedestrian Awareness Camera]], [[Hyster Tracker Telemetry]], [[IRIS 860 Sensor Pack]], [[Inventus Smart Battery Monitor SBM-01]], [[Jungheinrich ISM Online]], [[Jungheinrich Pedestrian Detection System]], [[Jungheinrich Reverse Area Warning System]], [[Jungheinrich curveCONTROL]], [[Komatsu Digital Load Scale]], [[Komatsu KOMTRAX]], [[Komatsu Operator Presence Sensing System]], [[Linde Dynamic Mast Control]], [[Linde Load Management Advanced]], [[Linde MT18 Multifunction Display]], [[Linde Motion Detection]], [[Linde Safety Pilot]], [[Linde System Control]], [[Linde connect]], [[Logisnext Lift Link]], [[Mitsubishi Integrated Presence System]], [[Panacea Smart Start]], [[PosiCharge BMID 3]], [[PosiCharge Battery Rx]], [[Power Designers PowerTrac 3]], [[Power Designers PowerTrac Monitor]], [[Powerfleet Forklift Gateway]], [[Raymond Fork Tilt Leveling]], [[Raymond Fork-Tip Laser Guide]], [[Raymond In-Aisle Detection System]], [[Raymond Mast Lift Limit Switch with Bypass]], [[Raymond Operator Compartment Sensor System]], [[Raymond Travel Speed Control]], [[Raymond Zoning and Positioning]], [[Raymond iBattery]], [[Raymond iWAREHOUSE]], [[Raymond iWAREHOUSE Fieldsense]], [[Raymond iWAREHOUSE Integrated Tether System]], [[Raymond iWAREHOUSE Real-Time Location System]], [[STILL Curve Speed Control]], [[STILL FleetManager]], [[STILL Safety Assist]], [[STILL Safety Packages]], [[STILL Smart Portal]], [[STILL neXXt fleet]], [[Toyota Acu-Laser]], [[Toyota Assist]], [[Toyota Auto Height Select]], [[Toyota Compartment Sensing System]], [[Toyota Load Weight Sensing]], [[Toyota MyInsights Telematics]], [[Toyota PIN Code Access Pad]], [[Toyota SEnS Pedestrian Detection]], [[Toyota SEnS+ Pedestrian and Object Detection]], [[Toyota System of Active Stability]], [[UniCarriers Curve Control]], [[Yale Reliant Portfolio]], [[Yale Vision Telemetry]]
- *acts on, typical:* [[Crown InfoLink]], [[Doosan Lin-Q]], [[Hangcha FIMS]], [[Heli Fleet Management System]], [[Hyster Tracker Telemetry]], [[Jungheinrich ISM Online]], [[Komatsu KOMTRAX]], [[Linde connect]], [[Logisnext Lift Link]], [[Panacea Cam-DVR with Impact Sensors]], [[Panacea Smart Start]], [[Powerfleet Forklift Gateway]], [[Raymond iWAREHOUSE]], [[STILL FleetManager]], [[STILL Safety Assist]], [[STILL Smart Portal]], [[STILL neXXt fleet]], [[Toyota MyInsights Telematics]], [[Toyota PIN Code Access Pad]], [[Yale Vision Telemetry]]

**[[Truck Hydraulics]]**

- *acts on, typical:* [[Hyster Dynamic Stability System]], [[Hyster Reaction]], [[Jungheinrich curveCONTROL]], [[Linde Load Management Advanced]], [[Linde Safety Pilot]], [[Linde System Control]], [[Raymond Mast Lift Limit Switch with Bypass]], [[Toyota Assist]], [[Toyota System of Active Stability]], [[Yale Reliant Portfolio]]

**[[Truck Drive and Brakes]]**

- *acts on, typical:* [[Cat Presence Detection System]], [[Crown ProximityAssist System]], [[Heli Operator Presence Sensing System]], [[Hyster Dynamic Stability System]], [[Hyster Reaction]], [[Jungheinrich Pedestrian Detection System]], [[Jungheinrich curveCONTROL]], [[Jungheinrich zoneCONTROL]], [[Komatsu Operator Presence Sensing System]], [[Linde Load Management Advanced]], [[Linde Safety Guard]], [[Linde Safety Guard Zone Marker]], [[Linde Safety Pilot]], [[Linde System Control]], [[Powerfleet Pedestrian Proximity Detection]], [[Raymond In-Aisle Detection System]], [[Raymond Operator Compartment Sensor System]], [[Raymond Travel Speed Control]], [[Raymond Zoning and Positioning]], [[Raymond iWAREHOUSE Integrated Tether System]], [[Raymond iWAREHOUSE ObjectSense]], [[Raymond iWAREHOUSE Real-Time Location System]], [[STILL Curve Speed Control]], [[STILL Safety Assist]], [[STILL Safety Packages]], [[Toyota Assist]], [[Toyota Compartment Sensing System]], [[Toyota SEnS+ Pedestrian and Object Detection]], [[Toyota System of Active Stability]], [[UniCarriers Curve Control]], [[Yale Reliant Portfolio]]

**[[Truck Rear Body]]**

- *mounts on, stated:* [[Toyota Object Detection Radar]] (radar sensor mounted to the back of the counterweight)
- *mounts on, typical:* [[Blaxtair Pedestrian Detection System]] (alt.), [[Cat Safety Lighting Options]] (alt.), [[Crown ProximityAssist System]] (alt.), [[Doosan Bobcat Pedestrian Detection Camera]] (alt.), [[Hyster Pedestrian Awareness Camera]] (alt.), [[Hyster Reaction]] (alt.), [[IRIS 860 Sensor Pack]] (alt.), [[Jungheinrich Pedestrian Detection System]], [[Jungheinrich Reverse Area Warning System]], [[Larson Explosion-Proof Blue LED Forklift Light]] (alt.), [[Linde BlueSpot]] (alt.), [[Linde Safety Guard]] (alt.), [[Linde Safety Guard Portable Unit]] (alt.), [[Linde Safety Guard Static Unit]] (alt.), [[Panacea Blue Warning Light]] (alt.), [[Powerfleet Forklift Safety Lights]] (alt.), [[Raymond In-Aisle Detection System]] (alt.), [[Raymond iWAREHOUSE Fieldsense]] (alt.), [[Raymond iWAREHOUSE ObjectSense]] (alt.), [[STILL SafetyLight 4Plus]] (alt.), [[STILL Warning Zone Light]] (alt.), [[TVH Forklift Arrow Lights]] (alt.), [[Toyota SEnS Pedestrian Detection]] (alt.), [[Toyota SEnS+ Pedestrian and Object Detection]], [[UniCarriers Lighting Packages]] (alt.)

**[[Truck Wheels]]**

- no accessory mapped

**[[Truck Lighting]]**

- *connects to, typical:* [[Cat Safety Lighting Options]], [[Larson Explosion-Proof Blue LED Forklift Light]], [[Linde BlueSpot]], [[Linde Safety Guard Portable Unit]], [[Linde Safety Guard Static Unit]], [[Panacea Blue Warning Light]], [[Powerfleet Forklift Safety Lights]], [[STILL SafetyLight 4Plus]], [[STILL Warning Zone Light]], [[TVH Forklift Arrow Lights]], [[Toyota Forklift Lighting Options]], [[UniCarriers Lighting Packages]]
- *acts on, typical:* [[Cat Safety Lighting Options]], [[Larson Explosion-Proof Blue LED Forklift Light]], [[Linde BlueSpot]], [[Linde Safety Guard]], [[Linde Safety Guard Portable Unit]], [[Linde Safety Guard Static Unit]], [[Panacea Blue Warning Light]], [[Powerfleet Forklift Safety Lights]], [[STILL Safety Assist]], [[STILL Safety Packages]], [[STILL SafetyLight 4Plus]], [[STILL Warning Zone Light]], [[TVH Forklift Arrow Lights]], [[Toyota Forklift Lighting Options]]

**Unmapped accessories**

| Accessory | Reason |
|---|---|
| [[ACT ACTview]] | back-office software; not mounted or connected to a truck part |
| [[Fronius Charge & Connect]] | back-office software; not mounted or connected to a truck part |
| [[Philadelphia Scientific iBOS]] | back-office software; not mounted or connected to a truck part |
| [[PosiCharge PosiConnect]] | back-office software; not mounted or connected to a truck part |
| [[PosiCharge PosiLink]] | back-office software; not mounted or connected to a truck part |
| [[PosiCharge SkyLink]] | back-office software; not mounted or connected to a truck part |
| [[Stryten inCOMMAND]] | back-office software; not mounted or connected to a truck part |
| [[Toyota Cold Conditioning Package]] | whole-truck conditioning package; no single part |
| [[UniCarriers Freezer Option]] | whole-truck conditioning package; no single part |
- **Round 32:** GSE accessories, and the battery-side devices that fit both trucks and GSE, are mapped in [[GSE Part Connection Register]]; those devices were left out of this register because they carry the GSE tag.

## Aliases

- Truck part mapping

## Former ids
