---
type: Info
subtype:
id: INFO-00073
uid: 20261002162520382skellyspencer
status: Draft
tags:
  - battery-landscape
  - competitors
  - bmid
describes:
  - "[[PosiCharge BMID]]"
  - "[[Battery Identification and Charge Interface Device]]"
  - "[[Battery Monitoring Device]]"
---

# BMID Competitor Landscape

## Definition

Working comparison of battery-installed identification and monitoring products against the PosiCharge BMID family, with only evidence-backed facts and explicit unknowns.

## Notes

- **Method:** web search on 2026-10-02; vendor pages where retrieved, otherwise trade press. Unknown means no retrieved source states it, not that the product lacks it. No datasheet was opened except Prestolite BID Ah Accumulator.
- **Reading guide:** closest functional matches to the PosiCharge BMID are the products that identify the battery to a charger and report temperature: [[Crown V-Force BMID]], [[AMETEK Prestolite Power BID]] and [[Fronius TagID]]. EnerSys, Philadelphia Scientific and WBID Pro are monitoring and data products with no retrieved evidence of charger interaction.

| Product | Maker | Mount / locus | Charger link (evidence) | Wireless | CAN | Sensors stated | Chemistry stated | Status evidence | Source links |
|---|---|---|---|---|---|---|---|---|---|
| PosiCharge BMID family (BMID 1, BMID 3, Battery Rx, PosiGuard) | PosiCharge | on battery | identity, profile and temperature to charger; GSE page: recognizes voltage, SOC, temperature | BLE option on BMID 3 (user); wireless BMID via Bluetooth | BMID 3 CAN option (user); PosiGuard CAN | immersed thermistor; level on Battery Rx and PosiGuard | lead-acid; PosiGuard lead-acid and lithium | current | [1](https://www.posicharge.com/faq/) [2](https://posicharge.com/products/posiguard/) [3](https://www.posicharge.com/procoreedge) |
| Crown V-Force BMID | Crown | battery top | adjusts charge rate for Crown chargers; method n/s | Bluetooth Class 1 (config) | n/s | voltage, temperature, low electrolyte | lead-acid | listed for sale | [1](https://shop.crown.com/crown/en/Batteries-and-Chargers/Battery-and-Charger-Parts-and-Accessories/Battery-and-Charger-Accessories//p/396525-BTM) [2](https://crown.com/en-vn/batteries-and-chargers/vhfm3-charger.html) |
| AMETEK Prestolite BID / BID with Ah Accumulator | AMETEK Prestolite | on battery | ID, type, Ah, cells, start rate, temperature to charger | none stated | none stated | temperature; Ah (Accumulator) | n/s | current page | [1](https://www.prestolitepower.com/products/datadevices/bid) [2](https://www.prestolitepower.com/products/datadevices) |
| AMETEK Prestolite WBID Pro | AMETEK Prestolite | battery-mounted | n/s for Pro (obsolete WBID: over DC cable, 2014) | ZigBee | n/s | level, electrolyte and ambient temperature | n/s | current page | [1](https://www.prestolitepower.com/products/datadevices/wbid-pro) [2](https://www.prestolitepower.com/products/obsolete-products/wbid) |
| AMETEK Prestolite TruBid | AMETEK Prestolite | battery top, probe in cell | works with charger to end charge; wireless to charger | wireless to charger | n/s | electrolyte temperature, specific gravity | lead-acid | status unclear | [1](https://dcvelocity.com/articles/31462-ametek-s-trubid-system-accurately-measures-battery-charge) |
| Power Designers PowerTrac 3 | Power Designers | on battery | REVOLUTION charger recognizes voltage and Ah | wireless, band n/s | n/s | voltage, temperature, current, level | n/s | vendor page | [1](https://powerdesignerssibex.com/powertrac-3-wireless-battery-monitor/) |
| Power Designers PowerTrac SP+ / Monitor / DT3 | Power Designers | on battery (DT3 temporary) | SP+: RS-485 PowerCharge interface option | SP+ wireless n/s; DT3 900 MHz; Monitor via PowerTrac Link | n/s | voltage, current, temperature; level option on SP+ | any, 12-84 V | SP+ 2014 sheet | [1](https://www.powerdesignerssibex.com/powertrac-sp/) [2](https://powerdesignerssibex.com/powertrac-monitor/) [3](https://www.powerdesignerssibex.com/wp-content/uploads/2024/04/PDS-PT-DT3_PowerTracDT3.pdf) |
| EnerSys Wi-iQ4 | EnerSys | on battery harness | battery type and voltage to NexSys+ chargers, charger temperature compensation, Zigbee ([guide](https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf)) | Zigbee, BLE | optional (CANopen, J1939); lift lock-out trigger | voltage incl. half-battery; current; temperature; level | flooded, TPPL (VRLA basic) | manual 2025 | [1](https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf) |
| EnerSys iQ Mini | EnerSys | on battery | none stated | BLE | none stated | not detailed | flooded, VRLA, TPPL | launched 2024 | [1](https://www.enersys.com/en-gb/products/monitoring-and-fleet-management/data-logger/enersys/iq-mini/) |
| HOPPECKE trak collect | HOPPECKE | permanently on battery | communicates with charger; temperature-controlled charging | NFC, Bluetooth | CAN-LIN, battery bus | voltage, medium voltage, current, temperature, level | lead-acid | vendor pages | [1](https://www.hoppecke.com/uk/news/hoppecke-trak-collect-taking-lead-acid-batteries-into-the-digital-age/) [2](https://hoppecke.com/en/stories/show/switch-from-gas-to-electrically-powered-forklift-trucks) |
| Advanced Charging Technologies BATTview | ACT (Deka dealers) | n/s | real-time communication with Quantum chargers (equalization, termination) | Wi-Fi | n/s | voltage, current, temperature, level alert | n/s | spec sheet | [1](https://og.mhi.org/media/members/41607/133717592244521430.pdf) [2](https://dcvelocity.com/articles/31570-advanced-charging-technologies-improves-battview-battery-monitors) |
| Exide Motion+ EasyMonitor | Exide | cell connector probe | none stated | n/s | n/s | level, temperature, voltage symmetry, Ah | lead-acid | leaflet | [1](https://www.exidegroup.com/en/product/easymonitor) [2](https://www.exidegroup.com/en/document/easy-monitor-leaflet) |
| Fronius TagID / TagID+ | Fronius | on battery | charger adjusts to battery temperature (Selectiva 4.0) | n/s | n/s | temperature; level on TagID+ | wet and gel lead-acid | 2022 launch | [1](https://www.fronius.com/en/battery-charging-technology/our-solutions/individual-battery-charging-solutions/battery-sensor-tagid) |
| Philadelphia Scientific eGO! range (pro, plus, core, Mini, c) | Philadelphia Scientific | battery top | none stated | Bluetooth to gateway; USB; cloud | n/s | voltage, temperature, level, current (pro) | flooded, VRLA | vendor pages | [1](https://www.phlsci.com/products/ego-battery-performance-monitors/ego-pro/) [2](https://www.phlsci.com/products/ego-battery-performance-monitors/) |
| Crown Battery Health Monitor | Crown | on battery | none stated | Bluetooth to InfoLink | n/s | temperature, water level, Ah | lead-acid | trade press | [1](https://www.mhlnews.com/new-products/forklift-battery-performance-monitor-new-products) |
| Raymond iBattery | Raymond | on battery | none stated | via iWarehouse | n/s | temperature, level, voltage, SOC, weight | lead-acid | 2010 launch; page on test host | [1](https://raymondcorp.com/news/2010/ibattery-launch) [2](https://test-iwarehouseknows.raymondcorp.com/products/battery-monitoring) |
| Hyster Battery Tracker / Yale Battery Vision | Hyster-Yale | stays with battery | none stated | cellular | n/s | SOC, water, voltage, current, temperature | n/s | trade press; powered by PosiCharge | [1](https://refrigeratedfrozenfood.com/articles/91289-forklift-battery-management-solution-monitors-health-usage) [2](https://www.mhlnews.com/new-products/forklift-battery-monitor-new-products) |
| Access Control Group CellTrac | Access Control Group | n/s | none stated | n/s | n/s | voltage, Ah, temperature, water level | n/s | undated; status unclear | [1](https://www.mhlnews.com/archive/celltrac) |

- **Previously listed as candidates, now modeled:** [[HOPPECKE trak collect]] and [[Hyster Battery Tracker]] (an OEM channel for PosiCharge technology, conflicts C18). Wider function and design comparison: [[Function Map]], [[Design Map]], [[Monitor Comparison Matrix]].
- **Lithium side not covered:** products that identify or interface lithium batteries (BMS-to-charger CAN) are in [[Battery Management System]]. Whether a BMID-class device competes with a BMS for lithium customers is open.
- **Not covered (superseded by the refresh line below):** Zivan, Delta-Q, Lester, Jungheinrich, Linde, Toyota device-level products, Asian vendors, and general-purpose battery monitors (marine, RV, solar). Japanese BTRC-R100 and BTRC-Z100 lead-acid monitors appear in a catalog with no maker identified <https://www.ipros.com/en/cg3/Battery%20performance%20monitoring%20system/>.
- **Refresh 2026-10-02:** table rebuilt with 17 rows. Wi-iQ charger link corrected (C16); PowerTrac, TruBid, HOPPECKE and others added. The earlier version said no charger interaction was stated for Wi-iQ.
- **Refresh round 2 (2026-10-02):** table rebuilt with 18 rows and a source-link column. Added Exide EasyMonitor, ACT BATTview, PowerTrac Monitor and DT3, eGO! range detail; Wi-iQ4 charger link corrected from the manual. Not covered: Zivan, Delta-Q, Lester, Toyota, Linde and Jungheinrich device-level products (searches found only a Jungheinrich electrolyte-sensor accessory <https://www.jungheinrich-shop.si/en/spare-parts-and-accessories/battery-accessories/electrolyte-level-sensor--51233095>); Midtronics BMS-100 targets heavy-duty fleet starting batteries <https://www.midtronics.com/?p=15573>; stationary-battery monitors (for example <https://www.franklingrid.com/en/products/battery-monitoring/>) are a different market.
- **Wi-iQ upgrade (2026-10-02):** EnerSys's NexSys+ guide states the charger identifies battery type and voltage through Wi-iQ and compensates for temperature <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf>. Wi-iQ is the closest functional match to the PosiCharge BMID found among battery makers.

## Aliases

- BMID competitors


## Former ids
