---
type: Object
subtype: electrical
id: OBJ-00556
uid: 20261014105727140skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - hands-free
  - charger
  - wireless
productCategory: charger
powerKwMin: 1
powerKwMax: 30
outputVoltageMinV: 24
outputVoltageMaxV: 80
outputCurrentMaxA: 300
airGapMmMin: 0
airGapMmMax: 150
efficiencyPct: 95
subtypeOf:
  - "[[Wireless Charger]]"
describedBy:
  - "[[Document - Delta MOOVair01 48V Data Sheet (Rev 3.1)]]"
  - "[[Document - Delta 30 kW Wireless Charging Article (2024-03-21)]]"
  - "[[Document - Auto Innovations Delta Neumaier Inductive Charging Article]]"
  - "[[Document - Delta EMEA Wireless Charging Systems Page (retrieved 2026-10-14)]]"
  - "[[Document - Delta MOOVair 30 Data Sheet (R3.0, 2024)]]"
  - "[[Document - Delta MOOVair 03 24V Page (retrieved 2026-10-14)]]"
  - "[[Document - Delta MOOVair 03 48V Page (retrieved 2026-10-14)]]"
  - "[[Document - Delta MOOVair 10 36V Page (retrieved 2026-10-14)]]"
  - "[[Document - Delta MOOVair 10 48V Page (retrieved 2026-10-14)]]"
  - "[[Document - Delta Industrial Battery Charging Category Page (retrieved 2026-10-14)]]"
performs:
  - "[[Charge Wirelessly Despite Misalignment]]"
  - "[[Exchange Charge Control Data Between Pads]]"
  - "[[Follow Vehicle Charge Setpoints over CANopen]]"
  - "[[Charge Battery Wirelessly]]"
hasDesign:
  - "[[Inductive Wireless Charging]]"
madeBy:
  - "[[Delta Energy Systems]]"
---

# Delta MOOVair Wireless Charging Series

## Definition

Delta MOOVair inductive charging series from 1 kW (24/36/48 V, 0-20 mm gap) to 30 kW (20-150 mm gap) for forklifts, AGVs and GSE.

## Notes

- The 1 kW data sheet states 24, 36 or 48 V output; the 30 kW article gives no voltage, so 80 V trucks are not shown. Sources: <https://psu.deltaww.com/en/products/download/Datasheet/MOOVair%2001%2048V> (T1); <https://www.mhwmag.com/?p=102503> (T2).

- **Update 2026-10-14 (deployments):** MOOVair 30 is described at 30 kW, 80 V, up to 300 A, 95% over up to 150 mm, IP69, on a Linde P180 tractor converted to the autonomous Factory Train FT630; MOOVair 10 at 10 kW, up to 275 A, on several Linde E16 counterbalanced forklifts converted to the autonomous outdoor FE616 (battery, dates not stated; C260). Range efficiency up to 95.5% wall to battery. Sources: <https://www.auto-innovations.net/news/107451-when-charging-breaks-are-no-longer-an-option>; <https://www.delta-emea.com/en-GB/products/wireless-charging-systems/ALL/> (T2/T1).


- **Model specifications (Delta pages and data sheets, 2026-10-14):**

| Model | Power | Output | Gap | Misalignment | IP (pads) | Source |
|---|---|---|---|---|---|---|
| MOOVair 01 | 1 kW | 24 V 41.7 A; 36 V 27.7 A; 48 V 20.8 A | 0-20 mm | up to 20 mm | IP65 | 48 V data sheet (T1) |
| MOOVair 03 | 3.3 kW | 24 V (12-33 V) 132 A; 48 V (24-66 V) 66 A | 10-30 mm | not stated | IP67 | Delta pages (T1) |
| MOOVair 10 | 10 kW | 36 V (18-44 V) 280 A; 48 V (36-60 V) 200 A; 24/36 V secondary unit | up to 185 mm | not stated | IP69 | Delta pages (T1) |
| MOOVair 30 | 30 kW | 100 V (72-120 V) 300 A, lithium-ion | 105-155 mm | +/-50 mm | IP69 | data sheet R3.0 (T1) |

- Common: CANopen setpoints, Ethernet, Delta pad-to-pad link; efficiency over 92% (01 to 10) and over 95% (30). MOOVair 30 parallel operation and some FCC items are marked pending. Sources: <https://psu.deltaww.com/en/file/marketing_resources/Delta-MOOVair-30-30kW-Wireless-Charging-System-R3.0_2024.106987138b24f82.pdf>; <https://psu.deltaww.com/en/products/wireless-charging-system/MOOVair%2003%2024V>; <https://psu.deltaww.com/en/products/wireless-charging-system/MOOVair%2003%2048V>; <https://psu.deltaww.com/en/products/wireless-charging-system/MOOVair%2010%2036V>; <https://psu.deltaww.com/tr/products/wireless-charging-system/MOOVair%2010%2048V>

## Aliases

- MOOVair


## Former ids
