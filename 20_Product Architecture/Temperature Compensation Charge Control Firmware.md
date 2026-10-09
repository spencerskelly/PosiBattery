---
type: Object
subtype: firmware
id: OBJ-90152
uid: 20261006234000004skellyspencer
status: Draft
tags:
  - reusable-architecture
  - firmware
  - charger
  - temperature
reuseScope: cross-product
hasDesign:
  - "[[Temperature-Compensated Charge Control Design]]"
dependsOn:
  - "[[Control Circuit]]"
performs:
  - "[[Compensate Charge for Battery Temperature]]"
partOf:
  - "[[AMETEK Prestolite Power Eclipse II]]"
  - "[[AMETEK Prestolite Power ULTRA]]"
  - "[[Crown V-HFM3 Charger]]"
  - "[[EnerSys Express Charger]]"
  - "[[EnerSys NexSys+ Charger]]"
  - "[[Fronius Selectiva 4.0]]"
  - "[[HOPPECKE trak charger HF premium]]"
  - "[[PosiCharge DVS100]]"
  - "[[PosiCharge DVS150]]"
  - "[[PosiCharge DVS300 Series]]"
  - "[[PosiCharge SVS100]]"
  - "[[Stryten EHI Charger]]"
  - "[[Stryten X-7 Charger]]"
  - "[[Lester Summit Series II]]"
  - "[[EnerSys NexSys AIR Wireless Charger]]"
  - "[[Compensate Charge for Battery Temperature]]"
---

# Temperature Compensation Charge Control Firmware

## Definition

Charger-control firmware that validates battery temperature and adjusts the active charge profile according to the product's temperature-compensation rules.

## Notes

- Candidate responsibilities include temperature validation, filtering, compensation-curve lookup, current/voltage/end-point adjustment, chemistry-specific limits, sensor-fault fallback, and charge inhibit at unsafe temperatures.
- The firmware does not measure battery temperature directly unless the charger architecture includes a dedicated temperature input.
- The charger power stage remains responsible for delivering the commanded electrical output.
- Internal firmware partitioning is generally unpublished and is modeled as an engineering abstraction unless directly identified.

## Former ids
