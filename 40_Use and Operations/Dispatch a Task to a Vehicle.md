---
type: Use Case
subtype: what
id: UC-00057
uid: 20261014152245729skellyspencer
status: Draft
tags:
  - operational-use-case
  - operational-hypothesis
participants:
  - "[[Fleet Operations Manager]]"
realizedBy:
  - "[[Dispatch Vehicles to Tasks]]"
  - "[[Exchange Vehicle and Order Data with Warehouse System]]"
givesRiseTo:
  - "[[Right-Size the Fleet from Usage Data]]"
  - "[[Act on Fleet Data Without Information Overload]]"
arisesIn:
  - "[[Material-Handling Fleet Site]]"
---

# Dispatch a Task to a Vehicle

## Definition

A fleet manager or warehouse system sends a move or pick task to the vehicle best placed to do it, using vehicle position and availability, and receives status back.

## Notes

- **Evidence status: analyst hypothesis, drafted 2026-10-14.** The steps are not an observed customer procedure; they are reasoned from vendor descriptions of the functions. Robot fleets are far better evidenced than manually driven forklift fleets here. Please correct with real workflow.
- Primary context: [[Material-Handling Fleet Site]].
- Steps (analyst wording): a task arrives from the warehouse system or a person; the fleet software chooses a vehicle by location and availability; the task goes to the vehicle; status returns to the warehouse system.
- Completion: the task is assigned and its status is visible to the warehouse system.
- Vendor descriptions behind the steps: robot fleet software ([[Seegrid Fleet Central]], [[OTTO Fleet Manager]], [[MiR Fleet]]) and a vendor article on forklift telematics feeding a WMS ([[FleetRabbit]], T3). Whether battery state is a factor in choosing a vehicle is stated by OTTO's dealer page, not by MiR.

## Traceability

- Source needs: [[Right-Size the Fleet from Usage Data]], [[Act on Fleet Data Without Information Overload]].

## Former ids
