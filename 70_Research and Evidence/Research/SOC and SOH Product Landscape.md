---
type: Info
subtype:
id: INFO-90032
uid: 20261013190000002skellyspencer
status: Draft
tags:
  - research
  - soc-soh
  - products
describedBy:
  - "[[Document - ADI Considerations for Fuel Gauging Lithium Iron Phosphate Batteries]]"
  - "[[Document - TI BQ34Z100-G1 Product Page (retrieved 2026-10-13)]]"
  - "[[Document - Electronic Design TI bq34z110 Lead-Acid Gas Gauge IC (2013-05-30)]]"
  - "[[Document - ADI MAX17320 Product Page (retrieved 2026-10-13)]]"
  - "[[Document - Victron SmartShunt Product Page (retrieved 2026-10-13)]]"
  - "[[Document - Midtronics Using Conductance Technology to Ensure Battery System Reliability (BATTCON 2003)]]"
  - "[[Document - TWAICE Fleet Operator Page (retrieved 2026-10-13)]]"
  - "[[Document - Orion BMS State of Charge Calculation with Dynamic Drift (retrieved 2026-10-13)]]"
  - "[[Document - Orion BMS Troubleshooting State of Charge Jumps]]"
  - "[[Document - EnerSys Truck iQ Operating Manual (GLOB-EN-OM-TIQ-APAC 0324)]]"
  - "[[Document - Cadex Spectro Technology Page (retrieved 2026-10-13)]]"
  - "[[Document - Flux Power LiFT Pack L-Series L48 Brochure]]"
  - "[[Document - Delta Systems Flux Power SOC Display]]"
---

# SOC and SOH Product Landscape

## Definition

Products that provide SOC or SOH today, grouped by what they are: gauge ICs, shunt monitors, battery management systems (BMS), forklift battery packs and displays, test instruments and cloud analytics. This is a reference of what the sources state, not a ranking. Methods are in [[SOC and SOH Methods Reference]]; specifications in [[SOC and SOH Specifications and Standards]].

## Notes

**Scope and limits.** Pages were read on 2026-10-13 through a summarising fetch; items the page did not state are marked 'not stated'. Where a product is already modeled in the vault, its note is linked and not re-derived here. Product status (active, discontinued) was checked only for the TI BQ34Z100-G1 (listed active).

### Gauge ICs

| Product | Chemistries | Range | SOC and SOH output | Interfaces | Stated accuracy | Source |
|---|---|---|---|---|---|---|
| TI BQ34Z100-G1 (Impedance Track) | lead-acid, Li-ion and Li-polymer, LiFePO4, NiMH, NiCd | 3 V to 65 V through an external voltage translation circuit; 100 mAh to 32,000 mAh; up to 32 A in standard configurations; -40 C to 85 C | SOC integer 0 to 100% with MaxError; StateOfHealth 0 to 100%; remaining and full-charge capacity 1 mAh per bit | I2C, HDQ, LEDs, ALERT pin; SHA-1/HMAC authentication | 'as little as 1% error' (conditions not stated) | S2, S3 |
| TI bq34z110 (2013 article) | lead-acid | 4 V, 12 V, 24 V, 48 V and higher with external scaling, up to 65,535 mV | SOC and SOH, tab-disconnect detection in a 2-cell parallel system | HDQ, I2C | SOC 'within 1% error over normal operating conditions'; capacity 'up to a 95-percent accurate' for the battery's life (conditions not stated) | S4 |
| ADI MAX17320 (ModelGauge m5 EZ) | Li-ion and Li-polymer, 2S to 4S | not stated beyond 2S to 4S; evaluation kit -10 A to +10 A with a 5 mOhm sense resistor | age and a 'Cycle+' age forecast | I2C, 1-Wire; SBS 1.1 register set | not stated | S5 |
| ADI MAX17201 and MAX17055 families | lithium, with an LFP mode | single cell and small packs | SOC | I2C | under 2% on one LFP test cell (S1) | S1 |

### Monitors and BMS

| Product | Class | Chemistries | SOC and SOH | Interfaces | Stated accuracy | Source |
|---|---|---|---|---|---|---|
| Victron SmartShunt | shunt battery monitor, 300 A to 2000 A | lithium, AGM, flooded (custom profiles) | SOC, time remaining, V, I, Ah, cycles, deepest discharge; no SOH listed; Peukert exponent set by the user (S7) | Bluetooth app, VE.Direct | '99.6% accuracy' without saying which quantity | S6, S7 |
| Orion BMS | lithium BMS | lithium (page says Li-Ion) | SOC by current counting with voltage-based drift correction; needs a current sensor; defaults to 50% SOC after reset | not covered here | not stated | S13, S14 |

### Forklift packs, displays and vault products

| Product | What the source says about SOC or SOH | Source |
|---|---|---|
| [[Flux Power LiFT Pack]] L-Series L48 (LiFePO4, 48 V, 420 Ah, 20.2 kWh) | In-house UL Listed BMS; 'accurate battery discharge indicator', lift lockout at low SOC, early warning for safe shutdown; CAN to the truck; no SOH, no J1939 mention, no accuracy figure. A separate display works with J1939 or CANopen BMS | S18, S19 |
| [[EnerSys Truck iQ]] with Wi-iQ 3/4 or NexSys iON BMS | The display shows SOC read from the monitor or BMS; the manual does not explain the calculation. Default warning and alert: flooded and TPPL 30% and 20% SoC; TPPL with ATP 10% and 5% USoC; NexSys iON 4% and 2% USoC, not adjustable. CANopen (PN3) and J1939 (PN2 with Wi-iQ 4 and later); voltage shown to 0.1 V; 15 to 120 V input | S15 |
| Already in the vault | [[PosiCharge BMID]], [[AMETEK Prestolite Power WBID Pro]], [[Power Designers PowerTrac DT3]], [[Philadelphia Scientific eGO!pro]], [[Raymond iBattery]], [[EnerSys Wi-iQ]], [[EnerSys NexSys iON Battery]]: see each note for what it states about SOC or SOH | vault |

### Test instruments and analytics

| Product | Role | What the source says | Source |
|---|---|---|---|
| Midtronics conductance testers | handheld SOH test for lead-acid | Vendor paper on conductance (see M-H3); specific tester models were not read | S8 |
| Cadex Spectro | handheld multi-model impedance spectroscopy | Capacity in seconds; no numeric accuracy on the page; traction batteries not mentioned | S17, S12 |
| TWAICE | cloud battery analytics for e-vehicle fleets | 'industry leading accuracy' with no metric, inputs or deployment stated; points to sales for technical detail | S9, S10 |

### Observations (engineering inference, not source claims)

- Only one gauge-IC claim in the set covers lead-acid and lithium with the same part (TI BQ34Z100-G1), and its stated voltage ceiling is 65 V (see C193 against 80 V forklift packs).
- Two products report a usable SOC (USoC) that differs from SOC (EnerSys PN3 thresholds); the meaning of 0% differs by product, which matters when comparing readings.
- None of the forklift-pack sources states how SOC is calculated or how accurate it is.
- A Flux Power patent on battery state of health was reported by a financial news site (barchart); the page returned no text, so its content is not recorded. Open item: obtain the patent number.

## Sources

- **S1** [[Document - ADI Considerations for Fuel Gauging Lithium Iron Phosphate Batteries]] <https://wcm-cce.cldnet.analog.com/media/en/technical-documentation/tech-articles/considerations-for-fuel-gauging-lithiumironphosphate-batteries.pdf>
- **S2** [[Document - TI BQ34Z100-G1 Product Page (retrieved 2026-10-13)]] <https://www.ti.com/product/BQ34Z100-G1>
- **S3** [[Document - TI BQ34Z100-G1 Data Sheet]] <https://www.ti.com/lit/gpn/BQ34Z100-G1>
- **S4** [[Document - Electronic Design TI bq34z110 Lead-Acid Gas Gauge IC (2013-05-30)]] <https://www.electronicdesign.com/technologies/power/power-delivery/charger-ics/article/21195994/gas-gauge-ic-monitors-lead-acid-battery-state-of-health-state-of-charge>
- **S5** [[Document - ADI MAX17320 Product Page (retrieved 2026-10-13)]] <https://www.analog.com/en/products/max17320.html>
- **S6** [[Document - Victron SmartShunt Product Page (retrieved 2026-10-13)]] <https://www.victronenergy.com/battery-monitors/smart-battery-shunt>
- **S7** [[Document - Victron BMV-712 Smart Manual Battery Capacity and Peukert Exponent (retrieved 2026-10-13)]] <https://www.victronenergy.com/media/pg/BMV-712_Smart/en/battery-capacity-and-peukert-exponent.html>
- **S8** [[Document - Midtronics Using Conductance Technology to Ensure Battery System Reliability (BATTCON 2003)]] <https://www.vertiv.com/48dfcf/globalassets/documents/battcon-static-assets/2003/using-conductance-technology-to-ensure-battery-system-reliability.pdf>
- **S9** [[Document - TWAICE State of Health Encyclopedia Entry (retrieved 2026-10-13)]] <https://www.twaice.com/battery-encyclopedia/state-of-health>
- **S10** [[Document - TWAICE Fleet Operator Page (retrieved 2026-10-13)]] <https://www.twaice.com/industries/e-mobility/fleet-operator>
- **S12** [[Document - Battery University BU-904 How to Measure Capacity (retrieved 2026-10-13)]] <https://batteryuniversity.com/article/bu-904-how-to-measure-capacity>
- **S13** [[Document - Orion BMS State of Charge Calculation with Dynamic Drift (retrieved 2026-10-13)]] <https://orionbms.com/?p=107>
- **S14** [[Document - Orion BMS Troubleshooting State of Charge Jumps]] <https://www.orionbms.com/manuals/pdf/troubleshooting_soc_jumps.pdf>
- **S15** [[Document - EnerSys Truck iQ Operating Manual (GLOB-EN-OM-TIQ-APAC 0324)]] <https://enersys.com/48e4ff/globalassets/documents/product-documentation/_enersys/apac/glob-en-om-tiq-apac-0324.pdf>
- **S17** [[Document - Cadex Spectro Technology Page (retrieved 2026-10-13)]] <https://www.cadex.com/technology/our-technologies/spectro>
- **S18** [[Document - Flux Power LiFT Pack L-Series L48 Brochure]] <https://www.fluxpower.com/hubfs/L48%20Battery%20Pack%20-%20Brochure-2.pdf>
- **S19** [[Document - Delta Systems Flux Power SOC Display]] <https://deltasystemsinc.com/capabilities/how-we-innovate/flux-power-charges-on-with-new-soc-display-from-delta-systems>

## Former ids
