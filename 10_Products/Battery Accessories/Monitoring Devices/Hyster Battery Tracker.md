---
type: Object
subtype: electrical
id: OBJ-00039
uid: 20261002164202407skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - forklift
  - lead-acid
  - oem-branded
  - powered-by-posicharge
  - scope-aftermarket
subtypeOf:
  - "[[Battery Monitoring Device]]"
describedBy:
  - "[[Battery Product Landscape Conflicts and Open Questions]]"
performs:
  - "[[Measure Battery Voltage]]"
  - "[[Measure Battery Current]]"
  - "[[Measure Battery Temperature]]"
  - "[[Sense Electrolyte Level]]"
  - "[[Estimate State of Charge]]"
  - "[[Alert on Abnormal Condition]]"
  - "[[Transmit Battery Data Wirelessly]]"
  - "[[Upload Battery Data to Cloud Portal]]"
  - "[[Log Battery Events and Usage]]"
  - "[[Detect Voltage Imbalance]]"
  - "[[Track Equalization]]"
hasDesign:
  - "[[Remote Exception Notification]]"
  - "[[Cellular Communication Interface]]"
  - "[[Cloud Portal Integration]]"
hasPart:
  - "[[Remote Alert Notification Service]]"
offeredBy:
  - "[[Hyster-Yale]]"
poweredBy:
  - "[[PosiCharge]]"
---

# Hyster Battery Tracker

## Definition

Hyster-branded battery monitor, described as powered by PosiCharge technology, that stays with the battery and reports over cellular.

## Notes

**Summary:**
Hyster-branded battery monitoring solution, described as powered by PosiCharge technology, that reports battery data over existing wireless networks to Hyster Tracker.

**Marketed features:**
- 24/7 monitoring via existing wireless networks to cloud-based Hyster Tracker
- State of charge, voltage, current and temperature analytics
- Lifetime data storage for warranty compliance
- Electrolyte high/low reporting
- Email alerts: high temperature, equalization overdue, deep discharge, electrolyte high/low, imbalance
- Weekly exception and lifetime history reports; fleet data download

**Summary and features sources:**
Maker or publisher marketing claims as stated, not independently verified.
- Hyster (T1), retrieved 2026-10-04. <https://www.hyster.com/4a9a28/globalassets/coms/hyster/north-america/documents/telematics/0109het6fc001_e_en-us_battery-tracker-flyer.pdf>
- Hyster (T1), retrieved 2026-10-04. <https://www.hyster.com/en-us/north-america/technology/telematics/hyster-tracker/>
- Hyster (T1), retrieved 2026-10-04. <https://www.hyster.com/globalassets/coms/hyster/north-america/documents/telematics/0109het6fc001_e_en-us_battery-tracker-flyer.pdf>

- Hyster-Yale introduced Hyster Battery Tracker 'Powered by PosiCharge technology': a low-profile device that stays with the battery, installs in as little as 20 minutes, uses cellular communications to report state of charge, water levels, voltage, current and temperature, sends email notifications, and feeds a reporting suite with daily, weekly and lifetime reports. Source: Trade press listing (undated) (T2), retrieved 2026-10-02. <https://refrigeratedfrozenfood.com/articles/91289-forklift-battery-management-solution-monitors-health-usage>
- **Open (C18):** relationship to [[PosiCharge Battery Rx]] and PosiNET is not stated. Treat as an OEM-branded channel for PosiCharge technology, not an independent competitor, until a source says otherwise.
- **Functions performed, with citations** (V = verified this pass, C = carried from seed text, U = user-stated):
  - [[Measure Battery Voltage]] (V): <https://refrigeratedfrozenfood.com/articles/91289-forklift-battery-management-solution-monitors-health-usage>
  - [[Measure Battery Current]] (V): <https://refrigeratedfrozenfood.com/articles/91289-forklift-battery-management-solution-monitors-health-usage>
  - [[Measure Battery Temperature]] (V): <https://refrigeratedfrozenfood.com/articles/91289-forklift-battery-management-solution-monitors-health-usage>
  - [[Sense Electrolyte Level]] (V): <https://refrigeratedfrozenfood.com/articles/91289-forklift-battery-management-solution-monitors-health-usage>
  - [[Estimate State of Charge]] (V): <https://refrigeratedfrozenfood.com/articles/91289-forklift-battery-management-solution-monitors-health-usage>
  - [[Alert on Abnormal Condition]] (V): <https://refrigeratedfrozenfood.com/articles/91289-forklift-battery-management-solution-monitors-health-usage>
  - [[Transmit Battery Data Wirelessly]] (V): <https://refrigeratedfrozenfood.com/articles/91289-forklift-battery-management-solution-monitors-health-usage>
  - [[Upload Battery Data to Cloud Portal]] (V): <https://refrigeratedfrozenfood.com/articles/91289-forklift-battery-management-solution-monitors-health-usage>
  - [[Log Battery Events and Usage]] (V): <https://www.hyster.com/4a9a28/globalassets/coms/hyster/north-america/documents/telematics/0109het6fc001_e_en-us_battery-tracker-flyer.pdf>
  - [[Detect Voltage Imbalance]] (V): <https://www.hyster.com/4a9a28/globalassets/coms/hyster/north-america/documents/telematics/0109het6fc001_e_en-us_battery-tracker-flyer.pdf>
  - [[Track Equalization]] (V): <https://www.hyster.com/4a9a28/globalassets/coms/hyster/north-america/documents/telematics/0109het6fc001_e_en-us_battery-tracker-flyer.pdf>
- **Design characteristics, with citations:**
  - [[Cellular Communication Interface]] (V): <https://refrigeratedfrozenfood.com/articles/91289-forklift-battery-management-solution-monitors-health-usage>
  - [[Cloud Portal Integration]] (V): <https://refrigeratedfrozenfood.com/articles/91289-forklift-battery-management-solution-monitors-health-usage>
- **Sources used for the mapping above:** Trade press listing (undated) <https://refrigeratedfrozenfood.com/articles/91289-forklift-battery-management-solution-monitors-health-usage>
- **Truck parts (round 31):** typical (inferred from the device type, not from a source): mounts on [[Truck Battery Compartment]]. See [[Truck Part Connection Register]].

- **Architecture realization — abnormal-condition alert:** Hyster explicitly publishes email alerts for high temperature, overdue equalization, deep discharge, electrolyte high/low and imbalance. [[Remote Exception Notification]] and [[Remote Alert Notification Service]] capture the verified end-to-end notification role without asserting where the alert rule executes or which hosted software component sends the message.

## Aliases

- Battery Tracker


## Former ids
