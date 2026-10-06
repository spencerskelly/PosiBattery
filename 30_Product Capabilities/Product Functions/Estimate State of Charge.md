---
type: Function
subtype:
id: FUNC-00007
uid: 20261002164202353skellyspencer
status: Draft
tags:
  - battery-monitoring
  - extra
  - product-function
subtypeOf:
  - "[[Sense Battery State]]"
performedBy:
  - "[[Stryten M-Series Li610 Battery]]"
  - "[[PosiCharge BMID]]"
  - "[[PosiCharge Battery Rx]]"
  - "[[AMETEK Prestolite Power WBID Pro]]"
  - "[[EnerSys Wi-iQ]]"
  - "[[Exide Motion+ EasyMonitor]]"
  - "[[Hyster Battery Tracker]]"
  - "[[Inventus Smart Battery Monitor SBM-01]]"
  - "[[Power Designers PowerTrac DT3]]"
  - "[[Power Designers PowerTrac Monitor]]"
  - "[[Raymond iBattery]]"
  - "[[Yale Battery Vision]]"
  - "[[EnerSys Truck iQ]]"
  - "[[TUG ALPHA 1 Pushback]]"
  - "[[HOPPECKE trak collect]]"
  - "[[State of Charge Estimation Firmware]]"
realizes:
  - "[[Know Battery State Before and During the Shift]]"
  - "[[Inspect Battery Condition Through a BMID]]"
  - "[[Start a Shift and Confirm Vehicle Energy Readiness]]"
realizedBy:
  - "[[State of Charge Estimation Design]]"
supportedBy:
  - "[[Document - PosiCharge GSE BMID Page]]"
---

# Estimate State of Charge

## Definition

Estimate the battery's state of charge from measurements.

## Notes

- Estimation method is not stated by any retrieved source.
- Product links are made only where a source states the behavior; no link means unknown, not absent. Overview: [[Function Map]].
- No Requirement is linked: nothing here is a committed requirement, so model-health will show these Functions without satisfied Requirements. That gap is intentional.
- **Sources** (product, evidence level, web page):
  - [[PosiCharge BMID]] (V): <https://www.posicharge.com/airport-ground-support-equipment/>
  - [[PosiCharge Battery Rx]] (V): <https://www.posicharge.com/source/PDF/BatteryRx.pdf>
  - [[AMETEK Prestolite Power WBID Pro]] (C): <https://www.prestolitepower.com/products/datadevices/wbid-pro>
  - [[EnerSys Wi-iQ]] (V): <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>
  - [[EnerSys Truck iQ]] (V): <https://enersys.com/en/products/monitoring-and-fleet-management/data-logger/enersys/truck-iqsuptradesup-smart-battery-dashboard>
  - [[Power Designers PowerTrac DT3]] (V): <https://www.materialhandling247.com/product/powertrac_dt_battery_diagnostics_tool>
  - [[Power Designers PowerTrac Monitor]] (V): <https://powerdesignerssibex.com/powertrac-monitor/>
  - [[Raymond iBattery]] (V): <https://mhlnews.com/archive/article/22045964/raymond-battery-module>
  - [[Hyster Battery Tracker]] (V): <https://refrigeratedfrozenfood.com/articles/91289-forklift-battery-management-solution-monitors-health-usage>
  - [[Yale Battery Vision]] (V): <https://www.mhlnews.com/new-products/forklift-battery-monitor-new-products>
  - [[Inventus Smart Battery Monitor SBM-01]] (V): <https://inventuspower.com/wp-content/uploads/TDS_Smart-Battery-Monitor_2023-Aug_V1.pdf>
  - [[Exide Motion+ EasyMonitor]] (V): <https://www.exidegroup.com/en/document/easy-monitor-leaflet>
  - [[Stryten M-Series Li610 Battery]] (V): <https://www.businesswire.com/news/home/20260413514429/en/Stryten-Energy-Launches-New-MSeries-Li610-LithiumIon-Battery-at-MODEX>
  - [[TUG ALPHA 1 Pushback]] (V): <https://www.aviationpros.com/ground-support-worldwide/gse/pushbacks-tractors-utility-vehicles/press-release/21160222/textron-gse-textron-gse-introduces-the-tug-alpha-1>
  - [[HOPPECKE trak collect]] (V): <https://warehousenews.co.uk/?p=103814>
- **Extra (round 30):** documented for 4 of 21 battery maker groups (19 percent), delivered by devices or software (accessory and software notes); rule and caveats in [[Extra Functions Register]].

## Aliases


## Former ids
