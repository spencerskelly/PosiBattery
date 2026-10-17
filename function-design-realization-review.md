# Function-to-Design Realization Review

Step 16 whole-vault review of direct Function→Design implementation and enabling Function→Design dependencies.

## Summary

| Metric | Count |
|---|---:|
| bmid_approved_design_dependencies | 4 |
| bmid_approved_direct_realizations | 5 |
| function_dependency_target_Document | 2 |
| function_dependency_target_Object | 2 |
| function_to_design_dependency_assertions | 92 |
| function_to_design_realization_assertions | 48 |
| functions | 159 |
| functions_with_design_dependency | 76 |
| functions_with_design_realization | 47 |
| findings | 0 |

## Direct realizations

| Function | Design |
|---|---|
| 30_Product Capabilities/Product Functions/Accumulate Amp-Hours.md | 30_Product Capabilities/Product Designs/Current Integration Amp-Hour Accumulation.md |
| 30_Product Capabilities/Product Functions/Adapt Charge to Battery Condition.md | 30_Product Capabilities/Product Designs/Adaptive Charge Profile Control Design.md |
| 30_Product Capabilities/Product Functions/Alert on Abnormal Condition.md | 30_Product Capabilities/Product Designs/Abnormal Condition Alert Design.md |
| 30_Product Capabilities/Product Functions/Alert on Low Electrolyte Level.md | 30_Product Capabilities/Product Designs/Low Electrolyte Alert Design.md |
| 30_Product Capabilities/Product Functions/Calculate Battery Abuse Cycles.md | 30_Product Capabilities/Product Designs/Battery Abuse Cycle Analytics.md |
| 30_Product Capabilities/Product Functions/Charge Under BMS Control.md | 30_Product Capabilities/Product Designs/BMS-Directed Charge Control Design.md |
| 30_Product Capabilities/Product Functions/Circulate Electrolyte.md | 30_Product Capabilities/Product Designs/Air Injection Electrolyte Circulation.md |
| 30_Product Capabilities/Product Functions/Circulate Electrolyte.md | 30_Product Capabilities/Product Designs/Forced Electrolyte Circulation.md |
| 30_Product Capabilities/Product Functions/Command Vehicle Operating Limits over CAN.md | 30_Product Capabilities/Product Designs/CAN Vehicle Operating Limit Command.md |
| 30_Product Capabilities/Product Functions/Communicate Battery State over CAN.md | 30_Product Capabilities/Product Designs/CAN Battery State Communication Design.md |
| 30_Product Capabilities/Product Functions/Communicate with Charger.md | 30_Product Capabilities/Product Designs/Battery-Charger Data Communication Design.md |
| 30_Product Capabilities/Product Functions/Compensate Charge for Battery Temperature.md | 30_Product Capabilities/Product Designs/Temperature-Compensated Charge Control Design.md |
| 30_Product Capabilities/Product Functions/Complete Missed Equalization Automatically.md | 30_Product Capabilities/Product Designs/Missed Equalization Recovery Design.md |
| 30_Product Capabilities/Product Functions/Configure Device from Mobile App or PC.md | 30_Product Capabilities/Product Designs/Device Configuration and Service Design.md |
| 30_Product Capabilities/Product Functions/Control Charger from Remote Panel.md | 30_Product Capabilities/Product Designs/Wired Remote Charger Control Design.md |
| 30_Product Capabilities/Product Functions/Control Operator Access.md | 30_Product Capabilities/Product Designs/Operator Access Authorization Design.md |
| 30_Product Capabilities/Product Functions/Desulfate Battery During Charge.md | 30_Product Capabilities/Product Designs/Lead-Acid Desulfation Charge Control Design.md |
| 30_Product Capabilities/Product Functions/Detect Battery Weight.md | 30_Product Capabilities/Product Designs/Battery Weight Determination Design.md |
| 30_Product Capabilities/Product Functions/Detect Cell Failure.md | 30_Product Capabilities/Product Designs/Cell Failure Diagnostic Design.md |
| 30_Product Capabilities/Product Functions/Detect Voltage Imbalance.md | 30_Product Capabilities/Product Designs/Voltage Imbalance Detection Design.md |
| 30_Product Capabilities/Product Functions/Diagnose Vehicle Remotely.md | 30_Product Capabilities/Product Designs/Remote Vehicle Diagnostics Design.md |
| 30_Product Capabilities/Product Functions/Display Battery Status to Operator.md | 30_Product Capabilities/Product Designs/Vehicle Operator Display Design.md |
| 30_Product Capabilities/Product Functions/Display Truck Status to Operator.md | 30_Product Capabilities/Product Designs/Vehicle Operator Display Design.md |
| 30_Product Capabilities/Product Functions/Enforce Pre-Shift Checklist.md | 30_Product Capabilities/Product Designs/Pre-Shift Checklist Enforcement Design.md |
| 30_Product Capabilities/Product Functions/Estimate Remaining Run Time.md | 30_Product Capabilities/Product Designs/Remaining Runtime Estimation Design.md |
| 30_Product Capabilities/Product Functions/Estimate State of Charge.md | 30_Product Capabilities/Product Designs/State of Charge Estimation Design.md |
| 30_Product Capabilities/Product Functions/Estimate State of Health.md | 30_Product Capabilities/Product Designs/Usage-History State of Health Analytics.md |
| 30_Product Capabilities/Product Functions/Export Battery Data to PC.md | 30_Product Capabilities/Product Designs/PC Battery Data Export Design.md |
| 30_Product Capabilities/Product Functions/Identify Battery to Charger.md | 30_Product Capabilities/Product Designs/Battery Identification and Charger Communication Software Design.md |
| 30_Product Capabilities/Product Functions/Indicate Battery Status Locally.md | 30_Product Capabilities/Product Designs/Warning and Display Device Design.md |
| 30_Product Capabilities/Product Functions/Indicate Charger Status Locally.md | 30_Product Capabilities/Product Designs/Local Charger Status Indication.md |
| 30_Product Capabilities/Product Functions/Lock Out Vehicle After Impact.md | 30_Product Capabilities/Product Designs/Impact-Triggered Vehicle Lockout Design.md |
| 30_Product Capabilities/Product Functions/Log Battery Events and Usage.md | 30_Product Capabilities/Product Designs/Battery Event and Usage Logging Design.md |
| 30_Product Capabilities/Product Functions/Manage Chargers Remotely.md | 30_Product Capabilities/Product Designs/Remote Charger Management Design.md |
| 30_Product Capabilities/Product Functions/Measure Battery Current.md | 30_Product Capabilities/Product Designs/Current Sensing Design.md |
| 30_Product Capabilities/Product Functions/Measure Battery Temperature.md | 30_Product Capabilities/Product Designs/Battery Temperature Measurement Design.md |
| 30_Product Capabilities/Product Functions/Measure Battery Voltage.md | 30_Product Capabilities/Product Designs/Battery Voltage Measurement Design.md |
| 30_Product Capabilities/Product Functions/Measure Electrolyte Specific Gravity.md | 30_Product Capabilities/Product Designs/In-Cell Specific Gravity Probe.md |
| 30_Product Capabilities/Product Functions/Predict Battery Replacement Timing.md | 30_Product Capabilities/Product Designs/Battery Replacement Timing Prediction Design.md |
| 30_Product Capabilities/Product Functions/Protect Battery from Deep Discharge.md | 30_Product Capabilities/Product Designs/Deep Discharge Protection Design.md |
| 30_Product Capabilities/Product Functions/Record Images of Load Handling.md | 30_Product Capabilities/Product Designs/Load-Handling Image Capture Design.md |
| 30_Product Capabilities/Product Functions/Report Battery Temperature to Charger.md | 30_Product Capabilities/Product Designs/Battery Temperature Reporting to Charger.md |
| 30_Product Capabilities/Product Functions/Report Truck Telemetry.md | 30_Product Capabilities/Product Designs/Truck Telemetry Reporting Design.md |
| 30_Product Capabilities/Product Functions/Sense Electrolyte Level.md | 30_Product Capabilities/Product Designs/Electrolyte Level Sensing Design.md |
| 30_Product Capabilities/Product Functions/Track Equalization.md | 30_Product Capabilities/Product Designs/Equalization Event Tracking Design.md |
| 30_Product Capabilities/Product Functions/Transmit Battery Data Wirelessly.md | 30_Product Capabilities/Product Designs/Wireless Battery Data Communication Design.md |
| 30_Product Capabilities/Product Functions/Upload Battery Data to Cloud Portal.md | 30_Product Capabilities/Product Designs/Cloud Battery Data Upload Design.md |
| 30_Product Capabilities/Product Functions/Water Battery Cells.md | 30_Product Capabilities/Product Designs/Battery Cell Watering Design.md |

## Design dependencies

| Function | Design |
|---|---|
| 30_Product Capabilities/Product Functions/Adapt Speed to Load and Lift Height.md | 30_Product Capabilities/Product Designs/Vehicle State Sensing Design.md |
| 30_Product Capabilities/Product Functions/Adapt Truck to Battery Chemistry.md | 30_Product Capabilities/Product Designs/Vehicle Energy Interface Design.md |
| 30_Product Capabilities/Product Functions/Alert Operator of Hazards.md | 30_Product Capabilities/Product Designs/Warning and Display Device Design.md |
| 30_Product Capabilities/Product Functions/Alert on Low Electrolyte Level.md | 30_Product Capabilities/Product Designs/Electrolyte Level Sensing Design.md |
| 30_Product Capabilities/Product Functions/Assist Lift Positioning.md | 30_Product Capabilities/Product Designs/Fork Laser Guide.md |
| 30_Product Capabilities/Product Functions/Balance Cells.md | 30_Product Capabilities/Product Designs/Active Cell Balancing.md |
| 30_Product Capabilities/Product Functions/Balance Cells.md | 30_Product Capabilities/Product Designs/Passive Cell Balancing.md |
| 30_Product Capabilities/Product Functions/Balance Charging Power Across Site Capacity.md | 30_Product Capabilities/Product Designs/Site Power Load Management Design.md |
| 30_Product Capabilities/Product Functions/Change Battery Quickly.md | 30_Product Capabilities/Product Designs/Quick-Change Battery Compartment.md |
| 30_Product Capabilities/Product Functions/Charge Battery Conventionally.md | 30_Product Capabilities/Product Designs/Charger Power Stage Design.md |
| 30_Product Capabilities/Product Functions/Charge Battery Conventionally.md | 30_Product Capabilities/Product Designs/Charge Profile Control Design.md |
| 30_Product Capabilities/Product Functions/Charge Battery Fast.md | 30_Product Capabilities/Product Designs/Charger Power Stage Design.md |
| 30_Product Capabilities/Product Functions/Charge Battery Fast.md | 30_Product Capabilities/Product Designs/Charge Profile Control Design.md |
| 30_Product Capabilities/Product Functions/Charge Battery Fast.md | 30_Product Capabilities/Product Designs/Thin Plate Pure Lead Plates.md |
| 30_Product Capabilities/Product Functions/Charge Battery Fast.md | 30_Product Capabilities/Product Designs/Integrated Battery Management System.md |
| 30_Product Capabilities/Product Functions/Charge Battery Fast.md | 30_Product Capabilities/Product Designs/Heavy-Duty Intercell Connectors.md |
| 30_Product Capabilities/Product Functions/Charge Battery Fast.md | 30_Product Capabilities/Product Designs/Copper Inserted Posts.md |
| 30_Product Capabilities/Product Functions/Charge Battery Wirelessly.md | 30_Product Capabilities/Product Designs/Inductive Wireless Charging.md |
| 30_Product Capabilities/Product Functions/Charge Battery by Automatic Contact.md | 30_Product Capabilities/Product Designs/Conductive Auto-Contact Charging.md |
| 30_Product Capabilities/Product Functions/Charge Battery by Opportunity.md | 30_Product Capabilities/Product Designs/Charger Power Stage Design.md |
| 30_Product Capabilities/Product Functions/Charge Battery by Opportunity.md | 30_Product Capabilities/Product Designs/Charge Profile Control Design.md |
| 30_Product Capabilities/Product Functions/Charge Battery by Opportunity.md | 30_Product Capabilities/Product Designs/Thin Plate Pure Lead Plates.md |
| 30_Product Capabilities/Product Functions/Charge Battery by Opportunity.md | 30_Product Capabilities/Product Designs/Integrated Battery Management System.md |
| 30_Product Capabilities/Product Functions/Charge Battery from Standard Power Outlet.md | 30_Product Capabilities/Product Designs/Battery Onboard Charger.md |
| 30_Product Capabilities/Product Functions/Charge Lithium-Ion Battery.md | 30_Product Capabilities/Product Designs/Charger Power Stage Design.md |
| 30_Product Capabilities/Product Functions/Charge Lithium-Ion Battery.md | 30_Product Capabilities/Product Designs/Charge Profile Control Design.md |
| 30_Product Capabilities/Product Functions/Charge Under BMS Control.md | 30_Product Capabilities/Product Designs/Integrated Battery Management System.md |
| 30_Product Capabilities/Product Functions/Charge Wirelessly Despite Misalignment.md | 30_Product Capabilities/Product Designs/Inductive Wireless Charging.md |
| 30_Product Capabilities/Product Functions/Command Vehicle Operating Limits over CAN.md | 30_Product Capabilities/Product Designs/CAN Interface.md |
| 30_Product Capabilities/Product Functions/Communicate Battery State over CAN.md | 30_Product Capabilities/Product Designs/CAN Interface.md |
| 30_Product Capabilities/Product Functions/Connect Battery to Charger or Vehicle.md | 30_Product Capabilities/Product Designs/Manual Plug-In Charging.md |
| 30_Product Capabilities/Product Functions/Continue Charging Through Module Fault.md | 30_Product Capabilities/Product Designs/Modular Power Modules.md |
| 30_Product Capabilities/Product Functions/Control Charger from Remote Panel.md | 30_Product Capabilities/Product Designs/Charger Operator Interface Design.md |
| 30_Product Capabilities/Product Functions/Control Operator Access.md | 30_Product Capabilities/Product Designs/Operator Identification Design.md |
| 30_Product Capabilities/Product Functions/Cut Lift at Programmed Height.md | 30_Product Capabilities/Product Designs/Mast Lift Limit Switch.md |
| 30_Product Capabilities/Product Functions/Cut Power in an Emergency.md | 30_Product Capabilities/Product Designs/Emergency Cut-Off Switch.md |
| 30_Product Capabilities/Product Functions/Damp Mast Oscillation.md | 30_Product Capabilities/Product Designs/Electric Mast Thrust Drive.md |
| 30_Product Capabilities/Product Functions/Deliver Constant Power Through Shift.md | 30_Product Capabilities/Product Designs/Fuel Cell Hybrid Power Stage.md |
| 30_Product Capabilities/Product Functions/Detect Foreign and Live Objects.md | 30_Product Capabilities/Product Designs/Inductive Wireless Charging.md |
| 30_Product Capabilities/Product Functions/Detect Pedestrians and Objects Near Truck.md | 30_Product Capabilities/Product Designs/Object and Proximity Sensing Design.md |
| 30_Product Capabilities/Product Functions/Detect and Record Impacts.md | 30_Product Capabilities/Product Designs/Impact Sensor.md |
| 30_Product Capabilities/Product Functions/Diagnose Vehicle Remotely.md | 30_Product Capabilities/Product Designs/Wireless Interface Design.md |
| 30_Product Capabilities/Product Functions/Dispatch Vehicles to Tasks.md | 30_Product Capabilities/Product Designs/Vehicle Task Dispatch Design.md |
| 30_Product Capabilities/Product Functions/Enforce Pre-Shift Checklist.md | 30_Product Capabilities/Product Designs/Display Device Design.md |
| 30_Product Capabilities/Product Functions/Equalize Battery on Schedule.md | 30_Product Capabilities/Product Designs/Battery-Stored Equalization Schedule.md |
| 30_Product Capabilities/Product Functions/Exchange Battery Automatically.md | 30_Product Capabilities/Product Designs/Automated Battery Swap.md |
| 30_Product Capabilities/Product Functions/Exchange Charge Control Data Between Pads.md | 30_Product Capabilities/Product Designs/Inductive Wireless Charging.md |
| 30_Product Capabilities/Product Functions/Exchange Vehicle and Order Data with Warehouse System.md | 30_Product Capabilities/Product Designs/Warehouse System Data Interface Design.md |
| 30_Product Capabilities/Product Functions/Float Charge Battery.md | 30_Product Capabilities/Product Designs/Voltage-Triggered Ready-State Top-Up.md |
| 30_Product Capabilities/Product Functions/Follow Operator Automatically.md | 30_Product Capabilities/Product Designs/Belt-Worn Remote Control.md |
| 30_Product Capabilities/Product Functions/Follow Vehicle Charge Setpoints over CANopen.md | 30_Product Capabilities/Product Designs/CAN BMS-Directed Charging.md |
| 30_Product Capabilities/Product Functions/Hold Truck on Slope.md | 30_Product Capabilities/Product Designs/Electric Parking Brake.md |
| 30_Product Capabilities/Product Functions/Indicate Aircraft Proximity to Operator.md | 30_Product Capabilities/Product Designs/Aircraft Proximity Indicator Light.md |
| 30_Product Capabilities/Product Functions/Inhibit Drive Until Equipment Is Stowed.md | 30_Product Capabilities/Product Designs/Vehicle State Sensing Design.md |
| 30_Product Capabilities/Product Functions/Limit Truck Speed Automatically.md | 30_Product Capabilities/Product Designs/Object and Proximity Sensing Design.md |
| 30_Product Capabilities/Product Functions/Limit Vehicle Motion by Location Zone.md | 30_Product Capabilities/Product Designs/Proximity Tag System.md |
| 30_Product Capabilities/Product Functions/Lock Out Vehicle After Impact.md | 30_Product Capabilities/Product Designs/Impact Sensor.md |
| 30_Product Capabilities/Product Functions/Log Battery Events and Usage.md | 30_Product Capabilities/Product Designs/Data Handling Design.md |
| 30_Product Capabilities/Product Functions/Manage Temperature During Fast Charging.md | 30_Product Capabilities/Product Designs/Battery Cabinet Cooling Fan.md |
| 30_Product Capabilities/Product Functions/Operate Truck Remotely.md | 30_Product Capabilities/Product Designs/Remote Vehicle Operation Link Design.md |
| 30_Product Capabilities/Product Functions/Operate in Cold Storage.md | 30_Product Capabilities/Product Designs/Integrated Battery Heater.md |
| 30_Product Capabilities/Product Functions/Operate in Wet or Dusty Conditions.md | 30_Product Capabilities/Product Designs/Ingress-Protected Drive Components.md |
| 30_Product Capabilities/Product Functions/Predict Battery Replacement Timing.md | 30_Product Capabilities/Product Designs/Data Handling Design.md |
| 30_Product Capabilities/Product Functions/Program Travel, Lift and Tilt Speeds.md | 30_Product Capabilities/Product Designs/Programmable Motor Controller.md |
| 30_Product Capabilities/Product Functions/Recover Energy by Regeneration.md | 30_Product Capabilities/Product Designs/Regenerative Braking.md |
| 30_Product Capabilities/Product Functions/Reduce Charge Current in Site-Set Time Windows.md | 30_Product Capabilities/Product Designs/Time-Window Charge Current Setting.md |
| 30_Product Capabilities/Product Functions/Reduce Speed When Seat Belt Is Unfastened.md | 30_Product Capabilities/Product Designs/Seat Belt Interlock.md |
| 30_Product Capabilities/Product Functions/Refuel Truck Power Source in Minutes.md | 30_Product Capabilities/Product Designs/Hydrogen Storage Tank.md |
| 30_Product Capabilities/Product Functions/Report Truck Telemetry.md | 30_Product Capabilities/Product Designs/Wireless Interface Design.md |
| 30_Product Capabilities/Product Functions/Restrict Lift When Load Exceeds Limit.md | 30_Product Capabilities/Product Designs/Vehicle State Sensing Design.md |
| 30_Product Capabilities/Product Functions/Scale Charge Power by Module Count.md | 30_Product Capabilities/Product Designs/Modular Power Modules.md |
| 30_Product Capabilities/Product Functions/Schedule Charging Around Vehicle Readiness.md | 30_Product Capabilities/Product Designs/Charge Scheduling and Prioritization Design.md |
| 30_Product Capabilities/Product Functions/Sense Load Weight and Lift Height.md | 30_Product Capabilities/Product Designs/Vehicle State Sensing Design.md |
| 30_Product Capabilities/Product Functions/Share Power Between Charging Stations.md | 30_Product Capabilities/Product Designs/Charger-Group Peer Load Management.md |
| 30_Product Capabilities/Product Functions/Show Battery and Charger State in Fleet Software.md | 30_Product Capabilities/Product Designs/Fleet State Dashboard Design.md |
| 30_Product Capabilities/Product Functions/Show Camera View to Operator.md | 30_Product Capabilities/Product Designs/Display Device Design.md |
| 30_Product Capabilities/Product Functions/Size Battery and Charger Fleet.md | 30_Product Capabilities/Product Designs/Fleet Sizing Analytics Design.md |
| 30_Product Capabilities/Product Functions/Slow Truck in Curves.md | 30_Product Capabilities/Product Designs/Steering-Angle Curve Speed Control.md |
| 30_Product Capabilities/Product Functions/Slow and Stop Near Aircraft.md | 30_Product Capabilities/Product Designs/Object and Proximity Sensing Design.md |
| 30_Product Capabilities/Product Functions/Stabilize Truck Dynamically.md | 30_Product Capabilities/Product Designs/Active Stability Actuator.md |
| 30_Product Capabilities/Product Functions/Stabilize Truck Dynamically.md | 30_Product Capabilities/Product Designs/Stability-Limit Function Intervention.md |
| 30_Product Capabilities/Product Functions/Stabilize Truck Dynamically.md | 30_Product Capabilities/Product Designs/Steering-Angle Curve Speed Control.md |
| 30_Product Capabilities/Product Functions/Start and Stop Charge Automatically.md | 30_Product Capabilities/Product Designs/Inductive Wireless Charging.md |
| 30_Product Capabilities/Product Functions/Start and Stop Charge Automatically.md | 30_Product Capabilities/Product Designs/Conductive Auto-Contact Charging.md |
| 30_Product Capabilities/Product Functions/Start and Stop Charge Automatically.md | 30_Product Capabilities/Product Designs/Automated Connector Charging.md |
| 30_Product Capabilities/Product Functions/Steer with Electric Power Assist.md | 30_Product Capabilities/Product Designs/Electric Power Steering.md |
| 30_Product Capabilities/Product Functions/Stop Truck for Detected Obstacle.md | 30_Product Capabilities/Product Designs/Object and Proximity Sensing Design.md |
| 30_Product Capabilities/Product Functions/Stop Vehicle When Operator Is Out of Position.md | 30_Product Capabilities/Product Designs/Operator Presence Sensing Design.md |
| 30_Product Capabilities/Product Functions/Transmit Battery Data Wirelessly.md | 30_Product Capabilities/Product Designs/Wireless Interface Design.md |
| 30_Product Capabilities/Product Functions/Upload Battery Data to Cloud Portal.md | 30_Product Capabilities/Product Designs/Wireless Interface Design.md |
| 30_Product Capabilities/Product Functions/Upload Battery Data to Cloud Portal.md | 30_Product Capabilities/Product Designs/Cloud Portal Integration.md |
| 30_Product Capabilities/Product Functions/Warn Pedestrians of Approaching Truck.md | 30_Product Capabilities/Product Designs/Indicator and Alarm Design.md |

## Explicit BMID design gaps

| Function | Disposition |
|---|---|

## Findings

| Path | Kind | Detail |
|---|---|---|
| _None_ | | |

## Interpretation

- realizedBy/realizes means a Design directly implements the Function; use it only when the implementation claim is specific and defensible.
- dependsOn/dependencyOf means a Design enables or is required by the Function without claiming that the Design itself realizes the full behavior.
- The same Function/Design pair should not simultaneously carry realizedBy and dependsOn unless a reviewed semantic reason explicitly justifies both.
- Function→Function realizedBy remains legal under the schema but is outside the Function→Design focus of this step.
- The three Step 89 BMID gaps remain explicit. No Design is created or substituted merely to reduce traceability findings.