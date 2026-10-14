---
type: Info
subtype: research
id: INFO-00935
uid: 20261014124358188skellyspencer
status: Draft
tags:
  - research-note
  - traceability
describes:
  - "[[Product to Customer Need Map]]"
---

# Function-to-Need Gap Register

## Definition

Register of the product functions that still have no customer need linked, with the reason and the candidate need where one is plausible. Created 2026-10-14 after the first function-to-need pass.

## Notes

- **Method:** a function is linked to a need (Use Case, why) only when the need's own problem statement covers what the function does; links are analyst hypotheses, marked in each need note. A need is created only where vault sources state the customer problem or benefit; otherwise the function is listed here.
- **Result of the 2026-10-14 pass:** functions with a need 71 to 106 of 149; leaf functions (those that products perform) 71 to 106 of 123 (58% to 86%); commercial products that perform a need-linked function 307 to 344 of 484 (63% to 71%); products performing only unlinked functions 61 to 24; products with no function linked 116 (unchanged). One new need: [[Charge Without Anyone Plugging In]]; 31 links added to 11 existing needs.
- **Limit:** all 26 needs remain vendor-stated hypotheses; this pass raises link coverage, not customer evidence. Product counts in the need notes and in [[Product to Customer Need Map]] are not regenerated.

### Leaf functions still without a need

| Function | Reason | Candidate need or action |
|---|---|---|
| [[Charge Battery Conventionally]] | baseline charging; no customer problem stated in the sources | none |
| [[Circulate Electrolyte]] | limits acid stratification; no source ties it to a customer problem | source needed (maintenance labor or battery life) |
| [[Configure Device from Mobile App or PC]] | technician tooling; no problem statement | source needed (service effort) |
| [[Convert Traction Battery Voltage for Onboard Systems]] | supply for onboard systems; no problem statement | none |
| [[Cushion Fork Lowering]] | protects loads; no problem statement | candidate: handle loads without damage |
| [[Cut Power in an Emergency]] | emergency stop; no problem statement | candidate: keep the truck under control |
| [[Detect Battery Weight]] | checks battery-truck compatibility; no problem statement | candidate: fit the right battery to the truck |
| [[Detect Isolation Fault]] | high-voltage safety; not about connecting at the site | candidate: protect people from high-voltage faults |
| [[Float Charge Battery]] | baseline; no problem statement | none |
| [[Follow Operator Automatically]] | reduces operator effort; no problem statement | candidate: reduce operator physical effort |
| [[Hold Truck on Slope]] | prevents roll-back; no problem statement | candidate: keep the truck under control |
| [[Indicate Charger Status Locally]] | local light or display; existing needs are remote or battery-side | candidate: see charge status at the charger |
| [[Program Travel, Lift and Tilt Speeds]] | speed setting by operator or task; the speed need is zone-based | candidate: match truck behavior to operator and task |
| [[Reduce Speed When Seat Belt Is Unfastened]] | enforces belt use; the speed need is zone-based | candidate: enforce safe operator practice |
| [[Reduce Wheel Slip]] | traction control; no problem statement | candidate: keep the truck under control |
| [[Report Fuel Cell State to Truck]] | fuel-cell equivalent of battery state; battery-only needs | candidate: extend 'Know Battery State' to fuel cells |
| [[Steer with Electric Power Assist]] | reduces steering effort; no problem statement | candidate: reduce operator physical effort |

### Category functions (traced through their sub-functions, not a gap)

[[Charge Battery]], [[Communicate Battery and Vehicle Data]], [[Connect Battery Power Path]], [[Control Charge Profile]], [[Deliver Energy to Vehicles]], [[Hold or Stop Vehicle Automatically]], [[Inform Operator of Truck Condition]], [[Inform Users of Battery Condition]], [[Keep Charging Available and Safe]], [[Keep Equipment Working in Its Environment]], [[Know and Protect Battery Condition]], [[Limit Vehicle Speed Automatically]], [[Maintain Battery Electrolyte]], [[Maintain Vehicle Stability and Load Awareness]], [[Manage Fleet Use]], [[Manage Fleet Use and Data]], [[Operate in Harsh Conditions]], [[Protect Battery from Harm]], [[Protect People and Equipment Near Vehicles]], [[Reduce Operator Effort]], [[Sense Battery State]], [[Sense Collision Risk and Events]], [[Supply Vehicle Energy Without Charging]], [[Support Operator View and Positioning]], [[Support the Operator]], [[Warn People of Hazards]]

## Aliases

- Function Need Gaps

## Former ids
