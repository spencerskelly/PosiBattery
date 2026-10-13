---
type: Info
subtype:
id: INFO-90010
uid: 20261012234500000skellyspencer
status: Draft
tags:
  - research
  - literature-review
  - battery-monitoring
  - state-of-charge
  - state-of-health
  - embedded-cloud-allocation
describes: []
---

# SOC and Health Estimation Literature Review

## Definition

File-by-file review of the papers and patents supplied for the [[Estimate State of Charge]] and [[Estimate State of Health]] functions. For each file it records the estimation approach, the measurements that approach depends on, the compute it implies, and what the source says about where the software runs, so each approach can be modeled as a candidate implementation with its own dependencies and its own embedded (on the battery or truck) or cloud (fleet service) portions. Values are as the source states them. None is verified against a second source.

## Notes

**Evidence limit.** These are academic papers and one patent. None is a product document, and most never say where the estimator runs. Any embedded or cloud allocation drawn from them is an engineering inference by the note author, not a source claim. The vault convention for inferred allocations (an engineering-confidence statement on the Object) applies.

**Files supplied (commit e11b7953, 19 PDFs, 16 distinct by checksum).** Three files each have a byte-identical "(1)" copy: `Battery_studypaper`, `ISIE2014`, `Transformer-Based_Transfer_Learning_for_Battery_St`. Copies are kept in `Downloads/` and counted once. `Battery_state-of-charge_observer.pdf` is an image-only scan (US 8,922,217 B2, GM, Dec 30, 2014), read from the page image.

| # | File | What it is | Review status |
|---|---|---|---|
| 1 | `Research_on_the_State_of_Charge_Estimation_of_Elec` | Wang, Zhang, Hu, Batteries 2026, 12, 41: SOC of an LFP electric forklift pack with a Transformer | reviewed below |
| 2 | `Battery_Model_Identification_Approach_for_Electric` | da Silva et al., Energies 2021: battery model identification for an electric forklift (tested on a LiFePO4 cell) | reviewed below |
| 3 | `Battery_studypaper` | Alshaebi et al., ISERC 2017 (Raymond Corp co-author): forklift battery systems compared by simulation | pending |
| 4 | `DesignandFabricationofForklift` | Sequeira et al., JESA 2019: design and fabrication of a battery-operated forklift | pending, likely out of scope |
| 5 | `State-of-the-art_of_battery_state-of-charge_determ` | Pop et al., Meas. Sci. Technol. 2005: SOC determination review | pending |
| 6 | `Comparative_Analysis_of_Battery_State_of_Charge_Es` | Margal et al., E3S Web Conf. 2025: SOC methods compared | pending |
| 7 | `Battery_state-of-charge_observer` | US 8,922,217 B2, GM: robust SOC observer from open-circuit voltage | pending |
| 8 | `JOINT_FRACTIONAL-ORDER_MODELING_AND_KALMAN_FILTERI` | Lakhdari, Rev. Roum. Sci. Techn. 2026: fractional-order model with EKF for SOC | pending |
| 9 | `The_Estimation_of_Battery_State_of_Charge_using_Co` | Ismail et al., IJRTE 2024: SOC with a neural network | pending |
| 10 | `author_version` | Anthony et al., IMECE 2025: SOC from strain sensing and machine learning | pending |
| 11 | `126_Paper` | Yunusoglu et al.: SOH and RUL with an LLM framework, LTO cells | pending |
| 12 | `ISIE2014` | Sarikurt et al., ISIE 2014: analytical SOH method | pending |
| 13 | `Machine_Learning_Techniques_for_Battery_State_of_H` | Mbagaya et al.: SOH machine learning review | pending |
| 14 | `Transformer-Based_Transfer_Learning_for_Battery_St` | Giuliano et al., McMaster: Transformer transfer learning for SOH | pending |
| 15 | `main` | Ahmed et al., Huddersfield: lifecycle-aware SOH evaluation, LightGBM, edge-deployable | pending |
| 16 | `1_batteries` | Kafadarova et al., Batteries: surface temperature of cylindrical cells by thermal camera | pending, likely a sensing input rather than SOC or SOH |

### How the vault models an estimation approach

The approach chosen for Estimate State of Charge or Estimate State of Health decides which other functions it depends on. The vault already works this way for SOC: [[Voltage-Based State of Charge Estimator Firmware]] depends on [[Battery Voltage Acquisition Firmware]]; [[Coulomb Counting State of Charge Estimator Firmware]] on [[Battery Current Acquisition Firmware]]; [[Hybrid State of Charge Estimator Firmware]] on voltage, current and [[Battery Temperature Acquisition Firmware]]. The SOH candidates ([[Capacity-Retention State of Health Estimator]], [[Resistance-Trend State of Health Estimator]]) have no dependencies recorded yet, and [[Battery State of Health Analytics Service]] depends only on [[Raymond iBattery]]. Each source below is reduced to one row in the register that follows, so the candidate Objects and their dependencies can be added from it.

Embedded or cloud is a property of the candidate implementation, not of the function: an embedded candidate is firmware on the battery-mounted device or truck; a cloud candidate is a service that needs history from the fleet or pooled data. Where a source is silent on location, the row says so and any allocation is an engineering inference by the note author.

### Approach register (grows with each file)

| Source | Function | Approach | Depends on (measurements and functions) | Runs where, per the source | Vault candidate |
|---|---|---|---|---|---|
| 1 Wang 2026 | SOC | learned model (Improved Transformer 2) on Kalman-filtered, PCA-reduced inputs | pack voltage, system current, cell voltages (total, max, min, average), cumulative charge and discharge energy and capacity counters | not stated; training time only | none yet; needs a data-driven SOC candidate |
| 2 da Silva 2021 | SOC (model only; SOC estimator is future work) | equivalent-circuit model, nonlinear grey box, parameters fitted by nonlinear least squares, OCV-SOC curve | terminal voltage and current to fit parameters; nominal capacity; the OCV-SOC curve | parameter fitting offline on test data; the OCV-SOC curve is stated to be stored in the BMS microcontroller as a lookup table, polynomial or piecewise linear function | none yet; closest are the voltage-based and hybrid candidates |

### Source 1: Wang, Zhang, Hu (2026), "Research on the State of Charge Estimation of Electric Forklift Batteries Based on an Improved Transformer Model"

Source: Batteries 2026, 12, 41, MDPI, open access (CC BY), published 2026-01-23, <https://doi.org/10.3390/batteries12020041>. Peer-reviewed journal article, 14 pages. The PDF is `Research_on_the_State_of_Charge_Estimation_of_Elec.pdf` in the repo `Downloads` folder. Section numbers are the paper's own.

| Quantity or statement | Value | Basis and conditions | Section |
|---|---|---|---|
| Battery under test | LFP, 3.2 V 280 Ah cells, 24 series by 2 parallel = 76.8 V, 560 Ah, 43 kWh | forklift pack, 3.5-ton truck | 3 |
| Check of the pack figures | 24 x 3.2 = 76.8 V; 2 x 280 = 560 Ah; 76.8 x 560 = 43,008 Wh | derived by the note author, consistent with the paper | 3 |
| Run time | continuous operation for 6 h | same truck | 3 |
| Motor power | traction 8 kW, lift 12 kW; maximum discharge rate below 1 C | paper's estimate at full-load lifting | 3 |
| Data collection | all pack data collected by the "BMS collector"; a test bench with two temperature chambers and a high-rate cell tester provided cell-level boundary data | real-vehicle tests | 3 |
| Model inputs | 12 signals: pack inner voltage, pack outer voltage, system current, cumulative charging energy, cumulative discharging capacity, cumulative discharging energy, cumulative charging capacity, single charging energy, total cell voltage, maximum cell voltage, minimum cell voltage, average cell voltage | no temperature input listed in the 12, although cell temperature was recorded at the bench | 3 |
| Preprocessing | Kalman filter to suppress noise, then PCA to reduce 12 inputs to 3, 5 or 7 dimensions; 5 gave the lowest error | model trained on the reduced data | 2, 4.1 |
| Model structure | position embedding, convolution (kernel 3, 64 filters), two attention layers (4 heads, dimension 128), LSTM (50 hidden units), fully connected, regression output; "Improved Transformer 2" removes the LSTM layer | trained to minimize mean squared error | 2, 4.2 |
| Data split | 70% training, 30% test; how the split was made (random or in time order) is not stated | | 4.1 |
| Preprocessing results (MAE / RMSE) | Kalman 0.095 / 0.119; Kalman + PCA 0.070 / 0.086 | units not stated | Table 1 |
| Dimension results (MAE / RMSE) | 3: 0.082 / 0.101; 5: 0.070 / 0.086; 7: 0.087 / 0.108 | units not stated | Table 2 |
| Layer-removal results (MAE / RMSE / time) | no convolution 0.077 / 0.095 / 75 s; no LSTM 0.053 / 0.064 / 197 s; no attention 0.075 / 0.092 / 142 s; full 0.070 / 0.086 / 300 s | "computational time"; whether training or inference is not stated | Table 3 |
| Model comparison (MAE / RMSE / R2 / time) | LSTM 0.232 / 0.776 / 0.980110 / 45 s; CNN 0.188 / 0.320 / 0.996613 / 111 s; Improved Transformer 2 0.053 / 0.064 / 0.999864 / 197 s | same data | Table 4 |
| Checked reductions in the abstract | all eight stated percentages recompute from Tables 1, 2 and 4 (for example 0.082 to 0.070 is 14.63%) | derived by the note author | Abstract |

**What the paper says about where the software runs.** Nothing. There is no statement about the on-truck processor, memory, model size, inference time, sampling rate, or connection to a server. The 45 to 300 s figures are labeled "computational time" under a training-comparison heading, so they are read here as training time on an unspecified computer. Treat inference cost as unknown.

**What it implies for the allocation (engineering inference, not a source claim).**

| Stage | Allocation | Why |
|---|---|---|
| Acquire pack voltage, current, cell voltages, cumulative energy and capacity counters | embedded | these come from the BMS collector on the truck, so the estimator needs a BMS-class battery, not a voltage and current monitor alone |
| Kalman filter | embedded | a few operations per sample, used in the existing vault candidate list only as part of hybrid correction |
| PCA projection | embedded, parameters fixed after training | a matrix multiply of 12 inputs by a stored matrix; the matrix is learned offline |
| Transformer inference | undetermined | the paper gives no model size or latency; a 128-dimension attention model is plausible in the cloud or on a small accelerator, and unproven on a microcontroller |
| Model training and retraining | cloud (or offline workstation) | 75 to 300 s on whatever machine was used; needs pooled data to generalize |

**Gaps in the evidence.**

- MAE and RMSE units are not stated. If the values are fractions of full scale, 0.053 is 5.3% SOC; if percentage points, 0.053%. The two readings differ by a factor of 100, and the R2 of 0.9998 does not settle which. A reader should not use the error values until the units are known.
- The 30% test set is drawn from the same real-vehicle runs as the training set. If the split is random rather than in time order, adjacent samples leak across it and the very high R2 is optimistic. The paper does not say.
- One truck and one pack. No temperature sweep on the real truck, no aging, no second battery.
- Chemistry is LFP. The vault's current monitoring products are mostly lead-acid, where per-cell voltage is usually not available to a battery-mounted monitor, so the 12-input model does not transfer without that input set.
- The paper says Coulomb counting is unsuitable for forklifts because of long-term variable load, with no data to support it (see C142).

**Vault gaps this source exposes.**

- The vault has voltage-based, Coulomb counting and hybrid SOC firmware candidates and no data-driven (learned model) candidate. A learned estimator would be a fourth candidate, split into training in the cloud and inference at the battery or in the cloud.
- [[Estimate State of Charge]] has no Requirement linked, so no accuracy or latency target exists to compare this paper's numbers against.

### Source 2: da Silva, Dias, Araujo, Pellini, Lagana (2021), "Battery Model Identification Approach for Electric Forklift Application"

Source: Energies 2021, 14, 6221, MDPI, open access, published 2021-09-29, <https://doi.org/10.3390/en14196221>. Peer-reviewed journal article, 26 pages. The PDF is `Battery_Model_Identification_Approach_for_Electric.pdf` in the repo `Downloads` folder. Section numbers are the paper's own.

| Quantity or statement | Value | Basis and conditions | Section |
|---|---|---|---|
| Purpose | pick the battery model, optimizer and experiment design for parameter estimation; the best model is "intended for" SOC estimation on a forklift battery | no SOC estimator is built in this paper | Abstract, 1 |
| Test article | one cylindrical LiFePO4 cell: 6 Ah, 3.2 V nominal, 3.65 V upper and 2 V lower cut-off, 1C maximum continuous charge and discharge | cell data from the maker; not a forklift pack and not lead-acid | 3.1, Table 2 |
| Models compared | transfer function (TF), output error (OE), nonlinear Hammerstein-Wiener (NLHW), nonlinear grey box (NLGR) | four models, four optimizers, seven experiment designs | 3 |
| Fit to estimation data / validation data | TF 73.90% / 58.73%; OE 78.81% / 73%; NLHW 93.94% / 63.01%; NLGR 93.13% / 78.98% | NLGR picked for the best fit to validation data | Table 5 |
| Best optimizer | nonlinear least squares, trust-region reflective, "little computational effort" (no time or memory figure given) | for the NLGR model | 3.2, 5 |
| Best experiment | 1 min current pulses with 30 s rest, chosen as representative of forklift duty | more than 86% fit "in most validation data sets" | 5 |
| Prediction error | no more than 55 mV | NLGR, one-step-ahead | 5 |
| Parameter spread | R0 4.4 mOhm, R1 5.2 mOhm, C1 1488 F standard deviation; output variance 4.1 mV | chosen experiment | 5 |
| Why C1 is poorly determined | forklift duty "does not reach all the battery capacitance dynamics" | the paper's own explanation | 5 |
| OCV-SOC curve storage | lookup table: good accuracy, high microcontroller memory use; polynomial approximation: good accuracy with less memory but needs a suitable order; piecewise linear: ten breakpoints shown sufficient | "the microcontroller used to implement the BMS functions" | 2 |
| Hysteresis | Li-ion OCV-SOC differs between charge and discharge; the model has a one-state hysteresis form | LiFePO4 | 2 |
| Compute figures given | none: no sampling time, processor, memory figure, run time or fixed-point note | | |
| Stated next steps | develop a model giving enough data for accurate initial states; implement SOC estimation with the model in a BMS "to use in a real electric forklift" | future work | 5 |

**Approach and dependencies.** Parameter identification needs terminal voltage and current recorded through a designed pulse test, so that step is offline and belongs on a workstation or a cloud job. The stored OCV-SOC curve and the identified model parameters are what would be loaded into the battery-side device. The paper gives no real-time estimator, so the embedded part of this approach (running the model online) is only proposed.

**Engineering inference (not a source claim).** If this model were used for SOC online, the device would need terminal voltage, current and, because the paper's own variables list temperature, aging and capacity as influences, temperature and a capacity value, the same set as the hybrid SOC candidate. Identification and re-identification as the battery ages is the part that could sit in the cloud, if the device streams voltage and current pulses to it.

**Gaps in the evidence.**

- The abstract opens with lead-acid as the common forklift battery, but every experiment uses a LiFePO4 cell. No lead-acid data is presented, and the 6 Ah cell is far from a forklift pack (compare the 560 Ah pack in source 1).
- "Forklift" enters only through the shape of the current pulses. Figure 9 shows an actual forklift current profile; the paper does not state the truck, battery or voltage.
- No temperature variation in the tests; the abstract's "more than 80% of fit" is not the figure the conclusion gives (see C143).
- Fit percentages, not SOC error, are the result. The paper cannot yet say how accurate an SOC estimate from this model would be.

Related: [[Estimate State of Charge]], [[Estimate State of Health]], [[State of Charge Estimation Firmware]], [[Coulomb Counting State of Charge Estimator Firmware]], [[Hybrid State of Charge Estimator Firmware]], [[Battery State of Health Analytics Service]], [[Cloud Battery Data Upload Service]].

## Former ids

## Aliases

- SOC and SOH literature review
