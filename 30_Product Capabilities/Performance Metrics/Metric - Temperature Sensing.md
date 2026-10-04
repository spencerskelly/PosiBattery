---
type: Info
subtype:
id: INFO-00133
uid: 20261002195812525skellyspencer
status: Draft
tags:
  - performance-metric
  - monitor
  - comparison
describes:
  - "[[Battery Monitoring and Identification Device]]"
  - "[[Measure Battery Temperature]]"
  - "[[Electrolyte-Immersed Temperature Sensor]]"
---

# Metric - Temperature Sensing

## Definition

Temperature Sensing: Where and how battery temperature is sensed.

## Notes

- **Code and class:** MM05; monitor metric. Unit or format: sensor type; C range; resolution.
- **Comparability rule:** Electrolyte-immersed, cell-top, cable and ambient sensors give different readings; say which.
- **Direction:** immersed is closer to cell temperature.
- **Values on file (as stated in each product note; n/s means not stated):**
  - [[AMETEK Prestolite Power BID]]: compensation range 32-158 F (0-70 C); sensing method n/s (battery average temperature)
  - [[AMETEK Prestolite Power TruBid]]: electrolyte temperature by probe in a cell
  - [[AMETEK Prestolite Power WBID Pro]]: electrolyte and ambient sensors
  - [[Advanced Charging Technologies BATTview]]: resolution +/-1.0 F
  - [[EnerSys Wi-iQ]]: external thermistor
  - [[Fronius TagID]]: temperature sensor (standard)
  - [[HOPPECKE trak collect]]: -30 to 100 C; 0.1 K resolution
  - [[Philadelphia Scientific eGO!core]]: internal sensor
  - [[Philadelphia Scientific eGO!plus]]: internal sensor
  - [[Philadelphia Scientific eGO!pro]]: internal sensor (US page); dual temperature indicators (UK page)
  - [[PosiCharge BMID]]: electrolyte-immersed thermistor
  - [[PosiCharge Battery Rx]]: electrolyte-immersed sensor
  - [[Power Designers PowerTrac 3]]: external thermistor (sheet)
- **Source rule:** the product note holds the source URL for each value; this note copies the value for comparison. If they differ, the product note wins and this note is fixed.
- **Gaps and to-do:** 11 product(s) have a value; document-based values to be added as documents are supplied.

## Aliases

- MM05
- Temperature Sensing


## Former ids
