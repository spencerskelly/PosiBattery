# MHE Cost Drivers Mapped to Product Functions

## Purpose

This document maps the major cost drivers in a warehouse or production facility using material-handling equipment (MHE) to product functions that can reduce those costs. It emphasizes functions adjacent to a connected battery, charger, forklift, and cloud platform, while identifying options that extend into fleet, safety, energy, inventory, and warehouse operations.

The preferred product model is **sense → interpret → act → optimize → verify**. Monitoring provides visibility; workflow integration and control create direct operational value; financial verification makes the value defensible.

## Executive Mapping

| Cost driver | Operational impact | Core product functions | Options and extended features | Customer KPIs |
|---|---|---|---|---|
| Labor and productivity | Travel, waiting, searching, charging, inspections, paperwork, rework | Asset identity, utilization state, shift-readiness dashboard, exception alerts | Operator guidance, task display, WMS/LMS integration, load sensing, indoor location, automated dispatch | Labor cost/move, paid-to-productive time, moves/hour |
| Inventory carrying and loss | Excess safety stock, missing inventory, shrink, obsolete stock, search time | Asset association, movement-event API, dwell alerts | Forklift RFID/barcode reader, RTLS gateway, weight sensing, cycle counting, aging analytics | Inventory accuracy, turns, days on hand, shrink, search time |
| Facility and space | Space consumed by aisles, staging, charging, battery handling, spare equipment | Charger occupancy, battery-room throughput, fleet utilization by zone | Congestion heat maps, charging-footprint planner, digital-twin export, slotting integration | Cube utilization, ft²/pallet, staging dwell, charging area avoided |
| Transportation and packaging | Detention, poor trailer fill, loading errors, claims, excess packaging | Dock activity events, truck availability, load timestamps | Dock/TMS integration, trailer sensors, scales, dimensioning, proof-of-load imaging | Detention, trailer turn time, utilization, claims, freight/unit |
| MHE lifecycle cost | Excess fleet, premature battery replacement, maintenance, rentals | Runtime/utilization, battery health, charger status, cost history | Fleet right-sizing, cost/hour, warranty/lease analytics, replacement planning | TCO/truck-hour, fleet utilization, battery life, capital deferred |
| Downtime and congestion | Unavailable equipment, charger queues, blocked aisles, delayed repairs | Predictive diagnostics, readiness prediction, fault workflow | CMMS work orders, technician app, spare assignment, traffic analytics | Availability, MTBF, MTTR, queue time, lost moves |
| Safety and damage | Injuries, rack/product damage, insurance, investigations, compliance | Operator ID, impact sensing, electronic inspections, event records | Proximity warning, cameras, UWB/RFID tags, geofenced speed, lockout, coaching | Impacts/1,000 hours, damage cost, checklist compliance, near misses |
| Utilities and energy | Electricity, peak demand, charging losses, battery degradation | Charger scheduling, efficiency monitoring, peak-demand control | Tariff optimization, solar/storage integration, BMS interface, power throttling | kWh/move, peak kW, charging efficiency, energy cost/order |
| Systems and administration | Duplicate entry, disconnected records, slow response, audit burden | Common asset model, dashboards, alerts, API | WMS/CMMS/ERP/EHS connectors, workflow engine, BI export, multi-site benchmarking | Admin hours, alert closure, audit time, data completeness |

## Product Architecture

### Connected Power Core

- Unique battery, charger, and truck identities.
- Voltage, current, temperature, state-of-charge, and state-of-health acquisition.
- Charge, discharge, cycle, and fault history.
- Charger state and availability reporting.
- Cloud connectivity, configurable alerts, and event storage.
- Fleet/site/shift asset hierarchy.
- Versioned APIs, webhooks, and export.

Commercial fleet platforms already combine battery, utilization, maintenance, impact, and operator data to support fleet, labor, and asset decisions.[Raymond iWAREHOUSE](https://www.raymondcorp.com/optimization/iwarehouse-fleet-management) [Powerfleet On-Site](https://www.powerfleet.com/us/products/on-site/)

### Operational Intelligence

- Classify assets as ready, charging, working, idle, waiting, faulted, or unavailable.
- Predict shift-start readiness and remaining runtime.
- Estimate charge-completion time.
- Identify abnormal heat, voltage, current, watering, and charging behavior.
- Detect underused, overused, or incorrectly assigned assets.
- Correlate recurring faults by battery, charger, truck, operator, and shift.
- Calculate cost per truck-hour, charge cycle, and material move.

### Action and Control

- Assign the correct battery or charger.
- Create and route a maintenance work order.
- Escalate unresolved critical alarms.
- Lock out unsafe or defective equipment where supported.
- Trigger local warnings or speed limits in defined zones.
- Schedule charging around readiness and site power limits.
- Verify acknowledgement, action, and closure.

## Labor and Productivity

### Product Functions

- **Shift-readiness manager:** Predicts which truck/battery combinations can complete the next shift.
- **Asset finder:** Reports the latest location or operating zone of equipment.
- **Utilization engine:** Separates productive work, powered idle, charging, unavailable time, and unassigned time.
- **Exception routing:** Delivers actionable faults to the responsible person instead of broadcasting generic alarms.
- **Digital inspection:** Replaces paper forms with asset-specific inspections and automatic escalation.

### Extended Features

| Feature | Function | Customer value |
|---|---|---|
| Operator display/mobile app | Gives charging, battery, task, and exception instructions | Less search and decision time |
| WMS/LMS integration | Correlates paid time and completed tasks with truck activity | Exposes nonproductive labor |
| Fork/load sensor | Separates loaded travel from empty travel | Reduces deadhead movement |
| Indoor location | Tracks routes, queues, and staging dwell | Supports layout and dispatch improvements |
| Automated dispatch | Assigns the closest suitable equipment | Reduces response time and empty travel |
| Multilingual workflow | Supplies visual role-specific instructions | Faster onboarding and lower variability |

**KPIs:** labor cost per move, moves per paid hour, productive seat time, empty-travel time, charging labor, inspection duration, search time, and overtime.

## Inventory Carrying and Loss

### Product Functions

- Associate truck, operator, time, and work zone with movement events.
- Publish confirmed pickup, movement, and drop events.
- Detect unexpected dwell or movement outside assigned areas.
- Maintain traceable MHE identities independently from inventory identities.

### Extended Features

| Feature | Function | Customer value |
|---|---|---|
| Mounted barcode scanner | Confirms pallet and location at pickup/drop | Fewer misplaced loads and keyed transactions |
| RFID reader/gateway | Captures tagged loads without line-of-sight scans | Faster counting and movement verification |
| UWB/BLE location | Locates assets and high-value material | Less searching and shrink |
| Weight sensing | Compares actual and expected load | Detects loading and transaction errors |
| Cycle-count workflow | Directs counts based on risk | Reduces full physical counts |
| Dwell/aging analytics | Flags stalled or aging material | Reduces obsolescence and expiry |

**KPIs:** inventory accuracy, adjustments, search minutes, mis-picks, dwell, shrink, turns, and working capital released.

## Facility and Space

### Product Functions

- Charger occupancy and queue analytics.
- Battery-room throughput and dwell reporting.
- Fleet utilization by zone and time.
- Heat maps for idle equipment, impacts, and congestion.
- Charging-infrastructure capacity model.

### Extended Features

- Indoor-location traffic maps.
- Charging-footprint comparison for centralized, distributed, and opportunity-charging strategies.
- Digital-twin export for layout simulation.
- Slotting/WMS integration.
- Dock and staging occupancy sensors.
- Electrical and floor-space capacity forecasts.

**KPIs:** pallet positions per square foot, cube utilization, staging dwell, charging-space area, congestion minutes, and avoided expansion.

## Transportation and Packaging

### Product Functions

- Report dock-assigned equipment availability and activity.
- Timestamp loading start, completion, and idle periods.
- Detect whether sufficient MHE is ready for scheduled arrivals.
- Publish events to dock, yard, and transportation systems.

### Extended Features

- Dock-scheduling and yard-management connectors.
- Trailer-presence and door-status sensors.
- Forklift scales and shipment-weight validation.
- Dimensioning and cartonization integration.
- Load-sequence guidance.
- Proof-of-load imaging and pallet-ID capture.
- Detention-risk alerts.

EPA SmartWay identifies load, route, and network optimization as shipper improvement strategies.[EPA SmartWay resources](https://www.epa.gov/smartway/smartway-shipper-partner-tools-and-resources)

**KPIs:** detention hours, trailer turn time, on-time departure, trailer cube/weight utilization, loading errors, claims, and freight per unit.

## MHE Lifecycle Cost

### Product Functions

- Runtime and utilization by truck, battery, and charger.
- Battery capacity/health trends and replacement forecast.
- Charge quality and compatibility checks.
- Asset cost and maintenance history.
- Fleet right-sizing and redistribution recommendations.

### Extended Features

| Feature | Function | Customer value |
|---|---|---|
| Cost-per-hour engine | Combines lease, service, battery, energy, and downtime | Objective repair/replace decisions |
| Usage-based maintenance | Triggers service from runtime and condition | Avoids early or late maintenance |
| Lease/warranty module | Tracks limits, claims, and return conditions | Avoids overages and missed recovery |
| Cross-brand normalization | Creates common mixed-fleet metrics | Vendor-neutral procurement decisions |
| Battery assignment optimizer | Matches battery health to application demand | Longer battery life and fewer failures |
| Fleet scenario planner | Models transfer, retirement, rental, and purchase | Lower capital and spare fleet |

A complete MHE cost model should include charging labor and infrastructure, not only truck and battery purchase prices.[U.S. DOE/NREL TCO study](https://www.energy.gov/sites/prod/files/2014/03/f10/fuel_cell_mhe_cost.pdf)

**KPIs:** TCO per truck-hour, maintenance cost/hour, utilization, spare ratio, rentals, battery life, charger utilization, and capital avoided.

## Downtime and Congestion

### Product Functions

- Predictive battery and charger alerts.
- Remaining-runtime and readiness prediction.
- Fault history with probable cause and recommended action.
- Alert acknowledgement, escalation, and closure.
- Availability by shift and equipment class.

### Extended Features

- CMMS auto-ticketing with fault context.
- Technician diagnostics and guided troubleshooting.
- Parts recommendations.
- Indoor queue and congestion analytics.
- Automatic spare assignment.
- Service-response reporting.
- Remote firmware and configuration management.

**KPIs:** availability, MTBF, MTTR, repeated faults, work-order response, lost moves, charger queue time, and emergency rentals.

## Safety and Damage

### Product Functions

- Operator authentication and qualification validation.
- Configurable electronic pre-use checks.
- Impact detection with operator, asset, time, and location.
- Automatic defect escalation and auditable records.
- Lockout after critical failed inspections where appropriate.

### Extended Features

| Feature | Function | Customer value |
|---|---|---|
| Pedestrian proximity detection | Warns drivers and pedestrians | Lower collision risk |
| Geofenced speed control | Applies limits by zone and condition | Lower incident frequency/severity |
| AI/DVR camera | Captures context and unsafe precursors | Faster investigation and targeted coaching |
| UWB/RFID personnel tags | Provides person-to-vehicle ranging | Protects blind corners and mixed traffic |
| Safety lights/alarms | Improves local awareness | Low-complexity immediate mitigation |
| Coaching workflow | Assigns training from event patterns | Turns telemetry into behavior change |
| Incident packet | Combines video, impact, operator, and asset data | Less investigation labor |

OSHA requires trained and evaluated operators and truck examinations at least daily; trucks in continuous operation must be examined after each shift.[OSHA 29 CFR 1910.178](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.178)

**KPIs:** impacts per 1,000 operating hours and pallet moves, damage cost, near misses, speeding, checklist completion, lockouts, investigation time, and coaching closure.

## Utilities and Energy

### Product Functions

- Energy by battery, charger, truck, and shift.
- Charging efficiency and loss detection.
- Readiness-aware charge scheduling.
- Site peak-demand limiting.
- Energy cost per productive hour or move.

### Extended Features

- Time-of-use tariff optimization.
- Demand-response support.
- Solar and stationary-storage coordination.
- Charger throttling and sequencing.
- Transformer/panel capacity monitoring.
- Building-management integration.
- Carbon and customer energy reporting.
- Battery thermal optimization.

EIA reports that space heating and lighting are major warehouse/storage energy uses, so charger optimization should complement—not replace—facility energy management.[EIA warehouse energy profile](https://www.eia.gov/consumption/commercial/pba/warehouse-and-storage.php)

**KPIs:** kWh per truck-hour and move, peak kW, charging efficiency, demand charges, readiness failures, and temperature exposure.

## Systems and Administration

### Product Functions

- Common asset/site hierarchy.
- Role-based alerts, acknowledgement, and escalation.
- Configurable dashboards and scheduled reports.
- REST API, webhooks, and exports.
- Identity, access, audit, and retention controls.
- Data-quality and connectivity monitoring.

### Extended Features

- Prebuilt CMMS, WMS, ERP, LMS, and EHS connectors.
- No-code workflow builder.
- Customer-defined KPIs.
- BI/data-lake connector.
- Multi-site benchmarking.
- Single sign-on and user provisioning.
- Offline/store-and-forward gateway.
- Edge rules for low-latency actions.

**KPIs:** manual entries eliminated, reporting hours, alert closure time, data completeness, audit preparation, and integration maintenance cost.

## Commercial Packaging

| Package | Included functions | Primary buyer | Value proposition |
|---|---|---|---|
| Connected Power | Battery/charger identity, health, sessions, history, alerts | Battery/fleet manager | Protect battery investment and readiness |
| Operations | Utilization, readiness, assignment, workflow, CMMS | Operations/maintenance | Reduce waiting, downtime, and coordination |
| Fleet Intelligence | Truck telemetry, operator identity, cost/hour, right-sizing | Fleet leadership | Lower fleet TCO and labor cost |
| Safety | Checklists, impact, access, proximity, coaching | EHS/operations | Reduce incidents, damage, and compliance work |
| Energy | Charge orchestration, peak control, tariff optimization | Facilities/energy | Lower cost while preserving readiness |
| Enterprise | Cross-site model, APIs, BI, benchmarking | Corporate operations | Standardize mixed-site decisions |

## Priority Roadmap

| Priority | Product function | Main impact | Platform adjacency | Complexity |
|---:|---|---|---|---|
| 1 | Shift-readiness prediction | Labor, downtime, capacity | Very high | Medium |
| 2 | CMMS work-order integration | Downtime, administration | Very high | Low–medium |
| 3 | Truck–battery–charger identity | TCO, diagnosis, accountability | Very high | Medium |
| 4 | Charger assignment/queue management | Labor, availability, battery life | Very high | Medium |
| 5 | Energy/demand orchestration | Energy, infrastructure, readiness | High | Medium–high |
| 6 | Utilization/fleet right-sizing | Capital, rentals, maintenance | High with truck signal | Medium |
| 7 | Electronic inspections/operator access | Safety, administration | Medium | Medium |
| 8 | Impact sensing/coaching | Safety, damage | Medium | Medium |
| 9 | Indoor location/traffic analytics | Labor, space, congestion | Medium | High |
| 10 | Mobile inventory gateway | Inventory, labor | Medium | High |
| 11 | Proximity/speed controls | Safety, liability | Lower adjacency; high value | High/safety-critical |
| 12 | Automated dispatch | Labor, throughput | Requires deep WMS integration | High |

The recommended near-term wedge is **connected power plus operational workflow**: asset identity, shift readiness, automated maintenance, charger assignment, and energy orchestration. It builds on battery and charger telemetry without directly replacing established WMS or fleet-telematics platforms.

## Product Requirements

- Mixed-chemistry and mixed-vendor support.
- Reliable asset identity and association history.
- Local operation during network outages.
- Secure remote firmware/configuration updates.
- Stable, versioned event schemas and APIs.
- Role- and site-based access control.
- Configurable thresholds without firmware changes.
- Auditable actions, acknowledgements, and overrides.
- Explicit separation between advisory and safety-control functions.
- Baseline and post-deployment KPI measurement.

Safety-control features require formal hazard analysis, safe-state behavior, cybersecurity controls, installation validation, and explicit responsibility boundaries. Digital tools support compliance but do not transfer the employer's OSHA obligations.

## Value Verification

Use the following commercial model:

> **Annual value = labor avoided + downtime avoided + damage avoided + energy savings + maintenance savings + capital deferred − annual product cost**

Avoid double counting. For example, charging labor saved should not also be claimed as additional throughput unless the recovered capacity is actually used and measured.

Minimum pilot design:

1. Establish a historical baseline or comparable control area.
2. Normalize by pallet moves, truck-hours, orders, or production volume.
3. Include at least one complete demand cycle and peak period.
4. Measure workflow adoption as well as technical performance.
5. Convert operational improvements using customer-approved cost rates.
6. Confirm persistence after training and launch effects.

## Risks and Design Conflicts

- **Visibility versus action:** More alerts increase workload unless ownership and closure are built in.
- **Utilization versus resilience:** Removing all spare capacity lowers capital but raises disruption risk.
- **Demand control versus readiness:** Delayed charging saves money only if equipment remains available.
- **Safety versus throughput:** Poorly tuned speed/proximity controls create nuisance alarms and workarounds.
- **Interoperability versus support burden:** Open integration expands value but increases lifecycle validation.
- **Cloud optimization versus local safety:** Safety-critical responses cannot depend only on cloud connectivity.
- **Analytics versus privacy:** Operator analytics need policy, access control, and retention limits.
- **OEM depth versus neutrality:** Deep integrations enable control but can constrain mixed-fleet scalability.

## Future Work

- Define product-to-sensor architecture for each priority function.
- Create a dependency matrix covering hardware, firmware, cloud, mobile, and integrations.
- Build a customer-specific ROI calculator.
- Benchmark competitors by function, openness, hardware, and commercial model.
- Standardize battery, charger, truck, operator, impact, location, and work-order events.
- Perform functional-safety and cybersecurity assessments for control features.
- Create pilot protocols and acceptance criteria by value module.
- Validate which truck states can be inferred from battery current versus direct vehicle data.
- Decide build/partner strategy for RTLS, RFID, cameras, proximity, and enterprise connectors.
- Develop tiered pricing tied to verified operational outcomes.
