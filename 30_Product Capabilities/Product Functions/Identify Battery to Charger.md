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
  - "[[Fronius TagID]]"
  - "[[PosiCharge Battery Rx]]"
  - "[[Battery Identification and Charger Communication Firmware]]"
  - "[[PosiCharge PosiGuard]]"
realizes:
  - "[[Charge a BMID-Equipped Battery Using Battery Information]]"
  - "[[Charge Each Battery Correctly for Its Chemistry and Condition]]"
satisfies:
  - "[[BMID - Provide Battery Identity to Compatible Charger]]"
supportedBy:
  - "[[Document - PosiCharge BMID FAQ]]"
realizedBy:
  - "[[Battery Identification and Charger Communication Software Design]]"
---

# Identify Battery to Charger

## Definition

Give a charger the battery's identity and charge parameters so the charger can choose a profile.

## Notes

- Evidence is from vendor descriptions; the physical or logical means differs and is mostly not stated.
- Product links are made only where a source states the behavior; no link means unknown, not absent. Overview: [[Function Map]].
- The Function now satisfies [[BMID - Provide Battery Identity to Compatible Charger]] and has a modeled implementation allocation.
- **Sources** (product, evidence level, web page):
  - [[PosiCharge BMID]] (V): <https://www.posicharge.com/faq/>
  - [[Crown V-Force BMID]] (V): <https://shop.crown.com/crown/en/Batteries-and-Chargers/Battery-and-Charger-Parts-and-Accessories/Battery-and-Charger-Accessories//p/396525-BTM>
  - [[AMETEK Prestolite Power BID]] (V): <https://www.prestolitepower.com/products/datadevices/bid>
  - [[AMETEK Prestolite Power BID with Ah Accumulator]] (V): <https://www.prestolitepower.com/-/media/ametekprestolite/documentation/bid/bid-ah-accumulator-datasheet-aug-2018.pdf>
  - [[Power Designers PowerTrac 3]] (V): <https://powerdesignerssibex.com/powertrac-3-wireless-battery-monitor/>
  - [[EnerSys Wi-iQ]] (V): <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf>
  - [[EnerSys NexSys+ Charger]] (V): <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf> (also [[Document - EnerSys IMPAQ and NexSys+ Charger Product Guide (AMER 0125)]])
  - [[Fronius TagID]] (V): <https://manuals.fronius.com/html/4204102645/en-US.html>
  - [[PosiCharge Battery Rx]] (V): <https://www.posicharge.com/source/PDF/BatteryRx.pdf>
- **Extra (round 30):** documented for 2 of 21 battery maker groups (10 percent), delivered by devices or software (accessory and software notes); rule and caveats in [[Extra Functions Register]].

## Implementation Allocation

The primary modeled realization is [[Battery Identification and Charger Communication Software Design]], performed by [[Battery Identification and Charger Communication Firmware]].

Shared infrastructure:
- [[Control Circuit]] executes the firmware but is not by itself the complete Function realization.
- [[Communication Interface Circuit]] is an abstract physical-interface family selected by product/variant.

Wired solution family:
- [[Wired Communication Circuit]]
  - [[CAN Communication Circuit]] -> [[CAN Transceiver]]
  - [[Serial Communication Circuit]] -> [[Serial Transceiver]]
- Existing Design definitions used by these circuits include [[CAN Interface]] and [[RS-232 and RS-485 Serial Interface]].

Wireless solution family:
- [[Wireless Communication Circuit]]
  - [[BLE Communication Circuit]] -> [[BLE Radio Module]]
  - [[LoRa Communication Circuit]] -> [[LoRa Radio Module]]
  - [[Wi-Fi Communication Circuit]] -> [[Wi-Fi Radio Module]]
  - [[Custom RF Communication Circuit]] -> [[Custom RF Radio Module]]
- Existing Design definitions used by these circuits include [[Bluetooth Interface]], [[LoRa Interface]], [[Wi-Fi Interface]], and [[Custom RF Interface]].

These are implementation alternatives, not a claim that every product contains every interface.

### Product allocation

- [[PosiCharge BMID]]: the control-circuit and firmware allocation is an explicit **>=95% engineering assumption**, based on public evidence that the electronic device stores battery identity/profile/history and communicates with a charger. No internal schematic or processor identification has been found.
- [[PosiCharge PosiGuard]]: added as a performer using an explicit **>=95% engineering assumption**. PosiGuard is modeled as a BMID-family device and publicly documents charger communication using Serial, CAN, Bluetooth, and optional LoRa. The exact internal identity-message implementation is not public.
- For PosiGuard, CAN, serial, BLE, and LoRa communication circuits are modeled as product parts because those interface types are publicly documented. The exact component topology remains an assumption at circuit abstraction level; no transceiver/module part number is claimed.

## Aliases


## Former ids
