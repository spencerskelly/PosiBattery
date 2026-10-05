# Product Functions

## Purpose

This folder models what products, systems, or subsystems do. Function notes are phrased as capabilities and support traceability from customer/operational needs to technical designs, product offerings, and measurable outcomes.

## Behavioral navigation by goal

Use the existing modeled Function hierarchy as the primary navigation grouping. These categories are derived from explicit goal-to-family relationships; they do not create a second semantic taxonomy and do not make folder placement authoritative.

- **[[Deliver Energy to Vehicles]]** — charging, charge-profile control, charging availability/safety, non-charging energy supply, and battery/vehicle power-path connection.
- **[[Keep Equipment Working in Its Environment]]** — operation in cold, wet, dusty, weather-exposed, and other harsh conditions.
- **[[Know and Protect Battery Condition]]** — battery sensing, condition reporting, protection, and electrolyte maintenance.
- **[[Manage Fleet Use and Data]]** — battery/vehicle communications, fleet controls, remote management, access, event recording, and telemetry.
- **[[Protect People and Equipment Near Vehicles]]** — collision sensing, automatic speed/stop functions, hazard warning, and vehicle stability/load awareness.
- **[[Support the Operator]]** — operator visibility/positioning, reduced physical effort, and truck-condition information.

The complete 129-function goal → general family → specific function tree is maintained in [[Function and Design Levels]]. Use `BASE_all_Product Functions.base` for exhaustive discovery rather than creating arbitrary count-based folders.

## Navigation

- [[CANVAS_Product Functions]] — visual map of functional concepts.
- `BASE_all_Product Functions.base` — view across all function notes.
- `BASE_local_Product Functions.base` — locally scoped function view.

## Related areas

- [[README_Product Designs|Product Designs]] — implementation patterns that realize functions.
- [[README_Performance Metrics|Performance Metrics]] — measures used to assess functional outcomes.
- [[README_Products|Products]] — offerings that perform or expose functions.
- [[README_Research|Research]] — function maps, comparison work, gaps, and open questions.

## Maintenance

Describe the intended capability rather than a particular technology. Add links to designs that realize the function, products that provide it, and metrics that determine whether it is successful.
