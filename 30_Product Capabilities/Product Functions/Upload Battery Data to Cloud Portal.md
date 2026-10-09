---
type: Function
subtype:
id: FUNC-00020
uid: 20261002164202366skellyspencer
status: Draft
tags:
  - battery-monitoring
  - extra
  - product-function
subtypeOf:
  - "[[Communicate Battery and Vehicle Data]]"
dependsOn:
  - "[[Wireless Interface Design]]"
  - "[[Cloud Portal Integration]]"
  - "[[Cloud Battery Data Upload Design]]"
performedBy:
  - "[[PosiCharge Battery Rx]]"
  - "[[PosiCharge PosiGuard]]"
  - "[[AMETEK Prestolite Power WBID Pro]]"
  - "[[Advanced Charging Technologies BATTview]]"
  - "[[Crown Battery Health Monitor]]"
  - "[[EnerSys iQ Mini]]"
  - "[[Energywith withBMS BMU]]"
  - "[[HOPPECKE trak collect]]"
  - "[[Hyster Battery Tracker]]"
  - "[[Philadelphia Scientific eGO!Mini]]"
  - "[[Philadelphia Scientific eGO!c]]"
  - "[[Philadelphia Scientific eGO!core]]"
  - "[[Philadelphia Scientific eGO!pro]]"
  - "[[Raymond iBattery]]"
  - "[[Yale Battery Vision]]"
  - "[[Philadelphia Scientific eGO!gateway]]"
  - "[[PosiCharge PosiLink]]"
  - "[[PosiCharge PosiNet]]"
  - "[[Philadelphia Scientific eGO!plus]]"
  - "[[Power Designers PowerTrac 3]]"
  - "[[Cloud Battery Data Upload Service]]"
  - "[[Battery Data Gateway Upload Service]]"
realizes:
  - "[[Document Battery Care for Warranty Compliance]]"
  - "[[Monitor and Manage Chargers and Batteries Across Sites]]"
  - "[[Review BMID Battery History and Exceptions]]"
  - "[[Integrate a BMID with Charger Vehicle and Fleet Systems]]"
  - "[[Review Battery Care and Warranty Compliance]]"
realizedBy:
  - "[[Cloud Battery Data Upload Design]]"
---

# Upload Battery Data to Cloud Portal

## Definition

Send battery data to a hosted portal for fleet reporting.

## Notes

- Path may be cellular, gateway or truck-based; see [[Cloud Portal Integration]].
- Product links are made only where a source states the behavior; no link means unknown, not absent. Overview: [[Function Map]].
- No Requirement is linked: nothing here is a committed requirement, so model-health will show these Functions without satisfied Requirements. That gap is intentional.
- **Sources** (product, evidence level, web page):
  - [[PosiCharge Battery Rx]] (V): <https://www.posicharge.com/source/files/PosiCharge_80_200_300-SpecSheet-04302019.pdf> <https://posicharge.com/products/battery-rx/>
  - [[PosiCharge PosiGuard]] (V): <https://posicharge.com/products/posiguard/>
  - [[AMETEK Prestolite Power WBID Pro]] (V): <https://www.prestolitepower.com/products/datadevices/wbid-pro>
  - [[EnerSys iQ Mini]] (V): <https://www.enersys.com/en-gb/products/monitoring-and-fleet-management/data-logger/enersys/iq-mini/> <https://www.enersys.com/en/about-us/news/enersys-to-showcase-advanced-battery-management-at-2024-north-american-issa-show/>
  - [[Philadelphia Scientific eGO!pro]] (V): <https://www.phlsci.com/media/vbohieng/egopro-ssh-ps-us-en-doc0642.pdf>
  - [[Philadelphia Scientific eGO!core]] (V): <https://phlsci.com/product-lines/ego-battery-performance-monitors/ego-core>
  - [[Philadelphia Scientific eGO!gateway]] (V): <https://www.phlsci.com/products/ego-battery-performance-monitors/ego-gateway/>
  - [[Philadelphia Scientific eGO!Mini]] (V): <https://www.phlsci.com/media/151762/ego-mini-egou-ps-ssh-doc0184-eng.pdf>
  - [[Philadelphia Scientific eGO!c]] (V): <https://warehousenews.co.uk/?p=68147>
  - [[Energywith withBMS BMU]] (C): <https://www.energy-with.com/en/solutions/forklift-battery-monitoring/>
  - [[HOPPECKE trak collect]] (V): <https://warehousenews.co.uk/?p=103814>
  - [[Crown Battery Health Monitor]] (V): <https://www.mhlnews.com/new-products/forklift-battery-performance-monitor-new-products>
  - [[Raymond iBattery]] (V): <https://test-iwarehouseknows.raymondcorp.com/products/battery-monitoring>
  - [[Hyster Battery Tracker]] (V): <https://refrigeratedfrozenfood.com/articles/91289-forklift-battery-management-solution-monitors-health-usage>
  - [[Yale Battery Vision]] (V): <https://www.mhlnews.com/new-products/forklift-battery-monitor-new-products>
  - [[Advanced Charging Technologies BATTview]] (V): <https://og.mhi.org/media/members/41607/133717592244521430.pdf> <https://www.airsideint.com/issue-article/act-moves-into-the-gse-battery-charging-business/>
  - [[PosiCharge PosiLink]] (V): <https://posicharge.com/products/posilink/>
  - [[PosiCharge PosiNet]] (V): <https://og.mhi.org/media/members/16696/131261342583679925.pdf>
  - [[Philadelphia Scientific eGO!plus]] (V): <https://www.phlsci.com/product-lines/battery-performance-monitors/ego-plus/>
  - [[Power Designers PowerTrac 3]] (V): <https://powerdesignerssibex.com/wp-content/uploads/2024/04/PDS-PT-PT3_PowerTrac-3.pdf>
- **Extra (round 30):** documented for 4 of 21 battery maker groups (19 percent); [[Cloud Portal Integration]] remains the hosted-service dependency, while [[Cloud Battery Data Upload Design]] represents the actual upload behavior.

## Implementation Allocation

The reusable realization is [[Cloud Battery Data Upload Design]].

### Direct device path

[[Direct Device Cloud Upload]] -> [[Cloud Battery Data Upload Service]]

A field device can authenticate and send battery data directly to a hosted service over a WAN-capable connection such as cellular, Wi-Fi, or Ethernet. No product is assigned to this child Design unless the source establishes a direct device-to-cloud path.

### Gateway-mediated path

[[Gateway-Mediated Cloud Upload]] -> [[Battery Data Gateway Upload Service]]

[[Philadelphia Scientific eGO!gateway]] is the clearest verified implementation: it collects eGO! monitor data locally over Bluetooth and uploads it to batterymanagement.net over cellular.

### Cloud-service boundary

[[Cloud Portal Integration]] represents the hosted portal relationship and remains a dependency. Upload behavior is modeled separately because a product can integrate with a cloud portal through different field architectures.

Products that state cloud/portal reporting but do not expose whether they connect directly or through a gateway remain at the generic [[Cloud Battery Data Upload Design]] level.

## Aliases


## Former ids
