---
type: Object
subtype: electrical
id: OBJ-00079
uid: 20261002191446822skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - charger
subtypeOf:
  - "[[Industrial Modular Charger]]"
performs:
  - "[[Manage Chargers Remotely]]"
  - "[[Compensate Charge for Battery Temperature]]"
  - "[[Adapt Charge to Battery Condition]]"
madeBy:
  - "[[Fronius International]]"
offeredWith:
  - "[[Fronius TagID]]"
hasDesign:
  - "[[Remote Charger Management Design]]"
  - "[[Adaptive Charge Profile Control Design]]"
  - "[[Ri-Based Adaptive Charging]]"
  - "[[Temperature-Compensated Charge Control Design]]"
  - "[[Communicated Battery Temperature Charge Compensation]]"
hasPart:
  - "[[Charger Remote Management Agent]]"
  - "[[Adaptive Charge Profile Control Firmware]]"
  - "[[Temperature Compensation Charge Control Firmware]]"
  - "[[Fronius Charge & Connect]]"
---

# Fronius Selectiva 4.0

## Definition

Fronius lead-acid charger family with the Ri charging process, offered in 2 to 30 kW models including 96 and 120 V.

## Notes

- Fronius says Selectiva 4.0 charges lead-acid batteries with the Ri process that adapts to battery condition, in 2, 3, 8, 16, 18 and 30 kW classes, with a five-year guarantee. Source: Logistics Matters (T2), retrieved 2026-10-02. <https://www.logisticsmatters.co.uk/?p=19654>
- The 96 V and 120 V flyer lists 16 kW and 30 kW models (for example 9250 at 96 V, 250 A), Charger InterLock for parallel batteries, and connection to Fronius Charge & Connect for state of charge, energy use and charger status. Source: Fronius Selectiva 4.0 96V/120V flyer (T1), retrieved 2026-10-02. <https://fronius.com/~/downloads/Perfect%20Charging/Flyer/PC_FLY_Selectiva_4.0_96V-120V_EN_fin-MRM_.pdf>
- **Functions performed, with citations** (V = verified this pass):
  - [[Manage Chargers Remotely]] (V): <https://fronius.com/~/downloads/Perfect%20Charging/Flyer/PC_FLY_Selectiva_4.0_96V-120V_EN_fin-MRM_.pdf>
  - [[Compensate Charge for Battery Temperature]] (V): <https://www.fronius.com/en/battery-charging-technology/our-solutions/individual-battery-charging-solutions/battery-sensor-tagid>
- Fronius says its Ri charging process (in series production since 2013) does not follow a fixed characteristic: it determines the battery's condition from its effective internal resistance Ri, which depends on age, temperature and state of charge, and adapts the characteristic, so every charge has an individual curve, the battery receives only the current it needs, overcharging, gassing and warming are reduced, and overall efficiency reaches up to 84 percent (device 93 percent times charging 90 percent); the Selectiva brochure adds a calendar function for time-controlled charges, a special characteristic for opportunity and fast charging at the push of a button, a refresh characteristic for weak batteries and a deep discharge characteristic for deeply discharged batteries. Source: Fronius Ri charging process page and Selectiva 4.0 brochure (T1), retrieved 2026-10-03. <https://www.fronius.com/en/perfect-charging/our-solutions/technologies/ri-charging-process>
- **Functions performed, with citations:**
  - [[Adapt Charge to Battery Condition]] (V): <https://www.fronius.com/en/perfect-charging/our-solutions/technologies/ri-charging-process>

- **Architecture realization — remote charger management:** published material supports [[Remote Charger Management Design]]. [[Charger Remote Management Agent]] is allocated at **>=95% engineering confidence** because remote management requires a charger-side executable endpoint while the internal software partition is unpublished. The exact commands, permissions, network protocol, and safety handoff remain product-specific.

- **Architecture realization — adaptive charge profile:** published behavior supports [[Adaptive Charge Profile Control Design]] with [[Ri-Based Adaptive Charging]]. [[Adaptive Charge Profile Control Firmware]] is allocated at **>=95% engineering confidence** because the adaptive control behavior is explicit while the internal firmware partition is unpublished.

- **Architecture realization — temperature-compensated charging:** published behavior supports [[Temperature-Compensated Charge Control Design]] with [[Communicated Battery Temperature Charge Compensation]]. [[Temperature Compensation Charge Control Firmware]] is allocated at **>=95% engineering confidence** because the charger must apply temperature-dependent control while its internal software partition is unpublished. Compensation slope, thresholds, filtering, and fault fallback remain product-specific.

## Aliases

- Selectiva 4.0


## Former ids
