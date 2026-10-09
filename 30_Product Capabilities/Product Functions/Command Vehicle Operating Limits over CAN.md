---
type: Function
subtype:
id: FUNC-00026
uid: 20261002165629052skellyspencer
status: Draft
tags:
  - battery-monitoring
  - extra
  - product-function
subtypeOf:
  - "[[Protect Battery from Harm]]"
dependsOn:
  - "[[CAN Interface]]"
  - "[[CAN Vehicle Operating Limit Command]]"
performedBy:
  - "[[EnerSys Wi-iQ]]"
  - "[[Vehicle Operating Limit Command Firmware]]"
realizes:
  - "[[Integrate the Battery with Truck and Charger Controls]]"
realizedBy:
  - "[[CAN Vehicle Operating Limit Command]]"
  - "[[Integrate the Battery with Truck and Charger Controls]]"
---

# Command Vehicle Operating Limits over CAN

## Definition

Send the vehicle a limited-operation or lift lock-out trigger over CAN so the truck reduces or stops functions when the battery state requires it.

## Notes

- Stated only in the Wi-iQ4 manual, as parameters sent to trucks under OEM-specific protocols.
- Citations are listed under Sources below. Links to products are made only where a source states the behavior.
- **Sources** (product, evidence level, web page):
  - [[EnerSys Wi-iQ]] (V): <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>
- **Extra (round 30):** documented for 1 of 21 battery maker groups (5 percent); the transport dependency [[CAN Interface]] is retained, while the actual behavior is realized by [[CAN Vehicle Operating Limit Command]]. Rule and caveats remain in [[Extra Functions Register]].

## Implementation Allocation

The specific realization is [[CAN Vehicle Operating Limit Command]] -> [[Vehicle Operating Limit Command Firmware]].

[[CAN Interface]] remains a required transport dependency, implemented physically through [[CAN Communication Circuit]] and its CAN transceiver path. The command firmware converts an internal battery-protection or limit state into the OEM-specific CAN message or parameter expected by the vehicle.

For [[EnerSys Wi-iQ]], the firmware and CAN circuit allocations are **>=95% engineering-confidence assumptions** based on the published optional CAN module and OEM-specific operating-limit communication. The internal IC, message layout, software partition, and truck-side enforcement logic are not published.

No product-specific [[Interface]] or [[Connection]] is created because the evidence does not identify a specific receiving truck/controller endpoint. The model therefore stops at the Wi-iQ CAN boundary rather than inventing a paired vehicle architecture.

## Aliases


## Former ids
