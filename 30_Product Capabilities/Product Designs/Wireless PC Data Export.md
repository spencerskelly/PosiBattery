---
type: Design
subtype:
id: DES-90941
uid: 20261006210500003skellyspencer
status: Draft
tags:
  - battery-monitoring
  - pc
  - export
  - wireless
subtypeOf:
  - "[[PC Battery Data Export Design]]"
designOf:
  - "[[Power Designers PowerTrac DT3]]"
dependsOn:
  - "[[900 MHz Industrial Wireless Interface]]"
---

# Wireless PC Data Export

## Definition

PC data-export path in which logged battery data is transferred over a short-range wireless link to a PC-side receiver or adapter.

## Notes

- [[Power Designers PowerTrac DT3]] explicitly uses 900 MHz industrial wireless and a PowerTrac Link USB device for PC upload.
- The exact RF protocol, adapter architecture, pairing, and transfer framing are not published.
- This Design can coexist with a USB adapter because the battery-device side can be wireless while the PC-side adapter is USB.

## Former ids
