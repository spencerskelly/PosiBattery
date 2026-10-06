---
type: Object
subtype: electrical
id: OBJ-00049
uid: 20261002164202417skellyspencer
status: Draft
tags:
  - adjacent
  - battery-market-reference
  - commercial-product
  - forklift
  - scope-aftermarket
  - vehicle-mounted
subtypeOf:
  - "[[Operator Display]]"
performs:
  - "[[Estimate State of Charge]]"
  - "[[Estimate Remaining Run Time]]"
  - "[[Display Battery Status to Operator]]"
  - "[[Detect Voltage Imbalance]]"
  - "[[Alert on Abnormal Condition]]"
hasDesign:
  - "[[Operator Touch Display]]"
  - "[[Bluetooth Low Energy Interface]]"
  - "[[Vehicle-Mounted Display]]"
hasPart:
  - "[[Operator Touchscreen Display Module]]"
  - "[[Operator Display Controller Circuit]]"
  - "[[Operator Display HMI Firmware]]"
  - "[[BLE Communication Circuit]]"
madeBy:
  - "[[EnerSys]]"
offeredWith:
  - "[[EnerSys Wi-iQ]]"
---

# EnerSys Truck iQ

## Definition

EnerSys truck-mounted display that shows data read wirelessly from the Wi-iQ on the battery.

## Notes

**Summary:**
EnerSys truck-mounted smart battery dashboard that shows live battery data read over Bluetooth from the Wi-iQ monitor.

**Marketed features:**
- 4.3 in (10.9 cm) touchscreen mounted on the dashboard
- Displays state of charge, alerts, alarms and other battery parameters
- Wireless Bluetooth link to Wi-iQ3/Wi-iQ4, manual or automatic pairing
- Starts automatically with the vehicle; powered from the battery via truck cables
- Marketed to avoid downtime and premature asset failure

**Summary and features sources:**
Maker or publisher marketing claims as stated, not independently verified.
- EnerSys (T1), retrieved 2026-10-04. <https://enersys.com/en/products/monitoring-and-fleet-management/data-logger/enersys/truck-iqsuptradesup-smart-battery-dashboard>
- EnerSys (T1), retrieved 2026-10-04. <https://www.enersys.com/en-gb/about-us/news/enersys_suite_of_power_management_tools_elevate_fleet_performance/>
- EnerSys (T1), retrieved 2026-10-04. <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>

- EnerSys says Truck iQ is a truck-mounted touchscreen powered through the lift truck cables that reads Wi-iQ3 data wirelessly and shows remaining work time, battery warnings, state of charge, temperatures, electrolyte level and cell imbalance, connecting without driver action. Source: EnerSys Truck iQ page (T1), retrieved 2026-10-02. <https://enersys.com/en/products/monitoring-and-fleet-management/data-logger/enersys/truck-iqsuptradesup-smart-battery-dashboard>
- EnerSys describes the Wi-iQ data as communicated by Bluetooth to the Truck iQ dashboard. Source: EnerSys news release (T2), retrieved 2026-10-02. <https://www.enersys.com/en-gb/about-us/news/enersys_suite_of_power_management_tools_elevate_fleet_performance/>
- **Locus:** vehicle-mounted; adjacent, not battery-installed.
- **Functions performed, with citations** (V = verified this pass, C = carried from seed text, U = user-stated):
  - [[Estimate State of Charge]] (V): <https://enersys.com/en/products/monitoring-and-fleet-management/data-logger/enersys/truck-iqsuptradesup-smart-battery-dashboard>
  - [[Estimate Remaining Run Time]] (V): <https://enersys.com/en/products/monitoring-and-fleet-management/data-logger/enersys/truck-iqsuptradesup-smart-battery-dashboard>
  - [[Display Battery Status to Operator]] (V): <https://enersys.com/en/products/monitoring-and-fleet-management/data-logger/enersys/truck-iqsuptradesup-smart-battery-dashboard> <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>
  - [[Detect Voltage Imbalance]] (V): <https://enersys.com/en/products/monitoring-and-fleet-management/data-logger/enersys/truck-iqsuptradesup-smart-battery-dashboard>
  - [[Alert on Abnormal Condition]] (V): <https://www.enersys.com/en-gb/about-us/news/enersys_suite_of_power_management_tools_elevate_fleet_performance/>
- **Design characteristics, with citations:**
  - [[Bluetooth Low Energy Interface]] (V): <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>
  - [[Vehicle-Mounted Display]] (V): <https://enersys.com/en/products/monitoring-and-fleet-management/data-logger/enersys/truck-iqsuptradesup-smart-battery-dashboard>
- **Sources used for the mapping above:** EnerSys Truck iQ page <https://enersys.com/en/products/monitoring-and-fleet-management/data-logger/enersys/truck-iqsuptradesup-smart-battery-dashboard>; EnerSys Wi-iQ4 owner's manual (Truck iQ section) <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>
- The Wi-iQ4 manual says the Truck iQ is a display powered by the battery via the truck cables that reads Wi-iQ4 data in real time over BLE and shows alerts, alarms, state of charge and other parameters. Source: EnerSys Wi-iQ4 owner's manual (T1), retrieved 2026-10-02. <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>
- **Architecture realization — operator battery display:** the 4.3-inch touchscreen and BLE link to Wi-iQ are verified. [[Operator Touchscreen Display Module]] and [[BLE Communication Circuit]] therefore capture verified implementation roles. [[Operator Display Controller Circuit]] and [[Operator Display HMI Firmware]] are allocated at **>=95% engineering confidence** because the internal controller/software architecture is not published.
- **Truck parts (round 31):** stated by the source: mounts on [[Truck Controls and Display]] (a truck-mounted touchscreen) | typical (inferred from the device type, not from a source): connects to [[Truck Controller and CAN Bus]]; acts on [[Truck Controls and Display]]. See [[Truck Part Connection Register]].

## Aliases

- Truck iQ


## Former ids
