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
- **Not written (no design note yet):** managing temperature during fast charging, recording images of load handling and illuminating the work area (2026-10-04); stop on operator out of position for seat switches, charging wirelessly. Battery voltage, battery temperature, state-of-charge estimation, and cell-failure diagnosis now have reusable Design families.

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
| [[Measure Electrolyte Specific Gravity]] | [[In-Cell Specific Gravity Probe]] | one verified implementation | typical | only TruBID is currently documented; probe placement is known but transduction principle is not | current implementation requires an in-cell probe; generalize under a dedicated specific-gravity sensing family if a second materially different implementation appears |
| [[Detect Battery Weight]] | [[Battery Weight Determination Design]] | implementation review | strong | Raymond verifies stored specification lookup over power-line communication; direct load-cell measurement remains an unallocated engineering alternative | determining battery weight/compatibility requires one member of the weight-determination design family; the verified Raymond path uses stored battery specification data rather than physical weighing |
| [[Calculate Battery Abuse Cycles]] | [[Battery Abuse Cycle Analytics]] | implementation review | strong | products publish abuse-cycle or abuse-analytics results but do not establish whether computation is device-resident or cloud-based | calculating abuse cycles requires an analytics method over battery-use/misuse history; device firmware and cloud service are retained as concrete unallocated alternatives |
| [[Detect Cell Failure]] | [[Cell Failure Diagnostic Design]] | implementation review | strong | TruBID verifies cell-failure detection / cell-fail alert but does not publish the diagnostic locus or causal input | requires some diagnostic method; TruBID remains on the generic family while algorithmic firmware and dedicated threshold circuitry are retained as unallocated alternatives |
| [[Detect Voltage Imbalance]] | [[Voltage Imbalance Detection Design]] | implementation review | strong | Wi-iQ and EasyMonitor establish midpoint/symmetry sensing; Hyster verifies imbalance detection but does not publish the sensing or evaluation mechanism | needs a voltage-comparison input plus evaluation logic/circuitry; verified physical path is midpoint voltage symmetry detection |
| [[Estimate State of Health]] | [[Usage-History State of Health Analytics]] | implementation review | typical | Raymond publishes the SOH dashboard and contributing history/factors but not its formula; Inventus SBM-01 displays battery-supplied SOH rather than estimating it | current product-backed implementation is multi-factor usage-history analytics; capacity-retention and resistance-trend estimators remain unallocated implementation options |
| [[Estimate State of Charge]] | [[State of Charge Estimation Design]] | implementation review | strong | Truck iQ and SBM-01 are display endpoints; battery-side estimators do not publish the exact algorithm | requires a battery-side SOC estimation implementation; product-backed loci are battery-monitor estimation and integrated-BMS estimation, while algorithm choices remain candidate firmware |
| [[Estimate Remaining Run Time]] | [[Report Battery Temperature to Charger]] | [[Battery Temperature Reporting to Charger]] | implementation review | strong | products explicitly provide battery temperature to compatible chargers; sensing location and communication transport vary | requires both [[Battery Temperature Measurement Design]] and [[Battery-Charger Data Communication Design]]; sensor alone is not sufficient |
| [[Remaining Runtime Estimation Design]] | implementation review | strong | HOPPECKE publishes remaining-driving-time data and Linde explicitly says its energy-management system calculates projected remaining operating time; Truck iQ and SBM-01 only display received runtime information | requires software that relates available battery energy/state to operating demand; exact algorithms remain unpublished |
| [[Accumulate Amp-Hours]] | [[Current Integration Amp-Hour Accumulation]] | implementation review | strong | strong examples combine explicit current measurement with Ah in/out, used, throughput, or lifetime totals; Crown BHM and Site Probe do not publish the calculation locus | amp-hours are accumulated by integrating battery current over elapsed time; lifetime counters may additionally require persistent storage |
| [[Measure Battery Temperature]] | [[Battery Temperature Measurement Design]] | analyst inference (necessity) | strong | many products state temperature measurement without naming sensor technology or locus | needs a temperature sensing implementation; known implementations now include immersed, external thermistor, internal, ambient, cell-connector, and BMS-internal sensing |
| [[Detect Pedestrians and Objects Near Truck]] | [[Object and Proximity Sensing Design]] | analyst inference (necessity) | strong | sources do not name the sensing element | needs a sensing technology |
| [[Slow and Stop Near Aircraft]] | [[Object and Proximity Sensing Design]] | analyst inference (necessity) | strong | no gap | needs distance sensing |
| [[Detect and Record Impacts]] | [[Impact Sensor]] | analyst inference (necessity) | strong | sources do not name the sensor | needs an impact sensor |
| [[Control Operator Access]] | [[Operator Access Authorization Design]] | implementation review | strong | products explicitly restrict operation to authorized users using PIN, fingerprint, RFID or fleet-managed credentials | requires operator identification plus authorization logic and a vehicle enable/inhibit mechanism |
| [[Stop Vehicle When Operator Is Out of Position]] | [[Operator Presence Sensing Design]] | analyst inference (necessity) | strong | sources name the presence system or seat-leave protection but not the sensing method | needs a way to sense the operator |
| [[Sense Load Weight and Lift Height]] | [[Vehicle State Sensing Design]] | analyst inference (necessity) | strong | sources do not name the sensing | needs a load or height sensor |
| [[Restrict Lift When Load Exceeds Limit]] | [[Vehicle State Sensing Design]] | analyst inference (necessity) | strong | sources do not name the sensing | needs a load sensor |
| [[Recover Energy by Regeneration]] | [[Regenerative Braking]] | analyst inference (necessity) | strong | no gap | is the design |
| [[Refuel Truck Power Source in Minutes]] | [[Hydrogen Storage Tank]] | analyst inference (necessity) | strong | no gap | needs on-truck fuel storage (fuel cell trucks) |
| [[Circulate Electrolyte]] | [[Air Injection Electrolyte Circulation]] | implementation review | strong | current products identify air agitation/circulation; Midac explicitly identifies charger-mounted pump and in-cell tubes, HAWKER an air pump, HOPPECKE air delivered into each cell | requires an air source and cell distribution path; exact pump/control topology remains product-specific |
| [[Log Battery Events and Usage]] | [[Battery Event and Usage Logging Design]] | implementation review | strong | products publish retained event/history records; PowerTrac 3, HOPPECKE trak collect, and Wi-iQ explicitly support persistent event logs and timekeeping | requires event-recognition/record-generation logic plus persistent storage and a time/sequence source |
| [[Continue Charging Through Module Fault]] | [[Modular Power Modules]] | analyst inference (necessity) | typical | module count not named in two sources | needs a modular power stage |
| [[Charge Under BMS Control]] | [[Integrated Battery Management System]] | analyst inference (necessity) | strong | cross-product: chargers perform the function and the design lives on the battery | needs a BMS |
| [[Export Battery Data to PC]] | [[PC Battery Data Export Design]] | implementation review | strong | eGO!Mini, PowerTrac DT3 and PowerTrac SP+ explicitly support technician/PC data extraction through USB, wireless, infrared or serial paths | requires export/serialization behavior plus a selected local transfer interface; logging remains a separate prerequisite behavior |
| [[Configure Device from Mobile App or PC]] | [[Device Configuration and Service Design]] | implementation review | strong | products explicitly support mobile, tablet, laptop or PC configuration/service access | requires technician-facing software plus device-side service behavior and a selected local communication interface |
| [[Communicate with Charger]] | [[Battery-Charger Data Communication Design]] | implementation review | strong | multiple products explicitly exchange data with compatible chargers over PLC, CAN, wired or wireless links; message content and direction vary | requires application/session behavior plus a selected communication interface; identity exchange is a specialized child design |
| [[Communicate Battery State over CAN]] | [[CAN Battery State Communication Design]] | implementation review | strong | products explicitly exchange battery state over CAN; protocols vary and message maps are usually unpublished | requires application-layer CAN message handling plus [[CAN Interface]] transport |
| [[Command Vehicle Operating Limits over CAN]] | [[CAN Vehicle Operating Limit Command]] | implementation review | strong | Wi-iQ explicitly supports OEM-specific vehicle operating-limit communication over optional CAN; internal firmware/message implementation is not published | command behavior requires control/message logic plus [[CAN Interface]] transport |
| [[Track Equalization]] | [[Equalization Event Tracking Design]] | implementation review | strong | products publish equalization status/history but usually do not disclose whether the event is inferred locally or reported by another system | requires an equalization-event recognition/recording method; local classification and reported-status tracking remain concrete unallocated alternatives |
| [[Transmit Battery Data Wirelessly]] | [[Wireless Battery Data Communication Design]] | analyst inference (necessity) | strong | sources do not name the radio | needs a radio interface |
| [[Upload Battery Data to Cloud Portal]] | [[Cloud Battery Data Upload Design]] | implementation review | strong | products publish hosted portal upload/reporting; eGO!gateway explicitly proves a local-gateway-to-cellular-cloud path | requires field upload/ingestion behavior plus [[Cloud Portal Integration]]; direct and gateway-mediated paths remain distinct |
| [[Report Truck Telemetry]] | [[Wireless Interface Design]] | analyst inference (necessity) | typical | sources do not name the interface | needs a radio path to the portal |
| [[Diagnose Vehicle Remotely]] | [[Wireless Interface Design]] | analyst inference (necessity) | typical | TUG Endurance names Bluetooth; TUG ALPHA 1 does not name the link | remote diagnostics need a radio or portal path to the technician (added round 40) |
| [[Follow Operator Automatically]] | [[Belt-Worn Remote Control]] | analyst inference (necessity) | typical | no gap | the operator's signal comes from a worn remote (easyPILOT) |
| [[Adapt Speed to Load and Lift Height]] | [[Vehicle State Sensing Design]] | analyst inference (necessity) | strong | sources do not name the sensing | needs the load and height measured |
| [[Enforce Pre-Shift Checklist]] | [[Pre-Shift Checklist Enforcement Design]] | implementation review | strong | products publish electronic inspection checklists tied to vehicle authorization/lockout; exact software and interlock partition varies | requires operator display/input, checklist validation logic, and an inhibit/release path such as [[Vehicle Enable Interlock]] |
| [[Change Battery Quickly]] | [[Quick-Change Battery Compartment]] | analyst inference (necessity) | strong | no gap | needs a side door, sideways change or roller pack |
| [[Charge Battery from Standard Power Outlet]] | [[Battery Onboard Charger]] | analyst inference (necessity) | strong | no gap | needs a built-in charger |
| [[Steer with Electric Power Assist]] | [[Electric Power Steering]] | analyst inference (necessity) | strong | no gap | is the mechanism |
| [[Cut Power in an Emergency]] | [[Emergency Cut-Off Switch]] | analyst inference (necessity) | strong | no gap | needs a cut-off switch |
| [[Protect Battery from Deep Discharge]] | [[Deep Discharge Protection Design]] | implementation review | strong | current evidence shows battery-resident BMS limitation, truck-side BDI interlock, and CAN-coordinated shutdown as distinct implementations | requires an enforcement method that limits or stops operation at protected discharge state; child Designs preserve the different loci |
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
| [[Control Operator Access]] | [[Operator Access Authorization Design]] | strong | 8 of 15 | credential mechanism varies; authorization/interlock implementation often unpublished |
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
| [[Predict Battery Replacement Timing]] | [[Battery Replacement Timing Prediction Design]] | implementation review | strong | products publish replacement/life-expectancy prediction but usually do not disclose the execution locus or forecast model; Energywith explicitly places degradation/replacement analysis in its service platform | requires a replacement-forecasting method over degradation/usage history; device-resident and fleet-service paths are modeled separately |
| [[Adapt Truck to Battery Chemistry]] | [[Vehicle Energy Interface Design]] | analyst inference (necessity) | weak | Hyster names the factory Battery Discharge Indicator and modes, not the interface design | the truck must take the battery's chemistry into its energy interface; only one implementation known (added 2026-10-04) |
| [[Lock Out Vehicle After Impact]] | [[Impact Sensor]] | analyst inference (necessity) | strong | TLD says impact strength is measured; sensor type not named | a lockout after impact needs an impact to be sensed; only one implementation known, so the specific design is used (generalize when a second appears) (added 2026-10-04) |

## Aliases

- Function dependencies

## Former ids

| [[Water Battery Cells]] | [[Battery Cell Watering Design]] | implementation review | strong | current products show float-valve single-point, injector level-sensing, charger-controlled automatic, and generic automatic watering variants | requires a controlled water-distribution/fill method; child Designs preserve distinct shutoff and control architectures |
