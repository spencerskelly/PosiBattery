---
type: Use Case
subtype: why
id: UC-00043
uid: 20261013210000018skellyspencer
status: Draft
tags:
  - customer-need
  - need-hypothesis
  - vendor-stated
describedBy:
  - "[[Document - MMH Lithium-Ion Batteries Help Trim Fleet by a Third (Standard Distributing)]]"
realizedBy:
  - "[[Report Truck Telemetry]]"
  - "[[Size Battery and Charger Fleet]]"
  - "[[Dispatch Vehicles to Tasks]]"
  - "[[Report Truck Hours and Usage]]"
participants:
  - "[[Fleet Operations Manager]]"
needOf:
  - "[[Fleet Operations Manager]]"
arisesIn:
  - "[[Review Fleet Utilization and Idle Capacity]]"
---

# Right-Size the Fleet from Usage Data

## Definition

Customer need: Right-Size the Fleet from Usage Data. The problem behind it: A manager needs to know which trucks are idle, which are overused and when peaks occur, to decide whether to rent, buy or reallocate trucks and how to staff shifts.

## Notes

- **Customer-side evidence added 2026-10-14 (priority 6):** the distributor cut its fleet from 17 to 12 trucks after switching to lithium-ion ([[Document - MMH Lithium-Ion Batteries Help Trim Fleet by a Third (Standard Distributing)]], T2, one site, vendor-supplied); the page does not say the cut came from usage data, so it does not support this need directly.
- **Added 2026-10-14 (telemetry split, analyst reasoning):** [[Report Truck Hours and Usage]] realizes this need for the three products whose sources state hours or usage; [[Report Truck Telemetry]] stays for products whose sources state only generic fleet monitoring.
- **Added 2026-10-14 (software pass, analyst reasoning):** [[Dispatch Vehicles to Tasks]]: analyst reasoning: dispatch by availability raises utilization, which is the usage the need looks at (OTTO claims lower idle time; FleetRabbit claims 15 to 20 percent less empty travel, no method).
- **Evidence status: need hypothesis.** The statements below are what makers, dealers and trade press say fleet managers do or want. At most one named customer source supports any need; none ranks it. Per the ruleset, source research becomes a validated need only after customer-side evidence. Full evidence is in [[Fleet Manager and Admin Digital Access Evidence]].
- **Problem solved (analyst wording):** A manager needs to know which trucks are idle, which are overused and when peaks occur, to decide whether to rent, buy or reallocate trucks and how to staff shifts.
- **Who has the problem:** [[Fleet Operations Manager]].
- **Realized by (specific functions; products link to these):** [[Report Truck Telemetry]].
- **Update 2026-10-14 (analyst links, hypothesis):** added realizing functions [[Size Battery and Charger Fleet]] - rationale: working out battery and charger quantities from operating data. Product counts above predate these links and are not regenerated.
- **Evidence (by source):**
  - F1: the Chicago Tribune Freedom Center's receiving team lead says utilization data for trucks and operators informs production and staffing decisions: 'That information is vital for [us] to make decisions about the future.' Customer statement reported by a trade-press article about Crown InfoLink (T2, 2021). [[Document - MMH Turning Fleet Data into Savings (Chicago Tribune and Crown InfoLink)]]
  - F2: Raymond lists 'Equipment and Operator Utilization' with hour meters (login, travel, lift, deadman) and a Utilization Dashboard (heading only). (T1) [[Document - Raymond iWAREHOUSE Reporting and Analytics (retrieved 2026-10-13)]]
  - F3: Toyota says managers monitor peak hours to raise utilization and cut idle time, and check whether the fleet has the right number of machines. (T1) [[Document - Toyota I_Site Fleet Management Page (retrieved 2026-10-13)]]
  - F4: Linde says reports on operating hours let a manager 'identify free capacity'. (T1) [[Document - Linde connect desk Fleet Management Page (retrieved 2026-10-13)]]
  - F12: a Crown column advises monitoring which trucks are in use or idle, then renting, buying or reallocating, and planning peak seasons by facility. Vendor-authored. (T2) [[Document - MMH Crown Other Voices Five Steps to a Healthier Forklift Fleet (2020-02-27)]]
- **Gaps:** one named customer statement (F1); the rest is vendor-stated. No source gives a utilization target or the data a manager would need beyond hours. How many fleets actually change fleet size from this data is not stated.
- **Products reaching this need:** 44 by function, design or option (owner decision, round 40: design and option routes count as reached); 30 of those perform a realizing function. Largest families by function: Fleet Software and Platforms/Truck Telematics (21), Fleet Software and Platforms (5), Vehicle Accessories/Proximity and Object Detection (2), Fleet Software and Platforms/Battery and Charger Management (1). The metric route (hypothesis, carried over) adds 0 more. Per-product routes in [[Product to Customer Need Map]]. Recounted 2026-10-14.

## Aliases


## Former ids
