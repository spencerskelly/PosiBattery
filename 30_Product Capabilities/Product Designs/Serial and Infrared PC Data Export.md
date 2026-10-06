---
type: Design
subtype:
id: DES-90942
uid: 20261006210500004skellyspencer
status: Draft
tags:
  - battery-monitoring
  - pc
  - export
  - serial
  - infrared
subtypeOf:
  - "[[PC Battery Data Export Design]]"
designOf:
  - "[[Power Designers PowerTrac SP+]]"
dependsOn:
  - "[[Infrared Data Port]]"
  - "[[RS-232 and RS-485 Serial Interface]]"
---

# Serial and Infrared PC Data Export

## Definition

Local PC data-export path using infrared, RS-232, or RS-485 interfaces.

## Notes

- [[Power Designers PowerTrac SP+]] explicitly provides an infrared port and serial options, including RS-232 for real-time data collection.
- The current source does not establish which interface is used for every export workflow, so both verified local service interfaces remain available within this Design.
- Exact cable/adapter, serial framing, IR protocol, and PC application are not published.

## Former ids
