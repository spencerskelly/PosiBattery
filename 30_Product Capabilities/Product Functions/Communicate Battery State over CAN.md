---
type: Function
subtype:
id: FUNC-00019
uid: 20261002164202365skellyspencer
status: Draft
tags:
  - battery-monitoring
  - extra
  - product-function
subtypeOf:
  - "[[Communicate Battery and Vehicle Data]]"
dependsOn:
  - "[[CAN Interface]]"
  - "[[CAN Battery State Communication Design]]"
describedBy:
  - "[[Metric - Wired and Vehicle Interfaces]]"
performedBy:
  - "[[PosiCharge PosiGuard]]"
  - "[[EnerSys Wi-iQ]]"
  - "[[Inventus Smart Battery Monitor SBM-01]]"
  - "[[Hyster Power Cellect]]"
  - "[[Stryten M-Series Li600 Battery]]"
  - "[[Green Cubes GSE Lithium Battery]]"
  - "[[HOPPECKE trak collect]]"
  - "[[CAN Battery State Communication Firmware]]"
realizes:
  - "[[Integrate a BMID with Charger Vehicle and Fleet Systems]]"
  - "[[Integrate the Battery with Truck and Charger Controls]]"
realizedBy:
  - "[[CAN Battery State Communication Design]]"
  - "[[Integrate the Battery with Truck and Charger Controls]]"
---

# Communicate Battery State over CAN

## Definition

Provide battery state to other equipment over a CAN network.

## Notes

- Protocols stated: CANopen, J1939 for Wi-iQ4; others not stated.
- Product links are made only where a source states the behavior; no link means unknown, not absent. Overview: [[Function Map]].
- No Requirement is linked: nothing here is a committed requirement, so model-health will show these Functions without satisfied Requirements. That gap is intentional.
- **Sources** (product, evidence level, web page):
  - [[PosiCharge PosiGuard]] (V): <https://posicharge.com/products/posiguard/>
  - [[EnerSys Wi-iQ]] (V): <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf> <https://integration.enersys.com/493bb4/globalassets/documents/product-documentation/_misc/wi-iq/emea/wi-iq3-battery-monitoring-device-brochure.pdf>
  - [[Inventus Smart Battery Monitor SBM-01]] (V): <https://inventuspower.com/wp-content/uploads/TDS_Smart-Battery-Monitor_2023-Aug_V1.pdf>
  - [[Hyster Power Cellect]] (V): <https://www.inddist.com/new-products/material-handling-storage/product/22885612/hyster-power-cellect-provides-forklift-battery-freedom>
  - [[Stryten M-Series Li600 Battery]] (V): <https://www.foodlogistics.com/sustainability/carbon-footprint/news/22891172/stryten-energy-lithium-batteries-for-cold-chain>
  - [[Green Cubes GSE Lithium Battery]] (V): <https://www.aviationpros.com/gse/video/55251746/green-cubes-technology-highlights-lithium-safeflex-batteries-for-gse>
  - [[HOPPECKE trak collect]] (V): <https://www.HOPPECKE.com/fileadmin/Redakteur/Hoppecke-Main/Products-Import/trak_collect_brochure_en.pdf>
- **Extra (round 30):** documented for 1 of 21 battery maker groups (5 percent); [[CAN Interface]] remains the transport dependency, while [[CAN Battery State Communication Design]] represents the application behavior.

## Implementation Allocation

The reusable realization is [[CAN Battery State Communication Design]] -> [[CAN Battery State Communication Firmware]].

[[CAN Interface]] and [[CAN Communication Circuit]] provide the physical/protocol transport. The firmware selects battery state, encodes it according to the product's CAN application protocol, and exchanges it with the connected equipment.

### Product allocation

Products with explicit CAN battery-state communication can use this common application-layer Design even when their protocol differs. Published examples include [[EnerSys Wi-iQ]], [[Inventus Smart Battery Monitor SBM-01]], [[PosiCharge PosiGuard]], [[Hyster Power Cellect]], [[Stryten M-Series Li600 Battery]], [[Green Cubes GSE Lithium Battery]], and [[HOPPECKE trak collect]].

The internal firmware allocation is **>=95% engineering confidence** where the product literature establishes CAN state exchange but does not expose the software partition.

CAN message IDs, PGNs, CANopen objects, signal scaling, update rates, heartbeats, node addressing, and timeout behavior remain product-specific.

## Aliases


## Former ids
