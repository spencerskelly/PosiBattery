---
type: Object
subtype: electrical
id: OBJ-00244
uid: 20261003094918663skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - gse
  - proximity
  - scope-oem-option
  - truck-device
subtypeOf:
  - "[[Proximity and Object Detection System]]"
performs:
  - "[[Limit Truck Speed Automatically]]"
  - "[[Detect and Record Impacts]]"
madeBy:
  - "[[TLD Group]]"
offeredWith:
  - "[[TLD RBL Electric Regional Belt Loader]]"
  - "[[TLD NBL-E Belt Loader]]"
---

# TLD Aircraft Safety Docking

## Definition

TLD aircraft safety docking (ASD) system that reduces speed close to aircraft and reports collisions.

## Notes

**Summary:**
TLD aircraft safe docking (ASD) option for belt loaders that limits approach speed near aircraft and records impacts.

**Marketed features:**
- ASD button engages safe mode with a flashing beacon
- Speed limited to 5 km/h; proximity sensor and sensitive bumper activated
- 3D camera detects obstacles up to 7 m ahead
- Buzzer warning, then automatic stop if the driver does not react
- 0.7 km/h in final docking phase
- Impact strength measured; GSE locked until a manager unlocks it after inspection

**Summary and features sources:**
Maker or publisher marketing claims as stated, not independently verified.
- Aero Specialties (T3), retrieved 2026-10-04. <https://www.aerospecialties.com/product/tld-rbl/>

- TLD's Group Chief Procurement Officer says the ASD system is now an industry standard, preventing aircraft damage by automatically reducing speed close to aircraft and making sure collisions are reported. Source: Ground Handling International (April 2023) (T2), retrieved 2026-10-03. <https://ghi.mydigitalpublication.co.uk/april-2023/page-44>
- **Unknown:** sensor type, ranges and which TLD models carry it.
- **Functions performed, with citations:**
  - [[Limit Truck Speed Automatically]] (V): <https://ghi.mydigitalpublication.co.uk/april-2023/page-44>
  - [[Detect and Record Impacts]] (V): <https://ghi.mydigitalpublication.co.uk/april-2023/page-44>
- **GSE parts (round 32):** typical (inferred from the device type, not from a source): mounts on [[GSE Front Body and Bumper]] (alternative) or [[GSE Load-Handling Structure]] (alternative); connects to [[GSE Controller and CAN Bus]]; acts on [[GSE Drive and Brakes]], [[GSE Controller and CAN Bus]]. See [[GSE Part Connection Register]].
- A dealer listing says the ASD system on the TLD RBL uses a 3D camera that detects any obstacle in front of the vehicle up to 7 m and keeps the loader from approaching the aircraft too fast, with the operator pressing an ASD button after entering the safety area; TLD's NBL-E page lists customizations including ASD 'no touch'; a 2020 trade report names TLD's Aircraft Avoidance Strike System using a camera and infrared and a belt-stop feature for a baggage strap caught between belt and boom (text fragmentary). Source: Aero Specialties listing, TLD NBL-E page and Ramp Equipment News (2020) (T3/T1/T2), retrieved 2026-10-03. <https://www.aerospecialties.com/product/tld-rbl/>
- **Name (C70):** the sources use ASD (Aircraft Safe Docking), Aircraft Safety Docking and ASD+; no source says the three are the same product line, so they stay as two notes, see [[TLD ASD+ Assisted Docking]].

## Aliases

- ASD
- TLD ASD

## Former ids
