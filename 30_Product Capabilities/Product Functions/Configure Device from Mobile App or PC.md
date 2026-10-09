---
type: Function
subtype:
id: FUNC-00022
uid: 20261002164202368skellyspencer
status: Draft
tags:
  - battery-monitoring
  - extra
  - product-function
subtypeOf:
  - "[[Communicate Battery and Vehicle Data]]"
performedBy:
  - "[[Crown V-Force BMID]]"
  - "[[PosiCharge PosiGuard]]"
  - "[[EnerSys Wi-iQ]]"
  - "[[PosiCharge PosiConnect]]"
  - "[[Fronius TagID]]"
  - "[[HOPPECKE trak collect]]"
  - "[[Device Configuration and Service Firmware]]"
  - "[[PC Service Tool Software]]"
realizes:
  - "[[Configure and Service a Supported BMID]]"
satisfies:
  - "[[PosiGuard - Support Local Service Configuration]]"
realizedBy:
  - "[[Device Configuration and Service Design]]"
supportedBy:
  - "[[Document - PosiCharge PosiConnect Product Page]]"
dependsOn:
  - "[[Device Configuration and Service Design]]"
  - "[[Document - PosiCharge PosiConnect Product Page]]"
---

# Configure Device from Mobile App or PC

## Definition

Let a technician configure the device and read its logs from a phone, tablet or PC.

## Notes

- Tools named: PosiConnect, E Connect, eGO!Tools, PowerTrac setup utilities.
- Product links are made only where a source states the behavior; no link means unknown, not absent. Overview: [[Function Map]].
- No Requirement is linked: nothing here is a committed requirement, so model-health will show these Functions without satisfied Requirements. That gap is intentional.
- **Sources** (product, evidence level, web page):
  - [[PosiCharge PosiGuard]] (V): <https://apps.apple.com/mx/app/posiconnect/id6748969496>
  - [[Crown V-Force BMID]] (V): <https://shop.crown.com/crown/en/Batteries-and-Chargers/Battery-and-Charger-Parts-and-Accessories/Battery-and-Charger-Accessories//p/396525-BTM>
  - [[EnerSys Wi-iQ]] (V): <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>
  - [[PosiCharge PosiConnect]] (V): <https://posicharge.com/products/posiconnect/>
  - [[Fronius TagID]] (V): <https://manuals.fronius.com/html/4204102645/en-US.html>
  - [[HOPPECKE trak collect]] (V): <https://www.HOPPECKE.com/fileadmin/Redakteur/Hoppecke-Main/Products-Import/trak_collect_brochure_en.pdf>
- **Extra (round 30):** documented for 2 of 21 battery maker groups (10 percent); the reusable realization is now [[Device Configuration and Service Design]], with mobile and PC tool paths separated.

## Implementation Allocation

The reusable realization is [[Device Configuration and Service Design]].

### Mobile/tablet path

[[Mobile App Interface]] remains the appropriate front-end Design for products configured from a phone or tablet. Examples include [[PosiCharge PosiGuard]] with [[PosiCharge PosiConnect]], [[EnerSys Wi-iQ]], and [[Fronius TagID]].

### PC/laptop path

[[PC Service Tool Interface]] -> [[PC Service Tool Software]] represents desktop/laptop service workflows. [[Crown V-Force BMID]] explicitly supports laptop/tablet connection over Bluetooth Class 1, and [[HOPPECKE trak collect]] publishes PC software access.

### Device-side behavior

[[Device Configuration and Service Firmware]] represents the embedded configuration/service endpoint in the device. It is allocated at **>=95% engineering confidence** where published configuration behavior requires executable command handling but the internal firmware partition is not disclosed.

The service transport is modeled separately through the applicable Bluetooth/BLE, NFC, USB, serial, or other communication interface.

## Aliases


## Former ids
