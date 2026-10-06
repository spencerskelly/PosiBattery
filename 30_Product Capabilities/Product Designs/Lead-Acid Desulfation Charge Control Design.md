---
type: Design
subtype:
id: DES-90960
uid: 20261006234100001skellyspencer
status: Draft
tags:
  - charger
  - lead-acid
  - desulfation
  - charge-control
designOf:
  - "[[Desulfation Charge Control Firmware]]"
  - "[[EnerSys Express Charger]]"
  - "[[EnerSys IMPAQ Charger]]"
  - "[[EnerSys NexSys+ Charger]]"
  - "[[Power Designers REVOLUTION X]]"
realizes:
  - "[[Desulfate Battery During Charge]]"
dependencyOf:
  - "[[Desulfate Battery During Charge]]"
dependsOn:
  - "[[Charger Power Stage Design]]"
---

# Lead-Acid Desulfation Charge Control Design

## Definition

Reusable charger-control design that executes a dedicated lead-acid desulfation charging cycle or profile and commands the charger power stage to apply the required electrical output.

## Notes

- Published product evidence establishes a desulfation cycle/profile on the allocated chargers, but does not establish a common proprietary algorithm, waveform, pulse method, voltage/current thresholds, duration, or termination logic.
- [[Desulfation Charge Control Firmware]] represents the controller-side sequencing and profile logic at **>=95% engineering confidence**; the exact internal software partition is not published.
- [[Charger Power Stage Design]] supplies the commanded current/voltage output. This Design is therefore control behavior rather than a separate power-conversion topology.
- The model intentionally does not assume pulse desulfation, high-frequency excitation, chemical additives, or dedicated desulfation hardware because the current sources do not establish those mechanisms.
- Applicability is limited to supported lead-acid battery profiles; chemistry eligibility and safety limits remain product-specific.

## Former ids
