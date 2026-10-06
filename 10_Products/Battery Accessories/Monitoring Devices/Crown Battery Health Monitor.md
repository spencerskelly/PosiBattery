---
type: Object
subtype: electrical
id: OBJ-00037
uid: 20261002164202405skellyspencer
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
performs:
  - "[[Measure Battery Temperature]]"
  - "[[Sense Electrolyte Level]]"
  - "[[Accumulate Amp-Hours]]"
  - "[[Track Equalization]]"
  - "[[Alert on Abnormal Condition]]"
  - "[[Transmit Battery Data Wirelessly]]"
  - "[[Upload Battery Data to Cloud Portal]]"
hasDesign:
  - "[[Remote Exception Notification]]"
  - "[[Bluetooth Interface]]"
  - "[[Cloud Portal Integration]]"
  - "[[Equalization Event Tracking Design]]"
hasPart:
  - "[[Remote Alert Notification Service]]"
offeredBy:
  - "[[Crown Equipment]]"
offeredWith:
  - "[[Crown InfoLink]]"
---

# Crown Battery Health Monitor

## Definition

Crown battery-mounted monitor that pairs over Bluetooth with the truck's InfoLink module and reports battery data to the InfoLink portal.

## Notes

**Summary:**
Crown battery-mounted monitor that pairs over Bluetooth with the truck's InfoLink module and reports lead-acid battery data to the InfoLink portal.

**Marketed features:**
- Real-time battery activity and per-battery performance capture
- Automatic Bluetooth pairing with InfoLink (Advantage Plan)
- Temperature threshold alerts compared with water level and last equalization
- Per-battery performance profiles
- Cloud portal dashboards; email or text alerts

**Summary and features sources:**
Maker or publisher marketing claims as stated, not independently verified.
- MH&L (T2), retrieved 2026-10-04. <https://www.mhlnews.com/new-products/forklift-battery-performance-monitor-new-products>

- Crown says the Battery Health Monitor is installed on the battery and monitors real-time battery activity, alerts when temperature exceeds a threshold, and shows water levels, last equalization, Ah throughput and run time; it works with any forklift equipped with InfoLink Advantage Plan, pairing by Bluetooth with the InfoLink module, which sends data to a cloud portal. Source: Crown press coverage in M H&W and MH&L (undated) (T2), retrieved 2026-10-02. <https://www.mhlnews.com/new-products/forklift-battery-performance-monitor-new-products>
- **Not stated in retrieved sources:** Bluetooth variant, voltage range, price, whether it also talks to a charger. Relationship to [[Crown V-Force BMID]] is unknown.
- **Functions performed, with citations** (V = verified this pass, C = carried from seed text, U = user-stated):
  - [[Measure Battery Temperature]] (V): <https://www.mhlnews.com/new-products/forklift-battery-performance-monitor-new-products>
  - [[Sense Electrolyte Level]] (V): <https://www.mhlnews.com/new-products/forklift-battery-performance-monitor-new-products>
  - [[Accumulate Amp-Hours]] (V): <https://www.mhlnews.com/new-products/forklift-battery-performance-monitor-new-products>
  - [[Track Equalization]] (V): <https://www.mhlnews.com/new-products/forklift-battery-performance-monitor-new-products>
  - [[Alert on Abnormal Condition]] (V): <https://www.mhlnews.com/new-products/forklift-battery-performance-monitor-new-products>
  - [[Transmit Battery Data Wirelessly]] (V): <https://www.mhlnews.com/new-products/forklift-battery-performance-monitor-new-products>
  - [[Upload Battery Data to Cloud Portal]] (V): <https://www.mhlnews.com/new-products/forklift-battery-performance-monitor-new-products>
- **Design characteristics, with citations:**
  - [[Bluetooth Interface]] (V): <https://www.mhlnews.com/new-products/forklift-battery-performance-monitor-new-products>
  - [[Cloud Portal Integration]] (V): <https://www.mhlnews.com/new-products/forklift-battery-performance-monitor-new-products>
- **Sources used for the mapping above:** M H&L New Products (undated) <https://www.mhlnews.com/new-products/forklift-battery-performance-monitor-new-products>
- **Truck parts (round 31):** typical (inferred from the device type, not from a source): mounts on [[Truck Battery Compartment]]. See [[Truck Part Connection Register]].

- **Architecture realization — abnormal-condition alert:** Crown explicitly publishes cloud dashboards with email or text alerts. [[Remote Exception Notification]] and [[Remote Alert Notification Service]] capture the verified end-to-end notification role without asserting where the alert rule executes or which hosted software component sends the message.

- **Architecture realization — equalization tracking:** the product is allocated [[Equalization Event Tracking Design]] because published evidence establishes equalization status, history, or accumulated equalization information. The evidence does not establish whether the product locally classifies charge behavior or records an explicit status from another system, so neither concrete child Design is selected.

## Aliases

- Crown BHM
- Battery Health Monitor


## Former ids
