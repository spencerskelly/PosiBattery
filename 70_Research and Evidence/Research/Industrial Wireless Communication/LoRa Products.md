---
type: Info
subtype:
id: INFO-90006
uid: 20261012182106687skellyspencer
status: Draft
tags:
  - lora
  - lorawan
  - industrial-wireless
  - warehouse
  - production-plant
  - product-shortlist
  - market-research
describes: []
---

# LoRa Products

## Definition

Shortlist of ready-to-deploy LoRaWAN products relevant to warehouses and production plants, with selection by function, pilot candidates, integration cautions and a procurement approach.

## Notes

**Provenance:** moved into the model on 2026-10-12 from the `_Industrial Wireless Communication` folder; text preserved as received, with headings demoted one level. None of the cited claims has been independently verified in this vault yet. The 45 citations were converted from double-bracketed to ordinary single-bracketed Markdown links so they are not read as wikilinks; one URL containing escaped parentheses was rewritten with %28/%29.

Below is a market-facing shortlist of **ready-to-deploy LoRaWAN products** relevant to warehouses and production plants. I have prioritized commercial equipment from established industrial IoT vendors, including gateways, sensors, condition-monitoring devices, asset trackers, and safety/operational endpoints.

A practical deployment requires at least: **one or more LoRaWAN gateways**, a network/application platform, and field devices. The products below use standard LoRaWAN, so they can generally be combined across vendors, subject to regional frequency plan, certification, payload support, and platform/device-codec compatibility.[tektelic](https://tektelic.com/expertise/guide-to-lorawan-sensors/)[thethingsnetwork](https://www.thethingsnetwork.org/device-repository/)

### Recommended product shortlist

|Product / family|Vendor|Category|Warehouse / plant function|Readiness and key capability|
|---|---|---|---|---|
|WISE-2410|Advantech|Condition-monitoring sensor|Motors, pumps, fans, conveyors, gearboxes, compressors|Battery LoRaWAN vibration sensor with onboard 3-axis accelerometer, temperature sensing, eight calculated vibration indicators, IP66 enclosure, and no sensor wiring. Strong candidate for retrofit predictive maintenance. [advantech](https://www.advantech.com/en-us/products/b7e2306f-d561-4ca9-b0e3-33f7057e185f/wise-2410/mod_25018dc7-355c-40b4-bf9b-c93f6c73f1a0)|
|WISE-2410-NB|Advantech|Condition-monitoring sensor|Machinery health and vibration trending|Variant of the WISE-2410 supporting regional LoRaWAN bands. It transmits computed values such as VRMS, ARMS, peak, displacement, kurtosis, crest factor, skewness, and standard deviation rather than raw waveform streams. [iotmart](https://www.iotmart.com/en-us/s/product/detail/01t2y000000I5azAAC)|
|WISE-2410X|Advantech|Hazardous-area vibration sensor|Rotating equipment in hazardous or more demanding industrial areas|Explosion-proof version in Advantech’s industrial LoRaWAN portfolio, positioned alongside its vibration and current-meter solutions. Qualification must confirm the exact regional/explosion approvals required for a specific site. [advcloudfiles.advantech](https://advcloudfiles.advantech.com/ecatalog/2024/03221432.pdf)|
|Sense Asset+ Industrial|HID|Industrial asset tracker|Tools, carts, fixtures, cable reels, MHE attachments, mobile plant assets|Rugged battery-powered tag using LoRaWAN plus BLE and GNSS. BLE supports indoor locating; GNSS supports outdoor positioning; an LED and buzzer assist physical asset recovery. Particularly relevant for outdoor warehouses, laydown yards, and large industrial areas. [hidglobal](https://www.hidglobal.com/products/sense-asset-industrial)|
|AT101|Milesight|Asset tracker|Outdoor and mixed indoor/outdoor asset tracking|LoRaWAN tracker using GNSS and Wi‑Fi scanning for positioning. Suitable for containers, carts, vehicles, trailers, and assets that move between site, dock, and yard. [milesight](https://www.milesight.com/iot/product/lorawan-sensor/at101)|
|TS301 / TS302|Milesight|Temperature / humidity sensor|Cold rooms, warehouses, food/pharma storage, process areas|High-accuracy LoRaWAN temperature and humidity sensor with display and multiple probe options. Appropriate for environmental monitoring and cold-chain excursions. [milesight](https://www.milesight.com/iot/product/lorawan-sensor/ts30x)|
|EM500-PT100|Milesight|Industrial temperature sensor|Process equipment, refrigeration, high/low temperature process monitoring|Industrial LoRaWAN temperature device with PT100 probe options and an advertised measurement range of −200 °C to +800 °C. A useful option where standard ambient sensors are insufficient. [milesight](https://www.milesight.com/iot/product/lorawan-sensor/ts30x)|
|TUNDRA|TEKTELIC|Cold-chain temperature/humidity sensor|Freezers, walk-ins, cold rooms, refrigerated warehouse areas|IP67 LoRaWAN cold-chain sensor designed for −40 °C to +70 °C operation. Supports external temperature probe configurations and can operate as a utility-meter pulse counter. [tektelic](https://tektelic.com/products/sensors/tundra-iot-cold-chain-monitoring-sensor/)|
|KONA Micro Gateway|TEKTELIC|Indoor gateway|Warehouse and plant RF coverage|Compact indoor LoRaWAN gateway suitable for an initial pilot or localized coverage zone. TEKTELIC describes it as an indoor gateway option for low-cost private deployments. [tektelic](https://tektelic.com/expertise/lorawan-asset-tracking-the-lowest-cost-solution-without-citywide-coverage/)|
|KONA Enterprise Gateway|TEKTELIC|Outdoor / campus gateway|Plant campuses, yards, docks, remote structures|Industrial-grade gateway class for broad coverage and more demanding outdoor deployments. Appropriate for connecting warehouses, external staging areas, and site utilities. [tektelic](https://tektelic.com/expertise/lorawan-asset-tracking-the-lowest-cost-solution-without-citywide-coverage/)|
|LoRaWAN wireless vibration sensor|TE Connectivity|Condition-monitoring sensor|Pumps, fans, motors, bearings, rotating production equipment|Battery-operated uniaxial or triaxial vibration/temperature sensor. The product family is designed for harsh environments and includes ATEX-certified options. [te](https://www.te.com/en/product-CAT-WVS0001.html)|
|CT300|MultiTech|Current / energy sensor|Conveyor run-state, motor load, equipment utilization, energy monitoring|Compact current-transformer device for monitoring electrical current. Useful for identifying runtime, idle time, abnormal loading, and simple energy-management signals. [multitech](http://multitech.com/all-products/wireless-sensors/)|
|Door/Window Sensor with Temperature & Humidity|MultiTech|Door/contact environmental sensor|Cold rooms, freezer doors, access/security doors, storage rooms|Combines door state with temperature and humidity. A clear fit for refrigeration compliance, door-open alarms, energy-loss reduction, and access monitoring. [multitech](https://multitech.com/product/lorawan-door-window-sensor-with-air-temperature-humidityus-canada/)|
|LSV01 Industrial Vibration Sensor|Minew|Vibration/temperature sensor|Plant machinery and industrial asset monitoring|LoRaWAN sensor tag with temperature and three-axis vibration monitoring for industrial telemetry. [minew](https://www.minew.com/product-category/sensor-tag/)|
|LSD01 LoRaWAN Door Sensor|Minew|Door/contact sensor|Loading doors, cold rooms, cabinets, gates, restricted areas|Long-range door sensor with real-time event reporting and anti-tamper-oriented applications. [minew](https://www.minew.com/product-category/sensor-tag/)|
|LST01 Temperature & Humidity Sensor|Minew|Environmental sensor|Warehouse zones, storage areas, workspaces, environmental compliance|LoRaWAN temperature/humidity monitoring endpoint suitable for low-power ambient sensing. [minew](https://www.minew.com/lorawan-asset-tracking/)[minew](https://www.minew.com/product-category/sensor-tag/)|
|LBM01 Smart Button|Minew|Human-input endpoint|Operator call, maintenance request, material-replenishment request, exception reporting|Battery endpoint for human-initiated events. It can be used as a simple Andon-like signal where a low-cost wireless call point is more appropriate than a fixed HMI. [minew](https://www.minew.com/lorawan-asset-tracking/)|
|MG6 4G LoRaWAN Stellar Gateway|Minew|Gateway|Plants, warehouses, temporary or cellular-backhauled sites|Gateway option with 4G backhaul; useful where an Ethernet drop is unavailable at the desired RF gateway location. [minew](https://www.minew.com/lorawan-asset-tracking/)|
|SenseCAP LoRaWAN Gateway|Seeed Studio / SenseCAP|Industrial outdoor gateway|Pilot networks, remote warehouse zones, outdoor yards|Industrial IP66 gateway platform with Ethernet and 4G connectivity. SenseCAP documents support for LoRaWAN sensor nodes and industrial outdoor conditions. [wiki.seeedstudio](https://wiki.seeedstudio.com/Network/SenseCAP_Network/Sensecap-LoRaWAN-Gateway-and-Wireless-Sensor-User-Guide/)[sensecap-docs.seeed](https://sensecap-docs.seeed.cc/pdf/SenseCAP%20Product%20User%20Guide%28LoRaWAN%20Series%29-V1.3.pdf)|
|SenseCAP LoRaWAN sensor nodes|Seeed Studio / SenseCAP|Environmental sensor ecosystem|General environment, remote monitoring, rapid proof-of-concept|Sensor/gateway ecosystem with API and management platform. Better suited to environmental and facility monitoring than high-end predictive maintenance. [wiki.seeedstudio](https://wiki.seeedstudio.com/Network/SenseCAP_Network/Sensecap-LoRaWAN-Gateway-and-Wireless-Sensor-User-Guide/)[sensecapmx](https://www.sensecapmx.com/docs/sensecap-sensors/sensor-nodes/)|
|LS200-PT|PLANET|Product-temperature sensor|Cold storage, food, pharma, materials under controlled storage|IP65 LoRaWAN product-temperature device with PT1000 needle probe; specified for −70 °C to +200 °C monitoring. [planetechusa](https://planetechusa.com/product/ls200-pt-ip53-ip65-lorawan-product-temperature-sensor/)|
|LS200-TC|PLANET|Machine-temperature sensor|Machine surface/process temperature monitoring|Part of PLANET’s industrial LoRaWAN sensing range for machine temperature applications. [planetechusa](https://planetechusa.com/product/ls200-mf8-ip30-lorawan-multi-functional-sensor/)|
|LS200-CM3|PLANET|Three-phase current meter|Three-phase plant loads, motors, compressors, HVAC, chargers|LoRaWAN three-phase current-meter product for energy and utilization data from distributed loads. [planetechusa](https://planetechusa.com/product/ls200-mf8-ip30-lorawan-multi-functional-sensor/)|
|LS200-MF8|PLANET|Multifunction environmental sensor|Facility environment, storage zones, local equipment rooms|Multiparameter indoor device for variables including temperature, humidity, and tilt. Useful where a single point needs several condition signals. [planetechusa](https://planetechusa.com/product/ls200-mf8-ip30-lorawan-multi-functional-sensor/)|
|Industrial Temperature Sensor family|ioX-Connect|Industrial temperature products|Cold storage, HVAC, process equipment, electrical rooms|Multi-probe, high/low-temperature, and temperature/humidity variants, positioned for facilities and cold-chain applications with live alerts. [iox-connect](https://www.iox-connect.com/products/lorawan-devices/lorawan-temperature-sensors)|
|LoRaWAN current, pressure, flow, leak, distance, and air-quality devices|ioX-Connect|Industrial sensor catalog|Utilities, tanks, leaks, compressed air, facility condition monitoring|Broad catalog for temperature, humidity, water leak, distance/level, pressure, flow, current, and air-quality signals. Useful if vendor consolidation is more valuable than selecting best-in-class devices per function. [iox-connect](https://www.iox-connect.com/products/lorawan-devices-and-sensors)|

### Product selection by function

The following view may be more useful than a vendor catalog when building a pilot BOM or identifying product adjacency opportunities.

|Operational need|Ready products|What the device does|Likely receiving system|
|---|---|---|---|
|Cold-room compliance|Milesight TS301/TS302, TEKTELIC TUNDRA, PLANET LS200-PT, ioX temperature families|Logs air/product temperature, supports alerts for excursions, and may add humidity or door-state evidence|Quality system, BMS, facilities dashboard, ERP/WMS alert workflow|
|Refrigeration energy loss|MultiTech Door/Window + T/H Sensor, TUNDRA, CT300|Correlates door-open events, ambient temperature, and compressor or refrigeration electrical load|BMS/EMS, maintenance, facilities|
|Conveyor/motor health|Advantech WISE-2410/2410-NB, TE Connectivity vibration sensors, Minew LSV01|Measures vibration and temperature, then transmits condition indicators or alarms|CMMS/EAM, historian, predictive-maintenance platform|
|Machine run-time/utilization|MultiTech CT300, PLANET LS200-CM3, industrial I/O/current devices|Detects electrical current or power state to infer running, idle, off, overloaded, or abnormal conditions|MES, OEE analytics, CMMS, EMS|
|Distributed utility monitoring|PLANET LS200-CM3, ioX current/pressure/flow devices, TUNDRA pulse-input use case|Measures current, meter pulses, pressure, flow, or leakage conditions|EMS, BMS, sustainability reporting, maintenance|
|Door, dock, and security status|Minew LSD01, MultiTech door/window sensor|Reports door open/closed state and can pair it with temperature/humidity data|Security, BMS, WMS/dock operations|
|Asset visibility|HID Sense Asset+ Industrial, Milesight AT101|Reports movement, location, zone, outdoor GNSS position, and BLE/Wi‑Fi-assisted indoor positioning|WMS, EAM, yard management, asset-management platform|
|Asset recovery|HID Sense Asset+ Industrial|Activates a local LED/buzzer via BLE or LoRaWAN downlink to locate a particular tagged asset|EAM or asset-location application|
|Operator exception reporting|Minew LBM01 Smart Button|Sends manual service/material/maintenance/quality request events|Andon, MES, WMS, CMMS, workflow engine|
|General environmental sensing|Minew LST01, SenseCAP nodes, PLANET LS200-MF8, ioX devices|Captures temperature, humidity, air quality, tilt, leak, or occupancy-adjacent state|BMS, quality, facilities, EHS|

### Best candidates for a production-plant pilot

For an industrial site with charging systems, battery handling, MHE, production equipment, and warehouse operations, the most defensible initial product set would be:

1. **Advantech WISE-2410** on representative rotating assets—conveyors, fans, pumps, compressors, or ventilation motors—to demonstrate vibration-derived maintenance insight without wiring. Its onboard vibration-feature computation makes it appropriate for LoRaWAN bandwidth constraints.[advantech](https://www.advantech.com/en-us/products/b7e2306f-d561-4ca9-b0e3-33f7057e185f/wise-2410/mod_25018dc7-355c-40b4-bf9b-c93f6c73f1a0)[iotmart](https://www.iotmart.com/en-us/s/product/detail/01t2y000000I5azAAC)
2. **Milesight TS301/TS302 or TEKTELIC TUNDRA** in cold, temperature-sensitive, battery-storage, or controlled process areas. TUNDRA is especially relevant if freezer/cold-room operation, IP67 protection, or sub-zero performance is required.[milesight](https://www.milesight.com/iot/product/lorawan-sensor/ts30x)[tektelic](https://tektelic.com/products/sensors/tundra-iot-cold-chain-monitoring-sensor/)
3. **MultiTech CT300 or PLANET LS200-CM3** on compressors, chargers, conveyor feeders, HVAC, or other three-phase loads to establish run-time, idle-time, and electrical-load visibility.[multitech](http://multitech.com/all-products/wireless-sensors/)[planetechusa](https://planetechusa.com/product/ls200-mf8-ip30-lorawan-multi-functional-sensor/)
4. **HID Sense Asset+ Industrial** for a bounded high-value mobile asset group—maintenance carts, test fixtures, battery handling equipment, or MHE attachments—where both inside-the-building recovery and outdoor-yard location may matter.[hidglobal](https://www.hidglobal.com/products/sense-asset-industrial)
5. **Minew LSD01 or MultiTech door/temperature/humidity device** for dock, cold-room, battery-room, restricted-door, or equipment-enclosure monitoring.[multitech](https://multitech.com/product/lorawan-door-window-sensor-with-air-temperature-humidityus-canada/)[minew](https://www.minew.com/product-category/sensor-tag/)
6. **One indoor gateway plus a second gateway for RF diversity**—for example TEKTELIC KONA Micro indoors, with a SenseCAP or TEKTELIC outdoor/industrial gateway where yard or exterior coverage is needed. Gateway placement should be based on an RF survey inside representative rack, machinery, and metal-density zones rather than a theoretical range estimate.[tektelic](https://tektelic.com/expertise/lorawan-asset-tracking-the-lowest-cost-solution-without-citywide-coverage/)[wiki.seeedstudio](https://wiki.seeedstudio.com/Network/SenseCAP_Network/Sensecap-LoRaWAN-Gateway-and-Wireless-Sensor-User-Guide/)

### Integration cautions

### Location accuracy

Do not interpret “LoRaWAN asset tracker” as a stand-alone precision RTLS solution. Products such as HID Sense Asset+ combine **LoRaWAN backhaul** with BLE for indoor position and GNSS for outdoor position; that hybrid architecture is what makes it usable across warehouse, dock, and yard environments.[hidglobal](https://www.hidglobal.com/products/sense-asset-industrial)

For forklift-level collision avoidance, automated material-handling control, or precise aisle/bay location, evaluate UWB, BLE AoA, Wi‑Fi RTLS, or vision systems separately. LoRaWAN can carry the asset-status information but should not be the safety/location layer.

### Condition monitoring

For vibration monitoring, procure a device that calculates features locally—such as RMS, peak, crest factor, kurtosis, or band-energy metrics—and transmits these values periodically. The Advantech WISE-2410 family does this onboard. Sending continuous raw vibration waveforms would exceed the intended low-data-rate operating model.[advantech](https://www.advantech.com/en-us/products/b7e2306f-d561-4ca9-b0e3-33f7057e185f/wise-2410/mod_25018dc7-355c-40b4-bf9b-c93f6c73f1a0)[iotmart](https://www.iotmart.com/en-us/s/product/detail/01t2y000000I5azAAC)

### Product qualification

Before placing a purchase order, verify these items for each exact SKU, not merely the product family:

- US **915 MHz** or other site-appropriate LoRaWAN regional band plan.
- FCC, IC, CE/RED, and any customer-specific approvals.
- UL/ETL, hazardous-location, ATEX/IECEx, or IP/NEMA rating where needed.
- Operating temperature, condensation/icing performance, probe rating, and battery chemistry.
- Payload format, uplink interval, downlink behavior, firmware-update process, and device management.
- LoRaWAN version/class support, OTAA provisioning, security-key ownership, and private-network compatibility.
- Availability, MOQ, lifecycle statement, battery replaceability, calibration requirements, and warranty.
- Northbound integration with MQTT, REST API, OPC UA gateway, historian, CMMS, WMS, MES, or ERP.

### Practical procurement approach

Avoid committing to a single sensor vendor before site testing. Instead, define a **small interoperable pilot BOM** around three functional use cases:

|Pilot workstream|Suggested field devices|Decision to validate|
|---|---|---|
|Equipment health|4–8 Advantech WISE-2410 or TE vibration sensors|Signal quality, vibration threshold usefulness, battery behavior, CMMS workflow|
|Temperature and facility state|6–12 Milesight/TEKTELIC/PLANET temperature nodes plus door contacts|RF performance in racks/cold rooms, alert quality, audit/compliance workflow|
|Asset/material visibility|10–25 HID or Milesight asset tags|Zone/location accuracy, tag mounting survivability, event frequency, WMS/EAM data model|
|Network foundation|2 gateways with Ethernet/cellular backhaul|Coverage overlap, packet delivery, network-server integration, outage behavior|

This approach produces enough evidence to select product families based on installation effort, actual packet delivery, battery life, data quality, integration burden, and measurable operational value—not just vendor range claims.

## Former ids
