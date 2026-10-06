---
type: Object
subtype: electrical
id: OBJ-00055
uid: 20261002165629065skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - floor-care
  - lead-acid
  - scope-aftermarket
subtypeOf:
  - "[[Battery Monitoring Device]]"
performs:
  - "[[Measure Battery Temperature]]"
  - "[[Sense Electrolyte Level]]"
  - "[[Log Battery Events and Usage]]"
  - "[[Transmit Battery Data Wirelessly]]"
  - "[[Upload Battery Data to Cloud Portal]]"
  - "[[Calculate Battery Abuse Cycles]]"
  - "[[Alert on Abnormal Condition]]"
  - "[[Indicate Battery Status Locally]]"
hasDesign:
  - "[[Remote Exception Notification]]"
  - "[[Internal Temperature Sensor]]"
  - "[[Mobile App Interface]]"
  - "[[Battery Abuse Cycle Analytics]]"
hasPart:
  - "[[Remote Alert Notification Service]]"
  - "[[Integrated Temperature Sensor Element]]"
madeBy:
  - "[[Philadelphia Scientific]]"
---

# Philadelphia Scientific eGO!core

## Definition

Philadelphia Scientific entry eGO! monitor for 12 V flooded and VRLA batteries that records cycles and temperatures.

## Notes

**Summary:**
Philadelphia Scientific entry-level eGO! battery performance monitor for smaller batteries that records key metrics for fleet decisions at lower cost of ownership.

**Marketed features:**
- Records work, rest, charge and cool-down hours, opportunity and abuse cycles
- Indications for connectivity, electrolyte level and high temperature
- eGO!alerts and Critical Alert Service via batterymanagement.net
- Light-triggered manual upload (phone torch)
- Data via eGO!cloudlink, eGO!receiver, eGO!gateway or eGO!tools app
- Listed for PPT and LLOP applications

**Summary and features sources:**
Maker or publisher marketing claims as stated, not independently verified.
- Philadelphia Scientific (T1), retrieved 2026-10-04. <https://phlsci.com/product-lines/ego-battery-performance-monitors/ego-core>

- The page lists 12 V nominal, flooded and VRLA versions, cycle data, internal temperature sensor, 100 x 30 x 18 mm, 100 g (flooded) and 80 g (VRLA), 2-year warranty, and data collection through eGO!cloudlink, eGO!receiver, eGO!gateway or the eGO!tools Android app. Source: PhilSci eGO!core page (T1), retrieved 2026-10-02. <https://phlsci.com/product-lines/ego-battery-performance-monitors/ego-core>
- The owner's manual says eGO!core is intended for 12 V flooded and VRLA batteries and monitors and records cycles and temperatures. Source: PhilSci eGO!core owner's manual (T1), retrieved 2026-10-02. <https://www.phlsci.com/media/ux3nu5uy/egocore-om-ps-en-us-doc0652.pdf>
- **Fit:** 12 V only, so it targets scrubbers and similar equipment, not 24 to 80 V forklift batteries. Not stated in retrieved sources: forklift or GSE use.
- **Functions performed, with citations** (V = verified this pass, C = carried from seed text, U = user-stated):
  - [[Measure Battery Temperature]] (V): <https://phlsci.com/product-lines/ego-battery-performance-monitors/ego-core> <https://www.phlsci.com/media/ux3nu5uy/egocore-om-ps-en-us-doc0652.pdf>
  - [[Sense Electrolyte Level]] (V): <https://phlsci.com/product-lines/ego-battery-performance-monitors/ego-core>
  - [[Log Battery Events and Usage]] (V): <https://phlsci.com/product-lines/ego-battery-performance-monitors/ego-core> <https://www.phlsci.com/media/ux3nu5uy/egocore-om-ps-en-us-doc0652.pdf>
  - [[Transmit Battery Data Wirelessly]] (V): <https://phlsci.com/product-lines/ego-battery-performance-monitors/ego-core>
  - [[Upload Battery Data to Cloud Portal]] (V): <https://phlsci.com/product-lines/ego-battery-performance-monitors/ego-core>
  - [[Calculate Battery Abuse Cycles]] (V): <https://phlsci.com/product-lines/ego-battery-performance-monitors/ego-core>
  - [[Alert on Abnormal Condition]] (V): <https://phlsci.com/product-lines/ego-battery-performance-monitors/ego-core>
  - [[Indicate Battery Status Locally]] (V): <https://phlsci.com/product-lines/ego-battery-performance-monitors/ego-core>
- **Design characteristics, with citations:**
  - [[Internal Temperature Sensor]] (V): <https://phlsci.com/product-lines/ego-battery-performance-monitors/ego-core>
  - [[Mobile App Interface]] (V): <https://phlsci.com/product-lines/ego-battery-performance-monitors/ego-core>
- **Sources used for the mapping above:** PhilSci eGO!core page <https://phlsci.com/product-lines/ego-battery-performance-monitors/ego-core>; PhilSci eGO!core owner's manual <https://www.phlsci.com/media/ux3nu5uy/egocore-om-ps-en-us-doc0652.pdf>
- **Truck parts (round 31):** typical (inferred from the device type, not from a source): mounts on [[Truck Battery Compartment]]. See [[Truck Part Connection Register]].

- **Architecture realization — abnormal-condition alert:** Philadelphia Scientific explicitly publishes eGO!alerts and Critical Alert Service through batterymanagement.net. [[Remote Exception Notification]] and [[Remote Alert Notification Service]] capture the verified end-to-end notification role without asserting where the alert rule executes or which hosted software component sends the message.

- **Architecture realization — battery abuse analytics:** the product is allocated [[Battery Abuse Cycle Analytics]] because its published feature set explicitly reports abuse cycles / abuse analytics. The calculation location and algorithm are not published, so neither [[Device-Resident Abuse Cycle Analytics]] nor [[Cloud-Based Abuse Cycle Analytics]] is selected.

## Aliases

- eGO!core


## Former ids
