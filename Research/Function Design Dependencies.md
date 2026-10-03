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
| [[Damp Mast Oscillation]] | [[Electric Mast Thrust Drive]] | analyst inference (necessity) | the only implementation found uses an electric thrust drive |
| [[Follow Operator Automatically]] | [[Belt-Worn Remote Control]] | analyst inference (necessity) | the operator's signal comes from a worn remote (easyPILOT) |
| [[Adapt Speed to Load and Lift Height]] | [[Vehicle State Sensing Design]] | analyst inference (necessity) | needs the load and height measured |
| [[Enforce Pre-Shift Checklist]] | [[Display Device Design]] | analyst inference (necessity) | the checklist is shown on a display (keypad or touch) |

## Aliases

- Function dependencies

## Former ids
