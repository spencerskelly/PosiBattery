---
type: Info
subtype:
id: INFO-00152
uid: 20261002195812544skellyspencer
status: Draft
tags:
  - performance-metric
  - charger
  - comparison
describes:
  - "[[Industrial Battery Charger]]"
  - "[[Compensate Charge for Battery Temperature]]"
---

# Charger Metric - Temperature Compensation Source

## Definition

Temperature Compensation Source: What supplies battery temperature for compensation.

## Notes

- **Code and class:** CM09; charger metric. Unit or format: device.
- **Comparability rule:** Immersed sensor, cell-top module and ambient probe give different readings.
- **Direction:** n/a.
- **Values on file (as stated in each product note; n/s means not stated):**
  - [[AMETEK Prestolite Power Eclipse II]]: intelligent monitoring; BID
  - [[AMETEK Prestolite Power ULTRA]]: BID, 32-158 F
  - [[Crown V-HFM3 Charger]]: BMID (optional)
  - [[EnerSys Express Charger]]: Active Temperature/Output Management; Wi-iQ
  - [[EnerSys NexSys+ Charger]]: Wi-iQ when configured correctly; earlier note: Wi-iQ
  - [[Fronius Selectiva 4.0]]: TagID
  - [[HOPPECKE trak charger HF premium]]: trak | collect
  - [[Lester Summit Series II]]: battery temperature connector (QD terminal block); earlier note: battery temperature input; sensor optional
  - [[PosiCharge DVS100]]: electrolytic thermistor and BMID
  - [[PosiCharge ProCore Edge]]: BMID
  - [[Stryten EHI Charger]]: battery temperature as data over power line
  - [[Stryten X-7 Charger]]: inCOMMAND-linked battery temperature; charger adjusts rate
- **Source rule:** the product note holds the source URL for each value; this note copies the value for comparison. If they differ, the product note wins and this note is fixed.
- **Gaps and to-do:** 9 product(s) have a value; document-based values to be added as documents are supplied.

## Aliases

- CM09
- Temperature Compensation Source

## Former ids
