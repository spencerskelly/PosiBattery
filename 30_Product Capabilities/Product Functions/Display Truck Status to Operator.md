---
type: Function
subtype:
id: FUNC-00116
uid: 20261003163422033skellyspencer
status: Draft
tags:
  - extra
  - product-function
  - truck-function
subtypeOf:
  - "[[Inform Operator of Truck Condition]]"
dependsOn:
  - "[[Vehicle Operator Display Design]]"
performedBy:
  - "[[Vehicle Operator Display Assembly]]"
  - "[[Operator Display HMI Firmware]]"
  - "[[Vehicle-Mounted Display Module]]"
  - "[[Operator Touchscreen Display Module]]"
  - "[[Crown RC 5700 Series]]"
  - "[[Hangcha A Series Electric Forklifts]]"
  - "[[Mallaghan SkyBelt]]"
  - "[[Komatsu Operator Presence Sensing System]]"
  - "[[Crown Gena Operating System]]"
  - "[[Linde MT18 Multifunction Display]]"
realizedBy:
  - "[[Vehicle Operator Display Design]]"
realizes:
  - "[[Find and Fix Vehicle Faults Without Downtime]]"
---

# Display Truck Status to Operator

## Definition

Show the operator the truck's own status, such as diagnostics and warnings, on a dashboard or screen.

## Notes

- Behavior found in product descriptions. Product links only where a source states the behavior.
- No Requirement is linked (intentional gap).
- **Sources** (product, evidence level, web page):
  - [[Hangcha A Series Electric Forklifts]] (V): <https://www.hcforklift.com/upload/files/bbc143097cbd12b51ec8eb6ff9e84d96.pdf>
  - [[Mallaghan SkyBelt]] (V): <https://www.aviationpros.com/ground-support-worldwide/gse/article/55018081/mallaghan-expands-into-the-belt-loader-market>
  - [[Crown RC 5700 Series]] (V): <https://www.crown.com/content/dam/crown/pdfs/en-uk/specs/forklift-rc5700-spec-GB.pdf>
  - [[Komatsu Operator Presence Sensing System]] (V): <https://www.bkforklift.com/uploaded/images/1640141725202112226BR-EX50emi-004.pdf>
  - [[Crown Gena Operating System]] (V): <https://crown.com/content/dam/crown/pdfs/apac/brochures/SP-1500-Broch-APAC.pdf>
  - [[Linde MT18 Multifunction Display]] (V): <https://www.linde-mh.us/content/dam/linde/en/images/products/pallet-trucks/1133-03/Linde_MT18_Spec_Sheet_V2.pdf>
- **Extra (round 30):** documented for 2 of 10 truck maker groups (20 percent); the implementation dependency has since been refined from the broad [[Display Device Design]] to [[Vehicle Operator Display Design]]. Rule and caveats remain in [[Extra Functions Register]].

## Implementation Allocation

This Function reuses the same vehicle-side HMI architecture as [[Display Battery Status to Operator]]: [[Vehicle Operator Display Design]] -> [[Vehicle Operator Display Assembly]] with [[Operator Display Controller Circuit]], a visible display module, and [[Operator Display HMI Firmware]]. The difference is the **source information**, not necessarily the display hardware.

### Verified implementation paths

- **Crown RC 5700:** [[Vehicle-Mounted Display Module]] presents event codes and Access 1 2 3 diagnostics on the Crown display. The controller/HMI implementation is **>=95% engineering confidence**; the internal vehicle-data transport is not published.
- **Hangcha A Series:** a verified multi-function dashboard is represented by [[Vehicle-Mounted Display Module]]. Controller and HMI firmware are **>=95% engineering-confidence assumptions**.
- **Mallaghan SkyBelt:** a verified on-board diagnostics screen is represented by [[Vehicle-Mounted Display Module]]. Controller/HMI internals and data transport are not published.
- **Crown Gena:** [[Operator Touchscreen Display Module]] plus [[Operator Display HMI Firmware]] presents widgets, safety messages, operating guidance, and truck state on the verified 7-inch touchscreen. No specific internal bus is inferred.
- **Linde MT18:** [[Vehicle-Mounted Display Module]] plus HMI logic presents hour meter, maintenance state, and internal fault codes; internal electronics and transport are not published.
- **Komatsu Operator Presence Sensing System:** the interlock state is verified as appearing on the truck display/color monitor. Because the display is not part of the sensing accessory, the system depends on [[Vehicle-Mounted Display Module]] and [[Operator Display HMI Firmware]] rather than containing them.

### Data-source boundary

The display Function does not imply that every source uses CAN. Truck state may originate in a vehicle controller, safety/interlock controller, diagnostics subsystem, sensor controller, or other ECU. No CAN, LIN, Ethernet, serial, or proprietary transport is assigned unless a product source establishes it.

## Aliases


## Former ids
