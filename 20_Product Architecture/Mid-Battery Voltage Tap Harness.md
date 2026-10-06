---
type: Object
subtype: assembly
id: OBJ-90079
uid: 20261006183500005skellyspencer
status: Draft
tags:
  - reusable-architecture
  - battery-monitoring
  - voltage
  - harness
reuseScope: cross-product
hasDesign:
  - "[[Mid-Battery Voltage Tap]]"
partOf:
  - "[[EnerSys Wi-iQ]]"
  - "[[Exide Motion+ EasyMonitor]]"
  - "[[HOPPECKE trak collect]]"
dependencyOf:
  - "[[Mid-Battery Differential Voltage Measurement Circuit]]"
---

# Mid-Battery Voltage Tap Harness

## Definition

Physical balance-wire or midpoint-tap connection that brings the battery midpoint voltage to a monitoring circuit.

## Notes

- [[EnerSys Wi-iQ]] explicitly uses a gray balance wire with fuse for half-battery voltage measurement.
- [[Exide Motion+ EasyMonitor]] explicitly uses a middle-voltage tap for imbalance detection.
- [[HOPPECKE trak collect]] is linked because its existing verified [[Mid-Battery Voltage Tap]] Design establishes the physical midpoint connection, even though this pass does not assign it the [[Detect Voltage Imbalance]] Function.
- Connector, wire gauge, fuse rating, insulation, routing and attachment hardware remain product-specific.

## Former ids
