---
type: Function
subtype:
id: FUNC-00088
uid: 20261003141234119skellyspencer
status: Draft
tags:
  - accessory-function
  - extra
  - product-function
subtypeOf:
  - "[[Inform Users of Battery Condition]]"
dependsOn:
  - "[[Electrolyte Level Sensing Design]]"
  - "[[Low Electrolyte Alert Design]]"
performedBy:
  - "[[Crown Battery Acid Indicators]]"
  - "[[Crown V-Force BMID]]"
  - "[[Flow-Rite Eagle Eye Elite IV]]"
  - "[[Philadelphia Scientific SmartBlinky Pro]]"
  - "[[Low Electrolyte Alert Logic]]"
  - "[[Low Electrolyte Threshold Circuit]]"
  - "[[Low Electrolyte Alert Output Assembly]]"
  - "[[LED Status Indicator Element]]"
  - "[[Audible Alarm Transducer]]"
realizedBy:
  - "[[Low Electrolyte Alert Design]]"
realizes:
  - "[[Keep Trucks Working Without Battery Maintenance Labor]]"
---

# Alert on Low Electrolyte Level

## Definition

Warn users that the electrolyte level in a flooded battery is low and water is needed.

## Notes

- Behavior found in product descriptions. Product links only where a source states the behavior.
- No Requirement is linked (intentional gap).
- **Sources** (product, evidence level, web page):
  - [[Crown Battery Acid Indicators]] (V): <https://www.crown.com/en-ca/batteries-and-chargers/>
  - [[Crown V-Force BMID]] (V): <https://www.crown.com/content/dam/crown/pdfs/en-us/brochures/products/vhfm3-chargers.pdf>
  - [[Flow-Rite Eagle Eye Elite IV]] (V): <https://www.flow-rite.com/wp-content/uploads/2023/07/MM-001-EE-ELITE-IV-0723.pdf>
  - [[Philadelphia Scientific SmartBlinky Pro]] (V): <https://www.phlsci.com/products/blinky-battery-watering-monitors/smartblinky-pro/>
- **Extra (round 30):** documented for 1 of 21 battery maker groups (5 percent); the realization has since been refined into [[Electrolyte Level Sensing Design]] plus [[Low Electrolyte Alert Design]]. Rule and caveats remain in [[Extra Functions Register]].

## Implementation Allocation

This Function requires two stages: an electrolyte-level state from [[Electrolyte Level Sensing Design]], followed by an alert-delivery solution from [[Low Electrolyte Alert Design]].

### Alert-decision alternatives

- **Controller/software path:** [[Low Electrolyte Alert Logic]] consumes a qualified level state and can implement threshold qualification, delay, hysteresis, multi-stage status, and output selection. It is allocated to [[Philadelphia Scientific SmartBlinky Pro]] and [[Crown V-Force BMID]] at **>=95% engineering confidence** because their published behavior requires nontrivial low-level state handling while the internal implementation is not disclosed.
- **Hardware-only path:** [[Low Electrolyte Threshold Circuit]] can implement thresholding and hysteresis with dedicated electronics and drive an alert without programmable firmware. It remains a reusable implementation alternative because no current public product source proves that specific internal topology.

### Alert-delivery alternatives

- **Local visual or audible alert:** [[Local Low Electrolyte Alert]] can be implemented through [[LED Status Indicator Element]], [[Audible Alarm Transducer]], or both. Verified examples are [[Flow-Rite Eagle Eye Elite IV]], [[Philadelphia Scientific SmartBlinky Pro]], and the smart variants represented by [[Crown Battery Acid Indicators]].
- **Communicated watering need:** [[Communicated Watering Need Alert]] is verified for [[Crown V-Force BMID]], which detects low electrolyte and communicates the need to water. The transport and charger-side presentation are not stated, so no specific communication interface is inferred.

The local-output path is physically represented by the abstract reusable [[Low Electrolyte Alert Output Assembly]]. Specific products are linked only to the output components their evidence establishes.

## Aliases


## Former ids
