---
type: Function
subtype:
id: FUNC-00034
uid: 20261002193402989skellyspencer
status: Draft
tags:
  - charger
  - extra
  - product-function
subtypeOf:
  - "[[Control Charge Profile]]"
dependsOn:
  - "[[Integrated Battery Management System]]"
  - "[[BMS-Directed Charge Control Design]]"
performedBy:
  - "[[Exide Motion+ Lithium Charger]]"
  - "[[Fronius SelectION]]"
  - "[[PosiCharge ProCore Edge]]"
  - "[[Delta-Q IC650]]"
  - "[[Lester Summit Series II]]"
  - "[[BMS-Directed Charge Control Firmware]]"
realizes:
  - "[[Charge Each Battery Correctly for Its Chemistry and Condition]]"
realizedBy:
  - "[[BMS-Directed Charge Control Design]]"
  - "[[Charge Each Battery Correctly for Its Chemistry and Condition]]"
---

# Charge Under BMS Control

## Definition

Take charge limits from the battery's BMS (often over CAN), with the charger acting as a slave to the BMS.

## Notes

- Charger-side or charger-and-battery behavior found in product descriptions. Links to products are made only where a source states the behavior; no link means unknown.
- No Requirement is linked (intentional gap).
- **Sources** (product, evidence level, web page):
  - [[Exide Motion+ Lithium Charger]] (V): <https://exidegroup.com/us/en/document/solition-light-traction-battery-leaflet>
  - [[PosiCharge ProCore Edge]] (V): <https://www.posicharge.com/procoreedge>
  - [[Fronius SelectION]] (V): <https://www.fronius.com/en/battery-charging-technology/info-centre/news/lead-acid-lithium-ion>
  - [[Lester Summit Series II]] (V): <https://www.rjbatt.com.au/media/nufe2twh/summit-series-ii_650w_data-sheet_060223.pdf>
  - [[Delta-Q IC650]] (V): <https://eepower.com/new-industry-products/delta-q-introduces-can-bus-functionality-to-the-ic650-charger/>
- **Extra (round 30):** documented for 5 of 18 charger maker groups (28 percent); the reusable charger-side realization is now [[BMS-Directed Charge Control Design]].

## Implementation Allocation

The reusable realization is [[BMS-Directed Charge Control Design]] -> [[BMS-Directed Charge Control Firmware]].

[[Integrated Battery Management System]] supplies battery-specific charge permission, voltage/current limits, targets, or stop conditions. The charger-side firmware validates those inputs and converts them into commands for the charger power stage while retaining local safety ownership.

[[CAN BMS-Directed Charging]] captures the common CAN implementation. It is allocated to [[PosiCharge ProCore Edge]], [[Delta-Q IC650]], [[Fronius SelectION]], and [[Lester Summit Series II]] because their published material explicitly identifies CAN-based lithium/BMS communication.

[[Exide Motion+ Lithium Charger]] receives the generic BMS-directed Design because Exide states that the Solition battery BMS controls the charger, but the retrieved source does not establish the transport.

## Aliases


## Former ids
