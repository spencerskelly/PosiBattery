---
type: Document
subtype:
id: DOC-00350
uid: 20261014132745961skellyspencer
status: Draft
tags:
  - source-document
  - tier-T1
sourceClass: standard
sourceUrl: "https://vda.de/dam/jcr:f0c9c019-1506-4dee-998a-e92723fbf025/VDA5050-V2p1p0.pdf"
accessed: 2026-10-14
describes:
  - "[[Warehouse and Business Software Landscape Register]]"
---

# Document - VDA 5050 Version 2.1.0 AGV Communication Interface

## Definition

VDA 5050 version 2.1.0, the interface between AGVs and a master control.

## Notes

Facts below were read through the fetch tool's summary of the page, not from the raw page; vendor statements are claims.

- Transport: MQTT with JSON. State is published by the AGV on events and at least every 30 seconds.
- batteryState (section 6.10.6): batteryCharge (percent), batteryVoltage (V), charging (true or false), batteryHealth (percent) and reach (m).
- Actions startCharging and stopCharging (sections 6.8.1 and 6.8.2) can be sent by master control as instant or node actions; charging can happen at a spot or on a lane; protection against overcharging is the vehicle's responsibility; energy management is a master control function and charging orders can interrupt transfer orders.
- No charge thresholds are defined; the specification is written for AGVs and treats freely navigating vehicles as out of detailed scope.

## Provenance

- **Source identity:** VDA.
- **Original web address:** <https://vda.de/dam/jcr:f0c9c019-1506-4dee-998a-e92723fbf025/VDA5050-V2p1p0.pdf>.
- **Access date:** 2026-10-14. **Revision:** V2.1.0
- **Evidence tier:** T1 industry standard (VDA) (values second-hand through the fetch tool's summary).

## Traceability

- `describes` links the document to the products it covers; disagreements are logged in the conflict register.

## Aliases

## Former ids
