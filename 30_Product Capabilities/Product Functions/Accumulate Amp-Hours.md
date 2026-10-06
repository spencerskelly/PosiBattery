---
type: Function
subtype:
id: FUNC-00006
uid: 20261002164202352skellyspencer
status: Draft
tags:
  - battery-monitoring
  - extra
  - product-function
subtypeOf:
  - "[[Sense Battery State]]"
performedBy:
  - "[[Amp-Hour Accumulator Firmware]]"
  - "[[AMETEK Prestolite Power BID with Ah Accumulator]]"
  - "[[AMETEK Prestolite Power Site Probe]]"
  - "[[AMETEK Prestolite Power WBID Pro]]"
  - "[[AMETEK Prestolite Power WBID]]"
  - "[[Access Control Group CellTrac]]"
  - "[[Crown Battery Health Monitor]]"
  - "[[EnerSys Wi-iQ]]"
  - "[[Exide Motion+ EasyMonitor]]"
  - "[[HOPPECKE trak collect]]"
  - "[[Power Designers PowerTrac DT3]]"
  - "[[Power Designers PowerTrac SP+]]"
dependsOn:
  - "[[Current Integration Amp-Hour Accumulation]]"
realizedBy:
  - "[[Current Integration Amp-Hour Accumulation]]"
---

# Accumulate Amp-Hours

## Definition

Accumulate amp-hours of charge and discharge, per event and over the battery's life.

## Notes

- Some products report kWh instead; a product that reports only kWh is not mapped here.
- Amp-hours are accumulated by integrating battery current over time. The current product-backed implementation family is [[Current Integration Amp-Hour Accumulation]].
- [[Inventus Smart Battery Monitor SBM-01]] was removed as a performer on 2026-10-06 because its evidence establishes display/reporting of a lifetime-Ah value received from the battery system, not local integration in the panel monitor.
- Product links are made only where a source states the behavior; no link means unknown, not absent. Overview: [[Function Map]].
- No Requirement is linked: nothing here is a committed requirement, so model-health will show these Functions without satisfied Requirements. That gap is intentional.
- **Sources** (product, evidence level, web page):
  - [[AMETEK Prestolite Power BID with Ah Accumulator]] (V): <https://www.prestolitepower.com/products/datadevices> <https://www.prestolitepower.com/-/media/ametekprestolite/documentation/bid/bid-ah-accumulator-datasheet-aug-2018.pdf>
  - [[AMETEK Prestolite Power WBID Pro]] (V): <https://www.prestolitepower.com/products/datadevices/wbid-pro>
  - [[AMETEK Prestolite Power WBID]] (V): <https://finance.yahoo.com/news/ametek-prestolite-power-launches-wireless-142836825.html>
  - [[AMETEK Prestolite Power Site Probe]] (V): <https://www.mhwmag.com/?p=5495>
  - [[EnerSys Wi-iQ]] (V): <https://www.enersys.com/en-gb/products/monitoring-and-fleet-management/data-logger/enersys/wi-iq/>
  - [[Power Designers PowerTrac SP+]] (V): <https://www.powerdesignerssibex.com/powertrac-sp/>
  - [[Power Designers PowerTrac DT3]] (V): <https://www.powerdesignerssibex.com/wp-content/uploads/2024/04/PDS-PT-DT3_PowerTracDT3.pdf>
  - [[HOPPECKE trak collect]] (V): <https://warehousenews.co.uk/?p=103814>
  - [[Crown Battery Health Monitor]] (V): <https://www.mhlnews.com/new-products/forklift-battery-performance-monitor-new-products>
  - [[Access Control Group CellTrac]] (V): <https://www.mhlnews.com/archive/celltrac>
  - [[Exide Motion+ EasyMonitor]] (V): <https://www.exidegroup.com/en/document/easy-monitor-leaflet> <https://exidegroup.com/it/en/document/gnb-pro-20-battery-protection-brochure>
- **Extra (round 30):** documented for 4 of 21 battery maker groups (19 percent); the reusable implementation dependency is now [[Current Integration Amp-Hour Accumulation]]. Rule and caveats remain in [[Extra Functions Register]].

## Implementation Allocation

The reusable realization is [[Current Integration Amp-Hour Accumulation]], implemented by [[Amp-Hour Accumulator Firmware]].

### Core calculation path

[[Battery Current Measurement Circuit]] -> [[Battery Current Acquisition Firmware]] -> [[Amp-Hour Accumulator Firmware]]

The accumulator integrates signed or direction-aware battery current over elapsed time to maintain charge/discharge Ah totals. Exact sampling rate, integration method, current deadband, zero-offset correction, event-boundary rules, and rollover behavior remain product-specific unless published.

### Verified / high-confidence current-integration implementations

- **[[AMETEK Prestolite Power BID with Ah Accumulator]]:** strongest direct evidence. Prestolite states that it adds current monitoring, samples charge/discharge current more than 100 times per second, and stores every amp-hour including regeneration.
- **[[Power Designers PowerTrac SP+]]:** verified external-shunt current measurement plus charge/discharge Ah since installation and per event.
- **[[Power Designers PowerTrac DT3]]:** verified Hall-effect current measurement plus Ah per event and since installation.
- **[[EnerSys Wi-iQ]]:** verified Hall-effect bidirectional current measurement plus charged/discharged Ah reporting.
- **[[HOPPECKE trak collect]]:** verified shunt current measurement plus charged/discharged Ah and Wh.
- **[[Access Control Group CellTrac]]:** verified shuntless current sensing plus Ah available/used.
- **[[Exide Motion+ EasyMonitor]]:** verified battery-state/usage monitoring with Ah turnover; its exact current-sensing topology is not published.
- **[[AMETEK Prestolite Power WBID]] / [[AMETEK Prestolite Power WBID Pro]]:** persistent battery-resident Ah-in/out history establishes local current integration at **>=95% engineering confidence**, while the current-sensing topology is unpublished.

### Persistent counter state

For products that retain lifetime or non-volatile history, [[Amp-Hour Counter State Memory]] preserves accumulator state and uses the existing [[Non-Volatile Event Memory]] Design. It is not treated as mandatory for a purely session-level accumulator.

### Implementation still unresolved

- [[Crown Battery Health Monitor]] explicitly reports Ah throughput, but the available source does not establish whether integration occurs in the battery monitor or in the InfoLink/cloud layer.
- [[AMETEK Prestolite Power Site Probe]] provides built-in analysis of Ah consumed, but the physical current-input path and calculation location are not stated.

These products remain Function-verified without a specific current-integration architecture allocation.

### Presentation boundary

[[Inventus Smart Battery Monitor SBM-01]] receives battery-system information over CAN and reports lifetime Ah consumed. The panel monitor is therefore a presentation/reporting endpoint for that value, not the modeled accumulator.

## Aliases


## Former ids
