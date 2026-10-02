---
type: Info
subtype:
id: INFO-00078
uid: 20261002164202422skellyspencer
status: Draft
tags:
  - battery-landscape
  - comparison
  - performance
describes:
  - "[[Battery Monitoring Device]]"
  - "[[Battery Identification and Charge Interface Device]]"
---

# Battery Monitoring Performance Comparison

## Definition

Stated performance and specification values for products where a source gives them, with unknowns left blank as n/s (not stated).

## Notes

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

## Aliases

- Performance matrix

## Former ids
