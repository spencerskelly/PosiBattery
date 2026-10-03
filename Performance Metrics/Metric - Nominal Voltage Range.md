---
type: Info
subtype:
id: INFO-00129
uid: 20261002195812521skellyspencer
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
  - "[[Multi-Voltage Output]]"
  - "[[Industrial Traction Battery]]"
---

# Metric - Nominal Voltage Range

## Definition

Nominal Voltage Range: shared metric used for monitors, chargers, batterys.

## Notes

- **Code and class:** MM01, CM01, BM02 (monitor, charger, battery metrics merged by the note re-use rule). Unit or format: V.
- **Definition by class:**
  - monitor (MM01): Nominal Battery Voltage Range: Battery voltage range the monitor is specified for.
  - charger (CM01): Battery Voltage Range: Battery nominal voltages the charger covers.
  - battery (BM02): Nominal Voltage: Nominal pack voltage.
- **Comparability rules by class:**
  - monitor (MM01): Record nominal, operating and supply voltage separately; they are not the same number.
  - charger (CM01): Multi-voltage via automatic sensing differs from fixed models per voltage.
  - battery (BM02): Cell count by voltage differs for lead-acid and lithium.
- **Direction:** wider is better.
- **Values on file (as stated in each product note; n/s means not stated):**
  - [[ACT Quantum 2]]: 24-96 V (sheet); earlier note: 24-96 V
  - [[ACT Quantum 3]]: 24-120 V (sheet); earlier note: 24-120 V
  - [[ACT Quantum Outdoor]]: 24-96 V
  - [[Advanced Charging Technologies BATTview]]: 12-80 V nominal; operating 12-110 V
  - [[Crown V-HFM3 Charger]]: 24, 36, 48, 72, 80, 96 V
  - [[Delta-Q IC650]]: 24, 36, 48 V
  - [[EnerSys Wi-iQ]]: 24-80 V and 96-120 V (nominal and operating)
  - [[EnerSys iQ Mini]]: 12-80 V (carried from seed)
  - [[Exide Motion+ EasyMonitor]]: 18-120 V
  - [[Flow-Rite Eagle Eye Essential IV]]: 4-12 V DC supply
  - [[Flux Power GSE Pack]]: 72 V
  - [[Flux Power LiFT Pack]]: 24 V (first unit)
  - [[Fronius Selectiva 4.0]]: 96 V and 120 V models on the flyer; 2-30 kW classes overall
  - [[Green Cubes GSE Lithium Battery]]: 80 V (FBP-1000)
  - [[Green Cubes SAFEFlex Battery]]: 48 V (FBP-1000)
  - [[Green Cubes SAFEFlex PLUS Battery]]: 24, 36, 48, 80 V
  - [[HOPPECKE trak collect]]: supply 17-150 VDC
  - [[Inventus Smart Battery Monitor SBM-01]]: 9-60 VDC supply
  - [[Lester Summit Series II]]: 24, 36, 48 V nominal; 36/54/72 V maximum (1425 W sheet); earlier note: 24, 36, 48 V
  - [[Philadelphia Scientific eGO!core]]: 12 V
  - [[Philadelphia Scientific eGO!plus]]: 24-80 V (12, 72, 120 V optional)
  - [[Philadelphia Scientific eGO!pro]]: 24-80 V (12, 72, 120 V optional)
  - [[PosiCharge Battery Rx]]: 24-96 V (vendor page)
  - [[PosiCharge DVS100]]: 24-80 V
  - [[PosiCharge DVS300 Series]]: 24-96 V (sheet)
  - [[PosiCharge MVS400 and MVS800]]: 24-96 V (sheets)
  - [[PosiCharge PosiGuard]]: 24-96 V nominal; operating 18-120 V
  - [[PosiCharge ProCore Edge]]: 24-96 V
  - [[PosiCharge SVS100]]: 24-80 V (sheet)
  - [[PosiCharge SVS200]]: 24-96 V
  - [[Power Designers PowerTrac 3]]: 24-84 V nominal; operating 18-120 V (sheet)
  - [[Power Designers PowerTrac DT3]]: 24-84 V nominal; operating 18-120 V
  - [[Power Designers PowerTrac SP+]]: 12-84 V nominal
  - [[Power Designers REVOLUTION X]]: multi-voltage modules; with PowerTrac 24/36/48 recognition
  - [[Stryten EHF Charger]]: 24 V and 36 V models (more in the brochure)
  - [[Stryten EHY Charger]]: nominal 24, 36, 48, 72, 80 VDC
  - [[Stryten M-Series AGM220 Battery]]: 24 V (four 6 V AGM210)
  - [[Stryten X-3 Charger]]: 24 V modules; multi-voltage 24/36/48 V; 72/80 V (brochure); earlier note: 24, 36, 48 V (3-bay to 10-bay)
  - [[Stryten X-7 Charger]]: up to 96 V (72-96 V range added)
- **Source rule:** the product note holds the source URL for each value; this note copies the value for comparison.
- **Gaps and to-do:** values come from documents as they are absorbed.

## Aliases

- MM01
- CM01
- BM02
- Nominal Battery Voltage Range
- Battery Voltage Range
- Nominal Voltage


## Former ids
- INFO-00144 (Charger Metric - Battery Voltage Range)
- INFO-00160 (Battery Metric - Nominal Voltage)
