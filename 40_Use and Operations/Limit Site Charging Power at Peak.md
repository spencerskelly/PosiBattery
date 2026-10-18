---
type: Use Case
subtype: what
id: UC-00056
uid: 20261014152245714skellyspencer
status: Draft
tags:
  - operational-use-case
  - operational-hypothesis
participants:
  - "[[Fleet Operations Manager]]"
realizedBy:
  - "[[Balance Charging Power Across Site Capacity]]"
givesRiseTo:
  - "[[Charge Within Site Power Limits and Utility Costs]]"
arisesIn:
  - "[[Material-Handling Fleet Site]]"
---

# Limit Site Charging Power at Peak

## Definition

A fleet manager sets a maximum charging power for the site or a charger group and a priority among trucks, so charging stays under the site supply or avoids a peak-rate window.

## Notes

- **Evidence status: analyst hypothesis, drafted 2026-10-14.** The steps are not an observed customer procedure; they are reasoned from vendor descriptions of the functions. The sources are vendor statements; no customer procedure or savings figure was read. Please correct with real workflow.
- Primary context: [[Material-Handling Fleet Site]].
- Steps (analyst wording): find the site power limit or the peak-rate window; set a total power limit for a group of chargers; set which trucks charge first; check the dashboard that trucks are still ready; change the limit or schedule when shifts change.
- Completion: simultaneous charging stays within the limit and the trucks needed are ready.
- Vendor descriptions behind the steps: [[Linde connect charger]], [[Jungheinrich Active Load Management]], [[Toyota Peak Load Management]], [[Crown V-HFM3 Charger]] (Demand Response Management), [[Fronius PV Connect]], [[ACT ACTenergy]], and the EV software [[Flip Turn Energy Management]], [[PowerFlex X]] and [[Siemens depotfinity]]. See [[Forklift Charger Load Management Register]].

## Traceability

- Source needs: [[Charge Within Site Power Limits and Utility Costs]].

## Former ids
