---
type: Use Case
subtype: what
id: UC-00055
uid: 20261014152245690skellyspencer
status: Draft
tags:
  - operational-use-case
  - operational-hypothesis
participants:
  - "[[Fleet Operations Manager]]"
realizedBy:
  - "[[Schedule Charging Around Vehicle Readiness]]"
givesRiseTo:
  - "[[Return Trucks to Service Quickly After a Low Charge]]"
  - "[[Monitor and Manage Chargers and Batteries Across Sites]]"
---

# Schedule Charging for the Next Shift

## Definition

Before a shift or a break, a fleet manager sets when each charger runs, which trucks charge first and when each truck must be ready, so that trucks leave the charger charged when they are needed.

## Notes

- **Evidence status: analyst hypothesis, drafted 2026-10-14.** The steps are not an observed customer procedure; they are reasoned from vendor descriptions of the functions. Most vendor sources are EV or robot fleet software; no source read shows a forklift fleet doing this. Please correct with real workflow.
- Primary context: [[Distributed and Opportunity Charging Area]].
- Steps (analyst wording): see which trucks and batteries will be needed and when; set charging priority and ready times; confirm the schedule against what chargers are free; adjust when a truck comes in early or late.
- Completion: every truck needed in the next shift has a charge slot that meets its ready time.
- Vendor descriptions behind the steps: scheduling around schedules and priorities ([[Siemens depotfinity]]), a charging scheduler ([[PowerFlex X]]), assignment to chargers by readiness ([[Ampcontrol Yard Management for Electric Vehicles]]), battery priority and availability ([[Exide GNB Fleet]]).

## Traceability

- Source needs: [[Return Trucks to Service Quickly After a Low Charge]], [[Monitor and Manage Chargers and Batteries Across Sites]].

## Former ids
