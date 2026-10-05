---
type: Info
subtype:
id: INFO-90004
uid: 20261005113400000skellyspencer
status: Draft
tags:
  - product-context
  - bmid
  - posicharge
---

# PosiCharge BMID Product Context

## Purpose

Define the external systems, equipment, actors, environments, and interface boundaries needed to understand the [[PosiCharge BMID]] family in operation without treating those external elements as BMID parts.

## Product of Interest

[[PosiCharge BMID]] is the product family at the center of this context.

The BMID boundary includes the battery-installed electronics, directly integrated sensing, stored battery identity/profile/history, and product-defined external communication interfaces. Everything below is external unless a specific child-product definition explicitly incorporates it.

## External Physical Systems

### Industrial traction battery

[[Industrial Traction Battery]] is the physical host and energy-storage system associated with the BMID.

The BMID may sense supported battery quantities and retain battery-specific identity or history, but the electrochemical battery itself remains outside the BMID product boundary.

### Industrial battery charger

[[Industrial Battery Charger]] is the external charging system.

BMID-family behavior may provide identity, temperature, condition, or other supported data to a compatible charger. The charger remains responsible for charger-controlled current, voltage, charging algorithms, and power conversion.

[[PosiCharge ProCore Edge]] is one evidence-backed example of a compatible PosiCharge charger, not a mandatory family dependency.

### Industrial vehicle

The BMID operates with batteries used in material-handling vehicles such as [[Class I Electric Rider Truck]] and with [[Ground Support Equipment]].

The vehicle remains external context. Vehicle CAN or other data-bus interaction is variant-specific and must not be generalized across the BMID family.

### Battery management system

[[Battery Management System]] is external context when a battery has a BMS.

The BMID and BMS roles must remain distinct. A BMS may own battery protection, limits, or CAN-based charge-control information; the BMID role is defined only by supported product behavior. Later requirements must resolve overlap explicitly for lithium applications.

## External Digital and Service Systems

### Fleet and cloud platform

[[PosiCharge PosiLink]] is an evidence-backed external fleet/cloud system for supported products such as PosiGuard and Battery Rx-related workflows.

Cloud upload is not assumed for every BMID generation.

### Local configuration and service tool

[[PosiCharge PosiConnect]] is an evidence-backed configuration/service application for [[PosiCharge PosiGuard]].

Mobile-app configuration is therefore variant-specific rather than a mandatory BMID-family interface.

## Human and Organizational Actors

Primary human roles already modeled for BMID use include:

- [[Forklift Operator]]
- [[GSE Operator]]
- [[Maintenance Technician]]
- [[Fleet Operations Manager]]
- [[Dealer Service Technician]]
- [[Equipment Installer]]
- [[Truck OEM Integration Engineer]]

These are external actors. They participate through the product Use Cases rather than becoming product architecture elements.

## Operating Environments

The BMID family is currently modeled in these reusable operating contexts:

- [[Material-Handling Fleet Site]]
- [[Airport Ground-Support Operating Area]]
- [[Centralized Battery Room and Charging Area]]
- [[Distributed and Opportunity Charging Area]]

Environmental constraints such as temperature, water, dust, washdown, vibration, chemical exposure, and airport/outdoor use become product requirements only when supported by product evidence or an approved design target.

## Context Interactions

### Battery-side interaction

Potential interaction categories include supported voltage, current, temperature, electrolyte-level, identity, state/history, and BMS/CAN information.

These categories are **not universal family requirements**. Each later requirement must identify which BMID variant or product definition it applies to.

### Charger interaction

Supported BMID variants may identify the battery, report battery information, or exchange other charging-related data with a compatible charger.

The BMID provides information; charger power-control authority remains external unless explicitly reassigned by a future requirement.

### Vehicle interaction

A supported variant may exchange battery state or other data with vehicle electronics. Current evidence supports CAN-related behavior for specific products, not every BMID.

### Fleet/cloud interaction

Supported variants may upload logs, alerts, battery history, or fleet information to external systems. This is variant/system dependent.

### Configuration/service interaction

Supported variants may expose local configuration, firmware-update, log-export, or status interfaces to service tools. Current direct evidence is strongest for PosiGuard with PosiConnect.

## Product Use Cases in This Context

- [[Charge a BMID-Equipped Battery Using Battery Information]]
- [[Inspect Battery Condition Through a BMID]]
- [[Review BMID Battery History and Exceptions]]
- [[Configure and Service a Supported BMID]]
- [[Integrate a BMID with Charger Vehicle and Fleet Systems]]

## Boundary Rules

- External context is not modeled as BMID `hasPart`.
- A surrounding product is not a mandatory dependency merely because one BMID generation integrates with it.
- Variant-specific interfaces must remain variant-specific.
- Physical mounting, connector pinout, protocol, wiring, and BMS ownership must not be inferred from market-level evidence.
- Reusable vehicle and GSE architecture stays in the existing Product Architecture sets rather than being copied into the BMID model.
- Later Local Model work may create contextual occurrences without changing these reusable definitions.

## Visual Context

See [[CANVAS_PosiCharge BMID Product Context]].

Canvas edges are explanatory context labels only. They are not authoritative MDSE relationship assertions unless the same relationship is explicitly stored in governed YAML.
