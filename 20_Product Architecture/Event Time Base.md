---
type: Object
subtype: component
id: OBJ-90123
uid: 20261006203800007skellyspencer
status: Draft
tags:
  - reusable-architecture
  - component
  - timekeeping
  - logging
reuseScope: cross-product
dependencyOf:
  - "[[Battery Event Logger Firmware]]"
performs:
  - "[[Log Battery Events and Usage]]"
partOf:
  - "[[Power Designers PowerTrac 3]]"
  - "[[HOPPECKE trak collect]]"
  - "[[EnerSys Wi-iQ]]"
---

# Event Time Base

## Definition

Time-reference role used by an event logger to associate battery records with time, duration, or ordered sequence.

## Notes

- The role may be implemented by a real-time clock, controller timer plus retained epoch, host/gateway time synchronization, or another sequence/time source.
- [[Power Designers PowerTrac 3]] and [[HOPPECKE trak collect]] explicitly publish real-time-clock capability, but this reusable Object does not require a dedicated RTC for every product.
- Accuracy, battery backup, synchronization, drift correction, and timestamp resolution remain product-specific.

## Former ids
