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
  - vrla-gel
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

### East Penn / Deka Industrial Battery Service Manual 0656 (flooded and gel lead-acid)

Source: East Penn Industrial Battery Service Manual 0656 (2019 PDF, 40 pp), East Penn Manufacturing, Lyon Station, PA. Manufacturer manual (T1). The PDF is the file `0656-Service-Manual.pdf` supplied in the repo `Downloads` folder; a public URL for this exact manual was not confirmed (the East Penn site hosts sibling manuals such as [D-Series IO Manual 0628](https://www.eastpennmanufacturing.com/wp-content/uploads/D-Series-IO-Manual-0628.pdf)). Page numbers below are the manual's own. The manual covers Deka D, M, P (Max Powr), H and DL/DLU flooded series and G-series gel. It points to "P.23 for full warranty information" but page 23 carries no warranty text. Values are as stated; conflicts with other sources are listed in the conflict section at the end of this note and in the landscape conflicts register (C118 to C127).

#### Rating basis and construction conventions (flooded)

| Quantity | Value | Basis and conditions | Page | Related metric note |
|---|---|---|---|---|
| Capacity rating basis | ampere-hours at the 6-hour rate to 1.70 V per cell, electrolyte at 77 F (25 C), full-charge specific gravity at nameplate rating | flooded; "normal" discharge is any rate between 3 and 8 hours (glossary) | 5, 19, glossary | Capacity |
| Cell voltage | about 2 V open circuit; 2.12 to 2.70 V while charging; 36 V truck = 18 cells | flooded | 4 | Nominal Voltage Range |
| Positive plate rating | a D100 positive plate delivers 16.66 A for 6 h = 100 Ah to 1.70 V; positive plates = (total plates - 1) / 2; 13 plates = 6 positive = 600 Ah | flooded D-series; D75 or D125 plates scale the rating down or up | 5 | Chemistry and Plate Construction; Capacity |
| Energy | 100 A x 6 h x 1.930 average volts per cell = 1.158 kWh per cell; an 18-cell 600 Ah battery = 20.84 kWh | flooded, 6-hour rate | 5 | Capacity |
| Battery weight | the average lift truck battery weighs more than 2,000 lb; service weight is stamped on the tray near a lifting hole and must fall within the truck nameplate range because the battery counterweights the load | flooded and gel | 9, 25 | Size and Mass |
| Compartment clearance | block or clip clearance must not exceed 1/2 inch (about 13 mm, derived); the battery must not be wedged tight | installation | 12 | Size and Mass |
| Electrolyte acid content | specific gravity 1.280 = 37.40% acid by weight; 1.290 = 38.55%; 1.325 = 42.50%; 1.400 = 50.5% | flooded | 9, 20 | Full-Charge Specific Gravity |

#### Specific gravity (flooded)

| Quantity | Value | Basis and conditions | Page | Related metric note |
|---|---|---|---|---|
| Full-charge specific gravity, range (Table 1-1) | D 1.280 to 1.295; M 1.245 to 1.255; P (Max Powr) 1.320 to 1.330; DL/DLU 1.245 to 1.255; H 1.295 to 1.305 | at 77 F (25 C); the M range is printed "1-255" for the upper limit and is read here as 1.255 | 4 | Full-Charge Specific Gravity |
| Recommended specific gravity (Table 4-1) | D 1.290; H 1.300; M 1.250; P 1.325; DL/DLU 1.250 | at 77 F, fully charged, electrolyte at the bottom of the vent well, on charge at the finish rate or less | 20 | Full-Charge Specific Gravity |
| Temperature correction | add 0.004 per 10 F above 77 F and subtract 0.004 per 10 F below; Table 3-1 gives +0.016 specific gravity and +0.13 V per cell at 115 F and -0.010 and -0.08 V at 52 F | rule of thumb plus table | 14 | Temperature Compensation Source |
| Depth-of-discharge indication | specific gravity falls in proportion to ampere-hours removed; example 1.290 full to 1.140 is a 150-point drop, so 1.190 = 67% discharged; discharged cells approach 1.100; wait at least 1 hour after discharge for a true reading | flooded, corrected to 77 F | 5 | Depth of Discharge Limit |
| Cell-to-cell spread | more than 0.020 between any two cells means equalize; a reading 0.020 above or below nominal 1.290, an on-charge cell voltage range above 0.15 V, or an open-circuit cell voltage more than 0.03 V below the battery average can signal cell failure | flooded | 14, 16, 17 | Voltage Measurement |
| Storage self-discharge | specific gravity lost per day on open circuit: 0.004 at 120 F, 0.003 at 100 F, 0.001 at 80 F, 0.0005 at 50 F | new batteries in storage | 12 | none yet |
| Specific gravity adjustment | 1.400 acid raises it, water lowers it; about 1/4 to 1/2 inch of electrolyte removed per 5 points of change (rough, varies with cell height); charge 1/2 to 1 hour after adding acid | flooded, on charge at the finish rate | 20 | none yet |

#### Discharge, charging and cycle rules (flooded)

| Quantity | Value | Basis and conditions | Page | Related metric note |
|---|---|---|---|---|
| Discharge floor | limit discharge to 80% of rated capacity (20% remaining) for optimum life; frequent over-discharge shortens life drastically | flooded | 13 | Depth of Discharge Limit |
| Cycle life | an average battery lasts 1,500 to 1,800 cycles, or 5 to 6 years; one cycle = a discharge and its recharge | flooded; actual life depends on type, severity of use and maintenance | 13, glossary | Cycle Life and Warranty |
| Repair or replace | repair at 1 to 2 years (300 to 600 cycles) if repair cost is under 25% of replacement; replace at 3 or more years (900 or more cycles) or repairs of 25% or more | flooded | 27 | Cycle Life and Warranty |
| Capacity versus temperature | 100% of rated capacity at 77 F (25 C) but only 65% at 32 F (0 C) | flooded | 13 | Operating Temperature Range |
| Operating and charging temperature | operate at 115 F (46 C) or lower; charging rate is any rate that does not exceed 115 F (46 C) or cause excessive gassing; place a battery on charge below 90 F (32 C) | flooded | 13, 21 | Charge Temperature Limits |
| Starting rate | not more than 20 A per 100 Ah of rated capacity; glossary defines starting rate as the current that avoids gassing or cell temperature above 110 F (43 C) | flooded, automatic charger | 13, glossary | Maximum Continuous Charge Current |
| Gassing voltage and finish rate | gassing voltage 2.37 V per cell at 77 F held until current tapers to 5 A per 100 Ah; finish rate not less than 5 A per 100 Ah at 2.60 V per cell; East Penn finish rate = 5% of the 6-hour ampere-hours (D100-13 600 Ah = 30 A), printed on the nameplate (8-hour basis for diesel types) | flooded | 14, 20 | Charge Rate Taper; Constant Voltage Setpoint |
| Standard recharge | based on an 8-hour charging cycle; a fully charged battery shows stable voltage, free gassing, current leveled at the finish rate and specific gravity no longer rising | flooded | 14 | Charge End Criterion; Charge Time |
| Equalize | a 3-hour continuation of the standard recharge at no more than the finish rate, at least 3 A per 100 Ah; also described as 3 or 4 hours until four readings 1/2 hour apart are constant; "equalize once each week" as a rule of thumb and "weekly maintenance schedule" | flooded | 14, 13, 20 | Equalize Scheduling; Equalizing Charge Rule |
| Freshening and storage | give a new battery a freshening charge; a stored battery can be held fully charged for up to a year but needs a freshening charge when specific gravity falls below 1.240 or every 6 weeks; check specific gravity monthly above 68 F (20 C) and at least every 2 months below | flooded | 12, 13 | none yet |
| Charge-gas limit | ventilation is satisfactory if hydrogen does not exceed 2% in any location; above 4% is explosive | flooded charging area | 10 | Charging Gas Emissions |
| Partial charging | "Recharge FULLY after each duty cycle. Avoid partial recharging." The manual does not mention opportunity charging | flooded | 23 | Opportunity Charging Window |

#### Water, cleaning and testing (flooded)

| Quantity | Value | Basis and conditions | Page | Related metric note |
|---|---|---|---|---|
| Water purity | NEMA maximums: total solids 350 ppm, chlorides 25 ppm, nitrates 10 ppm, iron 4 ppm; use distilled or de-ionized water where local water is unsuitable; tap water is unsuitable at any time in some areas | flooded watering | 18 | Watering Interval |
| Electrolyte level limits | low limit = top of the perforated separator protector; high limit = bottom of the vent well opening; "Add approved water to 1/4 inch below vent well only at the end of charge" | flooded; the specific gravity spec is set at the high level | 18, 23, 30 | Electrolyte Level Sensing |
| Watering timing | page 18: only while on charge and gassing or as soon after recharge as possible; page 23: only at the end of charge, never before charging; page 21: if the level is low, add water to just cover the separator protector while discharged | flooded | 18, 21, 23 | Watering Interval |
| Level check frequency | weekly | flooded | 23 | Watering Interval |
| Cleaning | about once a month on average, more often in dust; non-corrosive water-based cleaner with no hazardous ingredients; some products labeled "battery cleaner" are to be avoided | flooded battery top | 18, 11 | none yet |
| Capacity test | discharge a fully charged, equalized battery at the 6-hour rate (rated Ah / 6) to 1.70 V per cell; capacity % = minutes to final voltage / 360 x 100 (336 min = 93%); at least 80% (288 min) can return to service, over 90% after sulfation treatment | flooded | 19 | Capacity |
| Sulfation treatment | charge at the finish rate until specific gravity is unchanged for 3 hours (hourly readings); stop and cool to 90 F (32 C) or lower if temperature passes 115 F (46 C); repeat after a full discharge | flooded | 19 | none yet |
| Element air exposure | do not expose a pulled element to air for more than 5 minutes | repair | 29 | none yet |

#### Valve-regulated gel (G-series)

| Quantity | Value | Basis and conditions | Page | Related metric note |
|---|---|---|---|---|
| Charger end-of-charge limit | limit voltage to 2.55 V per cell at 77 F +/- 2 F; compensate -10 mV per cell per 3 F (from the curve legend) | gel; only the supplied or East Penn-approved charger; warranty void otherwise | 24 | Constant Voltage Setpoint; Temperature Compensation Source |
| Charge curve values (Deka Dominator curve) | Vgas 2.33 V per cell; start 16.3 A per 100 Ah; finish 1.5 A per 100 Ah; the 80% stage begins when current falls below 8.2 A per 100 Ah | gel | 24 | Charge Rate Taper |
| Charger types barred | constant-current and ferroresonant charges "should NEVER be used" | gel | 24 | Charge Profile Types Offered |
| Open-circuit voltage vs state of charge | 100% = 2.15 to 2.18 V; 75% = 2.12; 50% = 2.07; 25% = 2.01; 0% = 1.97; measure no earlier than 4 hours after charge | gel, per cell | 25 | Voltage Measurement |
| Freshening and equalize | freshening charge if voltage falls below 2.14 V or at least every 6 weeks; equalize every 1 to 4 weeks depending on service | gel | 25, 26 | Equalize Scheduling |
| Design life | water loss kept low enough for a service life of five years or more | gel | 24 | Cycle Life and Warranty |
| Capacity ratings by plate count | G45: 9 to 19 plates = 180 to 405 Ah; G75: 5 to 33 plates = 150 to 1,200 Ah; G105: 11 to 17 plates = 525 to 840 Ah (6-hour rate) | gel; Ah = ((plates - 1) / 2) x type number, which holds for every listed entry | 26 | Capacity |

#### Conflicts raised by East Penn 0656 (side by side)

These entries are also in the landscape conflicts register as C118 to C127. Nothing here is resolved.

| # | Topic | East Penn 0656 | Other source | Status |
|---|---|---|---|---|
| C118 | Flooded equalize interval | weekly rule of thumb (p13, p14); trigger at 0.020 specific gravity spread | East Penn D-Series IO manual 0628 and Max Powr IO manual 0608, as recorded in the vault from search snippets: every one to four weeks; Fleetman: every 5 to 10 cycles; EnerSys IMPAQ, NexSys+ and PosiCharge ProCore Edge: weekly. In 0656 the one-to-four-week wording appears in the gel section | open; 0628 and 0608 not yet read in full |
| C119 | Watering timing | p18 allows watering while on charge and gassing or right after; p23 says only at the end of charge; p21 says add enough water to just cover the protector while discharged | Fleetman: after charging, never before. An earlier summary in this project stated that East Penn says "after charging, never before"; that overstated it | open; the manual disagrees with itself |
| C120 | Fill level reference | high limit at the bottom of the vent well (p18); 1/4 inch below the vent well at end of charge (p23, p30) | Fleetman: about 1/4 inch of water above the perforated element protector | open; different datums, equivalence depends on cell design |
| C121 | Cleaning interval and agent | about monthly; non-corrosive water-based cleaner; warns against some "battery cleaner" products | Fleetman: once a year or as required, mild baking soda and water | open |
| C122 | Cycle life | 1,500 to 1,800 cycles or 5 to 6 years | Fleetman: about 1,500 cycles | open; ranges overlap |
| C123 | Charge temperature limit | 115 F (46 C) on p13 and p21; p16 prints "115 F (25 C)"; glossary starting rate uses 110 F (43 C) | vault note Metric - Charge Temperature Limits says Deka's 115 F is for photovoltaic use, a different application; 0656 states 115 F for industrial motive power | open; the p16 value is read as a misprint |
| C124 | Max Powr full-charge specific gravity | Table 1-1: 1.320 to 1.330; Table 4-1: P prefix 1.325 | Max Powr IO manual 0608 (snippet in vault): 1.310 to 1.330 | open; three statements from one maker |
| C125 | Specific gravity spread wording | p16 prints "20 points (0.20)"; every other place says 0.020 | none | recorded as 0.020; misprint |
| C126 | Opportunity and partial charging | "Avoid partial recharging" (p23); no opportunity window given; standard recharge based on 8 hours | Western Materials (dealer, T3): D-Series is designed for conventional and opportunity charging; RICO allows opportunity charging with a specialized charger | open |
| C127 | Energy basis | average 1.930 V per cell at the 6-hour rate (p5) | Fleetman chart kWh implies about 1.94 V per cell and does not state the discharge rate | open; small difference, basis of the chart's Ah unconfirmed |

## Former ids
