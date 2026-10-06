---
type: Object
subtype: component
id: OBJ-90094
uid: 20261006212000003skellyspencer
status: Draft
tags:
  - reusable-architecture
  - battery-monitoring
  - memory
  - amp-hours
reuseScope: cross-product
hasDesign:
  - "[[Non-Volatile Event Memory]]"
dependsOn:
  - "[[Amp-Hour Accumulator Firmware]]"
partOf:
  - "[[AMETEK Prestolite Power BID with Ah Accumulator]]"
  - "[[AMETEK Prestolite Power WBID]]"
  - "[[AMETEK Prestolite Power WBID Pro]]"
  - "[[EnerSys Wi-iQ]]"
  - "[[Power Designers PowerTrac DT3]]"
  - "[[Power Designers PowerTrac SP+]]"
---

# Amp-Hour Counter State Memory

## Definition

Non-volatile storage used to retain accumulated amp-hour counters and related event/lifetime state across power interruptions.

## Notes

- This Object is allocated only where the available evidence establishes non-volatile memory, lifetime data retention, or persistent battery-history storage.
- The exact technology—internal MCU flash, external EEPROM, FRAM, serial flash, filesystem, or another memory device—is not published and is not inferred.
- [[AMETEK Prestolite Power BID with Ah Accumulator]], [[Power Designers PowerTrac DT3]], and [[Power Designers PowerTrac SP+]] explicitly publish non-volatile memory.
- [[AMETEK Prestolite Power WBID]] stores data for the life of the battery; WBID Pro records long-term battery operating history; [[EnerSys Wi-iQ]] publishes an onboard event-log memory.
- Products can perform [[Accumulate Amp-Hours]] without being linked to this Object when persistence location is not established.

## Former ids
