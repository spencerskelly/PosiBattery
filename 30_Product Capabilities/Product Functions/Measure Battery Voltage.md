---
type: Function
subtype:
id: FUNC-00001
uid: 20261002164202347skellyspencer
status: Draft
tags:
  - battery-monitoring
  - extra
  - product-function
subtypeOf:
  - "[[Sense Battery State]]"
describedBy:
  - "[[Metric - Voltage Measurement]]"
performedBy:
  - "[[Stryten M-Series Li610 Battery]]"
  - "[[Crown V-Force BMID]]"
  - "[[PosiCharge BMID]]"
  - "[[PosiCharge Battery Rx]]"
  - "[[PosiCharge PosiGuard]]"
  - "[[AMETEK Prestolite Power WBID]]"
  - "[[Access Control Group CellTrac]]"
  - "[[Advanced Charging Technologies BATTview]]"
  - "[[EnerSys Wi-iQ]]"
  - "[[Energywith withBMS BMU]]"
  - "[[Exide Motion+ EasyMonitor]]"
  - "[[HOPPECKE trak collect]]"
  - "[[Hyster Battery Tracker]]"
  - "[[Inventus Smart Battery Monitor SBM-01]]"
  - "[[Philadelphia Scientific eGO!Mini]]"
  - "[[Philadelphia Scientific eGO!pro]]"
  - "[[Power Designers PowerTrac 3]]"
  - "[[Power Designers PowerTrac DT3]]"
  - "[[Power Designers PowerTrac Monitor]]"
  - "[[Power Designers PowerTrac SP+]]"
  - "[[Raymond iBattery]]"
  - "[[Yale Battery Vision]]"
  - "[[Green Cubes SAFEFlex Battery]]"
  - "[[Exide Solition Light Traction Battery]]"
  - "[[Battery Voltage Measurement Circuit]]"
  - "[[Battery Voltage Acquisition Firmware]]"
realizes:
  - "[[Inspect Battery Condition Through a BMID]]"
realizedBy:
  - "[[Battery Voltage Measurement Design]]"
---

# Measure Battery Voltage

## Definition

Measure the battery's overall terminal voltage (some products also measure half-battery voltage).

## Notes

- Accuracy and resolution differ by product; only PowerTrac DT3 states a figure (0.1 V accuracy).
- Product links are made only where a source states the behavior; no link means unknown, not absent. Overview: [[Function Map]].
- No Requirement is linked: nothing here is a committed requirement, so model-health will show these Functions without satisfied Requirements. That gap is intentional.
- **Sources** (product, evidence level, web page):
  - [[PosiCharge BMID]] (V): <https://www.posicharge.com/airport-ground-support-equipment/>
  - [[PosiCharge Battery Rx]] (V): <https://www.posicharge.com/source/PDF/BatteryRx.pdf>
  - [[PosiCharge PosiGuard]] (V): <https://posicharge.com/products/posiguard/>
  - [[Crown V-Force BMID]] (V): <https://crown.com/en-vn/batteries-and-chargers/vhfm3-charger.html>
  - [[AMETEK Prestolite Power WBID]] (V): <https://finance.yahoo.com/news/ametek-prestolite-power-launches-wireless-142836825.html>
  - [[EnerSys Wi-iQ]] (V): <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>
  - [[Philadelphia Scientific eGO!pro]] (V): <https://www.phlsci.com/products/ego-battery-performance-monitors/ego-pro/>
  - [[Philadelphia Scientific eGO!Mini]] (V): <https://www.phlsci.com/media/151762/ego-mini-egou-ps-ssh-doc0184-eng.pdf>
  - [[Energywith withBMS BMU]] (C): <https://www.energy-with.com/en/solutions/forklift-battery-monitoring/>
  - [[Power Designers PowerTrac SP+]] (V): <https://www.powerdesignerssibex.com/powertrac-sp/>
  - [[Power Designers PowerTrac DT3]] (V): <https://www.powerdesignerssibex.com/wp-content/uploads/2024/04/PDS-PT-DT3_PowerTracDT3.pdf>
  - [[Power Designers PowerTrac 3]] (V): <https://powerdesignerssibex.com/powertrac-3-wireless-battery-monitor/>
  - [[Power Designers PowerTrac Monitor]] (V): <https://powerdesignerssibex.com/powertrac-monitor/>
  - [[HOPPECKE trak collect]] (V): <https://www.hoppecke.com/uk/product/trak-collect-premium/> <https://www.hoppecke.com/uk/news/hoppecke-trak-collect-taking-lead-acid-batteries-into-the-digital-age/>
  - [[Raymond iBattery]] (V): <https://mhlnews.com/archive/article/22045964/raymond-battery-module>
  - [[Hyster Battery Tracker]] (V): <https://refrigeratedfrozenfood.com/articles/91289-forklift-battery-management-solution-monitors-health-usage>
  - [[Yale Battery Vision]] (V): <https://www.mhlnews.com/new-products/forklift-battery-monitor-new-products>
  - [[Access Control Group CellTrac]] (V): <https://www.mhlnews.com/archive/celltrac>
  - [[Inventus Smart Battery Monitor SBM-01]] (V): <https://inventuspower.com/wp-content/uploads/TDS_Smart-Battery-Monitor_2023-Aug_V1.pdf>
  - [[Exide Motion+ EasyMonitor]] (V): <https://www.exidegroup.com/en/product/easymonitor>
  - [[Advanced Charging Technologies BATTview]] (V): <https://og.mhi.org/media/members/41607/133717592244521430.pdf>
  - [[Stryten M-Series Li610 Battery]] (V): <https://www.businesswire.com/news/home/20260413514429/en/Stryten-Energy-Launches-New-MSeries-Li610-LithiumIon-Battery-at-MODEX>
  - [[Green Cubes SAFEFlex Battery]] (V): <https://www.forkliftaction.com/cards/1518/green-cubes-technology/default.aspx>
  - [[Exide Solition Light Traction Battery]] (V): <https://exidegroup.com/us/en/document/solition-light-traction-battery-leaflet>
- **Extra (round 30):** documented for 6 of 21 battery maker groups (29 percent), delivered by devices or software (accessory and software notes); rule and caveats in [[Extra Functions Register]].

## Implementation Allocation

The primary reusable realization is [[Battery Voltage Measurement Design]], performed jointly by [[Battery Voltage Measurement Circuit]] and [[Battery Voltage Acquisition Firmware]] using shared [[Control Circuit]] resources.

Concrete solution alternatives:
- [[Resistive Divider ADC Voltage Measurement]]
  - [[Precision Resistive Divider Network]]
  - [[Voltage Input Protection and Filter]]
  - [[Analog-to-Digital Converter]]
- [[Isolated Voltage Measurement]]
  - [[Isolated Voltage Measurement Device]]
- [[Mid-Battery Differential Voltage Measurement]]
  - requires [[Mid-Battery Voltage Tap]]
  - uses additional scaled/conditioned ADC measurement to compare battery halves.

### Product allocation

- [[PosiCharge BMID]]: a battery-voltage measurement circuit plus acquisition/scaling firmware is modeled as a **>=95% engineering assumption** because PosiCharge publicly states the BMID recognizes/measures battery voltage. The exact divider, ADC, isolation, and protection topology is not public.
- [[PosiCharge PosiGuard]]: a battery-voltage measurement circuit plus acquisition/scaling firmware is modeled as a **>=95% engineering assumption** because PosiGuard publicly specifies battery-voltage monitoring, an 18–120 V operating range, and 30 mV voltage resolution. The published data does not establish whether the internal circuit is a resistive divider, isolated front end, dedicated monitor IC, or another topology.
- No concrete child topology is assigned to either PosiCharge product until stronger product-specific evidence exists.

## Aliases


## Former ids
