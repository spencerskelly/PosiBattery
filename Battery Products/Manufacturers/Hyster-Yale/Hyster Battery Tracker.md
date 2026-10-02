---
type: Object
subtype: electrical
id: OBJ-00039
uid: 20261002164202407skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - forklift
  - lead-acid
  - oem-branded
  - powered-by-posicharge
subtypeOf:
  - "[[Battery Monitoring Device]]"
describedBy:
  - "[[Battery Product Landscape Conflicts and Open Questions]]"
performs:
  - "[[Estimate State of Charge]]"
  - "[[Sense Electrolyte Level]]"
  - "[[Measure Battery Voltage]]"
  - "[[Measure Battery Current]]"
  - "[[Measure Battery Temperature]]"
  - "[[Alert on Abnormal Condition]]"
  - "[[Upload Battery Data to Cloud Portal]]"
  - "[[Transmit Battery Data Wirelessly]]"
hasDesign:
  - "[[Cellular Communication Interface]]"
  - "[[Cloud Portal Integration]]"
---

# Hyster Battery Tracker

## Definition

Hyster-branded battery monitor, described as powered by PosiCharge technology, that stays with the battery and reports over cellular.

## Notes

- Hyster-Yale introduced Hyster Battery Tracker 'Powered by PosiCharge technology': a low-profile device that stays with the battery, installs in as little as 20 minutes, uses cellular communications to report state of charge, water levels, voltage, current and temperature, sends email notifications, and feeds a reporting suite with daily, weekly and lifetime reports. Source: Trade press listing (undated) (T2), retrieved 2026-10-02. <https://refrigeratedfrozenfood.com/articles/91289-forklift-battery-management-solution-monitors-health-usage>
- **Open (C18):** relationship to [[PosiCharge Battery Rx]] and PosiNET is not stated. Treat as an OEM-branded channel for PosiCharge technology, not an independent competitor, until a source says otherwise.
- **Functions performed (evidence):** [[Estimate State of Charge]] (V); [[Sense Electrolyte Level]] (V); [[Measure Battery Voltage]] (V); [[Measure Battery Current]] (V); [[Measure Battery Temperature]] (V); [[Alert on Abnormal Condition]] (V); [[Upload Battery Data to Cloud Portal]] (V); [[Transmit Battery Data Wirelessly]] (V). V = verified this pass, C = carried from seed text, U = user-stated.
- **Design characteristics (evidence):** [[Cellular Communication Interface]] (V); [[Cloud Portal Integration]] (V).

## Aliases

- Battery Tracker

## Former ids
