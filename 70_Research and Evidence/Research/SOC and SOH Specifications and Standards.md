---
type: Info
subtype:
id: INFO-90033
uid: 20261013190000003skellyspencer
status: Draft
tags:
  - research
  - soc-soh
  - specifications
  - standards
describedBy:
  - "[[Document - TI BQ34Z100-G1 Product Page (retrieved 2026-10-13)]]"
  - "[[Document - TI BQ34Z100-G1 Data Sheet]]"
  - "[[Document - TWAICE State of Health Encyclopedia Entry (retrieved 2026-10-13)]]"
  - "[[Document - Fluke Recommended Battery Tests and Testing Schedule (retrieved 2026-10-13)]]"
  - "[[Document - Bilfinger et al. Why We Need a Standardized State of Health Definition for EV Battery Packs (2025)]]"
  - "[[Document - ISO 12405-4:2018 Standard Page (retrieved 2026-10-13)]]"
  - "[[Document - SIST EN IEC 62485-6:2021 Catalog Page (retrieved 2026-10-13)]]"
  - "[[Document - EUR-Lex Regulation 2023-1542 Full Text as Published 2023-07-28 (Articles 3, 10, 13, 14, 77, 78 and Annexes IV, VII, XIII read)]]"
---

# SOC and SOH Specifications and Standards

## Definition

Definitions, measurement-chain specifications and standards that bound an SOC or SOH design. It supports the decision matrix in [[SOC and SOH Decision Criteria]]; methods are in [[SOC and SOH Methods Reference]] and products in [[SOC and SOH Product Landscape]].

## Notes

### Definitions found in the sources

| Term | Definition as stated | Source |
|---|---|---|
| SOH, capacity-based (SOHc) | ratio of current capacity to initial capacity; usually scaled so 1 is new and 0 is the end-of-life criterion, for example 80% remaining capacity | S9 |
| SOH, resistance-based (SOHr) | tracks how far internal resistance has grown | S9 |
| SOH, energy-based (SOHe) | energy still available against energy when new | S9, S20 |
| Standard SOH | S20 (a 2025 preprint) says that for EV packs 'no standard vehicle-level measurement method exists' and proposes capacity- and energy-based metrics measured with onboard charging. No forklift standard definition was found | S20 |
| SOC and usable SOC (USoC) | EnerSys uses USoC for NexSys TPPL with ATP and NexSys iON thresholds and SoC for flooded and TPPL; the manual does not define either | S15 |
| Comparability rule | capacity today and initial capacity must be measured under the same conditions (voltage or SOC limits, rate, temperature) | S9 |

### Measurement-chain specification (TI BQ34Z100-G1 data sheet, as an example chain)

| Item | Value | Source |
|---|---|---|
| Voltage ADC | 14 to 15 bit, 1 mV input offset, 125 ms conversion; BAT pin recommended up to 5 V; external divider to reach 65 V; divider draws about 45 uA typical when enabled | S3 |
| Voltage error plots | pack 25.2 to 39.6 V test range in Fig. 6-4 (error axis -200 to +200 mV; read from plot axes, not a stated spec) | S3 |
| Current ADC (coulomb counter) | 0.125 V either way across the sense resistor; 14 to 15 bit; 10 uV offset; INL 0.007% typical and 0.034% of full scale maximum; 1 s conversion; 2.5 MOhm input resistance | S3 |
| Sense resistor | 5 to 20 mOhm typical | S3, S4 |
| Current thresholds | deadband 5 mA; discharge and charge detection 60 mA and 75 mA default | S3 |
| Temperature | internal sensor -2 mV per C; external thermistor input | S3 |
| Reported resolution | current 1 mA per bit; capacity 1 mAh per bit; SOC and SOH integer percent | S3 |
| Max error register | 1% to 100%, set by relearn state (see M6 in the methods note) | S3 |
| Derived: current range | 0.125 V divided by 5 mOhm is 25 A; by 20 mOhm is 6.25 A; 32 A needs 3.9 mOhm or less (derived) | S3, S2 |
| Derived: offset current error | 10 uV divided by sense resistance: 2 mA at 5 mOhm, 10 mA at 1 mOhm, 40 mA at 0.25 mOhm (derived; 0.25 mOhm is the value that gives 100 mV at 400 A) | S3 |
| ModelGauge MAX17320 kit | default range -10 A to +10 A with 5 mOhm; thermistors read within 1 C | S5 |
| Victron SmartShunt | shunt ratings 300, 500, 1000, 2000 A, IP21 and IP65 versions | S6 |

### Forklift operating context for the chain (from vault sources)

- [[Flux Power LiFT Pack]] L48: 51.2 V nominal, 400 A continuous charge and discharge (S18). A 400 A range is 16 times the 25 A that a 5 mOhm sense resistor allows on this gauge (derived).
- Heli H4 80 V trucks and 80 V lead-acid batteries are above the 65 V ceiling of the gauge examples. See C193.
- Truck displays (S15): 15 to 120 V input range, CAN, voltage shown to 0.1 V.

### Standards and practices

Status 'read' means the catalogue page was read on 2026-10-13, never the standard itself (all are paid documents).

| Standard | Scope as stated | Status | Relevance | Read | Source |
|---|---|---|---|---|---|
| EN IEC 62485-6:2021 | safe operation of lithium-ion batteries in traction applications: electric off-road vehicles including industrial trucks; also installation, use, inspection, maintenance, disposal; defines a BMS as an electronic system that controls current for overcharge, overcurrent, overdischarge and overheating and monitors the battery's state; has BMS (10.1) and inspection and monitoring (14) clauses | CENELEC approval 2021-02-09 | the BMS and monitoring clauses may set what state monitoring a lithium truck battery must provide; text not seen | catalogue page | S24 |
| ISO 12405-4:2018 | test procedures for performance, reliability and electrical functionality of lithium-ion traction packs in electrically propelled road vehicles | edition 1, 2018-07; stage 90.60 | road vehicles; the page does not mention capacity or SOH tests; useful only as a model for test procedure; cell level is IEC 62660 | catalogue page | S23 |
| IEEE 1188 (and IEEE 450) | maintenance, testing and replacement of stationary VRLA (1188) and vented (450) lead-acid batteries; a test vendor's blog cites periodic discharge intervals and says the 80% replacement point comes from manufacturers, not IEEE | not read | stationary batteries; a template for capacity-test and ohmic-trend schedules, not a traction standard | blog only | S16 |
| Regulation (EU) 2023/1542 (EU law, not a standard) | legal definitions of state of charge (available energy as a percentage of manufacturer-declared rated capacity) and state of health (condition and ability to deliver specified performance compared with initial condition); Annex VII state-of-health parameters (remaining capacity, power, round trip efficiency, self-discharge, ohmic resistance; SOCE for EV); Annex XIII passport use data include periodically recorded state of charge | full text read 2026-10-18 | EU market only; Art. 14 names stationary, LMT and EV batteries, not forklift traction batteries (C351); no accuracy requirement for SOC or SOH was found in the text | primary text in repo | [[Document - EUR-Lex Regulation 2023-1542 Full Text as Published 2023-07-28 (Articles 3, 10, 13, 14, 77, 78 and Annexes IV, VII, XIII read)]] |
| EN 1175-1 and similar truck electrical standards | safety of industrial trucks, electrical requirements (title from search results) | not read | may constrain truck-side display and battery interface | not read | none |

No document was found that defines required SOC accuracy for forklift batteries.

### Documents to download

Not available free in this session; please obtain if you want the matrix to cite them. Priority order:

1. EN IEC 62485-6:2021 (BMS clause 10.1, inspection and monitoring clause 14).
2. IEEE 1188-2005 and IEEE 450 (capacity test and ohmic-trend rules for lead-acid).
3. TI application notes for Impedance Track (theory and implementation) and for lead-acid configuration of the BQ34Z100, plus the bq34z110 data sheet if lead-acid at 12 to 48 V is of interest.
4. MAX17320 and MAX17201 data sheets (accuracy tables) from Analog Devices.
5. Victron SmartShunt and BMV-712 data sheets (accuracy by quantity, SOC calculation).
6. Midtronics and Cadex tester data sheets for traction (large-cell) batteries.
7. The Flux Power SOH patent (number not retrieved) and the Hu, Berecibar and Plett reviews in full text.
8. Truck-OEM CAN specifications for battery SOC messages (for example the J1939 and CANopen profiles named in S15 and S19).
9. EN 1175-1 and UL standards for lithium forklift batteries, after confirming which apply.

## Sources

- **S2** [[Document - TI BQ34Z100-G1 Product Page (retrieved 2026-10-13)]] <https://www.ti.com/product/BQ34Z100-G1>
- **S3** [[Document - TI BQ34Z100-G1 Data Sheet]] <https://www.ti.com/lit/gpn/BQ34Z100-G1>
- **S4** [[Document - Electronic Design TI bq34z110 Lead-Acid Gas Gauge IC (2013-05-30)]] <https://www.electronicdesign.com/technologies/power/power-delivery/charger-ics/article/21195994/gas-gauge-ic-monitors-lead-acid-battery-state-of-health-state-of-charge>
- **S5** [[Document - ADI MAX17320 Product Page (retrieved 2026-10-13)]] <https://www.analog.com/en/products/max17320.html>
- **S6** [[Document - Victron SmartShunt Product Page (retrieved 2026-10-13)]] <https://www.victronenergy.com/battery-monitors/smart-battery-shunt>
- **S9** [[Document - TWAICE State of Health Encyclopedia Entry (retrieved 2026-10-13)]] <https://www.twaice.com/battery-encyclopedia/state-of-health>
- **S15** [[Document - EnerSys Truck iQ Operating Manual (GLOB-EN-OM-TIQ-APAC 0324)]] <https://enersys.com/48e4ff/globalassets/documents/product-documentation/_enersys/apac/glob-en-om-tiq-apac-0324.pdf>
- **S16** [[Document - Fluke Recommended Battery Tests and Testing Schedule (retrieved 2026-10-13)]] <https://www.fluke.com/en/learn/blog/energy-efficiency/recommended-battery-tests>
- **S18** [[Document - Flux Power LiFT Pack L-Series L48 Brochure]] <https://www.fluxpower.com/hubfs/L48%20Battery%20Pack%20-%20Brochure-2.pdf>
- **S20** [[Document - Bilfinger et al. Why We Need a Standardized State of Health Definition for EV Battery Packs (2025)]] <https://arxiv.org/abs/2508.15517>
- **S23** [[Document - ISO 12405-4:2018 Standard Page (retrieved 2026-10-13)]] <https://www.iso.org/standard/71407.html>
- **S24** [[Document - SIST EN IEC 62485-6:2021 Catalog Page (retrieved 2026-10-13)]] <https://iteh.es/catalog/standards/sist/323f4ad1-1c3c-498a-a61a-059a70066d3e/sist-en-iec-62485-6-2021>

## Aliases

- SOC accuracy
- SOH threshold
- 80% end of life
- EN IEC 62485-6
- IEEE 1188
- ISO 12405-4
- measurement chain
- shunt resistor error
- SOC standards

## Former ids
