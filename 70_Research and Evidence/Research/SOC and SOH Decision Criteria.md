---
type: Info
subtype:
id: INFO-90034
uid: 20261013190000004skellyspencer
status: Draft
tags:
  - research
  - soc-soh
  - decision-support
describedBy:
describes:
  - "[[Estimate State of Charge]]"
  - "[[Estimate State of Health]]"
---

# SOC and SOH Decision Criteria

## Definition

Criteria and candidate approach families for an engineer building the SOC and SOH decision matrix. It states what the evidence in the vault says for each criterion and what is missing. It does not score anything: weights and the target accuracy are product decisions that need the owner's input.

## Notes

### Candidate approach families

| Id | Family | Basis in the vault |
|---|---|---|
| A | Embedded counting with OCV recalibration in our own firmware | M3, M5; [[Coulomb Counting State of Charge Estimator Firmware]], [[Voltage-Based State of Charge Estimator Firmware]] |
| B | Gauge IC (Impedance Track or ModelGauge type) | M5, M6; product table in [[SOC and SOH Product Landscape]] |
| C | Model-based filter firmware | M7; [[Model-Based State of Charge Estimator Firmware]] |
| D | Cloud data-driven SOH from fleet history | M8, H6; [[Learned State of Health Service]] |
| E | Periodic test with an instrument (conductance or impedance) | H3, H4 |
| F | Read SOC and SOH from the battery maker's BMS over CAN | Flux Power, EnerSys products in the landscape note |
| G | Full-cycle capacity test as the SOH reference | H1 |

### Criteria with the evidence and gaps

| Criterion | What the evidence says | Gap or input needed |
|---|---|---|
| Chemistry coverage | gauge IC claims lead-acid and lithium (S2); Peukert and specific gravity apply to lead-acid only (S7, S11); LFP needs flat-curve handling (S1, S14) | which chemistries are in scope, and whether one design must serve both |
| Voltage range | TI examples reach 65 V with external scaling (S2, S4); forklift packs go to 80 V and above (C193) | the highest pack voltage in scope |
| Current range and shunt | 25 A max at 5 mOhm on the example gauge; 400 A packs exist (S18); offset error grows as shunt resistance falls (derived) | the maximum and typical current, and the allowed offset error |
| SOC accuracy | claims are not comparable (C191); no forklift-specific requirement exists | the accuracy target, the test profile and the error definition (see [[Estimate State of Charge and Health - Declare Accuracy Basis]]) |
| SOH definition and threshold | capacity, resistance and energy versions exist (S9); thresholds of 80%, 90%, 70%, 30% appear with different meanings (C192) | which SOH, which threshold, and who acts on it |
| Rest and relearn opportunities | OCV methods need hours of rest (C190); the TI gauge needs low-current relaxation (S3); forklift duty may have little rest (opportunity charging is not in the sources' test profiles) | typical rest and charge pattern in the target fleets |
| Start-up and fault behaviour | Orion defaults to 50% after reset and cannot compute SOC without a current sensor (S14); TI MaxError is 100% after reset (S3) | what the product must show after a reset or sensor fault |
| Calibration and commissioning | OCV tables and drift points (S14), vendor cell characterization for a model (S1), Peukert exponent (S7), learned Qmax and Ra (S3) | who characterizes each battery model, and how often |
| Compute location | embedded versus cloud split is in [[SOC and Health Estimation Literature Review]]; vendor gauges are embedded | whether a gateway or cloud link is always present |
| Interfaces | I2C, HDQ (gauge ICs); CANopen and J1939 (truck displays, S15, S19); Bluetooth (S6, S15) | the truck-side message set required |
| Standards | EN IEC 62485-6 has BMS and monitoring clauses (S24); no SOC accuracy standard found | read the standard; confirm UL and EN 1175-1 applicability |
| Intellectual property and supplier lock-in | Impedance Track and ModelGauge are vendor algorithms; Midtronics and Cadex methods are patented (S17 cites two US patents) | licence and supply terms (not in the sources) |
| Cost, lead time, availability | not in the sources | quotes |

### Questions for the owner (needed before scoring)

1. Which battery chemistries and voltage range must the design cover?
2. What is the target SOC accuracy, over which duty cycle and temperature range, and who verifies it?
3. Is SOH needed for replacement planning (a threshold such as 80%), for warranty evidence, or for charger control?
4. Is the estimator on the battery-side device (such as the BMID), in the charger, or in the cloud?

### Update 2026-10-18: owner answer to question 1 and white paper direction

The questions above are not edited. Recorded from the owner on 2026-10-18:

- **Scope:** all chemistries, up to 96 VDC.
- **Direction:** white papers on this topic are wanted for review and for discussing solutions; the owner will check the [[Document Wishlist]] for obtainable ones. Twelve rows were added there in round R73.
- **Not yet stated:** whether 96 VDC is the nominal pack voltage or the highest voltage the estimator must measure. This changes the input range. Derived from the C193 basis: 48 lead-acid cells at 2.30 to 2.35 V per cell give about 110 to 113 V at charge, and 30 LFP cells at 3.65 V give about 110 V, so a 96 V nominal scope needs inputs rated above 96 V. Open; see IB-327.
- **Not yet a list:** "all chemistries" has no named members. Chemistries with SOC or SOH sources in the vault are lead-acid (flooded, VRLA) and LFP; nickel-based and sodium-ion have none (IB-326).
- **Evidence gap found in the R73 search:** the papers located are mostly automotive lithium-ion reviews. One covers flooded lead-acid SOC (Khan et al. 2024, test voltages not stated in the page read) and one lead-acid SOH on stationary UPS batteries (Lazzarin and Barbi); none targets traction duty at 24 to 96 V (IB-325). Evidence for the lead-acid 80 percent rule is in conflict (C349).
- **Effect on C193:** the owner's range raises the gauge-limit conflict from 80 V packs to 96 V packs; the TI gauge range of 3 V to 65 V through external translation is unchanged.

Questions 2 to 4 are still open.

### Update 2026-10-18 (later): nominal versus maximum voltage answered

The text above is not edited, including the line that said the nominal-versus-maximum question was not yet stated. Recorded from the owner:

- **96 V is a nominal voltage**, the highest commonly seen. **80 V is a reasonable maximum for the majority** of packs.
- Derived from the C193 basis (2.30 to 2.35 V per cell for lead-acid at charge, 3.65 V per cell for LFP): an 80 V nominal pack is 40 lead-acid cells, about 92 to 94 V at charge, or 25 LFP cells, about 91 V. A 96 V nominal pack is 48 lead-acid cells, about 110 to 113 V at charge, or 30 LFP cells, about 110 V. Cell counts for other lithium chemistries were not worked out.
- Measurement inputs therefore have two sizing points: about 94 V at charge for the majority case and about 113 V at charge for the 96 V case. The 96 V case is the stretch case that exceeds the TI gauge range in C193 by a wider margin. Which of the two the first design must meet is a decision not yet taken; see IB-327.
- No source in the vault gives the share of the installed base at 96 V or at 80 V, so "majority" and "commonly seen" rest on the owner's statement only.

### Update 2026-10-18 (nine papers absorbed)

Nine of the R73 papers are now in the repo and read ([[SOC and SOH Methods Reference]], source keys S25 to S33). Effects on the criteria, with no scoring:

- **Chemistry coverage:** lead-acid has two new papers (S25 SOC, S26 SOH); LFP has one (S33). Nickel-based and sodium-ion still have none (IB-326). Seven of the nine are lithium-ion, EV or cell-level.
- **Voltage range:** nothing tested exceeds a 12 V battery (S25), a 2.5 Ah cell (S33) or a 192 V stationary string measured per 12 V battery (S26). No source validates an estimator at the 94 V or 113 V sizing points.
- **Compute location (question 4):** S26 is a worked example of an SOH measurement integrated in the charger; it is stationary UPS duty, three months of data, 16 batteries.
- **SOH threshold:** more second-hand statements of an 80 percent rule were found (C349); none is the standard.
- **Rest and relearn:** a fourth rest definition and a linear-versus-hysteresis disagreement on lead-acid OCV (C350).
- **Still true:** no source covers traction duty at 24 to 96 V (IB-325); the maker white-paper row remains wanted.

### Update 2026-10-18 (EU regulation text read)

- **Standards criterion:** Regulation (EU) 2023/1542 now has legal definitions of state of charge and state of health and a list of state-of-health parameters (Annex VII); no required accuracy was found. See [[SOC and SOH Specifications and Standards]] and C351.
- **Output the product may have to supply (EU market, owner has not confirmed any EU sales, IB-281):** passport use data for industrial batteries include periodically recorded state of charge, so a SOC estimate would feed a legal record if a battery maker chooses the device as its source. This is a hypothesis; the text puts the duty on the battery's market operator ([[EU Battery Passport and Battery Regulation Register]]).

## Sources

See the source keys in [[SOC and SOH Methods Reference]], [[SOC and SOH Product Landscape]] and [[SOC and SOH Specifications and Standards]].

## Aliases

- SOC SOH decision matrix inputs
- approach families
- estimator selection criteria
- SOC SOH owner questions

## Former ids
