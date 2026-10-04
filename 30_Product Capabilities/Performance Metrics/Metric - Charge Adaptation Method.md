---
type: Info
subtype:
id: INFO-00266
uid: 20261003203338371skellyspencer
status: Draft
tags:
  - performance-metric
  - charger
  - comparison
describes:
  - "[[Industrial Modular Charger]]"
---

# Metric - Charge Adaptation Method

## Definition

Charge Adaptation Method: how the charger adapts the charge to the battery

## Notes

- **Code and class:** CM20; charger metric. Unit or format: how the charger adapts the charge to the battery.
- **Comparability rule:** Describes what is measured or identified; not a measure of quality.
- **Direction:** not ranked.
- **Values on file (as stated in each product note; n/s means not stated):**
  - [[Fronius Selectiva 4.0]]: effective internal resistance Ri (depends on age, temperature and state of charge); individual curve per charge
  - [[EnerSys IMPAQ Charger]]: HDUTY profile diagnoses battery status or capacity through continuous current loops; settings or a programmed Wi-iQ for capacity, temperature and equalize values
  - [[Crown V-HFM3 Charger]]: identifies the battery on connection and applies the profile for 24 to 96 V; BMID adds temperature compensation and level monitoring
  - [[Delta-Q IC650]]: selected charge profile; temperature compensation on some algorithms with the charger's sensor
  - [[PosiCharge ProCore Edge]]: BMID mode (battery identity and sensors) or voltage mode
- **Source rule:** the product note holds the source URL for each value; this note copies the value for comparison. If they differ, the product note wins and this note is fixed.
- **Gaps and to-do:** Add other chargers; check whether EnerSys NexSys+ adds anything beyond IMPAQ.

## Aliases


## Former ids
