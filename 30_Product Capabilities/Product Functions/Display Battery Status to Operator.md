---
type: Function
subtype:
id: FUNC-00014
uid: 20261002164202360skellyspencer
status: Draft
tags:
  - battery-monitoring
  - extra
  - product-function
subtypeOf:
  - "[[Inform Users of Battery Condition]]"
dependsOn:
  - "[[Vehicle Operator Display Design]]"
performedBy:
  - "[[Vehicle Operator Display Assembly]]"
  - "[[Operator Display HMI Firmware]]"
  - "[[Vehicle-Mounted Display Module]]"
  - "[[Operator Touchscreen Display Module]]"
  - "[[Battery Discharge Indicator Module]]"
  - "[[Yale ERC050-060VGL]]"
  - "[[EnerSys Truck iQ]]"
  - "[[Linde MT18 Multifunction Display]]"
  - "[[Crown Gena Operating System]]"
  - "[[Hyster Power Cellect]]"
realizedBy:
  - "[[Vehicle Operator Display Design]]"
realizes:
  - "[[Know Battery State Before and During the Shift]]"
  - "[[Start a Shift and Confirm Vehicle Energy Readiness]]"
---

# Display Battery Status to Operator

## Definition

Show battery status to the vehicle operator on a vehicle-side display.

## Notes

- Performed by vehicle-side devices, which are adjacent to the battery.
- Product links are made only where a source states the behavior; no link means unknown, not absent. Overview: [[Function Map]].
- No Requirement is linked: nothing here is a committed requirement, so model-health will show these Functions without satisfied Requirements. That gap is intentional.
- **Sources** (product, evidence level, web page):
  - [[EnerSys Truck iQ]] (V): <https://enersys.com/en/products/monitoring-and-fleet-management/data-logger/enersys/truck-iqsuptradesup-smart-battery-dashboard> <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>
  - [[Linde MT18 Multifunction Display]] (V): <https://expoproduction.thelogisticsworld.com/wp-content/themes/theme-summitexpo/directorio/assets/fichas/d0631ac8-a3f8-4b21-8640-bf6f41154ae8.pdf>
  - [[Yale ERC050-060VGL]] (V): <https://www.allmachines.com/forklifts/yale-erc060vgl>
  - [[Crown Gena Operating System]] (V): <https://crown.com/content/dam/crown/pdfs/apac/brochures/SP-1500-Broch-APAC.pdf>
  - [[Hyster Power Cellect]] (V): <https://www.enersys.com/de/about-us/news/fleet-managers-get-powerful-flexibility-combining-enersys-technology-breadth-with-yale-power-key-and-hyster-power-cellect/>
- **Extra (round 30):** documented for 2 of 10 truck maker groups (20 percent); the implementation dependency has since been refined from the broad [[Display Device Design]] to [[Vehicle Operator Display Design]]. Rule and caveats remain in [[Extra Functions Register]].

## Implementation Allocation

The reusable realization is [[Vehicle Operator Display Design]] implemented by [[Vehicle Operator Display Assembly]], visible display modules, and [[Operator Display HMI Firmware]]. [[Operator Display Controller Circuit]] provides the shared controller electronics inside the display architecture.

### Known implementation paths

- **BLE-fed touchscreen dashboard:** [[EnerSys Truck iQ]] receives Wi-iQ battery data over its verified BLE link using [[BLE Communication Circuit]], then presents state of charge, remaining work time, warnings and other values through [[Operator Touchscreen Display Module]]. The display controller and HMI firmware are **>=95% engineering-confidence assumptions** because the internal architecture is unpublished.
- **CAN-fed factory battery-discharge indicator:** [[Hyster Power Cellect]] uses a verified CAN link between battery and truck and presents battery information on the factory [[Battery Discharge Indicator Module]]. [[CAN Communication Circuit]] is the reusable physical-layer abstraction; exact transceiver/controller placement is not published.
- **Integrated multifunction display:** [[Linde MT18 Multifunction Display]] directly contains a multifunction vehicle display and battery-discharge indication. Its controller/HMI implementation is **>=95% engineering confidence**; the battery-data transport is not stated.
- **Integrated truck display:** [[Yale ERC050-060VGL]] shows state of charge and low-charge warnings on the truck display. The display module is verified while its controller, HMI software and input transport remain implementation assumptions.
- **Touchscreen operating system:** [[Crown Gena Operating System]] presents battery capacity on its verified 7-inch touchscreen. Because Gena is software, the physical touchscreen and controller are modeled as dependencies while [[Operator Display HMI Firmware]] represents the battery-status HMI role within the operating system.

No CAN, BLE, LIN, serial, or other data transport is inferred for Linde, Yale or Crown Gena where the source does not state it.

## Aliases


## Former ids
