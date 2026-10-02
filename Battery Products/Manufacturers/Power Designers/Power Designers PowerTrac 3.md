---
type: Object
subtype: electrical
id: OBJ-00034
uid: 20261002164202402skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - forklift
  - lead-acid
  - charge-interface
subtypeOf:
  - "[[Battery Monitoring Device]]"
  - "[[Battery Identification and Charge Interface Device]]"
performs:
  - "[[Measure Battery Voltage]]"
  - "[[Measure Battery Temperature]]"
  - "[[Measure Battery Current]]"
  - "[[Sense Electrolyte Level]]"
  - "[[Log Battery Events and Usage]]"
  - "[[Transmit Battery Data Wirelessly]]"
  - "[[Track Equalization]]"
  - "[[Identify Battery to Charger]]"
  - "[[Communicate with Charger]]"
hasDesign:
  - "[[Shuntless Current Sensing]]"
  - "[[Non-Volatile Event Memory]]"
---

# Power Designers PowerTrac 3

## Definition

Power Designers wireless battery monitoring device with shuntless intercell sensing and an electrolyte sensor that also lets a Power Designers REVOLUTION charger recognize the battery.

## Notes

- Manufacturer: Power Designers (Power Designers Sibex).
- The vendor page says PowerTrac 3 tracks voltage, temperature, current and electrolyte level (variable-length probe), stores up to 10,000 events, transfers data wirelessly, uses a shuntless design, uses up to 90 percent less energy than previous models, and reports cycles, equalization status and kWh per event; it communicates with the REVOLUTION charger so the charger can automatically recognize battery voltage (24/36/48 V, footnoted by charger rating) and Ah capacity. Source: Power Designers PowerTrac 3 page (T1), retrieved 2026-10-02. <https://powerdesignerssibex.com/powertrac-3-wireless-battery-monitor/>
- **Not retrieved:** the specification sheet and installation guides linked from the page (radio band, nominal voltage range, operating temperature). **Competitive relevance:** closest match found to the BMID behavior of identifying a battery to a charger by a charger vendor's own monitor.
- **Functions performed (evidence):** [[Measure Battery Voltage]] (V); [[Measure Battery Temperature]] (V); [[Measure Battery Current]] (V); [[Sense Electrolyte Level]] (V); [[Log Battery Events and Usage]] (V); [[Transmit Battery Data Wirelessly]] (V); [[Track Equalization]] (V); [[Identify Battery to Charger]] (V); [[Communicate with Charger]] (V). V = verified this pass, C = carried from seed text, U = user-stated.
- **Design characteristics (evidence):** [[Shuntless Current Sensing]] (V); [[Non-Volatile Event Memory]] (V).

## Aliases

- PowerTrac 3
- PT3

## Former ids
