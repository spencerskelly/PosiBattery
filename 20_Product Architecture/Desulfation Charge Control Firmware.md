---
type: Object
subtype: firmware
id: OBJ-90154
uid: 20261006234100002skellyspencer
status: Draft
tags:
  - reusable-architecture
  - firmware
  - charger
  - desulfation
reuseScope: cross-product
hasDesign:
  - "[[Lead-Acid Desulfation Charge Control Design]]"
dependsOn:
  - "[[Control Circuit]]"
performs:
  - "[[Desulfate Battery During Charge]]"
partOf:
  - "[[EnerSys Express Charger]]"
  - "[[EnerSys IMPAQ Charger]]"
  - "[[EnerSys NexSys+ Charger]]"
  - "[[Power Designers REVOLUTION X]]"
---

# Desulfation Charge Control Firmware

## Definition

Charger-control firmware that selects, sequences, supervises, and terminates a lead-acid desulfation charging profile while commanding the charger power stage.

## Notes

- Candidate responsibilities include chemistry/profile eligibility checks, profile selection, current/voltage command sequencing, phase timing, completion criteria, safety-limit enforcement, fault fallback, and return to normal charging.
- The firmware realization is an engineering abstraction at **>=95% confidence** because all allocated products explicitly provide a desulfation cycle/profile while their internal software partition is unpublished.
- No specific pulse shape, frequency, amplitude, algorithm, or proprietary EnerSys/Power Designers implementation is asserted.
- Physical energy conversion remains in the charger power stage rather than this firmware Object.

## Former ids
