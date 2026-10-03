---
type: Function
subtype:
id: FUNC-00016
uid: 20261002164202362skellyspencer
status: Draft
tags:
  - battery-monitoring
  - product-function
describedBy:
  - "[[Metric - Charger Link]]"
performedBy:
  - "[[AMETEK Prestolite Power BID with Ah Accumulator]]"
  - "[[AMETEK Prestolite Power BID]]"
  - "[[Fronius TagID]]"
  - "[[PosiCharge BMID]]"
  - "[[EnerSys Wi-iQ]]"
  - "[[HOPPECKE trak collect]]"
---

# Report Battery Temperature to Charger

## Definition

Give the charger the battery temperature so the charger can adjust its charge.

## Notes

- Often implemented together with [[Identify Battery to Charger]] but stated separately by some vendors.
- Product links are made only where a source states the behavior; no link means unknown, not absent. Overview: [[Function Map]].
- No Requirement is linked: nothing here is a committed requirement, so model-health will show these Functions without satisfied Requirements. That gap is intentional.
- **Sources** (product, evidence level, web page):
  - [[PosiCharge BMID]] (V): <https://www.posicharge.com/faq/>
  - [[Fronius TagID]] (V): <https://www.fronius.com/en/battery-charging-technology/our-solutions/individual-battery-charging-solutions/battery-sensor-tagid>
  - [[AMETEK Prestolite Power BID]] (V): <https://www.prestolitepower.com/products/datadevices/bid>
  - [[AMETEK Prestolite Power BID with Ah Accumulator]] (V): <https://www.prestolitepower.com/-/media/ametekprestolite/documentation/bid/bid-ah-accumulator-datasheet-aug-2018.pdf>
  - [[HOPPECKE trak collect]] (V): <https://hoppecke.com/en/stories/show/switch-from-gas-to-electrically-powered-forklift-trucks>
  - [[EnerSys Wi-iQ]] (V): <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf>

## Aliases


## Former ids
