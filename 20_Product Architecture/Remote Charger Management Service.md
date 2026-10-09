---
type: Object
subtype: software
id: OBJ-90136
uid: 20261006215000002skellyspencer
status: Draft
tags:
  - reusable-architecture
  - software
  - charger
  - remote-management
reuseScope: cross-product
hasDesign:
  - "[[Remote Charger Management Design]]"
performs:
  - "[[Manage Chargers Remotely]]"
partOf:
  - "[[ACT ACTview]]"
  - "[[PosiCharge SkyLink]]"
  - "[[Manage Chargers Remotely]]"
---

# Remote Charger Management Service

## Definition

Hosted or remote software service that presents charger status and issues authorized configuration, update, troubleshooting, or control operations to managed chargers.

## Notes

- Candidate responsibilities include fleet selection, charger status, configuration, firmware deployment, diagnostics, remote support actions, user/role enforcement, audit logging, and command tracking.
- This Object does not require a specific cloud provider or API.

## Former ids
