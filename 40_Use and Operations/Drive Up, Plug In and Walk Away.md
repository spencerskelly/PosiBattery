---
type: Use Case
subtype: what
id: UC-00061
uid: 20261014175657858skellyspencer
status: Draft
tags:
  - operational-use-case
  - owner-stated
participants:
  - "[[Forklift Operator]]"
  - "[[GSE Operator]]"
realizedBy:
  - "[[Connect Battery to Charger or Vehicle]]"
  - "[[Avoid Arcing at the Charge Connection]]"
  - "[[Start and Stop Charge from an External Control]]"
givesRiseTo:
  - "[[Connect Chargers and Batteries Safely at the Site]]"
  - "[[Return Trucks to Service Quickly After a Low Charge]]"
---

# Drive Up, Plug In and Walk Away

## Definition

The operator drives the vehicle up to a charger, plugs in and leaves, and the charge runs without the operator staying. At some sites the operator must also press a start button when plugging in and a stop button when the charge ends.

## Notes

- **Evidence status: owner statement (2026-10-14, U).** The owner (PosiCharge engineering) described this as 'the general use case': drive up, plug in, walk away; some sites require a start and stop button to be pushed at the beginning and end of the charge. It is a first-hand account, not a documented customer procedure, and it names no site, customer or share of sites.
- Primary contexts: [[Distributed and Opportunity Charging Area]] and [[Centralized Battery Room and Charging Area]] (the owner said 'general'; no split by context was given).
- Steps (owner wording): drive up; plug in; walk away. Variant at some sites: press start after plugging in; press stop when the charge ends.
- Completion: the vehicle is connected and charging without the operator attending.
- **Origin of the button step (owner statement 2026-10-14, U):** old chargers used to spark when connected if they were not turned off, and the start and stop button remained as a practice even though the owner's chargers now stop charge automatically. So at those sites the button is a legacy habit, not a feature the current charger needs.
- **Supporting evidence read:** a 2014 safety meeting topic in the vault says 'charger off before connecting or disconnecting' ([[Document - Safety Meeting Topic Forklift Battery Use and Maintenance (2014)]], T4); PosiCharge's SVS100 page lists 'automatic start/stop' and 'anti-arcing disconnect' ([[PosiCharge SVS100]], T1); Fronius says its Selectiva 4.0 range offers 'external start/stop to increase user safety' (flyer, T1). Whether other makers' chargers still spark on connection is not shown (C275).
- **What the variant means for the vault:** the button variant is now modeled by [[Start and Stop Charge from an External Control]] and the underlying hazard by [[Avoid Arcing at the Charge Connection]] (both added 2026-10-14, one performer each). [[Start and Stop Charge Automatically]] covers a different case (no plugging or unplugging). No Design is written for either, because no source states the mechanism (IB-239). The need links below are analyst reasoning from the connection step; the owner did not name the needs.

## Traceability

- Source needs: [[Connect Chargers and Batteries Safely at the Site]], [[Return Trucks to Service Quickly After a Low Charge]] (analyst-linked).
- Operating contexts: [[Distributed and Opportunity Charging Area]], [[Centralized Battery Room and Charging Area]].

## Former ids
