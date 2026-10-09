---
type: Object
subtype: software
id: OBJ-00166
uid: 20261003084359646skellyspencer
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
madeBy:
  - "[[Hyster-Yale]]"
offeredWith:
  - "[[Hyster Power Cellect]]"
hasDesign:
  - "[[Truck Telemetry Reporting Design]]"
hasPart:
  - "[[Truck Telemetry Acquisition Logic]]"
  - "[[Truck Telemetry Reporting Service]]"
  - "[[Hyster Power Cellect]]"
---

# Hyster Tracker Telemetry

## Definition

Hyster forklift telemetry for wireless fleet management, compatible with all Hyster models and competitive units.

## Notes

- Hyster's brochure says Hyster Tracker is compatible with all Hyster models and competitive units, and the wireless monitoring base level is standard on all A Series models. Source: Hyster solutions brochure (T1), retrieved 2026-10-03. <https://www.hyster.com/globalassets/coms/hyster/north-america/documents/trucks/0000hbxxbc001_e_en-us_hyster-solutions-brochure-view.pdf>
- **Conflict-visible (C60):** earlier notes treated 'Hyster Tracker' as the battery monitor [[Hyster Battery Tracker]] (powered by PosiCharge technology). This brochure describes Hyster Tracker as truck telemetry. They may be separate products with similar names.
- **Functions performed, with citations:**
  - [[Report Truck Telemetry]] (V): <https://www.hyster.com/globalassets/coms/hyster/north-america/documents/trucks/0000hbxxbc001_e_en-us_hyster-solutions-brochure-view.pdf>
- The Hyster solutions brochure (Downloads/0000hbxxbc001_e_en-us_hyster-solutions-brochure-view.pdf) says Hyster Tracker gives real-time telemetry, usage metrics, OSHA pre-shift checklist, restricting truck access to approved operators, operator training updates and impact detection, lockouts and alerts, with options named 'Battery vision' (monitor battery usage and alert users) and 'Load sensing'. Source: Hyster solutions brochure (read round 20) (T1), retrieved 2026-10-03. <https://www.hyster.com/globalassets/coms/hyster/north-america/documents/trucks/0000hbxxbc001_e_en-us_hyster-solutions-brochure-view.pdf>
- **C60 update (round 20):** Hyster's own brochure calls the battery option 'Battery vision', not 'Battery Tracker'; Yale's counterpart is Yale Battery Vision. See [[Hyster Battery Tracker]].
- **Functions performed, with citations:**
  - [[Control Operator Access]] (V): <https://www.hyster.com/globalassets/coms/hyster/north-america/documents/trucks/0000hbxxbc001_e_en-us_hyster-solutions-brochure-view.pdf>
  - [[Detect and Record Impacts]] (V): <https://www.hyster.com/globalassets/coms/hyster/north-america/documents/trucks/0000hbxxbc001_e_en-us_hyster-solutions-brochure-view.pdf>
  - [[Enforce Pre-Shift Checklist]] (V): <https://www.hyster.com/globalassets/coms/hyster/north-america/documents/trucks/0000hbxxbc001_e_en-us_hyster-solutions-brochure-view.pdf>
- **Truck parts (round 31):** typical (inferred from the device type, not from a source): mounts on [[Truck Controller and CAN Bus]]; connects to [[Truck Controller and CAN Bus]]; acts on [[Truck Controller and CAN Bus]], [[Truck Controls and Display]]. See [[Truck Part Connection Register]].

- **Architecture realization — truck telemetry:** published behavior establishes vehicle operating data and event reporting to a fleet-management system, supporting [[Truck Telemetry Reporting Design]]. [[Truck Telemetry Acquisition Logic]] and [[Truck Telemetry Reporting Service]] are allocated at **>=95% engineering confidence** where the vendor does not publish the internal software partition. Exact signal sources, CAN/J1939 mapping, buffering, wireless transport, and cloud protocol remain product-specific.

## Aliases

- Hyster Tracker


## Former ids
