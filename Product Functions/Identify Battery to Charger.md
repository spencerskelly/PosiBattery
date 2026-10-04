---
type: Function
subtype:
id: FUNC-00015
uid: 20261002164202361skellyspencer
status: Draft
tags:
  - battery-monitoring
  - extra
  - product-function
subtypeOf:
  - "[[Communicate Battery and Vehicle Data]]"
describedBy:
  - "[[Metric - Charger Link]]"
performedBy:
  - "[[AMETEK Prestolite Power BID with Ah Accumulator]]"
  - "[[AMETEK Prestolite Power BID]]"
  - "[[Crown V-Force BMID]]"
  - "[[PosiCharge BMID]]"
  - "[[EnerSys Wi-iQ]]"
  - "[[Power Designers PowerTrac 3]]"
  - "[[EnerSys NexSys+ Charger]]"
realizes:
  - "[[Charge Each Battery Correctly for Its Chemistry and Condition]]"
---

# Identify Battery to Charger

## Definition

Give a charger the battery's identity and charge parameters so the charger can choose a profile.

## Notes

- Evidence is from vendor descriptions; the physical or logical means differs and is mostly not stated.
- Product links are made only where a source states the behavior; no link means unknown, not absent. Overview: [[Function Map]].
- No Requirement is linked: nothing here is a committed requirement, so model-health will show these Functions without satisfied Requirements. That gap is intentional.
- **Sources** (product, evidence level, web page):
  - [[PosiCharge BMID]] (V): <https://www.posicharge.com/faq/>
  - [[Crown V-Force BMID]] (V): <https://shop.crown.com/crown/en/Batteries-and-Chargers/Battery-and-Charger-Parts-and-Accessories/Battery-and-Charger-Accessories//p/396525-BTM>
  - [[AMETEK Prestolite Power BID]] (V): <https://www.prestolitepower.com/products/datadevices/bid>
  - [[AMETEK Prestolite Power BID with Ah Accumulator]] (V): <https://www.prestolitepower.com/-/media/ametekprestolite/documentation/bid/bid-ah-accumulator-datasheet-aug-2018.pdf>
  - [[Power Designers PowerTrac 3]] (V): <https://powerdesignerssibex.com/powertrac-3-wireless-battery-monitor/>
  - [[EnerSys Wi-iQ]] (V): <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf>
  - [[EnerSys NexSys+ Charger]] (V): <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf> (also [[Document - EnerSys IMPAQ and NexSys+ Charger Product Guide (AMER 0125)]])
- **Extra (round 30):** documented for 2 of 21 battery maker groups (10 percent), delivered by devices or software (accessory and software notes); rule and caveats in [[Extra Functions Register]].

## Aliases


## Former ids
