---
type: Function
subtype:
id: FUNC-00038
uid: 20261002211134429skellyspencer
status: Draft
tags:
  - charger
  - extra
  - product-function
subtypeOf:
  - "[[Control Charge Profile]]"
performedBy:
  - "[[EnerSys Express Charger]]"
  - "[[EnerSys IMPAQ Charger]]"
  - "[[EnerSys NexSys+ Charger]]"
  - "[[Power Designers REVOLUTION X]]"
  - "[[Desulfation Charge Control Firmware]]"
dependsOn:
  - "[[Lead-Acid Desulfation Charge Control Design]]"
realizedBy:
  - "[[Lead-Acid Desulfation Charge Control Design]]"
  - "[[Desulfation Charge Control Firmware]]"
---

# Desulfate Battery During Charge

## Definition

Run a desulfation cycle or profile during charging of lead-acid batteries.

## Notes

- Found in the documents absorbed in round 11. Product links only where a source states the behavior; no link means unknown.
- No Requirement is linked (intentional gap).
- **Sources** (product, evidence level, web page):
  - [[EnerSys IMPAQ Charger]] (V): <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf> (also [[Document - EnerSys IMPAQ and NexSys+ Charger Product Guide (AMER 0125)]])
  - [[EnerSys Express Charger]] (V): <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf> (also [[Document - EnerSys IMPAQ and NexSys+ Charger Product Guide (AMER 0125)]])
  - [[EnerSys NexSys+ Charger]] (V): <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf> (also [[Document - EnerSys IMPAQ and NexSys+ Charger Product Guide (AMER 0125)]])
- [[Power Designers REVOLUTION X]] also publishes a built-in desulfation cycle; this adds a second charger maker group with verified support.
- **Implementation allocation:** [[Lead-Acid Desulfation Charge Control Design]] is the reusable behavior design. [[Desulfation Charge Control Firmware]] is the >=95% engineering-confidence controller realization; [[Charger Power Stage Design]] executes the commanded electrical output. Exact waveform/algorithm remains unknown.
- **Extra (round 30, corrected 2026-10-06):** documented for 2 of 18 charger maker groups (11 percent), delivered by charger control software and the existing power stage; rule and caveats in [[Extra Functions Register]].

## Aliases


## Former ids
