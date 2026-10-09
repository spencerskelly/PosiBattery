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
  - scope-aftermarket
subtypeOf:
  - "[[Battery Monitoring Device]]"
performs:
  - "[[Measure Battery Voltage]]"
  - "[[Measure Battery Current]]"
  - "[[Measure Battery Temperature]]"
  - "[[Sense Electrolyte Level]]"
  - "[[Accumulate Amp-Hours]]"
  - "[[Log Battery Events and Usage]]"
  - "[[Alert on Abnormal Condition]]"
  - "[[Communicate with Charger]]"
  - "[[Transmit Battery Data Wirelessly]]"
  - "[[Export Battery Data to PC]]"
hasDesign:
  - "[[Current Integration Amp-Hour Accumulation]]"
  - "[[External Shunt Current Sensing]]"
  - "[[External Thermistor Temperature Sensor]]"
  - "[[Internal Thermistor Temperature Sensor]]"
  - "[[RS-232 and RS-485 Serial Interface]]"
  - "[[Infrared Data Port]]"
  - "[[Non-Volatile Event Memory]]"
  - "[[Reverse-Polarity Protection]]"
  - "[[Battery-Charger Data Communication Design]]"
  - "[[PC Battery Data Export Design]]"
  - "[[Serial and Infrared PC Data Export]]"
hasPart:
  - "[[Amp-Hour Counter State Memory]]"
  - "[[Battery Current Measurement Circuit]]"
  - "[[Battery Current Acquisition Firmware]]"
  - "[[Amp-Hour Accumulator Firmware]]"
  - "[[Control Circuit]]"
  - "[[Battery Data Export Firmware]]"
  - "[[PC Battery Data Retrieval Software]]"
madeBy:
  - "[[Power Designers]]"
offeredWith:
  - "[[Power Designers REVOLUTION X]]"
dependsOn:
  - "[[Non-Volatile Event Memory]]"
partOf:
  - "[[Power Designers REVOLUTION X]]"
---

# Power Designers PowerTrac SP+

## Definition

Power Designers battery data logger for industrial and motive batteries that attaches to the battery, logs voltage, current and temperature, and uses an external shunt.

## Notes

**Summary:**
Power Designers battery data logger for industrial and motive batteries that uses an external shunt for precise current measurement.

**Marketed features:**
- Logs voltage, current and temperature per event with time stamps
- Lifetime totals of Ah and hours of charge and discharge
- Works with any 50 mV shunt (500 A/50 mV bolt-on and clamp shunts offered)
- 12-84 V nominal batteries; motive, automotive and stationary uses
- Wireless transfer; non-volatile memory; fleet and individual tracking
- Marketed energy savings: avoid peak demand penalties

**Summary and features sources:**
Maker or publisher marketing claims as stated, not independently verified.
- Power Designers (T1), retrieved 2026-10-04. <https://www.powerdesignerssibex.com/powertrac-sp/>
- Power Designers (T1), retrieved 2026-10-04. <https://powerdesignerssibex.com/wp-content/uploads/2024/04/PD-TRA-SP_PowerTrac_SP_BatteryDataLogger.pdf>

- Manufacturer: Power Designers (site and sheets also use the name Power Designers Sibex). POWER TRAC is a registered trademark of Power Designers, LLC for a 'vehicle battery charge monitor' (registry record) <https://trademarks.justia.com/owners/power-designers-llc-1054278>.
- The vendor page says PowerTrac SP+ attaches to the battery, logs instantaneous voltage, current and temperature, charge and discharge Ah since installation and per event, event start time and duration, min and max voltages, and over and under voltage, over current and over temperature alarms; applications listed are forklift trucks, GSE and neighborhood electric vehicles; a 50 mV shunt of any size is used, with 500 A bolt-on (PTBS-500) and clamp-on (PTCS-500) shunts offered; nominal battery voltage 12 to 84 V. Source: Power Designers PowerTrac SP+ page (T1), retrieved 2026-10-02. <https://www.powerdesignerssibex.com/powertrac-sp/>
- The 2014 data sheet adds operating temperature -25 to 60 C, reverse-polarity protection, an infrared port with RS-232 and RS-485 options, non-volatile memory, options for external or internal thermistor, electrolyte level sensor, RS-485 (PowerCharge interface) and RS-232 (real-time data collection) (issued 10/2014, dated). Source: PowerTrac SP+ data sheet (T1 (dated)), retrieved 2026-10-02. <https://powerdesignerssibex.com/wp-content/uploads/2024/04/PD-TRA-SP_PowerTrac_SP_BatteryDataLogger.pdf>
- **Conflict-visible note:** the page says SP+ can go on 'any type of battery' from 12 to 84 V, including automotive and stationary batteries; the focus here is motive batteries. The data sheet lists wireless data transfer as a feature but no radio is named.
- **Functions performed, with citations** (V = verified this pass, C = carried from seed text, U = user-stated):
  - [[Measure Battery Voltage]] (V): <https://www.powerdesignerssibex.com/powertrac-sp/>
  - [[Measure Battery Current]] (V): <https://www.powerdesignerssibex.com/powertrac-sp/>
  - [[Measure Battery Temperature]] (V): <https://www.powerdesignerssibex.com/powertrac-sp/>
  - [[Sense Electrolyte Level]] (V): <https://powerdesignerssibex.com/wp-content/uploads/2024/04/PD-TRA-SP_PowerTrac_SP_BatteryDataLogger.pdf>
  - [[Accumulate Amp-Hours]] (V): <https://www.powerdesignerssibex.com/powertrac-sp/>
  - [[Log Battery Events and Usage]] (V): <https://www.powerdesignerssibex.com/powertrac-sp/>
  - [[Alert on Abnormal Condition]] (V): <https://www.powerdesignerssibex.com/powertrac-sp/>
  - [[Communicate with Charger]] (V): <https://powerdesignerssibex.com/wp-content/uploads/2024/04/PD-TRA-SP_PowerTrac_SP_BatteryDataLogger.pdf>
  - [[Transmit Battery Data Wirelessly]] (V): <https://powerdesignerssibex.com/wp-content/uploads/2024/04/PD-TRA-SP_PowerTrac_SP_BatteryDataLogger.pdf>
  - [[Export Battery Data to PC]] (V): <https://powerdesignerssibex.com/wp-content/uploads/2024/04/PD-TRA-SP_PowerTrac_SP_BatteryDataLogger.pdf>
- **Design characteristics, with citations:**
  - [[External Thermistor Temperature Sensor]] (V, option): <https://powerdesignerssibex.com/wp-content/uploads/2024/04/PD-TRA-SP_PowerTrac_SP_BatteryDataLogger.pdf>
  - [[Internal Thermistor Temperature Sensor]] (V, option): <https://powerdesignerssibex.com/wp-content/uploads/2024/04/PD-TRA-SP_PowerTrac_SP_BatteryDataLogger.pdf>
  - [[External Shunt Current Sensing]] (V): <https://www.powerdesignerssibex.com/powertrac-sp/> <https://powerdesignerssibex.com/wp-content/uploads/2024/04/PD-TRA-SP_PowerTrac_SP_BatteryDataLogger.pdf>
  - [[RS-232 and RS-485 Serial Interface]] (V): <https://powerdesignerssibex.com/wp-content/uploads/2024/04/PD-TRA-SP_PowerTrac_SP_BatteryDataLogger.pdf>
  - [[Infrared Data Port]] (V): <https://powerdesignerssibex.com/wp-content/uploads/2024/04/PD-TRA-SP_PowerTrac_SP_BatteryDataLogger.pdf>
  - [[Non-Volatile Event Memory]] (V): <https://powerdesignerssibex.com/wp-content/uploads/2024/04/PD-TRA-SP_PowerTrac_SP_BatteryDataLogger.pdf>
  - [[Reverse-Polarity Protection]] (V): <https://powerdesignerssibex.com/wp-content/uploads/2024/04/PD-TRA-SP_PowerTrac_SP_BatteryDataLogger.pdf>
- **Sources used for the mapping above:** PowerTrac SP+ page <https://www.powerdesignerssibex.com/powertrac-sp/>; PowerTrac SP+ data sheet (10/2014, dated) <https://powerdesignerssibex.com/wp-content/uploads/2024/04/PD-TRA-SP_PowerTrac_SP_BatteryDataLogger.pdf>
- **GSE parts (round 32):** typical (inferred from the device type, not from a source): mounts on [[GSE Battery Compartment]]. The same device also fits trucks: typical mount [[Truck Battery Compartment]] (see [[Truck Part Connection Register]]). See [[GSE Part Connection Register]].

- **Architecture realization — amp-hour accumulation:** PowerTrac SP+ explicitly measures battery current through an external shunt and reports charge/discharge Ah since installation and per event. [[Current Integration Amp-Hour Accumulation]] is therefore verified at the implementation-principle level. [[Amp-Hour Accumulator Firmware]] and the prerequisite current-acquisition/controller roles are allocated at **>=95% engineering confidence** because the internal firmware partition is not published.

- **Architecture realization — charger communication:** published evidence establishes data exchange with a compatible charger, supporting [[Battery-Charger Data Communication Design]]. The transport and message set remain product-specific.

- **Architecture realization — PC data export:** the published transfer method supports [[PC Battery Data Export Design]] with [[Serial and Infrared PC Data Export]]. [[Battery Data Export Firmware]] and [[PC Battery Data Retrieval Software]] are modeled as reusable roles; their exact implementation and application names are not published.

## Aliases

- PowerTrac SP
- PowerTrac SP+ Series


## Former ids
