---
type: Object
subtype: electrical
id: OBJ-00083
uid: 20261002192008508skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - charger
  - light-duty
  - oem-supplier
  - lithium
subtypeOf:
  - "[[Industrial Battery Charger]]"
performs:
  - "[[Charge Lithium-Ion Battery]]"
  - "[[Charge Under BMS Control]]"
hasDesign:
  - "[[Onboard Charger Mounting]]"
madeBy:
  - "[[Delta-Q Technologies]]"
---

# Delta-Q IC650

## Definition

Delta-Q industrial charger with CAN bus (CANopen, CiA 419) for on-board or off-board integration with lead-acid and lithium packs.

## Notes

- Delta-Q says the IC650 Comm versions support CAN bus using an isolated physical layer and CANopen, with the CiA 419 charger device profile, for on-board or off-board use; with lithium, the charger acts as a slave to the BMS, which monitors cell voltages and temperatures and controls charging. Source: Delta-Q news release and EE Power report (T1), retrieved 2026-10-02. <https://eepower.com/new-industry-products/delta-q-introduces-can-bus-functionality-to-the-ic650-charger/>
- **Scope note (Q11):** light-duty OEM charger; included as the clearest example of the charger-as-slave-to-BMS pattern.
- **Functions performed, with citations** (V = verified this pass):
  - [[Charge Lithium-Ion Battery]] (V): <https://eepower.com/new-industry-products/delta-q-introduces-can-bus-functionality-to-the-ic650-charger/>
  - [[Charge Under BMS Control]] (V): <https://eepower.com/new-industry-products/delta-q-introduces-can-bus-functionality-to-the-ic650-charger/>
- **Design characteristics, with citations:**
  - [[Onboard Charger Mounting]] (V): <https://eepower.com/new-industry-products/delta-q-introduces-can-bus-functionality-to-the-ic650-charger/>

## Aliases

- IC650

## Former ids
