---
type: Use Case
subtype: why
id: UC-00051
uid: 20261014131151819skellyspencer
status: Draft
tags:
  - customer-need
  - need-hypothesis
  - analyst-derived
realizedBy:
  - "[[Hold Truck on Slope]]"
  - "[[Reduce Wheel Slip]]"
  - "[[Cut Power in an Emergency]]"
  - "[[Program Travel, Lift and Tilt Speeds]]"
participants:
  - "[[Forklift Operator]]"
  - "[[Site Safety Manager]]"
needOf:
  - "[[Forklift Operator]]"
  - "[[Site Safety Manager]]"
---

# Keep the Truck Under Control on Slopes, Slippery Floors and in Emergencies

## Definition

Customer need: Keep the Truck Under Control on Slopes, Slippery Floors and in Emergencies. The problem behind it: a loaded truck can roll back on a ramp, spin or lock its wheels on a slick floor, or keep driving when something goes wrong, and the operator has to manage that by skill alone.

## Notes

- **Evidence status: need hypothesis, analyst-derived.** No vault source states this need as a customer problem. The need was reasoned from what the functions below do and from the work the customer is doing; the product statements are what makers say the features do. No customer, user or buyer source confirms the need or its rank.
- **Customer work this need protects or removes (analyst reasoning):** driving loaded across ramps, dock plates and wet or dusty floors, stopping and parking on a grade, and responding to a fault or a person at risk. Candidate operational Use Cases: Park or Stop on a Ramp, Drive on a Slippery Floor, Stop the Truck in an Emergency. The functions remove the case where the operator must hold the truck by foot control, or lose control before stopping.
- **Problem solved (analyst wording):** the functions take over the moments the operator cannot manage by feel (hold on a slope, limit wheel spin, cut drive power at once, and set speeds to the operator and task).
- **Who has the problem:** [[Forklift Operator]], [[Site Safety Manager]].
- **Realized by (specific functions; products link to these):** [[Hold Truck on Slope]], [[Reduce Wheel Slip]], [[Cut Power in an Emergency]], [[Program Travel, Lift and Tilt Speeds]].
- **Product-stated evidence:**
  - [[Doosan Bobcat 7-Series Plus Electric Forklifts]] and [[Doosan Bobcat NXE Series Electric Forklifts]]: Hold Truck on Slope. Source: <https://www.directindustry.com/prod/doosan-industrial-vehicles/product-26467-2856186.html> (V), <https://www.directindustry.com/prod/doosan-industrial-vehicles/product-26467-2856190.html> (V).
  - [[Crown RR-RD 5700 Series]]: OnTrac anti-slip traction control reduces tire spin during acceleration, plugging and braking. Source: <https://www.crown.com/en-au/forklifts/reach-trucks/rr-rd-rider-deep-reach-truck.html> (V).
  - [[Hangcha XC Series Electric Forklifts]]: emergency cut-off. Source: <https://www.summithandling.com/summit-product/hangcha-xc-series-mid-electric-outdoor-lithium-ion-forklift/> (V).
  - [[Heli G Series Lithium Forklifts]] and [[Komatsu FB Series Electric Forklifts]]: selectable travel, lift and tilt speeds. Source: <https://www.liftstoday.com/listing/for-sale/259364865/2026-heli-cpd15-pneumatic-tire-forklifts?print=1> (V), <https://www.komatsu.com/en-au/products/equipment/forklifts/standard-electric-powered/komatsu-fb> (V).
  - Hazard context: [[Document - OSHA Summaries of Selected Forklift Fatalities (retrieved 2026-10-14)]] describes an unloaded forklift that tipped on a 13 percent ramp slope; the page gives no rates.
- **Gaps:** no customer or buyer source; no source says how often rollback, wheel slip or runaway events happen in electric fleets; the speed-setting function is the weakest fit and could belong with [[Prevent Tip-Overs and Overloads]]; no Requirement is linked.

## Operational traceability

- Operational Use Cases: none yet; the operational Use Cases in the 40_Use and Operations folder cover charging and fleet-data work, not driving or load handling. Candidate operational Use Cases are named in the work line above.

## Former ids
