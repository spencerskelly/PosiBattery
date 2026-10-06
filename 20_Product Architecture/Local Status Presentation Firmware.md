---
type: Object
subtype: firmware
id: OBJ-90061
uid: 20261006155500002skellyspencer
status: Draft
tags:
  - reusable-architecture
  - firmware
  - local-status
reuseScope: cross-product
dependsOn:
  - "[[Control Circuit]]"
performs:
  - "[[Indicate Battery Status Locally]]"
partOf:
  - "[[EnerSys Wi-iQ]]"
  - "[[EnerSys iQ Mini]]"
  - "[[Exide Motion+ EasyMonitor]]"
---

# Local Status Presentation Firmware

## Definition

Firmware that converts battery-state and fault information into local visual status, icons, text, colors, or indicator patterns.

## Notes

- Allocation to [[EnerSys Wi-iQ]], [[EnerSys iQ Mini]], and [[Exide Motion+ EasyMonitor]] is an **>=95% engineering-confidence assumption** because these electronic monitors present multi-state local information while the public documents do not disclose the internal software partition.
- This role can select display pages, icons, colors, LED patterns, warning states, and update timing.
- Simple standalone indicators may perform equivalent behavior entirely in hardware and do not require this firmware Object.

## Former ids
