---
type: Object
subtype: electrical
id: OBJ-00077
uid: 20261002191446820skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - charger
subtypeOf:
  - "[[Industrial Modular Charger]]"
performs:
  - "[[Charge Battery Conventionally]]"
  - "[[Charge Battery by Opportunity]]"
  - "[[Charge Battery Fast]]"
  - "[[Equalize Battery on Schedule]]"
  - "[[Compensate Charge for Battery Temperature]]"
madeBy:
  - "[[AMETEK Prestolite Power]]"
offeredBy:
  - "[[East Penn Manufacturing]]"
offeredWith:
  - "[[AMETEK Prestolite Power BID]]"
  - "[[AMETEK Prestolite Power BID with Ah Accumulator]]"
hasDesign:
  - "[[Temperature-Compensated Charge Control Design]]"
hasPart:
  - "[[Temperature Compensation Charge Control Firmware]]"
  - "[[AMETEK Prestolite Power BID with Ah Accumulator]]"
---

# AMETEK Prestolite Power Eclipse II

## Definition

AMETEK Prestolite high-frequency charger line with an optional BID battery identification module.

## Notes

- Prestolite says the Eclipse II (conventional) and Eclipse II Plus (opportunity and fast) are 93 percent efficient, use IGBT high-frequency conversion and the EC2000 control, recharge a drained lead-acid battery in eight hours or less, and offer an optional battery identification module (BID) holding rated capacity, rated voltage and battery type. Source: Fleet Owner (T2), retrieved 2026-10-02. <https://www.fleetowner.com/equipment/news/updated-industrial-battery-charger-1115>
- The Eclipse II HE second generation (2014) keeps 93 percent efficiency, a 0.95 power factor, and an intelligent monitoring system for optimum charge regardless of battery age, type or electrolyte temperature. Source: M H&W magazine (T2 (dated)), retrieved 2026-10-02. <https://www.mhwmag.com/?p=2184>
- **Functions performed, with citations** (V = verified this pass):
  - [[Charge Battery Conventionally]] (V): <https://www.fleetowner.com/equipment/news/updated-industrial-battery-charger-1115>
  - [[Charge Battery by Opportunity]] (V): <https://www.fleetowner.com/equipment/news/updated-industrial-battery-charger-1115>
  - [[Charge Battery Fast]] (V): <https://www.fleetowner.com/equipment/news/updated-industrial-battery-charger-1115>
  - [[Equalize Battery on Schedule]] (V): <https://www.fleetowner.com/equipment/news/updated-industrial-battery-charger-1115>
  - [[Compensate Charge for Battery Temperature]] (V): <https://www.fleetowner.com/equipment/news/updated-industrial-battery-charger-1115>

- **Architecture realization — temperature-compensated charging:** published behavior supports [[Temperature-Compensated Charge Control Design]]. [[Temperature Compensation Charge Control Firmware]] is allocated at **>=95% engineering confidence** because the charger must apply temperature-dependent control while its internal software partition is unpublished. Compensation slope, thresholds, filtering, and fault fallback remain product-specific.

## Aliases

- Eclipse II
- Eclipse II Plus


## Former ids
