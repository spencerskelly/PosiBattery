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
  - scope-aftermarket
  - telemetry
subtypeOf:
  - "[[Battery Monitoring Device]]"
performs:
  - "[[Measure Battery Voltage]]"
  - "[[Measure Battery Current]]"
  - "[[Measure Battery Temperature]]"
  - "[[Sense Electrolyte Level]]"
  - "[[Alert on Abnormal Condition]]"
  - "[[Transmit Battery Data Wirelessly]]"
  - "[[Upload Battery Data to Cloud Portal]]"
  - "[[Log Battery Events and Usage]]"
madeBy:
dependencyOf:
  - "[[Energywith withBMS Analytics Service]]"
  - "[[Energywith]]"
---

# Energywith withBMS BMU

## Definition

Battery Monitoring Unit installed on forklift lead-acid batteries as the battery-resident measurement hardware for Energywith's withBMS monitoring service.

## Notes

**Summary:**
Battery monitoring unit installed on forklift lead-acid batteries as the measurement hardware for Energywith's withBMS monitoring service.

**Marketed features:**
- 24/7 measurement of current, total voltage, temperature and electrolyte level
- Data to the service platform via an IoT gateway
- Alerts for insufficient watering, overcharge and abnormal heating
- Reports on operation, idle and charging time per site
- Replacement-timing estimates from degradation trends
- Supports all JIS-compliant forklift lead-acid batteries

**Summary and features sources:**
Maker or publisher marketing claims as stated, not independently verified.
- Energywith (T1), retrieved 2026-10-04. <https://www.energy-with.com/en/solutions/forklift-battery-monitoring/>
- Energywith (T1), retrieved 2026-10-04. <https://www.energy-with.com/en/strength/technology-development/ev-battery-monitoring/>

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
- **Functions performed, with citations** (V = verified this pass, C = carried from seed text, U = user-stated):
  - [[Measure Battery Voltage]] (C): <https://www.energy-with.com/en/solutions/forklift-battery-monitoring/>
  - [[Measure Battery Current]] (C): <https://www.energy-with.com/en/solutions/forklift-battery-monitoring/>
  - [[Measure Battery Temperature]] (C): <https://www.energy-with.com/en/solutions/forklift-battery-monitoring/>
  - [[Sense Electrolyte Level]] (C): <https://www.energy-with.com/en/solutions/forklift-battery-monitoring/>
  - [[Alert on Abnormal Condition]] (C): <https://www.energy-with.com/en/solutions/forklift-battery-monitoring/>
  - [[Transmit Battery Data Wirelessly]] (C): <https://www.energy-with.com/en/solutions/forklift-battery-monitoring/>
  - [[Upload Battery Data to Cloud Portal]] (C): <https://www.energy-with.com/en/solutions/forklift-battery-monitoring/>
  - [[Predict Battery Replacement Timing]] (V): <https://www.energy-with.com/en/solutions/forklift-battery-monitoring/>
  - [[Log Battery Events and Usage]] (V): <https://www.energy-with.com/en/solutions/forklift-battery-monitoring/>
- **Sources used for the mapping above:** Seed note (cites the Energywith vendor pages) <https://www.energy-with.com/en/solutions/forklift-battery-monitoring/>
- **Truck parts (round 31):** typical (inferred from the device type, not from a source): mounts on [[Truck Battery Compartment]]. See [[Truck Part Connection Register]].

- **Architecture correction — replacement timing:** Energywith's published architecture places degradation/replacement analysis in the service platform, while this BMU is the battery-resident measurement source. [[Energywith withBMS Analytics Service]] therefore performs [[Predict Battery Replacement Timing]], and this BMU supplies its data.

## Aliases

- withBMS BMU
- Battery Monitoring Unit


## Former ids
