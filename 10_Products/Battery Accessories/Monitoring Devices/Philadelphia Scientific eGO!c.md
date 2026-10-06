---
type: Object
subtype: electrical
id: OBJ-00048
uid: 20261002164202416skellyspencer
status: Draft
tags:
  - battery-market-reference
  - cloud
  - commercial-product
  - forklift
  - lead-acid
  - scope-aftermarket
subtypeOf:
  - "[[Battery Monitoring Device]]"
performs:
  - "[[Log Battery Events and Usage]]"
  - "[[Alert on Abnormal Condition]]"
  - "[[Indicate Battery Status Locally]]"
  - "[[Upload Battery Data to Cloud Portal]]"
  - "[[Calculate Battery Abuse Cycles]]"
  - "[[Transmit Battery Data Wirelessly]]"
  - "[[Predict Battery Replacement Timing]]"
hasDesign:
  - "[[Local LED Indicator]]"
  - "[[Battery-Top Mounting]]"
  - "[[Mobile App Interface]]"
  - "[[Cloud Portal Integration]]"
  - "[[Battery Abuse Cycle Analytics]]"
hasPart:
  - "[[LED Status Indicator Element]]"
madeBy:
  - "[[Philadelphia Scientific]]"
---

# Philadelphia Scientific eGO!c

## Definition

Philadelphia Scientific connected battery monitor that records every battery cycle and uploads to batterymanagement.net.

## Notes

**Summary:**
Philadelphia Scientific connected battery monitor that records every battery cycle and uploads wirelessly to batterymanagement.net.

**Marketed features:**
- Over 250,000 samples per day across 38 measurement fields
- Wireless upload via CloudLink gateway
- Red/amber/green indicators for water, temperature and OK
- 40 configurable alerts with email to up to three recipients
- Abuse analytics and predicted replacement date
- Marketed for larger fleets; claims payback with 30 days of extra battery life

**Summary and features sources:**
Maker or publisher marketing claims as stated, not independently verified.
- IPE Search (T2), retrieved 2026-10-04. <https://www.ipesearch.co.uk/iOT-technology-for-batteries>
- Warehouse News (T2), retrieved 2026-10-04. <https://warehousenews.co.uk/?p=68147>

- The trade feature says eGO!c records every battery cycle and uploads automatically to batterymanagement.net; a second trade source says it takes over 250,000 samples a day into 38 fields and gives 40 alerts, claims that are manufacturer figures. Source: Warehouse News and iPE feature (T4), retrieved 2026-10-02. <https://www.ipesearch.co.uk/iOT-technology-for-batteries>
- **Functions performed, with citations** (V = verified this pass, C = carried from seed text, U = user-stated):
  - [[Log Battery Events and Usage]] (V): <https://www.ipesearch.co.uk/iOT-technology-for-batteries>
  - [[Alert on Abnormal Condition]] (V): <https://www.ipesearch.co.uk/iOT-technology-for-batteries>
  - [[Indicate Battery Status Locally]] (V): <https://www.ipesearch.co.uk/iOT-technology-for-batteries>
  - [[Upload Battery Data to Cloud Portal]] (V): <https://warehousenews.co.uk/?p=68147>
  - [[Calculate Battery Abuse Cycles]] (V): <https://www.ipesearch.co.uk/iOT-technology-for-batteries>
  - [[Transmit Battery Data Wirelessly]] (V): <https://www.ipesearch.co.uk/iOT-technology-for-batteries>
  - [[Predict Battery Replacement Timing]] (V): <https://www.ipesearch.co.uk/iOT-technology-for-batteries>
- **Design characteristics, with citations:**
  - [[Local LED Indicator]] (V): <https://www.ipesearch.co.uk/iOT-technology-for-batteries>
  - [[Battery-Top Mounting]] (V): <https://warehousenews.co.uk/?p=68147>
  - [[Mobile App Interface]] (V): <https://warehousenews.co.uk/?p=68147>
  - [[Cloud Portal Integration]] (V): <https://warehousenews.co.uk/?p=68147>
- **Sources used for the mapping above:** iPE feature on eGO!c <https://www.ipesearch.co.uk/iOT-technology-for-batteries>; Warehouse News eGO! feature (undated) <https://warehousenews.co.uk/?p=68147>
- **Truck parts (round 31):** typical (inferred from the device type, not from a source): mounts on [[Truck Battery Compartment]]. See [[Truck Part Connection Register]].

- **Architecture realization — battery abuse analytics:** the product is allocated [[Battery Abuse Cycle Analytics]] because its published feature set explicitly reports abuse cycles / abuse analytics. The calculation location and algorithm are not published, so neither [[Device-Resident Abuse Cycle Analytics]] nor [[Cloud-Based Abuse Cycle Analytics]] is selected.

## Aliases

- eGO!c
- eGO C


## Former ids
