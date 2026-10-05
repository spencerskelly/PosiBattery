---
type: Object
subtype: electrical
id: OBJ-00038
uid: 20261002164202406skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - fleet-management
  - forklift
  - lead-acid
  - scope-oem-option
subtypeOf:
  - "[[Battery Monitoring Device]]"
describedBy:
  - "[[Battery Product Landscape Conflicts and Open Questions]]"
performs:
  - "[[Measure Battery Voltage]]"
  - "[[Measure Battery Temperature]]"
  - "[[Sense Electrolyte Level]]"
  - "[[Estimate State of Charge]]"
  - "[[Estimate State of Health]]"
  - "[[Log Battery Events and Usage]]"
  - "[[Track Equalization]]"
  - "[[Alert on Abnormal Condition]]"
  - "[[Upload Battery Data to Cloud Portal]]"
  - "[[Detect Battery Weight]]"
hasDesign:
  - "[[Cloud Portal Integration]]"
offeredBy:
  - "[[Raymond]]"
---

# Raymond iBattery

## Definition

Raymond battery-resident module that reports battery statistics through the iWarehouse fleet system.

## Notes

**Summary:**
Raymond iWAREHOUSE battery module that reports battery statistics and maintenance data to fleet managers.

**Marketed features:**
- Reports charge/discharge cycles, high and low temperatures and low water
- Detects battery weight to verify truck specification
- State of charge and voltage to prevent over-discharge
- Reports on charge intervals, temperature, watering and equalization for warranty compliance
- Web portal access via iWAREHOUSE Gateway

**Summary and features sources:**
Maker or publisher marketing claims as stated, not independently verified.
- Raymond (T1), retrieved 2026-10-04. <https://raymondcorp.com/news/2010/ibattery-launch>
- MH&L (T2), retrieved 2026-10-04. <https://mhlnews.com/archive/article/22045964/raymond-battery-module>

- Raymond's 2010 launch release says the iBattery module reports charge and discharge cycles, high and low temperatures and low water levels, helps prevent over-discharge through voltage and state-of-charge detection, can detect battery weight against truck specifications, and gives reports on charging intervals, temperature, watering and equalization for warranty compliance; DC Velocity says the module rests on the battery itself. Source: Raymond press release (2010) and DC Velocity (T1/T2 (dated)), retrieved 2026-10-02. <https://raymondcorp.com/news/2010/ibattery-launch>
- A current product page describes the iBATTERY system as sending email or SMS alerts on temperature, water level, charge interval and state of charge, and forwarding data through iWAREHOUSE (note: page is on a 'develop-' subdomain, so treat as possibly non-production). Source: Raymond iBATTERY page (T1 (caution)), retrieved 2026-10-02. <https://develop-iwarehouseknows.raymondcorp.com/products/battery-monitoring>
- **Not stated in retrieved sources:** radio, voltage range, enclosure rating, whether it is still sold as a standalone device.
- **Functions performed, with citations** (V = verified this pass, C = carried from seed text, U = user-stated):
  - [[Measure Battery Voltage]] (V): <https://mhlnews.com/archive/article/22045964/raymond-battery-module>
  - [[Measure Battery Temperature]] (V): <https://raymondcorp.com/news/2010/ibattery-launch>
  - [[Sense Electrolyte Level]] (V): <https://raymondcorp.com/news/2010/ibattery-launch>
  - [[Estimate State of Charge]] (V): <https://mhlnews.com/archive/article/22045964/raymond-battery-module>
  - [[Estimate State of Health]] (V): <https://test-iwarehouseknows.raymondcorp.com/products/battery-monitoring>
  - [[Log Battery Events and Usage]] (V): <https://raymondcorp.com/news/2010/ibattery-launch>
  - [[Track Equalization]] (V): <https://raymondcorp.com/news/2010/ibattery-launch>
  - [[Alert on Abnormal Condition]] (V): <https://test-iwarehouseknows.raymondcorp.com/products/battery-monitoring>
  - [[Upload Battery Data to Cloud Portal]] (V): <https://test-iwarehouseknows.raymondcorp.com/products/battery-monitoring>
  - [[Detect Battery Weight]] (V): <https://mhlnews.com/archive/article/22045964/raymond-battery-module>
- **Design characteristics, with citations:**
  - [[Cloud Portal Integration]] (V): <https://test-iwarehouseknows.raymondcorp.com/products/battery-monitoring>
- **Sources used for the mapping above:** Raymond iBATTERY launch release (2010, dated) <https://raymondcorp.com/news/2010/ibattery-launch>; M H&L Raymond Battery Module (2010, dated) <https://mhlnews.com/archive/article/22045964/raymond-battery-module>; Raymond iBATTERY page (on a test subdomain, caution) <https://test-iwarehouseknows.raymondcorp.com/products/battery-monitoring>
- The iBATTERY page says it gives timely data on temperature, water levels, charge intervals and state of charge, alerts on low water, temperature condition, weight and overcharges, shows a battery state-of-health chart that targets batteries needing replacement, and forwards data through the iWAREHOUSE system. Source: Raymond iBATTERY page (test subdomain) (T1 (caution)), retrieved 2026-10-02. <https://test-iwarehouseknows.raymondcorp.com/products/battery-monitoring>
- **Truck parts (round 31):** typical (inferred from the device type, not from a source): mounts on [[Truck Battery Compartment]]; connects to [[Truck Controller and CAN Bus]]. See [[Truck Part Connection Register]].

## Aliases

- iBattery

## Former ids
