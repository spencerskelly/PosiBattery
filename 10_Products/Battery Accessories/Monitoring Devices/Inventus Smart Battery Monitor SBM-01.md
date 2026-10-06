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
  - "[[Alert on Abnormal Condition]]"
  - "[[Communicate Battery State over CAN]]"
hasDesign:
  - "[[Vehicle-Mounted Display]]"
  - "[[Battery Status Gauge]]"
  - "[[CAN Interface]]"
  - "[[Panel-Mount Gauge Form Factor]]"
  - "[[CAN Battery State Communication Design]]"
hasPart:
  - "[[Vehicle-Mounted Display Module]]"
  - "[[Battery Status Gauge Display Element]]"
  - "[[CAN Communication Circuit]]"
  - "[[CAN Battery State Communication Firmware]]"
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
  - [[Display Battery Status to Operator]] (V): <https://inventuspower.com/wp-content/uploads/IP_User_Manual_SBM-01_2023-08-04_V1.9.pdf>
  - [[Alert on Abnormal Condition]] (V): <https://inventuspower.com/wp-content/uploads/TDS_Smart-Battery-Monitor_2023-Aug_V1.pdf>
  - [[Communicate Battery State over CAN]] (V): <https://inventuspower.com/wp-content/uploads/TDS_Smart-Battery-Monitor_2023-Aug_V1.pdf>
- **Design characteristics, with citations:**
  - [[CAN Interface]] (V): <https://inventuspower.com/wp-content/uploads/TDS_Smart-Battery-Monitor_2023-Aug_V1.pdf>
  - [[Panel-Mount Gauge Form Factor]] (V): <https://inventuspower.com/wp-content/uploads/TDS_Smart-Battery-Monitor_2023-Aug_V1.pdf>
- **Sources used for the mapping above:** Inventus SBM-01 data sheet (08/2023) <https://inventuspower.com/wp-content/uploads/TDS_Smart-Battery-Monitor_2023-Aug_V1.pdf>
- **Truck parts (round 31):** typical (inferred from the device type, not from a source): mounts on [[Truck Battery Compartment]]; connects to [[Truck Controller and CAN Bus]]. See [[Truck Part Connection Register]].

- **Scope correction — amp-hours (2026-10-06):** the SBM-01 data sheet says it reports lifetime Ah consumed, while Inventus describes the panel monitor as receiving battery-system information over CAN. The current evidence therefore supports display/reporting of a battery-supplied Ah counter, not local [[Accumulate Amp-Hours]] execution in the SBM-01.
- **Scope correction — state of charge (2026-10-06):** Inventus describes SBM-01 as receiving battery-system information over CAN and reporting/displaying SOC. The current evidence does not establish that the panel monitor calculates SOC locally, so it no longer directly performs [[Estimate State of Charge]].
- **Scope correction — remaining runtime (2026-10-06):** the SBM-01 receives battery-system information over CAN and reports/displays remaining runtime. The current evidence does not establish that the panel monitor calculates runtime locally, so it no longer directly performs [[Estimate Remaining Run Time]].
- **Scope correction — state of health (2026-10-06):** Inventus states that SBM-01 uses integrated intelligence to **receive important information from the battery system**, while the data sheet/user manual say it reports/displays SOH. Inventus separately states that PROformance batteries communicate battery SOH. Accordingly, SBM-01 no longer performs [[Estimate State of Health]]; it performs [[Display Battery Status to Operator]] as a panel-mounted CAN display of battery-supplied SOH.
- The underlying Inventus battery/BMS SOH estimator is not added as a product performer because no PROformance battery product note currently exists in the vault.

- **Evidence clarification — SOH locus:** Inventus states that the SBM-01 receives battery-system information and displays battery SOH; Inventus separately states that PROformance batteries communicate SOH. This supports the display role, not local SOH estimation in the SBM-01.

- **Architecture realization — CAN battery state communication:** the product is allocated [[CAN Battery State Communication Design]] because published evidence establishes battery-state exchange over CAN or a CAN-based vehicle/battery interface. Message identifiers, signal maps, update rates, and protocol details remain product-specific.

## Aliases

- SBM-01
- Smart Battery Monitor


## Former ids
