# Energy Management Systems for Warehouses and Production Facilities

## Executive summary

Energy management systems for warehouses and production facilities combine electrical metering, building automation, industrial controls, energy analytics, distributed-energy management, and utility interfaces. Their value increases as the implementation progresses from basic monitoring to automated coordination of HVAC, lighting, refrigeration, production equipment, compressed air, material-handling-equipment charging, battery storage, generators, and solar generation.

The market does not offer a single universal system that performs every function equally well. Most facilities combine several platforms:

- An electrical energy-management system for power, demand, power quality, and cost allocation.
- A building-management system for HVAC, lighting, and environmental controls.
- PLC, SCADA, or industrial energy software for production equipment and utilities.
- A distributed-energy-resource controller for battery storage, solar, generators, and microgrid operation.
- A utility or aggregator interface for demand response.
- Enterprise analytics for tariffs, carbon accounting, reporting, and portfolio management.

For MHE-intensive facilities, charging is an important controllable load because its timing and power can often be adjusted without reducing throughput—provided the control system protects battery readiness for upcoming shifts. This creates an opportunity for an MHE energy-orchestration layer that translates facility-level power limits into charger-level commands using battery state, asset priority, and workload forecasts.

## System objectives

An energy-management implementation should address one or more of the following customer needs:

| Customer need | Required system capability | Expected impact |
|---|---|---|
| Understand energy use | Metering, trending, dashboards, load disaggregation | Identifies baseload, waste, abnormal operation, and high-cost loads |
| Allocate energy cost | Department, tenant, process, or work-order attribution | Improves accountability and product-cost accuracy |
| Reduce peak demand | Real-time demand forecasting and load limiting | Reduces demand charges and electrical-capacity risk |
| Optimize tariffs | Rate models and time-based scheduling | Moves flexible consumption into lower-cost periods |
| Improve asset efficiency | Energy-intensity analytics and fault detection | Reduces consumption per unit, order, pallet, or operating hour |
| Automate building loads | Scheduling, setbacks, setpoint optimization, and occupancy control | Reduces unnecessary HVAC and lighting operation |
| Coordinate production | PLC, SCADA, MES, and historian integration | Relates consumption to machine state and production output |
| Manage MHE charging | Charger power allocation and fleet-readiness forecasting | Reduces peaks without creating unavailable trucks |
| Coordinate distributed energy | Battery, solar, generator, and microgrid control | Supports peak shaving, resilience, and renewable utilization |
| Participate in grid programs | Utility or aggregator communication | Enables demand-response participation and incentive revenue |
| Track sustainability | Energy, emissions, and renewable accounting | Supports internal goals and customer or regulatory reporting |
| Avoid infrastructure upgrades | Transformer, feeder, and service-capacity management | Defers capital expenditure caused by electrification |

## System categories

### Electrical management

Electrical energy-management systems collect data from utility meters, submeters, protective devices, switchgear, power-quality meters, generators, solar inverters, battery-storage systems, and major electrical loads.

Typical functions include:

- Real-time power and energy monitoring.
- Demand and load-profile analysis.
- Power-quality monitoring.
- Alarm and event analysis.
- Electrical hierarchy modeling.
- Cost allocation.
- Tariff analysis.
- Capacity monitoring.
- Energy reporting.
- Measurement and verification.

Schneider Electric EcoStruxure Power Monitoring Expert is a representative product in this category. Schneider documentation describes an architecture in which data is acquired over Ethernet, serial communications, gateways, digital or analog inputs, Modbus, OPC, ETL, and file-based exchange before being processed by Power Monitoring Expert or Power Operation.[cite:1813] Schneider’s device tools also expose Modbus and OPC mapping for integrating device measurements into the platform.[cite:1811]

Electrical-management platforms are generally strongest at electrical visibility and analysis. Fast equipment control, machine safety, and local protection should remain in PLCs, equipment controllers, BAS controllers, charger controls, protection relays, or dedicated energy controllers.

### Building management

A building-management system, or BMS, supervises HVAC, ventilation, lighting, refrigeration, environmental conditions, and other building services. It usually contains local equipment controllers, field buses, network engines, operator workstations, alarm handling, schedules, trends, and supervisory control logic.

Johnson Controls Metasys is a representative BMS. Current Metasys network engines support combinations of BACnet/IP, BACnet Secure Connect, BACnet MS/TP, Modbus, KNX, M-Bus, LonWorks, MQTT, OPC UA, and vendor-specific integrations, depending on model and software release.[cite:1814][cite:1816]

Common BMS functions include:

- Occupancy schedules.
- Temperature and humidity control.
- Ventilation control.
- Setpoint resets.
- Equipment staging.
- Economizer control.
- Lighting schedules and dimming.
- Alarm management.
- Trend collection.
- Load shedding.
- Demand limiting.
- Fault detection.
- Runtime-based maintenance data.

A BMS commonly acts as the execution layer for building loads. An electrical EMS may determine that facility demand is approaching a limit, while the BMS applies a staged reduction to HVAC, lighting, or other eligible loads.

### Industrial management

Industrial energy-management systems connect energy measurements to machine state, production quantity, product type, shift, batch, work order, and operating condition. Their purpose is to distinguish energy required for productive output from energy lost during idle, standby, changeover, malfunction, leakage, or inefficient operating states.

These systems commonly integrate with:

- PLCs.
- SCADA platforms.
- Distributed control systems.
- MES platforms.
- Production historians.
- Utility meters.
- Machine-level meters.
- Compressed-air systems.
- Boilers, chillers, ovens, pumps, and process cooling.
- ERP cost centers and production orders.

Important industrial metrics include:

- kWh per unit produced.
- kWh per machine-hour.
- Energy cost per work order.
- Energy consumed during idle time.
- Compressed-air consumption per production unit.
- Peak power by line or process.
- Energy intensity by shift.
- Energy variance by product type.

Industrial energy management is most useful when the facility has energy-intensive production processes or substantial variation in production schedules. A warehouse may need only building, electrical, and charging management; a production facility usually requires machine and process context as well.

### Distributed resources

A distributed-energy-resource management system coordinates resources such as:

- Battery energy storage.
- Solar photovoltaic generation.
- Standby or prime generators.
- Combined heat and power.
- Controllable building loads.
- EV and MHE chargers.
- Utility power.
- Microgrid switchgear.

Honeywell describes Power Manager as monitoring grid status, utility rates, and weather while optimizing local battery-storage, solar, and generation assets.[cite:1815] This represents the transition from passive energy reporting to active dispatch of facility generation, storage, and controllable demand.

Typical control objectives include:

- Peak shaving.
- Demand-charge management.
- Time-of-use arbitrage.
- Backup-power reserve.
- Renewable-energy utilization.
- Generator minimization.
- Utility export limitation.
- Islanded microgrid operation.
- Demand-response participation.
- Transformer-capacity management.

### Energy analytics

An energy information system can sit above existing meters, BMS platforms, SCADA systems, or distributed-energy controllers. It may not directly control equipment but provides:

- Portfolio benchmarking.
- Energy baselines.
- Weather normalization.
- Anomaly detection.
- Tariff modeling.
- Carbon accounting.
- Savings verification.
- Forecasting.
- Reports and dashboards.
- Work-order recommendations.

These systems are useful when a customer already has control infrastructure but lacks cross-site visibility or consistent analytics. Their value depends on data quality, equipment context, alert ownership, and the operating processes used to convert findings into corrective action.

## Representative products

| Supplier and product | Primary category | Core strengths | Common integration role |
|---|---|---|---|
| Schneider Electric EcoStruxure Power Monitoring Expert | Electrical EMS | Meter aggregation, demand, power quality, events, reporting, cost allocation | Supervisory layer above meters, switchgear, gateways, and selected third-party devices |
| Schneider Electric Power Operation | Electrical SCADA | Real-time electrical supervision and operational control | Electrical-control layer for complex or critical power systems |
| Johnson Controls Metasys | BMS | HVAC, environmental control, schedules, trends, alarms, and supervisory automation | Building-load execution layer connected to field controllers and third-party systems |
| Siemens SIMATIC Energy Manager PRO | Industrial EMS | Production-context energy analysis and energy accounting | Connects meters, automation systems, historians, and production context |
| ABB Ability Energy Manager | Electrical and enterprise energy management | Energy visibility, benchmarking, alarms, and multi-site analysis | Supervisory analytics over ABB and third-party electrical infrastructure |
| Honeywell Forge Sustainability+ | Enterprise energy and sustainability | Energy and carbon monitoring across facilities | Enterprise reporting and optimization layer |
| Honeywell Power Manager | DER and demand management | Grid, tariff, weather, storage, solar, and generator coordination | Site power optimization and resilience layer |
| Rockwell FactoryTalk Energy Manager | Industrial energy analytics | Production-integrated energy reporting | Connects industrial automation data with energy and production metrics |
| GridPoint Energy Manager | Building and distributed-load management | Submetering, HVAC control, analytics, and demand management | Cloud-supervised control for commercial facilities |
| Ignition with energy modules | Industrial integration platform | OPC UA, MQTT, databases, dashboards, and custom workflows | Vendor-neutral integration layer between field data and enterprise applications |
| Utility or aggregator platforms | Demand response | Event signaling, dispatch, performance verification, and settlement | External interface between the facility and grid programs |

Product capabilities vary by version, licensing, region, and installed controller type. Procurement should verify each required protocol and function rather than assuming that a vendor’s overall portfolio implies support in every product.

## Functional architecture

A robust architecture separates enterprise optimization from deterministic local control.

```text
Utility, tariff, weather, and grid-service data
                     |
          Utility or OpenADR gateway
                     |
       Facility energy optimization layer
                     |
     +---------------+----------------+
     |               |                |
Electrical EMS      BMS        Industrial EMS
     |               |                |
Meters and          HVAC and         PLC, SCADA,
switchgear          lighting         MES, historian
     |               |                |
     +---------------+----------------+
                     |
             Site control gateway
                     |
       +-------------+-------------+
       |             |             |
   MHE chargers     BESS        Solar/generator
       |
 Batteries, trucks, fleet system, and WMS
```

### Control hierarchy

| Layer | Main responsibility | Typical update rate |
|---|---|---|
| Protection and safety | Electrical protection, battery protection, equipment interlocks, emergency shutdown | Milliseconds to seconds |
| Local equipment control | Charger regulation, motor control, HVAC loops, inverter control, machine sequencing | Subsecond to seconds |
| Supervisory control | Equipment staging, demand limiting, schedule execution, setpoint coordination | Seconds to minutes |
| Optimization | Tariff scheduling, charging allocation, storage dispatch, production-aware planning | Minutes to hours |
| Enterprise analytics | Reporting, benchmarking, carbon accounting, capital planning | Hours to months |

Cloud or enterprise software should not become part of a safety-critical or protection loop. Loss of an enterprise connection should cause local equipment to enter a known fallback mode rather than stopping safe, essential operation.

## Common interfaces

### Modbus

Modbus RTU and Modbus TCP are common interfaces for meters, protective devices, variable-frequency drives, chargers, inverters, PLCs, and environmental equipment. Schneider documentation identifies direct Modbus acquisition as one path for collecting data from third-party equipment.[cite:1813]

Advantages:

- Broad device availability.
- Straightforward register-based implementation.
- Suitable for embedded controllers.
- Easy gateway conversion between serial and Ethernet.

Limitations:

- Vendor-specific register maps.
- Weak semantic modeling.
- Scaling and byte-order differences.
- Limited native security.
- Polling-load constraints.
- Inconsistent alarm and timestamp behavior.

A product integrating through Modbus should include configurable register maps, scaling, quality indicators, communication health, timeout behavior, and version-controlled device profiles.

### BACnet

BACnet/IP and BACnet MS/TP dominate building automation. BACnet/IP operates over facility networks, while MS/TP connects controllers and sensors over serial field buses. Metasys uses BACnet network engines to supervise field controllers and can use routing between IP and MS/TP segments.[cite:1817]

Typical BACnet objects include:

- Analog inputs and outputs.
- Binary inputs and outputs.
- Multistate values.
- Schedules.
- Trend logs.
- Alarms.
- Device status.
- Command priorities.

BACnet integration is appropriate when an EMS must read building conditions or request changes to HVAC, ventilation, lighting, or other building loads.

### OPC UA

OPC UA is widely used between industrial equipment, gateways, SCADA systems, historians, and enterprise applications. Modern Metasys network engines also list OPC UA among supported integration methods.[cite:1816]

Benefits include:

- Structured data models.
- Browseable namespaces.
- Subscription-based data delivery.
- Authentication and encryption.
- Richer metadata than basic register protocols.
- Better support for industrial interoperability.

OPC UA is a strong choice for integrating production systems with an energy-management layer, particularly when energy data must be associated with machine states and work orders.

### MQTT

MQTT is useful for edge-to-cloud telemetry, event distribution, and loosely coupled integration. Metasys network engines list MQTT among their supported integrations.[cite:1816]

A warehouse energy application could publish:

- Meter readings.
- Charger state.
- Battery state of charge.
- Demand-limit events.
- Site-power forecasts.
- Fleet-readiness risks.
- Faults and alarms.

MQTT does not define the business meaning of each message by itself. Implementations need a controlled topic hierarchy, payload schema, units, timestamps, quality flags, identity model, and security policy.

### REST APIs

REST or similar web APIs commonly connect the EMS with:

- WMS.
- MES.
- ERP.
- CMMS.
- Fleet-management systems.
- Sustainability platforms.
- Utility-rate services.
- Weather services.
- Mobile applications.

APIs are most useful for operational context and workflow integration. Fast closed-loop equipment control should generally use local controllers and industrial protocols.

### File exchange

CSV, scheduled reports, database transfers, and ETL pipelines remain common in established facilities. Schneider documentation identifies ETL, OPC, and CSV-based methods for importing and exporting information among customer systems.[cite:1813]

File exchange is appropriate for:

- Billing data.
- Historical reporting.
- Production totals.
- Cost-center allocation.
- Utility invoices.
- Sustainability reports.

It is less suitable for real-time demand limiting or charger control.

### Other interfaces

| Interface | Common use |
|---|---|
| M-Bus | Thermal, water, gas, and utility metering |
| KNX | Lighting and building automation |
| LonWorks | Legacy building automation |
| DNP3 | Utility and electrical automation |
| IEC 61850 | Substation and protection-system integration |
| SunSpec Modbus | Solar and storage equipment |
| CAN or CANopen | Batteries, chargers, vehicles, and embedded equipment |
| J1939 | Mobile equipment and industrial vehicles |
| OCPP | Road-EV charging infrastructure |
| Digital and analog I/O | Legacy equipment, demand signals, alarms, and enable commands |

Johnson Controls documents support for M-Bus, KNX, LonWorks, Modbus, BACnet, MQTT, and OPC UA across appropriate Metasys network-engine configurations.[cite:1814][cite:1816]

## Control functions

### Monitoring

The foundation is reliable acquisition of:

- Active power.
- Reactive power.
- Apparent power.
- Energy.
- Voltage.
- Current.
- Frequency.
- Power factor.
- Demand.
- Harmonics.
- Equipment state.
- Runtime.
- Temperature.
- Flow.
- Pressure.
- Occupancy.
- Production quantity.

Monitoring alone does not guarantee savings. It creates value when the information identifies an owner, recommended action, expected financial impact, and verification method.

### Scheduling

Scheduling stops or reduces loads when they are not required. Applicable loads include:

- Lighting.
- HVAC.
- ventilation.
- Dock equipment.
- Battery-room ventilation.
- Compressed air.
- Process cooling.
- Water heating.
- Chargers.
- Noncritical pumps and fans.

Schedules should use production calendars, shift schedules, occupancy, holidays, and exception handling. Static time schedules are simple but can waste energy when operations change; occupancy- or production-aware schedules are more adaptive.

### Demand limiting

Peak-demand limiting uses real-time power and a projected demand value to prevent the facility from exceeding a target. The controller should shed or reduce loads according to customer-defined priority.

A typical sequence might be:

1. Delay low-priority charging.
2. Reduce selected charger current.
3. Adjust HVAC setpoints within approved limits.
4. Reduce noncritical lighting.
5. Dispatch battery storage.
6. Defer suitable process loads.
7. Notify operations if the site remains above target.

The system must use hysteresis, minimum run times, recovery staging, and anti-oscillation logic so that loads do not repeatedly cycle around the demand limit.

### Tariff optimization

Tariff optimization considers:

- Energy price by time.
- Demand charges.
- Coincident-peak charges.
- Seasonal rates.
- Ratchets.
- Demand-response events.
- Export compensation.
- Standby charges.
- Battery cycling cost.

The lowest-energy schedule is not always the lowest-cost schedule. A control platform should calculate avoided cost using the customer’s actual tariff and operating constraints.

### Fault detection

Energy data can reveal:

- Equipment operating outside scheduled hours.
- Compressors running continuously.
- Simultaneous heating and cooling.
- Excessive HVAC cycling.
- Failed lighting controls.
- Unexpected charger standby consumption.
- Battery or charger inefficiency.
- Air leaks.
- Degraded motors or pumps.
- Metering failures.
- Production equipment left in idle mode.

Useful fault detection must distinguish normal operational variation from actionable abnormal behavior. Alerts should include context, duration, estimated cost, likely cause, recommended action, and responsible owner.

### Storage dispatch

Battery energy storage may be dispatched for:

- Peak shaving.
- Time-of-use shifting.
- Demand response.
- Backup reserve.
- Solar self-consumption.
- Power-quality support.
- Microgrid operation.

The controller must account for state of charge, power limits, energy capacity, efficiency, degradation cost, warranty constraints, reserve requirements, and outage strategy.

### HVAC control

HVAC energy management may include:

- Occupancy-based scheduling.
- Temperature setbacks.
- Supply-air resets.
- Static-pressure resets.
- Economizer control.
- Chiller and boiler staging.
- Demand-controlled ventilation.
- Weather-based preconditioning.
- Dock-door and infiltration response.
- Thermal-load shifting.

Control changes must preserve temperature, humidity, air quality, process requirements, and worker comfort.

### Production coordination

Production-aware energy management identifies flexible and inflexible loads. Suitable control opportunities may include:

- Preheating during lower-cost periods.
- Sequencing large motors to avoid coincident startup.
- Scheduling batch processes.
- Limiting compressed-air pressure during low demand.
- Coordinating process cooling.
- Reducing idle energy.
- Synchronizing maintenance and shutdown windows.
- Avoiding unnecessary simultaneous operation.

Production throughput, quality, safety, and delivery commitments should remain higher-priority constraints than energy savings.

## MHE charging

### Operating problem

Unmanaged opportunity charging can create coincident electrical demand when operators connect multiple vehicles during breaks, shift changes, or low-work periods. A simple demand controller may reduce this peak but can create a larger operational cost if required trucks are not ready.

The energy-management problem is therefore:

> Minimize energy and demand cost while guaranteeing the required fleet capacity for every operational period.

### Required data

| Source | Required information |
|---|---|
| Charger | Input power, output current, output voltage, status, fault, session energy, available capacity |
| Battery | State of charge, temperature, state of health, charge acceptance, battery identity |
| Vehicle | Vehicle identity, assignment, operating state, energy use, location |
| Fleet system | Asset priority, required quantity, maintenance status |
| WMS or production system | Workload forecast, shift plan, wave schedule, operational exceptions |
| Facility EMS | Site demand, demand target, tariff period, grid event |
| BESS or solar system | Available power, state of charge, generation forecast |
| Operator interface | Manual priority, override, required-ready time |

### Control outputs

The orchestration layer may issue:

- Charger enable or disable.
- Maximum input power.
- Maximum output current.
- Charge-session priority.
- Scheduled start time.
- Required completion time.
- Load-shed request.
- Recovery authorization.
- Exception alert.
- Battery or charger reassignment recommendation.

Battery and charger safety limits must remain local and take precedence over external energy commands.

### Priority model

A practical charging priority calculation can consider:

- Time until the vehicle is required.
- Current state of charge.
- Expected workload.
- Battery temperature.
- Charge acceptance.
- Available alternate vehicles.
- Maintenance status.
- Charger compatibility.
- Tariff period.
- Facility demand.
- Customer override.

A warehouse with abundant spare trucks may tolerate aggressive peak limiting. A facility with a tightly sized fleet requires more conservative control and more accurate readiness prediction.

## Customer impact

### Energy cost

Energy-management systems reduce cost by:

- Eliminating off-hours operation.
- Correcting abnormal loads.
- Improving HVAC and lighting control.
- Shifting flexible loads to lower-cost periods.
- Reducing coincident demand.
- Coordinating on-site generation and storage.
- Improving equipment efficiency.
- Verifying persistence of savings.

### Infrastructure cost

Electrification can require upgrades to:

- Utility service.
- Transformers.
- Switchgear.
- Feeders.
- Panels.
- Conductors.
- Backup generation.
- Cooling and ventilation.

Coordinated charging and demand limiting can keep aggregate load below installed capacity, potentially delaying upgrades. Any claim of avoided capital cost should be validated through electrical studies, duty cycles, diversity assumptions, growth projections, and local utility requirements.

### Productivity

Energy management improves productivity when it:

- Prevents equipment unavailability.
- Ensures charged MHE at shift start.
- Reduces manual charger management.
- Automates alarm routing.
- Identifies failing equipment earlier.
- Reduces utility-data collection.
- Prevents demand-limit trips or overloads.
- Coordinates maintenance with operating schedules.

Energy optimization that disrupts production, comfort, or fleet readiness destroys more value than it saves. Operational constraints must therefore be part of the optimization model.

### Maintenance

Energy and runtime data can support:

- Condition-based maintenance.
- Identification of abnormal loads.
- Verification of repair effectiveness.
- Runtime-based service intervals.
- Charger and battery diagnostics.
- Motor and pump performance monitoring.
- Detection of control-sequence problems.

Energy anomalies are diagnostic indicators rather than definitive failure diagnoses. Maintenance workflows should combine energy data with alarms, inspections, vibration, temperature, and equipment history.

### Sustainability

A mature platform can calculate:

- Purchased electricity.
- Fuel consumption.
- Renewable generation.
- Storage charging and discharging.
- Location- or market-based emissions.
- Energy intensity.
- Avoided emissions.
- Demand-response performance.
- Energy by product or customer.

Sustainability reporting requires controlled meter boundaries, emission factors, timestamp alignment, data-quality rules, and audit trails.

## Key metrics

### Facility metrics

- Total kWh.
- Peak kW.
- Billing demand.
- Load factor.
- Power factor.
- Energy cost.
- Demand cost.
- Cost per operating hour.
- Cost per order, pallet, or unit.
- Baseload percentage.
- Off-hours consumption.
- Renewable self-consumption.
- Avoided peak demand.
- Avoided infrastructure capacity.
- Carbon emissions.

### MHE metrics

- Charging kWh per truck-hour.
- Charging kWh per move.
- Peak charging kW.
- Maximum coincident chargers.
- Charger utilization.
- Charge efficiency.
- Battery-ready compliance.
- Trucks unavailable due to energy.
- Charge-session interruptions.
- Manual charging interventions.
- Demand reduction during charging periods.
- Energy cost per operating hour.
- Battery temperature excursions.

### Control metrics

- Number of automated control events.
- Load shed per event.
- Recovery time.
- Override frequency.
- Failed commands.
- Communication availability.
- Forecast error.
- Demand-target compliance.
- False-alarm rate.
- Savings persistence.
- Operator acceptance.

## Integration requirements

### Asset model

Every connected point should map to a consistent hierarchy:

```text
Enterprise
  Site
    Building
      Electrical service
        Switchboard
          Feeder
            System
              Equipment
                Component
```

For MHE, the hierarchy should support:

```text
Site
  Department
    Vehicle
      Battery
      Charger session
      Operator or shift
```

The model should preserve relationships over time because batteries, chargers, and trucks may be reassigned.

### Data quality

Each data point should contain:

- Asset identity.
- Measurement name.
- Value.
- Unit.
- Timestamp.
- Quality indicator.
- Source.
- Update interval.
- Scaling.
- Valid operating range.
- Communication status.

Without quality indicators, missing or stale data may be interpreted as valid consumption or equipment state.

### Time synchronization

Meters, gateways, PLCs, chargers, and cloud services must use synchronized time. Misaligned timestamps make it difficult to correlate:

- Demand peaks.
- Charging sessions.
- production events.
- alarms.
- shift transitions.
- tariff intervals.
- control commands.
- utility bills.

### Command governance

Every externally controllable asset should define:

- Allowed command set.
- Operating limits.
- Local interlocks.
- Command priority.
- Override behavior.
- Communication-loss behavior.
- Maximum command duration.
- Recovery sequence.
- Audit logging.
- User authorization.

### Cybersecurity

Relevant controls include:

- Network segmentation.
- Industrial firewalls.
- Role-based access.
- Unique credentials.
- Certificate management.
- Encryption.
- Secure remote access.
- Patch management.
- Signed firmware.
- Audit logging.
- Backup and recovery.
- Disablement of unused services.
- Local fallback modes.

Connecting BMS, OT, charger, and enterprise networks can create pathways between systems that were previously isolated. Security architecture should be designed before broad interoperability is enabled.

## Product opportunity

A differentiated warehouse energy product could operate as an **MHE-aware facility-energy controller**.

### Core functions

- Aggregate charger and battery data.
- Forecast charging demand.
- Forecast fleet readiness.
- Apply a site charging-power limit.
- Allocate power by operational priority.
- Coordinate opportunity and overnight charging.
- Report energy, demand, and readiness.
- Provide facility EMS integration.
- Preserve local charger and battery protection.
- Generate savings and performance reports.

### Extended functions

- Tariff-aware scheduling.
- Open utility-event integration.
- Solar-surplus charging.
- BESS coordination.
- Transformer thermal or capacity protection.
- Production-schedule integration.
- Multi-site fleet-energy benchmarking.
- Automated CMMS work orders.
- Battery-health-aware charge optimization.
- Operator guidance.
- Dynamic reserve margin.
- Automated commissioning.
- Utility-program measurement and verification.

### Commercial packages

| Package | Functions | Customer |
|---|---|---|
| Monitor | Metering, dashboards, alarms, reports | Customer seeking visibility |
| Demand Control | Site limit, charger prioritization, peak alerts | Customer with demand charges or constrained service |
| Fleet Readiness | Battery prediction, shift planning, exception management | High-utilization warehouse |
| Tariff Optimizer | Rate model, scheduled charging, cost forecast | Time-of-use customer |
| DER Coordinator | Solar, BESS, generator, and charger coordination | Electrified or resilient facility |
| Enterprise | Multi-site analytics, APIs, governance, benchmarking | Large fleet or national account |

## Implementation roadmap

### Phase one: Baseline

- Collect utility bills and tariff schedules.
- Inventory major energy-consuming assets.
- Map meters, chargers, batteries, HVAC, lighting, production loads, and DER.
- Establish data ownership.
- Validate time synchronization.
- Measure interval demand.
- Define operational constraints.
- Establish baseline KPIs.

### Phase two: Visibility

- Add main-service and major-load metering.
- Integrate existing meters and BAS data.
- Establish electrical and asset hierarchies.
- Configure dashboards and alarms.
- Identify off-hours consumption.
- Quantify MHE charging demand.
- Validate data against utility bills.

### Phase three: Advisory

- Forecast demand.
- Identify abnormal consumption.
- Recommend charging schedules.
- Recommend HVAC or production changes.
- Quantify expected savings.
- Route recommendations to accountable users.
- Track action closure.

### Phase four: Closed loop

- Apply charger power limits.
- Execute staged demand control.
- Integrate BMS load shedding.
- Dispatch BESS where available.
- Implement automatic recovery.
- Monitor operational side effects.
- Maintain local fallback control.

### Phase five: Optimization

- Incorporate WMS, MES, weather, tariffs, fleet readiness, solar forecasts, and storage state.
- Optimize across energy cost, demand, productivity, battery health, and resilience.
- Extend control across multiple facilities.
- Automate measurement and verification.

## Pilot design

A practical pilot should include:

- One facility.
- One representative MHE operating area.
- Main-service interval data.
- Charger-level power and session data.
- Battery identity and state of charge.
- Shift requirements.
- A fixed demand target.
- Manual override.
- A control and comparison period.

Success criteria should include:

- Reduction in charging peak.
- Reduction in facility peak.
- No decrease in fleet readiness.
- No increase in charging exceptions.
- No adverse battery-temperature events.
- Operator acceptance.
- Demonstrated savings under the actual tariff.
- Reliable command and communication performance.

The pilot should separate three effects:

1. Savings from improved visibility.
2. Savings from operational process changes.
3. Savings directly attributable to automated control.

## Procurement criteria

### Functional requirements

- Required energy and demand calculations.
- Supported tariffs.
- Electrical and building asset models.
- Alarm and event functions.
- Automated control functions.
- Fleet-readiness support.
- BESS, solar, and generator support.
- Multi-site capability.
- Carbon reporting.
- Measurement and verification.

### Interface requirements

- Supported protocol and version.
- Client, server, master, or slave role.
- Point and device limits.
- Polling and update rates.
- Write-command support.
- Security capabilities.
- Gateway requirements.
- API availability.
- Data ownership.
- Export capability.
- Offline behavior.

### Lifecycle requirements

- Licensing model.
- Subscription requirements.
- Firmware and software support.
- Cybersecurity update policy.
- Hardware replacement plan.
- Configuration backup.
- Vendor lock-in.
- Integrator availability.
- Commissioning tools.
- Remote-support model.
- Product lifecycle and migration path.

## Risks and conflicts

### Operations versus energy

Demand reduction may conflict with:

- Production throughput.
- Fleet readiness.
- temperature limits.
- ventilation requirements.
- battery charging requirements.
- maintenance windows.
- employee comfort.
- delivery schedules.

Operational limits must be explicit constraints rather than assumptions.

### Control ownership

A single asset may receive commands from a local controller, BAS, EMS, utility gateway, operator interface, or cloud platform. The design must define command priority and avoid competing control loops.

### Vendor lock-in

Vendor-specific data models and closed APIs can make future integration costly. Open protocols help but do not guarantee semantic interoperability or unrestricted data access.

### Savings attribution

Energy savings may result from weather, production changes, maintenance, occupancy, equipment replacement, or automated control. Baselines and normalization are needed before assigning savings to a specific product.

### Communications loss

Loss of cloud, WAN, or supervisory communications must not create unsafe operation or prevent critical equipment from functioning. Local fallback behavior must be tested.

### Data gaps

Poor meter placement, unknown load boundaries, inconsistent asset identity, and missing production context can undermine optimization and ROI calculations.

## Product priorities

The highest-value near-term product sequence for an MHE charging supplier is:

1. Charger and battery energy visibility.
2. Fleet-readiness forecasting.
3. Facility charging-demand limiting.
4. Priority-based charger power allocation.
5. Tariff-aware scheduling.
6. Facility EMS and BMS integration.
7. Solar and BESS coordination.
8. Utility demand-response participation.
9. Multi-site optimization and benchmarking.

This sequence builds from existing charger and battery knowledge while limiting early dependence on complete facility automation. The product can first control the domain it understands—MHE charging—and expose a stable interface to the broader facility EMS.

## Future work

- Create a detailed comparison matrix for Schneider, Siemens, ABB, Honeywell, Johnson Controls, Rockwell, GridPoint, and vendor-neutral platforms.
- Document exact protocol roles, licensing, point limits, and write-control capabilities for each product.
- Develop reference architectures for warehouse-only, production, cold-storage, and microgrid facilities.
- Define a standardized charger-to-EMS data model.
- Evaluate OpenADR, IEEE 2030.5, OCPP, SunSpec, MQTT, and OPC UA for external energy coordination.
- Develop an MHE charging-demand simulation using real site load and shift data.
- Quantify infrastructure deferral for constrained transformers and utility services.
- Evaluate cybersecurity requirements for bridging charger, OT, BAS, and enterprise networks.
- Develop a pilot measurement-and-verification plan.
- Identify utilities and aggregators offering demand-response programs applicable to warehouse charging loads.
- Define fallback and command-priority requirements across local charger control, site EMS, and utility dispatch.
- Evaluate whether fleet-energy orchestration should be embedded in charger hardware, deployed as an edge gateway, or delivered through cloud software.