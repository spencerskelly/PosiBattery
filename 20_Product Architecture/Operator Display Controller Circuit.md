---
type: Object
subtype: circuit
id: OBJ-90068
uid: 20261006170500004skellyspencer
status: Draft
tags:
  - reusable-architecture
  - operator-interface
  - display
  - control
reuseScope: cross-product
subtypeOf:
  - "[[Control Circuit]]"
dependencyOf:
  - "[[Crown Gena Operating System]]"
  - "[[Operator Display HMI Firmware]]"
partOf:
  - "[[EnerSys Truck iQ]]"
  - "[[Linde MT18 Multifunction Display]]"
  - "[[Yale ERC050-060VGL]]"
  - "[[Vehicle Operator Display Assembly]]"
---

# Operator Display Controller Circuit

## Definition

Controller electronics that receive status data, execute display/HMI logic, and drive an operator-facing display.

## Notes

- A realization may use an MCU, application processor, integrated display controller, memory, power regulation, input circuitry, and display-interface peripherals.
- Exact processor, memory, power-supply topology, and display bus are product-specific.
- The circuit is a specific reuse of the general [[Control Circuit]] role rather than a second parallel controller concept.
- Product allocations to Truck iQ, Linde MT18 and Yale ERC050-060VGL are **>=95% engineering-confidence assumptions** because each presents dynamic vehicle/battery information electronically while the controller electronics are not published.

## Former ids
