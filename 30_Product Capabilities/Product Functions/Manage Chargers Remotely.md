---
type: Function
subtype:
id: FUNC-00035
uid: 20261002193402990skellyspencer
status: Draft
tags:
  - charger
  - extra
  - product-function
subtypeOf:
  - "[[Manage Fleet Use]]"
describedBy:
  - "[[Metric - Communication and Remote Management]]"
performedBy:
  - "[[ACT Quantum 2]]"
  - "[[ACT Quantum 3]]"
  - "[[ACT Quantum Outdoor]]"
  - "[[Crown V-HFM3 Charger]]"
  - "[[Fronius Selectiva 4.0]]"
  - "[[Lester Summit Series II]]"
  - "[[ACT ACTview]]"
  - "[[PosiCharge SkyLink]]"
  - "[[Remote Charger Management Service]]"
  - "[[Charger Remote Management Agent]]"
realizes:
  - "[[Monitor and Manage Chargers and Batteries Across Sites]]"
dependsOn:
  - "[[Remote Charger Management Design]]"
realizedBy:
  - "[[Remote Charger Management Design]]"
---

# Manage Chargers Remotely

## Definition

Configure, monitor or update chargers from a remote portal or app.

## Notes

- Charger-side or charger-and-battery behavior found in product descriptions. Links to products are made only where a source states the behavior; no link means unknown.
- No Requirement is linked (intentional gap).
- **Sources** (product, evidence level, web page):
  - [[Crown V-HFM3 Charger]] (V): <https://www.crown.com/en-au/batteries-and-chargers/vhfm3-charger.html>
  - [[ACT Quantum 2]] (V): <https://og.mhi.org/media/members/41607/133717591610794845.pdf>
  - [[ACT Quantum 3]] (V): <https://og.mhi.org/media/members/41607/133717589840217692.pdf>
  - [[ACT Quantum Outdoor]] (V): <https://og.mhi.org/media/members/41607/133717591287578074.pdf>
  - [[Fronius Selectiva 4.0]] (V): <https://fronius.com/~/downloads/Perfect%20Charging/Flyer/PC_FLY_Selectiva_4.0_96V-120V_EN_fin-MRM_.pdf>
  - [[Lester Summit Series II]] (V): <https://voltloop.ca/products/summit-series-ii-charger-1050w-24v-36v-48v>
  - [[PosiCharge SkyLink]] (V): <https://posicharge.com/products/skylink/>
  - [[ACT ACTview]] (V): <https://og.mhi.org/media/members/41607/133717591610794845.pdf>
- **Extra (round 30):** documented for 5 of 18 charger maker groups (28 percent); the reusable realization is now [[Remote Charger Management Design]].

## Implementation Allocation

The reusable realization is [[Remote Charger Management Design]].

### Remote service side

[[Remote Charger Management Service]] represents the portal or application that exposes charger status and authorized management actions such as settings changes, firmware updates, diagnostics, troubleshooting, or other remote service operations.

### Charger side

[[Charger Remote Management Agent]] represents the charger-side software/firmware endpoint that validates and applies approved remote actions while preserving local safety ownership.

### Evidence boundary

Passive telemetry alone is not enough to satisfy this Function. The modeled products are retained because their source material describes remote management, update, configuration, or troubleshooting behavior rather than only status reporting.

[[ACT ACTview]] and [[PosiCharge SkyLink]] are clear service-side examples. The charger products use the generic Design; charger-side agent allocation is an **>=95% engineering-confidence abstraction** where remote management is explicit but the internal software partition is not published.

## Aliases


## Former ids
