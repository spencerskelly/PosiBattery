---
type: Requirement
subtype: engineering
id: REQ-00052
uid: 20261017124013000skellyspencer
status: Draft
tags:
  - regulatory-driver
  - regulation
  - california
  - candidate-from-research
  - analyst-proposed
  - metering
  - data-export
appliesTo:
  - "[[Industrial Battery Charger]]"
derivedFrom:
  - "[[California LCFS - Forklift Charging Energy Shall Be Metered]]"
  - "[[California LCFS - Facility Owner Registers Charging Locations and Reports as First Reporting Entity]]"
drivenBy:
  - "[[Report Metered Forklift Charging Energy for LCFS Credits]]"
---

# Charging Energy Reporting - Provide kWh by Charging Location with Declared Accuracy

## Definition

A charger, or the software that collects its data, shall provide energy delivered per charging location per reporting quarter, with a declared measurement accuracy basis.

## Notes

- **Proposed from the regulation text; there is no customer or stakeholder source for it.** It stays Draft until a person decides whether it is a requirement. Hypothesis ids H1 to H4 are in [[California Forklift Electrification Regulations Register]].
- Why: owners must report per registered location and use measurement within 5 percent. The accuracy value for any PosiCharge product is not evidenced; [[PosiCharge E-Meter]] is a device that records energy and usage data and its accuracy is not stated in the vault.
- Open: whether charger-reported data qualifies at all (C287, IB-243). The 5 percent target is the obligation's; this requirement states no accuracy value.

## Former ids
