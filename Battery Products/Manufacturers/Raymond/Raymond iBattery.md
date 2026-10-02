---
type: Object
subtype: electrical
id: OBJ-00038
uid: 20261002164202406skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - forklift
  - lead-acid
  - fleet-management
subtypeOf:
  - "[[Battery Monitoring Device]]"
performs:
  - "[[Log Battery Events and Usage]]"
  - "[[Measure Battery Temperature]]"
  - "[[Sense Electrolyte Level]]"
  - "[[Estimate State of Charge]]"
  - "[[Measure Battery Voltage]]"
  - "[[Detect Battery Weight]]"
  - "[[Track Equalization]]"
  - "[[Alert on Abnormal Condition]]"
  - "[[Upload Battery Data to Cloud Portal]]"
hasDesign:
  - "[[Cloud Portal Integration]]"
---

# Raymond iBattery

## Definition

Raymond battery-resident module that reports battery statistics through the iWarehouse fleet system.

## Notes

- Raymond's 2010 launch release says the iBattery module reports charge and discharge cycles, high and low temperatures and low water levels, helps prevent over-discharge through voltage and state-of-charge detection, can detect battery weight against truck specifications, and gives reports on charging intervals, temperature, watering and equalization for warranty compliance; DC Velocity says the module rests on the battery itself. Source: Raymond press release (2010) and DC Velocity (T1/T2 (dated)), retrieved 2026-10-02. <https://raymondcorp.com/news/2010/ibattery-launch>
- A current product page describes the iBATTERY system as sending email or SMS alerts on temperature, water level, charge interval and state of charge, and forwarding data through iWAREHOUSE (note: page is on a 'develop-' subdomain, so treat as possibly non-production). Source: Raymond iBATTERY page (T1 (caution)), retrieved 2026-10-02. <https://develop-iwarehouseknows.raymondcorp.com/products/battery-monitoring>
- **Not stated in retrieved sources:** radio, voltage range, enclosure rating, whether it is still sold as a standalone device.
- **Functions performed (evidence):** [[Log Battery Events and Usage]] (V); [[Measure Battery Temperature]] (V); [[Sense Electrolyte Level]] (V); [[Estimate State of Charge]] (V); [[Measure Battery Voltage]] (V); [[Detect Battery Weight]] (V); [[Track Equalization]] (V); [[Alert on Abnormal Condition]] (V); [[Upload Battery Data to Cloud Portal]] (V). V = verified this pass, C = carried from seed text, U = user-stated.
- **Design characteristics (evidence):** [[Cloud Portal Integration]] (V).

## Aliases

- iBattery
- iBATTERY

## Former ids
