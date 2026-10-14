---
type: Use Case
subtype: why
id: UC-00013
uid: 20261003215631077skellyspencer
status: Draft
tags:
  - customer-need
  - need-hypothesis
  - vendor-stated
realizedBy:
  - "[[Slow Truck in Curves]]"
  - "[[Adapt Speed to Load and Lift Height]]"
  - "[[Restrict Lift When Load Exceeds Limit]]"
  - "[[Stabilize Truck Dynamically]]"
  - "[[Cut Lift at Programmed Height]]"
  - "[[Sense Load Weight and Lift Height]]"
  - "[[Damp Mast Oscillation]]"
  - "[[Detect Battery Weight]]"
  - "[[Reduce Speed When Seat Belt Is Unfastened]]"
participants:
  - "[[Forklift Operator]]"
  - "[[Site Safety Manager]]"
needOf:
  - "[[Forklift Operator]]"
  - "[[Site Safety Manager]]"
---

# Prevent Tip-Overs and Overloads

## Definition

Customer need: Prevent Tip-Overs and Overloads. The problem behind it: Cornering too fast, or lifting too high or too heavy, tips trucks and drops loads.

## Notes

- **Added 2026-10-14 (analyst reasoning):** [[Reduce Speed When Seat Belt Is Unfastened]]: OSHA case summaries show seat belts unused in forklift overturn deaths, including a 1998 ramp tip-over ([[Document - OSHA Summaries of Selected Forklift Fatalities (retrieved 2026-10-14)]], T1, second-hand). STILL says its seat belt control reduces speed if the belt is not used (source: [[STILL EasyBelt]]). Analyst reasoning: the feature removes the case where an operator drives without a belt. Customer work: driving the truck.
- **Added 2026-10-14 (analyst reasoning):** [[Detect Battery Weight]]: Raymond says the iBattery module detects battery weight against truck specifications (source: [[Raymond iBattery]]). Analyst reasoning: on a counterbalanced truck the battery is part of the counterweight, so a wrong-weight battery is a stability risk; no vault source states this. Customer work: changing or installing a battery in a truck.
- **Evidence status: need hypothesis.** The statements below are what makers and dealers say their products do for customers. No customer, user or buyer source in the vault confirms that customers hold this need or rank it. Per the ruleset, source research becomes a validated need only after customer-side evidence.
- **Problem solved (analyst wording):** Cornering too fast, or lifting too high or too heavy, tips trucks and drops loads.
- **Who has the problem:** [[Forklift Operator]], [[Site Safety Manager]].
- **Operating segments (analyst crosswalk to [[PosiCharge Market Segments and Jobs-to-Be-Done]], hypothesis):** Material-handling fleets.
- **Realized by (specific functions; products link to these):** [[Slow Truck in Curves]], [[Adapt Speed to Load and Lift Height]], [[Restrict Lift When Load Exceeds Limit]], [[Stabilize Truck Dynamically]].
- **Update 2026-10-14 (analyst links, hypothesis):** added realizing functions [[Cut Lift at Programmed Height]], [[Sense Load Weight and Lift Height]], [[Damp Mast Oscillation]] - rationale: limiting lift height, showing load limits and damping mast swing. Product counts above predate these links and are not regenerated.
- **Products reaching this need:** 25 by function, design or option (owner decision, round 40: design and option routes count as reached); 19 of those perform a realizing function. Largest families by function: Vehicle Accessories/Operator Assist and Stability (12), Forklifts/Class I Electric Rider Trucks (5), Vehicle Accessories/Proximity and Object Detection (1), Forklifts/Class II Electric Narrow Aisle Trucks (1). The metric route (hypothesis) adds 0 more. Per-product routes in [[Product to Customer Need Map]].
- **Vendor-stated evidence (by product):**
  - [[STILL Curve Speed Control]]: STILL says Curve Speed Control regulates driving speed automatically according to the steering angle, is available on various forklift trucks and warehouse devices (standard on the EXH-SF 16C/20C), and addresses tipping accidents whose frequent cause is excessive cornering speed. Source: STILL pages and 2021 STILL release (T1/T2), retrieved 2026-10-03. <https://www.still.co.uk/company/news-press/news/detail/safe-safer-still.html>
  - [[Jungheinrich curveCONTROL]]: Jungheinrich says curveCONTROL improves forklift stability by automatically reducing cornering speed when necessary. Source: Jungheinrich safety page (T1), retrieved 2026-10-03. <https://www.jungheinrich.ch/about-us/stories/safety-549042>
  - [[Yale Reliant Portfolio]]: The Yale white paper (Reference Files/133294183726805278.pdf) lists operator assist capabilities: overload arrest, automatic speed reduction when cornering, keeping equipment out of designated pedestrian-only zones, line-of-sight support and location-based fork height restriction to avoid low beams. Source: Yale operator assist white paper (read round 20) (T1), retrieved 2026-10-03. <https://og.mhi.org/media/members/14259/133294183726805278.pdf>
- **Independent evidence that the problem exists (not that the product is wanted):**
  - OSHA Region I Local Emphasis Program directive for powered industrial trucks (Oct 2016, FY2018 copy, dated) (G, US government): repeats that there are roughly 85 forklift fatalities, 34,900 serious injuries and 97,185 accidents each year, with 42 percent of fatalities from operators crushed by a tipping vehicle; the directive does not name its own underlying source in the retrieved text. Retrieved 2026-10-03. <https://www.osha.gov/sites/default/files/enforcement/directives/reg1_fy2018_cpl-04-00-023e_powered-industrial-trucks_1.pdf>
  - BLS fact sheet 'Occupational Injuries, Illnesses, and Fatalities Involving Forklifts' (June 2019, 2017 data, dated) (G, US government statistics): 614 workers died in forklift-related incidents from 2011 to 2017; of 74 fatal forklift injuries in 2017, 9 were pedestrian vehicular incidents; of 9,050 nonfatal cases with days away from work in 2017, 1,850 involved pedestrians while the forklift was in transportation use, and those pedestrian cases had the highest median days away (20). Retrieved 2026-10-03. <https://www.bls.gov/iif/factsheets/fatal-occupational-injuries-forklifts-2017.htm>
  - Secondary pages repeat different fatality and injury figures; see conflicts C101 to C104 in [[Battery Product Landscape Conflicts and Open Questions]]. Only the government sources above are used here.
- **Gaps:** no customer-side source; each function in the list is realized by only the products that state it, so the product count is a lower bound; no Requirement is linked (the vault leaves requirements as an intentional gap).

## Aliases


## Former ids
