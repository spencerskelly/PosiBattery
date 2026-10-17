---
type: Requirement
subtype: engineering
id: REQ-00058
uid: 20261017132008000skellyspencer
status: Draft
tags:
  - regulatory-driver
  - candidate-from-research
  - analyst-proposed
appliesTo:
  - "[[Industrial Battery Charger]]"
derivedFrom:
  - "[[Oregon CFP - Forklift Charging Energy Shall Be Directly Metered]]"
  - "[[California LCFS - Forklift Charging Energy Shall Be Metered]]"
---

# Charging Energy Reporting - Provide Unadjusted Energy Data at the Output or Forklift Side

## Definition

A charger, or the software that collects its data, shall be able to report energy delivered to the battery per charger and, where fitted, per forklift, as measured data with no efficiency or other adjustment applied, together with the measurement point and its identity.

## Notes

- **Proposed from the regulation text; there is no customer or stakeholder source for it.** It stays Draft until a person decides whether it is a requirement.
- Why (analyst reasoning): Oregon forbids adjusting metered data while California applies a charger-efficiency adjustment to upstream meters (C291). Energy measured at the charger output or on the forklift needs no California adjustment, so one measured basis could serve both states. Oregon explicitly allows a charger as the registered FSE when its data tracking is documented ([[Document - Oregon DEQ Forklift Transition Guidance (2023)]]); California's guidance does not say whether charger-reported data qualifies (C287).
- The accuracy value is not set here. No PosiCharge product's measurement accuracy is evidenced; see [[PosiCharge E-Meter]]. Related: [[Charging Energy Reporting - Provide kWh by Charging Location with Declared Accuracy]].

## Former ids
