---
type: Object
subtype: firmware
id: OBJ-90910
uid: 20261013161000003skellyspencer
status: Draft
tags:
  - reusable-architecture
  - firmware
  - battery-monitoring
  - state-of-health
reuseScope: cross-product
dependsOn:
  - "[[Battery Voltage Acquisition Firmware]]"
  - "[[Battery Current Acquisition Firmware]]"
performs:
  - "[[Segment Discharge Cycles]]"
describedBy:
  - "[[SOC and Health Estimation Literature Review]]"
---

# Discharge Cycle Segmentation Firmware

## Definition

Candidate firmware that finds where each charge or discharge cycle begins and ends in the measured current and voltage and labels which cycles are complete.

## Notes

- **Candidate implementation, not a product claim.** No modeled product is allocated. It is the performer for [[Segment Discharge Cycles]] so that the function has an owner; the cycle rules are not specified by any source in the vault.
- Every source in [[SOC and Health Estimation Literature Review]] uses laboratory data with a full constant-current discharge; none describes segmentation under partial discharge or opportunity charging.
- Allocation (engineering inference): embedded, on the battery-side device, since it consumes the sampled voltage and current streams.

## Former ids
