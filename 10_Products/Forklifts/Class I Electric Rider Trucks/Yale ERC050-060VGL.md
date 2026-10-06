---
type: Object
subtype: electrical
id: OBJ-00147
uid: 20261003084359627skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - forklift-model
subtypeOf:
  - "[[Class I Electric Rider Truck]]"
performs:
  - "[[Display Battery Status to Operator]]"
  - "[[Alert on Abnormal Condition]]"
  - "[[Charge Battery from Standard Power Outlet]]"
hasDesign:
  - "[[Operator Dashboard Abnormal Alert]]"
  - "[[Vehicle-Mounted Display]]"
  - "[[Battery Onboard Charger]]"
hasPart:
  - "[[Vehicle-Mounted Display Module]]"
  - "[[Operator Display Controller Circuit]]"
  - "[[Operator Display HMI Firmware]]"
madeBy:
  - "[[Hyster-Yale]]"
offeredWith:
  - "[[Yale Vision Telemetry]]"
---

# Yale ERC050-060VGL

## Definition

Yale four-wheel electric forklift with a fully integrated lithium-ion battery for indoor and outdoor use.

## Notes

- Yale lists the ERC050-060VGL as a fully integrated lithium-ion four-wheel counterbalance forklift for indoor and outdoor applications; its capacity range is not stated in the retrieved text. Source: Yale ERC page (T1), retrieved 2026-10-03. <https://www.yale.com/en-us/north-america/lithium-ion-forklifts/erc080vhl/>
- Yale says the ERC050-060VGL has a fully integrated lithium-ion battery with no emissions, no battery maintenance, consistent power and a full charge in just over an hour, and a dealer-data page adds state of charge on the truck display, low state-of-charge warnings and early shutdown warnings; the spec sheet describes an onboard charging option for charging through commonly (text cut off in the retrieved copy) available outlets; Yale Vision telemetry is offered. Source: Yale ERC page, Yale spec sheet and dealer-data pages (T1/T3), retrieved 2026-10-03. <https://yale.com/en-us/north-america/lithium-ion-forklifts/erc050-060vgl>
- **Fetch caveat:** the spec sheet sentence on the onboard charging option is cut off after 'commonly'.
- **Functions performed, with citations:**
- **Functions performed, with citations:**
  - [[Display Battery Status to Operator]] (V): <https://www.allmachines.com/forklifts/yale-erc060vgl>
  - [[Alert on Abnormal Condition]] (V): <https://www.allmachines.com/forklifts/yale-erc060vgl>
- **Functions performed, with citations:**
  - [[Charge Battery from Standard Power Outlet]] (V): <https://www.yale.com/globalassets/coms/yale/north-america/documents/trucks/4-wheel-electric/1015ybc1sp002_e_en-us_erc050-060vgl-spec-sheet_view.pdf>
- **Design characteristics, with citations:**
  - [[Battery Onboard Charger]] (V): <https://www.yale.com/globalassets/coms/yale/north-america/documents/trucks/4-wheel-electric/1015ybc1sp002_e_en-us_erc050-060vgl-spec-sheet_view.pdf>

- **Architecture realization — operator battery display:** state of charge and low-charge warnings on the truck display are verified. [[Vehicle-Mounted Display Module]] captures the physical display role. [[Operator Display Controller Circuit]] and [[Operator Display HMI Firmware]] are allocated at **>=95% engineering confidence** because the source does not identify the internal controller, software architecture, or battery-data transport.

- **Architecture realization — abnormal-condition alert:** Yale explicitly states that low state-of-charge and early-shutdown warnings appear on the truck display. [[Operator Dashboard Abnormal Alert]] therefore reuses the existing [[Vehicle-Mounted Display Module]] and [[Operator Display HMI Firmware]] architecture. The battery-data transport and warning-rule implementation are not published.

## Aliases

- ERC050-060VGL


## Former ids
