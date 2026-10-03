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
  - "[[EnerSys]]"
performs:
  - "[[Measure Battery Voltage]]"
  - "[[Measure Battery Current]]"
  - "[[Measure Battery Temperature]]"
  - "[[Sense Electrolyte Level]]"
  - "[[Accumulate Amp-Hours]]"
  - "[[Estimate State of Charge]]"
  - "[[Log Battery Events and Usage]]"
  - "[[Track Equalization]]"
  - "[[Alert on Abnormal Condition]]"
  - "[[Indicate Battery Status Locally]]"
  - "[[Communicate with Charger]]"
  - "[[Transmit Battery Data Wirelessly]]"
  - "[[Communicate Battery State over CAN]]"
  - "[[Configure Device from Mobile App or PC]]"
  - "[[Detect Voltage Imbalance]]"
  - "[[Command Vehicle Operating Limits over CAN]]"
hasDesign:
  - "[[Hall-Effect Current Sensing]]"
  - "[[Bluetooth Low Energy Interface]]"
  - "[[ZigBee 2.4 GHz Interface]]"
  - "[[CAN Interface]]"
  - "[[Local LED Indicator]]"
  - "[[Audible Alarm]]"
  - "[[Harness Ring-Terminal Mounting]]"
  - "[[Acid-Resistant Sealed Housing]]"
  - "[[Mobile App Interface]]"
  - "[[Integrated LCD Display]]"
  - "[[Mid-Battery Voltage Tap]]"
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
- **Functions performed, with citations** (V = verified this pass, C = carried from seed text, U = user-stated):
  - [[Measure Battery Voltage]] (V): <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>
  - [[Measure Battery Current]] (V): <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>
  - [[Measure Battery Temperature]] (V): <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>
  - [[Sense Electrolyte Level]] (V): <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>
  - [[Accumulate Amp-Hours]] (C): <https://www.enersys.com/en-gb/products/monitoring-and-fleet-management/data-logger/enersys/wi-iq/>
  - [[Estimate State of Charge]] (V): <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>
  - [[Log Battery Events and Usage]] (V): <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>
  - [[Track Equalization]] (V): <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>
  - [[Alert on Abnormal Condition]] (V): <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf> <https://www.enersys.com/en-gb/about-us/news/enersys_suite_of_power_management_tools_elevate_fleet_performance/>
  - [[Indicate Battery Status Locally]] (V): <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf> <https://www.enersys.com/en-gb/about-us/news/enersys_suite_of_power_management_tools_elevate_fleet_performance/>
  - [[Communicate with Charger]] (V): <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf> <https://integration.enersys.com/493bb4/globalassets/documents/product-documentation/_misc/wi-iq/emea/wi-iq3-battery-monitoring-device-brochure.pdf>
  - [[Transmit Battery Data Wirelessly]] (V): <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf> <https://integration.enersys.com/493bb4/globalassets/documents/product-documentation/_misc/wi-iq/emea/wi-iq3-battery-monitoring-device-brochure.pdf>
  - [[Communicate Battery State over CAN]] (V): <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf> <https://integration.enersys.com/493bb4/globalassets/documents/product-documentation/_misc/wi-iq/emea/wi-iq3-battery-monitoring-device-brochure.pdf>
  - [[Configure Device from Mobile App or PC]] (V): <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>
  - [[Detect Voltage Imbalance]] (V): <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>
  - [[Command Vehicle Operating Limits over CAN]] (V): <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>
- **Design characteristics, with citations:**
  - [[Hall-Effect Current Sensing]] (V): <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>
  - [[Bluetooth Low Energy Interface]] (V): <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>
  - [[ZigBee 2.4 GHz Interface]] (V): <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>
  - [[CAN Interface]] (V): <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>
  - [[Local LED Indicator]] (V): <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf> <https://www.enersys.com/en-gb/about-us/news/enersys_suite_of_power_management_tools_elevate_fleet_performance/>
  - [[Audible Alarm]] (V): <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf> <https://www.enersys.com/en-gb/about-us/news/enersys_suite_of_power_management_tools_elevate_fleet_performance/>
  - [[Harness Ring-Terminal Mounting]] (V): <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>
  - [[Acid-Resistant Sealed Housing]] (V): <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>
  - [[Mobile App Interface]] (V): <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>
  - [[Integrated LCD Display]] (V): <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>
  - [[Mid-Battery Voltage Tap]] (V): <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>
- **Sources used for the mapping above:** EnerSys Wi-iQ4 owner's manual (EMEA, 2025 revision) <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>; EnerSys news release on the Wi-iQ suite <https://www.enersys.com/en-gb/about-us/news/enersys_suite_of_power_management_tools_elevate_fleet_performance/>; EnerSys Wi-iQ3 brochure (earlier generation) <https://integration.enersys.com/493bb4/globalassets/documents/product-documentation/_misc/wi-iq/emea/wi-iq3-battery-monitoring-device-brochure.pdf>; Seed note (cites the EnerSys Wi-iQ page for amp-hours) <https://www.enersys.com/en-gb/products/monitoring-and-fleet-management/data-logger/enersys/wi-iq/>
- The Wi-iQ4 manual (2025 revision) says the device has an LCD, three LEDs and an audible alarm; is IP65; fits flooded lead-acid and NexSys TPPL; comes in 24-80 V and 96-120 V configurations; operates -20 to 60 C; measures current by a Hall-effect sensor up to +/-1000 A at 1 A resolution; measures overall and half-battery voltage with 0.1 V accuracy; uses an external thermistor and an electrolyte sensor; stores more than 8,000 events; has Zigbee range about 10 m and BLE range about 5 m; draws 1 W; and measures 40.07 x 19.5 x 107.97 mm. Source: EnerSys Wi-iQ4 owner's manual (T1), retrieved 2026-10-02. <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>
- The manual says Zigbee connects to the Wi-iQ Report PC software, to chargers (NexSys+ battery charger) and to the Xinx system, BLE connects to the E Connect app and Truck iQ, and an optional CAN module offers CANopen CiA 418 or J1939 to trucks (under OEM protocols) and AGVs, sending usable state of charge, DC bus voltage and current, battery temperature, and lift lock-out and limited-operation triggers. Source: EnerSys Wi-iQ4 owner's manual (T1), retrieved 2026-10-02. <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>
- The manual says it supports equalization requests (an equal-period setting), an adjustable SoC warning with buzzer, six part numbers (Basic flooded, Basic VRLA, Premium CAN single and dual sensor, 120 V versions), and that it must be installed on the battery side and does not work on the truck side for a power study. Source: EnerSys Wi-iQ4 owner's manual (T1), retrieved 2026-10-02. <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>
- **Verification 2026-10-02:** the earlier refinement that CAN is an optional module stands, and the earlier competitor-table statement that no charger link was stated is corrected: the Wi-iQ4 manual lists wireless communication with the NexSys+ charger (conflicts C16).

## Aliases

- Wi-iQ
- Wi-iQ 4

## Former ids
