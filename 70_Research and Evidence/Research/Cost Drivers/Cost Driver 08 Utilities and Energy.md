# Cost Driver 08: Utilities and Energy

**Scope:** Warehouses, distribution centers, and production facilities using material-handling equipment (MHE)  
**Focus:** Commercial products used today, needs solved, productivity gains, costs reduced, and adjacent product opportunities

## Executive summary

Utilities and energy costs are driven by total consumption, peak demand, tariffs, power quality, and the operating cost of energy-using assets. Key loads include lighting, HVAC, dock infiltration, conveyors, compressed air, refrigeration, process equipment, and MHE battery charging. Refrigerated warehouses require separate benchmarking because their energy intensity is much higher than that of non-refrigerated facilities ([ENERGY STAR EUI metrics](https://www.energystar.gov/buildings/benchmark/understand-metrics/what-eui)).

Products used today fall into eight practical categories:

1. Energy-management systems (EMS)
2. Electrical meters and submeters
3. Connected LED lighting
4. Building-management and HVAC controls
5. Dock and building-envelope controls
6. Compressed-air monitoring and control
7. Managed MHE charging
8. Solar, storage, and microgrid controls

The strongest MHE-specific opportunity is a **fleet-energy orchestration platform** combining charger control, battery state, vehicle readiness, facility demand, tariffs, and work schedules. Eaton reports a 66% reduction in forklift-charging energy cost at its Spartanburg warehouse after applying load balancing and peak shaving. Linde’s connect:charger deployment at Arvato caps the combined load of 17 chargers while prioritizing the trucks with the lowest state of charge ([Eaton](https://www.eaton.com/us/en-us/markets/success-stories/spartanburg.html); [Linde](https://www.linde-mh.com/en/About-us/Magazine/Arvato-connect-charger/)).

## Cost-driver definition

This cost driver includes:

- Electrical energy consumption in kWh
- Utility peak-demand charges based on kW or kVA
- Time-of-use and real-time electricity pricing
- Natural gas and other heating fuels
- Refrigeration and cold-storage energy
- Water and sewer usage, including lead-acid battery watering
- Compressed-air generation and leakage
- Power-factor, reactive-power, or tariff penalties
- Maintenance of lights, HVAC units, chargers, motors, and controls
- Productivity lost to insufficient electrical capacity, failed chargers, and poor charging schedules
- Capital for service upgrades, transformers, switchgear, feeders, panels, and charging infrastructure

## Customer needs

| Customer need | Operational problem | Cost consequence | Required outcome |
|---|---|---|---|
| See energy by load | Utility bills show only site totals | Waste cannot be assigned to an asset, process, shift, or department | Trusted asset- and zone-level consumption |
| Limit peak demand | Chargers, HVAC, compressors, and production loads overlap | Demand charges and possible service upgrades | Enforced site and feeder power ceilings |
| Maintain MHE readiness | Poor load limiting leaves vehicles undercharged | Delays, queues, overtime, and missed production | Required SOC by dispatch deadline |
| Shift consumption | Energy prices vary by time | Purchase during expensive periods | Automated charging and load scheduling |
| Eliminate idle load | Lights, conveyors, ventilation, and machines run without work | Wasted energy and equipment wear | Occupancy-, task-, and schedule-based control |
| Detect abnormalities | Leaks, failed sensors, and degraded assets persist | Recurring energy and maintenance expense | Actionable anomaly alerts |
| Improve lighting | Legacy fixtures consume energy and require servicing | Electricity and relamping cost | Efficient light at required task levels |
| Control HVAC | Open docks and broad conditioning waste energy | High heating/cooling cost | Zone, occupancy, and door-aware control |
| Reduce compressed-air waste | Leaks and excessive pressure are difficult to see | Continuous electrical waste | Detection, optimization, and repair verification |
| Electrify within capacity | New chargers raise coincident load | Transformer and switchgear upgrades | Dynamic allocation within existing capacity |
| Automate reporting | Data collection is manual and inconsistent | Labor and audit exposure | Automatic energy, cost, and emissions reporting |
| Improve resilience | Outages interrupt production and charging | Throughput and recovery losses | Critical-load prioritization and backup control |

## Product landscape

### Energy-management systems

**Representative commercial products**

- Eaton Brightlayer Energy
- Schneider Electric EcoStruxure Power Monitoring Expert and Building Operation
- Honeywell Forge and building-control platforms
- Siemens building and energy-management platforms
- Independent industrial EMS platforms

**Functions**

- Aggregate meter, sensor, utility, weather, and operating data
- Establish baselines and normalize consumption
- Detect abnormal loads and operating schedules
- Forecast demand and energy use
- Control flexible loads or issue recommendations
- Verify savings and generate reports

**Needs solved**

- Fragmented data across utility bills, BMS, production equipment, and chargers
- No ownership of load by department or asset
- Limited understanding of demand peaks
- Manual sustainability reporting

**Productivity gained**

- Less manual meter reading and spreadsheet reconciliation
- Faster fault and waste diagnosis
- Fewer emergency investigations of demand events
- Better capital planning from measured load profiles

**Costs reduced**

- Electricity and fuel consumption
- Demand charges
- Reporting and audit labor
- Maintenance from excessive runtime
- Avoidable electrical upgrades

**Documented use**

Eaton reports that Brightlayer Energy, sensors, and smart meters reduced energy spend at its Spartanburg warehouse by 17%, producing more than $44,000 in annual savings. Approximately $40,000 was associated with forklift charging and $4,000 with compressed-air improvements ([case study](https://www.eaton.com/us/en-us/markets/success-stories/spartanburg.html)).

Schneider Electric reports that connected devices, local control, analytics, power monitoring, and building management at Barry Callebaut’s Belgian distribution center supported a 10% reduction in energy use and a 38% reduction in purchased energy while maintaining storage conditions ([case study](https://www.se.com/be/en/work/campaign/case-study/local/barry-callebaut/)).

**Options and extended features**

- Revenue-grade metering
- Retrofit current sensors
- Time-of-use and demand-charge tariff engine
- Automated measurement and verification
- Carbon-intensity tracking
- Demand-response interface
- Weather and workload forecasting
- CMMS work-order generation
- WMS, WES, BMS, CMMS, charger, and fleet APIs

### Smart meters and submeters

**Representative products**

- Schneider PowerLogic
- Siemens SENTRON
- Eaton Power Xpert
- Accuenergy and similar industrial meters
- Wireless branch-circuit and clamp-on retrofit sensors

**Functions and needs solved**

- Isolate lighting, HVAC, refrigeration, charging, compressed air, conveyors, and production loads
- Identify shutdown baseload and peak coincidence
- Verify retrofit savings
- Detect voltage events, phase imbalance, poor power factor, or harmonics when supported

**Productivity gained**

- Faster troubleshooting of unexplained utility increases
- Less dependence on temporary power studies
- Remote comparison across facilities
- Automatic data collection

**Costs reduced**

- Hidden persistent waste
- Engineering labor
- Power-quality-related failures and nuisance trips
- Overdesign based only on nameplate ratings

**Options and extended features**

- Edge buffering during communications loss
- Load-signature recognition
- Per-charger and per-compressor metering
- Cost per order, pallet move, batch, or operating hour
- Shift- and season-specific alarm thresholds

### Connected LED lighting

**Representative products**

- Signify Interact
- Acuity Brands nLight
- Current connected lighting
- Similar industrial IoT lighting platforms

**Functions**

- Efficient LED illumination
- Occupancy sensing
- Daylight harvesting
- Scheduling, zoning, and dimming
- Fixture-health monitoring
- Centralized or cloud management

**Documented use**

A DOE/NREL case study of an 800,000-square-foot Prologis distribution center reported a 41% reduction in electricity use, 1.9 million kWh of annual savings, approximately $226,000 in expected annual cost savings, and an 11-month simple payback after a high-bay lighting retrofit with occupancy sensors ([DOE case study](https://www1.eere.energy.gov/buildings/publications/pdfs/alliances/prologis_retrofit_30_percent_savings.pdf)).

DHL reported roughly 53% lower building energy consumption after installing connected LED high-bay fixtures, sensors, zoning, and cloud controls at a warehouse near Columbus, Ohio. The result exceeded its one-million-kWh annual savings target ([Signify case study](https://www.signify.com/en-us/blog/archive/showcase/signify-interact-industry-connected-lighting-dhl-supply-chain-warehouse)).

Pilkington Automotive uses more than 1,300 luminaires and 600 sensors at a 47,000-square-meter warehouse. Signify reports up to 50% lower energy use than comparable conventionally lit sites through demand-based control, daylight harvesting, and presence sensing ([case study](https://www.signify.com/global/case-studies/pilkington)).

**Needs solved**

- Lighting unoccupied aisles
- Uniform output despite different task requirements
- Poor fixture-failure visibility
- High relamping labor and lift access

**Productivity gained**

- Better light at picks, docks, and inspection stations
- Faster fault identification
- Remote commissioning
- Fewer maintenance interruptions
- Occupancy data for workflow analysis

**Costs reduced**

- Lighting energy
- Replacement lamps and relamping labor
- Lift rental and disposal
- Cooling load from inefficient lighting

**Options and extended features**

- Aisle-level sensing
- Skylight daylight sensors
- Task scenes for picking, cleaning, and inspection
- Emergency-light monitoring
- Occupancy and location analytics
- Lighting-as-a-Service
- MHE-aware activation ahead of a moving truck

### Building-management and HVAC controls

**Representative products**

- Schneider Electric Building Operation
- Honeywell building controls
- Siemens building platforms
- Johnson Controls Metasys
- Packaged rooftop-unit controllers

**Functions**

- HVAC scheduling and setback
- Zone control
- Setpoint and ventilation optimization
- Fault detection and diagnostics
- Door and occupancy integration
- Refrigeration supervision

ENERGY STAR identifies scheduling, setpoint review, occupancy control, dock seals, conditioned-zone separation, demand ventilation, high-efficiency equipment, variable-frequency drives, and advanced rooftop-unit controllers as applicable warehouse measures ([warehouse best practices](https://www.energystar.gov/sites/default/files/tools/Warehouse%20best%20practices%20062014.pdf)).

**Needs solved**

- Conditioning empty areas
- Simultaneous heating and cooling
- Open-door infiltration
- Poor high-bay temperature distribution
- Excess ventilation
- Limited remote fault information

**Productivity gained**

- More stable worker and storage conditions
- Fewer manual thermostat changes
- Faster HVAC diagnosis
- Reduced unplanned downtime
- Central support across sites

**Costs reduced**

- Heating fuel and HVAC electricity
- Compressor, fan, pump, and heater runtime
- Maintenance from cycling
- Temperature-related product losses
- Technician travel

**Options and extended features**

- Dock-door/HVAC interlock
- Weather-compensated setpoints
- Demand-controlled ventilation
- Temperature, humidity, and air-quality sensing
- Predictive maintenance
- Adaptive refrigeration defrost
- Digital-twin experimentation
- Production-schedule integration

### Dock and envelope products

**Representative products**

- Dock seals and shelters
- High-speed insulated doors
- Air curtains
- Door-position sensors
- Insulated roofs and walls
- Cool-roof systems
- Thermal-imaging inspection products

**Needs solved**

- Conditioned-air loss at docks
- Rain, dust, and outdoor-air entry
- Doors remaining open after MHE traffic
- Roof and wall heat transfer

**Productivity gained**

- Stable dock conditions
- Faster vehicle passage with high-speed doors
- Fewer manual open-door checks
- Less weather-related interruption

**Costs reduced**

- HVAC and refrigeration energy
- Temperature-related product loss
- HVAC capacity and runtime
- Contamination and moisture maintenance

**Options and extended features**

- Door-open timer and alarm
- Trailer-presence sensing
- MHE approach detection
- Dock leveler, restraint, door, and HVAC interlocks
- Automated thermal inspection
- Door-open minutes by dock, carrier, shift, or operator

### Compressed-air monitoring

**Representative products**

- Ultrasonic leak detectors
- Permanent acoustic leak sensors
- Flow, pressure, dewpoint, and power meters
- Compressor sequencers and master controls
- Cloud compressed-air analytics

**Functions and needs solved**

- Detect leaks
- Identify excess pressure
- Coordinate compressor staging
- Find nonproduction baseload
- Allocate air use by production area

**Productivity gained**

- Faster leak localization and repair verification
- Less manual inspection
- Better maintenance planning
- More stable process pressure

**Costs reduced**

- Compressor electricity
- Runtime and maintenance
- Low-pressure production interruptions
- Unnecessary capacity additions

**Options and extended features**

- Mobile survey application with photo and location
- Automatic CMMS ticketing
- Leak-cost calculation
- Adaptive staging and pressure optimization
- Shift-based baseload alarms

### Managed MHE charging

**Representative products**

- Linde connect:charger
- HOPPECKE trak monitoring and energy-management products
- Charger-network platforms from industrial battery and charger manufacturers
- Facility EMS platforms such as Eaton Brightlayer

**Functions**

- Monitor charger input and output
- Import battery SOC, temperature, and identity
- Set an aggregate power ceiling
- Prioritize charging by SOC, deadline, and asset importance
- Shift charging around tariffs and facility loads
- Forecast readiness and power requirements

**Documented use**

At Arvato, Linde connect:charger supervises 17 lithium-ion chargers, enforces a 180 kW aggregate ceiling, and prioritizes the trucks with the lowest SOC ([Linde case study](https://www.linde-mh.com/en/About-us/Magazine/Arvato-connect-charger/)).

At Eaton’s Spartanburg warehouse, load balancing and peak shaving addressed random charging spikes and unnecessary high-power charging. Eaton reports a 66% reduction in forklift-charging energy cost and approximately $40,000 in annual savings ([Eaton case study](https://www.eaton.com/us/en-us/markets/success-stories/spartanburg.html)).

A HOPPECKE project coordinated photovoltaic generation, forklift batteries, chargers, and monitoring. HOPPECKE reports that direct solar charging of traction batteries avoided intermediate storage and improved system efficiency by 10% ([HOPPECKE case study](https://www.hoppecke.com/fileadmin/Redakteur/Hoppecke-Main/Downloads/casestudies/trak_case_study_green-charging-with-pv_en.pdf)).

**Needs solved**

- Simultaneous charger starts
- High demand peaks
- Charging during expensive periods
- Excess charge rate
- Undercharged vehicles at shift start
- Overbuilt electrical infrastructure
- Disconnect between fleet readiness and site power

**Productivity gained**

- Fewer charging queues
- Improved shift readiness
- Less operator charger-selection effort
- Faster identification of charger and battery problems
- Better growth and electrification planning

**Costs reduced**

- Demand charges
- Time-of-use energy cost
- Electrical upgrades
- Battery wear
- Charge-related downtime and overtime
- Manual battery-room management

**Options and extended features**

- Site, transformer, feeder, panel, and charger constraints
- Dispatch-deadline prioritization
- Tariff- and carbon-aware scheduling
- Connector-temperature and charger-health monitoring
- WMS/WES workload forecasts
- Offline edge fallback
- Mixed-chemistry fleet support
- Solar and stationary-storage coordination
- Fleet-growth simulator

### Solar, storage, and microgrid controls

**Representative products**

- Rooftop photovoltaic systems
- Battery energy-storage systems
- Microgrid controllers
- Automatic transfer and islanding systems
- Integrated distributed-energy-resource management

**Needs solved**

- Purchased-energy exposure
- Demand peaks
- Grid outages
- Utility-capacity limits
- Renewable-energy objectives

**Productivity gained**

- Continued operation of critical IT, controls, chargers, and processes
- Automated load shedding and source selection
- Less manual generator coordination

**Costs reduced**

- Purchased energy
- Demand charges
- Outage losses
- Generator fuel in suitable applications
- Electrical upgrades where storage supports peaks

**Options and extended features**

- Critical-load hierarchy
- Islanding and black start where permitted
- Tariff-optimized storage dispatch
- Solar-to-fleet optimization
- Demand response
- Resilience runtime dashboard
- Bidirectional charging, subject to charger, battery, warranty, safety, and utility constraints

Warehouses have substantial roof area but often modest energy density; DOE notes that this mismatch can limit how much rooftop solar can be consumed behind the meter unless load, storage, or export arrangements are aligned with generation ([DOE case study](https://betterbuildingssolutioncenter.energy.gov/sites/default/files/attachments/Link_PV_Valuation_Case_Study.pdf)).

## Existing-product matrix

| Category | Representative products | Need solved | Productivity mechanism | Primary cost reduction |
|---|---|---|---|---|
| EMS | Eaton Brightlayer; Schneider EcoStruxure; Honeywell Forge | Fragmented data and uncontrolled loads | Analytics, alarms, automated control | Energy, demand, reporting labor |
| Metering | PowerLogic; SENTRON; Power Xpert | Lack of load visibility | Remote measurement and fault isolation | Waste, studies, power-quality losses |
| Connected lighting | Signify Interact; Acuity nLight | Excess lighting and maintenance | Occupancy/daylight control | Lighting energy, relamping, cooling |
| BMS/HVAC | Schneider, Honeywell, Siemens, Johnson Controls | Conditioning and ventilation waste | Scheduling, zoning, diagnostics | Energy, fuel, maintenance |
| Dock/envelope | High-speed doors, seals, sensors | Air infiltration | Automated door behavior | HVAC/refrigeration and product loss |
| Compressed air | Leak sensors, meters, sequencers | Leaks and poor pressure control | Faster repair and staging | Compressor energy and capacity |
| Managed charging | Linde, HOPPECKE, charger networks | Peak/readiness conflict | SOC- and deadline-aware allocation | Demand, tariffs, infrastructure, downtime |
| Solar/storage/microgrid | PV, BESS, microgrid controls | Purchased energy, peaks, outages | Generation, dispatch, islanding | Energy, demand, outage exposure |

Product names illustrate commercial categories rather than a procurement shortlist. Selection should consider protocols, service, cybersecurity, warranty, integration, and evidence from similar duty cycles.

## Documented outcomes

| Deployment | Product function | Reported result | Decision implication |
|---|---|---|---|
| Eaton Spartanburg | Metering, analytics, load balancing | 17% lower spend; over $44,000 annual savings; 66% lower forklift-charging energy cost | Strong evidence for charging orchestration and submetering |
| Prologis distribution center | High-bay retrofit and occupancy sensing | 41% electricity reduction; $226,000/year; 11-month payback | Legacy lighting can have rapid payback |
| DHL Supply Chain | Connected LED, sensing, zoning | Roughly 53% lower building energy; over 1 million kWh/year | Control adds value beyond fixture efficiency |
| Pilkington Automotive | Daylight and presence-based lighting | Up to 50% below conventional-lighting sites | Baseline and occupancy determine result |
| Barry Callebaut | Integrated building/power management | 10% lower energy; 38% lower purchased energy | Controls can reduce energy while protecting storage conditions |
| Arvato | Charger-load cap and SOC prioritization | 180 kW cap across 17 chargers | Power limiting can preserve readiness when priorities are known |
| HOPPECKE logistics center | Solar-directed charging | 10% efficiency improvement reported | Direct PV-to-traction charging can reduce conversion losses |

These are vendor or government-program case studies, not guaranteed outcomes. Normalize for baseline equipment, facility size, climate, tariff, schedule, workload, and implementation scope.

## Productivity mechanisms

| Mechanism | Productivity effect | Measurement |
|---|---|---|
| Automatic load control | Removes manual curtailment decisions | Operator interventions per shift |
| Readiness optimization | Prevents undercharged MHE | Ready vehicles; delay minutes |
| Remote diagnostics | Reduces travel and troubleshooting | Mean time to diagnose; labor hours |
| Predictive maintenance | Moves work to planned windows | Emergency work; downtime |
| Stable environment | Protects workers, equipment, and inventory | Excursions; complaints; quality losses |
| Improved lighting | Supports picking and inspection | Error rate; task time |
| Automated reporting | Eliminates data reconciliation | Administrative hours/month |
| Capacity optimization | Adds assets without immediate upgrade | Vehicles per installed kVA |

## Cost-reduction model

### Consumption

Avoided consumption is reduced kWh or fuel multiplied by the applicable rate. Savings can come from LEDs, occupancy control, HVAC scheduling, dock seals, VFDs, adaptive refrigeration, compressed-air leak repair, and charger-efficiency improvements.

### Peak demand

Demand savings result from lowering the billed peak. The algorithm must use the utility’s actual billing interval and ratchet rules rather than simply smoothing instantaneous power.

### Infrastructure deferral

Dynamic load management may keep aggregate charging under feeder, panel, transformer, or utility-service constraints. Avoided infrastructure cost can exceed annual energy savings.

### Maintenance

Longer-life lighting, fault detection, runtime reduction, and condition-based service reduce labor, parts, access equipment, and disruption. Account for these benefits separately from utility savings.

### Operational losses

A fleet-energy system creates value by preventing undercharged trucks, failed chargers, queues, and constrained production. Base savings on documented delay minutes, labor rates, throughput loss, and recovery cost.

## KPI framework

### Facility

- Electricity in kWh/month
- Electricity cost/month
- Site EUI
- Maximum billed kW or kVA
- Load factor
- Energy cost per order, pallet move, unit, or labor hour
- Shutdown baseload
- Renewable fraction and self-consumption
- Avoided emissions with documented factors

### MHE energy

- kWh per truck operating hour
- kWh per pallet move or work cycle
- Charger input-to-battery efficiency
- Peak charging demand
- Charging coincidence factor
- Ready-at-shift-start percentage
- Charge-related delay minutes
- Charger utilization and queue time
- Battery energy throughput and temperature exposure
- Energy cost per truck-hour

### Building systems

- Lighting kWh per occupied hour
- Weather-normalized HVAC energy
- Dock-open minutes during conditioning
- Compressed-air baseload outside production
- Refrigeration kWh per pallet-day
- Temperature-excursion count and duration

## ROI method

**Annual benefit** = energy savings + demand savings + maintenance savings + labor savings + avoided downtime + annualized deferred-capital value.

**Net annual benefit** = annual benefit − software subscription − communications − calibration − maintenance − support.

**Simple payback** = installed cost ÷ net annual benefit.

For managed charging, include:

- Utility-interval load history
- Charger/facility demand coincidence
- Energy and demand tariffs
- Truck schedules and dispatch deadlines
- SOC and energy requirements
- Electrical hierarchy and limits
- Fleet growth
- Battery and charger efficiency
- Cost of missed readiness
- Integration and lifecycle cost
- Avoided electrical upgrades

Normalize pre/post results for weather, workload, occupancy, and schedule. Utility-bill comparisons alone can misattribute unrelated changes.

## MHE-adjacent opportunities

### Fleet Energy Orchestrator

**Core functions**

- Ingest charger input/output, state, faults, and availability
- Ingest battery SOC, state of health, temperature, chemistry, and identity
- Associate battery, charger, truck, operator, and department
- Accept site and feeder constraints
- Forecast energy required by asset and shift
- Allocate power to meet deadlines at minimum cost
- Maintain local fallback during cloud loss

**Customer value**

- Reduces demand and time-of-use costs
- Preserves shift readiness
- Defers service and distribution upgrades
- Supports electrification within existing capacity
- Produces auditable cost per truck and department

**Extended features**

- WMS/WES integration
- Demand-response and tariff integration
- Solar/storage coordination
- Carbon-aware scheduling
- Charger-health scoring
- Growth and placement simulation
- Multi-level electrical constraints
- Multi-site benchmarking
- BMS, EMS, CMMS, and finance APIs

### Shift Readiness and Energy Planner

**Functions**

- Predict next-shift SOC
- Flag vehicles unlikely to be ready
- Recommend charger, charge window, or replacement battery
- Prioritize critical trucks
- Quantify remaining energy and time

**Value**

- Reduces shift-start delays
- Prevents low-priority charging from blocking critical assets
- Connects energy optimization to throughput
- Gives supervisors exception-based workflows

### Electrical Capacity Planner

**Functions**

- Import load profiles and the electrical hierarchy
- Model additional trucks, chargers, shifts, and strategies
- Compare unmanaged, static-cap, and dynamic-control scenarios
- Estimate transformer and feeder headroom
- Generate planning and quotation reports

**Value**

- Reduces engineering effort
- Avoids overbuilding
- Accelerates site design
- Quantifies deferred capital

### Charger and Power Quality Monitor

**Functions**

- Detect abnormal current, imbalance, voltage sag, harmonics, connector heat, and interruptions
- Correlate power events with charger faults and battery behavior
- Create CMMS work orders with diagnostic context

**Value**

- Prevents failures and nuisance trips
- Shortens diagnosis
- Distinguishes charger, battery, connector, and facility problems
- Reduces unnecessary parts replacement

### Energy Cost Allocation

**Functions**

- Allocate energy and demand costs by truck, charger, shift, department, customer, or cost center
- Normalize by runtime, moves, or throughput
- Export to finance and sustainability systems

**Value**

- Creates accountability
- Supports chargeback and contract costing
- Identifies high-cost applications
- Expresses value in operational units

### Site Energy Gateway

**Functions and options**

- Aggregate chargers, batteries, meters, docks, lighting, solar, and BMS data
- Ethernet, Wi-Fi, cellular, and isolated industrial interfaces
- Modbus TCP/RTU, BACnet/IP, MQTT, REST, OCPP where applicable, and vendor adapters
- Local historian and store-and-forward
- Local load-shedding rules
- Secure updates and certificate management
- Segmented OT/IT interfaces

**Value**

- Reduces integration hardware
- Extends a charging platform into facility energy
- Preserves local control during outages
- Provides a vendor-neutral integration point

## Product tiers

| Tier | Scope | Customer | Primary value |
|---|---|---|---|
| Monitor | Charger/battery visibility, alerts, reports | Small fleets and pilots | Establish baseline and expose waste |
| Control | Dynamic limits, SOC priorities, schedules | Multi-shift fleets | Reduce peaks while preserving readiness |
| Optimize | Tariffs, workload forecasts, solar/storage | Large facilities | Minimize total energy and infrastructure cost |
| Enterprise | Multi-site benchmarking, APIs, governance | National/global operators | Standardize performance and reporting |
| Managed service | Monitoring, tuning, M&V, reporting | Customers lacking energy specialists | Sustain savings over time |

## Functional requirements

### Data acquisition

- Measure charger input energy and peak power
- Capture output data and charge states
- Receive SOC, voltage, current, temperature, health, and alarms
- Import utility interval data and tariffs
- Accept electrical constraints by hierarchy
- Integrate shift calendars and vehicle requirements
- Maintain synchronized timestamps

### Optimization

- Meet configurable minimum SOC by deadline when physically possible
- Enforce hard electrical constraints locally
- Support priorities, reserves, and emergency overrides
- Optimize for cost, demand, carbon, or combined objectives
- Explain control decisions
- Recalculate when connections, jobs, or facility loads change

### Reporting

- Compare actual cost with uncontrolled and static baselines
- Show peak contribution by charger and interval
- Report readiness compliance
- Separate energy, demand, labor, downtime, and capital benefits
- Export auditable data and assumptions

### Reliability and safety

- Fail to a defined local mode
- Keep charger and battery safety controls authoritative
- Prevent cloud software from bypassing electrical or thermal limits
- Log all user, rule, and API actions
- Use role-based access, signed firmware, encryption, and secure provisioning

## Architecture

1. **Asset layer:** batteries, chargers, forklifts, meters, solar, BESS, HVAC, and lighting
2. **Edge layer:** protocol adapters, historian, deterministic control, cybersecurity boundary, offline operation
3. **Platform layer:** asset model, tariff engine, forecasts, optimization, analytics, APIs
4. **Application layer:** operator guidance, dashboards, planning, maintenance, executive reporting
5. **Enterprise layer:** WMS/WES, CMMS/EAM, BMS/EMS, ERP, utility, identity, sustainability reporting

Keep safety control, operational control, and economic optimization distinct. Battery and charger protection stays local; shift orchestration can run at the edge; long-horizon planning and portfolio analytics can run in the cloud.

## Pilot design

### Baseline

- Instrument site service, charging distribution, and representative chargers
- Gather normal and peak operational cycles
- Import tariffs and billing rules
- Map schedules, SOC needs, and charge-related delays
- Validate meter accuracy and identity

### Advisory mode

- Forecast demand and readiness without control
- Compare recommendations with supervisor decisions
- Estimate peak and tariff savings
- Tune constraints and thresholds

### Controlled deployment

- Apply a conservative aggregate limit
- Prioritize by SOC, deadline, and criticality
- Retain operator override
- Monitor readiness, queues, peak, and temperature

### Optimization

- Add tariff-aware scheduling
- Integrate workload forecasts
- Coordinate solar, storage, HVAC, or other flexible loads
- Verify operational and financial results

### Acceptance criteria

- No increase in missed readiness
- Measurable reduction in peak or billed demand
- Correct local behavior during network/cloud loss
- Accurate asset association and accounting
- Positive verified net savings
- Accepted operator and maintenance workflow

## Risks and conflicts

| Risk or conflict | Impact | Mitigation |
|---|---|---|
| Vendor-claimed savings | May reflect an old baseline or unusual tariff | Use site-specific interval data |
| Peak reduction vs. readiness | Curtailment can harm throughput | SOC deadlines, reserves, priorities |
| Mixed protocols | Inconsistent data and control | Normalized model and qualified adapters |
| Poor asset identity | Incorrect savings and diagnostics | Controlled commissioning workflows |
| Cloud dependence | Connectivity could interrupt control | Deterministic edge fallback |
| Cybersecurity | Operational controls expand attack surface | Segmentation, authentication, logs, secure updates |
| Tariff complexity | Incorrect savings calculation | Utility-specific billing logic |
| Baseline drift | Weather and volume distort results | Normalize and re-baseline |
| Battery warranty | Optimization may exceed limits | Treat OEM/BMS limits as hard constraints |
| Certification | External control may affect listings | Do not bypass certified protection; assess impact |
| Split incentives | Owner and tenant value differ | Shared savings, lease, or managed service |
| Rebound effect | Added capacity consumes savings | Track energy per productive unit |

Additional design tensions:

- Lowest peak versus full vehicle readiness
- Lowest energy price versus battery life
- Cloud optimization versus deterministic local control
- Open integration versus cybersecurity
- Cross-vendor breadth versus diagnostic depth
- Quick lighting payback versus strategic energy-platform investment
- Energy policy versus operator convenience

## Recommended roadmap

### Near term

- Add accurate charger input-energy and peak reporting
- Associate charger, battery, and truck identities
- Implement readiness forecasting and alerts
- Add facility and charging-demand dashboards
- Provide tariff-aware savings estimation

### Mid term

- Add edge-based aggregate load control
- Prioritize by SOC, deadline, and criticality
- Import electrical hierarchy and utility interval data
- Create CMMS workflows for anomalies
- Release capacity-planning tools

### Extended

- Integrate WMS/WES demand forecasts
- Coordinate solar, storage, HVAC, and demand response
- Add multi-site optimization
- Offer managed energy services and M&V
- Evaluate bidirectional forklift charging only after technical, warranty, safety, economic, and utility validation

## Future research

- Compare representative warehouse tariffs and identify regions where managed charging has strongest value
- Benchmark industrial charger and BMS protocols and remote-control capabilities
- Establish required data resolution for optimization and auditable savings
- Compare Modbus, CAN, BACnet, OCPP, MQTT, and vendor API architectures
- Assess electrical-code, listing, and certification implications
- Quantify charging strategy effects on battery temperature, life, and warranty
- Define energy cost per productive MHE hour or pallet move
- Determine which WMS/WES inputs improve forecasts
- Compare software-only, submetered, and storage-supported economics
- Map applicable utility incentives and demand-response programs
- Quantify avoided transformer and service upgrades from real designs
- Develop a cybersecurity threat model for connected charging fleets

## Procurement checklist

- Does the product measure charger input and battery-delivered energy?
- Can it enforce site, transformer, panel, and charger limits?
- Does it use SOC and dispatch deadlines, or only schedules?
- Does safe control continue during network loss?
- Are local utility tariffs represented accurately?
- Can savings be exported and independently audited?
- Which charger, BMS, meter, and building protocols are supported?
- Are APIs documented and commercially available?
- How are identity, certificates, firmware, and access managed?
- What commissioning and recurring support are required?
- Are claims measured, modeled, or estimated?
- What conditions invalidate claimed savings?
- Can the system prove that savings did not reduce readiness or throughput?

## Conclusion

Utilities and energy should be managed as an operational system rather than treated only as a monthly bill. Mature commercial products already reduce lighting, HVAC, compressed-air, refrigeration, charging, maintenance, and reporting costs. The strategic MHE opportunity is to connect facility power constraints and tariffs with charger state, battery condition, truck identity, and operational demand.

A practical product sequence is monitoring, shift-readiness forecasting, deterministic edge control, and then broader facility optimization. This creates incremental value while preserving safety and compatibility with mixed fleets. Every investment case should use the customer’s actual tariff, equipment, duty cycle, baseline, and operational constraints.
