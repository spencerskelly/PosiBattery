---
type: Object
subtype: electrical
id: OBJ-00033
uid: 20261002164202401skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - forklift
  - gse
  - lead-acid
subtypeOf:
  - "[[Battery Monitoring Device]]"
performs:
  - "[[Measure Battery Voltage]]"
  - "[[Measure Battery Current]]"
  - "[[Measure Battery Temperature]]"
  - "[[Accumulate Amp-Hours]]"
  - "[[Log Battery Events and Usage]]"
  - "[[Alert on Abnormal Condition]]"
  - "[[Communicate with Charger]]"
  - "[[Sense Electrolyte Level]]"
  - "[[Export Battery Data to PC]]"
  - "[[Transmit Battery Data Wirelessly]]"
hasDesign:
  - "[[External Shunt Current Sensing]]"
  - "[[Infrared Data Port]]"
  - "[[RS-232 and RS-485 Serial Interface]]"
  - "[[Non-Volatile Event Memory]]"
  - "[[Reverse-Polarity Protection]]"
---

# Power Designers PowerTrac SP+

## Definition

Power Designers battery data logger for industrial and motive batteries that attaches to the battery, logs voltage, current and temperature, and uses an external shunt.

## Notes

- Manufacturer: Power Designers (site and sheets also use the name Power Designers Sibex). POWER TRAC is a registered trademark of Power Designers, LLC for a 'vehicle battery charge monitor' (registry record) <https://trademarks.justia.com/owners/power-designers-llc-1054278>.
- The vendor page says PowerTrac SP+ attaches to the battery, logs instantaneous voltage, current and temperature, charge and discharge Ah since installation and per event, event start time and duration, min and max voltages, and over and under voltage, over current and over temperature alarms; applications listed are forklift trucks, GSE and neighborhood electric vehicles; a 50 mV shunt of any size is used, with 500 A bolt-on (PTBS-500) and clamp-on (PTCS-500) shunts offered; nominal battery voltage 12 to 84 V. Source: Power Designers PowerTrac SP+ page (T1), retrieved 2026-10-02. <https://www.powerdesignerssibex.com/powertrac-sp/>
- The 2014 data sheet adds operating temperature -25 to 60 C, reverse-polarity protection, an infrared port with RS-232 and RS-485 options, non-volatile memory, options for external or internal thermistor, electrolyte level sensor, RS-485 (PowerCharge interface) and RS-232 (real-time data collection) (issued 10/2014, dated). Source: PowerTrac SP+ data sheet (T1 (dated)), retrieved 2026-10-02. <https://powerdesignerssibex.com/wp-content/uploads/2024/04/PD-TRA-SP_PowerTrac_SP_BatteryDataLogger.pdf>
- **Conflict-visible note:** the page says SP+ can go on 'any type of battery' from 12 to 84 V, including automotive and stationary batteries; the focus here is motive batteries. The data sheet lists wireless data transfer as a feature but no radio is named.
- **Functions performed (evidence):** [[Measure Battery Voltage]] (V); [[Measure Battery Current]] (V); [[Measure Battery Temperature]] (V); [[Accumulate Amp-Hours]] (V); [[Log Battery Events and Usage]] (V); [[Alert on Abnormal Condition]] (V); [[Communicate with Charger]] (V); [[Sense Electrolyte Level]] (V); [[Export Battery Data to PC]] (V); [[Transmit Battery Data Wirelessly]] (V). V = verified this pass, C = carried from seed text, U = user-stated.
- **Design characteristics (evidence):** [[External Shunt Current Sensing]] (V); [[Infrared Data Port]] (V); [[RS-232 and RS-485 Serial Interface]] (V); [[Non-Volatile Event Memory]] (V); [[Reverse-Polarity Protection]] (V).

## Aliases

- PowerTrac SP
- PowerTrac SP+ Series

## Former ids
