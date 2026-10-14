---
type: Info
subtype: research
id: INFO-00944
uid: 20261014132849798skellyspencer
status: Draft
tags:
  - research-note
  - fleet-software
  - adjacent-market
describedBy:
  - "[[Document - Phihong Fleet Platforms and Robotic Charging Stations Article (2025-08-07)]]"
  - "[[Document - VDA 5050 Version 2.1.0 AGV Communication Interface]]"
  - "[[Document - Fabrico Fleet Maintenance Software for Material Handling Review (retrieved 2026-10-14)]]"
  - "[[Document - Raymond West Warehouse Management Systems Page (Portland, retrieved 2026-10-14)]]"
describes:
  - "[[Robot and AGV Fleet Management Software]]"
  - "[[Fleet Charging and Energy Management Software]]"
  - "[[Warehouse and Business Systems Software]]"
---

# Warehouse and Business Software Landscape Register

## Definition

Register of warehouse, business, robot-fleet and energy-management software that relates to charging, vehicle management, fleet management or power management, with what each source states and what it leaves out. Created 2026-10-14.

## Notes

- **Inclusion test:** a product is listed when a page read states a charging, vehicle, fleet or power capability. Products found only through search results or a competitor's review are in the backlog, not here.
- **Already in the vault (not repeated):** 21 battery and charger management software notes and 26 truck telematics notes under [[Fleet Software and Platform]].

### Products by layer

| Product | Layer | Charging | Vehicle management | Fleet management | Power management | Evidence |
|---|---|---|---|---|---|---|
| [[Seegrid Fleet Central]] | robot fleet | schedules charging | dispatches AMRs | monitors battery levels | - | T1 brochure; Fleet Central page not read |
| [[Seegrid Auto Charge]] | robot charging | recharge without manual intervention; method not stated | - | integrated with Fleet Central | - | T1 brochure |
| [[OTTO Fleet Manager]] | robot fleet | recharge in idle periods | battery level a factor in assignment | utilization | - | T2 dealer page; maker inferred (C264) |
| [[MiR Fleet]] | robot fleet | not covered | location and availability | REST API to ERP, MES, WMS | - | T1 page |
| [[WiBotic Commander]] | charging fleet | per-robot charge scheduling, voltage and current | - | charger and battery data across fleet | - | T2 press, 2021 |
| [[Siemens depotfinity]] | charging fleet | scheduling, priorities, remote control | - | telematics-based charging (Premium) | load management, day-ahead optimization | T1 page; buses and trucks |
| [[PowerFlex X]] | site energy | remote start and stop, Fleet+ scheduler | - | state of charge and location (Fleet+) | adaptive load management, solar, storage | T1 page |
| [[Ampcontrol Yard Management for Electric Vehicles]] | charging fleet | geofence assignment to chargers by readiness | - | - | - | T1 page; OCPP 2.0.1 badge |
| [[Flip Turn Energy Management]] | site energy | queuing, priority ports | - | - | site limits, time-of-use, demand response | T1 page |
| [[FleetRabbit]] | forklift fleet | battery charge reported to WMS | dispatch nearest free truck | WMS data exchange | - | T3 vendor article |
| [[Blue Yonder Warehouse Execution]] | warehouse | not mentioned | multi-vendor robot orchestration (claim) | labor and robot interleaving (claim) | - | T1 page |

### Findings

- **Layers do not meet in the sources.** The EV and robot software (depotfinity, PowerFlex X, Flip Turn, Ampcontrol, WiBotic Commander, Seegrid, OTTO) states charging and power functions; the warehouse systems read (Blue Yonder, a Raymond West dealer page) state no battery or charging link. Only one vendor article (FleetRabbit, T3) says a WMS receives battery charge from forklifts.
- **No source shows an industrial truck charger managed by an OCPP charge-management platform.** Flip Turn and Ampcontrol say they work with OCPP chargers; PowerFlex X and depotfinity name EV fleets (buses, trucks, cars). Whether MHE chargers fit is open (IB-221).
- **Vendor content.** FleetRabbit, Phihong and Fabrico pages are vendor marketing (T3). Their claims (15 to 20 percent less empty travel; integration of fleet platforms with robotic stations; rankings of Samsara, Fleetio, TotalTrax, MaintainX) are recorded as claims, not facts about those products.
- **Dealer page, not product page.** The Raymond West page names no WMS product and does not describe the iWAREHOUSE modules in its menu.

### Standard: VDA 5050 version 2.1.0

- Interface between AGVs and a master control over MQTT with JSON. The AGV reports batteryState (charge percent, voltage, charging flag, health, reach). Master control can send startCharging and stopCharging; the vehicle is responsible for overcharge protection; charge thresholds are not defined; freely navigating vehicles are out of detailed scope. Source: [[Document - VDA 5050 Version 2.1.0 AGV Communication Interface]] (T1, second-hand).
- It sets the data a robot fleet manager can see; it does not cover forklift chargers. Compare the vault's [[Charger-Vehicle Interface Register]].

### Customer-need links

- New need [[Charge Within Site Power Limits and Utility Costs]] (UC-00054, vendor-stated) and four new functions: [[Balance Charging Power Across Site Capacity]], [[Schedule Charging Around Vehicle Readiness]], [[Dispatch Vehicles to Tasks]], [[Exchange Vehicle and Order Data with Warehouse System]]. Links to four existing needs are analyst reasoning, marked on those notes.

### Gaps

- Backlog IB-215 to IB-224.

## Former ids
