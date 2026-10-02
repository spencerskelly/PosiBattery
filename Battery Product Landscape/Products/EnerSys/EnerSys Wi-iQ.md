---
type: Object
subtype: electrical
id: OBJ-00006
uid: 20261002150858942skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - forklift
  - gse
subtypeOf:
  - "[[Battery Monitoring Device]]"
describedBy:
  - "[[Battery Product Landscape Conflicts and Open Questions]]"
---

# EnerSys Wi-iQ

## Definition

EnerSys commercial battery monitoring device for motive-power batteries.

## Notes

- Manufacturer: EnerSys
- Market evidence checked: 2026-10-02
- Installation locus: battery-mounted; EnerSys literature describes the device as fitted to a main DC cable on the battery.
- Published applications include forklifts/pallet trucks, AGVs, floor-care equipment, and ground support equipment.
- Published measurements include amp-hours charged/discharged, temperature, voltage, and optional electrolyte level.
- Current product specifications list CAN bus communication; product literature also describes wireless data exchange with EnerSys management tools.
- Evidence:
  - https://www.enersys.com/en-gb/products/monitoring-and-fleet-management/data-logger/enersys/wi-iq/
  - https://www.enersys.com/49761b/globalassets/documents/product-documentation/_misc/wi-iq/apac/wiiq_gb.pdf
- **Verification 2026-10-02 (re-verified, with refinement):** Wi-iQ4 is the fourth generation device; it fits batteries from 24 V to 80 V; wireless interfaces are Zigbee (2.4 GHz) and Bluetooth BLE; CAN is an optional module with a choice of CANopen or J1939; the manual says it is designed to install only on a battery. Source: EnerSys Wi-iQ4 owner's manual (T1) <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>
- **Refinement vs text above:** the text above says specifications list CAN bus communication. The manual describes CAN as optional ("if equipped"). Both statements are kept; treat CAN as an option, not a base feature.
- **Verification 2026-10-02 (lineage):** an earlier generation, Wi-iQ3, is described as installed on the battery harness, using Bluetooth to remote sensors with an optional CAN module. Source: EnerSys Wi-iQ3 brochure (T1) <https://integration.enersys.com/493bb4/globalassets/documents/product-documentation/_misc/wi-iq/emea/wi-iq3-battery-monitoring-device-brochure.pdf>
- **Not re-verified:** published GSE application; optional electrolyte-level probe details. **Not stated in retrieved sources:** any direct charger interaction.

## Aliases

- Wi-iQ
- Wi-iQ 4

## Former ids
