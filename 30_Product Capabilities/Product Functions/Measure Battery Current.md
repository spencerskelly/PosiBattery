---
type: Function
subtype:
id: FUNC-00002
uid: 20261002164202348skellyspencer
status: Draft
tags:
  - battery-monitoring
  - extra
  - product-function
subtypeOf:
  - "[[Sense Battery State]]"
dependsOn:
  - "[[Current Sensing Design]]"
describedBy:
  - "[[Metric - Current Measurement]]"
performedBy:
  - "[[Stryten M-Series Li610 Battery]]"
  - "[[PosiCharge Battery Rx]]"
  - "[[PosiCharge PosiGuard]]"
  - "[[Advanced Charging Technologies BATTview]]"
  - "[[EnerSys Wi-iQ]]"
  - "[[Energywith withBMS BMU]]"
  - "[[Exide Motion+ EasyMonitor]]"
  - "[[HOPPECKE trak collect]]"
  - "[[Hyster Battery Tracker]]"
  - "[[Philadelphia Scientific eGO!pro]]"
  - "[[Power Designers PowerTrac 3]]"
  - "[[Power Designers PowerTrac DT3]]"
  - "[[Power Designers PowerTrac Monitor]]"
  - "[[Power Designers PowerTrac SP+]]"
  - "[[Yale Battery Vision]]"
  - "[[Green Cubes SAFEFlex Battery]]"
  - "[[Exide Solition Light Traction Battery]]"
  - "[[Battery Current Acquisition Firmware]]"
  - "[[Battery Current Measurement Circuit]]"
realizedBy:
  - "[[Current Sensing Design]]"
---

# Measure Battery Current

## Definition

Measure current into and out of the battery.

## Notes

- Sensing method is a design choice: external shunt, shuntless, Hall effect or split-core. See the design notes.
- Product links are made only where a source states the behavior; no link means unknown, not absent. Overview: [[Function Map]].
- No Requirement is linked: nothing here is a committed requirement, so model-health will show these Functions without satisfied Requirements. That gap is intentional.
- **Sources** (product, evidence level, web page):
  - [[PosiCharge Battery Rx]] (V): <https://www.posicharge.com/source/PDF/BatteryRx.pdf>
  - [[PosiCharge PosiGuard]] (V): <https://posicharge.com/products/posiguard/>
  - [[EnerSys Wi-iQ]] (V): <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>
  - [[Philadelphia Scientific eGO!pro]] (V): <https://www.phlsci.com/media/vbohieng/egopro-ssh-ps-us-en-doc0642.pdf> <https://www.phlsci.co.uk/ego/ego-pro/>
  - [[Energywith withBMS BMU]] (C): <https://www.energy-with.com/en/solutions/forklift-battery-monitoring/>
  - [[Power Designers PowerTrac SP+]] (V): <https://www.powerdesignerssibex.com/powertrac-sp/>
  - [[Power Designers PowerTrac DT3]] (V): <https://www.powerdesignerssibex.com/wp-content/uploads/2024/04/PDS-PT-DT3_PowerTracDT3.pdf>
  - [[Power Designers PowerTrac 3]] (V): <https://powerdesignerssibex.com/powertrac-3-wireless-battery-monitor/>
  - [[Power Designers PowerTrac Monitor]] (V): <https://powerdesignerssibex.com/powertrac-monitor/>
  - [[HOPPECKE trak collect]] (V): <https://www.hoppecke.com/uk/product/trak-collect-premium/> <https://www.hoppecke.com/uk/news/hoppecke-trak-collect-taking-lead-acid-batteries-into-the-digital-age/>
  - [[Hyster Battery Tracker]] (V): <https://refrigeratedfrozenfood.com/articles/91289-forklift-battery-management-solution-monitors-health-usage>
  - [[Yale Battery Vision]] (V): <https://www.mhlnews.com/new-products/forklift-battery-monitor-new-products>
  - [[Exide Motion+ EasyMonitor]] (V): <https://www.exidegroup.com/en/document/easy-monitor-leaflet>
  - [[Advanced Charging Technologies BATTview]] (V): <https://og.mhi.org/media/members/41607/133717592244521430.pdf>
  - [[Stryten M-Series Li610 Battery]] (V): <https://www.businesswire.com/news/home/20260413514429/en/Stryten-Energy-Launches-New-MSeries-Li610-LithiumIon-Battery-at-MODEX>
  - [[Green Cubes SAFEFlex Battery]] (V): <https://www.forkliftaction.com/cards/1518/green-cubes-technology/default.aspx>
  - [[Exide Solition Light Traction Battery]] (V): <https://exidegroup.com/us/en/document/solition-light-traction-battery-leaflet>
- **Extra (round 30):** documented for 4 of 21 battery maker groups (19 percent), delivered by devices or software (Current Sensing Design); rule and caveats in [[Extra Functions Register]].

## Aliases


## Former ids
