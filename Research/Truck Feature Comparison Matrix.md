---
type: Info
subtype:
id: INFO-00251
uid: 20261003174625798skellyspencer
status: Draft
tags:
  - comparison
  - features
  - truck
describes:
  - "[[Battery-Connected Product]]"
---

# Truck Feature Comparison Matrix

## Definition

Feature-first comparison of electric trucks by maker group: which specific functions each group is documented to offer, built in or through its own or third-party accessories.

## Notes

- **Owner request (2026-10-03):** feature-first comparison for trucks. Generated from the vault; related earlier note: [[Truck Device Comparison Matrix]] (truck-side devices by metric).
- **Unit of comparison:** the maker group (a maker rolled up through subsidiaryOf, for example Raymond and Toyota Material Handling under Toyota Industries; Linde and STILL under KION; the Americas and Europe entities under Mitsubishi Logisnext). Truck notes are families, not single models.
- **Scope:** 36 electric truck notes and 106 truck accessory and software notes; 43 specific functions have evidence for at least one maker group and are shown (5 more are performed only by accessory notes that no truck group makes or is linked to: Detect Voltage Imbalance, Estimate State of Charge, Indicate Aircraft Proximity to Operator, Report Fuel Cell State to Truck, Slow and Stop Near Aircraft). ICE trucks and attachments are out of scope (decisions Q13, Q14).
- **Cell code:** B = a truck note of the group links the function (built in or listed as an option on the truck); A = an accessory or software note made by the group links it; 3P = third-party accessories tied to the group by offeredWith, distribution or integration; the digit is the number of notes; a dot means no evidence found.
- **Reading rule (important):** a dot means the vault holds no source for it, not that the truck lacks it. Columns differ in documentation depth (truck notes and T1 share below), so compare features across a row, and compare groups only after reading the counts. Mitsubishi Logisnext, Heli, Hangcha, Doosan and Komatsu rest mostly on dealer data (T3).
- **Not in the matrix:** properties that are metrics (chemistry, voltage, capacity, warranty, charge regimes, watering interval, ingress rating, operating temperature); see the metric notes, for example [[Metric - Watering Interval]], [[Metric - Ingress and Enclosure Protection]] and [[Metric - Operating Temperature Range]].

**Group coverage**

| Group | Rank (2025 list) | Truck notes | Truck accessory and software notes | Features with B or A | Notes with T1 evidence |
|---|---|---|---|---|---|
| [[Toyota Industries Corporation]] | 1 | 6 | 29 | 20 of 43 | 28 |
| [[KION Group]] | 2 | 6 | 24 | 21 of 43 | 19 |
| [[Jungheinrich]] | 3 | 1 | 7 | 10 of 43 | 6 |
| [[Crown Equipment]] | 4 | 5 | 4 | 19 of 43 | 8 |
| [[Mitsubishi Logisnext]] | 5 | 8 | 8 | 12 of 43 | 11 |
| [[Hyster-Yale]] | 6 | 3 | 6 | 14 of 43 | 7 |
| [[Anhui Heli]] | 7 | 2 | 3 | 7 of 43 | 0 |
| [[Hangcha Group]] | 8 | 2 | 2 | 11 of 43 | 4 |
| [[Doosan Bobcat]] | other lists | 2 | 3 | 11 of 43 | 0 |
| [[Komatsu]] | other lists | 1 | 3 | 6 of 43 | 3 |

**Matrix**

| General function | Feature (specific function) | Toyota | KION | Jung. | Crown | Mitsu. | H-Y | Heli | Hangcha | Doosan | Komatsu | Groups with B or A |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [[Charge Battery]] | [[Charge Battery from Standard Power Outlet]] | · | · | · | · | · | B1 | B1 A1 | · | · | · | 2 |
| [[Communicate Battery and Vehicle Data]] | [[Communicate Battery State over CAN]] | · | · | · | · | · | A1 | · | · | · | · | 1 |
| [[Hold or Stop Vehicle Automatically]] | [[Cut Power in an Emergency]] | · | · | · | · | · | · | · | B1 | · | · | 1 |
| [[Hold or Stop Vehicle Automatically]] | [[Hold Truck on Slope]] | · | · | · | B2 | · | · | · | · | B2 | · | 2 |
| [[Hold or Stop Vehicle Automatically]] | [[Reduce Wheel Slip]] | · | · | · | B1 | · | · | · | · | · | · | 1 |
| [[Hold or Stop Vehicle Automatically]] | [[Stop Vehicle When Operator Is Out of Position]] | B1 A3 | · | · | · | B2 A1 | · | A1 | B1 | B1 | A1 | 6 |
| [[Inform Operator of Truck Condition]] | [[Display Truck Status to Operator]] | · | · | · | B1 | · | · | · | B1 | · | · | 2 |
| [[Inform Operator of Truck Condition]] | [[Indicate Maintenance Due]] | B1 | · | · | · | · | · | · | · | · | · | 1 |
| [[Inform Users of Battery Condition]] | [[Alert on Abnormal Condition]] | · | · | · | · | · | B1 | · | · | · | · | 1 |
| [[Inform Users of Battery Condition]] | [[Display Battery Status to Operator]] | · | A1 | · | · | · | B1 | · | · | · | · | 2 |
| [[Limit Vehicle Speed Automatically]] | [[Adapt Speed to Load and Lift Height]] | · | A2 | · | B1 | · | · | · | · | · | · | 2 |
| [[Limit Vehicle Speed Automatically]] | [[Limit Truck Speed Automatically]] | A4 | A2 | A1 | B3 A1 | B1 | A1 | · | · | A1 | B1 | 8 |
| [[Limit Vehicle Speed Automatically]] | [[Limit Vehicle Motion by Location Zone]] | A2 | A3 | A1 | · | · | A2 | · | · | · | · | 4 |
| [[Limit Vehicle Speed Automatically]] | [[Program Travel, Lift and Tilt Speeds]] | · | B1 | · | B2 | · | · | B1 | · | · | B1 | 4 |
| [[Limit Vehicle Speed Automatically]] | [[Reduce Speed When Seat Belt Is Unfastened]] | · | A1 | · | · | · | · | · | · | · | · | 1 |
| [[Limit Vehicle Speed Automatically]] | [[Slow Truck in Curves]] | · | A3 | A1 | B3 | A1 | A3 | B1 | B1 | · | · | 7 |
| [[Maintain Vehicle Stability and Load Awareness]] | [[Cushion Fork Lowering]] | · | · | · | · | · | · | · | B2 | · | · | 1 |
| [[Maintain Vehicle Stability and Load Awareness]] | [[Cut Lift at Programmed Height]] | A1 | · | · | · | · | · | · | · | · | · | 1 |
| [[Maintain Vehicle Stability and Load Awareness]] | [[Damp Mast Oscillation]] | · | A1 | · | · | · | · | · | · | A1 | · | 2 |
| [[Maintain Vehicle Stability and Load Awareness]] | [[Restrict Lift When Load Exceeds Limit]] | · | A2 | · | · | · | A1 | · | · | · | · | 2 |
| [[Maintain Vehicle Stability and Load Awareness]] | [[Sense Load Weight and Lift Height]] | A3 | A2 | · | A1 | · | · | · | · | · | A1 | 4 |
| [[Maintain Vehicle Stability and Load Awareness]] | [[Stabilize Truck Dynamically]] | A2 | A1 | A1 | B2 | · | A2 | · | · | B1 | · | 6 |
| [[Manage Fleet Use]] | [[Control Operator Access]] | B1 A1 | B2 A4 | · | B1 | A1 3P1 | · | · | B1 | · | · | 5 |
| [[Manage Fleet Use]] | [[Enforce Pre-Shift Checklist]] | · | B1 | A1 | · | A1 3P1 | · | · | · | · | · | 3 |
| [[Manage Fleet Use]] | [[Report Truck Telemetry]] | A1 | A4 | A1 | · | A1 3P1 | · | A1 | A1 | A1 | A1 | 8 |
| [[Operate in Harsh Conditions]] | [[Operate in Cold Storage]] | A1 | · | · | B1 | A1 | · | B1 | B1 | B1 | · | 6 |
| [[Operate in Harsh Conditions]] | [[Operate in Wet or Dusty Conditions]] | B1 | B1 | · | B1 | · | · | B1 | · | B1 | B1 | 6 |
| [[Operate in Harsh Conditions]] | [[Shelter Operator from Weather]] | B1 | · | · | · | B1 | · | · | · | · | · | 2 |
| [[Protect Battery from Harm]] | [[Protect Battery from Deep Discharge]] | · | · | · | B1 | · | A1 | · | · | · | · | 2 |
| [[Reduce Operator Effort]] | [[Follow Operator Automatically]] | · | · | A1 | · | · | · | · | · | · | · | 1 |
| [[Reduce Operator Effort]] | [[Rotate Operator Workstation]] | · | A1 | · | · | · | · | · | · | · | · | 1 |
| [[Reduce Operator Effort]] | [[Steer with Electric Power Assist]] | · | · | · | · | B2 | · | · | · | · | · | 1 |
| [[Sense Battery State]] | [[Estimate Remaining Run Time]] | · | B1 | · | · | · | · | · | · | · | · | 1 |
| [[Sense Collision Risk and Events]] | [[Detect Pedestrians and Objects Near Truck]] | A7 | A3 | A3 3P1 | A1 | · | A3 | · | · | A1 | · | 6 |
| [[Sense Collision Risk and Events]] | [[Detect and Record Impacts]] | A1 | A2 | · | · | A1 3P1 | · | · | · | · | · | 3 |
| [[Supply Vehicle Energy Without Charging]] | [[Change Battery Quickly]] | B1 | · | · | · | · | · | · | B2 | B1 | · | 3 |
| [[Supply Vehicle Energy Without Charging]] | [[Deliver Constant Power Through Shift]] | · | · | · | · | · | B2 A1 | · | · | · | · | 1 |
| [[Supply Vehicle Energy Without Charging]] | [[Recover Energy by Regeneration]] | B1 | · | · | B1 | · | · | · | · | · | · | 2 |
| [[Supply Vehicle Energy Without Charging]] | [[Refuel Truck Power Source in Minutes]] | · | · | · | · | · | A1 | · | · | · | · | 1 |
| [[Support Operator View and Positioning]] | [[Assist Lift Positioning]] | A7 | · | · | B1 | · | · | · | · | · | · | 2 |
| [[Support Operator View and Positioning]] | [[Show Camera View to Operator]] | A4 | · | A1 | B1 | · | · | · | A1 | · | · | 4 |
| [[Warn People of Hazards]] | [[Alert Operator of Hazards]] | A4 | A1 | A2 3P1 | A2 | A1 | A3 | · | · | A1 | · | 7 |
| [[Warn People of Hazards]] | [[Warn Pedestrians of Approaching Truck]] | A1 | A8 | · | B1 | A1 | · | · | B1 | · | · | 5 |

**What the matrix shows (generated)**

- **Offered by six or more groups (common):** [[Limit Truck Speed Automatically]] (8); [[Report Truck Telemetry]] (8); [[Slow Truck in Curves]] (7); [[Alert Operator of Hazards]] (7); [[Stop Vehicle When Operator Is Out of Position]] (6); [[Stabilize Truck Dynamically]] (6); [[Operate in Cold Storage]] (6); [[Operate in Wet or Dusty Conditions]] (6); [[Detect Pedestrians and Objects Near Truck]] (6).
- **Documented for one group only (differentiator or documentation gap):** [[Communicate Battery State over CAN]] (H-Y); [[Cut Power in an Emergency]] (Hangcha); [[Reduce Wheel Slip]] (Crown); [[Indicate Maintenance Due]] (Toyota); [[Alert on Abnormal Condition]] (H-Y); [[Reduce Speed When Seat Belt Is Unfastened]] (KION); [[Cushion Fork Lowering]] (Hangcha); [[Cut Lift at Programmed Height]] (Toyota); [[Follow Operator Automatically]] (Jung.); [[Rotate Operator Workstation]] (KION); [[Steer with Electric Power Assist]] (Mitsu.); [[Estimate Remaining Run Time]] (KION); [[Deliver Constant Power Through Shift]] (H-Y); [[Refuel Truck Power Source in Minutes]] (H-Y).
- **Widest documented coverage:** KION Group, Toyota Industries Corporation, Crown Equipment; **thinnest:** Komatsu, Anhui Heli, Jungheinrich. Coverage reflects both the product range and how much was read.
- **Next research targets:** rows where a ranked group (Toyota, KION, Jungheinrich, Crown, Mitsubishi Logisnext, Hyster-Yale, Heli, Hangcha) shows a dot while at least three other groups show evidence; see the backlog item added with this note.

**Evidence behind each cell**

- **[[Charge Battery from Standard Power Outlet]]**
  - H-Y: trucks: [[Yale ERC050-060VGL]]
  - Heli: trucks: [[Heli A3 Series Lithium Forklifts]]; accessories and software: [[Heli Built-In Lithium Charger]]
- **[[Communicate Battery State over CAN]]**
  - H-Y: accessories and software: [[Hyster Power Cellect]]
- **[[Cut Power in an Emergency]]**
  - Hangcha: trucks: [[Hangcha XC Series Electric Forklifts]]
- **[[Hold Truck on Slope]]**
  - Crown: trucks: [[Crown FC 5700 Series]], [[Crown RC 5700 Series]]
  - Doosan: trucks: [[Doosan Bobcat 7-Series Plus Electric Forklifts]], [[Doosan Bobcat NXE Series Electric Forklifts]]
- **[[Reduce Wheel Slip]]**
  - Crown: trucks: [[Crown RR-RD 5700 Series]]
- **[[Stop Vehicle When Operator Is Out of Position]]**
  - Toyota: trucks: [[Raymond 4000 Series Counterbalanced Trucks]]; accessories and software: [[Raymond Operator Compartment Sensor System]], [[Raymond iWAREHOUSE Integrated Tether System]], [[Toyota Compartment Sensing System]]
  - Mitsu.: trucks: [[Cat 2EPC5000-2EP6500 Electric Pneumatic Tire Lift Trucks]], [[Mitsubishi FBCS Stand-Up Counterbalanced Forklifts]]; accessories and software: [[Cat Presence Detection System]]
  - Heli: accessories and software: [[Heli Operator Presence Sensing System]]
  - Hangcha: trucks: [[Hangcha XC Series Electric Forklifts]]
  - Doosan: trucks: [[Doosan Bobcat 7-Series Plus Electric Forklifts]]
  - Komatsu: accessories and software: [[Komatsu Operator Presence Sensing System]]
- **[[Display Truck Status to Operator]]**
  - Crown: trucks: [[Crown RC 5700 Series]]
  - Hangcha: trucks: [[Hangcha A Series Electric Forklifts]]
- **[[Indicate Maintenance Due]]**
  - Toyota: trucks: [[Toyota 3-Wheel Electric Forklift]]
- **[[Alert on Abnormal Condition]]**
  - H-Y: trucks: [[Yale ERC050-060VGL]]
- **[[Display Battery Status to Operator]]**
  - KION: accessories and software: [[Linde MT18 Multifunction Display]]
  - H-Y: trucks: [[Yale ERC050-060VGL]]
- **[[Adapt Speed to Load and Lift Height]]**
  - KION: accessories and software: [[Linde Load Management Advanced]], [[Linde System Control]]
  - Crown: trucks: [[Crown FC 5700 Series]]
- **[[Limit Truck Speed Automatically]]**
  - Toyota: accessories and software: [[Raymond In-Aisle Detection System]], [[Raymond Travel Speed Control]], [[Raymond iWAREHOUSE ObjectSense]], [[Toyota SEnS+ Pedestrian and Object Detection]]
  - KION: accessories and software: [[Linde Safety Guard]], [[STILL Safety Assist]]
  - Jung.: accessories and software: [[Jungheinrich Pedestrian Detection System]]
  - Crown: trucks: [[Crown FC 5700 Series]], [[Crown RC 5700 Series]], [[Crown RR-RD 5700 Series]]; accessories and software: [[Crown ProximityAssist System]]
  - Mitsu.: trucks: [[Cat 2EPC5000-2EP6500 Electric Pneumatic Tire Lift Trucks]]
  - H-Y: accessories and software: [[Hyster Reaction]]
  - Doosan: accessories and software: [[Doosan Bobcat Mast Sway Control]]
  - Komatsu: trucks: [[Komatsu FB Series Electric Forklifts]]
- **[[Limit Vehicle Motion by Location Zone]]**
  - Toyota: accessories and software: [[Raymond Zoning and Positioning]], [[Raymond iWAREHOUSE Real-Time Location System]]
  - KION: accessories and software: [[Linde Safety Guard]], [[Linde Safety Guard Zone Marker]], [[STILL Safety Assist]]
  - Jung.: accessories and software: [[Jungheinrich zoneCONTROL]]
  - H-Y: accessories and software: [[Hyster Reaction]], [[Yale Reliant Portfolio]]
- **[[Program Travel, Lift and Tilt Speeds]]**
  - KION: trucks: [[Linde E Series Electric Counterbalance Forklifts]]
  - Crown: trucks: [[Crown FC 5700 Series]], [[Crown RC 5700 Series]]
  - Heli: trucks: [[Heli G Series Lithium Forklifts]]
  - Komatsu: trucks: [[Komatsu FB Series Electric Forklifts]]
- **[[Reduce Speed When Seat Belt Is Unfastened]]**
  - KION: accessories and software: [[STILL EasyBelt]]
- **[[Slow Truck in Curves]]**
  - KION: accessories and software: [[STILL Curve Speed Control]], [[STILL Safety Assist]], [[STILL Safety Packages]]
  - Jung.: accessories and software: [[Jungheinrich curveCONTROL]]
  - Crown: trucks: [[Crown FC 5700 Series]], [[Crown RC 5700 Series]], [[Crown RR-RD 5700 Series]]
  - Mitsu.: accessories and software: [[UniCarriers Curve Control]]
  - H-Y: accessories and software: [[Hyster Dynamic Stability System]], [[Hyster Reaction]], [[Yale Reliant Portfolio]]
  - Heli: trucks: [[Heli G Series Lithium Forklifts]]
  - Hangcha: trucks: [[Hangcha XC Series Electric Forklifts]]
- **[[Cushion Fork Lowering]]**
  - Hangcha: trucks: [[Hangcha A Series Electric Forklifts]], [[Hangcha XC Series Electric Forklifts]]
- **[[Cut Lift at Programmed Height]]**
  - Toyota: accessories and software: [[Raymond Mast Lift Limit Switch with Bypass]]
- **[[Damp Mast Oscillation]]**
  - KION: accessories and software: [[Linde Dynamic Mast Control]]
  - Doosan: accessories and software: [[Doosan Bobcat Mast Sway Control]]
- **[[Restrict Lift When Load Exceeds Limit]]**
  - KION: accessories and software: [[Linde Load Management Advanced]], [[Linde Safety Pilot]]
  - H-Y: accessories and software: [[Yale Reliant Portfolio]]
- **[[Sense Load Weight and Lift Height]]**
  - Toyota: accessories and software: [[Raymond Load Weight Display]], [[Toyota Assist]], [[Toyota Load Weight Sensing]]
  - KION: accessories and software: [[Linde Load Management Advanced]], [[Linde Safety Pilot]]
  - Crown: accessories and software: [[Crown Capacity Data Monitor]]
  - Komatsu: accessories and software: [[Komatsu Digital Load Scale]]
- **[[Stabilize Truck Dynamically]]**
  - Toyota: accessories and software: [[Toyota Assist]], [[Toyota System of Active Stability]]
  - KION: accessories and software: [[Linde Safety Pilot]]
  - Jung.: accessories and software: [[Jungheinrich curveCONTROL]]
  - Crown: trucks: [[Crown FC 5700 Series]], [[Crown RC 5700 Series]]
  - H-Y: accessories and software: [[Hyster Dynamic Stability System]], [[Hyster Reaction]]
  - Doosan: trucks: [[Doosan Bobcat NXE Series Electric Forklifts]]
- **[[Control Operator Access]]**
  - Toyota: trucks: [[Raymond 8000 Series Pallet Trucks]]; accessories and software: [[Toyota PIN Code Access Pad]]
  - KION: trucks: [[STILL EXH-SF Low Lift Pallet Truck]], [[STILL RX 60 Electric Forklift]]; accessories and software: [[Linde connect]], [[STILL FleetManager]], [[STILL Safety Assist]], [[STILL Smart Portal]]
  - Crown: trucks: [[Crown RC 5700 Series]]
  - Mitsu.: accessories and software: [[Logisnext Lift Link]]; third-party: [[Powerfleet Forklift Gateway]]
  - Hangcha: trucks: [[Hangcha XC Series Electric Forklifts]]
- **[[Enforce Pre-Shift Checklist]]**
  - KION: trucks: [[STILL RX 60 Electric Forklift]]
  - Jung.: accessories and software: [[Jungheinrich ISM Online]]
  - Mitsu.: accessories and software: [[Logisnext Lift Link]]; third-party: [[Powerfleet Forklift Gateway]]
- **[[Report Truck Telemetry]]**
  - Toyota: accessories and software: [[Raymond iWAREHOUSE]]
  - KION: accessories and software: [[Linde connect]], [[STILL FleetManager]], [[STILL Smart Portal]], [[STILL neXXt fleet]]
  - Jung.: accessories and software: [[Jungheinrich ISM Online]]
  - Mitsu.: accessories and software: [[Logisnext Lift Link]]; third-party: [[Powerfleet Forklift Gateway]]
  - Heli: accessories and software: [[Heli Fleet Management System]]
  - Hangcha: accessories and software: [[Hangcha FIMS]]
  - Doosan: accessories and software: [[Doosan Lin-Q]]
  - Komatsu: accessories and software: [[Komatsu KOMTRAX]]
- **[[Operate in Cold Storage]]**
  - Toyota: accessories and software: [[Toyota Cold Conditioning Package]]
  - Crown: trucks: [[Crown RC 5700 Series]]
  - Mitsu.: accessories and software: [[UniCarriers Freezer Option]]
  - Heli: trucks: [[Heli G Series Lithium Forklifts]]
  - Hangcha: trucks: [[Hangcha XC Series Electric Forklifts]]
  - Doosan: trucks: [[Doosan Bobcat NXE Series Electric Forklifts]]
- **[[Operate in Wet or Dusty Conditions]]**
  - Toyota: trucks: [[Raymond 8000 Series Pallet Trucks]]
  - KION: trucks: [[Linde E Series Electric Counterbalance Forklifts]]
  - Crown: trucks: [[Crown RC 5700 Series]]
  - Heli: trucks: [[Heli A3 Series Lithium Forklifts]]
  - Doosan: trucks: [[Doosan Bobcat NXE Series Electric Forklifts]]
  - Komatsu: trucks: [[Komatsu FB Series Electric Forklifts]]
- **[[Shelter Operator from Weather]]**
  - Toyota: trucks: [[Raymond 4000 Series Counterbalanced Trucks]]
  - Mitsu.: trucks: [[Cat 2EPC5000-2EP6500 Electric Pneumatic Tire Lift Trucks]]
- **[[Protect Battery from Deep Discharge]]**
  - Crown: trucks: [[Crown RC 5700 Series]]
  - H-Y: accessories and software: [[Hyster Power Cellect]]
- **[[Follow Operator Automatically]]**
  - Jung.: accessories and software: [[Jungheinrich easyPILOT]]
- **[[Rotate Operator Workstation]]**
  - KION: accessories and software: [[Linde Rotating Operator Workstation]]
- **[[Steer with Electric Power Assist]]**
  - Mitsu.: trucks: [[Mitsubishi FB 3-Wheel Electric Forklifts]], [[Mitsubishi FBCS Stand-Up Counterbalanced Forklifts]]
- **[[Estimate Remaining Run Time]]**
  - KION: trucks: [[Linde 6-8 t Electric Counterbalance Forklifts]]
- **[[Detect Pedestrians and Objects Near Truck]]**
  - Toyota: accessories and software: [[Raymond In-Aisle Detection System]], [[Raymond iWAREHOUSE Fieldsense]], [[Raymond iWAREHOUSE ObjectSense]], [[Toyota Assist]], [[Toyota Object Detection Radar]], [[Toyota SEnS Pedestrian Detection]], [[Toyota SEnS+ Pedestrian and Object Detection]]
  - KION: accessories and software: [[Linde Motion Detection]], [[Linde Safety Guard]], [[Linde Safety Guard Truck Unit]]
  - Jung.: accessories and software: [[Jungheinrich Pedestrian Detection System]], [[Jungheinrich Reverse Area Warning System]], [[Jungheinrich zoneCONTROL]]; third-party: [[Blaxtair Pedestrian Detection System]]
  - Crown: accessories and software: [[Crown ProximityAssist System]]
  - H-Y: accessories and software: [[Hyster Pedestrian Awareness Camera]], [[Hyster Reaction]], [[Yale Reliant Portfolio]]
  - Doosan: accessories and software: [[Doosan Bobcat Pedestrian Detection Camera]]
- **[[Detect and Record Impacts]]**
  - Toyota: accessories and software: [[Raymond iWAREHOUSE]]
  - KION: accessories and software: [[Linde connect]], [[STILL Smart Portal]]
  - Mitsu.: accessories and software: [[Logisnext Lift Link]]; third-party: [[Powerfleet Forklift Gateway]]
- **[[Change Battery Quickly]]**
  - Toyota: trucks: [[Toyota Traigo48]]
  - Hangcha: trucks: [[Hangcha A Series Electric Forklifts]], [[Hangcha XC Series Electric Forklifts]]
  - Doosan: trucks: [[Doosan Bobcat 7-Series Plus Electric Forklifts]]
- **[[Deliver Constant Power Through Shift]]**
  - H-Y: trucks: [[Hyster J1.5-3.0UT(L)]], [[Yale ERC080VHL]]; accessories and software: [[Nuvera PowerEdge]]
- **[[Recover Energy by Regeneration]]**
  - Toyota: trucks: [[Raymond 7000 Series Reach-Fork Trucks]]
  - Crown: trucks: [[Crown RC 5700 Series]]
- **[[Refuel Truck Power Source in Minutes]]**
  - H-Y: accessories and software: [[Nuvera PowerEdge]]
- **[[Assist Lift Positioning]]**
  - Toyota: accessories and software: [[Raymond Fork Tilt Leveling]], [[Raymond Fork-Tip Laser Guide]], [[Raymond Vantage Point System]], [[Toyota Acu-Laser]], [[Toyota Assist]], [[Toyota Auto Height Select]], [[Toyota Carriage-Mounted Camera]]
  - Crown: trucks: [[Crown RR-RD 5700 Series]]
- **[[Show Camera View to Operator]]**
  - Toyota: accessories and software: [[Raymond Vantage Point System]], [[Toyota 360 Operating Camera]], [[Toyota Assist]], [[Toyota Carriage-Mounted Camera]]
  - Jung.: accessories and software: [[Jungheinrich addedVIEW Camera Systems]]
  - Crown: trucks: [[Crown RR-RD 5700 Series]]
  - Hangcha: accessories and software: [[Hangcha Backup Camera Option]]
- **[[Alert Operator of Hazards]]**
  - Toyota: accessories and software: [[Raymond iWAREHOUSE Fieldsense]], [[Raymond iWAREHOUSE ObjectSense]], [[Toyota SEnS Pedestrian Detection]], [[Toyota SEnS+ Pedestrian and Object Detection]]
  - KION: accessories and software: [[Linde Safety Guard Truck Unit]]
  - Jung.: accessories and software: [[Jungheinrich Reverse Area Warning System]], [[Jungheinrich zoneCONTROL]]; third-party: [[Blaxtair Pedestrian Detection System]]
  - Crown: accessories and software: [[Crown InfoLink 7-inch Touch Display]], [[Crown ProximityAssist System]]
  - Mitsu.: accessories and software: [[Mitsubishi Integrated Presence System]]
  - H-Y: accessories and software: [[Hyster Dynamic Stability System]], [[Hyster Pedestrian Awareness Camera]], [[Hyster Reaction]]
  - Doosan: accessories and software: [[Doosan Bobcat Pedestrian Detection Camera]]
- **[[Warn Pedestrians of Approaching Truck]]**
  - Toyota: accessories and software: [[Toyota Forklift Lighting Options]]
  - KION: accessories and software: [[Linde BlueSpot]], [[Linde Safety Guard]], [[Linde Safety Guard Portable Unit]], [[Linde Safety Guard Static Unit]], [[STILL Safety Assist]], [[STILL Safety Packages]], [[STILL SafetyLight 4Plus]], [[STILL Warning Zone Light]]
  - Crown: trucks: [[Crown RC 5700 Series]]
  - Mitsu.: accessories and software: [[Cat Safety Lighting Options]]
  - Hangcha: trucks: [[Hangcha A Series Electric Forklifts]]

## Aliases

- Truck feature matrix

## Former ids
