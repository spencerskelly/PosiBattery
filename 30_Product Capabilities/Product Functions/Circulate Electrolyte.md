---
type: Function
subtype:
id: FUNC-00065
uid: 20261003101711510skellyspencer
status: Draft
tags:
  - accessory-function
  - extra
  - product-function
subtypeOf:
  - "[[Maintain Battery Electrolyte]]"
dependsOn:
  - "[[Forced Electrolyte Circulation]]"
  - "[[Air Injection Electrolyte Circulation]]"
performedBy:
  - "[[GS Yuasa Traction Battery (Europe)]]"
  - "[[HAWKER Perfect Plus Battery]]"
  - "[[Exide AIR Electrolyte Agitation System]]"
  - "[[HOPPECKE trak air Electrolyte Circulation]]"
  - "[[Midac EUW Electrolyte Circulation System]]"
  - "[[Electrolyte Air Circulation Assembly]]"
  - "[[Electrolyte Circulation Air Pump]]"
  - "[[Cell Air Distribution Tubing]]"
realizedBy:
  - "[[Air Injection Electrolyte Circulation]]"
  - "[[HOPPECKE trak uplift air Battery]]"
---

# Circulate Electrolyte

## Definition

Mix or circulate electrolyte during charging to limit acid stratification.

## Notes

- Accessory behavior found in product descriptions. Product links only where a source states the behavior.
- No Requirement is linked (intentional gap).
- **Sources** (product, evidence level, web page):
  - [[Exide AIR Electrolyte Agitation System]] (V): <https://www.exidegroup.com/eu/sites/default/files/2021-08/GNB_MP_Overview_EN_web.pdf>
  - [[Midac EUW Electrolyte Circulation System]] (V): <https://www.batterie-siems.de/en-gb/2-pzs-280-2mdl140>
  - [[HOPPECKE trak air Electrolyte Circulation]] (V): <https://hoppecke.com/en/stories/show/switch-from-gas-to-electrically-powered-forklift-trucks>
  - [[GS Yuasa Traction Battery (Europe)]] (V): <https://www.logisticsbusiness.com/?p=40376>
  - [[HAWKER Perfect Plus Battery]] (V): <https://enersys.com/4a6cd5/globalassets/documents/product-documentation/hawker/perfect-plus/emea/hawker-perfect-plus-instruction-for-use-english.pdf>
  - [[HOPPECKE trak uplift air Battery]] (V): <https://hoppecke.com/en/stories/show/switch-from-gas-to-electrically-powered-forklift-trucks>
- **Extra (round 30):** documented for 4 of 21 battery maker groups (19 percent); [[Forced Electrolyte Circulation]] remains the general construction Design and [[Air Injection Electrolyte Circulation]] is the specific realization supported by the current products.

## Implementation Allocation

The current specific realization is [[Air Injection Electrolyte Circulation]] -> [[Electrolyte Air Circulation Assembly]].

The assembly is decomposed into [[Electrolyte Circulation Air Pump]] and [[Cell Air Distribution Tubing]]. The physical architecture may be split between charger and battery.

### Explicit pump/tubing evidence

- [[Midac EUW Electrolyte Circulation System]] explicitly uses in-cell tubes fed by a charger-mounted air pump. Both component roles are directly supported.
- [[HAWKER Perfect Plus Battery]] explicitly identifies an air pump in its electrolyte-circulation option. The pump is directly supported; the cell-distribution path is functionally necessary but its exact construction is unpublished.
- [[HOPPECKE trak air Electrolyte Circulation]] explicitly blows air into each cell during charging. [[Cell Air Distribution Tubing]] is allocated at **>=95% engineering confidence**; the source does not identify the air-pump implementation.

### Method-level allocations

[[Exide AIR Electrolyte Agitation System]], [[GS Yuasa Traction Battery (Europe)]], and [[HOPPECKE trak uplift air Battery]] are allocated [[Air Injection Electrolyte Circulation]] where air mixing/circulation is explicitly identified, but no additional component detail is asserted unless supported.

No charger-control firmware, relay, valve, flow sensor, or air-pressure feedback loop is added from the current evidence.

## Aliases


## Former ids
