---
type: Design
subtype:
id: DES-90955
uid: 20261006233500002skellyspencer
status: Draft
tags:
  - charger
  - bms
  - can
  - lithium
subtypeOf:
  - "[[BMS-Directed Charge Control Design]]"
dependsOn:
  - "[[CAN Interface]]"
designOf:
  - "[[PosiCharge ProCore Edge]]"
  - "[[Delta-Q IC650]]"
  - "[[Fronius SelectION]]"
  - "[[Lester Summit Series II]]"
---

# CAN BMS-Directed Charging

## Definition

BMS-directed charger control in which the battery management system communicates charge permission or voltage/current commands to the charger over CAN.

## Notes

- [[Delta-Q IC650]] is the clearest published example: Delta-Q states that the charger acts as a slave to the lithium BMS and can be commanded over CAN to deliver maximum voltage and current.
- [[Fronius SelectION]] publishes BatteryLink CAN with automatic baud-rate detection for lithium-ion batteries.
- [[PosiCharge ProCore Edge]] publishes a CAN/Lithium automatic operating mode.
- [[Lester Summit Series II]] publishes CANopen and SAE J1939 battery/vehicle communication for lithium/custom batteries.
- Exact application-layer protocol and BMS message set remain product-specific.

## Former ids
