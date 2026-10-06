---
type: Object
subtype: electrical
id: OBJ-00066
uid: 20261002191446809skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - charger
  - lithium
subtypeOf:
  - "[[Industrial Modular Charger]]"
performs:
  - "[[Charge Lithium-Ion Battery]]"
  - "[[Charge Battery Conventionally]]"
  - "[[Charge Battery by Opportunity]]"
  - "[[Charge Battery Fast]]"
  - "[[Compensate Charge for Battery Temperature]]"
hasDesign:
  - "[[Silicon-Carbide Power Stage]]"
  - "[[Modular Power Modules]]"
  - "[[Temperature-Compensated Charge Control Design]]"
offeredBy:
  - "[[Stryten Energy]]"
offeredWith:
  - "[[Stryten M-Series Li600 Battery]]"
  - "[[Stryten M-Series Li610 Battery]]"
hasPart:
  - "[[Temperature Compensation Charge Control Firmware]]"
  - "[[Stryten inCOMMAND]]"
---

# Stryten X-7 Charger

## Definition

Stryten M-Series modular silicon-carbide charger for lead and lithium forklift batteries.

## Notes

- Stryten's X-7 delivers up to 30 kW, handles lithium and other battery types with silicon carbide technology, offers standard, opportunity and fast charge, and now supports 72 to 96 V, with AGM compatibility planned. Source: North American Clean Energy (T2), retrieved 2026-10-02. <https://www.nacleanenergy.com/energy-storage/unlocking-fleet-versatility-while-simplifying-charging-infrastructure>
- Stryten's lineup sheet says X-3 and X-7 chargers use silicon carbide, monitor battery temperature and other parameters in real time, and are available CEC-certified. Source: Stryten lineup sheet (09/2024) (T1), retrieved 2026-10-02. <https://og.mhi.org/media/members/14502/133723547947804003.pdf>
- **Functions performed, with citations** (V = verified this pass):
  - [[Charge Lithium-Ion Battery]] (V): <https://www.nacleanenergy.com/energy-storage/unlocking-fleet-versatility-while-simplifying-charging-infrastructure>
  - [[Charge Battery Conventionally]] (V): <https://www.nacleanenergy.com/energy-storage/unlocking-fleet-versatility-while-simplifying-charging-infrastructure>
  - [[Charge Battery by Opportunity]] (V): <https://www.nacleanenergy.com/energy-storage/unlocking-fleet-versatility-while-simplifying-charging-infrastructure>
  - [[Charge Battery Fast]] (V): <https://www.nacleanenergy.com/energy-storage/unlocking-fleet-versatility-while-simplifying-charging-infrastructure>
- **Design characteristics, with citations:**
  - [[Silicon-Carbide Power Stage]] (V): <https://www.nacleanenergy.com/energy-storage/unlocking-fleet-versatility-while-simplifying-charging-infrastructure>
  - [[Modular Power Modules]] (V): <https://www.nacleanenergy.com/energy-storage/unlocking-fleet-versatility-while-simplifying-charging-infrastructure>
- **Related products and how they differ (offeredWith):**
  - [[Stryten M-Series Li600 Battery]]: no difference stated in the sources.
  - [[Stryten M-Series Li610 Battery]]: no difference stated in the sources.
- An earlier Stryten X-7 page says it comes in 2-bay (5-15 kW) and 4-bay (5-30 kW) cabinets, charges almost any motive battery including lithium-ion, supports user-programmable opportunity and fast charging with auto finish and equalization, and has an advanced 24/36/48 V multi-voltage modular design. Source: Stryten X-7 page (earlier version) (T1), retrieved 2026-10-02. <https://www.stryten.com/motive-power-solutions/m-series-x-7/>
- Stryten says M-Series chargers communicate with its inCOMMAND software, and if a battery's temperature rises the charger automatically adjusts the charge rate; X-7 is offered in 480 VAC and 208-240 VAC three-phase versions. Source: Stryten article on X-7 chargers (T1), retrieved 2026-10-02. <https://stryten.com/?p=173790>
- **Conflict-visible (C55):** the earlier page says 24/36/48 V; the 2026 article says the DC range was expanded to 72-96 V. Both are kept as the product's history, not as a disagreement of the same date. Sources: <https://www.stryten.com/motive-power-solutions/m-series-x-7/>; <https://www.nacleanenergy.com/energy-storage/unlocking-fleet-versatility-while-simplifying-charging-infrastructure>.
- **Functions performed, with citations (article):**
  - [[Compensate Charge for Battery Temperature]] (V): <https://stryten.com/?p=173790>

- **Architecture realization — temperature-compensated charging:** published behavior supports [[Temperature-Compensated Charge Control Design]]. [[Temperature Compensation Charge Control Firmware]] is allocated at **>=95% engineering confidence** because the charger must apply temperature-dependent control while its internal software partition is unpublished. Compensation slope, thresholds, filtering, and fault fallback remain product-specific.

## Aliases

- M-Series X-7
- X-7


## Former ids
