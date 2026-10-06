---
type: Design
subtype:
id: DES-90945
uid: 20261006215000001skellyspencer
status: Draft
tags:
  - charger
  - remote-management
  - cloud
  - control
designOf:
  - "[[Remote Charger Management Service]]"
  - "[[Charger Remote Management Agent]]"
realizes:
  - "[[Manage Chargers Remotely]]"
dependencyOf:
  - "[[Manage Chargers Remotely]]"
---

# Remote Charger Management Design

## Definition

Reusable design for remotely monitoring, configuring, updating, troubleshooting, or controlling a charger through a networked management service.

## Notes

- This Design requires more than passive telemetry visibility. It represents an actionable management path such as remote settings, firmware update, troubleshooting, commands, or service operations.
- [[Remote Charger Management Service]] represents the portal/cloud-side management role.
- [[Charger Remote Management Agent]] represents the charger-side endpoint that accepts authenticated management operations and applies them locally.
- The network path may use Wi-Fi, Ethernet, cellular, or another IP-capable connection.
- Command set, permissions, update security, rollback, buffering, audit logging, offline behavior, and cloud protocol remain product-specific.

## Former ids
