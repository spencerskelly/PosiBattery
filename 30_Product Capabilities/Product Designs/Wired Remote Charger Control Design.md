---
type: Design
subtype:
id: DES-90948
uid: 20261006223500001skellyspencer
status: Draft
tags:
  - charger
  - remote-control
  - wired
  - operator-interface
subtypeOf:
  - "[[Charger Operator Interface Design]]"
designOf:
  - "[[Wired Remote Charger Control Assembly]]"
  - "[[Crown V-HFM3 Wired Remote Control Kit]]"
  - "[[Crown V-HFM3 Charger]]"
realizes:
  - "[[Control Charger from Remote Panel]]"
dependencyOf:
  - "[[Control Charger from Remote Panel]]"
---

# Wired Remote Charger Control Design

## Definition

Reusable design for a physically remote, wired charger control panel that exposes charger status and operator commands away from the charger enclosure.

## Notes

- This Design is distinct from [[Remote Charger Management Design]], which represents networked/cloud remote management.
- A wired remote panel can provide local start/stop/control/status functions without any cloud or wide-area network.
- The Crown V-HFM3 implementation explicitly includes a wired remote, detachable cable, I/O expansion board, internal wiring loom, and DE9 mounting hardware.
- Exact command set, signal voltage, connector pinout, display technology, cable length, and safety interlocks remain product-specific.

## Former ids
