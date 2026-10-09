---
type: Function
subtype:
id: FUNC-00011
uid: 20261002164202357skellyspencer
status: Draft
tags:
  - battery-monitoring
  - extra
  - product-function
subtypeOf:
  - "[[Inform Users of Battery Condition]]"
performedBy:
  - "[[AMETEK Prestolite Power WBID Pro]]"
  - "[[Advanced Charging Technologies BATTview]]"
  - "[[Crown Battery Health Monitor]]"
  - "[[EnerSys Wi-iQ]]"
  - "[[Power Designers PowerTrac 3]]"
  - "[[Raymond iBattery]]"
  - "[[Hyster Battery Tracker]]"
  - "[[Equalization Event Tracking Firmware]]"
  - "[[Equalization Status Recording Software]]"
realizes:
  - "[[Document Battery Care for Warranty Compliance]]"
  - "[[Review Battery Care and Warranty Compliance]]"
dependsOn:
  - "[[Equalization Event Tracking Design]]"
realizedBy:
  - "[[Equalization Event Tracking Design]]"
  - "[[Review Battery Care and Warranty Compliance]]"
---

# Track Equalization

## Definition

Track whether and when equalization charging occurred.

## Notes

- Appears in fleet-management oriented products; not evidenced for simple indicators.
- Product links are made only where a source states the behavior; no link means unknown, not absent. Overview: [[Function Map]].
- No Requirement is linked: nothing here is a committed requirement, so model-health will show these Functions without satisfied Requirements. That gap is intentional.
- **Sources** (product, evidence level, web page):
  - [[AMETEK Prestolite Power WBID Pro]] (C): <https://www.prestolitepower.com/products/datadevices/wbid-pro>
  - [[EnerSys Wi-iQ]] (V): <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>
  - [[Power Designers PowerTrac 3]] (V): <https://powerdesignerssibex.com/powertrac-3-wireless-battery-monitor/>
  - [[Crown Battery Health Monitor]] (V): <https://www.mhlnews.com/new-products/forklift-battery-performance-monitor-new-products>
  - [[Raymond iBattery]] (V): <https://raymondcorp.com/news/2010/ibattery-launch>
  - [[Advanced Charging Technologies BATTview]] (V): <https://og.mhi.org/media/members/41607/133717592244521430.pdf> <https://dcvelocity.com/articles/31570-advanced-charging-technologies-improves-battview-battery-monitors>
  - [[Hyster Battery Tracker]] (V): <https://www.hyster.com/4a9a28/globalassets/coms/hyster/north-america/documents/telematics/0109het6fc001_e_en-us_battery-tracker-flyer.pdf>
- **Extra (round 30):** documented for 3 of 21 battery maker groups (14 percent), delivered by devices or software; the reusable realization family is now [[Equalization Event Tracking Design]]. Rule and caveats remain in [[Extra Functions Register]].

## Implementation Allocation

The reusable realization is [[Equalization Event Tracking Design]]. Published products report equalization status, equalization history, or accumulated equalization hours, but the detection mechanism is generally not disclosed.

### Local classification alternative

[[Local Equalization Event Classification]] -> [[Equalization Event Tracking Firmware]]

A local monitor can recognize equalization from charge-session measurements or charge-state history, then store completion, timestamp, duration, count, or accumulated equalization hours.

### Reported-status alternative

[[Reported Equalization Status Tracking]] -> [[Equalization Status Recording Software]]

A charger or other authoritative system can explicitly report equalization status or completion, allowing the monitor or fleet software to record it without independently inferring the event.

### Product allocation

The seven currently linked products remain allocated only to the generic [[Equalization Event Tracking Design]]. Their sources establish the tracked outcome but do not establish whether equalization is inferred locally or reported by another system.

Tracking is intentionally separated from controlling or initiating equalization.

## Aliases


## Former ids
