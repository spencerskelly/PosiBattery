---
type: Object
subtype: electrical
id: OBJ-00080
uid: 20261002191446823skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - charger
  - lithium
subtypeOf:
  - "[[Industrial Modular Charger]]"
performs:
  - "[[Charge Lithium-Ion Battery]]"
  - "[[Charge Under BMS Control]]"
madeBy:
hasDesign:
  - "[[BMS-Directed Charge Control Design]]"
  - "[[CAN BMS-Directed Charging]]"
hasPart:
  - "[[BMS-Directed Charge Control Firmware]]"
  - "[[Fronius International]]"
---

# Fronius SelectION

## Definition

Fronius lithium-ion charger family with Plug & Charge.

## Notes

- Fronius says SelectION is for charging lithium-ion batteries and uses Plug & Charge with no additional settings. Source: Fronius charging solutions page (T1), retrieved 2026-10-02. <https://www.fronius.com/en/battery-charging-technology/product-list>
- Fronius also describes BatteryLink CAN with automatic baud-rate detection for Li-ion forklift batteries. Source: Fronius (T1), retrieved 2026-10-02. <https://www.fronius.com/en/battery-charging-technology/info-centre/news/lead-acid-lithium-ion>
- **Functions performed, with citations** (V = verified this pass):
  - [[Charge Lithium-Ion Battery]] (V): <https://www.fronius.com/en/battery-charging-technology/product-list>
  - [[Charge Under BMS Control]] (V): <https://www.fronius.com/en/battery-charging-technology/info-centre/news/lead-acid-lithium-ion>

- **Architecture realization — BMS-directed charging:** published behavior supports [[BMS-Directed Charge Control Design]] and the CAN-specific [[CAN BMS-Directed Charging]] path. [[BMS-Directed Charge Control Firmware]] is allocated at **>=95% engineering confidence** because charger-side executable control is required while the internal software partition is unpublished. The exact BMS message set, timeout/fallback behavior, and safety handoff remain product-specific.

## Aliases

- SelectION


## Former ids
