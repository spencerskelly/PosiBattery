---
type: Info
subtype:
id: INFO-00254
uid: 20261003195554358skellyspencer
status: Draft
tags:
  - review
  - features
  - gse-parts
describes:
  - "[[Battery-Connected Product]]"
---

# GSE Part Connection Register

## Definition

Which of 12 generic GSE parts each GSE accessory, device and software note mounts on, connects to, or acts on, with stated mappings kept apart from typical ones.

## Notes

- **Owner request (2026-10-03):** do the same part mapping for GSE vehicles as for trucks ([[Truck Part Connection Register]]): three connection types (mounts on, connects to, acts on), stated first, then typical, kept visibly separate, about 12 parts. Parts: [[GSE Vehicle Anatomy]], adapted from the truck anatomy.
- **Scope:** 11 accessory, device and software notes tagged GSE; the 15 GSE vehicle notes are the hosts and are not mapped individually. Only 11 accessories are tied to GSE in the vault, which is a coverage gap: the Hyster-Yale, Toyota and Raymond style option catalogs have no GSE equivalent yet.
- **Stated** (the source names the part): 2 rows on 1 accessory (Textron Smart Sense). **Typical** (inferred from the device class and from the functions it performs, not from a source): 9 more accessories. 1 left unmapped.
- **Reading rule:** a typical row says where this kind of device usually goes or acts; it is analyst inference, not a fact about that product. Aircraft proximity devices are given two alternative mounts (front body and bumper, or the load-handling structure) because loaders carry them on the conveyor or deck and tractors on the bumper; no source says which for most products.
- **Devices that fit both trucks and GSE:** [[Advanced Charging Technologies BATTview]], [[EnerSys Wi-iQ]], [[PosiCharge PosiGuard]], [[Power Designers PowerTrac SP+]]; they carry a typical truck mount too.

**Function-level 'acts on' map (typical)**

| Function | Parts it acts on (typical, function-level) |
|---|---|
| [[Limit Truck Speed Automatically]] | [[GSE Drive and Brakes]] |
| [[Slow and Stop Near Aircraft]] | [[GSE Drive and Brakes]] |
| [[Indicate Aircraft Proximity to Operator]] | [[GSE Controls and Display]], [[GSE Lighting]] |
| [[Stop Vehicle When Operator Is Out of Position]] | [[GSE Drive and Brakes]] |
| [[Control Operator Access]] | [[GSE Controller and CAN Bus]] |
| [[Report Truck Telemetry]] | [[GSE Controller and CAN Bus]] |
| [[Detect and Record Impacts]] | [[GSE Controller and CAN Bus]] |
| [[Alert Operator of Hazards]] | [[GSE Controls and Display]] |
| [[Show Camera View to Operator]] | [[GSE Controls and Display]] |
| [[Display Truck Status to Operator]] | [[GSE Controls and Display]] |
| [[Warn Pedestrians of Approaching Truck]] | [[GSE Lighting]] |

**Accessories by part**

**[[GSE Operator Compartment]]**

- no accessory mapped

**[[GSE Controls and Display]]**

- no accessory mapped

**[[GSE Canopy and Roof]]**

- no accessory mapped

**[[GSE Battery Compartment]]**

- *mounts on, typical:* [[Advanced Charging Technologies BATTview]], [[EnerSys Wi-iQ]], [[PosiCharge PosiGuard]], [[Power Designers PowerTrac SP+]]

**[[GSE Controller and CAN Bus]]**

- *mounts on, typical:* [[Adveez Asset and Operations Monitoring System]], [[Oshkosh AeroTech iOPS]]
- *connects to, typical:* [[Adveez Asset and Operations Monitoring System]], [[Mallaghan Collision Avoidance System]], [[Oshkosh AeroTech Aircraft Proximity Detection]], [[Oshkosh AeroTech iOPS]], [[TLD Aircraft Safety Docking]], [[Textron Smart Sense]]
- *acts on, typical:* [[Adveez Asset and Operations Monitoring System]], [[Oshkosh AeroTech iOPS]], [[TLD Aircraft Safety Docking]]

**[[GSE Drive and Brakes]]**

- *acts on, stated:* [[Textron Smart Sense]] (signals the transmission to control speed, and stops the belt loader if the operator leaves the seat)
- *acts on, typical:* [[TLD Aircraft Safety Docking]]

**[[GSE Hydraulics]]**

- no accessory mapped

**[[GSE Load-Handling Structure]]**

- *mounts on, stated:* [[Textron Smart Sense]] (ultrasonic sensors on the front of the conveyor)
- *mounts on, typical:* [[Mallaghan Collision Avoidance System]] (alt.), [[Oshkosh AeroTech Aircraft Proximity Detection]] (alt.), [[TLD Aircraft Safety Docking]] (alt.)

**[[GSE Towing Interface]]**

- no accessory mapped

**[[GSE Front Body and Bumper]]**

- *mounts on, typical:* [[Mallaghan Collision Avoidance System]] (alt.), [[Oshkosh AeroTech Aircraft Proximity Detection]] (alt.), [[TLD Aircraft Safety Docking]] (alt.)

**[[GSE Rear Body]]**

- no accessory mapped

**[[GSE Lighting]]**

- no accessory mapped

**Unmapped accessories**

| Accessory | Reason |
|---|---|
| [[PosiCharge PosiNet]] | back-office software; not mounted or connected to a GSE part |
- **Round 33 additions:** the Oshkosh AeroTech APD components, JetDock, ramp visibility lights and TLD ASD+ were added after the main table was generated; their mappings are on each note (stated rows come from the APD brochure, which names the bumper, the cab control panel and the drive interlocks): [[Oshkosh AeroTech APD Forward Radar and Controller]], [[Oshkosh AeroTech APD Wheel Position Sensor]], [[Oshkosh AeroTech APD Engine Cowling Sensors]], [[Oshkosh AeroTech APD Wing and Fairing Sensors]], [[Oshkosh AeroTech APD Pressure-Sensitive Front Bumper]], [[Oshkosh AeroTech Powered Handrail with Distance Sensor]], [[Oshkosh AeroTech JetDock]], [[Oshkosh AeroTech Ramp Visibility Lights]], [[TLD ASD+ Assisted Docking]].

## Aliases

- GSE part mapping

## Former ids
