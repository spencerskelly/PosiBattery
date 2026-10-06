---
type: Object
subtype: software
id: OBJ-90141
uid: 20261006222000003skellyspencer
status: Draft
tags:
  - reusable-architecture
  - software
  - vehicle
  - diagnostics
  - remote-service
reuseScope: cross-product
hasDesign:
  - "[[Remote Vehicle Diagnostics Design]]"
dependsOn:
  - "[[Wireless Communication Circuit]]"
performs:
partOf:
  - "[[TUG Endurance Baggage Tractor]]"
  - "[[TUG ALPHA 1 Pushback]]"
  - "[[Diagnose Vehicle Remotely]]"
---

# Remote Vehicle Diagnostic Service

## Definition

Remote software role that receives vehicle diagnostic information and presents it to a technician or service workflow for fault isolation and troubleshooting.

## Notes

- Candidate responsibilities include diagnostic-session establishment, fault-code retrieval, snapshot display, trend/history review, technician notes, guided troubleshooting, and service-case linkage.
- This Object does not imply remote fault clearing, configuration, flashing, or vehicle control.
- It may run in a mobile tool, local service application, telematics backend, or cloud portal depending on product architecture.

## Former ids
