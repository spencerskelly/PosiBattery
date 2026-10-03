---
type: Info
subtype:
id: INFO-00141
uid: 20261002195812533skellyspencer
status: Draft
tags:
  - battery
  - charger
  - comparison
  - monitor
  - performance-metric
describes:
  - "[[Battery Monitoring and Identification Device]]"
  - "[[Industrial Battery Charger]]"
  - "[[Industrial Traction Battery]]"
---

# Metric - Size and Mass

## Definition

Size and Mass: shared metric used for monitors, chargers, batterys.

## Notes

- **Code and class:** MM13, CM13, BM11 (monitor, charger, battery metrics merged by the note re-use rule). Unit or format: mm; g; in or mm; lb or kg; mm; kg.
- **Definition by class:**
  - monitor (MM13): Size and Mass: Housing dimensions and mass.
  - charger (CM13): Size and Weight: Cabinet dimensions and weight.
  - battery (BM11): Size and Mass: Dimensions and mass (often DIN or BCI sizes).
- **Comparability rules by class:**
  - monitor (MM13): Convert in to mm (x 25.4); note multi-part housings.
  - charger (CM13): State configuration (module count).
  - battery (BM11): Fit to truck compartment matters more than raw size.
- **Direction:** smaller is better.
- **Values on file (as stated in each product note; n/s means not stated):**
  - [[ACT Quantum 2]]: Q4 16 x 16 x 24 in; Q6 24 x 16 x 24; Q12 24 x 16 x 36; 53-181 lb
  - [[ACT Quantum 3]]: 14.25 x 17 x 21.25 in; Q4 62 lb, Q8 124 lb
  - [[Advanced Charging Technologies BATTview]]: 5.5 x 1.75 x 1.0 in (140 x 44 x 25 mm)
  - [[Crown V-HFM3 Charger]]: FS3 12 x 9.5 x 14.5 in, up to 37.4 lb; FS4 and FS6 12 x 18.5 x 14.5 in, up to 71.5 lb
  - [[Deka PowerForce Charger]]: 14 x 14 x 16 in
  - [[Delta-Q IC650]]: 252 x 186 x 80 mm; 2.4 kg
  - [[EnerSys Wi-iQ]]: 40.07 x 19.5 x 107.97 mm
  - [[HOPPECKE trak collect]]: base 120 x 52 x 26 mm plus satellite 82 x 50 x 32 mm; 340 g
  - [[Lester Summit Series II]]: 13.438 x 8.188 x 4.531 in (341 x 208 x 115 mm); 13.4 lb (6.09 kg)
  - [[Philadelphia Scientific eGO!core]]: 100 x 30 x 18 mm; 100 g flooded, 80 g VRLA
  - [[Philadelphia Scientific eGO!pro]]: 235 g flooded; 212 g VRLA
  - [[PosiCharge Battery Rx]]: 7.63 x 2.25 x 1.25 in (194 x 57 x 32 mm)
  - [[PosiCharge PosiGuard]]: 4.05 x 1.80 x 1.00 in (103 x 46 x 25 mm)
  - [[Power Designers PowerTrac 3]]: 4.25 x 1.5 x 0.6 in (108 x 38 x 15 mm)
  - [[Power Designers PowerTrac DT3]]: 4.25 x 1.5 x 0.6 in (108 x 38 x 15 mm)
  - [[Stryten EHF Charger]]: cabinets G1 55 lb and G2 142 lb; EHY2 19.9 x 17.4 x 35.5 in
- **Source rule:** the product note holds the source URL for each value; this note copies the value for comparison.
- **Gaps and to-do:** values come from documents as they are absorbed.

## Aliases

- MM13
- CM13
- BM11
- Size and Mass
- Size and Weight


## Former ids
- INFO-00156 (Charger Metric - Size and Weight)
- INFO-00169 (Battery Metric - Size and Mass)
