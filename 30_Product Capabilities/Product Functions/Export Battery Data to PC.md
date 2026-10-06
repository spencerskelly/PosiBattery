---
type: Function
subtype:
id: FUNC-00021
uid: 20261002164202367skellyspencer
status: Draft
tags:
  - battery-monitoring
  - extra
  - product-function
subtypeOf:
  - "[[Communicate Battery and Vehicle Data]]"
performedBy:
  - "[[Philadelphia Scientific eGO!Mini]]"
  - "[[Power Designers PowerTrac DT3]]"
  - "[[Battery Data Export Firmware]]"
  - "[[PC Battery Data Retrieval Software]]"
dependsOn:
  - "[[PC Battery Data Export Design]]"
realizedBy:
  - "[[PC Battery Data Export Design]]"
  - "[[Power Designers PowerTrac SP+]]"
---

# Export Battery Data to PC

## Definition

Move logged data to a PC for analysis, by cable, USB or short-range wireless.

## Notes

- Includes technician download tools.
- Product links are made only where a source states the behavior; no link means unknown, not absent. Overview: [[Function Map]].
- No Requirement is linked: nothing here is a committed requirement, so model-health will show these Functions without satisfied Requirements. That gap is intentional.
- **Sources** (product, evidence level, web page):
  - [[Philadelphia Scientific eGO!Mini]] (V): <https://www.phlsci.com/media/151762/ego-mini-egou-ps-ssh-doc0184-eng.pdf>
  - [[Power Designers PowerTrac SP+]] (V): <https://powerdesignerssibex.com/wp-content/uploads/2024/04/PD-TRA-SP_PowerTrac_SP_BatteryDataLogger.pdf>
  - [[Power Designers PowerTrac DT3]] (V): <https://www.powerdesignerssibex.com/wp-content/uploads/2024/04/PDS-PT-DT3_PowerTracDT3.pdf>
- **Extra (round 30):** documented for 0 of 21 battery maker groups (0 percent); the reusable realization is now [[PC Battery Data Export Design]], with USB, wireless, and serial/infrared transfer paths kept distinct.

## Implementation Allocation

The reusable realization is [[PC Battery Data Export Design]] -> [[Battery Data Export Firmware]] plus [[PC Battery Data Retrieval Software]].

### USB path

[[USB Battery Data Export]] applies to [[Philadelphia Scientific eGO!Mini]] and [[Power Designers PowerTrac DT3]]. eGO!Mini uses removable USB media; DT3 uses a PowerTrac Link USB adapter.

### Wireless path

[[Wireless PC Data Export]] applies to [[Power Designers PowerTrac DT3]], where the battery-side device communicates over 900 MHz industrial wireless and the PC-side link terminates through a USB adapter.

### Serial / infrared path

[[Serial and Infrared PC Data Export]] applies to [[Power Designers PowerTrac SP+]], which publishes an infrared data port and RS-232/RS-485 service interfaces.

The export behavior is separate from [[Log Battery Events and Usage]]: logging creates and retains records; export transfers those records to a PC.

## Aliases


## Former ids
