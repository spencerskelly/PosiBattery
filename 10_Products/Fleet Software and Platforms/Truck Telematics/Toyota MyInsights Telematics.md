---
type: Object
subtype: software
id: OBJ-00163
uid: 20261003084359643skellyspencer
status: Draft
tags:
  - scope-oem-option
  - software
  - telematics
subtypeOf:
  - "[[Truck Telematics Software]]"
performs:
  - "[[Report Truck Telemetry]]"
  - "[[Detect and Record Impacts]]"
hasDesign:
  - "[[Impact Sensor]]"
  - "[[Truck Telemetry Reporting Design]]"
madeBy:
  - "[[Toyota Material Handling]]"
offeredWith:
  - "[[Toyota 3-Wheel Electric Forklift]]"
hasPart:
  - "[[Truck Telemetry Acquisition Logic]]"
  - "[[Truck Telemetry Reporting Service]]"
  - "[[Toyota 3-Wheel Electric Forklift]]"
---

# Toyota MyInsights Telematics

## Definition

Toyota's telematics solution, pre-installed on its three-wheel electric forklift.

## Notes

- Toyota says MyInsights delivers fleet insights including impact events and equipment tracking and comes pre-installed on the 3-Wheel Electric Forklift, with data on the MyToyota Portal. Source: Toyota forklift site (T1), retrieved 2026-10-03. <https://www.toyotaforklift.com/forklifts/3-wheel-electric-forklift>
- **Conflict-visible (C61):** one version of the page says the standard telematics data is free of charge; another version of the same page omits that. Source versions: <https://www.toyotaforklift.com/forklifts/3-wheel-electric-forklift>; <https://www.toyotaforklift.com/lifts/electric-motor-rider-forklifts/3-wheel-electric-forklift>.
- **Functions performed, with citations:**
  - [[Report Truck Telemetry]] (V): <https://www.toyotaforklift.com/forklifts/3-wheel-electric-forklift>
  - [[Detect and Record Impacts]] (V): <https://www.toyotaforklift.com/forklifts/3-wheel-electric-forklift>
- **Design characteristics, with citations:**
  - [[Impact Sensor]] (V): <https://www.toyotaforklift.com/forklifts/3-wheel-electric-forklift>
- Toyota says MyInsights provides visibility into impact events and equipment tracking. Source: Toyota forklift site (T1), retrieved 2026-10-03. <https://www.toyotaforklift.com/forklifts/3-wheel-electric-forklift>
- **Truck parts (round 31):** typical (inferred from the device type, not from a source): mounts on [[Truck Controller and CAN Bus]]; connects to [[Truck Controller and CAN Bus]]; acts on [[Truck Controller and CAN Bus]]. See [[Truck Part Connection Register]].

- **Architecture realization — truck telemetry:** published behavior establishes vehicle operating data and event reporting to a fleet-management system, supporting [[Truck Telemetry Reporting Design]]. [[Truck Telemetry Acquisition Logic]] and [[Truck Telemetry Reporting Service]] are allocated at **>=95% engineering confidence** where the vendor does not publish the internal software partition. Exact signal sources, CAN/J1939 mapping, buffering, wireless transport, and cloud protocol remain product-specific.

## Aliases

- MyInsights


## Former ids
