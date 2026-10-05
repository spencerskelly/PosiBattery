# Use and Operations

## Purpose

This is the canonical PosiBattery domain for deployment and operating context: Use Cases, workflows, Procedures, Setups, operating environments, operational issues, and other externally controlled scenarios.

Use this area to describe how products are used, deployed, serviced, maintained, configured, or operated. Product-controlled behavior belongs under [[README_Product Capabilities|Product Capabilities]] as Functions rather than being duplicated here.

See [[Canonical Vault Top-Level Taxonomy 0.1]] and [[PosiBattery Model Organization and Handoff]].

## Use Case versus Function boundary

Use this test before creating or retyping a note:

- **Use Case:** names an externally controlled actor goal or interaction. The actor can explain why they enter the scenario and what outcome tells them the scenario is complete.
- **Function:** names product-controlled behavior. It describes what the product, system, subsystem, software, or accessory does to support one or more Use Cases.
- **Condition / variant:** describes environment, fleet state, deployment mode, or other context that changes a scenario but is not itself an actor goal.
- **Design:** describes the reusable technical approach used to realize behavior.

A verb alone does not determine the type. For example, `Enforce Pre-Shift Checklist` is a Function because the product enforces the behavior; an operational Use Case would be `Authenticate and Complete Pre-Shift Authorization`, where the operator is the external actor pursuing a goal.

Customer Needs under [[README_Customer Needs|Customer Needs]] use `Use Case / subtype: why` to model desired outcomes. Operational scenarios created here should describe the actor interaction itself rather than duplicate those why-level needs.

## What belongs here

Examples include:

- externally controlled Use Cases and scenarios;
- operator, technician, fleet, or site workflows;
- reusable Procedures;
- Verification or operational Setups where use context is primary;
- deployment and environmental context;
- commissioning, service, maintenance, or troubleshooting workflows;
- operational Issues or constraints whose primary meaning is in use.

## Current maturity

The operational model is now being built from evidence-backed actor goals and contexts. Existing customer-need Use Cases in [[README_Customer Needs|Customer Needs]] remain desired outcomes and should not be copied here merely to populate this folder.

### Current operating contexts

Use these as reusable scenario context rather than duplicating environment language inside every Use Case:

- [[Material-Handling Fleet Site]]
- [[Airport Ground-Support Operating Area]]
  - [[Aircraft Service Envelope]]
- [[Centralized Battery Room and Charging Area]]
- [[Distributed and Opportunity Charging Area]]
- [[Shared Vehicle and Pedestrian Work Area]]
- [[Cold Storage Operating Environment]]
- [[Wet Dusty or Outdoor Operating Environment]]

These notes describe where scenarios occur. They do not replace product Functions such as cold-storage operation, charging, proximity detection, or automatic stopping.

### Current operational Use Cases

The first stable operational scenarios are now modeled here:

- [[Connect a Vehicle or Battery to a Charger]]
- [[Opportunity-Charge a Vehicle During a Work Break]]
- [[Start a Shift and Confirm Vehicle Energy Readiness]]
- [[Authenticate and Complete Pre-Shift Authorization]]
- [[Review an Impact Event and Decide Whether to Return the Vehicle to Service]]
- [[Approach and Dock GSE at an Aircraft]]
- [[Review Battery Care and Warranty Compliance]]

These are actor-goal scenarios, not replacements for Product Functions. Only formal `realizedBy` links whose inverse Function relationships are synchronized should be treated as committed semantic traceability; other Function support remains documented evidence until a later traceability pass.

### Reused surrounding systems and equipment

Operational Use Cases should link to existing canonical Objects and products rather than creating duplicate context copies. Common surrounding elements already modeled include [[Industrial Battery Charger]], [[Industrial Traction Battery]], [[Ground Support Equipment]], forklift product classes, battery-monitoring devices, vehicle architecture elements, and fleet/cloud software products.

Facility electrical service, utility/grid connection, building ventilation, racks, aircraft, and other infrastructure should be added as reusable Objects only when the model needs explicit relationships or requirements for them and the intended scope is clear.

## Traceability status

The current stable operational Use Cases identify participating Actors in `participants` and use formal `realizedBy` links only where the inverse Function `realizes` relationship is synchronized.

Customer Needs link into these scenarios through their **Operational traceability** sections. This keeps the chain navigable without introducing provisional `tracesTo` findings:

**Actor → Customer Need → Operational Use Case / context → Function**

No formal Use Case → Requirement links are created yet because the vault currently has no committed `Requirement` model notes for these scenarios. Research notes that describe external rules remain evidence until they are deliberately converted into Requirements.

## Navigation

- `BASE_local_Use and Operations.base` — direct Markdown contents.
- `BASE_all_Use and Operations.base` — recursive Markdown contents.
- [[CANVAS_Use and Operations]] — curated domain map.

## Related areas

- [[README_Customer Needs|Customer Needs]] — desired outcomes and user problems.
- [[README_Product Capabilities|Product Capabilities]] — product-controlled behavior.
- [[README_Stakeholders and Ecosystem|Stakeholders and Ecosystem]] — actors and organizations participating in use.
- [[README_Products|Products]] — offerings used in operational contexts.
