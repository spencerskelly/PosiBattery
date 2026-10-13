---
type: Info
subtype:
id: INFO-90031
uid: 20261013190000001skellyspencer
status: Draft
tags:
  - research
  - soc-soh
  - methods
  - reference
describedBy:
  - "[[Document - ADI Considerations for Fuel Gauging Lithium Iron Phosphate Batteries]]"
  - "[[Document - TI BQ34Z100-G1 Data Sheet]]"
  - "[[Document - Electronic Design TI bq34z110 Lead-Acid Gas Gauge IC (2013-05-30)]]"
  - "[[Document - Victron BMV-712 Smart Manual Battery Capacity and Peukert Exponent (retrieved 2026-10-13)]]"
  - "[[Document - Midtronics Using Conductance Technology to Ensure Battery System Reliability (BATTCON 2003)]]"
  - "[[Document - TWAICE State of Health Encyclopedia Entry (retrieved 2026-10-13)]]"
  - "[[Document - Battery University BU-903 How to Measure State of Charge (retrieved 2026-10-13)]]"
  - "[[Document - Battery University BU-904 How to Measure Capacity (retrieved 2026-10-13)]]"
  - "[[Document - Orion BMS State of Charge Calculation with Dynamic Drift (retrieved 2026-10-13)]]"
  - "[[Document - Orion BMS Troubleshooting State of Charge Jumps]]"
  - "[[Document - Fluke Recommended Battery Tests and Testing Schedule (retrieved 2026-10-13)]]"
  - "[[Document - Cadex Spectro Technology Page (retrieved 2026-10-13)]]"
  - "[[Document - Bilfinger et al. Why We Need a Standardized State of Health Definition for EV Battery Packs (2025)]]"
  - "[[Document - Paizulamu et al. LiFePO4 SOC Estimation under OCV-SOC Curve Error (arXiv 2024)]]"
  - "[[Document - Berecibar et al. Critical Review of State of Health Estimation Methods of Li-ion Batteries for Real Applications (2016)]]"
---

# SOC and SOH Methods Reference

## Definition

Engineer-facing reference of the methods used to find battery state of charge (SOC) and state of health (SOH): what each method needs, which chemistries it suits, and what the sources say about its limits. It extends the academic review in [[SOC and Health Estimation Literature Review]] with manufacturer, vendor and educational sources. Products are in [[SOC and SOH Product Landscape]]; measurement specifications, definitions and standards are in [[SOC and SOH Specifications and Standards]]; the criteria for choosing are in [[SOC and SOH Decision Criteria]].

## Notes

**Reading rule.** Source keys (S1 to S24) are listed at the bottom. Vendor-authored sources (tier T4, or T1 manufacturer claims) are marked as claims. Numbers are as stated by the source; none was reproduced here. Where this note derives a number the word *derived* appears. Disagreements are in [[Battery Product Landscape Conflicts and Open Questions]] (C190 to C195).

### SOC methods

| # | Method | Inputs | Chemistry in the sources | Stated strengths and limits | Source |
|---|---|---|---|---|---|
| M1 | Open-circuit voltage (OCV) lookup | terminal voltage after rest; temperature | lead-acid, lithium | Needs rest: 'at least four hours; battery manufacturers recommend 24 hours for lead acid'. Calcium additive raises lead-acid voltage 5 to 8 percent; surface charge raises it after charging. For Li-phosphate, NMC and Li-manganese '80 percent of the stored energy remains in the flat voltage profile'. BCI table for 12 V lead-acid after 24 h at 26 C: 12.65 V 100%, 12.45 V 75%, 12.24 V 50%, 12.06 V 25%, 11.89 V 0% | S11 |
| M1a | OCV on LiFePO4 | as M1 | LiFePO4 | 'Just 1% of SOC change corresponds to only a few millivolts'; hysteresis between charge and discharge, shown with an SOC error of 35% in the article's Figure 2. Orion: in the middle range 'just a 50mV difference can correspond to a 75% difference in state of charge' (about 0.67 mV per percent, derived); cell voltages of about 3.15 to 3.45 V are not usable as correction points | S1, S14 |
| M2 | Specific gravity (hydrometer) | electrolyte density, temperature | flooded lead-acid only | Same BCI table (SG 1.265 to 1.120). Full-charge SG by type: forklift traction 1.280, deep-cycle up to 1.330, starter 1.265, stationary 1.225; full-charge reading shifts with temperature (1.266 at 40 C, 1.280 at 20 C, 1.294 at 0 C). Stratification and evaporation distort it | S11 |
| M3 | Coulomb counting | current through a sense resistor or shunt; time; capacity | all | Works well in Li-ion because of high coulombic efficiency and low self-discharge; losses in other chemistries mean less energy out than in; periodic calibration recommended. Gauge-IC coulomb counter in S3: input range 0.125 V either way across the sense resistor, 10 uV input offset, 14 to 15 bit, 1 s conversion | S11, S3 |
| M4 | Peukert-corrected counting | as M3 plus a rate exponent | lead-acid | Monitor accepts an exponent of 1.00 to 1.50, default 1.25 'an acceptable average value for most lead acid batteries'; example: a 100 Ah lead-acid battery rated at C20 may deliver about 56 Ah at C2. The manual calls the exponent 'no more than a rough approximation of reality', so capacity is least certain at very high currents | S7 |
| M5 | Counting with voltage-based correction | as M3 plus cell voltages and a stored OCV table | lithium (Orion, ADI) | Orion: counts current, compares with a voltage-based estimate and lets SOC drift toward it; cannot calculate SOC without a working current sensor; after reset, fault clear or first connection it defaults to 50% SOC; SOC is set to a 'Charged SOC' value when the charger is turned off for a full charge; one weak or high-resistance cell causes jumps; iron-phosphate cells may show 50% of normal capacity in the cold. ADI: continual small OCV-based corrections need no rest, full or empty state; capacity relearn only outside a 20% to 72% keep-out window; reported error under 2% over a pattern of more than a week without reaching full or empty, on one 2.5 Ah 26650 test cell | S13, S14, S1 |
| M6 | Impedance Track (TI) | voltage, current, temperature, stored cell data | lead-acid, Li-ion, LiFePO4, NiMH, NiCd (product page) | Compares OCV with loaded voltage to get cell impedance and compares SOC before and after a load to get total capacity (Qmax). Relearn needs relaxation: average current under 40 mA for 60 s (default), not above C/20, OCV read after about 6 min, Qmax update also needs dV/dt below 4 uV/s. Self-reported error MaxError: 100% after full reset, 1% after Qmax and resistance update, 3% after Qmax only, 5% after resistance only. TI claims 'as little as 1% error across a wide variety of operating conditions' (conditions not stated) | S3, S2, S4 |
| M7 | Model-based filters (EKF, UKF, observers) | voltage, current, temperature, a fitted model, noise settings | mostly lithium | See the approach register in [[SOC and Health Estimation Literature Review]]. S21: on a 1.1 Ah CALCE LiFePO4 cell at -10 C (US06), a UKF baseline had 13.05% RMS SOC error and an adaptive multi-model filter 2.97% when the OCV-SOC curve was wrong; the paper estimates SOC bias of about +0.51 %/C at high temperature and -0.43 %/C at low temperature if a 25 C curve is used uncorrected | S21 |
| M8 | Data-driven (neural network, regression) | as M7 plus training data | mostly lithium | See [[SOC and Health Estimation Literature Review]]; needs training data covering the operating range | [[SOC and Health Estimation Literature Review]] |

### SOH methods

| # | Method | Inputs | Chemistry in the sources | Stated strengths and limits | Source |
|---|---|---|---|---|---|
| H1 | Full-cycle capacity test | controlled discharge, charge, discharge | all | 'Still the most dependable method to measure battery capacity' but 'not practical' on large lead-acid; two identical tests days apart 'differ much as +/-15 percent average in capacity'. IEEE-based schedule quoted by a test vendor: discharge test at intervals 'not greater than 25 % of the expected service life, or two years, whichever is less'; annually once the battery reaches 85% of expected life or has dropped more than 10% | S12, S16 |
| H2 | Capacity ratio from counting | Ah of one complete cycle over initial capacity | lithium (sources), any | Needs comparable conditions: 'the available capacity needs to be determined under the same conditions as the initial capacity'; field data are dynamic and noisy | S9, [[SOC and Health Estimation Literature Review]] |
| H3 | Conductance or ohmic trend | low-frequency ac signal through the battery, response | lead-acid (stationary) | Vendor claim: conductance tracks plate surface available for reaction and falls with sulfation and shedding; compare with a new or average battery; example cell at 400 S against a string average of 1500 S 'a significant loss of capacity'; no fixed replacement threshold; discharge test still advised for a questionable cell; says nothing about SOC. Test-vendor blog: capacity drop over 10% or resistance rise of 20% or more against baseline are failure indicators | S8, S16 |
| H4 | Multi-model impedance spectroscopy | multi-frequency signal of a few millivolts | lead-acid (starter), others | Cadex Spectro: estimates capacity in seconds; accuracy depends on the quality of the stored matrix; 'resistance alone cannot predict capacity'; best on a working battery pulled from service. The Cadex page gives no accuracy figure and does not mention traction batteries. The two Battery University pages disagree on whether it suits new batteries (C194) | S12, S17, S11 |
| H5 | Resistance trend from the gauge | Ra learned by Impedance Track | lead-acid, lithium | TI StateOfHealth register is 0 to 100%, full-charge capacity at 25 C and a set load (default -400 mA) over design capacity | S3 |
| H6 | Differential voltage, learned models, remaining useful life | high-resolution V and Ah, history | lithium | See [[SOC and Health Estimation Literature Review]] (sources 11 to 15); S22 is a 2016 review of SOH methods 'for real applications' (abstract only read here) | [[SOC and Health Estimation Literature Review]], S22 |

### What the sources do not give

- No source here compares methods on a forklift duty cycle (partial discharge, opportunity charging, high pulses) or on an 80 V pack.
- Lead-acid SOC and SOH evidence is mostly educational or vendor material; the academic evidence in [[SOC and Health Estimation Literature Review]] is mostly lithium.
- No source states a required accuracy for a forklift battery gauge. The requirement is a product decision (see [[SOC and SOH Decision Criteria]]).

## Sources

- **S1** [[Document - ADI Considerations for Fuel Gauging Lithium Iron Phosphate Batteries]] <https://wcm-cce.cldnet.analog.com/media/en/technical-documentation/tech-articles/considerations-for-fuel-gauging-lithiumironphosphate-batteries.pdf>
- **S2** [[Document - TI BQ34Z100-G1 Product Page (retrieved 2026-10-13)]] <https://www.ti.com/product/BQ34Z100-G1>
- **S3** [[Document - TI BQ34Z100-G1 Data Sheet]] <https://www.ti.com/lit/gpn/BQ34Z100-G1>
- **S4** [[Document - Electronic Design TI bq34z110 Lead-Acid Gas Gauge IC (2013-05-30)]] <https://www.electronicdesign.com/technologies/power/power-delivery/charger-ics/article/21195994/gas-gauge-ic-monitors-lead-acid-battery-state-of-health-state-of-charge>
- **S7** [[Document - Victron BMV-712 Smart Manual Battery Capacity and Peukert Exponent (retrieved 2026-10-13)]] <https://www.victronenergy.com/media/pg/BMV-712_Smart/en/battery-capacity-and-peukert-exponent.html>
- **S8** [[Document - Midtronics Using Conductance Technology to Ensure Battery System Reliability (BATTCON 2003)]] <https://www.vertiv.com/48dfcf/globalassets/documents/battcon-static-assets/2003/using-conductance-technology-to-ensure-battery-system-reliability.pdf>
- **S9** [[Document - TWAICE State of Health Encyclopedia Entry (retrieved 2026-10-13)]] <https://www.twaice.com/battery-encyclopedia/state-of-health>
- **S11** [[Document - Battery University BU-903 How to Measure State of Charge (retrieved 2026-10-13)]] <https://batteryuniversity.com/article/bu-903-how-to-measure-state-of-charge>
- **S12** [[Document - Battery University BU-904 How to Measure Capacity (retrieved 2026-10-13)]] <https://batteryuniversity.com/article/bu-904-how-to-measure-capacity>
- **S13** [[Document - Orion BMS State of Charge Calculation with Dynamic Drift (retrieved 2026-10-13)]] <https://orionbms.com/?p=107>
- **S14** [[Document - Orion BMS Troubleshooting State of Charge Jumps]] <https://www.orionbms.com/manuals/pdf/troubleshooting_soc_jumps.pdf>
- **S16** [[Document - Fluke Recommended Battery Tests and Testing Schedule (retrieved 2026-10-13)]] <https://www.fluke.com/en/learn/blog/energy-efficiency/recommended-battery-tests>
- **S17** [[Document - Cadex Spectro Technology Page (retrieved 2026-10-13)]] <https://www.cadex.com/technology/our-technologies/spectro>
- **S21** [[Document - Paizulamu et al. LiFePO4 SOC Estimation under OCV-SOC Curve Error (arXiv 2024)]] <https://arxiv.org/abs/2410.23646>
- **S22** [[Document - Berecibar et al. Critical Review of State of Health Estimation Methods of Li-ion Batteries for Real Applications (2016)]] <https://ideas.repec.org/a/eee/rensus/v56y2016icp572-587.html>

## Aliases

- state of charge methods
- state of health methods
- coulomb counting
- ampere-hour counting
- open-circuit voltage method
- OCV-SOC curve
- Peukert
- Kalman filter SOC
- impedance tracking
- fuel gauge algorithm
- SOHc
- SOHr
- SOHe

## Former ids
