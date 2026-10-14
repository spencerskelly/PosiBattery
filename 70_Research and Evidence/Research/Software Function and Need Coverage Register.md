---
type: Info
subtype: research
id: INFO-00945
uid: 20261014133319128skellyspencer
status: Draft
tags:
  - research-note
  - traceability
  - fleet-software
describes:
  - "[[Fleet Software and Platform]]"
---

# Software Function and Need Coverage Register

## Definition

What the 57 fleet, battery, charger and warehouse software products in the vault do (their functions), which operational Use Cases and customer needs those functions are linked to, and where the coverage is empty or thin. Created 2026-10-14. "Covered" here means a software function is linked to the need, not that the need is met or that customers hold it; every need is a hypothesis.

## Notes

- **Counts:** 57 software products; 51 perform at least one function; 29 distinct functions; 102 product-to-function links; 17 of 30 needs and 12 of 16 operational Use Cases have a software function.
- **Update 2026-10-14 (IB-221):** five load-management software products were added ([[Linde connect charger]], [[Jungheinrich Active Load Management]], [[Toyota Peak Load Management]], [[Fronius PV Connect]], [[ACT ACTenergy]]), giving 62 software products, 56 with a function, and 108 product-to-function links before the Crown V-HFM3 charger link (a charger, not counted). No new need is covered; the site-power need now rests on forklift-charger sources as well as EV software ([[Forklift Charger Load Management Register]]).
- **Method:** the chain product, function, Use Case, actor was read from the notes' relationships by script. Function-to-need links were made by the analyst (see each need note); functions linked to products only where a source states the behavior.

### Needs covered by software functions

| Need | Software functions | Product links | Links without Report Truck Telemetry | Main functions (products) |
|---|---|---|---|---|
| [[Retrofit Safety and Telematics Onto Existing Trucks]] | 3 | 42 | 21 | [[Report Truck Telemetry]] (21); [[Detect and Record Impacts]] (11); [[Control Operator Access]] (10) |
| [[Right-Size the Fleet from Usage Data]] | 4 | 30 | 9 | [[Report Truck Telemetry]] (21); [[Dispatch Vehicles to Tasks]] (5); [[Report Truck Hours and Usage]] (3); [[Size Battery and Charger Fleet]] (1) |
| [[Monitor and Manage Chargers and Batteries Across Sites]] | 5 | 18 | 18 | [[Schedule Charging Around Vehicle Readiness]] (6); [[Manage Chargers Remotely]] (5); [[Upload Battery Data to Cloud Portal]] (4); [[Transmit Battery Data Wirelessly]] (2) |
| [[Control Who Operates Each Truck]] | 2 | 17 | 17 | [[Control Operator Access]] (10); [[Enforce Pre-Shift Checklist]] (7) |
| [[Detect and Learn from Truck Impacts]] | 1 | 11 | 11 | [[Detect and Record Impacts]] (11) |
| [[Return Trucks to Service Quickly After a Low Charge]] | 3 | 10 | 10 | [[Schedule Charging Around Vehicle Readiness]] (6); [[Guide Battery Selection and Rotation]] (3); [[Exchange Battery Automatically]] (1) |
| [[Document Battery Care for Warranty Compliance]] | 3 | 6 | 6 | [[Upload Battery Data to Cloud Portal]] (4); [[Export Battery Data to PC]] (1); [[Log Battery Events and Usage]] (1) |
| [[Plan Battery Replacement and Budget Ahead]] | 3 | 6 | 6 | [[Upload Battery Data to Cloud Portal]] (4); [[Log Battery Events and Usage]] (1); [[Estimate State of Health]] (1) |
| [[Keep Trucks Slow in Hazardous Zones]] | 2 | 4 | 4 | [[Limit Truck Speed Automatically]] (3); [[Limit Vehicle Motion by Location Zone]] (1) |
| [[Charge Within Site Power Limits and Utility Costs]] | 1 | 3 | 3 | [[Balance Charging Power Across Site Capacity]] (3) |
| [[Act on Fleet Data Without Information Overload]] | 2 | 3 | 3 | [[Exchange Vehicle and Order Data with Warehouse System]] (2); [[Alert on Abnormal Condition]] (1) |
| [[Find and Fix Vehicle Faults Without Downtime]] | 1 | 3 | 3 | [[Diagnose Vehicle Remotely]] (3) |
| [[Charge Without Anyone Plugging In]] | 2 | 2 | 2 | [[Start and Stop Charge Automatically]] (1); [[Exchange Battery Automatically]] (1) |
| [[Charge Each Battery Correctly for Its Chemistry and Condition]] | 2 | 2 | 2 | [[Compensate Charge for Battery Temperature]] (1); [[Configure Device from Mobile App or PC]] (1) |
| [[Integrate the Battery with Truck and Charger Controls]] | 1 | 1 | 1 | [[Communicate with Charger]] (1) |
| [[Know Battery State Before and During the Shift]] | 1 | 1 | 1 | [[Show Battery and Charger State in Fleet Software]] (1) |
| [[Warn the Operator of People and Objects Near the Truck]] | 1 | 1 | 1 | [[Detect Pedestrians and Objects Near Truck]] (1) |

### Needs with no software function

| Need | Reason | Action |
|---|---|---|
| [[Charge Without a Ventilated Battery Room]] | expected: charger and battery hardware | none needed |
| [[Connect Chargers and Batteries Safely at the Site]] | expected: connectors and cables | none needed |
| [[Handle Loads Without Damaging Them]] | expected: truck feature | none needed |
| [[Keep Equipment Working in Cold, Wet and Dusty Conditions]] | expected: enclosures and heaters | none needed |
| [[Keep Trucks Working Without Battery Maintenance Labor]] | expected: watering and battery hardware | none needed |
| [[Keep the Operator Positioned and Able to See the Work]] | expected: truck and camera hardware | none needed |
| [[Keep the Truck Under Control on Slopes, Slippery Floors and in Emergencies]] | expected: truck feature | none needed |
| [[Prevent Battery Abuse and Premature Replacement]] | software could address it | see findings |
| [[Prevent Tip-Overs and Overloads]] | expected: truck stability systems | none needed |
| [[Protect Aircraft and Ground Crew During Ground Operations]] | expected: GSE sensors | none needed |
| [[Reduce Operator Effort and Fatigue]] | expected: truck feature | none needed |
| [[Stretch Truck Run Time per Charge]] | software could address it | see findings |
| [[Warn Pedestrians of an Approaching Truck]] | expected: warning lights and sensors | none needed |

### Operational Use Cases and software functions

| Operational Use Case | Software functions linked |
|---|---|
| [[Approach and Dock GSE at an Aircraft]] | none |
| [[Authenticate and Complete Pre-Shift Authorization]] | [[Control Operator Access]] (10), [[Enforce Pre-Shift Checklist]] (7) |
| [[Charge a BMID-Equipped Battery Using Battery Information]] | [[Communicate with Charger]] (1) |
| [[Configure and Service a Supported BMID]] | [[Configure Device from Mobile App or PC]] (1) |
| [[Connect a Vehicle or Battery to a Charger]] | none |
| [[Inspect Battery Condition Through a BMID]] | none |
| [[Integrate a BMID with Charger Vehicle and Fleet Systems]] | [[Communicate with Charger]] (1), [[Transmit Battery Data Wirelessly]] (2), [[Upload Battery Data to Cloud Portal]] (4) |
| [[Manage Fleet Portal Users and Alert Thresholds]] | [[Alert on Abnormal Condition]] (1), [[Control Operator Access]] (10) |
| [[Opportunity-Charge a Vehicle During a Work Break]] | none |
| [[Review BMID Battery History and Exceptions]] | [[Upload Battery Data to Cloud Portal]] (4), [[Alert on Abnormal Condition]] (1), [[Log Battery Events and Usage]] (1) |
| [[Review Battery Care and Warranty Compliance]] | [[Upload Battery Data to Cloud Portal]] (4), [[Log Battery Events and Usage]] (1) |
| [[Review Checklist Failures and Dispatch Service]] | [[Diagnose Vehicle Remotely]] (3), [[Enforce Pre-Shift Checklist]] (7) |
| [[Review Fleet Battery Health and Plan Replacements]] | [[Upload Battery Data to Cloud Portal]] (4), [[Estimate State of Health]] (1) |
| [[Review Fleet Utilization and Idle Capacity]] | [[Report Truck Telemetry]] (21), [[Report Truck Hours and Usage]] (3) |
| [[Review an Impact Event and Decide Whether to Return the Vehicle to Service]] | [[Detect and Record Impacts]] (11) |
| [[Start a Shift and Confirm Vehicle Energy Readiness]] | [[Alert on Abnormal Condition]] (1) |

### Products with no function (6)

- [[Crown Service Request App]]
- [[Exide BattID]]
- [[HOPPECKE trak monitor 4.0]]
- [[Philadelphia Scientific iBOS]]
- [[Raymond Power Source Integrated]]
- [[Raymond iWAREHOUSE GATEWAY]]

Fronius Charge & Connect and Phantom Auto now have functions (below). The others have notes that name them without saying what they do, so they stay unlinked (IB-184, IB-189, IB-193).

## Findings

- **Report Truck Telemetry was a catch-all and was narrowed on 2026-10-14 (C265).** It still carries 21 of 102 product links, but now realizes only three needs; hours and usage (3 products) and diagnostics (3 products) are now also carried by [[Report Truck Hours and Usage]] and [[Diagnose Vehicle Remotely]], so those needs no longer rest on the generic function. Ten products state only generic fleet monitoring and a location function is still missing (IB-225).
- **Know Battery State Before and During the Shift had no software function.** The battery-monitoring products measure state, but no software function said that a person sees it. [[Show Battery and Charger State in Fleet Software]] is added from the Fronius statement only; other products that likely show state (Exide GNB Fleet, PosiCharge E-Meter, Midac Mobile App, Raymond Energy Asset Manager) need a page that says so before they are linked.
- **Prevent Battery Abuse and Premature Replacement has no software function.** The vault's battery-care software (Exide GNB Fleet, Raymond Energy Asset Manager, the EnerSys tools) states reports and alerts, not abuse prevention. Whether an alert prevents abuse is not shown in any source; do not link without one.
- **The charging-software functions added today are thin.** Schedule Charging, Balance Power, Dispatch and Exchange Data each rest on 2 to 6 products from EV or robot fleets; Charge Within Site Power Limits has 3 product links and no operational Use Case. Industrial-truck sources for Balance Charging Power were added on 2026-10-14; none shows forklift or GSE chargers on an EV platform.
- **Missing operational Use Cases.** The 16 operational Use Cases cover charging connection, BMID work, checklists, impacts and fleet reviews. Software functions with no operational Use Case behind them: scheduling charging, assigning a vehicle to a charger, limiting site charging power, dispatching a task to a vehicle, sending orders to vehicles, operating a truck remotely. These are analyst candidates, not sourced customer work; they need your input before they are written.
- **Hardware-only needs are expected to show no software.** The 11 needs marked "expected" are met by hardware or truck features; empty software coverage there is not a gap.
- **Direction of the evidence.** Telematics products (the largest group) all state safety, access and impact functions; none states a battery-state function except Raymond iWAREHOUSE (state of health). Battery-side software states reports and uploads. Charging-control software exists mainly in the EV and robot products added today.

## Backlog

- IB-225: partly done; data lists for the generic-only products and a location function are still needed.
- IB-226: pages stating what Exide GNB Fleet, E-Meter, Midac app and Raymond Energy Asset Manager show to users (battery state display).

## Former ids
