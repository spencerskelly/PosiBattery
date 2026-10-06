---
type: Object
subtype: assembly
id: OBJ-90075
uid: 20261006175500007skellyspencer
status: Draft
tags:
  - reusable-architecture
  - battery-monitoring
  - alert
  - local-status
abstract: true
reuseScope: cross-product
hasDesign:
  - "[[Local Abnormal Condition Alert]]"
hasPart:
  - "[[LED Status Indicator Element]]"
  - "[[Audible Alarm Transducer]]"
  - "[[LCD Status Display Module]]"
performs:
  - "[[Alert on Abnormal Condition]]"
partOf:
  - "[[EnerSys Wi-iQ]]"
  - "[[EnerSys iQ Mini]]"
  - "[[Philadelphia Scientific eGO!Mini]]"
  - "[[Philadelphia Scientific eGO!pro]]"
---

# Local Abnormal Alert Output Assembly

## Definition

Reusable local output assembly that presents an abnormal battery condition through LEDs, an audible transducer, a display, or a combination of those outputs.

## Notes

- The `hasPart` list is the reusable option set; a specific product uses only the outputs established by its evidence.
- Alert decision logic is intentionally separate from this output assembly.

## Former ids
