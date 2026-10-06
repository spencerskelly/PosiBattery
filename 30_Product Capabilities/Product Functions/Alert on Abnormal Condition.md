---
type: Function
subtype:
id: FUNC-00012
uid: 20261002164202358skellyspencer
status: Draft
tags:
  - battery-monitoring
  - extra
  - product-function
subtypeOf:
  - "[[Inform Users of Battery Condition]]"
dependsOn:
  - "[[Abnormal Condition Alert Design]]"
performedBy:
  - "[[Abnormal Condition Evaluation Logic]]"
  - "[[Abnormal Condition Threshold Circuit]]"
  - "[[Local Abnormal Alert Output Assembly]]"
  - "[[Remote Alert Notification Service]]"
  - "[[Status Indicator Driver Circuit]]"
  - "[[LED Status Indicator Element]]"
  - "[[Audible Alarm Transducer]]"
  - "[[LCD Status Display Module]]"
  - "[[Local Status Presentation Firmware]]"
  - "[[Operator Display HMI Firmware]]"
  - "[[Operator Touchscreen Display Module]]"
  - "[[Access Control Group CellTrac]]"
  - "[[Advanced Charging Technologies BATTview]]"
  - "[[Crown Battery Health Monitor]]"
  - "[[EnerSys Wi-iQ]]"
  - "[[EnerSys iQ Mini]]"
  - "[[Energywith withBMS BMU]]"
  - "[[Exide Motion+ EasyMonitor]]"
  - "[[HOPPECKE trak collect]]"
  - "[[Hyster Battery Tracker]]"
  - "[[Inventus Smart Battery Monitor SBM-01]]"
  - "[[Philadelphia Scientific eGO!Mini]]"
  - "[[Philadelphia Scientific eGO!c]]"
  - "[[Philadelphia Scientific eGO!pro]]"
  - "[[Power Designers PowerTrac DT3]]"
  - "[[Power Designers PowerTrac SP+]]"
  - "[[Raymond iBattery]]"
  - "[[Yale Battery Vision]]"
  - "[[Philadelphia Scientific SmartBlinky Pro]]"
  - "[[Yale ERC050-060VGL]]"
  - "[[EnerSys Truck iQ]]"
  - "[[PosiCharge Battery Rx]]"
  - "[[Philadelphia Scientific eGO!core]]"
  - "[[Philadelphia Scientific eGO!plus]]"
realizedBy:
  - "[[Abnormal Condition Alert Design]]"
realizes:
  - "[[Review BMID Battery History and Exceptions]]"
  - "[[Start a Shift and Confirm Vehicle Energy Readiness]]"
---

# Alert on Abnormal Condition

## Definition

Raise an alarm or notification when a measured quantity crosses a threshold or a fault is detected.

## Notes

- Local alarm hardware is a design choice; see [[Audible Alarm]] and [[Local LED Indicator]].
- Product links are made only where a source states the behavior; no link means unknown, not absent. Overview: [[Function Map]].
- No Requirement is linked: nothing here is a committed requirement, so model-health will show these Functions without satisfied Requirements. That gap is intentional.
- **Sources** (product, evidence level, web page):
  - [[EnerSys Wi-iQ]] (V): <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf> <https://www.enersys.com/en-gb/about-us/news/enersys_suite_of_power_management_tools_elevate_fleet_performance/>
  - [[Philadelphia Scientific eGO!pro]] (V): <https://www.phlsci.com/products/ego-battery-performance-monitors/ego-pro/> <https://www.phlsci.com/media/vbohieng/egopro-ssh-ps-us-en-doc0642.pdf>
  - [[Philadelphia Scientific eGO!Mini]] (V): <https://www.phlsci.com/media/151762/ego-mini-egou-ps-ssh-doc0184-eng.pdf>
  - [[Philadelphia Scientific eGO!c]] (V): <https://www.ipesearch.co.uk/iOT-technology-for-batteries>
  - [[Philadelphia Scientific SmartBlinky Pro]] (V): <https://www.mhwmag.com/?p=7981>
  - [[Energywith withBMS BMU]] (C): <https://www.energy-with.com/en/solutions/forklift-battery-monitoring/>
  - [[Power Designers PowerTrac SP+]] (V): <https://www.powerdesignerssibex.com/powertrac-sp/>
  - [[Power Designers PowerTrac DT3]] (V): <https://www.powerdesignerssibex.com/wp-content/uploads/2024/04/PDS-PT-DT3_PowerTracDT3.pdf>
  - [[HOPPECKE trak collect]] (V): <https://www.hoppecke.com/uk/news/improved-battery-management-with-trak-collect/>
  - [[Crown Battery Health Monitor]] (V): <https://www.mhlnews.com/new-products/forklift-battery-performance-monitor-new-products>
  - [[Raymond iBattery]] (V): <https://test-iwarehouseknows.raymondcorp.com/products/battery-monitoring>
  - [[Hyster Battery Tracker]] (V): <https://refrigeratedfrozenfood.com/articles/91289-forklift-battery-management-solution-monitors-health-usage>
  - [[Yale Battery Vision]] (V): <https://www.mhlnews.com/new-products/forklift-battery-monitor-new-products>
  - [[Access Control Group CellTrac]] (V): <https://www.mhlnews.com/archive/celltrac>
  - [[Inventus Smart Battery Monitor SBM-01]] (V): <https://inventuspower.com/wp-content/uploads/TDS_Smart-Battery-Monitor_2023-Aug_V1.pdf>
  - [[Exide Motion+ EasyMonitor]] (V): <https://www.exidegroup.com/en/product/easymonitor> <https://www.exidegroup.com/en/document/easy-monitor-leaflet>
  - [[Advanced Charging Technologies BATTview]] (V): <https://og.mhi.org/media/members/41607/133717592244521430.pdf>
  - [[EnerSys iQ Mini]] (V): <https://www.enersys.com/496a7c/globalassets/documents/product-documentation/_enersys/glob/legacy/battery-management/iq-mini/glob-en-fly-iqm-0924-apac.pdf> (also [[Document - EnerSys iQ Mini Flyer (GLOB-EN-FLY-IQM 0924)]])
  - [[Yale ERC050-060VGL]] (V): <https://www.allmachines.com/forklifts/yale-erc060vgl>
  - [[EnerSys Truck iQ]] (V): <https://www.enersys.com/en-gb/about-us/news/enersys_suite_of_power_management_tools_elevate_fleet_performance/>
  - [[PosiCharge Battery Rx]] (V): <https://www.posicharge.com/source/PDF/BatteryRx.pdf>
  - [[Philadelphia Scientific eGO!core]] (V): <https://phlsci.com/product-lines/ego-battery-performance-monitors/ego-core>
  - [[Philadelphia Scientific eGO!plus]] (V): <https://www.phlsci.com/product-lines/battery-performance-monitors/ego-plus/>
- **Extra (round 30):** documented for 5 of 21 battery maker groups (24 percent); the implementation dependency has since been refined from [[Warning and Display Device Design]] to [[Abnormal Condition Alert Design]]. Rule and caveats remain in [[Extra Functions Register]].

## Implementation Allocation

The reusable realization is [[Abnormal Condition Alert Design]]. The alert chain is intentionally separated into **condition evaluation** and **alert delivery**.

### Condition-evaluation alternatives

- **Programmable/software path:** [[Abnormal Condition Evaluation Logic]] evaluates measurements, timers, histories, diagnostic flags or state transitions and decides when an abnormal condition becomes an alert. It is allocated to several electronic monitors at **>=95% engineering confidence** where the published product behavior proves threshold/state evaluation but not the internal software partition.
- **Hardware-only path:** [[Abnormal Condition Threshold Circuit]] represents a comparator/reference/hysteresis implementation for simple devices. It remains a valid reusable alternative, but no current product is assigned because the public evidence does not prove a hardware-only topology.

### Alert-delivery alternatives

- **Local device alert:** [[Local Abnormal Condition Alert]] -> [[Local Abnormal Alert Output Assembly]], using some combination of [[LED Status Indicator Element]], [[Audible Alarm Transducer]], [[LCD Status Display Module]], [[Status Indicator Driver Circuit]], and [[Local Status Presentation Firmware]]. Verified examples include [[EnerSys Wi-iQ]], [[EnerSys iQ Mini]], [[Philadelphia Scientific eGO!Mini]], and [[Philadelphia Scientific eGO!pro]].
- **Operator-dashboard alert:** [[Operator Dashboard Abnormal Alert]] reuses the vehicle HMI architecture. [[EnerSys Truck iQ]] is the verified example: alerts and alarms received from Wi-iQ are shown on the truck-mounted touchscreen over the product's verified BLE link.
- **Remote exception notification:** [[Remote Exception Notification]] -> [[Remote Alert Notification Service]], depending on the product's existing [[Cloud Portal Integration]] / communication path. Verified examples include [[Hyster Battery Tracker]], [[Yale Battery Vision]], [[PosiCharge Battery Rx]], [[Crown Battery Health Monitor]], [[Philadelphia Scientific eGO!core]], [[Philadelphia Scientific eGO!plus]], and [[Philadelphia Scientific eGO!pro]].

### Products intentionally left at the generic alert level

Several products explicitly state alarms, alerts, exceptions, fault diagnostics, or abnormal-condition detection but do not establish whether the user is notified locally, on a vehicle display, remotely, or only through recorded/reporting software. These include [[Advanced Charging Technologies BATTview]], [[Power Designers PowerTrac SP+]], [[Power Designers PowerTrac DT3]], [[HOPPECKE trak collect]], [[Raymond iBattery]], [[Access Control Group CellTrac]], [[Energywith withBMS BMU]], and others. No delivery Design is inferred from the word "alert" alone.

[[Philadelphia Scientific SmartBlinky Pro]] remains primarily modeled through the more specific [[Alert on Low Electrolyte Level]] architecture rather than being duplicated into this generic abnormal-condition family.

## Aliases


## Former ids
