---
type: Info
subtype:
id: INFO-00171
uid: 20261002195812563skellyspencer
status: Draft
tags:
  - comparison
  - monitor
  - performance-metric
describes:
  - "[[Battery Monitoring and Identification Device]]"
---

# Monitor Comparison Matrix

## Definition

Side-by-side stated performance of battery monitors on seven metrics, with conflicts and gaps visible.

## Notes

- Values are copied from the metric notes; each metric's comparability rule applies. n/s = not stated in any retrieved source. Only products with at least one value in these columns are listed.
- Metric definitions: [[Metric - Nominal Voltage Range]], [[Metric - Operating Temperature Range]], [[Metric - Current Measurement]], [[Metric - Data Storage]], [[Metric - Wireless Interfaces and Range]], [[Metric - Charger Link]], [[Metric - Ingress and Enclosure Protection]].
- This matrix is a reading aid. Fix a product note first, then its metric value.

| Product | MM01 Nominal Battery Voltage Range | MM02 Operating Temperature Range | MM04 Current Measurement | MM07 Data Storage | MM08 Wireless Interfaces and Range | MM10 Charger Link | MM12 Ingress and Chemical Protection | Authority |
|---|---|---|---|---|---|---|---|---|
| [[AMETEK Prestolite Power BID]] | n/s | n/s | n/s | non-volatile memory; size n/s | n/s | ID numbers, voltages, Ah sizes, start rates, construction types; voltage, temperature and Ah usage on demand; earlier note: ID, type, Ah, cell count, start rate; temperature | n/s | [[AMETEK Prestolite Power BID]] |
| [[AMETEK Prestolite Power BID with Ah Accumulator]] | n/s | n/s | samples charge and discharge current over 100 times per second; stores every Ah incl. regeneration | n/s | n/s | n/s | n/s | [[AMETEK Prestolite Power BID with Ah Accumulator]] |
| [[AMETEK Prestolite Power TruBid]] | n/s | n/s | n/s | n/s | n/s | works with charger to end charge; wireless download | n/s | [[AMETEK Prestolite Power TruBid]] |
| [[AMETEK Prestolite Power WBID]] | n/s | n/s | n/s | n/s | ZigBee up to 500 ft (152 m) truck-mounted (obsolete) | n/s | n/s | [[AMETEK Prestolite Power WBID]] |
| [[Access Control Group CellTrac]] | n/s | n/s | no shunt; range n/s | n/s | n/s | n/s | n/s | [[Access Control Group CellTrac]] |
| [[Advanced Charging Technologies BATTview]] | 12-80 V nominal; operating 12-110 V | -25 to 60 C | resolution +/-1 A minimum | n/s | Wi-Fi (range n/s) | n/s | sealed, splash proof, UL 94V-5 | [[Advanced Charging Technologies BATTview]] |
| [[Crown V-Force BMID]] | n/s | n/s | n/s | n/s | Bluetooth Class 1 (range n/s) | voltage and temperature; adjusts charge rate; watering needs | n/s | [[Crown V-Force BMID]] |
| [[EnerSys Wi-iQ]] | 24-80 V and 96-120 V (nominal and operating) | -20 to 60 C | Hall; +/-1000 A; 1 A resolution; bidirectional | 8,000 events (C42) | Zigbee 2.4 GHz about 10 m; BLE about 5 m | battery type, voltage and capacity to NexSys+ (Express: voltage and capacity); temperature compensation (C50); earlier note: battery type and voltage to NexSys+; temperature compensation; Zigbee | IP65; UL 94V-0; acid resistant | [[EnerSys Wi-iQ]] |
| [[EnerSys iQ Mini]] | 12-80 V (carried from seed) | n/s | n/s | n/s | wireless to iQ Gateway (radio n/s in flyer) | n/s | n/s | [[EnerSys iQ Mini]] |
| [[Exide Motion+ EasyMonitor]] | 18-120 V | -10 to 60 C | n/s | n/s | n/s | n/s | n/s | [[Exide Motion+ EasyMonitor]] |
| [[Flow-Rite Eagle Eye Essential IV]] | 4-12 V DC supply | -40 to 185 F (-40 to 85 C) | n/s | n/s | n/s | n/s | n/s | [[Flow-Rite Eagle Eye Essential IV]] |
| [[Fronius TagID]] | n/s | n/s | n/s | n/s | n/s | temperature to Selectiva 4.0 | n/s | [[Fronius TagID]] |
| [[HOPPECKE trak collect]] | supply 17-150 VDC | use -30 to 80 C; storage -30 to 80 C | shunt; 500 A permanent; 0 to +/-2100 A; 1% (+/-10 to 2100 A) (C39) | 8 MB (4 MB ring buffer); 10 s interval; 30-day ring buffer | NFC 16 mm; Bluetooth 4.0 Low Energy / 2.0 | communicates with charger; temperature-controlled charging | IP 69K; sulfuric acid 60% at 50 C | [[HOPPECKE trak collect]] |
| [[Inventus Smart Battery Monitor SBM-01]] | 9-60 VDC supply | -30 to 70 C; storage -40 to 80 C | n/s | n/s | n/s | n/s | n/s | [[Inventus Smart Battery Monitor SBM-01]] |
| [[Philadelphia Scientific eGO!core]] | 12 V | n/s | n/s | n/s | n/s | n/s | n/s | [[Philadelphia Scientific eGO!core]] |
| [[Philadelphia Scientific eGO!gateway]] | n/s | n/s | n/s | n/s | Bluetooth about 70 m; 4G/3G/2G | n/s | n/s | [[Philadelphia Scientific eGO!gateway]] |
| [[Philadelphia Scientific eGO!plus]] | 24-80 V (12, 72, 120 V optional) | n/s | n/s | n/s | n/s | n/s | n/s | [[Philadelphia Scientific eGO!plus]] |
| [[Philadelphia Scientific eGO!pro]] | 24-80 V (12, 72, 120 V optional) | n/s | Hall split-core; bidirectional; range n/s | minute-by-minute logs and cycle data | n/s | n/s | IP65 | [[Philadelphia Scientific eGO!pro]] |
| [[PosiCharge BMID]] | n/s | n/s | n/s | n/s | n/s | identity, profile, temperature, charge-event history to PosiCharge chargers | n/s | [[PosiCharge BMID]] |
| [[PosiCharge Battery Rx]] | 24-96 V (vendor page) | electrolyte sensor -20 to 165 F (-29 to 74 C) | +/-1000 A range | n/s | n/s | n/s | acid immersion and pressure-wash tolerance | [[PosiCharge Battery Rx]] |
| [[PosiCharge PosiGuard]] | 24-96 V nominal; operating 18-120 V | -25 to 75 C | resolution 100 mA | 16 MB | Bluetooth; LoRa (range n/s) | n/s | IP65 sealed against water and acid | [[PosiCharge PosiGuard]] |
| [[Power Designers PowerTrac 3]] | 24-84 V nominal; operating 18-120 V (sheet) | -25 to 60 C (-13 to 140 F) (sheet) | sheet: shuntless intercell or Hall effect; +/-500 A typical, 1 A resolution (C47); earlier note: shuntless; range n/s | 10,000 events (sheet; equals DT3, C47); earlier note: 10,000 events | 900 MHz industrial wireless; up to 150 ft (sheet; equals DT3, C47) | voltage and Ah capacity to REVOLUTION | water and acid resistant (no IP code) | [[Power Designers PowerTrac 3]] |
| [[Power Designers PowerTrac DT3]] | 24-84 V nominal; operating 18-120 V | -25 to 60 C | Hall; +/-500 A typical; 1 A resolution; bidirectional | 10,000 events | 900 MHz; up to 150 ft (46 m) | n/s | water and acid resistant (no IP code) | [[Power Designers PowerTrac DT3]] |
| [[Power Designers PowerTrac SP+]] | 12-84 V nominal | -25 to 60 C | external 50 mV shunt; 500 A shunts offered | n/s | n/s | n/s | n/s | [[Power Designers PowerTrac SP+]] |
- **Round 11:** rebuilt from the metric notes after the eight datasheets were absorbed; values carry 'earlier note:' where a product already had a different value.
- **Round 12:** rebuilt after the Stryten, Delta-Q, Fronius and Exide addresses and findings; earlier values kept after 'earlier note:'.
- **Earlier comparison table (merged from INFO-00078 'Battery Monitoring Performance Comparison', kept as written):**
  - Values are copied as stated; they are not normalized or tested. Units are as the source gave them (F and C are not converted). n/s means no retrieved source states it. n/a means not applicable to the device type.
  - Every row has source links in the last column (full URL in the link target). Only rows with at least one stated value are listed. Products with function evidence but no specs are not shown; see their notes.
  - 'Data storage' is event count where stated; some products store by time rather than events.

  | Product | Nominal voltage | Operating temperature | Current measurement | Data storage | Wireless and interfaces | Other stated | Evidence | Source links |
  |---|---|---|---|---|---|---|---|---|
  | [[Power Designers PowerTrac SP+]] | 12-84 V | -25 to 60 C | ext. 50 mV shunt (500 A shunts offered) | non-volatile, size n/s | IR; RS-232/485 options | reverse polarity prot. | data sheet 10/2014 | [1](https://powerdesignerssibex.com/wp-content/uploads/2024/04/PD-TRA-SP_PowerTrac_SP_BatteryDataLogger.pdf) [2](https://www.powerdesignerssibex.com/powertrac-sp/) |
  | [[Power Designers PowerTrac DT3]] | 24-84 V (op. 18-120 V) | -25 to 60 C | Hall, +/-500 A typ., 1 A res. | 10,000 events | 900 MHz, up to 150 ft; USB via Link | accuracy 0.1 V; 0.5 W; acid-resistant | data sheet 03/2018 | [1](https://www.powerdesignerssibex.com/wp-content/uploads/2024/04/PDS-PT-DT3_PowerTracDT3.pdf) |
  | [[Power Designers PowerTrac 3]] | n/s | n/s | shuntless | 10,000 events | wireless, band n/s | up to 90% less energy vs prior | vendor page 2024 | [1](https://powerdesignerssibex.com/powertrac-3-wireless-battery-monitor/) |
  | [[EnerSys Wi-iQ]] | 24-80 V and 96-120 V | -20 to 60 C | Hall, +/-1000 A, 1 A res. | 8,000+ events | Zigbee ~10 m, BLE ~5 m; CAN opt. (CANopen, J1939) | accuracy 0.1 V; 1 W; IP65; 40.07x19.5x107.97 mm | manual 2025 | [1](https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf) |
  | [[EnerSys iQ Mini]] | 12-80 V (carried) | n/s | n/s | n/s | BLE | colour status indicators | launched 2024 | [1](https://www.enersys.com/en-gb/products/monitoring-and-fleet-management/data-logger/enersys/iq-mini/) |
  | [[PosiCharge PosiGuard]] | 24-96 V (op. 18-120 V) | -25 to 75 C | resolution 100 mA | 16 MB | Serial, CAN, Bluetooth, LoRa | 30 mV resolution; IP65; 4.05x1.80x1.00 in; UL 583, EN 1175 | vendor page, current | [1](https://posicharge.com/products/posiguard/) |
  | [[PosiCharge Battery Rx]] | 24-96 V (page) | sensor -20 to 165 F | +/-1000 A | life of battery | optional cellular | 7.63x2.25x1.25 in; acid, pressure wash | sheet (dated) and page | [1](https://www.posicharge.com/source/PDF/BatteryRx.pdf) [2](https://posicharge.com/products/battery-rx/) |
  | [[Advanced Charging Technologies BATTview]] | 12-80 V (op. 12-110 V) | -25 to 60 C | +/-1 A resolution | n/s | Wi-Fi | 30 mV and 1.0 F resolution | spec sheet | [1](https://og.mhi.org/media/members/41607/133717592244521430.pdf) |
  | [[Exide Motion+ EasyMonitor]] | 18-120 V | -10 to 60 C | n/s | n/s | n/s | LED traffic light + LCD; EU 2014/35/EU | leaflet | [1](https://www.exidegroup.com/en/document/easy-monitor-leaflet) |
  | [[Philadelphia Scientific eGO!pro]] | 24-80 V (12, 72, 120 optional) | n/s | Hall split-core, bidirectional | minute logs | Bluetooth to gateway; light-triggered upload | IP65; 235 g; 2 yr warranty; power figures conflict (C22) | vendor pages | [1](https://www.phlsci.com/products/ego-battery-performance-monitors/ego-pro/) [2](https://www.phlsci.co.uk/ego/ego-pro/) |
  | [[Philadelphia Scientific eGO!plus]] | 24-80 V (12, 72, 120 optional) | n/s | n/s | cycle data | radio | 20-24 mA transmitting; shelf life 3 yr | vendor page | [1](https://www.phlsci.com/product-lines/battery-performance-monitors/ego-plus/) |
  | [[Philadelphia Scientific eGO!core]] | 12 V | n/s | n/s | cycle data | eGO! gateway / receiver / Android app | 100x30x18 mm; 100 g | vendor page | [1](https://phlsci.com/product-lines/ego-battery-performance-monitors/ego-core) |
  | [[Philadelphia Scientific eGO!gateway]] | 90-264 V AC supply | 0 to 50 C | n/a | n/a | 4G/3G/2G; Bluetooth ~70 m | site gateway | vendor page | [1](https://www.phlsci.com/products/ego-battery-performance-monitors/ego-gateway/) |
  | [[Crown V-Force BMID]] | n/s | n/s | n/s | event record, size n/s | Bluetooth Class 1 | price 583.33 USD; warranty 365 days | shop listing | [1](https://shop.crown.com/crown/en/Batteries-and-Chargers/Battery-and-Charger-Parts-and-Accessories/Battery-and-Charger-Accessories//p/396525-BTM) |
  | [[Flow-Rite Eagle Eye Essential IV]] | 4-12 V DC supply | -40 to 185 F | n/a | n/a | n/a | 0.015 A; 24 in leads; ETL UL 61010-1; 2 yr | 2022 launch | [1](https://mhwmag.com/?p=86116) [2](https://www.bestmag.co.uk/flow-rite-receives-etl-standard-electrolyte-sensor-range/) |
  | [[Inventus Smart Battery Monitor SBM-01]] | 9-60 VDC supply | -30 to 70 C (storage -40 to 80 C) | n/s | n/s | CAN auto baud 125 kbps-1 Mbps | 1.4 W typ.; 5-85% RH; 52 mm panel | data sheet 08/2023 | [1](https://inventuspower.com/wp-content/uploads/TDS_Smart-Battery-Monitor_2023-Aug_V1.pdf) |
  | [[AMETEK Prestolite Power WBID]] | 12-40 cell sizes | n/s | n/s | life of battery | ZigBee up to 500 ft; DC-cable comms | obsolete | releases 2014, 2017 | [1](https://finance.yahoo.com/news/ametek-prestolite-power-launches-wireless-142836825.html) [2](https://mhlnews.com/new-products/article/22054269/wireless-forklift-battery-monitor-new-products) |
  | [[HOPPECKE trak collect]] | n/s | n/s | n/s | n/s | NFC, Bluetooth, CAN-LIN, battery bus; cloud collector | EN 12895, EN 1175-1, DIN EN IEC 62485-3 | vendor pages | [1](https://www.hoppecke.com/uk/product/trak-collect-premium/) [2](https://www.hoppecke.com/uk/news/hoppecke-trak-collect-taking-lead-acid-batteries-into-the-digital-age/) |
  - **Superseded in part (round 10):** the metric-based [[Monitor Comparison Matrix]] covers the same ground with defined metrics and comparability rules; this note is kept for its earlier source links.

## Aliases


## Former ids
- INFO-00078 (Battery Monitoring Performance Comparison)
