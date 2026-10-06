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
- **Strength (round 28):** strong = the function cannot work without the design or a design in the class, whatever the implementation; typical = the common implementation found, others possible; weak = broad class target because implementations are unknown. **Gap handling** records why a performing product lacks the design link.
- **Basis:** 'owner-stated example' is the owner's wording; 'analyst inference (necessity)' is engineering logic that the function cannot work without that kind of design. Neither is a vendor claim; the vendor evidence for each product is on the product notes.
- **Not written (no design note yet):** managing temperature during fast charging, recording images of load handling and illuminating the work area (2026-10-04); stop on operator out of position for seat switches, charging wirelessly. Battery voltage, battery temperature, and state-of-charge estimation now have reusable Design families.

| Function | Design or class | Basis | Strength | Gap handling | Why |
|---|---|---|---|---|---|
| [[Display Battery Status to Operator]] | [[Vehicle Operator Display Design]] | owner-stated example + implementation review | strong | some products identify touchscreen, multifunction display, or factory BDI while others do not publish the data transport | displaying battery state to the operator needs a vehicle-side display implementation; verified paths now include BLE-fed touchscreen, CAN-fed BDI, multifunction display, and integrated truck touchscreen |
| [[Alert on Low Electrolyte Level]] | [[Electrolyte Level Sensing Design]], [[Low Electrolyte Alert Design]] | owner-stated example + implementation review | strong | products may alert locally or communicate watering need; internal decision logic is usually unpublished | a low-water alert needs both an electrolyte-level sensing implementation and an alert-delivery implementation |
| [[Sense Electrolyte Level]] | [[Electrolyte Level Sensing Design]] | analyst inference (necessity) | strong | many products state level sensing without publishing the physical principle | needs an electrolyte-level sensing implementation; verified implementations now include capacitive, electronic in-cell, variable-length probe, cell-connector, and low-current input approaches |
| [[Indicate Battery Status Locally]] | [[Warning and Display Device Design]] | analyst inference (necessity) | strong | some products identify LED, LCD or gauge implementations while others state only an indication | needs a local indicator or display; verified implementations include LED elements, integrated LCDs and a technology-neutral battery gauge |
| [[Alert on Abnormal Condition]] | [[Abnormal Condition Alert Design]] | implementation review | strong | alert delivery varies across local device, operator dashboard and remote/cloud notification; internal evaluation logic is usually unpublished | needs abnormal-condition evaluation plus an alert-delivery path |
| [[Alert Operator of Hazards]] | [[Warning and Display Device Design]] | analyst inference (necessity) | strong | sources do not name the device | needs a light, sound or display |
| [[Warn Pedestrians of Approaching Truck]] | [[Indicator and Alarm Design]] | analyst inference (necessity) | strong | sources name the light or alarm product but not its indicator design | needs a light, sound or wearable |
| [[Indicate Aircraft Proximity to Operator]] | [[Aircraft Proximity Indicator Light]] | analyst inference (necessity) | typical | no gap | only implementation found |
| [[Show Camera View to Operator]] | [[Display Device Design]] | analyst inference (necessity) | strong | sources name the camera option but not the display | needs a display |
| [[Measure Battery Current]] | [[Current Sensing Design]] | analyst inference (necessity) | strong | sources do not name the sensing method | needs a current sensing method |
| [[Detect Voltage Imbalance]] | [[Voltage Imbalance Detection Design]] | implementation review | strong | Wi-iQ and EasyMonitor establish midpoint/symmetry sensing; Hyster verifies imbalance detection but does not publish the sensing or evaluation mechanism | needs a voltage-comparison input plus evaluation logic/circuitry; verified physical path is midpoint voltage symmetry detection |
| [[Measure Battery Temperature]] | [[Battery Temperature Measurement Design]] | analyst inference (necessity) | strong | many products state temperature measurement without naming sensor technology or locus | needs a temperature sensing implementation; known implementations now include immersed, external thermistor, internal, ambient, cell-connector, and BMS-internal sensing |
| [[Detect Pedestrians and Objects Near Truck]] | [[Object and Proximity Sensing Design]] | analyst inference (necessity) | strong | sources do not name the sensing element | needs a sensing technology |
| [[Slow and Stop Near Aircraft]] | [[Object and Proximity Sensing Design]] | analyst inference (necessity) | strong | no gap | needs distance sensing |
| [[Detect and Record Impacts]] | [[Impact Sensor]] | analyst inference (necessity) | strong | sources do not name the sensor | needs an impact sensor |
| [[Control Operator Access]] | [[Operator Identification Design]] | analyst inference (necessity) | strong | sources do not name the reader | needs a way to identify the operator |
| [[Stop Vehicle When Operator Is Out of Position]] | [[Operator Presence Sensing Design]] | analyst inference (necessity) | strong | sources name the presence system or seat-leave protection but not the sensing method | needs a way to sense the operator |
| [[Sense Load Weight and Lift Height]] | [[Vehicle State Sensing Design]] | analyst inference (necessity) | strong | sources do not name the sensing | needs a load or height sensor |
| [[Restrict Lift When Load Exceeds Limit]] | [[Vehicle State Sensing Design]] | analyst inference (necessity) | strong | sources do not name the sensing | needs a load sensor |
| [[Recover Energy by Regeneration]] | [[Regenerative Braking]] | analyst inference (necessity) | strong | no gap | is the design |
| [[Refuel Truck Power Source in Minutes]] | [[Hydrogen Storage Tank]] | analyst inference (necessity) | strong | no gap | needs on-truck fuel storage (fuel cell trucks) |
| [[Circulate Electrolyte]] | [[Forced Electrolyte Circulation]] | analyst inference (necessity) | strong | no gap | is the mechanism |
| [[Log Battery Events and Usage]] | [[Data Handling Design]] | analyst inference (necessity) | strong | sources do not name the storage | needs storage that survives power loss; retargeted to the design class in round 28 because sources name different or no implementations |
| [[Continue Charging Through Module Fault]] | [[Modular Power Modules]] | analyst inference (necessity) | typical | module count not named in two sources | needs a modular power stage |
| [[Charge Under BMS Control]] | [[Integrated Battery Management System]] | analyst inference (necessity) | strong | cross-product: chargers perform the function and the design lives on the battery | needs a BMS |
| [[Communicate Battery State over CAN]] | [[CAN Interface]] | analyst inference (necessity) | strong | no gap | needs a CAN interface |
| [[Command Vehicle Operating Limits over CAN]] | [[CAN Interface]] | analyst inference (necessity) | strong | no gap | needs a CAN interface |
| [[Transmit Battery Data Wirelessly]] | [[Wireless Interface Design]] | analyst inference (necessity) | strong | sources do not name the radio | needs a radio interface |
| [[Upload Battery Data to Cloud Portal]] | [[Wireless Interface Design]], [[Cloud Portal Integration]] | analyst inference (necessity) | typical | sources do not name the portal integration | needs a radio path and a portal |
| [[Report Truck Telemetry]] | [[Wireless Interface Design]] | analyst inference (necessity) | typical | sources do not name the interface | needs a radio path to the portal |
| [[Diagnose Vehicle Remotely]] | [[Wireless Interface Design]] | analyst inference (necessity) | typical | TUG Endurance names Bluetooth; TUG ALPHA 1 does not name the link | remote diagnostics need a radio or portal path to the technician (added round 40) |
| [[Follow Operator Automatically]] | [[Belt-Worn Remote Control]] | analyst inference (necessity) | typical | no gap | the operator's signal comes from a worn remote (easyPILOT) |
| [[Adapt Speed to Load and Lift Height]] | [[Vehicle State Sensing Design]] | analyst inference (necessity) | strong | sources do not name the sensing | needs the load and height measured |
| [[Enforce Pre-Shift Checklist]] | [[Display Device Design]] | analyst inference (necessity) | strong | sources do not name the display | the checklist is shown on a display (keypad or touch) |
| [[Change Battery Quickly]] | [[Quick-Change Battery Compartment]] | analyst inference (necessity) | strong | no gap | needs a side door, sideways change or roller pack |
| [[Charge Battery from Standard Power Outlet]] | [[Battery Onboard Charger]] | analyst inference (necessity) | strong | no gap | needs a built-in charger |
| [[Steer with Electric Power Assist]] | [[Electric Power Steering]] | analyst inference (necessity) | strong | no gap | is the mechanism |
| [[Cut Power in an Emergency]] | [[Emergency Cut-Off Switch]] | analyst inference (necessity) | strong | no gap | needs a cut-off switch |
| [[Program Travel, Lift and Tilt Speeds]] | [[Programmable Motor Controller]] | analyst inference (necessity) | typical | sources name modes or electronic control, not a programmable controller | needs a programmable controller |
| [[Display Truck Status to Operator]] | [[Vehicle Operator Display Design]] | analyst inference (necessity) | strong | no gap | needs a display |
| [[Reduce Speed When Seat Belt Is Unfastened]] | [[Seat Belt Interlock]] | analyst inference (necessity) | strong | no gap | needs a belt interlock |
| [[Cut Lift at Programmed Height]] | [[Mast Lift Limit Switch]] | analyst inference (necessity) | strong | no gap | needs a limit switch |
**Withdrawn in round 27 (a source shows another mechanism)**

| Function | Design it was linked to | Why withdrawn |
|---|---|---|
| [[Hold Truck on Slope]] | [[Electric Parking Brake]] | Crown FC 5700 achieves hill hold through drive control and Crown RC 5700 holds the truck on a grade by closed-loop traction control; neither names a parking brake as the mechanism |
| [[Damp Mast Oscillation]] | [[Electric Mast Thrust Drive]] | Doosan Bobcat's mast sway control stabilizes the mast by cutting speed, not with a thrust drive |
| [[Operate in Wet or Dusty Conditions]] | [[Ingress-Protected Drive Components]] | Raymond uses hot-dip galvanization and Crown RC uses corrosion conditioning, which are finishes, not sealed drive components |

**Check against product links (regenerated in round 28)**

Each row is a dependency where at least one product that performs the function has no link to the design or to a design under the class. A gap means the sources do not name the design, not that the dependency is false. Run `99_System/check-dependencies.py` to regenerate this view; add `--strict` to fail when a strong row has an unreviewed gap.

| Function | Design or class | Strength | Performing products without it | Gap handling |
|---|---|---|---|---|
| [[Adapt Speed to Load and Lift Height]] | [[Vehicle State Sensing Design]] | strong | 3 of 3 | sources do not name the sensing |
| [[Alert Operator of Hazards]] | [[Warning and Display Device Design]] | strong | 12 of 15 | sources do not name the device |
| [[Alert on Abnormal Condition]] | [[Warning and Display Device Design]] | strong | 11 of 19 | sources do not name the device |
| [[Alert on Low Electrolyte Level]] | [[Electrolyte Level Sensing Design]] | strong | products without a concrete child Design remain intentionally on the general family | sources often identify the alert but not the sensor implementation |
| [[Charge Under BMS Control]] | [[Integrated Battery Management System]] | strong | 5 of 5 | cross-product: chargers perform the function and the design lives on the battery |
| [[Continue Charging Through Module Fault]] | [[Modular Power Modules]] | typical | 2 of 5 | module count not named in two sources |
| [[Control Operator Access]] | [[Operator Identification Design]] | strong | 8 of 15 | sources do not name the reader |
| [[Detect Pedestrians and Objects Near Truck]] | [[Object and Proximity Sensing Design]] | strong | 6 of 24 | sources do not name the sensing element |
| [[Detect and Record Impacts]] | [[Impact Sensor]] | strong | 5 of 10 | sources do not name the sensor |
| [[Display Battery Status to Operator]] | [[Display Device Design]] | strong | 1 of 3 | sources do not name the display |
| [[Enforce Pre-Shift Checklist]] | [[Display Device Design]] | strong | 5 of 6 | sources do not name the display |
| [[Indicate Battery Status Locally]] | [[Warning and Display Device Design]] | strong | 3 of 18 | sources do not name the indicator |
| [[Log Battery Events and Usage]] | [[Data Handling Design]] | strong | 16 of 25 | sources do not name the storage |
| [[Measure Battery Current]] | [[Current Sensing Design]] | strong | 9 of 15 | sources do not name the sensing method |
| [[Measure Battery Temperature]] | [[Battery Temperature Measurement Design]] | strong | performing products without a concrete child Design remain intentionally on the general family | sources often name temperature behavior but not sensor technology or placement |
| [[Program Travel, Lift and Tilt Speeds]] | [[Programmable Motor Controller]] | typical | 3 of 5 | sources name modes or electronic control, not a programmable controller |
| [[Report Truck Telemetry]] | [[Wireless Interface Design]] | typical | 18 of 18 | sources do not name the interface |
| [[Diagnose Vehicle Remotely]] | [[Wireless Interface Design]] | typical | 1 of 2 | TUG ALPHA 1 does not name the interface; TUG Endurance links Bluetooth Interface |
| [[Restrict Lift When Load Exceeds Limit]] | [[Vehicle State Sensing Design]] | strong | 3 of 3 | sources do not name the sensing |
| [[Sense Electrolyte Level]] | [[Electrolyte Level Sensing Design]] | strong | performing products without a concrete child Design remain intentionally on the general family | sources often identify electrolyte monitoring without publishing the sensing principle |
| [[Sense Load Weight and Lift Height]] | [[Vehicle State Sensing Design]] | strong | 6 of 7 | sources do not name the sensing |
| [[Show Camera View to Operator]] | [[Display Device Design]] | strong | 7 of 8 | sources name the camera option but not the display |
| [[Stop Vehicle When Operator Is Out of Position]] | [[Operator Presence Sensing Design]] | strong | 10 of 12 | sources name the presence system or seat-leave protection but not the sensing method |
| [[Transmit Battery Data Wirelessly]] | [[Wireless Interface Design]] | strong | 6 of 22 | sources do not name the radio |
| [[Upload Battery Data to Cloud Portal]] | [[Wireless Interface Design]] | typical | 3 of 18 | sources do not name the portal integration |
| [[Upload Battery Data to Cloud Portal]] | [[Cloud Portal Integration]] | typical | 10 of 18 | sources do not name the portal integration |
| [[Warn Pedestrians of Approaching Truck]] | [[Indicator and Alarm Design]] | strong | 4 of 16 | sources name the light or alarm product but not its indicator design |
| [[Control Charger from Remote Panel]] | [[Charger Operator Interface Design]] | analyst inference (necessity) | weak | source names a wired remote with status display; no specific remote-panel design note | needs a way to show charger status and take input away from the charger; one implementation known (wired remote), so the class is used until a design note exists (added 2026-10-04) |
| [[Indicate Charger Status Locally]] | [[Local Charger Status Indication]] | analyst inference (necessity) | strong | integrated LED bars and remote stack/tower lights are both verified | needs a local charger-status output; implementations differ in integrated versus remote physical arrangement |
| [[Stop Truck for Detected Obstacle]] | [[Object and Proximity Sensing Design]] | analyst inference (necessity) | strong | sources name LiDAR (Raymond), camera (TLD) or do not name the sensor (Linde) | cannot stop for an obstacle without sensing it; implementations differ, so the class is used (added 2026-10-04) |
| [[Inhibit Drive Until Equipment Is Stowed]] | [[Vehicle State Sensing Design]] | analyst inference (necessity) | weak | source names the interlock, not the position sensor | needs to sense that the handrail or platform is stowed; one implementation known (added 2026-10-04) |
| [[Predict Battery Replacement Timing]] | [[Data Handling Design]] | analyst inference (necessity) | typical | sources name portals or software (PosiNet, withBMS platform, batterymanagement.net, PowerTrac software) but not the storage design | a prediction needs stored usage history; known implementations hold it in a portal or software (added 2026-10-04) |
| [[Adapt Truck to Battery Chemistry]] | [[Vehicle Energy Interface Design]] | analyst inference (necessity) | weak | Hyster names the factory Battery Discharge Indicator and modes, not the interface design | the truck must take the battery's chemistry into its energy interface; only one implementation known (added 2026-10-04) |
| [[Lock Out Vehicle After Impact]] | [[Impact Sensor]] | analyst inference (necessity) | strong | TLD says impact strength is measured; sensor type not named | a lockout after impact needs an impact to be sensed; only one implementation known, so the specific design is used (generalize when a second appears) (added 2026-10-04) |

## Aliases

- Function dependencies

## Former ids
