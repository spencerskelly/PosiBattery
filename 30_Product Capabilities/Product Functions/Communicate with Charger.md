---
type: Function
subtype:
id: FUNC-00017
uid: 20261002164202363skellyspencer
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
  - "[[EnerSys NexSys iON Battery]]"
  - "[[Toyota Lithium-Ion 5-35 Battery Series]]"
  - "[[PosiCharge BMID]]"
  - "[[PosiCharge Battery Rx]]"
  - "[[PosiCharge PosiGuard]]"
  - "[[AMETEK Prestolite Power TruBid]]"
  - "[[AMETEK Prestolite Power WBID]]"
  - "[[Advanced Charging Technologies BATTview]]"
  - "[[EnerSys Wi-iQ]]"
  - "[[HOPPECKE trak collect]]"
  - "[[Power Designers PowerTrac 3]]"
  - "[[Power Designers PowerTrac SP+]]"
  - "[[Stryten inCOMMAND]]"
  - "[[Exide Solition Light Traction Battery]]"
  - "[[Crown V-Force BMID]]"
  - "[[Battery-Charger Communication Firmware]]"
realizes:
  - "[[Charge a BMID-Equipped Battery Using Battery Information]]"
  - "[[Integrate a BMID with Charger Vehicle and Fleet Systems]]"
  - "[[Integrate the Battery with Truck and Charger Controls]]"
dependsOn:
  - "[[Battery-Charger Data Communication Design]]"
realizedBy:
  - "[[Battery-Charger Data Communication Design]]"
---

# Communicate with Charger

## Definition

Exchange data with a charger in either direction.

## Notes

- Broader than the two charger functions above; use it where a source says the device communicates with the charger without saying what is exchanged.
- Product links are made only where a source states the behavior; no link means unknown, not absent. Overview: [[Function Map]].
- No Requirement is linked: nothing here is a committed requirement, so model-health will show these Functions without satisfied Requirements. That gap is intentional.
- **Sources** (product, evidence level, web page):
  - [[PosiCharge BMID]] (V): <https://www.posicharge.com/procoreedge>
  - [[PosiCharge Battery Rx]] (V): <https://www.posicharge.com/source/PDF/BatteryRx.pdf>
  - [[PosiCharge PosiGuard]] (V): <https://posicharge.com/products/posiguard/>
  - [[AMETEK Prestolite Power WBID]] (V): <https://finance.yahoo.com/news/ametek-prestolite-power-launches-wireless-142836825.html>
  - [[AMETEK Prestolite Power TruBid]] (V): <https://dcvelocity.com/articles/31462-ametek-s-trubid-system-accurately-measures-battery-charge>
  - [[EnerSys Wi-iQ]] (V): <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf> <https://integration.enersys.com/493bb4/globalassets/documents/product-documentation/_misc/wi-iq/emea/wi-iq3-battery-monitoring-device-brochure.pdf>
  - [[Power Designers PowerTrac SP+]] (V): <https://powerdesignerssibex.com/wp-content/uploads/2024/04/PD-TRA-SP_PowerTrac_SP_BatteryDataLogger.pdf>
  - [[Power Designers PowerTrac 3]] (V): <https://powerdesignerssibex.com/powertrac-3-wireless-battery-monitor/>
  - [[HOPPECKE trak collect]] (V): <https://www.hoppecke.com/uk/product/trak-collect-premium/> <https://hoppecke.com/en/stories/show/switch-from-gas-to-electrically-powered-forklift-trucks>
  - [[Advanced Charging Technologies BATTview]] (V): <https://og.mhi.org/media/members/41607/133717592244521430.pdf> <https://dcvelocity.com/articles/31570-advanced-charging-technologies-improves-battview-battery-monitors> <https://www.airsideint.com/issue-article/act-moves-into-the-gse-battery-charging-business/>
  - [[Toyota Lithium-Ion 5-35 Battery Series]] (V): <https://themachinemaker.com/news/toyota-material-handling-introduces-advanced-lithium-ion-batteries-to-boost-efficiency-and-productivity/>
  - [[Stryten inCOMMAND]] (V): <https://stryten.com/?p=173790>
  - [[EnerSys NexSys iON Battery]] (V): <https://www.enersys.com/en/about-us/news/enersys_now_offering_lithium_ion_li_ion_battery_to_global_portfolio_of_power_solutions/>
  - [[Exide Solition Light Traction Battery]] (V): <https://exidegroup.com/us/en/document/solition-light-traction-battery-leaflet>
  - [[Crown V-Force BMID]] (V): <https://www.crown.com/content/dam/crown/pdfs/en-us/brochures/products/vhfm3-chargers.pdf>
- **Extra (round 30):** documented for 4 of 21 battery maker groups (19 percent); the reusable behavioral realization is now [[Battery-Charger Data Communication Design]].

## Implementation Allocation

The reusable realization is [[Battery-Charger Data Communication Design]] -> [[Battery-Charger Communication Firmware]].

This behavior is intentionally transport-neutral. Depending on product, the battery-to-charger link may use [[DC-Cable Power-Line Communication]], [[CAN Interface]], serial communication, Bluetooth/BLE, ZigBee, proprietary RF, or another concrete communication interface.

[[Battery Identification and Charger Communication Software Design]] is a specialized child for the narrower case where the primary purpose is to provide battery identity and charge-configuration information.

### Product allocation

Products that explicitly exchange data with a charger can be allocated the generic communication Design even when the published source does not reveal the message set. Concrete transport Designs remain separate and are linked only where published.

The reusable firmware role is allocated at **>=95% engineering confidence** only for electronic monitors/BMS products where charger data exchange necessarily requires executable message/session handling and the internal software partition is not published.

This Function does not imply that the battery controls the charger. Directionality and command authority remain product-specific.

## Aliases


## Former ids
