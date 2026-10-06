---
type: Design
subtype:
id: DES-90914
uid: 20261006180500002skellyspencer
status: Draft
tags:
  - battery-monitoring
  - design-characteristic
  - firmware
  - equalization
subtypeOf:
  - "[[Equalization Event Tracking Design]]"
designOf:
  - "[[Equalization Event Tracking Firmware]]"
---

# Local Equalization Event Classification

## Definition

Equalization tracking performed locally by classifying charge-session measurements or charge-state history as an equalization event and storing the resulting event or duration.

## Notes

- Candidate inputs include charge voltage, current, charge duration, charge-state transitions, charger commands, temperature, and stored charge history.
- Candidate outputs include equalization-complete flags, timestamps, durations, counts, or accumulated equalization hours.
- This is a reusable engineering alternative. No current product is assigned because available sources do not establish that the equalization determination is made locally from measurements.

## Former ids
