---
type: Design
subtype:
id: DES-90947
uid: 20261006222000001skellyspencer
status: Draft
tags:
  - vehicle
  - diagnostics
  - remote-service
  - telematics
designOf:
  - "[[Vehicle Diagnostic Data Acquisition Logic]]"
  - "[[Remote Vehicle Diagnostic Service]]"
realizes:
  - "[[Diagnose Vehicle Remotely]]"
dependencyOf:
  - "[[Diagnose Vehicle Remotely]]"
dependsOn:
  - "[[Wireless Interface Design]]"
---

# Remote Vehicle Diagnostics Design

## Definition

Reusable design for acquiring vehicle fault and diagnostic information and making it available to a remote technician or service system for fault isolation without requiring an immediate vehicle visit.

## Notes

- [[Vehicle Diagnostic Data Acquisition Logic]] gathers fault codes, controller state, monitored conditions, and diagnostic snapshots from the vehicle.
- [[Remote Vehicle Diagnostic Service]] transports and presents that diagnostic information to a remote technician or service workflow.
- The network path may be Bluetooth, cellular, Wi-Fi, telematics gateway, or another supported wireless link.
- This Design is distinct from [[Truck Telemetry Reporting Design]]: telemetry may report routine usage/status, while remote diagnostics focuses on fault isolation and service troubleshooting.
- Fault-clear commands, parameter changes, software flashing, and remote actuation are not assumed unless separately evidenced.
- Diagnostic protocol, DTC format, controller coverage, data retention, snapshot content, and remote-security model remain product-specific.

## Former ids
