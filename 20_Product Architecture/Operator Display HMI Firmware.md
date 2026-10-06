---
type: Object
subtype: firmware
id: OBJ-90069
uid: 20261006170500005skellyspencer
status: Draft
tags:
  - reusable-architecture
  - operator-interface
  - display
  - firmware
reuseScope: cross-product
dependsOn:
  - "[[Operator Display Controller Circuit]]"
performs:
  - "[[Alert on Abnormal Condition]]"
  - "[[Display Truck Status to Operator]]"
  - "[[Display Battery Status to Operator]]"
dependencyOf:
  - "[[Komatsu Operator Presence Sensing System]]"
hasDesign:
  - "[[Operator Dashboard Abnormal Alert]]"
partOf:
  - "[[Hangcha A Series Electric Forklifts]]"
  - "[[Mallaghan SkyBelt]]"
  - "[[Crown RC 5700 Series]]"
  - "[[Vehicle Operator Display Assembly]]"
  - "[[Linde MT18 Multifunction Display]]"
  - "[[Yale ERC050-060VGL]]"
  - "[[EnerSys Truck iQ]]"
  - "[[Crown Gena Operating System]]"
---

# Operator Display HMI Firmware

## Definition

Firmware or embedded HMI software that converts battery, vehicle, diagnostic, or subsystem state into operator-facing values, icons, warnings, pages, or widgets.

## Notes

- Allocation to [[EnerSys Truck iQ]] is an **>=95% engineering-confidence assumption** because it is an electronic touchscreen dashboard with multiple live battery values and alerts, while EnerSys does not publish its internal firmware architecture.
- Allocation to [[Crown Gena Operating System]] is functionally direct because Gena is itself the truck operating/HMI software; this reusable note represents the battery-status presentation role within that software.
- The firmware does not imply the source transport. Product-specific battery data can arrive through BLE, CAN, or internal vehicle signals.
- Allocation to [[Linde MT18 Multifunction Display]], [[Yale ERC050-060VGL]], [[Crown RC 5700 Series]], [[Hangcha A Series Electric Forklifts]], and [[Mallaghan SkyBelt]] is **>=95% engineering confidence** because they present dynamic battery, vehicle, diagnostic, or warning information on electronic vehicle displays; their software partition is not published.
- [[Komatsu Operator Presence Sensing System]] depends on this HMI role rather than containing it because the interlock state is shown on the truck's display/color monitor.

## Former ids
