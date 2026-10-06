---
type: Function
subtype:
id: FUNC-00013
uid: 20261002164202359skellyspencer
status: Draft
tags:
  - battery-monitoring
  - extra
  - product-function
subtypeOf:
  - "[[Inform Users of Battery Condition]]"
dependsOn:
  - "[[Warning and Display Device Design]]"
performedBy:
  - "[[HOPPECKE trak uplift iQ Battery]]"
  - "[[AMETEK Prestolite Power TruBid]]"
  - "[[AMETEK Prestolite Power WBID Pro]]"
  - "[[Access Control Group CellVue]]"
  - "[[EnerSys Wi-iQ]]"
  - "[[EnerSys iQ Mini]]"
  - "[[Exide Motion+ EasyMonitor]]"
  - "[[HOPPECKE trak collect]]"
  - "[[Philadelphia Scientific eGO!Mini]]"
  - "[[Philadelphia Scientific eGO!c]]"
  - "[[Philadelphia Scientific eGO!plus]]"
  - "[[Philadelphia Scientific eGO!pro]]"
  - "[[Crown Battery Acid Indicators]]"
  - "[[Flow-Rite Eagle Eye Elite IV]]"
  - "[[Flow-Rite Eagle Eye Essential IV]]"
  - "[[Philadelphia Scientific SmartBlinky Pro]]"
  - "[[Fronius TagID]]"
  - "[[Philadelphia Scientific eGO!core]]"
realizedBy:
  - "[[Warning and Display Device Design]]"
realizes:
  - "[[Know Battery State Before and During the Shift]]"
  - "[[Start a Shift and Confirm Vehicle Energy Readiness]]"
---

# Indicate Battery Status Locally

## Definition

Show battery or maintenance status at the battery with a light or gauge.

## Notes

- Distinct from [[Display Battery Status to Operator]], which is at the vehicle.
- Product links are made only where a source states the behavior; no link means unknown, not absent. Overview: [[Function Map]].
- No Requirement is linked: nothing here is a committed requirement, so model-health will show these Functions without satisfied Requirements. That gap is intentional.
- **Sources** (product, evidence level, web page):
  - [[AMETEK Prestolite Power WBID Pro]] (V): <https://www.prestolitepower.com/products/datadevices/wbid-pro>
  - [[AMETEK Prestolite Power TruBid]] (V): <https://dcvelocity.com/articles/31462-ametek-s-trubid-system-accurately-measures-battery-charge>
  - [[EnerSys Wi-iQ]] (V): <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf> <https://www.enersys.com/en-gb/about-us/news/enersys_suite_of_power_management_tools_elevate_fleet_performance/>
  - [[EnerSys iQ Mini]] (V): <https://www.enersys.com/en/about-us/news/enersys-to-showcase-advanced-battery-management-at-2024-north-american-issa-show/>
  - [[Philadelphia Scientific eGO!pro]] (V): <https://www.phlsci.com/products/ego-battery-performance-monitors/ego-pro/>
  - [[Philadelphia Scientific eGO!plus]] (V): <https://www.phlsci.com/product-lines/battery-performance-monitors/ego-plus/>
  - [[Philadelphia Scientific eGO!Mini]] (V): <https://www.phlsci.com/media/151762/ego-mini-egou-ps-ssh-doc0184-eng.pdf> <https://warehousenews.co.uk/?p=68147>
  - [[Philadelphia Scientific eGO!c]] (V): <https://www.ipesearch.co.uk/iOT-technology-for-batteries>
  - [[Philadelphia Scientific SmartBlinky Pro]] (V): <https://www.mhwmag.com/?p=7981>
  - [[Flow-Rite Eagle Eye Elite IV]] (C): <https://www.flow-rite.com/category/application/battery-monitoring/>
  - [[Flow-Rite Eagle Eye Essential IV]] (V): <https://mhwmag.com/?p=86116>
  - [[HOPPECKE trak collect]] (V): <https://www.hoppecke.com/uk/product/trak-uplift-iq/>
  - [[Access Control Group CellVue]] (V): <https://www.mhlnews.com/archive/celltrac>
  - [[Exide Motion+ EasyMonitor]] (V): <https://www.exidegroup.com/en/product/easymonitor>
  - [[HOPPECKE trak uplift iQ Battery]] (V): <https://www.hoppecke.com/uk/product/trak-uplift-iq/>
  - [[Crown Battery Acid Indicators]] (V): <https://www.crown.com/en-ca/batteries-and-chargers/>
  - [[Crown V-HFM3 Tower Light Kit]] (V): <https://www.crown.com/content/dam/crown/pdfs/en-us/brochures/products/vhfm3-chargers.pdf>
  - [[PosiCharge Three-Color Stack Light]] (V): <https://posicharge.com/accessories/>
  - [[Fronius TagID]] (V): <https://manuals.fronius.com/html/4204102645/en-US.html>
  - [[Philadelphia Scientific eGO!core]] (V): <https://phlsci.com/product-lines/ego-battery-performance-monitors/ego-core>
- **Extra (round 30):** documented for 4 of 21 battery maker groups (19 percent), delivered by devices or software (Warning and Display Device Design); rule and caveats in [[Extra Functions Register]].

## Implementation Allocation

The common Design dependency remains [[Warning and Display Device Design]] because local battery status can be presented through indicator or display branches.

### Known implementation paths

- **LED indication:** [[Local LED Indicator]] -> [[Status Indicator Driver Circuit]] -> [[LED Status Indicator Element]]. The LED element is verified wherever the product source explicitly identifies LEDs; the internal driver circuit is generally an **>=95% engineering-confidence assumption** unless a driver board is published.
- **Integrated LCD:** [[Integrated LCD Display]] -> [[LCD Display Interface Circuit]] -> [[LCD Status Display Module]]. Verified as an LCD implementation for [[EnerSys Wi-iQ]] and [[Exide Motion+ EasyMonitor]]; the interface circuit is an **>=95% engineering-confidence assumption** because its topology is not published.
- **Technology-neutral gauge:** [[Battery Status Gauge]] -> [[Battery Status Gauge Display Element]]. Verified for [[Access Control Group CellVue]], whose source calls it a real-time battery gauge but does not identify the display technology.
- **Presentation firmware:** [[Local Status Presentation Firmware]] represents controller-based formatting and state-to-output logic for multi-state local displays and indicators. It is allocated only as an explicit engineering assumption where the product behavior strongly implies controller-based presentation.

Products that merely state an indication without naming LED, LCD, gauge technology, or another visible element remain at the Function level until stronger evidence exists.

### Scope correction

[[Crown V-HFM3 Tower Light Kit]] and [[PosiCharge Three-Color Stack Light]] were removed from this Function because they show **charger/charge-process status**, not battery-mounted status. They now perform [[Indicate Charger Status Locally]].

## Aliases


## Former ids
