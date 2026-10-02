---
type: Info
subtype:
id: INFO-00076
uid: 20261002164202420skellyspencer
status: Draft
tags:
  - battery-landscape
  - comparison
  - functions
describes:
  - "[[Battery Monitoring Device]]"
  - "[[Battery Identification and Charge Interface Device]]"
---

# Battery Monitoring Function Map

## Definition

Matrix of reusable monitoring and charger-interface functions against the products that perform them, split by evidence level.

## Notes

- Evidence levels: verified this pass (a source retrieved on 2026-10-02 states it), carried (from the earlier seed notes, not re-checked), user-stated. A blank means no source states it; it does not mean the product lacks the function.
- The authoritative link is `performs` on each product note; this table is a reading aid and is regenerated from the same mapping, so edit the product note first.
- Products with no entries (for example [[PosiCharge BMID 1]]) have no function evidence yet.

| Function | Verified this pass | Carried from seed text | User-stated |
|---|---|---|---|
| [[Measure Battery Voltage]] | [[PosiCharge BMID]], [[PosiCharge Battery Rx]], [[PosiCharge PosiGuard]], [[Crown V-Force BMID]], [[AMETEK Prestolite Power WBID]], [[EnerSys Wi-iQ]], [[Philadelphia Scientific eGO!pro]], [[Philadelphia Scientific eGO!Mini]], [[Power Designers PowerTrac SP+]], [[Power Designers PowerTrac DT3]], [[Power Designers PowerTrac 3]], [[Power Designers PowerTrac Monitor]], [[HOPPECKE trak collect]], [[Raymond iBattery]], [[Hyster Battery Tracker]], [[Yale Battery Vision]], [[Access Control Group CellTrac]], [[Inventus Smart Battery Monitor SBM-01]], [[Exide Motion+ EasyMonitor]], [[Advanced Charging Technologies BATTview]] | [[Energywith withBMS BMU]] | - |
| [[Measure Battery Current]] | [[PosiCharge Battery Rx]], [[PosiCharge PosiGuard]], [[EnerSys Wi-iQ]], [[Philadelphia Scientific eGO!pro]], [[Power Designers PowerTrac SP+]], [[Power Designers PowerTrac DT3]], [[Power Designers PowerTrac 3]], [[Power Designers PowerTrac Monitor]], [[HOPPECKE trak collect]], [[Hyster Battery Tracker]], [[Yale Battery Vision]], [[Exide Motion+ EasyMonitor]], [[Advanced Charging Technologies BATTview]] | [[Energywith withBMS BMU]] | - |
| [[Measure Battery Temperature]] | [[PosiCharge BMID]], [[PosiCharge Battery Rx]], [[Crown V-Force BMID]], [[Fronius TagID]], [[AMETEK Prestolite Power BID]], [[AMETEK Prestolite Power BID with Ah Accumulator]], [[AMETEK Prestolite Power WBID Pro]], [[AMETEK Prestolite Power WBID]], [[AMETEK Prestolite Power TruBid]], [[EnerSys Wi-iQ]], [[Philadelphia Scientific eGO!pro]], [[Philadelphia Scientific eGO!plus]], [[Philadelphia Scientific eGO!core]], [[Philadelphia Scientific eGO!Mini]], [[Power Designers PowerTrac SP+]], [[Power Designers PowerTrac DT3]], [[Power Designers PowerTrac 3]], [[Power Designers PowerTrac Monitor]], [[HOPPECKE trak collect]], [[Crown Battery Health Monitor]], [[Raymond iBattery]], [[Hyster Battery Tracker]], [[Yale Battery Vision]], [[Access Control Group CellTrac]], [[Exide Motion+ EasyMonitor]], [[Advanced Charging Technologies BATTview]] | [[EnerSys iQ Mini]], [[Energywith withBMS BMU]] | - |
| [[Sense Electrolyte Level]] | [[PosiCharge Battery Rx]], [[PosiCharge PosiGuard]], [[Crown V-Force BMID]], [[Fronius TagID]], [[AMETEK Prestolite Power WBID Pro]], [[EnerSys Wi-iQ]], [[Philadelphia Scientific eGO!pro]], [[Philadelphia Scientific eGO!plus]], [[Philadelphia Scientific eGO!core]], [[Philadelphia Scientific eGO!Mini]], [[Philadelphia Scientific SmartBlinky Pro]], [[Flow-Rite Eagle Eye Essential IV]], [[Power Designers PowerTrac SP+]], [[Power Designers PowerTrac 3]], [[HOPPECKE trak collect]], [[Crown Battery Health Monitor]], [[Raymond iBattery]], [[Hyster Battery Tracker]], [[Yale Battery Vision]], [[Access Control Group CellTrac]], [[Exide Motion+ EasyMonitor]], [[Advanced Charging Technologies BATTview]] | [[Energywith withBMS BMU]], [[Flow-Rite Eagle Eye Elite IV]] | - |
| [[Measure Electrolyte Specific Gravity]] | [[AMETEK Prestolite Power TruBid]] | - | - |
| [[Accumulate Amp-Hours]] | [[AMETEK Prestolite Power BID with Ah Accumulator]], [[AMETEK Prestolite Power WBID]], [[AMETEK Prestolite Power Site Probe]], [[Power Designers PowerTrac SP+]], [[Power Designers PowerTrac DT3]], [[HOPPECKE trak collect]], [[Crown Battery Health Monitor]], [[Access Control Group CellTrac]], [[Inventus Smart Battery Monitor SBM-01]], [[Exide Motion+ EasyMonitor]] | [[AMETEK Prestolite Power WBID Pro]], [[EnerSys Wi-iQ]] | - |
| [[Estimate State of Charge]] | [[PosiCharge BMID]], [[PosiCharge Battery Rx]], [[EnerSys Wi-iQ]], [[EnerSys Truck iQ]], [[Power Designers PowerTrac DT3]], [[Power Designers PowerTrac Monitor]], [[Raymond iBattery]], [[Hyster Battery Tracker]], [[Yale Battery Vision]], [[Inventus Smart Battery Monitor SBM-01]], [[Exide Motion+ EasyMonitor]] | [[AMETEK Prestolite Power WBID Pro]] | - |
| [[Estimate State of Health]] | [[Raymond iBattery]], [[Inventus Smart Battery Monitor SBM-01]] | - | - |
| [[Estimate Remaining Run Time]] | [[EnerSys Truck iQ]], [[HOPPECKE trak collect]], [[Inventus Smart Battery Monitor SBM-01]] | - | - |
| [[Log Battery Events and Usage]] | [[PosiCharge BMID]], [[PosiCharge Battery Rx]], [[PosiCharge PosiGuard]], [[Crown V-Force BMID]], [[AMETEK Prestolite Power WBID Pro]], [[AMETEK Prestolite Power WBID]], [[AMETEK Prestolite Power Site Probe]], [[EnerSys Wi-iQ]], [[Philadelphia Scientific eGO!pro]], [[Philadelphia Scientific eGO!plus]], [[Philadelphia Scientific eGO!core]], [[Philadelphia Scientific eGO!Mini]], [[Philadelphia Scientific eGO!c]], [[Power Designers PowerTrac SP+]], [[Power Designers PowerTrac DT3]], [[Power Designers PowerTrac 3]], [[Power Designers PowerTrac Monitor]], [[HOPPECKE trak collect]], [[Raymond iBattery]], [[Exide Motion+ EasyMonitor]], [[Advanced Charging Technologies BATTview]] | [[EnerSys iQ Mini]] | - |
| [[Track Equalization]] | [[EnerSys Wi-iQ]], [[Power Designers PowerTrac 3]], [[Crown Battery Health Monitor]], [[Raymond iBattery]], [[Advanced Charging Technologies BATTview]] | [[AMETEK Prestolite Power WBID Pro]] | - |
| [[Alert on Abnormal Condition]] | [[EnerSys Wi-iQ]], [[Philadelphia Scientific eGO!pro]], [[Philadelphia Scientific eGO!Mini]], [[Philadelphia Scientific eGO!c]], [[Philadelphia Scientific SmartBlinky Pro]], [[Power Designers PowerTrac SP+]], [[Power Designers PowerTrac DT3]], [[HOPPECKE trak collect]], [[Crown Battery Health Monitor]], [[Raymond iBattery]], [[Hyster Battery Tracker]], [[Yale Battery Vision]], [[Access Control Group CellTrac]], [[Inventus Smart Battery Monitor SBM-01]], [[Exide Motion+ EasyMonitor]], [[Advanced Charging Technologies BATTview]] | [[Energywith withBMS BMU]] | - |
| [[Indicate Battery Status Locally]] | [[AMETEK Prestolite Power WBID Pro]], [[AMETEK Prestolite Power TruBid]], [[EnerSys Wi-iQ]], [[EnerSys iQ Mini]], [[Philadelphia Scientific eGO!pro]], [[Philadelphia Scientific eGO!plus]], [[Philadelphia Scientific eGO!Mini]], [[Philadelphia Scientific eGO!c]], [[Philadelphia Scientific SmartBlinky Pro]], [[Flow-Rite Eagle Eye Essential IV]], [[HOPPECKE trak collect]], [[Access Control Group CellVue]], [[Exide Motion+ EasyMonitor]] | [[Flow-Rite Eagle Eye Elite IV]] | - |
| [[Display Battery Status to Operator]] | [[EnerSys Truck iQ]] | - | - |
| [[Identify Battery to Charger]] | [[PosiCharge BMID]], [[Crown V-Force BMID]], [[AMETEK Prestolite Power BID]], [[AMETEK Prestolite Power BID with Ah Accumulator]], [[Power Designers PowerTrac 3]] | - | - |
| [[Report Battery Temperature to Charger]] | [[PosiCharge BMID]], [[Fronius TagID]], [[AMETEK Prestolite Power BID]], [[AMETEK Prestolite Power BID with Ah Accumulator]], [[HOPPECKE trak collect]] | - | - |
| [[Communicate with Charger]] | [[PosiCharge BMID]], [[PosiCharge Battery Rx]], [[PosiCharge PosiGuard]], [[AMETEK Prestolite Power WBID]], [[AMETEK Prestolite Power TruBid]], [[EnerSys Wi-iQ]], [[Power Designers PowerTrac SP+]], [[Power Designers PowerTrac 3]], [[HOPPECKE trak collect]], [[Advanced Charging Technologies BATTview]] | - | - |
| [[Transmit Battery Data Wirelessly]] | [[PosiCharge BMID]], [[PosiCharge Battery Rx]], [[PosiCharge PosiGuard]], [[AMETEK Prestolite Power WBID Pro]], [[AMETEK Prestolite Power WBID]], [[AMETEK Prestolite Power TruBid]], [[EnerSys Wi-iQ]], [[EnerSys iQ Mini]], [[Philadelphia Scientific eGO!pro]], [[Philadelphia Scientific eGO!plus]], [[Philadelphia Scientific eGO!core]], [[Philadelphia Scientific eGO!gateway]], [[Power Designers PowerTrac SP+]], [[Power Designers PowerTrac DT3]], [[Power Designers PowerTrac 3]], [[Power Designers PowerTrac Monitor]], [[Crown Battery Health Monitor]], [[Hyster Battery Tracker]], [[Yale Battery Vision]], [[Advanced Charging Technologies BATTview]] | [[Energywith withBMS BMU]] | - |
| [[Communicate Battery State over CAN]] | [[PosiCharge PosiGuard]], [[EnerSys Wi-iQ]], [[Inventus Smart Battery Monitor SBM-01]] | - | - |
| [[Upload Battery Data to Cloud Portal]] | [[PosiCharge Battery Rx]], [[PosiCharge PosiGuard]], [[AMETEK Prestolite Power WBID Pro]], [[EnerSys iQ Mini]], [[Philadelphia Scientific eGO!pro]], [[Philadelphia Scientific eGO!core]], [[Philadelphia Scientific eGO!gateway]], [[Philadelphia Scientific eGO!Mini]], [[Philadelphia Scientific eGO!c]], [[HOPPECKE trak collect]], [[Crown Battery Health Monitor]], [[Raymond iBattery]], [[Hyster Battery Tracker]], [[Yale Battery Vision]], [[Advanced Charging Technologies BATTview]] | [[Energywith withBMS BMU]] | - |
| [[Export Battery Data to PC]] | [[Philadelphia Scientific eGO!Mini]], [[Power Designers PowerTrac SP+]], [[Power Designers PowerTrac DT3]] | - | - |
| [[Configure Device from Mobile App or PC]] | [[PosiCharge PosiGuard]], [[Crown V-Force BMID]], [[EnerSys Wi-iQ]] | - | - |
| [[Detect Cell Failure]] | [[AMETEK Prestolite Power TruBid]] | - | - |
| [[Detect Battery Weight]] | [[Raymond iBattery]] | - | - |
| [[Detect Voltage Imbalance]] | [[EnerSys Wi-iQ]], [[EnerSys Truck iQ]], [[Exide Motion+ EasyMonitor]] | - | - |
| [[Command Vehicle Operating Limits over CAN]] | [[EnerSys Wi-iQ]] | - | - |
- **Citations (2026-10-02):** every link in this table has its web page listed on the Function or Design note (section Sources) and on the product note. The table itself repeats no claims beyond product-to-note links.

## Aliases

- Function matrix

## Former ids
