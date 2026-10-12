---
type: Function
subtype:
id: FUNC-00123
uid: 20261003221343733skellyspencer
status: Draft
tags:
  - gse-function
  - product-function
subtypeOf:
  - "[[Manage Fleet Use]]"
dependsOn:
  - "[[Wireless Interface Design]]"
  - "[[Remote Vehicle Diagnostics Design]]"
performedBy:
  - "[[TUG Endurance Baggage Tractor]]"
  - "[[TUG ALPHA 1 Pushback]]"
  - "[[Vehicle Diagnostic Data Acquisition Logic]]"
  - "[[Remote Vehicle Diagnostic Service]]"
realizes:
  - "[[Find and Fix Vehicle Faults Without Downtime]]"
realizedBy:
  - "[[Remote Vehicle Diagnostics Design]]"
---

# Diagnose Vehicle Remotely

## Definition

Let a technician or service team read a vehicle's fault and diagnostic data from a distance (wireless link, telemetry or portal) so the cause can be found before or without a visit to the vehicle.

## Notes

- Behavior found in product descriptions. Product links only where a source states the behavior.
- No Requirement is linked (intentional gap).
- Added in round 40 (gap review 2026-10-03) because three GSE products state remote or Bluetooth diagnostics and no existing function covered it. Local-only diagnostics (a display or a PLC on the vehicle) are not linked here; see [[Display Truck Status to Operator]].
- **Sources** (product, evidence level, web page):
  - [[TUG Endurance Baggage Tractor]] (V): <https://www.aviationpros.com/ground-support-worldwide/gse/baggage-cargo/press-release/21280484/textron-gse-textron-gse-introduces-the-tug-endurance-baggage-tractor>
  - [[TUG ALPHA 1 Pushback]] (V): <https://fortbrand.com/products/tug-alpha-1-electric/>

## Implementation Allocation

The reusable realization is [[Remote Vehicle Diagnostics Design]].

[[Vehicle Diagnostic Data Acquisition Logic]] gathers controller faults, diagnostic states, and service snapshots from the vehicle. [[Remote Vehicle Diagnostic Service]] exposes that information to a technician or remote service workflow.

[[Wireless Interface Design]] remains the transport-family dependency. Bluetooth, cellular, Wi-Fi, or a telematics gateway can all carry the diagnostic session.

This Function is intentionally narrower than remote control: reading faults and diagnosing causes does not imply remote fault clearing, configuration, firmware flashing, or vehicle actuation.

[[TUG Endurance Baggage Tractor]] explicitly publishes Bluetooth remote diagnostics. [[TUG ALPHA 1 Pushback]] publishes remote and onboard diagnostics/fleet monitoring. Their internal diagnostic software partitions are modeled at **>=95% engineering confidence** because the vendor does not publish the implementation.

## Aliases

- Remote vehicle diagnostics

## Former ids
