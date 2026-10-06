---
type: Function
subtype:
id: FUNC-00004
uid: 20261002164202350skellyspencer
status: Draft
tags:
  - battery-monitoring
  - extra
  - product-function
subtypeOf:
  - "[[Sense Battery State]]"
dependsOn:
  - "[[Electrolyte Level Sensing Design]]"
describedBy:
  - "[[Metric - Electrolyte Level Sensing]]"
performedBy:
  - "[[Deka HydraSaver Battery]]"
  - "[[Exide MARATHON Battery]]"
  - "[[Crown V-Force BMID]]"
  - "[[Fronius TagID]]"
  - "[[PosiCharge Battery Rx]]"
  - "[[PosiCharge PosiGuard]]"
  - "[[AMETEK Prestolite Power WBID Pro]]"
  - "[[Access Control Group CellTrac]]"
  - "[[Advanced Charging Technologies BATTview]]"
  - "[[Crown Battery Health Monitor]]"
  - "[[EnerSys Wi-iQ]]"
  - "[[Energywith withBMS BMU]]"
  - "[[Exide Motion+ EasyMonitor]]"
  - "[[HOPPECKE trak collect]]"
  - "[[Hyster Battery Tracker]]"
  - "[[Philadelphia Scientific eGO!Mini]]"
  - "[[Philadelphia Scientific eGO!core]]"
  - "[[Philadelphia Scientific eGO!plus]]"
  - "[[Philadelphia Scientific eGO!pro]]"
  - "[[Power Designers PowerTrac 3]]"
  - "[[Power Designers PowerTrac SP+]]"
  - "[[Raymond iBattery]]"
  - "[[Yale Battery Vision]]"
  - "[[Crown Battery Acid Indicators]]"
  - "[[Flow-Rite Eagle Eye Elite IV]]"
  - "[[Flow-Rite Eagle Eye Essential IV]]"
  - "[[Philadelphia Scientific SmartBlinky Pro]]"
  - "[[Exide Automatic Watering System and Level Sensor]]"
  - "[[EnerSys iQ Mini]]"
  - "[[Electrolyte Level Measurement Circuit]]"
  - "[[Electrolyte Level Acquisition Firmware]]"
  - "[[Capacitive Electrolyte Level Sensor Assembly]]"
  - "[[Electronic Electrolyte Probe Assembly]]"
  - "[[Variable-Length Electrolyte Probe Assembly]]"
  - "[[Wrap-Around Cell Connector Sensor Assembly]]"
  - "[[Low-Current Electrolyte Level Input Circuit]]"
realizedBy:
  - "[[Electrolyte Level Sensing Design]]"
realizes:
  - "[[Keep Trucks Working Without Battery Maintenance Labor]]"
---

# Sense Electrolyte Level

## Definition

Sense whether the electrolyte level in a flooded lead-acid cell is adequate.

## Notes

- Level sensing differs from level indication; the indicating behavior is [[Indicate Battery Status Locally]].
- Product links are made only where a source states the behavior; no link means unknown, not absent. Overview: [[Function Map]].
- No Requirement is linked: nothing here is a committed requirement, so model-health will show these Functions without satisfied Requirements. That gap is intentional.
- **Sources** (product, evidence level, web page):
  - [[PosiCharge Battery Rx]] (V): <https://www.posicharge.com/source/PDF/BatteryRx.pdf>
  - [[PosiCharge PosiGuard]] (V): <https://posicharge.com/products/posiguard/>
  - [[Crown V-Force BMID]] (V): <https://crown.com/en-vn/batteries-and-chargers/vhfm3-charger.html>
  - [[Fronius TagID]] (V): <https://www.fronius.com/en/battery-charging-technology/our-solutions/individual-battery-charging-solutions/battery-sensor-tagid>
  - [[AMETEK Prestolite Power WBID Pro]] (V): <https://www.prestolitepower.com/products/datadevices/wbid-pro>
  - [[EnerSys Wi-iQ]] (V): <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>
  - [[Philadelphia Scientific eGO!pro]] (V): <https://www.phlsci.com/products/ego-battery-performance-monitors/ego-pro/>
  - [[Philadelphia Scientific eGO!plus]] (V): <https://www.phlsci.com/product-lines/battery-performance-monitors/ego-plus/>
  - [[Philadelphia Scientific eGO!core]] (V): <https://phlsci.com/product-lines/ego-battery-performance-monitors/ego-core>
  - [[Philadelphia Scientific eGO!Mini]] (V): <https://www.phlsci.com/media/151762/ego-mini-egou-ps-ssh-doc0184-eng.pdf>
  - [[Philadelphia Scientific SmartBlinky Pro]] (V): <https://www.mhwmag.com/?p=7981>
  - [[Energywith withBMS BMU]] (C): <https://www.energy-with.com/en/solutions/forklift-battery-monitoring/>
  - [[Flow-Rite Eagle Eye Elite IV]] (C): <https://www.flow-rite.com/category/application/battery-monitoring/>
  - [[Flow-Rite Eagle Eye Essential IV]] (V): <https://mhwmag.com/?p=86116>
  - [[Power Designers PowerTrac SP+]] (V): <https://powerdesignerssibex.com/wp-content/uploads/2024/04/PD-TRA-SP_PowerTrac_SP_BatteryDataLogger.pdf>
  - [[Power Designers PowerTrac 3]] (V): <https://powerdesignerssibex.com/powertrac-3-wireless-battery-monitor/>
  - [[HOPPECKE trak collect]] (V): <https://www.hoppecke.com/uk/product/trak-collect-premium/> <https://www.hoppecke.com/uk/news/hoppecke-trak-collect-taking-lead-acid-batteries-into-the-digital-age/>
  - [[Crown Battery Health Monitor]] (V): <https://www.mhlnews.com/new-products/forklift-battery-performance-monitor-new-products>
  - [[Raymond iBattery]] (V): <https://raymondcorp.com/news/2010/ibattery-launch>
  - [[Hyster Battery Tracker]] (V): <https://refrigeratedfrozenfood.com/articles/91289-forklift-battery-management-solution-monitors-health-usage>
  - [[Yale Battery Vision]] (V): <https://www.mhlnews.com/new-products/forklift-battery-monitor-new-products>
  - [[Access Control Group CellTrac]] (V): <https://www.mhlnews.com/archive/celltrac>
  - [[Exide Motion+ EasyMonitor]] (V): <https://www.exidegroup.com/en/product/easymonitor> <https://exidegroup.com/it/en/document/gnb-pro-20-battery-protection-brochure>
  - [[Advanced Charging Technologies BATTview]] (V): <https://og.mhi.org/media/members/41607/133717592244521430.pdf>
  - [[Exide MARATHON Battery]] (V): <https://www.exidegroup.com/eu/sites/default/files/2021-08/GNB_MP_Overview_EN_web.pdf>
  - [[Deka HydraSaver Battery]] (V): <https://www.eastpennmanufacturing.com/?p=5240>
  - [[Crown Battery Acid Indicators]] (V): <https://www.crown.com/en-ca/batteries-and-chargers/>
  - [[Exide Automatic Watering System and Level Sensor]] (V): <https://www.exidegroup.com/eu/sites/default/files/2021-08/GNB_MP_Overview_EN_web.pdf>
  - [[EnerSys iQ Mini]] (V): <https://www.enersys.com/496a7c/globalassets/documents/product-documentation/_enersys/glob/legacy/battery-management/iq-mini/glob-en-fly-iqm-0924-apac.pdf>
- **Extra (round 30):** documented for 6 of 21 battery maker groups (29 percent), delivered by devices or software (Battery Sensor Element Design); rule and caveats in [[Extra Functions Register]].

## Implementation Allocation

The reusable realization is [[Electrolyte Level Sensing Design]]. Physical implementations range from standalone probe assemblies to multi-function sensor assemblies and controller sensor-input circuits. [[Electrolyte Level Measurement Circuit]] represents the general electronic readout role, while [[Electrolyte Level Acquisition Firmware]] applies to controller-based monitors that qualify, log, or report the level state.

### Known implementation paths

- **Capacitive probe:** [[Capacitive Electrolyte Level Probe]] -> [[Capacitive Electrolyte Level Sensor Assembly]] -> [[Capacitive Electrolyte Probe Element]]. Verified for the Flow-Rite Eagle Eye sensor family; Flow-Rite states that capacitive sensing avoids sensing current through the probe.
- **Electronic in-cell probe:** [[Electronic In-Cell Electrolyte Probe]] -> [[Electronic Electrolyte Probe Assembly]]. Verified for [[Philadelphia Scientific SmartBlinky Pro]]. The maker identifies an electronic probe and patented Smart Sensing but does not publish the transduction principle.
- **Variable-length probe:** [[Variable-Length Electrolyte Level Probe]] -> [[Variable-Length Electrolyte Probe Assembly]]. Verified for [[Power Designers PowerTrac 3]].
- **Cell-connector multi-function sensor:** [[Cell-Connector Electrolyte Level Sensing]] + [[Wrap-Around Cell Connector Probe]] -> [[Wrap-Around Cell Connector Sensor Assembly]]. Verified for [[Exide Motion+ EasyMonitor]].
- **Low-current electrical input:** [[Low-Current Electrolyte Level Input]] -> [[Low-Current Electrolyte Level Input Circuit]]. Verified for [[HOPPECKE trak collect]] from its published 11.3 V / 55 µA trigger / 100 µA maximum electrolyte-level input.

### Products intentionally left unspecialized

Products that state only "electrolyte sensor," "level sensor," "water-level detector," or equivalent remain linked to the Function without a more specific child Design unless the available evidence establishes probe form, mounting, or electrical behavior. This includes several BMID-class products and monitoring devices; no conductive, capacitive, optical, or other mechanism is inferred solely from the presence of level sensing.

## Aliases


## Former ids
