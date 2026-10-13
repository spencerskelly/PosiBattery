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

### Lead-acid forklift battery size, capacity and weight (Fleetman selection chart)

Source: Fleetman Consulting Inc., "Forklift Battery Selection Chart" (undated, one page, no battery brand named; service provider catalog). 42 rows, all reproduced below as stated. Tray dimensions are steel tray length x width x height in inches; weights are approximate pounds. The discharge rate behind the Ah figures is not stated on the chart.

**Conventions confirmed on all 42 rows (derived by the note author):**

- Voltage = 2 V x cell count (the first number of the model code is the cell count; 6 cells = 12 V, 18 = 36 V, 24 = 48 V, 40 = 80 V).
- Ah = the middle number x the number of positive plates, where positive plates = (total plates - 1) / 2. The middle number is therefore Ah per positive plate, and the last number is the total plate count. Example: 18-85-17 has 8 positive plates, 8 x 85 = 680 Ah, as listed. This holds for every row.
- kWh = cells x Ah x about 1.94 V (1.940 to 1.941 V per cell across all rows), so the chart's kWh uses an average of about 1.94 V per cell, not the 2 V nominal.
- Specific weight is 80.2 to 97.0 lb per kWh across all rows (median 85.7), derived from the stated weight and kWh. That is about 36 to 44 kg per kWh.

**Summary by voltage (derived from the rows below):**

| Voltage | Rows | Ah range | kWh range | Weight range (lb) | lb per kWh | Tray height range (in) |
|---|---|---|---|---|---|---|
| 12 V | 1 | 510 | 5.94 | 522 | 87.9 | 23.3 |
| 24 V | 11 | 255 to 1,125 | 5.94 to 26.19 | 576 to 2,364 | 83.7 to 97 | 23.25 to 31.13 |
| 36 V | 13 | 625 to 1,105 | 21.83 to 38.59 | 1,890 to 3,096 | 80.2 to 86.6 | 22.62 to 30.56 |
| 48 V | 8 | 510 to 850 | 23.75 to 39.58 | 2,088 to 3,288 | 83.1 to 91.8 | 22.62 to 30.5 |
| 80 V | 9 | 425 to 750 | 32.98 to 58.2 | 2,920 to 4,960 | 85.2 to 89.7 | 23.68 to 33.13 |

**All rows as stated:**

| Voltage | Model code | Ah | kWh | Tray L x W x H (in) | Approx. weight (lb) |
|---|---|---|---|---|---|
| 12 V | 6-85-13 | 510 | 5.94 | 30.62 x 7.68 x 23.3 | 522 |
| 24 V | 12-85-7 | 255 | 5.94 | 25.25 x 8.5 x 23.25 | 576 |
| 24 V | 12-85-7 | 255 | 5.94 | 33.63 x 6.56 x 23.25 | 576 |
| 24 V | 12-85-13 | 510 | 11.87 | 30.5 x 12.63 x 23.25 | 1,044 |
| 24 V | 12-85-15 | 595 | 13.85 | 35 x 12.75 x 23.25 | 1,188 |
| 24 V | 12-100-13 | 600 | 13.97 | 30.5 x 12.63 x 26.25 | 1,236 |
| 24 V | 12-125-13 | 750 | 17.46 | 30.63 x 12.63 x 31.13 | 1,488 |
| 24 V | 12-125-13 | 750 | 17.46 | 35.63 x 11.56 x 30.5 | 1,488 |
| 24 V | 12-125-15 | 875 | 20.37 | 35 x 12.88 x 30.5 | 1,704 |
| 24 V | 12-125-15 | 875 | 20.37 | 36 x 14 x 30.5 | 1,704 |
| 24 V | 12-125-19 | 1,125 | 26.19 | 38.36 x 14.95 x 30.88 | 2,364 |
| 24 V | 12-170-11 | 850 | 19.79 | 35.12 x 13.25 x 30.5 | 1,728 |
| 36 V | 18-85-17 | 680 | 23.75 | 31.75 x 26.38 x 22.62 | 2,034 |
| 36 V | 18-85-17 | 680 | 23.75 | 33 x 25.38 x 22.62 | 2,034 |
| 36 V | 18-85-17 | 680 | 23.75 | 38 x 19.87 x 22.62 | 2,034 |
| 36 V | 18-85-19 | 765 | 26.71 | 38.13 x 22.25 x 22.62 | 2,250 |
| 36 V | 18-85-21 | 850 | 29.68 | 38.13 x 24.5 x 22.63 | 2,466 |
| 36 V | 18-85-23 | 935 | 32.65 | 38.25 x 26.87 x 22.62 | 2,682 |
| 36 V | 18-85-25 | 1,020 | 35.62 | 38.44 x 29.39 x 22.81 | 2,953 |
| 36 V | 18-85-27 | 1,105 | 38.59 | 38.13 x 31.38 x 22.63 | 3,096 |
| 36 V | 18-100-17 | 800 | 27.94 | 38.13 x 20 x 25.63 | 2,412 |
| 36 V | 18-125-11 | 625 | 21.83 | 38.08 x 13.37 x 30.56 | 1,890 |
| 36 V | 18-125-13 | 750 | 26.19 | 37.88 x 15.56 x 30.5 | 2,232 |
| 36 V | 18-125-15 | 875 | 30.56 | 38.25 x 17.81 x 30.5 | 2,556 |
| 36 V | 18-125-17 | 1,000 | 34.92 | 38.13 x 20 x 30.5 | 2,916 |
| 48 V | 24-85-13 | 510 | 23.75 | 30.63 x 25.25 x 22.63 | 2,088 |
| 48 V | 24-85-15 | 595 | 27.7 | 38.33 x 23.75 x 22.75 | 2,431 |
| 48 V | 24-85-17 | 680 | 31.66 | 38.13 x 26.5 x 22.62 | 2,712 |
| 48 V | 24-85-17 | 680 | 31.66 | 38.25 x 26.63 x 23.25 | 2,712 |
| 48 V | 24-85-19 | 765 | 35.62 | 38.13 x 29.5 x 22.63 | 3,000 |
| 48 V | 24-85-21 | 850 | 39.58 | 38.13 x 32.63 x 22.63 | 3,288 |
| 48 V | 24-100-13 | 600 | 27.94 | 30.5 x 25.25 x 25.63 | 2,472 |
| 48 V | 24-125-13 | 750 | 34.92 | 44 x 20.5 x 30.5 | 3,206 |
| 80 V | 40-85-11 | 425 | 32.98 | 45.63 x 26.38 x 23.68 | 2,920 |
| 80 V | 40-125-9 | 500 | 38.8 | 40.13 x 27.69 x 30.5 | 3,480 |
| 80 V | 40-125-9 | 500 | 38.8 | 63.38 x 14.85 x 33.13 | 3,480 |
| 80 V | 40-125-11 | 625 | 48.5 | 40 x 33 x 30.87 | 4,347 |
| 80 V | 40-125-11 | 625 | 48.5 | 40.23 x 28.08 x 30.81 | 4,200 |
| 80 V | 40-125-11 | 625 | 48.5 | 40.38 x 33.53 x 30.56 | 4,200 |
| 80 V | 40-125-11 | 625 | 48.5 | 55.69 x 24.43 x 30.81 | 4,200 |
| 80 V | 40-125-13 | 750 | 58.2 | 40 x 39 x 30.56 | 4,960 |
| 80 V | 40-125-13 | 750 | 58.2 | 40.57 x 32.37 x 30.56 | 4,960 |

Notes: some codes repeat with different tray sizes or weights (12-85-7 at 24 V appears twice with weight 576 lb for both trays, and 80 V 40-125-11 appears four times at 4,200 to 4,347 lb), so the same capacity is sold in several footprints. Metric note this would merge into: Size and Mass; Capacity; Nominal Voltage Range; Chemistry and Plate Construction.

## Former ids
