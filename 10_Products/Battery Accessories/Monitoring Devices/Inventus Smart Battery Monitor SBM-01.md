---
type: Object
subtype: electrical
id: OBJ-00050
uid: 20261002164202418skellyspencer
status: Draft
tags:
  - adjacent
  - battery-market-reference
  - can
  - commercial-product
  - lithium
  - scope-aftermarket
subtypeOf:
  - "[[Battery Monitoring Device]]"
performs:
  - "[[Display Battery Status to Operator]]"
  - "[[Measure Battery Voltage]]"
  - "[[Accumulate Amp-Hours]]"
  - "[[Estimate State of Charge]]"
  - "[[Estimate Remaining Run Time]]"
  - "[[Alert on Abnormal Condition]]"
  - "[[Communicate Battery State over CAN]]"
hasDesign:
  - "[[Battery Status Gauge]]"
  - "[[CAN Interface]]"
  - "[[Panel-Mount Gauge Form Factor]]"
madeBy:
  - "[[Inventus Power]]"
---

# Inventus Smart Battery Monitor SBM-01

## Definition

Inventus Power CAN battery monitor that reports lithium battery state and replaces an existing 52 mm panel monitor.

## Notes

**Summary:**
Inventus Power panel-mount CAN battery monitor that reports lithium battery state and replaces an existing 52 mm monitor.

**Marketed features:**
- Reports SOC, SOH, voltage, run time remaining and lifetime Ah
- Auto-detects CAN 125 kbps-1 Mbps; J1939, CANopen and NMEA 2000
- Limp-home notification and fault diagnostics
- Drop-in 52 mm replacement; tool-less flush mount; integrated 120 ohm termination
- IP67 front; -30 to 70 C; 9-60 VDC
- UL 583, EN 50498, FCC Class B, CE

**Summary and features sources:**
Maker or publisher marketing claims as stated, not independently verified.
- Inventus Power (T1), retrieved 2026-10-04. <https://inventuspower.com/wp-content/uploads/TDS_Smart-Battery-Monitor_2023-Aug_V1.pdf>

- The data sheet (Aug 2023) lists reporting of state of charge, state of health, battery voltage, run time remaining and lifetime Ah consumed; CAN with auto baud-rate detection from 125 kbps to 1 Mbps; limp-home mode notification; fault diagnostics; drop-in replacement for a 52 mm monitor; integrated CAN termination; supply 9 to 60 VDC; typical power 1.4 W; operating -30 to 70 C; storage -40 to 80 C; humidity 5 to 85 percent; kit for Inventus S/M-48V60-TRX batteries. Source: Inventus Power SBM-01 data sheet (T1), retrieved 2026-10-02. <https://inventuspower.com/wp-content/uploads/TDS_Smart-Battery-Monitor_2023-Aug_V1.pdf>
- **Locus and fit:** appears to be a panel-mounted vehicle-side monitor for Inventus lithium batteries; MHE or GSE use is not stated in the retrieved text.
- **Functions performed, with citations** (V = verified this pass, C = carried from seed text, U = user-stated):
  - [[Measure Battery Voltage]] (V): <https://inventuspower.com/wp-content/uploads/TDS_Smart-Battery-Monitor_2023-Aug_V1.pdf>
  - [[Accumulate Amp-Hours]] (V): <https://inventuspower.com/wp-content/uploads/TDS_Smart-Battery-Monitor_2023-Aug_V1.pdf>
  - [[Estimate State of Charge]] (V): <https://inventuspower.com/wp-content/uploads/TDS_Smart-Battery-Monitor_2023-Aug_V1.pdf>
  - [[Estimate State of Health]] (V): <https://inventuspower.com/wp-content/uploads/TDS_Smart-Battery-Monitor_2023-Aug_V1.pdf>
  - [[Estimate Remaining Run Time]] (V): <https://inventuspower.com/wp-content/uploads/TDS_Smart-Battery-Monitor_2023-Aug_V1.pdf>
  - [[Alert on Abnormal Condition]] (V): <https://inventuspower.com/wp-content/uploads/TDS_Smart-Battery-Monitor_2023-Aug_V1.pdf>
  - [[Communicate Battery State over CAN]] (V): <https://inventuspower.com/wp-content/uploads/TDS_Smart-Battery-Monitor_2023-Aug_V1.pdf>
- **Design characteristics, with citations:**
  - [[CAN Interface]] (V): <https://inventuspower.com/wp-content/uploads/TDS_Smart-Battery-Monitor_2023-Aug_V1.pdf>
  - [[Panel-Mount Gauge Form Factor]] (V): <https://inventuspower.com/wp-content/uploads/TDS_Smart-Battery-Monitor_2023-Aug_V1.pdf>
- **Sources used for the mapping above:** Inventus SBM-01 data sheet (08/2023) <https://inventuspower.com/wp-content/uploads/TDS_Smart-Battery-Monitor_2023-Aug_V1.pdf>
- **Truck parts (round 31):** typical (inferred from the device type, not from a source): mounts on [[Truck Battery Compartment]]; connects to [[Truck Controller and CAN Bus]]. See [[Truck Part Connection Register]].

- **Scope correction — state of health (2026-10-06):** Inventus states that SBM-01 uses integrated intelligence to **receive important information from the battery system**, while the data sheet/user manual say it reports/displays SOH. Inventus separately states that PROformance batteries communicate battery SOH. Accordingly, SBM-01 no longer performs [[Estimate State of Health]]; it performs [[Display Battery Status to Operator]] as a panel-mounted CAN display of battery-supplied SOH.
- The underlying Inventus battery/BMS SOH estimator is not added as a product performer because no PROformance battery product note currently exists in the vault.

## Aliases

- SBM-01
- Smart Battery Monitor


## Former ids
