---
type: Info
subtype:
id: INFO-00151
uid: 20261002195812543skellyspencer
status: Draft
tags:
  - performance-metric
  - charger
  - comparison
describes:
  - "[[Industrial Battery Charger]]"
  - "[[Identify Battery by Voltage]]"
---

# Metric - Battery Identification Method

## Definition

Battery Identification Method: How the charger identifies the battery: voltage sensing, monitor or ID device, CAN.

## Notes

- **Code and class:** CM08; charger metric. Unit or format: method.
- **Comparability rule:** Voltage sensing cannot identify capacity or type; monitors can.
- **Direction:** richer is better.
- **Values on file (as stated in each product note; n/s means not stated):**
  - [[AMETEK Prestolite Power Eclipse II]]: optional BID: capacity, voltage, type
  - [[AMETEK Prestolite Power ULTRA]]: BID required on opportunity and fast models
  - [[Crown V-HFM3 Charger]]: automatic voltage sensing; optional BMID
  - [[EnerSys Express Charger]]: Wi-iQ: voltage and capacity
  - [[EnerSys NexSys+ Charger]]: Wi-iQ: battery type, voltage and capacity; earlier note: Wi-iQ: battery type and voltage
  - [[Lester Summit Series II]]: automatic voltage detection
  - [[PosiCharge DVS100]]: BMID
  - [[PosiCharge ProCore Edge]]: CAN/Lithium, BMID or Voltage automatic modes
  - [[Power Designers REVOLUTION X]]: PowerTrac recognizes voltage and Ah
- **Source rule:** the product note holds the source URL for each value; this note copies the value for comparison. If they differ, the product note wins and this note is fixed.
- **Gaps and to-do:** 8 product(s) have a value; document-based values to be added as documents are supplied.

## Aliases

- CM08
- Battery Identification Method


## Former ids
