---
type: Object
subtype: part
id: OBJ-00208
uid: 20261003093855177skellyspencer
status: Draft
tags:
  - battery-market-reference
  - category-family
  - gse
abstract: true
supertypeOf:
  - "[[GSE Baggage and Tow Tractor]]"
  - "[[GSE Belt Loader]]"
  - "[[GSE Cargo Loader]]"
  - "[[GSE Pushback Tractor]]"
---

# Ground Support Equipment

## Definition

Reusable family for airport ground support equipment (GSE) vehicles and the devices added to them; vehicle families, GSE-side devices, chargers and batteries are modeled as they are found.

## Notes

- Salt Lake City airport's electric GSE inspection procedure is the vault's first GSE source (see the SLC note); GSE batteries and chargers already modeled include the Flux Power GSE Pack, Green Cubes GSE Lithium Battery and ACT Quantum Outdoor. Source: Vault notes (T3), retrieved 2026-10-03. <https://www.slcairport.com/assets/pdfDocuments/EGSEInspectionProcedures.pdf>
- **To-do (owner priority):** identify GSE vehicle types and the devices added to them (battery monitors and ID devices, chargers, displays, detection). See [[Investigation Backlog]].
- EPRI lists tow tractors, belt loaders and pushback tractors as the main electric GSE types, and electric GSE makers Charlatte, Eagle, JBT, JetPorter, Lektro, TLD America and TUG. Source: EPRI Mobile Electric Airport GSE (download) (T1), retrieved 2026-10-03. <https://restservice.epri.com/publicdownload/000000003002005771/0/Product>
- Salt Lake City airport requires all ground support equipment in terminal and concourse areas, except tug tunnels, to be electric from 2020-09-15, with lithium-ion batteries and Battery Monitor and Identifier Modules installed. Source: SLC EGSE inspection procedures (T1), retrieved 2026-10-03. <https://www.slcairport.com/assets/pdfDocuments/EGSEInspectionProcedures.pdf>
- **Vehicle categories modeled:** [[GSE Baggage and Tow Tractor]], [[GSE Belt Loader]], [[GSE Pushback Tractor]], [[GSE Cargo Loader]]. Not yet modeled: ground power units, air start and air conditioning units, deicers, lavatory service, catering trucks, passenger stairs, container and pallet dollies (see [[Investigation Backlog]]).
- **Devices and accessories found:** aircraft proximity systems ([[Textron Smart Sense]], [[TLD Aircraft Safety Docking]], [[Oshkosh AeroTech Aircraft Proximity Detection]], [[Mallaghan Collision Avoidance System]]), telematics ([[Oshkosh AeroTech iOPS]], [[Adveez Asset and Operations Monitoring System]]), battery monitors and ID devices ([[PosiCharge BMID]], [[PosiCharge Battery Rx]]), GSE batteries ([[Flux Power GSE Pack]], [[Green Cubes GSE Lithium Battery]]) and chargers ([[PosiCharge SVS100]], [[PosiCharge DVS300 Series]], [[PosiCharge MVS400 and MVS800]], [[ACT Quantum Outdoor]]).
- **Scope:** electric GSE only for now (same rule as forklifts); gasoline and diesel versions are named for context (for example the Oshkosh AeroTech B80).
- **Accessory sweep (round 17):** retrofit telematics kits for tugs, belt loaders, GPUs, dollies and service carts (Adveez); Textron's Smart Sense logic and the IATA AHM 913 recommendation (see [[Textron Smart Sense]]); see [[Function and Design Levels]] for how the GSE proximity functions generalize.

## Aliases


## Former ids
