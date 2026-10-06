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
  - scope-oem-option
subtypeOf:
  - "[[Battery Monitoring Device]]"
describedBy:
  - "[[Battery Product Landscape Conflicts and Open Questions]]"
  - "[[Document - EnerSys IMPAQ and NexSys+ Charger Product Guide (AMER 0125)]]"
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
  - "[[Identify Battery to Charger]]"
  - "[[Report Battery Temperature to Charger]]"
hasDesign:
  - "[[Midpoint Voltage Symmetry Detection]]"
  - "[[Local Abnormal Condition Alert]]"
  - "[[Hall-Effect Current Sensing]]"
  - "[[External Thermistor Temperature Sensor]]"
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
hasPart:
  - "[[Mid-Battery Voltage Tap Harness]]"
  - "[[Mid-Battery Differential Voltage Measurement Circuit]]"
  - "[[Voltage Imbalance Evaluation Firmware]]"
  - "[[Abnormal Condition Evaluation Logic]]"
  - "[[Local Abnormal Alert Output Assembly]]"
  - "[[Audible Alarm Transducer]]"
  - "[[LED Status Indicator Element]]"
  - "[[Status Indicator Driver Circuit]]"
  - "[[LCD Status Display Module]]"
  - "[[LCD Display Interface Circuit]]"
  - "[[Local Status Presentation Firmware]]"
madeBy:
  - "[[EnerSys]]"
offeredWith:
  - "[[EnerSys NexSys+ Charger]]"
  - "[[EnerSys Express Charger]]"
  - "[[EnerSys NexSys COMpact Charger]]"
  - "[[EnerSys Truck iQ]]"
  - "[[EnerSys NexSys TPPL Battery]]"
  - "[[EnerSys NexSys AIR Wireless Charger]]"
  - "[[HAWKER Perfect Plus Battery]]"
---

# EnerSys Wi-iQ

## Definition

EnerSys commercial battery monitoring device for motive-power batteries.

## Notes

**Summary:**
EnerSys fourth-generation battery monitoring device (Wi-iQ4) that monitors motive-power batteries and shares data with chargers, apps, truck displays and, optionally, CAN networks.

**Marketed features:**
- 24-80 V and 96-120 V configurations; flooded lead-acid and NexSys TPPL
- Hall-effect current up to +/-1000 A at 1 A resolution; full and half-battery voltage; temperature and electrolyte probes
- LCD, three LEDs and low-voltage buzzer, replacing a separate LVA device
- Zigbee to Wi-iQ Report, chargers and Xinx; BLE to E Connect app and Truck iQ
- Optional CAN module (CANopen or J1939) for trucks and AGVs
- IP65; more than 8,000 events stored (spec table says up to 8,000 records)

**Summary and features sources:**
Maker or publisher marketing claims as stated, not independently verified.
- EnerSys (T1), retrieved 2026-10-04. <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>
- EnerSys (T1), retrieved 2026-10-04. <https://www.enersys.com/en-gb/products/monitoring-and-fleet-management/data-logger/enersys/wi-iq/>
- EnerSys (T1), retrieved 2026-10-04. <https://www.enersys.com/49761b/globalassets/documents/product-documentation/_misc/wi-iq/apac/wiiq_gb.pdf>

- **Identity:** battery-harness monitoring device made by [[EnerSys]]; installed family [[Battery Monitoring Device]]; also performs battery identification and temperature reporting to EnerSys chargers, so it behaves like a BMID-class device. Generation covered: Wi-iQ4 (2025 manual); the earlier Wi-iQ3 is described in a brochure.
- **Specifications (as stated in the Wi-iQ4 owner's manual):**
| Parameter | Value as stated |
|---|---|
| Nominal and operating voltage | 24 to 80 VDC and 96 to 120 VDC (two configurations) |
| Operating temperature | -20 to 60 C (4 to 140 F) |
| Current measurement | Hall effect, bidirectional up to +/-1000 A, 1 A resolution; solid-core sensor for cables up to 4/0 |
| Voltage measurement | overall and half-battery voltage; accuracy 0.1 V |
| Temperature sensing | external thermistor |
| Electrolyte level | with electrolyte sensor (flooded version) |
| Wireless | Zigbee 2.4 GHz (legacy protocol) and Bluetooth BLE; range up to 10 m (Zigbee), 5 m (BLE) |
| CAN (optional) | CANopen CiA 418 or J1939; to trucks (OEM protocols) and AGVs |
| Data | real-time clock; event log; memory 'more than 8,000 events' (features) or 'up to 8,000 records' (spec table) |
| Power | 1 W; over-voltage and reverse-polarity protection |
| Enclosure | IP65, UL 94V-0, pollution level 3, water and acid resistant |
| Size | 40.07 x 19.5 x 107.97 mm |
| Compliance | 2014/35/EU, BS EN 61010-1, BS EN 12895, 2014/30/EU, 2011/65/EU, 2014/53/EU, ETSI EN 300 328 |
| Chemistries | flooded lead-acid; NexSys TPPL; Gel and VRLA in Basic VRLA version |
| Part numbers | Wi-iQ4 120V SGL GL0017459-0002; 120V DBL GL0017459-0007; Basic flooded 6LA20743-E0E; Basic VRLA 6LA20743-E3E; Wi-iQ4F 6LA20743-E1E; Wi-iQ4DUALF 6LA20743-E2E; electrolyte sensor 6LA20761 |
- **Spec source:** [EnerSys Wi-iQ4 owner manual (EMEA, 2025 revision)](https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf). Conflict-visible (C42): memory is 'more than 8,000 events' in the features list and 'up to 8,000 event log records' in the specification table.
- **Features (functions and designs, each with its citation):** see the citation lines in the source history below; they link to [[Measure Battery Voltage]], [[Measure Battery Current]], [[Identify Battery to Charger]], [[Report Battery Temperature to Charger]], [[Communicate Battery State over CAN]], [[Command Vehicle Operating Limits over CAN]] and the interface designs.
- **Related products and how they differ:**
  - [[EnerSys NexSys+ Charger]]: the charger receives battery type and voltage through Wi-iQ and compensates for temperature when Wi-iQ is present; this is the full charger-identification use.
  - [[EnerSys Express Charger]]: the guide says units are equipped with a Wi-iQ to provide battery voltage and capacity data.
  - **Correction (C43):** an earlier version of this note also linked [[EnerSys IMPAQ Charger]] on the strength of an ambiguous excerpt. The guide puts the Wi-iQ statement in the Express section, and its chart shows no automatic temperature adjustment via Wi-iQ for IMPAQ. The IMPAQ link was withdrawn.
  - [[EnerSys NexSys AIR Wireless Charger]]: the guide's chart shows automatic temperature adjustment via Wi-iQ for AIR (added).
  - [[EnerSys NexSys COMpact Charger]]: the charger embeds the Wi-iQ functions, so no separate device is fitted.
  - [[EnerSys Truck iQ]]: truck-mounted display reading Wi-iQ data over BLE; not a charger link.
  - [[EnerSys NexSys TPPL Battery]]: chemistry the TPPL version is built for.
  - Wi-iQ3 versus Wi-iQ4: the Wi-iQ3 brochure describes wireless communication with the modular charger; the Wi-iQ4 manual adds BLE, CAN, an LCD and a buzzer and calls Zigbee the legacy protocol.
- **Gaps and to-do:** price; Xinx and Wi-iQ Report software details; charger-side data model (what exactly the NexSys+ reads); US-region manual if different from EMEA; relation to the iQ Mini beyond the shared family.
- **Source history (earlier bullets kept as written):**
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
  - [[Identify Battery to Charger]] (V): <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf>
  - [[Report Battery Temperature to Charger]] (V): <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf>
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
- The NexSys+ charger guide says all NexSys+ chargers are Wi-iQ enabled to receive battery information including battery type and voltage, and that the charger automatically compensates for temperature when the Wi-iQ device is present; IMPAQ and Express chargers are also described as using a Wi-iQ device. Source: EnerSys IMPAQ and NexSys+ modular charger product guide (T1), retrieved 2026-10-02. <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf>
- The NexSys COMpact onboard charger is described as embedding the functionalities of the Wi-iQ battery monitoring device. Source: EnerSys NexSys COMpact brochure (T1), retrieved 2026-10-02. <https://enersys.com/49e7e9/globalassets/documents/product-documentation/_enersys/emea/legacy/chargers/emea-en-imp-nxs-com-0323.pdf>
- **Upgrade (2026-10-02):** this makes Wi-iQ a BMID-class device in function: it identifies the battery to EnerSys chargers and enables temperature compensation. The earlier classification under Battery Monitoring Device only understates this; see conflicts C20 and the competitor table.
- The charger guide says all NexSys+ chargers are Wi-iQ enabled to provide battery type, voltage and capacity data to the charger, and Express chargers are equipped with a Wi-iQ for battery voltage and capacity data. Source: [[Document - EnerSys IMPAQ and NexSys+ Charger Product Guide (AMER 0125)]] (T1, local copy; original <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf>), absorbed 2026-10-02.
- Listed in the Logisnext Promatch parts program for Mitsubishi, Cat, Jungheinrich and UniCarriers trucks (2025). Source: Logisnext Americas release (T1), retrieved 2026-10-03. <https://www.logisnextamericas.com/en/logisnext/news/mla-enersys-expand-power-solutions-for-material-handling-operations>
- **Implementation assumption — local status presentation:** the LCD and three LEDs are verified. [[LCD Status Display Module]] and [[LED Status Indicator Element]] therefore represent verified physical output roles; [[LCD Display Interface Circuit]], [[Status Indicator Driver Circuit]], and [[Local Status Presentation Firmware]] are **>=95% engineering-confidence assumptions** because EnerSys does not publish the internal interface/driver/firmware partition.
- **GSE parts (round 32):** typical (inferred from the device type, not from a source): mounts on [[GSE Battery Compartment]]. The same device also fits trucks: typical mount [[Truck Battery Compartment]] (see [[Truck Part Connection Register]]). See [[GSE Part Connection Register]].

- **Architecture realization — abnormal-condition alert:** Wi-iQ explicitly provides battery warnings/alarms using its LCD, LEDs and low-voltage buzzer. [[Abnormal Condition Evaluation Logic]] is allocated at **>=95% engineering confidence** because EnerSys publishes the evaluated alert behavior but not the internal firmware partition.

- **Architecture realization — voltage imbalance:** the midpoint / half-battery voltage input is verified and supports [[Midpoint Voltage Symmetry Detection]]. [[Mid-Battery Voltage Tap Harness]] and [[Mid-Battery Differential Voltage Measurement Circuit]] capture the physical sensing path. [[Voltage Imbalance Evaluation Firmware]] is allocated at **>=95% engineering confidence** because the product electronically determines imbalance while its internal evaluation implementation is not published.

## Aliases

- Wi-iQ
- Wi-iQ 4


## Former ids
