---
type: Object
subtype: electrical
id: OBJ-00061
uid: 20261002191446804skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - charger
  - wireless-charging
  - agv
subtypeOf:
  - "[[Wireless Charger]]"
describedBy:
  - "[[Document - EnerSys IMPAQ and NexSys+ Charger Product Guide (AMER 0125)]]"
performs:
  - "[[Charge Battery Wirelessly]]"
  - "[[Continue Charging Through Module Fault]]"
  - "[[Detect Foreign and Live Objects]]"
  - "[[Charge in Cold Storage]]"
  - "[[Charge Battery by Opportunity]]"
  - "[[Charge Battery Conventionally]]"
  - "[[Charge Lithium-Ion Battery]]"
  - "[[Compensate Charge for Battery Temperature]]"
  - "[[Equalize Battery on Schedule]]"
madeBy:
  - "[[EnerSys]]"
offeredWith:
  - "[[EnerSys Wi-iQ]]"
hasDesign:
  - "[[Temperature-Compensated Charge Control Design]]"
hasPart:
  - "[[Temperature Compensation Charge Control Firmware]]"
  - "[[EnerSys Wi-iQ]]"
---

# EnerSys NexSys AIR Wireless Charger

## Definition

EnerSys wireless charger for AGVs and other vehicles, compatible with all EnerSys battery technologies.

## Notes

- The brochure says NexSys AIR wireless chargers can charge multiple battery technologies including flooded lead-acid, are compatible with all EnerSys battery technologies, and can reduce AGV waiting time for charging. Source: EnerSys NexSys AIR brochure (T1), retrieved 2026-10-02. <https://www.enersys.com/493367/globalassets/documents/product-documentation/_enersys/apac/apac_en-imp-nex-com-air-0623.pdf>
- **Functions performed, with citations** (V = verified this pass):
  - [[Charge Battery Wirelessly]] (V): <https://www.enersys.com/493367/globalassets/documents/product-documentation/_enersys/apac/apac_en-imp-nex-com-air-0623.pdf>
- **Functions performed, with citations (round 11 document):**
  - [[Continue Charging Through Module Fault]] (V): <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf> (also [[Document - EnerSys IMPAQ and NexSys+ Charger Product Guide (AMER 0125)]])
  - [[Detect Foreign and Live Objects]] (V): <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf> (also [[Document - EnerSys IMPAQ and NexSys+ Charger Product Guide (AMER 0125)]])
  - [[Charge in Cold Storage]] (V): <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf> (also [[Document - EnerSys IMPAQ and NexSys+ Charger Product Guide (AMER 0125)]])
  - [[Charge Battery by Opportunity]] (V): <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf> (also [[Document - EnerSys IMPAQ and NexSys+ Charger Product Guide (AMER 0125)]])
  - [[Charge Battery Conventionally]] (V): <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf> (also [[Document - EnerSys IMPAQ and NexSys+ Charger Product Guide (AMER 0125)]])
  - [[Charge Lithium-Ion Battery]] (V): <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf> (also [[Document - EnerSys IMPAQ and NexSys+ Charger Product Guide (AMER 0125)]])
  - [[Compensate Charge for Battery Temperature]] (V): <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf> (also [[Document - EnerSys IMPAQ and NexSys+ Charger Product Guide (AMER 0125)]])
  - [[Equalize Battery on Schedule]] (V): <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf> (also [[Document - EnerSys IMPAQ and NexSys+ Charger Product Guide (AMER 0125)]])
- **Round 11 document:** Source: [[Document - EnerSys IMPAQ and NexSys+ Charger Product Guide (AMER 0125)]] (T1, local copy; original <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf>), absorbed 2026-10-02.
| Parameter | Value as stated |
|---|---|
| Use | hands-free charging for AGV applications; no manual intervention; eliminates mechanical contact wear |
| Safety | foreign and live object detection |
| Compatibility | flooded lead-acid, NexSys TPPL and NexSys iON; all EnerSys battery technologies |
| Controls | intuitive touchscreen; easily integrated charging pad in vertical or horizontal orientation |
| Chart | efficiency 94% or greater; automatic temperature adjustment via Wi-iQ; cold storage profile; TPPL and iON profiles |
| Ratings | not given (n/s) |

- **Architecture realization — temperature-compensated charging:** published behavior supports [[Temperature-Compensated Charge Control Design]]. [[Temperature Compensation Charge Control Firmware]] is allocated at **>=95% engineering confidence** because the charger must apply temperature-dependent control while its internal software partition is unpublished. Compensation slope, thresholds, filtering, and fault fallback remain product-specific.

## Aliases

- NexSys AIR


## Former ids
