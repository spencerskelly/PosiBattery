---
type: Object
subtype: electrical
id: OBJ-00014
uid: 20261002150858950skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - forklift
  - lead-acid
  - telemetry
subtypeOf:
  - "[[Battery Monitoring Device]]"
performs:
  - "[[Measure Battery Voltage]]"
  - "[[Measure Battery Current]]"
  - "[[Measure Battery Temperature]]"
  - "[[Sense Electrolyte Level]]"
  - "[[Transmit Battery Data Wirelessly]]"
  - "[[Upload Battery Data to Cloud Portal]]"
  - "[[Alert on Abnormal Condition]]"
---

# Energywith withBMS BMU

## Definition

Battery Monitoring Unit installed on forklift lead-acid batteries as the battery-resident measurement hardware for Energywith's withBMS monitoring service.

## Notes

- Manufacturer: Energywith
- Market evidence checked: 2026-10-02
- Vendor explicitly states the BMU is installed on the battery.
- Published measurements include battery voltage, current, temperature, and electrolyte level.
- Data is transferred through an IoT Gateway to the service platform for alerts, reports, operating-condition visualization, and degradation/replacement analysis.
- Vendor states support for JIS-compliant forklift lead-acid batteries.
- Evidence:
  - https://www.energy-with.com/en/solutions/forklift-battery-monitoring/
  - https://www.energy-with.com/en/strength/technology-development/ev-battery-monitoring/
- **Verification 2026-10-02:** not re-verified in this pass; claims above are carried from the seed branch as written.
- **Functions performed (evidence):** [[Measure Battery Voltage]] (C); [[Measure Battery Current]] (C); [[Measure Battery Temperature]] (C); [[Sense Electrolyte Level]] (C); [[Transmit Battery Data Wirelessly]] (C); [[Upload Battery Data to Cloud Portal]] (C); [[Alert on Abnormal Condition]] (C). V = verified this pass, C = carried from seed text, U = user-stated.

## Aliases

- withBMS BMU
- Battery Monitoring Unit

## Former ids
