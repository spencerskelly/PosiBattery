---
type: Object
subtype: electrical
id: OBJ-00034
uid: 20261002164202402skellyspencer
status: Draft
tags:
  - battery-market-reference
  - charge-interface
  - commercial-product
  - forklift
  - lead-acid
  - scope-aftermarket
subtypeOf:
  - "[[Battery Monitoring Device]]"
  - "[[Battery Identification and Charge Interface Device]]"
describedBy:
  - "[[Document - Power Designers PowerTrac 3 Specification (PDS-PT3 11-2025)]]"
performs:
  - "[[Measure Battery Voltage]]"
  - "[[Measure Battery Current]]"
  - "[[Measure Battery Temperature]]"
  - "[[Sense Electrolyte Level]]"
  - "[[Log Battery Events and Usage]]"
  - "[[Track Equalization]]"
  - "[[Identify Battery to Charger]]"
  - "[[Communicate with Charger]]"
  - "[[Transmit Battery Data Wirelessly]]"
  - "[[Complete Missed Equalization Automatically]]"
  - "[[Predict Battery Replacement Timing]]"
  - "[[Upload Battery Data to Cloud Portal]]"
hasDesign:
  - "[[Variable-Length Electrolyte Level Probe]]"
  - "[[Shuntless Current Sensing]]"
  - "[[External Thermistor Temperature Sensor]]"
  - "[[Non-Volatile Event Memory]]"
  - "[[DC-Cable Power-Line Communication]]"
  - "[[Equalization Event Tracking Design]]"
  - "[[Battery Replacement Timing Prediction Design]]"
  - "[[Battery Event and Usage Logging Design]]"
hasPart:
  - "[[Variable-Length Electrolyte Probe Assembly]]"
  - "[[Battery Event Logger Firmware]]"
  - "[[Event Log Memory]]"
  - "[[Event Time Base]]"
madeBy:
  - "[[Power Designers]]"
offeredWith:
  - "[[Power Designers REVOLUTION X]]"
---

# Power Designers PowerTrac 3

## Definition

Power Designers wireless battery monitoring device with shuntless intercell sensing and an electrolyte sensor that also lets a Power Designers REVOLUTION charger recognize the battery.

## Notes

**Summary:**
Power Designers wireless battery monitor with shuntless sensing and an electrolyte sensor that also lets REVOLUTION chargers recognize the battery.

**Marketed features:**
- Logs voltage, temperature, current and electrolyte level during charge, discharge and idle
- Shuntless, compact, easier installation; up to 90 percent less energy than earlier models
- Stores up to 10,000 events; wireless transfer
- Smart Equalize and auto voltage/Ah recognition with REVOLUTION chargers via power-line communication
- Predicts battery replacement; PowerCharge.Net fleet monitoring option

**Summary and features sources:**
Maker or publisher marketing claims as stated, not independently verified.
- Power Designers (T1), retrieved 2026-10-04. <https://powerdesignerssibex.com/powertrac-3-wireless-battery-monitor/>
- Power Designers (T1), retrieved 2026-10-04. <https://powerdesignerssibex.com/wp-content/uploads/2024/04/PDS-PT-PT3_PowerTrac-3.pdf>

- Manufacturer: Power Designers (Power Designers Sibex).
- The vendor page says PowerTrac 3 tracks voltage, temperature, current and electrolyte level (variable-length probe), stores up to 10,000 events, transfers data wirelessly, uses a shuntless design, uses up to 90 percent less energy than previous models, and reports cycles, equalization status and kWh per event; it communicates with the REVOLUTION charger so the charger can automatically recognize battery voltage (24/36/48 V, footnoted by charger rating) and Ah capacity. Source: Power Designers PowerTrac 3 page (T1), retrieved 2026-10-02. <https://powerdesignerssibex.com/powertrac-3-wireless-battery-monitor/>
- **Not retrieved:** the specification sheet and installation guides linked from the page (radio band, nominal voltage range, operating temperature). **Competitive relevance:** closest match found to the BMID behavior of identifying a battery to a charger by a charger vendor's own monitor.
- **Functions performed, with citations** (V = verified this pass, C = carried from seed text, U = user-stated):
  - [[Measure Battery Voltage]] (V): <https://powerdesignerssibex.com/powertrac-3-wireless-battery-monitor/>
  - [[Measure Battery Current]] (V): <https://powerdesignerssibex.com/powertrac-3-wireless-battery-monitor/>
  - [[Measure Battery Temperature]] (V): <https://powerdesignerssibex.com/powertrac-3-wireless-battery-monitor/>
  - [[Sense Electrolyte Level]] (V): <https://powerdesignerssibex.com/powertrac-3-wireless-battery-monitor/>
  - [[Log Battery Events and Usage]] (V): <https://powerdesignerssibex.com/powertrac-3-wireless-battery-monitor/>
  - [[Track Equalization]] (V): <https://powerdesignerssibex.com/powertrac-3-wireless-battery-monitor/>
  - [[Identify Battery to Charger]] (V): <https://powerdesignerssibex.com/powertrac-3-wireless-battery-monitor/>
  - [[Communicate with Charger]] (V): <https://powerdesignerssibex.com/powertrac-3-wireless-battery-monitor/>
  - [[Transmit Battery Data Wirelessly]] (V): <https://powerdesignerssibex.com/powertrac-3-wireless-battery-monitor/>
  - [[Predict Battery Replacement Timing]] (V): <https://powerdesignerssibex.com/wp-content/uploads/2024/04/PDS-PT-PT3_PowerTrac-3.pdf>
  - [[Upload Battery Data to Cloud Portal]] (V): <https://powerdesignerssibex.com/wp-content/uploads/2024/04/PDS-PT-PT3_PowerTrac-3.pdf>
- **Design characteristics, with citations:**
  - [[Variable-Length Electrolyte Level Probe]] (V): <https://powerdesignerssibex.com/wp-content/uploads/2024/04/PDS-PT-PT3_PowerTrac-3.pdf>
  - [[Shuntless Current Sensing]] (V): <https://powerdesignerssibex.com/powertrac-3-wireless-battery-monitor/>
  - [[Non-Volatile Event Memory]] (V): <https://powerdesignerssibex.com/powertrac-3-wireless-battery-monitor/>
- **Sources used for the mapping above:** PowerTrac 3 product page <https://powerdesignerssibex.com/powertrac-3-wireless-battery-monitor/>
- **Functions performed, with citations (round 11 document):**
  - [[Complete Missed Equalization Automatically]] (V): <https://powerdesignerssibex.com/wp-content/uploads/2024/04/PDS-PT-PT3_PowerTrac-3.pdf> (also [[Document - Power Designers PowerTrac 3 Specification (PDS-PT3 11-2025)]])
- **Design characteristics, with citations (round 11 document):**
  - [[DC-Cable Power-Line Communication]] (V): <https://powerdesignerssibex.com/wp-content/uploads/2024/04/PDS-PT-PT3_PowerTrac-3.pdf> (also [[Document - Power Designers PowerTrac 3 Specification (PDS-PT3 11-2025)]])
- **Round 11 document:** Source: [[Document - Power Designers PowerTrac 3 Specification (PDS-PT3 11-2025)]] (T1, local copy; original <https://powerdesignerssibex.com/wp-content/uploads/2024/04/PDS-PT-PT3_PowerTrac-3.pdf>), absorbed 2026-10-02.
| Parameter | Value as stated |
|---|---|
| Models | PT3 |
| Current monitoring | shuntless intercell sensing or Hall effect sensing |
| Temperature | external thermistor |
| Electrolyte level | standard electrolyte sensor with variable-length probe |
| Nominal and operating voltage | 24 to 84 V nominal; 18 to 120 V operating |
| Bidirectional current | +/-500 A typical, 1 A resolution |
| Voltage accuracy | 0.1 V |
| Operating temperature | -25 to 60 C (-13 to 140 F) |
| Size | 4.25 x 1.5 x 0.6 in (108 x 38 x 15 mm) |
| Communication | 900 MHz industrial wireless; up to 150 ft; PLC with REVOLUTION chargers; USB via PowerTrac Link (sold separately) |
| Data storage | 10,000 events; real-time clock |
| Power | 1/2 W nominal |
| Protection | internal fuse and external in-line fuse; reverse polarity |
| Packaging | water and acid resistant |
| Multi-voltage with REVOLUTION | 24/36/48/72/80 V capability, footnoted by charger rating (48 V chargers charge 24/36/48 batteries; 36 V chargers 24/36; 80 V chargers 24 to 80 V) |
- **Smart Equalize with REVOLUTION:** completes any missed equalization during the next charge cycle and continues until finished.
- **Conflicts (C47):** the product page says shuntless and lists 24/36/48 V; the sheet says shuntless intercell sensing or Hall effect and lists 24/36/48/72/80 V by charger rating. Every number in this sheet's spec table (900 MHz, 150 ft, 10,000 events, 1/2 W, 4.25 x 1.5 x 0.6 in, +/-500 A) matches the 2018 PowerTrac DT3 data sheet, so the two may share a platform or the table may be reused.
- **Truck parts (round 31):** typical (inferred from the device type, not from a source): mounts on [[Truck Battery Compartment]]; connects to [[Truck Controller and CAN Bus]]. See [[Truck Part Connection Register]].

- **Architecture realization — equalization tracking:** the product is allocated [[Equalization Event Tracking Design]] because published evidence establishes equalization status, history, or accumulated equalization information. The evidence does not establish whether the product locally classifies charge behavior or records an explicit status from another system, so neither concrete child Design is selected.

- **Architecture realization — replacement timing:** the product is allocated [[Battery Replacement Timing Prediction Design]] because published material states battery life-expectancy or replacement prediction. The execution locus and forecast model are not disclosed, so neither [[Device-Resident Replacement Forecasting]] nor [[Fleet-Service Replacement Forecasting]] is selected.

- **Architecture realization — event and usage logging:** the product explicitly retains event/history data, supporting [[Battery Event and Usage Logging Design]], [[Battery Event Logger Firmware]], and [[Event Log Memory]]. Published clock/timekeeping capability also supports [[Event Time Base]]. The internal record schema, memory technology, and firmware partition remain unpublished.

## Aliases

- PowerTrac 3
- PT3


## Former ids
