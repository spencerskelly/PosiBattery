---
type: Info
subtype:
id: INFO-00225
uid: 20261003141234122skellyspencer
status: Draft
tags:
  - register
  - functions
  - designs
  - dependencies
describes:
  - "[[Battery-Connected Product]]"
---

# Function Design Dependencies

## Definition

Register of which designs each function depends on, with the basis for each dependency.

## Notes

- **Owner decision (Q16, 2026-10-03):** functions depend on designs; for example showing state of charge depends on a display, and a low water level alert depends on a water level sensor. Written as `dependsOn` on the Function (inverse `dependencyOf` on the Design).
- **Rule:** depend on the most specific design that every known implementation of the function uses; if the implementations differ, depend on their general design class; if only one implementation is known, depend on that design and flag it for generalizing when a second appears.
- **Basis:** 'owner-stated example' is the owner's wording; 'analyst inference (necessity)' is engineering logic that the function cannot work without that kind of design. Neither is a vendor claim; the vendor evidence for each product is on the product notes.
- **Not written (no design note yet):** voltage and temperature measurement (needs a general temperature sensor design when two are found), stop on operator out of position for seat switches, charging wirelessly, estimating state of charge.

| Function | Depends on design | Basis | Why |
|---|---|---|---|
| [[Display Battery Status to Operator]] | [[Display Device Design]] | owner-stated example | owner example: displaying state of charge depends on a display |
| [[Alert on Low Electrolyte Level]] | [[Capacitive Electrolyte Level Probe]], [[Indicator and Alarm Design]] | owner-stated example | owner example: a low water alert depends on a water level sensor; the probe is the only level-sensing design found so far, so the dependency sits on it (generalize when a second appears) |
| [[Sense Electrolyte Level]] | [[Capacitive Electrolyte Level Probe]] | analyst inference (necessity) | needs a level sensing element; only one design found so far |
| [[Indicate Battery Status Locally]] | [[Warning and Display Device Design]] | analyst inference (necessity) | needs either an indicator or a display |
| [[Alert on Abnormal Condition]] | [[Warning and Display Device Design]] | analyst inference (necessity) | needs a way to signal the condition |
| [[Alert Operator of Hazards]] | [[Warning and Display Device Design]] | analyst inference (necessity) | needs a light, sound or display |
| [[Warn Pedestrians of Approaching Truck]] | [[Indicator and Alarm Design]] | analyst inference (necessity) | needs a light, sound or wearable |
| [[Indicate Aircraft Proximity to Operator]] | [[Aircraft Proximity Indicator Light]] | analyst inference (necessity) | only implementation found |
| [[Show Camera View to Operator]] | [[Display Device Design]] | analyst inference (necessity) | needs a display |
| [[Measure Battery Current]] | [[Current Sensing Design]] | analyst inference (necessity) | needs a current sensing method |
| [[Detect Pedestrians and Objects Near Truck]] | [[Object and Proximity Sensing Design]] | analyst inference (necessity) | needs a sensing technology |
| [[Slow and Stop Near Aircraft]] | [[Object and Proximity Sensing Design]] | analyst inference (necessity) | needs distance sensing |
| [[Detect and Record Impacts]] | [[Impact Sensor]] | analyst inference (necessity) | needs an impact sensor |
| [[Control Operator Access]] | [[Operator Identification Design]] | analyst inference (necessity) | needs a way to identify the operator |
| [[Stop Vehicle When Operator Is Out of Position]] | [[Operator Presence Sensing Design]] | analyst inference (necessity) | needs a way to sense the operator |
| [[Sense Load Weight and Lift Height]] | [[Vehicle State Sensing Design]] | analyst inference (necessity) | needs a load or height sensor |
| [[Restrict Lift When Load Exceeds Limit]] | [[Vehicle State Sensing Design]] | analyst inference (necessity) | needs a load sensor |
| [[Recover Energy by Regeneration]] | [[Regenerative Braking]] | analyst inference (necessity) | is the design |
| [[Refuel Truck Power Source in Minutes]] | [[Hydrogen Storage Tank]] | analyst inference (necessity) | needs on-truck fuel storage (fuel cell trucks) |
| [[Circulate Electrolyte]] | [[Forced Electrolyte Circulation]] | analyst inference (necessity) | is the mechanism |
| [[Log Battery Events and Usage]] | [[Non-Volatile Event Memory]] | analyst inference (necessity) | needs storage that survives power loss |
| [[Continue Charging Through Module Fault]] | [[Modular Power Modules]] | analyst inference (necessity) | needs a modular power stage |
| [[Charge Under BMS Control]] | [[Integrated Battery Management System]] | analyst inference (necessity) | needs a BMS |
| [[Communicate Battery State over CAN]] | [[CAN Interface]] | analyst inference (necessity) | needs a CAN interface |
| [[Command Vehicle Operating Limits over CAN]] | [[CAN Interface]] | analyst inference (necessity) | needs a CAN interface |
| [[Transmit Battery Data Wirelessly]] | [[Wireless Interface Design]] | analyst inference (necessity) | needs a radio interface |
| [[Upload Battery Data to Cloud Portal]] | [[Wireless Interface Design]], [[Cloud Portal Integration]] | analyst inference (necessity) | needs a radio path and a portal |
| [[Report Truck Telemetry]] | [[Wireless Interface Design]] | analyst inference (necessity) | needs a radio path to the portal |
| [[Follow Operator Automatically]] | [[Belt-Worn Remote Control]] | analyst inference (necessity) | the operator's signal comes from a worn remote (easyPILOT) |
| [[Adapt Speed to Load and Lift Height]] | [[Vehicle State Sensing Design]] | analyst inference (necessity) | needs the load and height measured |
| [[Enforce Pre-Shift Checklist]] | [[Display Device Design]] | analyst inference (necessity) | the checklist is shown on a display (keypad or touch) |
| [[Change Battery Quickly]] | [[Quick-Change Battery Compartment]] | analyst inference (necessity) | needs a side door, sideways change or roller pack |
| [[Charge Battery from Standard Power Outlet]] | [[Battery Onboard Charger]] | analyst inference (necessity) | needs a built-in charger |
| [[Steer with Electric Power Assist]] | [[Electric Power Steering]] | analyst inference (necessity) | is the mechanism |
| [[Cut Power in an Emergency]] | [[Emergency Cut-Off Switch]] | analyst inference (necessity) | needs a cut-off switch |
| [[Program Travel, Lift and Tilt Speeds]] | [[Programmable Motor Controller]] | analyst inference (necessity) | needs a programmable controller |
| [[Display Truck Status to Operator]] | [[Display Device Design]] | analyst inference (necessity) | needs a display |
| [[Reduce Speed When Seat Belt Is Unfastened]] | [[Seat Belt Interlock]] | analyst inference (necessity) | needs a belt interlock |
| [[Cut Lift at Programmed Height]] | [[Mast Lift Limit Switch]] | analyst inference (necessity) | needs a limit switch |
**Withdrawn in round 27 (a source shows another mechanism)**

| Function | Design it was linked to | Why withdrawn |
|---|---|---|
| [[Hold Truck on Slope]] | [[Electric Parking Brake]] | Crown FC 5700 achieves hill hold through drive control and Crown RC 5700 holds the truck on a grade by closed-loop traction control; neither names a parking brake as the mechanism |
| [[Damp Mast Oscillation]] | [[Electric Mast Thrust Drive]] | Doosan Bobcat's mast sway control stabilizes the mast by cutting speed, not with a thrust drive |
| [[Operate in Wet or Dusty Conditions]] | [[Ingress-Protected Drive Components]] | Raymond uses hot-dip galvanization and Crown RC uses corrosion conditioning, which are finishes, not sealed drive components |

**Check against product links (round 27, after the fixes)**

Each row is a dependency where at least one product that performs the function has no link to the design. A gap means the sources do not name the design, not that the dependency is false; the rows below were kept as they are by owner decision, except where noted.

| Function | Design | Performing products without the design | Disposition |
|---|---|---|---|
| [[Adapt Speed to Load and Lift Height]] | [[Vehicle State Sensing Design]] | 3 of 3 | kept |
| [[Alert Operator of Hazards]] | [[Warning and Display Device Design]] | 12 of 15 | kept |
| [[Alert on Abnormal Condition]] | [[Warning and Display Device Design]] | 11 of 19 | kept |
| [[Alert on Low Electrolyte Level]] | [[Capacitive Electrolyte Level Probe]] | 1 of 1 | kept (owner example); Crown Battery Acid Indicators are visual indicators without a named probe, flagged |
| [[Charge Under BMS Control]] | [[Integrated Battery Management System]] | 5 of 5 | kept; the function is performed by chargers and the design lives on the battery (cross-product) |
| [[Continue Charging Through Module Fault]] | [[Modular Power Modules]] | 2 of 5 | kept; module count not named in two sources |
| [[Control Operator Access]] | [[Operator Identification Design]] | 8 of 15 | kept |
| [[Detect Pedestrians and Objects Near Truck]] | [[Object and Proximity Sensing Design]] | 6 of 24 | kept |
| [[Detect and Record Impacts]] | [[Impact Sensor]] | 5 of 10 | kept; the sensor is not named by sources |
| [[Display Battery Status to Operator]] | [[Display Device Design]] | 1 of 3 | kept |
| [[Enforce Pre-Shift Checklist]] | [[Display Device Design]] | 5 of 6 | kept |
| [[Indicate Battery Status Locally]] | [[Warning and Display Device Design]] | 3 of 18 | kept |
| [[Log Battery Events and Usage]] | [[Non-Volatile Event Memory]] | 21 of 25 | kept; event memory is not named by sources |
| [[Measure Battery Current]] | [[Current Sensing Design]] | 9 of 15 | kept |
| [[Program Travel, Lift and Tilt Speeds]] | [[Programmable Motor Controller]] | 3 of 5 | Crown FC 5700 link added in round 27; Crown RC and Linde name modes or electronic control, not a programmable controller; kept |
| [[Report Truck Telemetry]] | [[Wireless Interface Design]] | 18 of 18 | kept |
| [[Restrict Lift When Load Exceeds Limit]] | [[Vehicle State Sensing Design]] | 3 of 3 | kept |
| [[Sense Electrolyte Level]] | [[Capacitive Electrolyte Level Probe]] | 26 of 28 | kept; sources rarely name the sensing method (owner example was a level sensor, not one probe type); decision pending |
| [[Sense Load Weight and Lift Height]] | [[Vehicle State Sensing Design]] | 6 of 7 | kept |
| [[Show Camera View to Operator]] | [[Display Device Design]] | 7 of 8 | kept |
| [[Stop Vehicle When Operator Is Out of Position]] | [[Operator Presence Sensing Design]] | 10 of 12 | kept |
| [[Transmit Battery Data Wirelessly]] | [[Wireless Interface Design]] | 6 of 22 | kept |
| [[Upload Battery Data to Cloud Portal]] | [[Wireless Interface Design]] | 3 of 18 | kept; portal integration is not named by sources |
| [[Upload Battery Data to Cloud Portal]] | [[Cloud Portal Integration]] | 10 of 18 | kept; portal integration is not named by sources |
| [[Warn Pedestrians of Approaching Truck]] | [[Indicator and Alarm Design]] | 4 of 16 | kept |

## Aliases

- Function dependencies

## Former ids
