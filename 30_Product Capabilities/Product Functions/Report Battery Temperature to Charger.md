---
type: Function
subtype:
id: FUNC-00016
uid: 20261002164202362skellyspencer
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
  - "[[Fronius TagID]]"
  - "[[PosiCharge BMID]]"
  - "[[EnerSys Wi-iQ]]"
  - "[[HOPPECKE trak collect]]"
  - "[[Crown V-Force BMID]]"
  - "[[Battery-Charger Communication Firmware]]"
realizes:
  - "[[Charge a BMID-Equipped Battery Using Battery Information]]"
satisfies:
  - "[[BMID - Provide Supported Battery Condition Information to Charger]]"
realizedBy:
  - "[[Battery Temperature Reporting to Charger]]"
supportedBy:
dependsOn:
  - "[[Battery Temperature Reporting to Charger]]"
  - "[[Document - PosiCharge BMID FAQ]]"
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
  - [[Crown V-Force BMID]] (V): <https://www.crown.com/content/dam/crown/pdfs/en-us/brochures/products/vhfm3-chargers.pdf>
- **Extra (round 30):** documented for 2 of 21 battery maker groups (10 percent); the implementation is now separated into temperature measurement plus charger communication through [[Battery Temperature Reporting to Charger]].

## Implementation Allocation

The reusable realization is [[Battery Temperature Reporting to Charger]].

This Design composes two existing capabilities:

- [[Battery Temperature Measurement Design]] provides the measured battery-temperature value.
- [[Battery-Charger Data Communication Design]] / [[Battery-Charger Communication Firmware]] delivers that value to the charger.

The previous direct realization through [[Electrolyte-Immersed Temperature Sensor]] was too narrow and semantically incorrect: a sensor can measure temperature but does not, by itself, report that value to a charger.

### Product allocation

[[PosiCharge BMID]], [[EnerSys Wi-iQ]], [[HOPPECKE trak collect]], [[Fronius TagID]], [[AMETEK Prestolite Power BID]], [[AMETEK Prestolite Power BID with Ah Accumulator]], and [[Crown V-Force BMID]] are allocated the generic reporting Design because each explicitly provides battery temperature to a charger.

Where the product already has a modeled charger-communication firmware role, that firmware also performs this Function. The exact temperature message, transport, update rate, and charger compensation behavior remain product-specific.

## Aliases


## Former ids
