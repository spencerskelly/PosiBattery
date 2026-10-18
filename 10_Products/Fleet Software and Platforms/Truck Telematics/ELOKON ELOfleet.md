---
type: Object
subtype: software
id: OBJ-00502
uid: 20261013220922866skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - scope-aftermarket
  - software
  - telematics
  - vehicle-accessory
  - retrofit-kit
  - third-party-kit
productCategory: fleet-software
commInterfaces:
  - bluetooth
  - wi-fi
  - rfid
subtypeOf:
  - "[[Truck Telematics Software]]"
describedBy:
  - "[[Document - ELOKON ELOfleet Product Page (retrieved 2026-10-13)]]"
performs:
  - "[[Control Operator Access]]"
  - "[[Detect and Record Impacts]]"
  - "[[Enforce Pre-Shift Checklist]]"
  - "[[Report Truck Telemetry]]"
  - "[[Limit Truck Speed Automatically]]"
hasDesign:
  - "[[Impact Sensor]]"
madeBy:
  - "[[ELOKON]]"
---

# ELOKON ELOfleet

## Definition

ELOKON ELOfleet OEM-neutral forklift fleet management system, sold as Sprint and Smart variants, retrofit to any make.

## Notes

- One family note; variants:
  - **Smart:** all listed features.
  - **Sprint:** omits front-end terminal display, PIN access, pre-operational checklist, configurable safety message and impact checklist (inferred by the fetch tool from a table that lost its check marks; unverified, C238).
- Phone/tablet based with Bluetooth vehicle sensors; MEMS impact detection; RFID or PIN login; maintenance block when due; presence detection; optional load-on-fork recognition; Azure or on-premises hosting; Wi-Fi; TYCO and VDI interfaces. Battery monitoring not mentioned. Source: <https://www.elokon.com/en-US/material-handling/elofleet-smart-forklift-fleet-management> (T1, second-hand).
- **Functions performed, with citations:**
  - [[Control Operator Access]] (V): <https://www.elokon.com/en-US/material-handling/elofleet-smart-forklift-fleet-management>
  - [[Detect and Record Impacts]] (V): <https://www.elokon.com/en-US/material-handling/elofleet-smart-forklift-fleet-management>
  - [[Enforce Pre-Shift Checklist]] (V, Smart only): <https://www.elokon.com/en-US/material-handling/elofleet-smart-forklift-fleet-management>
  - [[Report Truck Telemetry]] (V): <https://www.elokon.com/en-US/material-handling/elofleet-smart-forklift-fleet-management>
  - [[Limit Truck Speed Automatically]] (V, creep speed after severe impact): <https://www.elokon.com/en-US/material-handling/elofleet-smart-forklift-fleet-management>
- **Design characteristics, with citations:**
  - [[Impact Sensor]] (V, MEMS): <https://www.elokon.com/en-US/material-handling/elofleet-smart-forklift-fleet-management>

## Aliases

- ELOfleet
- ELOfleet Sprint
- ELOfleet Smart


## Former ids
