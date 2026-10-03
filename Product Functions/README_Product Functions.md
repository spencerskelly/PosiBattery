# Product Functions

## Purpose

This folder models what products, systems, or subsystems do. Function notes are phrased as capabilities and support traceability from customer/operational needs to technical designs, product offerings, and measurable outcomes.

## Key function families

- **Charging:** [[Charge Battery]], [[Charge Battery Conventionally]], [[Charge Battery Fast]], [[Charge Battery by Opportunity]], [[Charge Lithium-Ion Battery]], [[Charge Under BMS Control]], [[Control Charge Profile]], [[Compensate Charge for Battery Temperature]], and [[Equalize Battery on Schedule]].
- **Battery condition and protection:** [[Measure Battery Voltage]], [[Measure Battery Current]], [[Measure Battery Temperature]], [[Sense Electrolyte Level]], [[Estimate State of Charge]], [[Estimate State of Health]], [[Detect Cell Failure]], and [[Protect Battery from Deep Discharge]].
- **Communications and data:** [[Communicate Battery State over CAN]], [[Communicate with Charger]], [[Transmit Battery Data Wirelessly]], [[Upload Battery Data to Cloud Portal]], [[Export Battery Data to PC]], and [[Log Battery Events and Usage]].
- **Fleet and operator management:** [[Manage Chargers Remotely]], [[Manage Fleet Use and Data]], [[Configure Device from Mobile App or PC]], [[Display Battery Status to Operator]], and [[Control Operator Access]].
- **Vehicle safety and assistance:** [[Detect Pedestrians and Objects Near Truck]], [[Warn Pedestrians of Approaching Truck]], [[Detect and Record Impacts]], [[Limit Truck Speed Automatically]], [[Maintain Vehicle Stability and Load Awareness]], and [[Support Operator View and Positioning]].
- **Alternative power:** [[Supply Vehicle Energy Without Charging]], [[Refuel Truck Power Source in Minutes]], and [[Report Fuel Cell State to Truck]].

## Navigation

- [[CANVAS_Product Functions]] — visual map of functional concepts.
- `BASE_all_Product Functions.base` — view across all function notes.
- `BASE_local_Product Functions.base` — locally scoped function view.

## Related areas

- [[../Product Designs/README_Product Designs|Product Designs]] — implementation patterns that realize functions.
- [[../Performance Metrics/README_Performance Metrics|Performance Metrics]] — measures used to assess functional outcomes.
- [[../Products/README_Products|Products]] — offerings that perform or expose functions.
- [[../Research/README_Research|Research]] — function maps, comparison work, gaps, and open questions.

## Maintenance

Describe the intended capability rather than a particular technology. Add links to designs that realize the function, products that provide it, and metrics that determine whether it is successful.
