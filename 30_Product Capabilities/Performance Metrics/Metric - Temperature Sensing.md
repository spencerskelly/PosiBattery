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
  - "[[Battery Temperature Measurement Design]]"
  - "[[External Thermistor Temperature Sensor]]"
  - "[[Ambient Temperature Sensor]]"
  - "[[Internal Temperature Sensor]]"
  - "[[Cell-Connector Temperature Sensing]]"
  - "[[Internal Thermistor Temperature Sensor]]"
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
  - [[Power Designers PowerTrac SP+]]: external or internal thermistor options (dated sheet)
  - [[Exide Motion+ EasyMonitor]]: 3-in-1 sensor wrapped around a cell connector; temperature technology n/s
  - [[Green Cubes SAFEFlex Battery]]: internal temperature sensors monitored by the BMS
  - [[Stryten M-Series Li610 Battery]]: BMS-based temperature monitoring; sensor topology n/s
  - [[TUG ALPHA 1 Pushback]]: BMS monitors battery temperature; sensor topology n/s
- **Source rule:** the product note holds the source URL for each value; this note copies the value for comparison. If they differ, the product note wins and this note is fixed.
- **Gaps and to-do:** product notes remain authoritative. Several products report temperature without publishing sensor technology or locus; those stay at the generic [[Battery Temperature Measurement Design]] level until stronger evidence is available.

## Aliases

- MM05
- Temperature Sensing


## Former ids
