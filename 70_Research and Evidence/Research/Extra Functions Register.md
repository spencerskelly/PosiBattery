---
type: Info
subtype:
id: INFO-00252
uid: 20261003193952678skellyspencer
status: Draft
tags:
  - review
  - features
  - extras
describes:
  - "[[Battery-Connected Product]]"
---

# Extra Functions Register

## Definition

Which functions are 'Extra': controlled by devices or software and offered by fewer than half of the maker groups of that host kind, with the numbers behind each call.

## Notes

- **Owner definition (2026-10-03):** 'bonus' features are any features that are controlled by devices or software features not on every system; the owner chose to mark the function as Extra when it is uncommon. Hosts: all (trucks, batteries, chargers, GSE, fuel cells).
- **Rule (proposed numbers):** a function is Extra when (1) it is delivered by a device or software, meaning it is not on the short list of physical, chemical or enclosure features, and (2) fewer than 50 percent of the maker groups that make hosts of its main kind are documented to offer it, built in or through their own accessory notes. The main kind is the host kind with the most performing notes. Third-party accessories do not count toward prevalence. Tag `extra` is written on the function note with a line saying why.
- **Result:** 70 functions marked Extra, 12 Core, 1 with insufficient data (fewer than 5 maker groups of the host kind), 8 physical, chemical or enclosure features that are not device-controlled (an explicit list: constant power through a shift, soft fork lowering, wet or dusty and cold operation, cabin shelter, quick battery change, rotating workstation, hydrogen refuelling). Sensitivity of the Extra count to the threshold: 57 at 25 percent, 70 at 50 percent, 80 at 75 percent.
- **How to read battery and charger rows:** nearly every battery-side function is delivered by aftermarket devices (monitors, watering, circulation), which are not offered by battery makers themselves, so they come out as Extra by nature; charger functions are software or hardware inside the charger that few makers document.
- **Limits (read before using the tags):** prevalence is counted in the vault's documentation, not in the market; a function with few maker groups may only be thinly researched (see the documentation depth in [[Truck Feature Comparison Matrix]]). The tags should be re-run when coverage changes; the numbers below are generated.
- **Host links added in round 30:** 9 accessory and host pairs were linked where the accessory's own source names the host; most of the other unlinked accessories are maker-level options or aftermarket devices with no named host, so they stay unlinked rather than guessed.
- **2026-10-06 amp-hour scope correction:** [[Inventus Smart Battery Monitor SBM-01]] was reclassified as a lifetime-Ah display/reporting endpoint rather than an amp-hour accumulator. The generated prevalence/accessory-count fields below have not been regenerated in this edit; the implementation dependency was updated to [[Current Integration Amp-Hour Accumulation]].
- **2026-10-06 SOC scope correction:** [[EnerSys Truck iQ]] and [[Inventus Smart Battery Monitor SBM-01]] were reclassified as SOC display endpoints rather than estimators. The generated prevalence/count fields below have not been regenerated in this edit; only the now-known [[State of Charge Estimation Design]] dependency was updated.
- **Host scope:** every accessory note now carries `scope-oem-option` (its maker also makes hosts of that kind) or `scope-aftermarket`; counts below.

**Host scope by accessory type**

| Accessory type | Maker's own option (maker also makes hosts of that kind) | Aftermarket (maker makes no hosts of that kind) |
|---|---|---|
| Battery Accessories | 16 | 36 |
| Charger Accessories | 8 | 0 |
| Fleet Software and Platforms | 24 | 4 |
| Vehicle Accessories | 79 | 11 |

**Functions by status**

| Function | Host kind | Maker groups offering | Of | Prevalence | Delivered by (designs it depends on) | Accessory or software notes | Third-party makers | Status |
|---|---|---|---|---|---|---|---|---|
| [[Complete Missed Equalization Automatically]] | battery | 0 | 21 | 0% | - | 1 | 1 | Extra |
| [[Detect Cell Failure]] | battery | 0 | 21 | 0% | [[Cell Failure Diagnostic Design]] | 1 | 1 | Extra |
| [[Export Battery Data to PC]] | battery | 0 | 21 | 0% | - | 3 | 2 | Extra |
| [[Measure Electrolyte Specific Gravity]] | battery | 0 | 21 | 0% | [[In-Cell Specific Gravity Probe]] | 1 | 1 | Extra |
| [[Alert on Low Electrolyte Level]] | battery | 1 | 21 | 5% | [[Electrolyte Level Sensing Design]], [[Low Electrolyte Alert Design]] | 1 | 0 | Extra |
| [[Calculate Battery Abuse Cycles]] | battery | 1 | 21 | 5% | [[Battery Abuse Cycle Analytics]] | 1 | 0 | Extra |
| [[Command Vehicle Operating Limits over CAN]] | battery | 1 | 21 | 5% | [[CAN Vehicle Operating Limit Command]] | 1 | 0 | Extra |
| [[Communicate Battery State over CAN]] | battery | 1 | 21 | 5% | [[CAN Interface]] | 4 | 3 | Extra |
| [[Detect Battery Weight]] | battery | 1 | 21 | 5% | [[Battery Weight Determination Design]] | 1 | 0 | Extra |
| [[Estimate Remaining Run Time]] | battery | 1 | 21 | 5% | [[Remaining Runtime Estimation Design]] | 1 | 0 | Extra |
| [[Estimate State of Health]] | battery | 1 | 21 | 5% | [[Usage-History State of Health Analytics]] | 1 | 0 | Extra |
| [[Configure Device from Mobile App or PC]] | battery | 2 | 21 | 10% | - | 4 | 1 | Extra |
| [[Connect Battery to Charger or Vehicle]] | battery | 2 | 21 | 10% | - | 3 | 1 | Extra |
| [[Detect Voltage Imbalance]] | battery | 2 | 21 | 10% | [[Voltage Imbalance Detection Design]] | 3 | 0 | Extra |
| [[Identify Battery to Charger]] | battery | 2 | 21 | 10% | - | 5 | 2 | Extra |
| [[Report Battery Temperature to Charger]] | battery | 2 | 21 | 10% | - | 5 | 2 | Extra |
| [[Transmit Battery Data Wirelessly]] | battery | 2 | 21 | 10% | [[Wireless Interface Design]] | 21 | 6 | Extra |
| [[Track Equalization]] | battery | 3 | 21 | 14% | [[Equalization Event Tracking Design]] | 6 | 3 | Extra |
| [[Water Battery Cells]] | battery | 3 | 21 | 14% | - | 6 | 2 | Extra |
| [[Accumulate Amp-Hours]] | battery | 4 | 21 | 19% | [[Current Integration Amp-Hour Accumulation]] | 12 | 4 | Extra |
| [[Circulate Electrolyte]] | battery | 4 | 21 | 19% | [[Forced Electrolyte Circulation]] | 3 | 0 | Extra |
| [[Communicate with Charger]] | battery | 4 | 21 | 19% | - | 10 | 3 | Extra |
| [[Estimate State of Charge]] | battery | 4 | 21 | 19% | [[State of Charge Estimation Design]] | 11 | 4 | Extra |
| [[Indicate Battery Status Locally]] | battery | 4 | 21 | 19% | [[Warning and Display Device Design]] | 17 | 5 | Extra |
| [[Measure Battery Current]] | battery | 4 | 21 | 19% | [[Current Sensing Design]] | 14 | 5 | Extra |
| [[Upload Battery Data to Cloud Portal]] | battery | 4 | 21 | 19% | [[Wireless Interface Design]], [[Cloud Portal Integration]] | 18 | 6 | Extra |
| [[Alert on Abnormal Condition]] | battery | 5 | 21 | 24% | [[Abnormal Condition Alert Design]] | 18 | 7 | Extra |
| [[Log Battery Events and Usage]] | battery | 5 | 21 | 24% | [[Data Handling Design]] | 23 | 4 | Extra |
| [[Measure Battery Temperature]] | battery | 6 | 21 | 29% | [[Battery Temperature Measurement Design]] | 27 | 8 | Extra |
| [[Measure Battery Voltage]] | battery | 6 | 21 | 29% | - | 20 | 8 | Extra |
| [[Sense Electrolyte Level]] | battery | 6 | 21 | 29% | [[Electrolyte Level Sensing Design]] | 26 | 9 | Extra |
| [[Charge Battery Wirelessly]] | charger | 1 | 18 | 6% | - | 0 | 0 | Extra |
| [[Charge in Cold Storage]] | charger | 1 | 18 | 6% | - | 0 | 0 | Extra |
| [[Desulfate Battery During Charge]] | charger | 1 | 18 | 6% | - | 0 | 0 | Extra |
| [[Detect Foreign and Live Objects]] | charger | 1 | 18 | 6% | - | 0 | 0 | Extra |
| [[Diagnose Battery During Charge]] | charger | 1 | 18 | 6% | - | 0 | 0 | Extra |
| [[Float Charge Battery]] | charger | 1 | 18 | 6% | - | 0 | 0 | Extra |
| [[Continue Charging Through Module Fault]] | charger | 2 | 18 | 11% | [[Modular Power Modules]] | 0 | 0 | Extra |
| [[Manage Charging Cables]] | charger | 2 | 18 | 11% | - | 2 | 0 | Extra |
| [[Equalize Battery on Schedule]] | charger | 4 | 18 | 22% | - | 0 | 0 | Extra |
| [[Identify Battery by Voltage]] | charger | 4 | 18 | 22% | - | 0 | 0 | Extra |
| [[Charge Under BMS Control]] | charger | 5 | 18 | 28% | [[Integrated Battery Management System]] | 0 | 0 | Extra |
| [[Manage Chargers Remotely]] | charger | 5 | 18 | 28% | - | 2 | 0 | Extra |
| [[Charge Battery Conventionally]] | charger | 8 | 18 | 44% | - | 0 | 0 | Extra |
| [[Charge Battery Fast]] | charger | 8 | 18 | 44% | - | 0 | 0 | Extra |
| [[Charge Battery by Opportunity]] | charger | 8 | 18 | 44% | - | 0 | 0 | Extra |
| [[Compensate Charge for Battery Temperature]] | charger | 8 | 18 | 44% | - | 1 | 0 | Extra |
| [[Charge Lithium-Ion Battery]] | charger | 11 | 18 | 61% | - | 0 | 0 | Core |
| [[Report Fuel Cell State to Truck]] | fuel cell | 1 | 2 | 50% | - | 0 | 0 | insufficient data (fewer than 5 maker groups) |
| [[Refuel Truck Power Source in Minutes]] | fuel cell | 2 | 2 | 100% | [[Hydrogen Storage Tank]] | 0 | 0 | physical, chemical or enclosure (not device-controlled) |
| [[Indicate Aircraft Proximity to Operator]] | gse | 1 | 6 | 17% | [[Aircraft Proximity Indicator Light]] | 1 | 0 | Extra |
| [[Slow and Stop Near Aircraft]] | gse | 1 | 6 | 17% | [[Object and Proximity Sensing Design]] | 1 | 0 | Extra |
| [[Cushion Fork Lowering]] | truck | 1 | 10 | 10% | - | 0 | 0 | physical, chemical or enclosure (not device-controlled) |
| [[Cut Lift at Programmed Height]] | truck | 1 | 10 | 10% | [[Mast Lift Limit Switch]] | 1 | 0 | Extra |
| [[Cut Power in an Emergency]] | truck | 1 | 10 | 10% | [[Emergency Cut-Off Switch]] | 0 | 0 | Extra |
| [[Deliver Constant Power Through Shift]] | truck | 1 | 10 | 10% | - | 0 | 0 | physical, chemical or enclosure (not device-controlled) |
| [[Follow Operator Automatically]] | truck | 1 | 10 | 10% | [[Belt-Worn Remote Control]] | 1 | 0 | Extra |
| [[Indicate Maintenance Due]] | truck | 1 | 10 | 10% | - | 0 | 0 | Extra |
| [[Reduce Speed When Seat Belt Is Unfastened]] | truck | 1 | 10 | 10% | [[Seat Belt Interlock]] | 1 | 0 | Extra |
| [[Reduce Wheel Slip]] | truck | 1 | 10 | 10% | - | 0 | 0 | Extra |
| [[Rotate Operator Workstation]] | truck | 1 | 10 | 10% | - | 1 | 0 | physical, chemical or enclosure (not device-controlled) |
| [[Steer with Electric Power Assist]] | truck | 1 | 10 | 10% | [[Electric Power Steering]] | 0 | 0 | Extra |
| [[Adapt Speed to Load and Lift Height]] | truck | 2 | 10 | 20% | [[Vehicle State Sensing Design]] | 2 | 0 | Extra |
| [[Assist Lift Positioning]] | truck | 2 | 10 | 20% | - | 7 | 0 | Extra |
| [[Charge Battery from Standard Power Outlet]] | truck | 2 | 10 | 20% | [[Battery Onboard Charger]] | 0 | 0 | Extra |
| [[Damp Mast Oscillation]] | truck | 2 | 10 | 20% | - | 2 | 0 | Extra |
| [[Display Battery Status to Operator]] | truck | 2 | 10 | 20% | [[Vehicle Operator Display Design]] | 2 | 1 | Extra |
| [[Display Truck Status to Operator]] | truck | 2 | 10 | 20% | [[Vehicle Operator Display Design]] | 0 | 0 | Extra |
| [[Hold Truck on Slope]] | truck | 2 | 10 | 20% | - | 0 | 0 | Extra |
| [[Protect Battery from Deep Discharge]] | truck | 2 | 10 | 20% | [[Deep Discharge Protection Design]] | 1 | 0 | Extra |
| [[Recover Energy by Regeneration]] | truck | 2 | 10 | 20% | [[Regenerative Braking]] | 0 | 0 | Extra |
| [[Restrict Lift When Load Exceeds Limit]] | truck | 2 | 10 | 20% | [[Vehicle State Sensing Design]] | 3 | 0 | Extra |
| [[Shelter Operator from Weather]] | truck | 2 | 10 | 20% | - | 0 | 0 | physical, chemical or enclosure (not device-controlled) |
| [[Change Battery Quickly]] | truck | 3 | 10 | 30% | [[Quick-Change Battery Compartment]] | 0 | 0 | physical, chemical or enclosure (not device-controlled) |
| [[Limit Vehicle Motion by Location Zone]] | truck | 4 | 10 | 40% | - | 8 | 0 | Extra |
| [[Program Travel, Lift and Tilt Speeds]] | truck | 4 | 10 | 40% | [[Programmable Motor Controller]] | 0 | 0 | Extra |
| [[Sense Load Weight and Lift Height]] | truck | 4 | 10 | 40% | [[Vehicle State Sensing Design]] | 7 | 0 | Extra |
| [[Show Camera View to Operator]] | truck | 4 | 10 | 40% | [[Display Device Design]] | 7 | 1 | Extra |
| [[Detect and Record Impacts]] | truck | 5 | 10 | 50% | [[Impact Sensor]] | 10 | 3 | Core |
| [[Enforce Pre-Shift Checklist]] | truck | 5 | 10 | 50% | [[Display Device Design]] | 5 | 1 | Core |
| [[Warn Pedestrians of Approaching Truck]] | truck | 5 | 10 | 50% | [[Indicator and Alarm Design]] | 14 | 4 | Core |
| [[Control Operator Access]] | truck | 6 | 10 | 60% | [[Operator Identification Design]] | 10 | 2 | Core |
| [[Detect Pedestrians and Objects Near Truck]] | truck | 6 | 10 | 60% | [[Object and Proximity Sensing Design]] | 24 | 6 | Core |
| [[Operate in Cold Storage]] | truck | 6 | 10 | 60% | - | 2 | 0 | physical, chemical or enclosure (not device-controlled) |
| [[Operate in Wet or Dusty Conditions]] | truck | 6 | 10 | 60% | - | 0 | 0 | physical, chemical or enclosure (not device-controlled) |
| [[Stabilize Truck Dynamically]] | truck | 6 | 10 | 60% | - | 6 | 0 | Core |
| [[Stop Vehicle When Operator Is Out of Position]] | truck | 6 | 10 | 60% | [[Operator Presence Sensing Design]] | 7 | 1 | Core |
| [[Alert Operator of Hazards]] | truck | 7 | 10 | 70% | [[Warning and Display Device Design]] | 15 | 1 | Core |
| [[Slow Truck in Curves]] | truck | 7 | 10 | 70% | - | 8 | 0 | Core |
| [[Limit Truck Speed Automatically]] | truck | 8 | 10 | 80% | - | 13 | 3 | Core |
| [[Report Truck Telemetry]] | truck | 10 | 10 | 100% | [[Wireless Interface Design]] | 18 | 3 | Core |

**Extras (uncommon, device or software controlled)**

- [[Accumulate Amp-Hours]] (battery; 4 of 21)
- [[Alert on Abnormal Condition]] (battery; 5 of 21)
- [[Alert on Low Electrolyte Level]] (battery; 1 of 21)
- [[Calculate Battery Abuse Cycles]] (battery; 1 of 21)
- [[Circulate Electrolyte]] (battery; 4 of 21)
- [[Command Vehicle Operating Limits over CAN]] (battery; 1 of 21)
- [[Communicate Battery State over CAN]] (battery; 1 of 21)
- [[Communicate with Charger]] (battery; 4 of 21)
- [[Complete Missed Equalization Automatically]] (battery; 0 of 21)
- [[Configure Device from Mobile App or PC]] (battery; 2 of 21)
- [[Connect Battery to Charger or Vehicle]] (battery; 2 of 21)
- [[Detect Battery Weight]] (battery; 1 of 21)
- [[Detect Cell Failure]] (battery; 0 of 21)
- [[Detect Voltage Imbalance]] (battery; 2 of 21)
- [[Estimate Remaining Run Time]] (battery; 1 of 21)
- [[Estimate State of Charge]] (battery; 4 of 21)
- [[Estimate State of Health]] (battery; 1 of 21)
- [[Export Battery Data to PC]] (battery; 0 of 21)
- [[Identify Battery to Charger]] (battery; 2 of 21)
- [[Indicate Battery Status Locally]] (battery; 4 of 21)
- [[Log Battery Events and Usage]] (battery; 5 of 21)
- [[Measure Battery Current]] (battery; 4 of 21)
- [[Measure Battery Temperature]] (battery; 6 of 21)
- [[Measure Battery Voltage]] (battery; 6 of 21)
- [[Measure Electrolyte Specific Gravity]] (battery; 0 of 21)
- [[Report Battery Temperature to Charger]] (battery; 2 of 21)
- [[Sense Electrolyte Level]] (battery; 6 of 21)
- [[Track Equalization]] (battery; 3 of 21)
- [[Transmit Battery Data Wirelessly]] (battery; 2 of 21)
- [[Upload Battery Data to Cloud Portal]] (battery; 4 of 21)
- [[Water Battery Cells]] (battery; 3 of 21)
- [[Charge Battery Conventionally]] (charger; 8 of 18)
- [[Charge Battery Fast]] (charger; 8 of 18)
- [[Charge Battery Wirelessly]] (charger; 1 of 18)
- [[Charge Battery by Opportunity]] (charger; 8 of 18)
- [[Charge Under BMS Control]] (charger; 5 of 18)
- [[Charge in Cold Storage]] (charger; 1 of 18)
- [[Compensate Charge for Battery Temperature]] (charger; 8 of 18)
- [[Continue Charging Through Module Fault]] (charger; 2 of 18)
- [[Desulfate Battery During Charge]] (charger; 1 of 18)
- [[Detect Foreign and Live Objects]] (charger; 1 of 18)
- [[Diagnose Battery During Charge]] (charger; 1 of 18)
- [[Equalize Battery on Schedule]] (charger; 4 of 18)
- [[Float Charge Battery]] (charger; 1 of 18)
- [[Identify Battery by Voltage]] (charger; 4 of 18)
- [[Manage Chargers Remotely]] (charger; 5 of 18)
- [[Manage Charging Cables]] (charger; 2 of 18)
- [[Indicate Aircraft Proximity to Operator]] (gse; 1 of 6)
- [[Slow and Stop Near Aircraft]] (gse; 1 of 6)
- [[Adapt Speed to Load and Lift Height]] (truck; 2 of 10)
- [[Assist Lift Positioning]] (truck; 2 of 10)
- [[Charge Battery from Standard Power Outlet]] (truck; 2 of 10)
- [[Cut Lift at Programmed Height]] (truck; 1 of 10)
- [[Cut Power in an Emergency]] (truck; 1 of 10)
- [[Damp Mast Oscillation]] (truck; 2 of 10)
- [[Display Battery Status to Operator]] (truck; 2 of 10)
- [[Display Truck Status to Operator]] (truck; 2 of 10)
- [[Follow Operator Automatically]] (truck; 1 of 10)
- [[Hold Truck on Slope]] (truck; 2 of 10)
- [[Indicate Maintenance Due]] (truck; 1 of 10)
- [[Limit Vehicle Motion by Location Zone]] (truck; 4 of 10)
- [[Program Travel, Lift and Tilt Speeds]] (truck; 4 of 10)
- [[Protect Battery from Deep Discharge]] (truck; 2 of 10)
- [[Recover Energy by Regeneration]] (truck; 2 of 10)
- [[Reduce Speed When Seat Belt Is Unfastened]] (truck; 1 of 10)
- [[Reduce Wheel Slip]] (truck; 1 of 10)
- [[Restrict Lift When Load Exceeds Limit]] (truck; 2 of 10)
- [[Sense Load Weight and Lift Height]] (truck; 4 of 10)
- [[Show Camera View to Operator]] (truck; 4 of 10)
- [[Steer with Electric Power Assist]] (truck; 1 of 10)

## Aliases

- Extra functions
- Bonus features

## Former ids
