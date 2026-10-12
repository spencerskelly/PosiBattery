---
type: Function
subtype:
id: FUNC-00093
uid: 20261003152905094skellyspencer
status: Draft
tags:
  - accessory-function
  - product-function
subtypeOf:
  - "[[Manage Fleet Use]]"
dependsOn:
  - "[[Display Device Design]]"
  - "[[Pre-Shift Checklist Enforcement Design]]"
performedBy:
  - "[[Crown InfoLink]]"
  - "[[Hyster Tracker Telemetry]]"
  - "[[Jungheinrich ISM Online]]"
  - "[[Logisnext Lift Link]]"
  - "[[Powerfleet Forklift Gateway]]"
  - "[[STILL RX 60 Electric Forklift]]"
  - "[[STILL Safety Assist]]"
  - "[[Crown InfoLink 7-inch Touch Display]]"
  - "[[Pre-Shift Checklist Enforcement Logic]]"
realizes:
  - "[[Control Who Operates Each Truck]]"
  - "[[Authenticate and Complete Pre-Shift Authorization]]"
realizedBy:
  - "[[Pre-Shift Checklist Enforcement Design]]"
---

# Enforce Pre-Shift Checklist

## Definition

Require the operator to complete a vehicle inspection checklist before the truck can be used.

## Notes

- Behavior found in product descriptions. Product links only where a source states the behavior.
- No Requirement is linked (intentional gap).
- **Sources** (product, evidence level, web page):
  - [[Jungheinrich ISM Online]] (V): <https://www.industrial-production.de/wirtschaft---unternehmen/jungheinrich-verbessert-staplermanagement--neue-moeglichkeiten.htm>
  - [[Logisnext Lift Link]] (V): <https://www.mhlnews.com/new-products/article/21271747/forklift-telematics-solution>
  - [[Powerfleet Forklift Gateway]] (V): <https://www.globenewswire.com/news-release/2021/06/01/2239918/8494/en/Mitsubishi-Logisnext-Americas-Launches-Advanced-PowerFleet-Telematics-Solution-For-North-American-Market.html>
  - [[Crown InfoLink]] (V): <https://crown.com/content/dam/crown/pdfs/apac/brochures/SP-1500-Broch-APAC.pdf>
  - [[Hyster Tracker Telemetry]] (V): <https://www.hyster.com/globalassets/coms/hyster/north-america/documents/trucks/0000hbxxbc001_e_en-us_hyster-solutions-brochure-view.pdf>
  - [[STILL RX 60 Electric Forklift]] (V): <https://aviationspares.com/rx-60-25-35-t-electric-forklift-truck/>
  - [[STILL Safety Assist]] (V): <https://www.still.co.uk/forklift-trucks/driver-assistance/safety-assist.html>
  - [[Crown InfoLink 7-inch Touch Display]] (V): <https://www.crown.com/en-us/fleet-management/infolink.html>

## Implementation Allocation

The reusable realization is [[Pre-Shift Checklist Enforcement Design]] -> [[Pre-Shift Checklist Enforcement Logic]].

The implementation separates three roles:

- [[Display Device Design]] presents the checklist and captures operator responses.
- [[Pre-Shift Checklist Enforcement Logic]] evaluates completion, defects, blocking rules, and authorization state.
- [[Vehicle Enable Interlock]] prevents truck operation when the checklist is incomplete or contains a blocking condition.

A display alone does not enforce the checklist; enforcement requires both decision logic and a vehicle-use consequence.

[[Crown InfoLink]] and [[Crown InfoLink 7-inch Touch Display]] provide the clearest currently modeled example of the full workflow. Other fleet-management products remain valid Function performers even where the exact lockout/software partition is unpublished.

## Aliases


## Former ids
