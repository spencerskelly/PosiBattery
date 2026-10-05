---
type: Function
subtype:
id: FUNC-00003
uid: 20261002164202349skellyspencer
status: Draft
tags:
  - battery-monitoring
  - extra
  - product-function
subtypeOf:
  - "[[Sense Battery State]]"
describedBy:
  - "[[Metric - Temperature Sensing]]"
performedBy:
  - "[[Stryten M-Series Li610 Battery]]"
  - "[[AMETEK Prestolite Power BID with Ah Accumulator]]"
  - "[[AMETEK Prestolite Power BID]]"
  - "[[Crown V-Force BMID]]"
  - "[[Fronius TagID]]"
  - "[[PosiCharge BMID]]"
  - "[[PosiCharge Battery Rx]]"
  - "[[AMETEK Prestolite Power TruBid]]"
  - "[[AMETEK Prestolite Power WBID Pro]]"
  - "[[AMETEK Prestolite Power WBID]]"
  - "[[Access Control Group CellTrac]]"
  - "[[Advanced Charging Technologies BATTview]]"
  - "[[Crown Battery Health Monitor]]"
  - "[[EnerSys Wi-iQ]]"
  - "[[EnerSys iQ Mini]]"
  - "[[Energywith withBMS BMU]]"
  - "[[Exide Motion+ EasyMonitor]]"
  - "[[HOPPECKE trak collect]]"
  - "[[Hyster Battery Tracker]]"
  - "[[Philadelphia Scientific eGO!Mini]]"
  - "[[Philadelphia Scientific eGO!core]]"
  - "[[Philadelphia Scientific eGO!plus]]"
  - "[[Philadelphia Scientific eGO!pro]]"
  - "[[Power Designers PowerTrac 3]]"
  - "[[Power Designers PowerTrac DT3]]"
  - "[[Power Designers PowerTrac Monitor]]"
  - "[[Power Designers PowerTrac SP+]]"
  - "[[Raymond iBattery]]"
  - "[[Yale Battery Vision]]"
  - "[[TUG ALPHA 1 Pushback]]"
  - "[[Green Cubes SAFEFlex Battery]]"
realizes:
  - "[[Inspect Battery Condition Through a BMID]]"
---

# Measure Battery Temperature

## Definition

Measure battery temperature, either of the electrolyte or of the surroundings.

## Notes

- Whether the sensor is immersed in electrolyte differs by product; see [[Electrolyte-Immersed Temperature Sensor]].
- Product links are made only where a source states the behavior; no link means unknown, not absent. Overview: [[Function Map]].
- No Requirement is linked: nothing here is a committed requirement, so model-health will show these Functions without satisfied Requirements. That gap is intentional.
- **Sources** (product, evidence level, web page):
  - [[PosiCharge BMID]] (V): <https://www.posicharge.com/faq/> <https://www.posicharge.com/airport-ground-support-equipment/>
  - [[PosiCharge Battery Rx]] (V): <https://www.posicharge.com/source/PDF/BatteryRx.pdf>
  - [[Crown V-Force BMID]] (V): <https://shop.crown.com/crown/en/Batteries-and-Chargers/Battery-and-Charger-Parts-and-Accessories/Battery-and-Charger-Accessories//p/396525-BTM> <https://crown.com/en-vn/batteries-and-chargers/vhfm3-charger.html>
  - [[Fronius TagID]] (V): <https://www.fronius.com/en/battery-charging-technology/our-solutions/individual-battery-charging-solutions/battery-sensor-tagid>
  - [[AMETEK Prestolite Power BID]] (V): <https://www.prestolitepower.com/products/datadevices/bid>
  - [[AMETEK Prestolite Power BID with Ah Accumulator]] (V): <https://www.prestolitepower.com/-/media/ametekprestolite/documentation/bid/bid-ah-accumulator-datasheet-aug-2018.pdf>
  - [[AMETEK Prestolite Power WBID Pro]] (V): <https://www.prestolitepower.com/products/datadevices/wbid-pro>
  - [[AMETEK Prestolite Power WBID]] (V): <https://finance.yahoo.com/news/ametek-prestolite-power-launches-wireless-142836825.html>
  - [[AMETEK Prestolite Power TruBid]] (V): <https://dcvelocity.com/articles/31462-ametek-s-trubid-system-accurately-measures-battery-charge>
  - [[EnerSys Wi-iQ]] (V): <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>
  - [[EnerSys iQ Mini]] (C): <https://www.enersys.com/496a7c/globalassets/documents/product-documentation/_enersys/glob/legacy/battery-management/iq-mini/glob-en-fly-iqm-0924-apac.pdf>
  - [[Philadelphia Scientific eGO!pro]] (V): <https://www.phlsci.com/products/ego-battery-performance-monitors/ego-pro/>
  - [[Philadelphia Scientific eGO!plus]] (V): <https://www.phlsci.com/product-lines/battery-performance-monitors/ego-plus/>
  - [[Philadelphia Scientific eGO!core]] (V): <https://phlsci.com/product-lines/ego-battery-performance-monitors/ego-core> <https://www.phlsci.com/media/ux3nu5uy/egocore-om-ps-en-us-doc0652.pdf>
  - [[Philadelphia Scientific eGO!Mini]] (V): <https://www.phlsci.com/media/151762/ego-mini-egou-ps-ssh-doc0184-eng.pdf>
  - [[Energywith withBMS BMU]] (C): <https://www.energy-with.com/en/solutions/forklift-battery-monitoring/>
  - [[Power Designers PowerTrac SP+]] (V): <https://www.powerdesignerssibex.com/powertrac-sp/>
  - [[Power Designers PowerTrac DT3]] (V): <https://www.powerdesignerssibex.com/wp-content/uploads/2024/04/PDS-PT-DT3_PowerTracDT3.pdf>
  - [[Power Designers PowerTrac 3]] (V): <https://powerdesignerssibex.com/powertrac-3-wireless-battery-monitor/>
  - [[Power Designers PowerTrac Monitor]] (V): <https://powerdesignerssibex.com/powertrac-monitor/>
  - [[HOPPECKE trak collect]] (V): <https://www.hoppecke.com/uk/product/trak-collect-premium/> <https://www.hoppecke.com/uk/news/hoppecke-trak-collect-taking-lead-acid-batteries-into-the-digital-age/>
  - [[Crown Battery Health Monitor]] (V): <https://www.mhlnews.com/new-products/forklift-battery-performance-monitor-new-products>
  - [[Raymond iBattery]] (V): <https://raymondcorp.com/news/2010/ibattery-launch>
  - [[Hyster Battery Tracker]] (V): <https://refrigeratedfrozenfood.com/articles/91289-forklift-battery-management-solution-monitors-health-usage>
  - [[Yale Battery Vision]] (V): <https://www.mhlnews.com/new-products/forklift-battery-monitor-new-products>
  - [[Access Control Group CellTrac]] (V): <https://www.mhlnews.com/archive/celltrac>
  - [[Exide Motion+ EasyMonitor]] (V): <https://www.exidegroup.com/en/product/easymonitor> <https://exidegroup.com/it/en/document/gnb-pro-20-battery-protection-brochure>
  - [[Advanced Charging Technologies BATTview]] (V): <https://og.mhi.org/media/members/41607/133717592244521430.pdf>
  - [[Stryten M-Series Li610 Battery]] (V): <https://www.businesswire.com/news/home/20260413514429/en/Stryten-Energy-Launches-New-MSeries-Li610-LithiumIon-Battery-at-MODEX>
  - [[TUG ALPHA 1 Pushback]] (V): <https://www.aviationpros.com/ground-support-worldwide/gse/pushbacks-tractors-utility-vehicles/press-release/21160222/textron-gse-textron-gse-introduces-the-tug-alpha-1>
  - [[Green Cubes SAFEFlex Battery]] (V): <https://www.forkliftaction.com/cards/1518/green-cubes-technology/default.aspx>
- **Extra (round 30):** documented for 6 of 21 battery maker groups (29 percent), delivered by devices or software (accessory and software notes); rule and caveats in [[Extra Functions Register]].

## Aliases


## Former ids
