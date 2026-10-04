---
type: Info
subtype:
id: INFO-00272
uid: 20261003220208403skellyspencer
status: Draft
tags:
  - charge-profile
  - cold-storage
  - reference
  - review
describes:
  - "[[Industrial Traction Battery]]"
---

# Cold Storage Charging Rules for Traction Batteries (ZVEI)

## Definition

Rules and formulas for operating and charging PzS (flooded) and PzV (gel) traction batteries at low temperatures, from a ZVEI industry leaflet read in full.

## Notes

- **Source:** ZVEI information leaflet 'Dependencies and rules for operating PzS- and PzV-traction batteries at low temperatures (cold storage house applications)', Working Group Industry Technique, edition August 2009, read in full. Tier: T2 with a note: industry association leaflet, not a manufacturer sheet. <https://www.zvei.org/fileadmin/user_upload/Verband/Fachverbaende/Batterien/Merkblaetter/Industriebatterien/21_e_Traction_Batteries_at_low_temeratures_2009-08.pdf>
- **Capacity:** the nominal capacity is valid at 30 C; at lower temperatures it falls about 0.6 percent per degree between 10 and 30 C, K(t) = K(30 C) x [1 + 0.006 x (temperature - 30 C)]; sulphuric acid viscosity is three times higher going from +30 C to -10 C; an example battery started at +15 C, worked in a -28 C cold store and recharged at +20 C averaged +10 C with 90 percent of capacity available; a thermally insulated tray keeps the temperature higher.
- **Charge voltage:** the gassing voltage rises at low temperatures, so a temperature coefficient of -0.004 V per cell per K is recommended from 0 to 40 C with an IUI characteristic: PzS U = 2.40 V + [-0.004 x (temperature - 30 C)], PzV U = 2.35 V + [-0.004 x (temperature - 30 C)] (and a constant 2.47 V per cell from 0 to -10 C, as printed). Example: a PzS battery charged in winter at 2.48 V per cell at +10 C is overcharged in summer, so a winter and summer switch is advised where charging is not temperature controlled.
- **Chargers:** only regulated IUI chargers with a temperature-controlled charge voltage prevent lack of charge; unregulated W(s)a and W0Wa chargers cause problems at low temperatures; chargers whose cut-off follows main charge time or ampere-hours, with a cold battery, cause lack of charge or acid stratification; with standard parameters a full recharge below 10 C is not possible; a short 5 to 6 hour charge with air agitation or a pulse charge is not possible below 10 C from full discharge.
- **Electrolyte:** nominal density 1.29 kg/L at 30 C; the correction is 0.0007 kg/L per C (a reading of 1.28 kg/L at 15 C corresponds to 1.27 kg/L at 30 C, as the leaflet states); acid of 1.29 kg/L freezes below -70 C, a discharged cell at 1.15 kg/L can freeze at -15 C.
- **Operation:** charging stations and parking should be at room temperature, not below 10 C; do a full recharge before a shift; refill purified water during the gassing phase, near the end of charge, so it mixes with the acid; automatic water refill systems must not be used where the ambient temperature is constantly below 0 C; battery accessories have limit temperatures; a typical battery cools through in 12 to 24 h (the leaflet's examples take a 24 V 3 PzS 375 from +10 C to -10 C in 8 h at -30 C ambient).
- **Related in the vault:** [[Operate in Cold Storage]] (function), [[Toyota Cold Conditioning Package]], [[Metric - Operating Temperature Range]], [[Metric - Charge Temperature Limits]].

## Aliases

- Cold storage charging

## Former ids
