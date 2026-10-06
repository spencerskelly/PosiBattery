---
type: Object
subtype: software
id: OBJ-00168
uid: 20261003084359648skellyspencer
status: Draft
tags:
  - scope-oem-option
  - software
  - telematics
subtypeOf:
  - "[[Truck Telematics Software]]"
performs:
  - "[[Report Truck Telemetry]]"
  - "[[Control Operator Access]]"
  - "[[Detect and Record Impacts]]"
  - "[[Enforce Pre-Shift Checklist]]"
hasDesign:
  - "[[Operator Touch Display]]"
  - "[[Operator Access Authorization Design]]"
  - "[[Pre-Shift Checklist Enforcement Design]]"
madeBy:
  - "[[Crown Equipment]]"
offeredWith:
  - "[[Crown FC 5700 Series]]"
  - "[[Crown RC 5700 Series]]"
  - "[[Crown Battery Health Monitor]]"
hasPart:
  - "[[Operator Access Authorization Logic]]"
  - "[[Pre-Shift Checklist Enforcement Logic]]"
  - "[[Vehicle Enable Interlock]]"
  - "[[Crown Gena Operating System]]"
---

# Crown InfoLink

## Definition

Crown wireless fleet and operator management system, paired with on-truck InfoPoint feedback.

## Notes

- Crown's FC 5700 brochure lists InfoLink wireless operator and fleet management and InfoPoint on-truck feedback; the RC 5700 sheet marks trucks InfoLink ready. Source: Crown FC 5700 brochure and RC 5700 sheet (T1), retrieved 2026-10-03. <https://www.crown.com/content/dam/crown/pdfs/apac/brochures/forklift-truck-fc5700-brochure-GB.pdf>
- **Functions performed, with citations:**
  - [[Report Truck Telemetry]] (V): <https://www.crown.com/content/dam/crown/pdfs/apac/brochures/forklift-truck-fc5700-brochure-GB.pdf>
- **Design characteristics, with citations:**
  - [[Operator Touch Display]] (V): <https://www.crown.com/content/dam/crown/pdfs/apac/brochures/forklift-truck-fc5700-brochure-GB.pdf>
- Crown lists InfoLink Operator and Fleet Management System features of access control, visual inspection checklists, impact detection and alerts and equipment lockout; it needs an InfoLink service plan and a 7 inch touch display or Gena screen shows alerts. Source: Crown SP 1500 brochure and ESR page (T1), retrieved 2026-10-03. <https://crown.com/content/dam/crown/pdfs/apac/brochures/SP-1500-Broch-APAC.pdf>
- **Functions performed, with citations:**
  - [[Control Operator Access]] (V): <https://crown.com/content/dam/crown/pdfs/apac/brochures/SP-1500-Broch-APAC.pdf>
  - [[Detect and Record Impacts]] (V): <https://crown.com/content/dam/crown/pdfs/apac/brochures/SP-1500-Broch-APAC.pdf>
  - [[Enforce Pre-Shift Checklist]] (V): <https://crown.com/content/dam/crown/pdfs/apac/brochures/SP-1500-Broch-APAC.pdf>
- **Truck parts (round 31):** typical (inferred from the device type, not from a source): mounts on [[Truck Controller and CAN Bus]]; connects to [[Truck Controller and CAN Bus]]; acts on [[Truck Controller and CAN Bus]], [[Truck Controls and Display]]. See [[Truck Part Connection Register]].

- **Architecture realization — operator access:** [[Operator Access Authorization Design]] is allocated because the product explicitly restricts truck use to authorized operators. [[Operator Access Authorization Logic]] is allocated at **>=95% engineering confidence** where the internal authorization software partition is unpublished. The exact credential database, controller, relay/CAN path, and synchronization method remain product-specific.

- **Architecture realization — pre-shift checklist:** published material explicitly describes electronic inspection checklists tied to truck access/lockout behavior, supporting [[Pre-Shift Checklist Enforcement Design]]. [[Pre-Shift Checklist Enforcement Logic]] is allocated at **>=95% engineering confidence** because the internal software partition is not published. [[Vehicle Enable Interlock]] captures the enforcement consequence when the checklist policy is not satisfied.

## Aliases

- InfoLink


## Former ids
