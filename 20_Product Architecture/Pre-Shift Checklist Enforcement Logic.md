---
type: Object
subtype: software
id: OBJ-90135
uid: 20261006213500002skellyspencer
status: Draft
tags:
  - reusable-architecture
  - software
  - checklist
  - authorization
reuseScope: cross-product
hasDesign:
  - "[[Pre-Shift Checklist Enforcement Design]]"
dependsOn:
  - "[[Operator Touchscreen Display Module]]"
  - "[[Vehicle Enable Interlock]]"
performs:
partOf:
  - "[[Crown InfoLink]]"
  - "[[Crown InfoLink 7-inch Touch Display]]"
  - "[[Enforce Pre-Shift Checklist]]"
---

# Pre-Shift Checklist Enforcement Logic

## Definition

Truck-side or telematics software that runs the operator inspection workflow, records responses, determines whether the checklist is acceptable, and controls release of the vehicle for operation.

## Notes

- Candidate responsibilities include question sequencing, response capture, completion tracking, defect classification, blocking rules, operator association, supervisor override, event logging, and enable/inhibit request.
- The checklist can be presented on a dedicated telematics display, an OEM truck display, or another operator interface.
- The exact software partition between telematics platform, truck ECU, display application, and cloud service remains product-specific.

## Former ids
