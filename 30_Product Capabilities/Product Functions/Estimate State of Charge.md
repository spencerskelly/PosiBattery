---
type: Function
subtype:
id: FUNC-00007
uid: 20261002164202353skellyspencer
status: Draft
tags:
  - battery-monitoring
  - extra
  - product-function
subtypeOf:
  - "[[Sense Battery State]]"
performedBy:
  - "[[Stryten M-Series Li610 Battery]]"
  - "[[PosiCharge BMID]]"
  - "[[PosiCharge Battery Rx]]"
  - "[[AMETEK Prestolite Power WBID Pro]]"
  - "[[EnerSys Wi-iQ]]"
  - "[[Exide Motion+ EasyMonitor]]"
  - "[[Hyster Battery Tracker]]"
  - "[[Power Designers PowerTrac DT3]]"
  - "[[Power Designers PowerTrac Monitor]]"
  - "[[Raymond iBattery]]"
  - "[[Yale Battery Vision]]"
  - "[[TUG ALPHA 1 Pushback]]"
  - "[[HOPPECKE trak collect]]"
  - "[[State of Charge Estimation Firmware]]"
realizes:
  - "[[Know Battery State Before and During the Shift]]"
  - "[[Inspect Battery Condition Through a BMID]]"
  - "[[Start a Shift and Confirm Vehicle Energy Readiness]]"
realizedBy:
  - "[[State of Charge Estimation Design]]"
supportedBy:
  - "[[Document - PosiCharge GSE BMID Page]]"
---

# Estimate State of Charge

## Definition

Estimate the battery's state of charge from measurements.

## Notes

- Estimation method is not stated by the retrieved product sources for the current commercial allocations; product notes therefore use the generic estimation firmware unless a specific algorithm is established.
- Product links are made only where a source states the behavior; no link means unknown, not absent. Overview: [[Function Map]].
- No Requirement is linked: nothing here is a committed requirement, so model-health will show these Functions without satisfied Requirements. That gap is intentional.
- **Sources** (product, evidence level, web page):
  - [[PosiCharge BMID]] (V): <https://www.posicharge.com/airport-ground-support-equipment/>
  - [[PosiCharge Battery Rx]] (V): <https://www.posicharge.com/source/PDF/BatteryRx.pdf>
  - [[AMETEK Prestolite Power WBID Pro]] (C): <https://www.prestolitepower.com/products/datadevices/wbid-pro>
  - [[EnerSys Wi-iQ]] (V): <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>
  - [[Power Designers PowerTrac DT3]] (V): <https://www.materialhandling247.com/product/powertrac_dt_battery_diagnostics_tool>
  - [[Power Designers PowerTrac Monitor]] (V): <https://powerdesignerssibex.com/powertrac-monitor/>
  - [[Raymond iBattery]] (V): <https://mhlnews.com/archive/article/22045964/raymond-battery-module>
  - [[Hyster Battery Tracker]] (V): <https://refrigeratedfrozenfood.com/articles/91289-forklift-battery-management-solution-monitors-health-usage>
  - [[Yale Battery Vision]] (V): <https://www.mhlnews.com/new-products/forklift-battery-monitor-new-products>
  - [[Exide Motion+ EasyMonitor]] (V): <https://www.exidegroup.com/en/document/easy-monitor-leaflet>
  - [[Stryten M-Series Li610 Battery]] (V): <https://www.businesswire.com/news/home/20260413514429/en/Stryten-Energy-Launches-New-MSeries-Li610-LithiumIon-Battery-at-MODEX>
  - [[TUG ALPHA 1 Pushback]] (V): <https://www.aviationpros.com/ground-support-worldwide/gse/pushbacks-tractors-utility-vehicles/press-release/21160222/textron-gse-textron-gse-introduces-the-tug-alpha-1>
  - [[HOPPECKE trak collect]] (V): <https://warehousenews.co.uk/?p=103814>
- **Extra (round 30):** documented for 4 of 21 battery maker groups (19 percent), delivered by devices or software (accessory and software notes); rule and caveats in [[Extra Functions Register]].

## Implementation Allocation

The primary reusable realization is [[State of Charge Estimation Design]], performed by [[State of Charge Estimation Firmware]] on the shared [[Control Circuit]].

Product-backed implementation loci:
- [[Battery-Monitor State of Charge Estimation]] for battery-mounted monitor/controller products.
- [[Integrated BMS State of Charge Estimation]] for batteries whose integrated BMS supplies the SOC estimate.

Candidate algorithm implementations are represented at the firmware/Object layer:
- [[Voltage-Based State of Charge Estimator Firmware]] — voltage/SOC mapping and optional loaded-voltage/temperature compensation.
- [[Coulomb Counting State of Charge Estimator Firmware]] — integrates battery current from a known/corrected SOC reference.
- [[Hybrid State of Charge Estimator Firmware]] — combines voltage, current, temperature, capacity/aging or model-based corrections.

These candidate firmware implementations are intentionally unallocated until a product source establishes the algorithm.

### Presentation-only endpoints

- [[EnerSys Truck iQ]] reads Wi-iQ data over BLE and displays SOC; it is not modeled as the estimator.
- [[Inventus Smart Battery Monitor SBM-01]] receives battery-system data over CAN and displays SOC; it is not modeled as the estimator.
- Both remain represented through [[Display Battery Status to Operator]].

### Product allocation

- [[PosiCharge BMID]] is allocated [[State of Charge Estimation Firmware]] as a **>=95% engineering assumption** because PosiCharge publicly states that the BMID recognizes state of charge. [[State of Charge Estimation Design]] remains the Function-level general family; the exact algorithm is not published.
- The current BMID evidence establishes voltage measurement, but does not establish whether BMID SOC uses voltage only, current integration, or a hybrid algorithm.
- [[EnerSys Wi-iQ]] is allocated [[State of Charge Estimation Firmware]] at **>=95% engineering confidence** because it locally measures battery voltage/current/temperature and supplies usable SOC to charger/truck interfaces; the exact algorithm is not published.
- [[Exide Motion+ EasyMonitor]] is allocated [[State of Charge Estimation Firmware]] at **>=95% engineering confidence** because it locally acquires battery state/usage data and reports SOC; the exact algorithm is not published.
- Other battery-side products remain Function-linked until their upstream measurement/processing architecture is sufficiently modeled to support a concrete firmware allocation.
- No algorithm-specific SOC firmware subtype is assigned to BMID, Wi-iQ, EasyMonitor, HOPPECKE, or Stryten until stronger product-specific evidence or an explicit engineering decision exists.
- [[PosiCharge PosiGuard]] is **not** allocated this Function or SOC implementation in this pass because the current PosiGuard evidence set does not explicitly establish SOC estimation.

## Aliases


## Former ids
