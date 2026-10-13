---
type: Info
subtype:
id: INFO-90009
uid: 20261012225139444skellyspencer
status: Draft
tags:
  - reference-values
  - specifications
  - source-register
  - lead-acid
describes: []
---

# Generic Reference Values

## Definition

Product-agnostic numbers, ranges, rules of thumb and conventions found in supplied manuals, care guides and similar documents, recorded with their basis and source so they can be reused later. Values are as the source states them. None is verified, and none has been adopted into a Metric note.

## Notes

**How to read the tables.** Basis gives the chemistry and conditions the source names. A value marked derived was computed by the note author from a stated value. Source type uses plain descriptors: manufacturer manual, service provider guidance, insurer, regulator, vendor marketing. The last column names the existing Metric note where the value would eventually be merged; it is a plain-text pointer, not a relationship. New sources are added as sections or rows; conflicting values stay side by side.

### Discharge, charging and cycle rules (lead-acid)

| Quantity | Value | Basis and conditions | Source | Source type | Related metric note |
|---|---|---|---|---|---|
| Discharge floor | never below 20% state of charge | forklift lead-acid; a truck lift interrupt is expected to enforce it | Fleetman Consulting care instructions (undated) | service provider guidance | Depth of Discharge Limit |
| Recharge trigger | charge as close to 20% state of charge as possible; do not charge daily for 1 to 2 hours of use a day; avoid charging at breaks well before 20% | lead-acid; argument rests on a fixed number of cycles per battery | Fleetman care instructions | service provider guidance | Opportunity Charging Window; Depth of Discharge Limit |
| Cycle definition | one cycle = a full recharge to 100% after any depth of discharge (30% and 50% count the same) | lead-acid | Fleetman care instructions | service provider guidance | Cycle Life and Warranty |
| Cycle life | about 1,500 cycles for a new battery (an estimate) | lead-acid | Fleetman care instructions | service provider guidance | Cycle Life and Warranty |
| Equalize interval | every 5 to 10 charge cycles ("not more and not less") | lead-acid | Fleetman care instructions | service provider guidance | Equalize Scheduling |
| Idle limit | not more than 1 month without a charge, or it begins to sulfate | lead-acid | Fleetman care instructions | service provider guidance | none yet |

### Water and maintenance (lead-acid)

| Quantity | Value | Basis and conditions | Source | Source type | Related metric note |
|---|---|---|---|---|---|
| Water quality | low mineral content; distilled not required except where water is hard | lead-acid watering | Fleetman care instructions | service provider guidance | Watering Interval |
| Watering timing | after charging, never before | lead-acid watering | Fleetman care instructions | service provider guidance | Watering Interval |
| Fill level | cover the perforated element protector below the cell cap with about 1/4 inch (about 6 mm, derived) of water; do not overfill | lead-acid watering; the source recommends a filling system with an indicator light | Fleetman care instructions | service provider guidance | Electrolyte Level Sensing |
| Cleaning interval | once a year or as required, with a mild baking soda and water mixture kept out of the cells; dry afterwards | lead-acid battery top | Fleetman care instructions | service provider guidance | none yet |

### Charger matching, ventilation and state-of-charge data (qualitative statements)

| Statement | Basis | Source | Source type | Related metric note |
|---|---|---|---|---|
| Battery and charger mismatches in voltage or size occur; with many trucks, use different plugs for different battery sizes and voltages | lead-acid fleets | Fleetman care instructions | service provider guidance | Charger Link |
| Hydrogen is released during normal charging; the charging area should be well ventilated, ideally with high ceilings, and free of flame or spark | lead-acid | Fleetman care instructions | service provider guidance | Charging Gas Emissions |
| Charging decisions need accurate state-of-charge data from the truck; many battery discharge indicators or lift interrupts are miscalibrated or missing, so a technician should check them | lead-acid trucks | Fleetman care instructions | service provider guidance | none yet |

## Former ids
