---
type: Object
subtype: software
id: OBJ-00221
uid: 20261003093855190skellyspencer
status: Draft
tags:
  - battery-charger-software
  - battery-market-reference
  - commercial-product
  - scope-oem-option
  - software
subtypeOf:
  - "[[Battery and Charger Management Software]]"
performs:
  - "[[Compensate Charge for Battery Temperature]]"
  - "[[Communicate with Charger]]"
madeBy:
  - "[[Stryten Energy]]"
offeredWith:
  - "[[Stryten X-7 Charger]]"
  - "[[Stryten X-3 Charger]]"
  - "[[Stryten M-Series Li610 Battery]]"
hasDesign:
  - "[[Battery-Charger Data Communication Design]]"
  - "[[Stryten M-Series Li610 Battery]]"
partOf:
  - "[[Stryten X-7 Charger]]"
---

# Stryten inCOMMAND

## Definition

Stryten energy performance management software for its batteries and chargers.

## Notes

- Stryten says M-Series chargers communicate with inCOMMAND, which monitors key battery data points in real time, and the charger adjusts its charge rate if battery temperature rises; the M-Series Li610 integrates with inCOMMAND. Source: Stryten article on X-7 chargers and Li610 release (T1/T2), retrieved 2026-10-03. <https://stryten.com/?p=173790>
- Stryten's 2023 naming release describes software for energy performance management of batteries and chargers. Source: Stryten release (2023-03-14) (T1), retrieved 2026-10-03. <https://www.stryten.com/?p=207972>
- **Functions performed, with citations:**
  - [[Compensate Charge for Battery Temperature]] (V): <https://stryten.com/?p=173790>
  - [[Communicate with Charger]] (V): <https://stryten.com/?p=173790>

- **Architecture realization — charger communication:** published evidence establishes data exchange with a compatible charger, supporting [[Battery-Charger Data Communication Design]]. The transport and message set remain product-specific.

## Aliases

- inCOMMAND


## Former ids
