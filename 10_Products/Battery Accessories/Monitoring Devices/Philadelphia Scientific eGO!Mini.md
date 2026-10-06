---
type: Object
subtype: electrical
id: OBJ-00047
uid: 20261002164202415skellyspencer
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
  - "[[Measure Battery Voltage]]"
  - "[[Measure Battery Temperature]]"
  - "[[Sense Electrolyte Level]]"
  - "[[Log Battery Events and Usage]]"
  - "[[Alert on Abnormal Condition]]"
  - "[[Indicate Battery Status Locally]]"
  - "[[Upload Battery Data to Cloud Portal]]"
  - "[[Export Battery Data to PC]]"
hasDesign:
  - "[[Local Abnormal Condition Alert]]"
  - "[[USB Data Download]]"
  - "[[Local LED Indicator]]"
  - "[[Audible Alarm]]"
  - "[[Battery-Top Mounting]]"
  - "[[Mobile App Interface]]"
hasPart:
  - "[[Abnormal Condition Evaluation Logic]]"
  - "[[Local Abnormal Alert Output Assembly]]"
  - "[[Status Indicator Driver Circuit]]"
  - "[[Audible Alarm Transducer]]"
  - "[[LED Status Indicator Element]]"
madeBy:
  - "[[Philadelphia Scientific]]"
---

# Philadelphia Scientific eGO!Mini

## Definition

Philadelphia Scientific low-profile battery data recorder that stores data on a removable USB drive.

## Notes

**Summary:**
Philadelphia Scientific slim battery-life monitor that records battery data to a removable USB drive for upload.

**Marketed features:**
- Monitors voltage, temperature and electrolyte level every 60 seconds
- Stores data on a USB flash drive for upload to BatteryManagement.net
- LED indicators and audible low-electrolyte alarm; over-temperature warning
- 24-hour Smart Delay to reduce incorrect topping
- Lead-acid and VRLA versions; 12-80 V; IP65
- 25 mm high, three-lead installation

**Summary and features sources:**
Maker or publisher marketing claims as stated, not independently verified.
- Warehouse News (T2), retrieved 2026-10-04. <https://warehousenews.co.uk/?p=68147>
- Philadelphia Scientific (T1), retrieved 2026-10-04. <https://www.phlsci.com/media/151762/ego-mini-egou-ps-ssh-doc0184-eng.pdf>

- The trade feature says eGO!Mini is slim, records data and stores it on a removable USB drive, with the eGO! range mounted on top of the battery and showing maintenance needs with LED indicators; the eGO!Tools Android app lets technicians upload data and program an eGO!. Source: Warehouse News feature (undated) (T4), retrieved 2026-10-02. <https://warehousenews.co.uk/?p=68147>
- **Functions performed, with citations** (V = verified this pass, C = carried from seed text, U = user-stated):
  - [[Measure Battery Voltage]] (V): <https://www.phlsci.com/media/151762/ego-mini-egou-ps-ssh-doc0184-eng.pdf>
  - [[Measure Battery Temperature]] (V): <https://www.phlsci.com/media/151762/ego-mini-egou-ps-ssh-doc0184-eng.pdf>
  - [[Sense Electrolyte Level]] (V): <https://www.phlsci.com/media/151762/ego-mini-egou-ps-ssh-doc0184-eng.pdf>
  - [[Log Battery Events and Usage]] (V): <https://www.phlsci.com/media/151762/ego-mini-egou-ps-ssh-doc0184-eng.pdf>
  - [[Alert on Abnormal Condition]] (V): <https://www.phlsci.com/media/151762/ego-mini-egou-ps-ssh-doc0184-eng.pdf>
  - [[Indicate Battery Status Locally]] (V): <https://www.phlsci.com/media/151762/ego-mini-egou-ps-ssh-doc0184-eng.pdf> <https://warehousenews.co.uk/?p=68147>
  - [[Upload Battery Data to Cloud Portal]] (V): <https://www.phlsci.com/media/151762/ego-mini-egou-ps-ssh-doc0184-eng.pdf>
  - [[Export Battery Data to PC]] (V): <https://www.phlsci.com/media/151762/ego-mini-egou-ps-ssh-doc0184-eng.pdf>
- **Design characteristics, with citations:**
  - [[USB Data Download]] (V): <https://www.phlsci.com/media/151762/ego-mini-egou-ps-ssh-doc0184-eng.pdf>
  - [[Local LED Indicator]] (V): <https://www.phlsci.com/media/151762/ego-mini-egou-ps-ssh-doc0184-eng.pdf> <https://warehousenews.co.uk/?p=68147>
  - [[Audible Alarm]] (V): <https://www.phlsci.com/media/151762/ego-mini-egou-ps-ssh-doc0184-eng.pdf>
  - [[Battery-Top Mounting]] (V): <https://warehousenews.co.uk/?p=68147>
  - [[Mobile App Interface]] (V): <https://warehousenews.co.uk/?p=68147>
- **Sources used for the mapping above:** PhilSci eGO!mini sheet <https://www.phlsci.com/media/151762/ego-mini-egou-ps-ssh-doc0184-eng.pdf>; Warehouse News eGO! feature (undated) <https://warehousenews.co.uk/?p=68147>
- **Truck parts (round 31):** typical (inferred from the device type, not from a source): mounts on [[Truck Battery Compartment]]. See [[Truck Part Connection Register]].

- **Architecture realization — abnormal-condition alert:** eGO!Mini explicitly provides LED indication, an audible low-electrolyte alarm and an over-temperature warning. The alert-evaluation logic is allocated at **>=95% engineering confidence** because the internal electronics/software partition is not published.

## Aliases

- eGO!Mini
- eGO Mini


## Former ids
