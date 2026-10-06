---
type: Object
subtype: electrical
id: OBJ-00035
uid: 20261002164202403skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - diagnostic
  - forklift
  - scope-aftermarket
  - temporary-install
subtypeOf:
  - "[[Battery Monitoring Device]]"
performs:
  - "[[Measure Battery Voltage]]"
  - "[[Measure Battery Current]]"
  - "[[Measure Battery Temperature]]"
  - "[[Accumulate Amp-Hours]]"
  - "[[Estimate State of Charge]]"
  - "[[Log Battery Events and Usage]]"
  - "[[Alert on Abnormal Condition]]"
  - "[[Transmit Battery Data Wirelessly]]"
  - "[[Export Battery Data to PC]]"
hasDesign:
  - "[[Current Integration Amp-Hour Accumulation]]"
  - "[[Hall-Effect Current Sensing]]"
  - "[[900 MHz Industrial Wireless Interface]]"
  - "[[USB Data Download]]"
  - "[[Non-Volatile Event Memory]]"
  - "[[Acid-Resistant Sealed Housing]]"
  - "[[Reverse-Polarity Protection]]"
hasPart:
  - "[[Amp-Hour Counter State Memory]]"
  - "[[Battery Current Measurement Circuit]]"
  - "[[Battery Current Acquisition Firmware]]"
  - "[[Amp-Hour Accumulator Firmware]]"
  - "[[Control Circuit]]"
madeBy:
  - "[[Power Designers]]"
---

# Power Designers PowerTrac DT3

## Definition

Power Designers wireless diagnostic data logger that is plugged into a battery for a short power study and then removed.

## Notes

**Summary:**
Power Designers plug-in wireless diagnostic logger used for short power studies to size batteries and chargers.

**Marketed features:**
- Plug-and-play on existing battery systems; compact and non-invasive
- Logs voltage, current, temperature and Ah per event and since install
- Over/under voltage, over-current and over-temperature alarms
- Non-volatile memory; wireless download
- One-click reports: daily Ah used/replaced, cycle log, battery assessment, energy use
- Helps decide battery count and opportunity vs fast charging

**Summary and features sources:**
Maker or publisher marketing claims as stated, not independently verified.
- Power Designers (T1), retrieved 2026-10-04. <https://www.powerdesignerssibex.com/wp-content/uploads/2024/04/PDS-PT-DT3_PowerTracDT3.pdf>

- Manufacturer: Power Designers (Power Designers Sibex). **Locus:** temporary connection for a study; adjacent, not permanently installed, so filed under the category and not under the installed-device family.
- The data sheet (issued 03/2018, dated) lists nominal battery voltage 24 to 84 V, operating voltage 18 to 120 V, Hall-effect current sensing, bidirectional plus or minus 500 A typical at 1 A resolution, voltage accuracy 0.1 V, operating temperature -25 to 60 C, 4.25 x 1.5 x 0.6 in, 900 MHz industrial wireless up to 150 ft, storage of 10,000 events, upload to PC through a PowerTrac Link USB device sold separately, water and acid resistant packaging, 0.5 W nominal power, internal and external fuse and reverse-polarity protection. Source: PowerTrac DT3 data sheet (T1 (dated)), retrieved 2026-10-02. <https://www.powerdesignerssibex.com/wp-content/uploads/2024/04/PDS-PT-DT3_PowerTracDT3.pdf>
- **Functions performed, with citations** (V = verified this pass, C = carried from seed text, U = user-stated):
  - [[Measure Battery Voltage]] (V): <https://www.powerdesignerssibex.com/wp-content/uploads/2024/04/PDS-PT-DT3_PowerTracDT3.pdf>
  - [[Measure Battery Current]] (V): <https://www.powerdesignerssibex.com/wp-content/uploads/2024/04/PDS-PT-DT3_PowerTracDT3.pdf>
  - [[Measure Battery Temperature]] (V): <https://www.powerdesignerssibex.com/wp-content/uploads/2024/04/PDS-PT-DT3_PowerTracDT3.pdf>
  - [[Accumulate Amp-Hours]] (V): <https://www.powerdesignerssibex.com/wp-content/uploads/2024/04/PDS-PT-DT3_PowerTracDT3.pdf>
  - [[Estimate State of Charge]] (V): <https://www.materialhandling247.com/product/powertrac_dt_battery_diagnostics_tool>
  - [[Log Battery Events and Usage]] (V): <https://www.powerdesignerssibex.com/wp-content/uploads/2024/04/PDS-PT-DT3_PowerTracDT3.pdf>
  - [[Alert on Abnormal Condition]] (V): <https://www.powerdesignerssibex.com/wp-content/uploads/2024/04/PDS-PT-DT3_PowerTracDT3.pdf>
  - [[Transmit Battery Data Wirelessly]] (V): <https://www.powerdesignerssibex.com/wp-content/uploads/2024/04/PDS-PT-DT3_PowerTracDT3.pdf> <https://www.materialhandling247.com/product/powertrac_dt_battery_diagnostics_tool>
  - [[Export Battery Data to PC]] (V): <https://www.powerdesignerssibex.com/wp-content/uploads/2024/04/PDS-PT-DT3_PowerTracDT3.pdf>
- **Design characteristics, with citations:**
  - [[Hall-Effect Current Sensing]] (V): <https://www.powerdesignerssibex.com/wp-content/uploads/2024/04/PDS-PT-DT3_PowerTracDT3.pdf>
  - [[900 MHz Industrial Wireless Interface]] (V): <https://www.powerdesignerssibex.com/wp-content/uploads/2024/04/PDS-PT-DT3_PowerTracDT3.pdf>
  - [[USB Data Download]] (V): <https://www.powerdesignerssibex.com/wp-content/uploads/2024/04/PDS-PT-DT3_PowerTracDT3.pdf>
  - [[Non-Volatile Event Memory]] (V): <https://www.powerdesignerssibex.com/wp-content/uploads/2024/04/PDS-PT-DT3_PowerTracDT3.pdf> <https://www.materialhandling247.com/product/powertrac_dt_battery_diagnostics_tool>
  - [[Acid-Resistant Sealed Housing]] (V): <https://www.powerdesignerssibex.com/wp-content/uploads/2024/04/PDS-PT-DT3_PowerTracDT3.pdf>
  - [[Reverse-Polarity Protection]] (V): <https://www.powerdesignerssibex.com/wp-content/uploads/2024/04/PDS-PT-DT3_PowerTracDT3.pdf>
- **Sources used for the mapping above:** PowerTrac DT3 data sheet (03/2018, dated) <https://www.powerdesignerssibex.com/wp-content/uploads/2024/04/PDS-PT-DT3_PowerTracDT3.pdf>; Material Handling 24/7 listing for PowerTrac DT <https://www.materialhandling247.com/product/powertrac_dt_battery_diagnostics_tool>
- **Truck parts (round 31):** typical (inferred from the device type, not from a source): mounts on [[Truck Battery Compartment]]. See [[Truck Part Connection Register]].

- **Architecture realization — amp-hour accumulation:** this product combines battery-current sensing/monitoring with accumulated amp-hour information, supporting [[Current Integration Amp-Hour Accumulation]]. [[Amp-Hour Accumulator Firmware]] and the prerequisite current-acquisition/controller roles are allocated at **>=95% engineering confidence** because the internal firmware partition is not published.

## Aliases

- PowerTrac DT3
- PowerTrac DT


## Former ids
