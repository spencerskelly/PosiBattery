---
type: Function
subtype:
id: FUNC-00010
uid: 20261002164202356skellyspencer
status: Draft
tags:
  - battery-monitoring
  - extra
  - product-function
subtypeOf:
  - "[[Communicate Battery and Vehicle Data]]"
dependsOn:
  - "[[Data Handling Design]]"
  - "[[Battery Event and Usage Logging Design]]"
describedBy:
  - "[[Metric - Data Storage]]"
performedBy:
  - "[[AMETEK Prestolite Power BID with Ah Accumulator]]"
  - "[[Crown V-Force BMID]]"
  - "[[PosiCharge BMID]]"
  - "[[PosiCharge Battery Rx]]"
  - "[[PosiCharge PosiGuard]]"
  - "[[AMETEK Prestolite Power Site Probe]]"
  - "[[AMETEK Prestolite Power WBID Pro]]"
  - "[[AMETEK Prestolite Power WBID]]"
  - "[[Advanced Charging Technologies BATTview]]"
  - "[[EnerSys Wi-iQ]]"
  - "[[EnerSys iQ Mini]]"
  - "[[Exide Motion+ EasyMonitor]]"
  - "[[HOPPECKE trak collect]]"
  - "[[Philadelphia Scientific eGO!Mini]]"
  - "[[Philadelphia Scientific eGO!c]]"
  - "[[Philadelphia Scientific eGO!core]]"
  - "[[Philadelphia Scientific eGO!plus]]"
  - "[[Philadelphia Scientific eGO!pro]]"
  - "[[Power Designers PowerTrac 3]]"
  - "[[Power Designers PowerTrac DT3]]"
  - "[[Power Designers PowerTrac Monitor]]"
  - "[[Power Designers PowerTrac SP+]]"
  - "[[Raymond iBattery]]"
  - "[[PosiCharge DVS150]]"
  - "[[PosiCharge E-Meter]]"
  - "[[Energywith withBMS BMU]]"
  - "[[Hyster Battery Tracker]]"
  - "[[Yale Battery Vision]]"
  - "[[Battery Event Logger Firmware]]"
  - "[[Event Log Memory]]"
  - "[[Event Time Base]]"
realizes:
  - "[[Document Battery Care for Warranty Compliance]]"
  - "[[Review BMID Battery History and Exceptions]]"
  - "[[Review Battery Care and Warranty Compliance]]"
satisfies:
  - "[[BMID - Retain Battery-Specific Usage History]]"
supportedBy:
realizedBy:
  - "[[Battery Event and Usage Logging Design]]"
  - "[[Document - PosiCharge BMID FAQ]]"
---

# Log Battery Events and Usage

## Definition

Record charge, discharge, temperature and fault events with time stamps for later review.

## Notes

- Storage size is a performance measure; see [[Monitor Comparison Matrix]].
- Product links are made only where a source states the behavior; no link means unknown, not absent. Overview: [[Function Map]].
- No Requirement is linked: nothing here is a committed requirement, so model-health will show these Functions without satisfied Requirements. That gap is intentional.
- **Sources** (product, evidence level, web page):
  - [[PosiCharge BMID]] (V): <https://www.posicharge.com/faq/>
  - [[PosiCharge Battery Rx]] (V): <https://www.posicharge.com/source/PDF/BatteryRx.pdf> <https://posicharge.com/products/battery-rx/>
  - [[PosiCharge PosiGuard]] (V): <https://posicharge.com/products/posiguard/> <https://apps.apple.com/mx/app/posiconnect/id6748969496>
  - [[Crown V-Force BMID]] (V): <https://shop.crown.com/crown/en/Batteries-and-Chargers/Battery-and-Charger-Parts-and-Accessories/Battery-and-Charger-Accessories//p/396525-BTM>
  - [[AMETEK Prestolite Power WBID Pro]] (V): <https://www.prestolitepower.com/products/datadevices/wbid-pro>
  - [[AMETEK Prestolite Power WBID]] (V): <https://www.prestolitepower.com/products/obsolete-products/wbid> <https://finance.yahoo.com/news/ametek-prestolite-power-launches-wireless-142836825.html>
  - [[AMETEK Prestolite Power Site Probe]] (V): <https://www.mhwmag.com/?p=5495>
  - [[EnerSys Wi-iQ]] (V): <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>
  - [[EnerSys iQ Mini]] (C): <https://www.enersys.com/496a7c/globalassets/documents/product-documentation/_enersys/glob/legacy/battery-management/iq-mini/glob-en-fly-iqm-0924-apac.pdf>
  - [[Philadelphia Scientific eGO!pro]] (V): <https://www.phlsci.com/products/ego-battery-performance-monitors/ego-pro/>
  - [[Philadelphia Scientific eGO!plus]] (V): <https://www.phlsci.com/product-lines/battery-performance-monitors/ego-plus/>
  - [[Philadelphia Scientific eGO!core]] (V): <https://phlsci.com/product-lines/ego-battery-performance-monitors/ego-core> <https://www.phlsci.com/media/ux3nu5uy/egocore-om-ps-en-us-doc0652.pdf>
  - [[Philadelphia Scientific eGO!Mini]] (V): <https://www.phlsci.com/media/151762/ego-mini-egou-ps-ssh-doc0184-eng.pdf>
  - [[Philadelphia Scientific eGO!c]] (V): <https://www.ipesearch.co.uk/iOT-technology-for-batteries>
  - [[Power Designers PowerTrac SP+]] (V): <https://www.powerdesignerssibex.com/powertrac-sp/>
  - [[Power Designers PowerTrac DT3]] (V): <https://www.powerdesignerssibex.com/wp-content/uploads/2024/04/PDS-PT-DT3_PowerTracDT3.pdf>
  - [[Power Designers PowerTrac 3]] (V): <https://powerdesignerssibex.com/powertrac-3-wireless-battery-monitor/>
  - [[Power Designers PowerTrac Monitor]] (V): <https://powerdesignerssibex.com/powertrac-monitor/>
  - [[HOPPECKE trak collect]] (V): <https://www.hoppecke.com/uk/product/trak-collect-premium/> <https://www.hoppecke.com/uk/news/hoppecke-trak-collect-taking-lead-acid-batteries-into-the-digital-age/> <https://www.hoppecke.com/uk/news/improved-battery-management-with-trak-collect/>
  - [[Raymond iBattery]] (V): <https://raymondcorp.com/news/2010/ibattery-launch>
  - [[Exide Motion+ EasyMonitor]] (V): <https://www.exidegroup.com/en/product/easymonitor>
  - [[Advanced Charging Technologies BATTview]] (V): <https://og.mhi.org/media/members/41607/133717592244521430.pdf>
  - [[EnerSys iQ Mini]] (V): <https://www.enersys.com/496a7c/globalassets/documents/product-documentation/_enersys/glob/legacy/battery-management/iq-mini/glob-en-fly-iqm-0924-apac.pdf> (also [[Document - EnerSys iQ Mini Flyer (GLOB-EN-FLY-IQM 0924)]])
  - [[AMETEK Prestolite Power BID with Ah Accumulator]] (V): <https://www.prestolitepower.com/-/media/ametekprestolite/documentation/bid/bid-ah-accumulator-datasheet-aug-2018.pdf> (also [[Document - Prestolite BID and BID with Ah Accumulator Data Sheet 1336 (08-18)]])
  - [[PosiCharge DVS150]] (V): <https://posicharge.com/products/dvs150/>
  - [[PosiCharge E-Meter]] (V): <https://posicharge.com/wp-content/uploads/2026/06/E-Meter.pdf>
  - [[Energywith withBMS BMU]] (V): <https://www.energy-with.com/en/solutions/forklift-battery-monitoring/>
  - [[Hyster Battery Tracker]] (V): <https://www.hyster.com/4a9a28/globalassets/coms/hyster/north-america/documents/telematics/0109het6fc001_e_en-us_battery-tracker-flyer.pdf>
  - [[Yale Battery Vision]] (V): <https://www.mhlnews.com/new-products/forklift-battery-monitor-new-products>
- **Extra (round 30):** documented for 5 of 21 battery maker groups (24 percent); the broad [[Data Handling Design]] dependency has been refined to [[Battery Event and Usage Logging Design]].

## Implementation Allocation

The reusable realization is [[Battery Event and Usage Logging Design]] -> [[Battery Event Logger Firmware]].

The logger depends on [[Event Log Memory]] for persistent record retention and on [[Event Time Base]] for timestamp, duration, or sequence association. [[Non-Volatile Event Memory]] remains the storage Design used by the memory component.

This structure intentionally separates:
- **event recognition and record creation** — firmware/software behavior,
- **persistent retention** — memory/storage,
- **time association** — RTC, synchronized time, timer/epoch, or sequence source.

### Product evidence boundaries

Many current products explicitly state event logs, cycle histories, battery history, or retained usage data, which is sufficient to support the generic logging Design. Some products additionally publish memory capacity or a real-time clock; those details can support the concrete storage/time roles individually.

Cloud upload and fleet reporting are downstream behaviors and remain separate Functions. Logging does not require a cloud connection.

The common event schema, sampling interval, timestamp resolution, memory technology, rollover behavior, and retention policy are not asserted across products.

## Aliases


## Former ids
