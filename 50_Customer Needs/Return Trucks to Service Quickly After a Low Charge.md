---
type: Use Case
subtype: why
id: UC-00003
uid: 20261003215631067skellyspencer
status: Draft
tags:
  - customer-need
  - need-hypothesis
  - vendor-stated
realizedBy:
  - "[[Charge Battery Fast]]"
  - "[[Charge Battery by Opportunity]]"
  - "[[Change Battery Quickly]]"
  - "[[Refuel Truck Power Source in Minutes]]"
  - "[[Manage Temperature During Fast Charging]]"
  - "[[Guide Battery Selection and Rotation]]"
  - "[[Exchange Battery Automatically]]"
  - "[[Schedule Charging Around Vehicle Readiness]]"
participants:
  - "[[Fleet Operations Manager]]"
  - "[[Forklift Operator]]"
needOf:
  - "[[Fleet Operations Manager]]"
  - "[[Forklift Operator]]"
---

# Return Trucks to Service Quickly After a Low Charge

## Definition

Customer need: Return Trucks to Service Quickly After a Low Charge. The problem behind it: A truck waiting on a charge, or a battery swap, is a truck not working during the shift.

## Notes

- **Added 2026-10-14 (software pass, analyst reasoning):** [[Schedule Charging Around Vehicle Readiness]]: analyst reasoning: the vehicle is charged before its work needs it (Ampcontrol claims lower idle time; no figures).
- **Evidence status: need hypothesis.** The statements below are what makers and dealers say their products do for customers. No customer, user or buyer source in the vault confirms that customers hold this need or rank it. Per the ruleset, source research becomes a validated need only after customer-side evidence.
- **Problem solved (analyst wording):** A truck waiting on a charge, or a battery swap, is a truck not working during the shift.
- **Who has the problem:** [[Fleet Operations Manager]], [[Forklift Operator]].
- **Operating segments (analyst crosswalk to [[PosiCharge Market Segments and Jobs-to-Be-Done]], hypothesis):** Material-handling fleets, Airport eGSE fleets, Distributed and opportunity charging.
- **Realized by (specific functions; products link to these):** [[Charge Battery Fast]], [[Charge Battery by Opportunity]], [[Change Battery Quickly]], [[Refuel Truck Power Source in Minutes]], [[Manage Temperature During Fast Charging]] (added 2026-10-04).
- **Update 2026-10-14 (analyst links, hypothesis):** added realizing functions [[Guide Battery Selection and Rotation]], [[Exchange Battery Automatically]] - rationale: choosing the next ready battery and swapping it without waiting. Product counts above predate these links and are not regenerated.
- **Products reaching this need:** 82 by function, design or option (owner decision, round 40: design and option routes count as reached); 63 of those perform a realizing function. Largest families by function: Chargers/Industrial Modular Chargers (21), Batteries/Lithium-Ion Batteries (9), Batteries/Flooded Lead-Acid Batteries (7), Fleet Software and Platforms (6). The metric route (hypothesis, carried over) adds 6 more. Per-product routes in [[Product to Customer Need Map]]. Recounted 2026-10-14.
- **Vendor-stated evidence (by product):**
  - [[Yale ERC080VHL]]: Yale says the ERC080VHL is designed around an integrated lithium-ion pack with greater operator space, zero emissions, no battery maintenance, full power until depletion and fast charging, for heavy-duty indoor use or converting internal combustion fleets, with Yale Vision telemetry. Source: Yale ERC080VHL page (T1), retrieved 2026-10-03. <https://www.yale.com/en-us/north-america/lithium-ion-forklifts/erc080vhl/>
  - [[EnerSys NexSys AIR Wireless Charger]]: The brochure says NexSys AIR wireless chargers can charge multiple battery technologies including flooded lead-acid, are compatible with all EnerSys battery technologies, and can reduce AGV waiting time for charging. Source: EnerSys NexSys AIR brochure (T1), retrieved 2026-10-02. <https://www.enersys.com/493367/globalassets/documents/product-documentation/_enersys/apac/apac_en-imp-nex-com-air-0623.pdf>
  - [[Deka Dominator Battery]]: Correction: East Penn's forklift products page describes Dominator as a maintenance-free gel design to save maintenance hours, designed for conventional and opportunity charging, spillproof and leakproof. Source: East Penn forklift products page (T1), retrieved 2026-10-02. <https://www.eastpennmanufacturing.com/forklift-products/>
- **Gaps:** no customer-side source; each function in the list is realized by only the products that state it, so the product count is a lower bound; no Requirement is linked (the vault leaves requirements as an intentional gap).

## Operational traceability

- Operational Use Cases: [[Connect a Vehicle or Battery to a Charger]], [[Opportunity-Charge a Vehicle During a Work Break]].
- Operating contexts: [[Distributed and Opportunity Charging Area]].

## Aliases


## Former ids
