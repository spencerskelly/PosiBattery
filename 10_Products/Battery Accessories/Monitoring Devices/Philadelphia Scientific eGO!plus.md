---
type: Object
subtype: electrical
id: OBJ-00054
uid: 20261002165629064skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - forklift
  - lead-acid
  - scope-aftermarket
subtypeOf:
  - "[[Battery Monitoring Device]]"
performs:
  - "[[Measure Battery Temperature]]"
  - "[[Sense Electrolyte Level]]"
  - "[[Log Battery Events and Usage]]"
  - "[[Indicate Battery Status Locally]]"
  - "[[Transmit Battery Data Wirelessly]]"
  - "[[Calculate Battery Abuse Cycles]]"
  - "[[Alert on Abnormal Condition]]"
  - "[[Upload Battery Data to Cloud Portal]]"
hasDesign:
  - "[[Remote Exception Notification]]"
  - "[[Local LED Indicator]]"
  - "[[Internal Temperature Sensor]]"
  - "[[Battery Abuse Cycle Analytics]]"
hasPart:
  - "[[Remote Alert Notification Service]]"
  - "[[LED Status Indicator Element]]"
  - "[[Integrated Temperature Sensor Element]]"
madeBy:
  - "[[Philadelphia Scientific]]"
---

# Philadelphia Scientific eGO!plus

## Definition

Philadelphia Scientific mid-tier eGO! battery performance monitor that records cycle data.

## Notes

**Summary:**
Philadelphia Scientific mid-tier eGO! battery performance monitor that logs minute-by-minute data across 25 indicators for heavy-duty fleets.

**Marketed features:**
- Minute-by-minute logs across 25 performance indicators incl. electrolyte and dual temperature
- Bidirectional energy monitoring; work/rest/charge/cool-down hours; opportunity and abuse cycles
- Configurable eGO!alerts and Critical Alert Service
- Light-triggered manual upload; reverse-polarity protected installation
- Data via eGO!cloudlink, receiver, gateway or Android app
- For LLOP, reach, counterbalance and VNA applications

**Summary and features sources:**
Maker or publisher marketing claims as stated, not independently verified.
- Philadelphia Scientific (T1), retrieved 2026-10-04. <https://www.phlsci.com/product-lines/battery-performance-monitors/ego-plus/>

- The page lists flooded and VRLA versions, 24 to 80 V nominal (12, 72 and 120 V optional), internal temperature sensor, LED indications for electrolyte, over-temperature and communications, cycle data storage, over-discharge threshold below 20 percent state of charge, flame retardant case, 20 to 24 mA while the radio transmits, 3-year unconnected shelf life and 2-year warranty. Source: PhilSci eGO!plus page (T1), retrieved 2026-10-02. <https://www.phlsci.com/product-lines/battery-performance-monitors/ego-plus/>
- **Open (C23):** the relationship of eGO!plus, eGO!core and eGO!pro to the older eGO!Mini and eGO!c names is not stated.
- **Functions performed, with citations** (V = verified this pass, C = carried from seed text, U = user-stated):
  - [[Measure Battery Temperature]] (V): <https://www.phlsci.com/product-lines/battery-performance-monitors/ego-plus/>
  - [[Sense Electrolyte Level]] (V): <https://www.phlsci.com/product-lines/battery-performance-monitors/ego-plus/>
  - [[Log Battery Events and Usage]] (V): <https://www.phlsci.com/product-lines/battery-performance-monitors/ego-plus/>
  - [[Indicate Battery Status Locally]] (V): <https://www.phlsci.com/product-lines/battery-performance-monitors/ego-plus/>
  - [[Transmit Battery Data Wirelessly]] (V): <https://www.phlsci.com/product-lines/battery-performance-monitors/ego-plus/>
  - [[Calculate Battery Abuse Cycles]] (V): <https://www.phlsci.com/product-lines/battery-performance-monitors/ego-plus/>
  - [[Alert on Abnormal Condition]] (V): <https://www.phlsci.com/product-lines/battery-performance-monitors/ego-plus/>
  - [[Upload Battery Data to Cloud Portal]] (V): <https://www.phlsci.com/product-lines/battery-performance-monitors/ego-plus/>
- **Design characteristics, with citations:**
  - [[Internal Temperature Sensor]] (V): <https://www.phlsci.com/product-lines/battery-performance-monitors/ego-plus/>
  - [[Local LED Indicator]] (V): <https://www.phlsci.com/product-lines/battery-performance-monitors/ego-plus/>
- **Sources used for the mapping above:** PhilSci eGO!plus page <https://www.phlsci.com/product-lines/battery-performance-monitors/ego-plus/>
- **Truck parts (round 31):** typical (inferred from the device type, not from a source): mounts on [[Truck Battery Compartment]]. See [[Truck Part Connection Register]].

- **Architecture realization — abnormal-condition alert:** Philadelphia Scientific explicitly publishes configurable eGO!alerts and Critical Alert Service. [[Remote Exception Notification]] and [[Remote Alert Notification Service]] capture the verified end-to-end notification role without asserting where the alert rule executes or which hosted software component sends the message.

- **Architecture realization — battery abuse analytics:** the product is allocated [[Battery Abuse Cycle Analytics]] because its published feature set explicitly reports abuse cycles / abuse analytics. The calculation location and algorithm are not published, so neither [[Device-Resident Abuse Cycle Analytics]] nor [[Cloud-Based Abuse Cycle Analytics]] is selected.

## Aliases

- eGO!plus


## Former ids
