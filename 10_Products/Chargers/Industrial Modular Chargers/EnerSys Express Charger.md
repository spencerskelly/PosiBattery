---
type: Object
subtype: electrical
id: OBJ-00059
uid: 20261002191446802skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - charger
subtypeOf:
  - "[[Industrial Modular Charger]]"
describedBy:
  - "[[Document - EnerSys IMPAQ and NexSys+ Charger Product Guide (AMER 0125)]]"
performs:
  - "[[Continue Charging Through Module Fault]]"
  - "[[Desulfate Battery During Charge]]"
  - "[[Diagnose Battery During Charge]]"
  - "[[Charge in Cold Storage]]"
  - "[[Charge Battery Fast]]"
  - "[[Charge Battery by Opportunity]]"
  - "[[Compensate Charge for Battery Temperature]]"
  - "[[Equalize Battery on Schedule]]"
hasDesign:
  - "[[Dual-Cable and Parallel Charging Configuration]]"
  - "[[Temperature-Compensated Charge Control Design]]"
  - "[[Communicated Battery Temperature Charge Compensation]]"
madeBy:
  - "[[EnerSys]]"
offeredWith:
hasPart:
  - "[[Temperature Compensation Charge Control Firmware]]"
  - "[[EnerSys Wi-iQ]]"
---

# EnerSys Express Charger

## Definition

EnerSys charger line described as charging quickly and safely, with units equipped with a Wi-iQ device.

## Notes

- The guide's Express charger text says Express chargers charge quickly and safely and that units are equipped with a Wi-iQ battery monitoring device to provide battery voltage and related data. Source: EnerSys IMPAQ and NexSys+ guide (T1), retrieved 2026-10-02. <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf>
- **Functions performed, with citations (round 11 document):**
  - [[Continue Charging Through Module Fault]] (V): <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf> (also [[Document - EnerSys IMPAQ and NexSys+ Charger Product Guide (AMER 0125)]])
  - [[Desulfate Battery During Charge]] (V): <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf> (also [[Document - EnerSys IMPAQ and NexSys+ Charger Product Guide (AMER 0125)]])
  - [[Diagnose Battery During Charge]] (V): <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf> (also [[Document - EnerSys IMPAQ and NexSys+ Charger Product Guide (AMER 0125)]])
  - [[Charge in Cold Storage]] (V): <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf> (also [[Document - EnerSys IMPAQ and NexSys+ Charger Product Guide (AMER 0125)]])
  - [[Charge Battery Fast]] (V): <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf> (also [[Document - EnerSys IMPAQ and NexSys+ Charger Product Guide (AMER 0125)]])
  - [[Charge Battery by Opportunity]] (V): <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf> (also [[Document - EnerSys IMPAQ and NexSys+ Charger Product Guide (AMER 0125)]])
  - [[Compensate Charge for Battery Temperature]] (V): <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf> (also [[Document - EnerSys IMPAQ and NexSys+ Charger Product Guide (AMER 0125)]])
  - [[Equalize Battery on Schedule]] (V): <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf> (also [[Document - EnerSys IMPAQ and NexSys+ Charger Product Guide (AMER 0125)]])
- **Design characteristics, with citations (round 11 document):**
  - [[Dual-Cable and Parallel Charging Configuration]] (V): <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf> (also [[Document - EnerSys IMPAQ and NexSys+ Charger Product Guide (AMER 0125)]])
- **Round 11 document:** Source: [[Document - EnerSys IMPAQ and NexSys+ Charger Product Guide (AMER 0125)]] (T1, local copy; original <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf>), absorbed 2026-10-02.
| Parameter | Value as stated |
|---|---|
| Purpose | designed exclusively for Express batteries; fast charge anytime during the workday |
| Profiles | IONIC profile with continuous diagnosis; proprietary Express fast charge profile; opportunity; cold storage; desulfation; auto equalization |
| Temperature | Active Temperature/Output Management; Wi-iQ equipped to provide battery voltage and capacity data |
| Configurations | dual-cable and parallel available (compatible battery configuration required) |
| Marks | California Energy Commission compliant; UL certified |
| Battery compatibility (chart) | flooded lead-acid opportunity and fast charging only |
- **Related-product note:** the guide ties this charger to the Express battery line, which is not yet modeled (see [[Unidentified Products Review]]).

- **Architecture realization — temperature-compensated charging:** published behavior supports [[Temperature-Compensated Charge Control Design]] with [[Communicated Battery Temperature Charge Compensation]]. [[Temperature Compensation Charge Control Firmware]] is allocated at **>=95% engineering confidence** because the charger must apply temperature-dependent control while its internal software partition is unpublished. Compensation slope, thresholds, filtering, and fault fallback remain product-specific.

## Aliases

- Express charger


## Former ids
