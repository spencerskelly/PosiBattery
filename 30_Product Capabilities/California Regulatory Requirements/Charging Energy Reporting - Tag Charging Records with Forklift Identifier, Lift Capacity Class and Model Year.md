---
type: Requirement
subtype: engineering
id: REQ-00063
uid: 20261017153005000skellyspencer
status: Draft
tags:
  - regulatory-driver
  - regulation
  - candidate-from-research
  - analyst-proposed
  - california
  - oregon
appliesTo:
  - "[[Industrial Battery Charger]]"
derivedFrom:
  - "[[California LCFS - Forklift Volumes Are Reported by Lift Capacity Class]]"
  - "[[California LCFS - Rental Forklift Charging Locations Are Registered and Movements Recorded]]"
drivenBy:
  - "[[Report Metered Forklift Charging Energy for LCFS Credits]]"
  - "[[Report Metered Forklift Charging Energy for Oregon, Washington or New Mexico Credits]]"
---

# Charging Energy Reporting - Tag Charging Records with Forklift Identifier, Lift Capacity Class and Model Year

## Definition

Each charging record, or the system that stores it, shall carry the forklift identifier (where one is entered), its lift capacity class (under or over 12,000 lb) and its model year, so that energy can be reported by class and, where a program asks, by model year.

## Notes

- **Proposed from regulation text; no customer or stakeholder source.** It stays Draft until a person decides whether it is a requirement.
- Why (analyst reasoning): California credits depend on the class, and without it all volume falls in the lowest class. Oregon's estimation report separated forklifts made before 2016 from later ones by model year ([[Document - Oregon DEQ Electric Forklift Estimation Methodology Memo (2023-06-09)]]); whether that split still applies to metered reports is not confirmed (IB-264).
- A charger sees a battery, not a truck; the forklift link must come from the operator or from a connected telematics source. Which PosiCharge products carry a truck identifier is not evidenced (see [[PosiCharge PosiLink]] and [[PosiCharge E-Meter]]).
- Related: [[Charging Energy Reporting - Provide kWh by Charging Location with Declared Accuracy]].

## Former ids
