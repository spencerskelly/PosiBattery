---
type: Object
subtype: electrical
id: OBJ-00123
uid: 20261002193402979skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - battery
  - canbus
  - heater
  - gse
subtypeOf:
  - "[[Lithium-Ion Traction Battery]]"
performs:
  - "[[Communicate Battery State over CAN]]"
hasDesign:
  - "[[Integrated Battery Management System]]"
  - "[[CAN Interface]]"
  - "[[Integrated Battery Heater]]"
  - "[[CAN Battery State Communication Design]]"
madeBy:
  - "[[Green Cubes Technology]]"
offeredWith:
  - "[[Green Cubes SAFEFlex Charger]]"
---

# Green Cubes GSE Lithium Battery

## Definition

Green Cubes lithium battery for ground support equipment with heaters and a CANbus interface.

## Notes

- Green Cubes says its GSE battery has a BMS on top of the pack and a CANbus interface for battery state, plus heaters for a wide temperature range; the 80 V FBP-1000 series is listed for eGSE. Source: Ground Support Worldwide video and press release (T2), retrieved 2026-10-02. <https://www.aviationpros.com/gse/video/55251746/green-cubes-technology-highlights-lithium-safeflex-batteries-for-gse>
- The press release says the battery uses LFP chemistry with heaters designed for extreme conditions. Source: Aviation Pros release (T2), retrieved 2026-10-02. <https://www.aviationpros.com/ground-support-worldwide/gse/press-release/55139765/green-cubes-technology-green-cubes-technology-unveils-new-li-ion-battery-for-ground-support-equipment>
- **Design characteristics, with citations:**
  - [[Integrated Battery Management System]] (V): <https://www.aviationpros.com/gse/video/55251746/green-cubes-technology-highlights-lithium-safeflex-batteries-for-gse>
  - [[CAN Interface]] (V): <https://www.aviationpros.com/gse/video/55251746/green-cubes-technology-highlights-lithium-safeflex-batteries-for-gse>
  - [[Integrated Battery Heater]] (V): <https://www.aviationpros.com/ground-support-worldwide/gse/press-release/55139765/green-cubes-technology-green-cubes-technology-unveils-new-li-ion-battery-for-ground-support-equipment>
- **Functions performed, with citations (round 40, gap review 2026-10-03):**
  - [[Communicate Battery State over CAN]] (V): <https://www.aviationpros.com/gse/video/55251746/green-cubes-technology-highlights-lithium-safeflex-batteries-for-gse>
- **Design characteristics, with citations (round 40, gap review 2026-10-03):**
  - [[Integrated Battery Management System]] (V): <https://www.aviationpros.com/gse/video/55251746/green-cubes-technology-highlights-lithium-safeflex-batteries-for-gse>
  - [[Integrated Battery Heater]] (V): <https://www.aviationpros.com/gse/video/55251746/green-cubes-technology-highlights-lithium-safeflex-batteries-for-gse>

- **Architecture realization — CAN battery state communication:** the product is allocated [[CAN Battery State Communication Design]] because published evidence establishes battery-state exchange over CAN or a CAN-based vehicle/battery interface. Message identifiers, signal maps, update rates, and protocol details remain product-specific.

## Aliases

- SAFEFlex GSE


## Former ids
