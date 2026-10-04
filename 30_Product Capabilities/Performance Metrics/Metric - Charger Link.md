---
type: Info
subtype:
id: INFO-00138
uid: 20261002195812530skellyspencer
status: Draft
tags:
  - performance-metric
  - monitor
  - comparison
describes:
  - "[[Battery Monitoring and Identification Device]]"
  - "[[Identify Battery to Charger]]"
  - "[[Report Battery Temperature to Charger]]"
  - "[[Communicate with Charger]]"
---

# Metric - Charger Link

## Definition

Charger Link: What the monitor exchanges with a charger: identity, profile, temperature, level.

## Notes

- **Code and class:** MM10; monitor metric. Unit or format: what is exchanged.
- **Comparability rule:** List the data items; a charger that identifies by voltage alone has no monitor link.
- **Direction:** more items is richer.
- **Values on file (as stated in each product note; n/s means not stated):**
  - [[AMETEK Prestolite Power BID]]: ID numbers, voltages, Ah sizes, start rates, construction types; voltage, temperature and Ah usage on demand; earlier note: ID, type, Ah, cell count, start rate; temperature
  - [[AMETEK Prestolite Power TruBid]]: works with charger to end charge; wireless download
  - [[Crown V-Force BMID]]: voltage and temperature; adjusts charge rate; watering needs
  - [[EnerSys Wi-iQ]]: battery type, voltage and capacity to NexSys+ (Express: voltage and capacity); temperature compensation (C50); earlier note: battery type and voltage to NexSys+; temperature compensation; Zigbee
  - [[Fronius TagID]]: temperature to Selectiva 4.0
  - [[HOPPECKE trak collect]]: communicates with charger; temperature-controlled charging
  - [[PosiCharge BMID]]: identity, profile, temperature, charge-event history to PosiCharge chargers
  - [[Power Designers PowerTrac 3]]: voltage and Ah capacity to REVOLUTION
- **Source rule:** the product note holds the source URL for each value; this note copies the value for comparison. If they differ, the product note wins and this note is fixed.
- **Gaps and to-do:** 8 product(s) have a value; document-based values to be added as documents are supplied.

## Aliases

- MM10
- Charger Link


## Former ids
