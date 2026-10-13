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
describes:
  - "[[Model-Based State of Charge Estimator Firmware]]"
  - "[[Data-Driven State of Health Estimator Firmware]]"
  - "[[Learned State of Health Service]]"
  - "[[Segment Discharge Cycles]]"
  - "[[Capacity-Retention State of Health Estimator]]"
  - "[[Resistance-Trend State of Health Estimator]]"
---

# SOC and Health Estimation Literature Review

## Definition

File-by-file review of the papers and patents supplied for the [[Estimate State of Charge]] and [[Estimate State of Health]] functions. For each file it records the estimation approach, the measurements that approach depends on, the compute it implies, and what the source says about where the software runs, so each approach can be modeled as a candidate implementation with its own dependencies and its own embedded (on the battery or truck) or cloud (fleet service) portions. Values are as the source states them. None is verified against a second source.

## Notes

**Evidence limit.** These are academic papers and one patent. None is a product document, and most never say where the estimator runs. Any embedded or cloud allocation drawn from them is an engineering inference by the note author, not a source claim. The vault convention for inferred allocations (an engineering-confidence statement on the Object) applies.

**Chemistry scope.** The approach register is written as general estimation approaches, not lithium-only ones: each row names the measurements and functions it needs, and those do not depend on chemistry. The evidence behind the rows is almost entirely lithium. Accuracy figures, model sizes and test results in this note come from lithium cells and should not be read as results for lead-acid or any other chemistry. Per source, as stated in each paper:

| Chemistry in the evidence | Sources |
|---|---|
| Lithium iron phosphate (LFP) | 1 Wang; 2 da Silva |
| Lithium-ion 18650 cells and packs (NASA, CALCE, LG data sets) | 8 Lakhdari; 9 Ismail; 13 Mbagaya; 14 Giuliano (also Oxford NMC pouch cells); 15 Ahmed; 16 Kafadarova |
| Lithium polymer | 5 Margal; 12 Sarikurt |
| Lithium titanate (LTO) | 11 Yunusoglu |
| Cylindrical lithium-ion cell (graphite intercalation) | 10 Anthony |
| Several chemistries (review): lead, lithium, NiCd, NiMH and others, with some methods tagged per chemistry | 4 Pop |
| Lithium-ion preferred, other batteries by changing the model | 7 GM patent |
| Lead-acid and lithium compared as truck batteries, no estimator tested | 3 Alshaebi |

Where a chemistry difference already affects a row it is logged in the conflict register: OCV hysteresis differs between LiCoO2 and LiFePO4 (C147) and the rest time before an OCV reading differs between a lithium patent and a gel lead-acid datasheet (C150). Lead-acid evidence in this set is limited to Pop's review, Alshaebi's fleet data and the East Penn datasheet in [[Generic Reference Values]]. Each candidate created from this register therefore needs its parameters (OCV-SOC curve, resistance, fade curve, rest time) supplied for the chemistry it is applied to; that is a commissioning input, not something these sources provide.

**Files supplied (commit e11b7953, 19 PDFs, 16 distinct by checksum).** Three files each have a byte-identical "(1)" copy: `Battery_studypaper`, `ISIE2014`, `Transformer-Based_Transfer_Learning_for_Battery_St`. Copies are kept in `Downloads/` and counted once. `Battery_state-of-charge_observer.pdf` is an image-only scan (US 8,922,217 B2, GM, Dec 30, 2014), read from the page image.

| # | File | What it is | Review status |
|---|---|---|---|
| 1 | `Research_on_the_State_of_Charge_Estimation_of_Elec` | Wang, Zhang, Hu, Batteries 2026, 12, 41: SOC of an LFP electric forklift pack with a Transformer | reviewed below |
| 2 | `Battery_Model_Identification_Approach_for_Electric` | da Silva et al., Energies 2021: battery model identification for an electric forklift (tested on a LiFePO4 cell) | reviewed below |
| 3 | `Battery_studypaper` | Alshaebi et al., ISERC 2017 (Raymond Corp co-author): lead-acid vs lithium reach trucks, measured data plus simulation | reviewed below |
| 4 | `State-of-the-art_of_battery_state-of-charge_determ` | Pop et al., Meas. Sci. Technol. 2005: SOC determination review | reviewed below |
| 5 | `Comparative_Analysis_of_Battery_State_of_Charge_Es` | Margal et al., E3S Web Conf. 2025: SOC methods compared | reviewed below |
| 6 | `DesignandFabricationofForklift` | Sequeira et al., JESA 2019: design and fabrication of a battery-operated forklift | skipped for now at the user's request (forklift design and fabrication, not SOC or SOH estimation) |
| 7 | `Battery_state-of-charge_observer` | US 8,922,217 B2, GM: robust SOC observer from open-circuit voltage | reviewed below |
| 8 | `JOINT_FRACTIONAL-ORDER_MODELING_AND_KALMAN_FILTERI` | Lakhdari, Rev. Roum. Sci. Techn. 2026: fractional-order model with EKF for SOC | reviewed below |
| 9 | `The_Estimation_of_Battery_State_of_Charge_using_Co` | Ismail et al., IJRTE 2024: SOC with a small feedforward neural network ("Corny") | reviewed below, low weight |
| 10 | `author_version` | Anthony et al., IMECE 2025: SOC from cell strain sensing and a small neural network | reviewed below |
| 11 | `126_Paper` | Yunusoglu et al.: SOH and RUL with an LLM framework, LTO cells | reviewed below, results contradict themselves |
| 12 | `ISIE2014` | Sarikurt et al., ISIE 2014: analytical SOH method | reviewed below, single 11 Ah cell, parameter labels and one table value inconsistent |
| 13 | `Machine_Learning_Techniques_for_Battery_State_of_H` | Mbagaya et al., WEVJ 2025: SOH machine learning review with a four-model test on NASA cells | reviewed below, secondary source |
| 14 | `Transformer-Based_Transfer_Learning_for_Battery_St` | Giuliano et al., Energies 2025: Transformer transfer learning for SOH (NASA to Oxford cells) | reviewed below, test design weaknesses |
| 15 | `main` | Ahmed, Aagela, Geth, Iqbal (University of Huddersfield): lifecycle-aware SOH evaluation, LightGBM baseline, 10k-parameter CNN preview | reviewed below, preprint-style, no on-target test |
| 16 | `1_batteries` | Kafadarova et al., Batteries 2023: surface temperature of cylindrical cells by thermal camera | reviewed below, a laboratory temperature measurement method, not an SOC or SOH estimator |

### How the vault models an estimation approach

The approach chosen for Estimate State of Charge or Estimate State of Health decides which other functions it depends on. The vault already works this way for SOC: [[Voltage-Based State of Charge Estimator Firmware]] depends on [[Battery Voltage Acquisition Firmware]]; [[Coulomb Counting State of Charge Estimator Firmware]] on [[Battery Current Acquisition Firmware]]; [[Hybrid State of Charge Estimator Firmware]] on voltage, current and [[Battery Temperature Acquisition Firmware]]. The SOH candidates ([[Capacity-Retention State of Health Estimator]], [[Resistance-Trend State of Health Estimator]]) have no dependencies recorded yet, and [[Battery State of Health Analytics Service]] depends only on [[Raymond iBattery]]. Each source below is reduced to one row in the register that follows, so the candidate Objects and their dependencies can be added from it.

Embedded or cloud is a property of the candidate implementation, not of the function: an embedded candidate is firmware on the battery-mounted device or truck; a cloud candidate is a service that needs history from the fleet or pooled data. Where a source is silent on location, the row says so and any allocation is an engineering inference by the note author.

### Approach register (grows with each file)

| Source | Function | Approach | Depends on (measurements and functions) | Runs where, per the source | Vault candidate |
|---|---|---|---|---|---|
| 1 Wang 2026 | SOC | learned model (Improved Transformer 2) on Kalman-filtered, PCA-reduced inputs | pack voltage, system current, cell voltages (total, max, min, average), cumulative charge and discharge energy and capacity counters | not stated; training time only | none yet; needs a data-driven SOC candidate |
| 2 da Silva 2021 | SOC (model only; SOC estimator is future work) | equivalent-circuit model, nonlinear grey box, parameters fitted by nonlinear least squares, OCV-SOC curve | terminal voltage and current to fit parameters; nominal capacity; the OCV-SOC curve | parameter fitting offline on test data; the OCV-SOC curve is stated to be stored in the BMS microcontroller as a lookup table, polynomial or piecewise linear function | none yet; closest are the voltage-based and hybrid candidates |
| 3 Alshaebi 2017 | SOC (simulation only) and usage-history capacity | SOC read from the battery voltage curve while the truck is idle; delivered Ah per discharge cycle compared with rated Ah ("practical capacity") | terminal voltage and current sampled at 10 Hz; truck travel and lift speed; rated capacity | analysis offline in a statistics package and a Demo3D simulation; the 10 Hz logging device is on the truck | SOC: closest is the voltage-based candidate; usage history: [[Amp-Hour Accumulator Firmware]], [[Log Battery Events and Usage]], cloud side [[Battery State of Health Analytics Service]] |
| 4 Pop 2005 (review) | SOC | loaded-voltage timing: time elapsed since the loaded voltage fell below a set value (Curtis traction-battery gauge, 1963), with a discharge-rate compensation | loaded terminal voltage, elapsed time, discharge rate | not stated; a gauge in the vehicle | closest: voltage-based candidate, in its loaded (not rest) form |
| 4 Pop 2005 | SOC | EMF or open-circuit voltage method, stored as a lookup table, piecewise linear function or fitted function | terminal voltage after rest or extrapolated to zero current; temperature | on the battery-side device; the review notes lookup tables cost memory and piecewise linear needs only interval limits | voltage-based candidate |
| 4 Pop 2005 | SOC | book-keeping: Coulomb counting with compensation for discharge efficiency, self-discharge and capacity loss | current through a shunt (accuracy and offset critical), voltage, temperature, cell characterization data in EEPROM, cycle history, register set (SOC counter, charge accumulator, discharge accumulator) | dedicated gauge IC with its own processor and EEPROM; the host reads the result over a serial bus | Coulomb counting and hybrid candidates, [[Amp-Hour Accumulator Firmware]] |
| 4 Pop 2005 | SOC and SOH | adaptive: Kalman or extended Kalman filter on a battery model, neural network, fuzzy logic | voltage, current, temperature (impedance data for fuzzy); the EKF can carry series resistance as a state, which gives a health indicator; a neural network needs training data | the review does not say; the EKF is sequential, needing only the previous sample; one neural network was trained on 2,860 discharge curves | no candidate; extends hybrid |
| 4 Pop 2005 | SOH | internal resistance from a current step; impedance spectroscopy; capacity tracked against initial capacity | current step and voltage response; small-signal ac excitation not above 10 mV; capacity measured at full charge or discharge | impedance sweeps judged impractical for SOC in a portable device but used for health | [[Resistance-Trend State of Health Estimator]], [[Capacity-Retention State of Health Estimator]] |
| 5 Margal 2025 | SOC | extended Kalman filter on a two-RC (dual polarization) Thevenin model; SOC-dependent parameters from fifth-order polynomials | battery current and terminal voltage; six polynomial parameter curves (R0, R1, C1, R2, C2, open-circuit voltage; 36 coefficients); noise covariances Q and R; initial state | simulation only (Matlab); not stated | hybrid-type candidate (voltage and current), no model-based candidate yet |
| 5 Margal 2025 | SOC | adaptive Luenberger observer, gain adapted by stochastic gradient | same model, current and voltage; learning rate | simulation only | same |
| 5 Margal 2025 | SOC | NARX recurrent neural network: 5 hidden units, 1 hidden layer, delay 2, Adam optimizer, 1,000 training epochs | past and present current, past SOC and voltage outputs fed back; needs data covering all operating points (the paper's own caveat) | training offline; the network is small enough to suggest on-device inference, but no inference cost is given | none; data-driven candidate |
| 7 GM patent US 8,922,217 | SOC | robust observer (minimizes an upper bound on the estimation error covariance) estimating open-circuit voltage while the battery is loaded, on a two-RC model with bounded, time-varying parameters; SOC then read from an open-circuit-voltage table that depends on temperature | terminal voltage, terminal current and temperature at every time step; nominal model matrices and parameter-variation bounds; tolerance levels; the voltage-to-SOC table | the vehicle's control module (processing unit); output goes to a display or an electronic control unit | no model-based candidate; closest is the hybrid candidate |
| 8 Lakhdari 2026 | SOC, with resistance as a health indicator | joint extended Kalman filter on a fractional-order equivalent circuit; the filter state holds SOC, a short voltage history (memory length 4), ohmic resistance and leakage resistance | current and terminal voltage at 1 Hz; open-circuit-voltage table by SOC (piecewise linear); nominal capacity; offline-identified polarization parameters (R1, Q1, alpha) and memory length; noise covariances | identification offline on a bench; the filter is described as real-time but run in simulation or post-processing; embedded hardware implementation is listed as future work | none; extends the voltage-and-current hybrid and, through the resistance state, the [[Resistance-Trend State of Health Estimator]] |
| 9 Ismail 2024 | SOC | small feedforward neural network ("Corny"): 5 inputs, two 55-unit layers, 1 output | voltage, current, temperature, and 500-second averages of voltage and current (5 channels); training data from a public data set | training offline; no deployment statement for this network | none; same data-driven candidate as Wang and Margal |
| 10 Anthony 2025 | SOC (discharge only) | small multilayer perceptron on windowed features of cell hoop strain (maximum, minimum, standard deviation, slope, mean) | a strain gauge bonded to the cell casing (plus a thermocouple on the cell); strain sampled at 1 Hz; a capacity-derived SOC label for training | training offline; no deployment statement | none; needs a strain-measurement function and element that the vault does not have |
| 11 Yunusoglu | SOH | capacity ratio: measured capacity of each cycle over nominal capacity, end of life at 80% | charge and discharge capacity per cycle (Ah accumulation over a full cycle), nominal capacity, cycle count | not stated; simple enough for the device | [[Capacity-Retention State of Health Estimator]] (no dependency recorded yet; this adds Accumulate Amp-Hours and a cycle boundary) |
| 11 Yunusoglu | SOH trend and remaining useful life | quadratic fit of SOH against cycle number, solved for the cycle where SOH reaches 80% | the history of per-cycle SOH values | not stated; needs a history store, suits a service | [[Battery Replacement Forecasting Service]] |
| 11 Yunusoglu | SOH features | differential voltage analysis: capacity change per volt, tracked in a voltage window | high-resolution voltage and charge over a controlled charge or discharge | not stated | none; needs a controlled-cycle condition |
| 11 Yunusoglu | SOH (claimed) | BERT-based regression on text-serialized data rows, 109 million parameters | voltage, current, capacity (and temperature) rows turned into text | the paper proposes edge inference with cloud fine-tuning, and reports no edge test | none; evidence does not support allocation |
| 12 Sarikurt 2014 | cycle number (input to SOH) | fit y = a/(x+b) to a voltage dip of the cell's response to a fixed urban driving current profile (ECE 15); two points on a dip give a and b; two fitted polynomials map a or b to cycle number | cell voltage and time during a known load profile; a pre-built equivalent-circuit model that generated the reference curves | not stated; two-point arithmetic, embedded-sized | none; needs a repeatable load profile, which a forklift does not have |
| 12 Sarikurt 2014 | SOH | percent capacity read from the manufacturer's capacity-versus-cycle curve (8th order polynomial), via the estimated cycle number; SoH = (capacity% - 80) x 5 | estimated cycle number; manufacturer fade curve | not stated; a polynomial lookup, embedded-sized | [[Capacity-Retention State of Health Estimator]] (a cycle-count variant, no measured capacity); dependency on cycle count from [[Log Battery Events and Usage]] |
| 13 Mbagaya 2025 | SOH | SVR or random forest on summary statistics (mean, standard deviation, percentiles, voltage slopes, correlations) of a resampled discharge cycle | full constant-current discharge of voltage, current and temperature, resampled to 120 points, plus derivatives; cycle labels from capacity | training offline on a workstation (SVR 5.3 s, RF 26 s); the paper says these suit resource-constrained BMS hardware, no embedded test | none; needs a full controlled discharge, which opportunity-charged forklifts rarely give |
| 13 Mbagaya 2025 | SOH | CNN or bidirectional LSTM on the same 6 x 120 sequences | same as above | training offline (CNN 58 s, LSTM 202 s); the paper says LSTM is hard to run on embedded BMS hardware and lists pruning, quantisation, distillation or offline/online split as options | none; no data-driven SOH candidate in the vault yet |
| 13 Mbagaya 2025 (reported from Chen 2024) | SOH | VMD plus Transformer in an edge-cloud collaborative framework | not given in this review | edge and cloud, per the cited title; split not described here | [[Battery State of Health Analytics Service]] (cloud side); read the primary paper before relying on it |
| 14 Giuliano 2025 | SOH | Transformer (117,161 parameters) on a 300-step window of voltage, current, temperature, relative time, cycle number and the previous cycle's capacity; predicts the next window's capacity; output smoothed by a Savitzky-Golay filter | voltage, current and temperature acquisition; cycle counter; previous-cycle capacity from Coulomb counting (Accumulate Amp-Hours); capacity labels for training | pre-training and fine-tuning offline; the paper says the model is "poorly suited for direct, real-time deployment" on an embedded BMS and that LSTM or ANN are more pragmatic there; no inference test | none; new data-driven candidate if used; inference would sit off the pack |
| 14 Giuliano 2025 | SOH (adaptation to a new cell type) | transfer learning: train on NASA cells for 5 epochs, fine-tune one epoch on one full-life cell of the target chemistry | a complete labeled life of at least one target cell; the pre-trained weights | cloud-side training workflow; weights could then be sent to devices | [[Battery State of Health Analytics Service]] (cloud side); needs a model and data store that the vault does not have |
| 14 Giuliano 2025 | capacity of previous cycle (feature) | Coulomb counting, eta times integral of current | current and time | not stated; counter arithmetic, embedded-sized | [[Coulomb Counting State of Charge Estimator Firmware]] and [[Amp-Hour Accumulator Firmware]] |
| 15 Ahmed | SOH | LightGBM regression on 61 features per discharge cycle (statistics, dwell times, curve-shape, dV/dt) from voltage, current and temperature; leave-one-battery-out testing | a complete discharge cycle of voltage, current and temperature held in memory, a cycle segmenter, a first-cycle capacity reference for the label | the paper wants SOH "on or near the asset" but argues its own model is "structurally non-deployable" on a Cortex-M class target; no port attempted | none; new data-driven candidate; needs a cycle buffer and feature extraction |
| 15 Ahmed | SOH | 1D CNN with depthwise-separable convolutions on a 3 x 200 resampled discharge cycle; 10,169 parameters, about 40 kB float32 or 10 kB INT8 | same cycle buffer, linear resampling to 200 points and per-channel normalisation | claimed quantisable to microcontroller scale (TFLM, CMSIS-NN); latency and energy not measured | none; the only source here sized for a microcontroller, claim untested |
| 15 Ahmed | SOH band (maintenance action) | map the SOH estimate to Good (90% or more), Fair (80 to 90), Poor (70 to 80), Critical (below 70) | the SOH estimate | not stated; a threshold table | [[Battery Replacement Forecasting Service]] and [[Battery State of Health Analytics Service]]; thresholds are configurable, not standard |
| 16 Kafadarova 2023 | temperature input (not an estimator) | infrared thermography of a rotating cylindrical cell, view-angle correction, 3D surface temperature map and average surface temperature | thermal camera, a motor-driven rotating fixture, thermographic paint, electronic load and voltmeter; offline Python image processing | laboratory only; the authors say the method is "for testing batteries in laboratory conditions"; no embedded or cloud split | none; it is a characterization method, not a candidate for [[Battery Temperature Acquisition Firmware]]; could inform where thermistors go |

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

### Source 3: Alshaebi, Dauod, Weiss, Yoon (2017), "Evaluation of Different Forklift Battery Systems Using Statistical Analysis and Discrete Event Simulation"

Source: Proceedings of the 2017 Industrial and Systems Engineering Conference (Coperich, Cudney, Nembhard, eds.), Binghamton University with a co-author from The Raymond Corporation; 6 pages. Conference paper, no DOI printed. The PDF is `Battery_studypaper.pdf` in the repo `Downloads` folder (a byte-identical `(1)` copy is also there). Section numbers are the paper's own.

| Quantity or statement | Value | Basis and conditions | Section |
|---|---|---|---|
| Test setup | two identical reach trucks in a cold warehouse: one with a new 700 Ah lithium-ion battery, one with a 1240 Ah lead-acid battery; five weeks of data | the intro prints "1240 lead acid" without a unit; section 3.1 says 1240 Ah | 1, 3.1 |
| Logged signals | voltage, current, reach, retract, travel speed (mph), lift speed (ft/s), timestamp | instrumented battery and truck | 1, 3.1, Table 1 |
| Sample rate | 10 samples per second | | 3.1 |
| Sample voltage readings | 39.37 V and 39.39 V (under load); nominal pack voltage not stated | Table 1 | 3.1 |
| Cold storage temperature | not stated; no temperature signal is in the logged list | | 1 |
| Discharge cycle, lithium | the period of consuming 80% of nominal capacity | author assumption | 3.1 |
| Discharge cycle, lead-acid | from fully charged until the battery is changed | author assumption | 3.1 |
| Internal resistance | assumed constant for both batteries | simplifies energy-waste calculation | 3.1 |
| Productivity | lead-acid 3,991 pallet moves in 221 h = 18.1 per hour; lithium 4,008 in 190 h = 21.1 per hour | derived check: 3,991 / 221 = 18.06; 4,008 / 190 = 21.09 | 4.1, Table 2 |
| Workload difference | travel and lift distances differ between the trucks (p = 0.001, 95% confidence), so productivity is not a like-for-like comparison | the paper's own caveat | 4.1 |
| Delivered energy per cycle | about 500 Ah on average for both batteries | 32 discharge cycles in total; Figure 5 shows roughly 30 points per battery, range about 230 to 740 Ah for lead-acid | 4.2, Fig 5 |
| Share of rated capacity used | lithium about 70%; lead-acid "around 45%" in section 4.2, 46% in Table 3 and the conclusion | see C144 | 4.2, 5 |
| Heat | lithium generates half the heat of lead-acid, attributed to lower internal resistance | no temperature or heat measurement is in the logged signals | 4.2 |
| Battery changes | lead-acid replaced at 20% SOC; replacement time uniform 8 to 20 min in the simulation; 1.5 h per truck per week saved with lithium (measured) | Figure 7 shows 27 replacement events at about 6 to 21 min | 3.3, 4.3 |
| SOC method in the model | state of charge "estimated according to the voltage curve when the truck is idle" | simulation input only, no accuracy given | 3.3 |
| Simulation | 20 trucks, six shifts (two days), 10 replications, Demo3D | | 3.3, 4.4 |
| Simulation outputs | lead-acid / lithium: energy efficiency 46% / 73%; productivity 18.5 / 21 per truck-hour; downtime 26 / 0 h per truck per week (Table 3); "around 25 labor hours" a week for 20 trucks in the text | see C145 | 4.4, Table 3 |
| Cost | lithium is "more expensive"; no figure; left to future work | | 5 |

**Approach and dependencies.** This paper does not propose an estimator. Two things in it bear on the functions:

- SOC is read from a voltage curve when the truck is idle. That is a rest-voltage method that depends only on terminal voltage and an idle-state flag, with no current integration. It matches the voltage-based candidate and shows its limit: it only works when the truck is idle.
- "Practical capacity" (delivered Ah in a cycle divided by rated Ah) is a usage-history metric. It depends on integrating current over each discharge cycle ([[Accumulate Amp-Hours]]) and on a rule for where a cycle starts and ends ([[Log Battery Events and Usage]]). The two cycle rules in this paper differ by chemistry (see C140), so any shared cycle counter would need one rule.

**Engineering inference (not a source claim).** The 10 Hz logging and cycle segmentation run on the battery or truck device. The cross-truck, cross-chemistry comparison, the five-week statistics and the simulation are fleet-level analysis that fits the cloud side, where the vault already models [[Battery State of Health Analytics Service]].

**Gaps in the evidence.**

- One truck of each chemistry for five weeks; the authors state the workloads differ significantly.
- The heat claim has no supporting measurement in the stated signals.
- No SOH is measured. Rated-capacity use is a utilization figure, not a health figure, and the lead-acid battery's age is not given.
- Raymond is a co-author, so the lead-acid truck and logger may be Raymond equipment, but the paper does not name the logging device.

### Source 4: Pop, Bergveld, Notten, Regtien (2005), "State-of-the-art of battery state-of-charge determination"

Source: Measurement Science and Technology 16 (2005) R93 to R110, IOP Publishing, doi:10.1088/0957-0233/16/12/R01, published 2005-10-31. Peer-reviewed review article, 18 pages, authors at University of Twente and Philips Research. The PDF is `State-of-the-art_of_battery_state-of-charge_determ.pdf` in the repo `Downloads` folder. Page numbers are the journal's R-numbers; section numbers are the paper's own. Everything below about other works (patents, other papers) is as the review reports it, not checked.

**Scope.** Portable electronics (phones, notebooks, power tools) and NiCd, NiMH and Li-ion batteries. Lead-acid appears in the history and in a few method rows, forklift traction batteries not at all. The review's worked examples are a Sony Li-ion cell (US18500G3, LiCoO2).

| Quantity or statement | Value | Basis and conditions | Section, page |
|---|---|---|---|
| Method families | direct measurement (voltage, EMF, impedance, relaxation), book-keeping (current integration), adaptive systems (Kalman filter, neural network, fuzzy logic) built on one or both | | 5, R101 |
| Voltage-only SOC | "can be very misleading": the voltage-to-charge relation varies greatly with temperature and discharge rate; cheaper and lighter on the processor than Coulomb counting | Li-ion; correcting for rate and temperature makes it costlier than Coulomb counting | 5.1.1, R101 |
| EMF by relaxation | the battery voltage relaxes to the EMF after current stops; this may take a long time when nearly empty, cold, or after a high discharge current | Li-ion | 5.1.2, R102 |
| EMF versus SOC | the relation does not change during cycling if SOC is expressed in relative capacity; temperature dependence small except near fully discharged or fully charged | Li-ion (LiCoO2) | 5.1.2, R102 |
| EMF curve in a table | 11 voltage intervals from 4.24 V (100%) down to 2.5 V (0%), for example 4.08 to 4.24 V = 85 to 100% and 3.8 to 3.88 V = 22 to 58.4% | Sony US18500G3 at 25 C; interpolation by equation 5.1 | 5.1.2, Table 3, R102 |
| Impedance excitation | amplitude not above about 10 mV to stay linear; high-capacity cells need several amps of ac current | any cell | 5.1.3, R103 |
| Lead-acid impedance shape | inductive above 100 Hz; high-frequency resistance in the milliohm range; small loop 0.1 to 100 Hz; large loop below 0.1 Hz | large-capacity lead-acid cell | 5.1.3, Fig 10, R103 |
| Impedance for SOC | not practical in a portable device because a frequency sweep is needed; impedance depends more on temperature than on SOC; used mainly for health | | 5.1.3, R104 |
| Health from resistance | wear-out shows as rising internal resistance; a current step can test whether the battery should be replaced | | 5.1.3, R104 |
| Coulomb counting accuracy | depends on current-measurement accuracy over the full range in both directions; shunt voltage drop is very small at large currents; offset errors accumulate | shunt-based measurement | 5.2, R104 |
| Book-keeping compensations | discharge efficiency, self-discharge (not seen by a Coulomb counter because no net current flows), capacity loss; the maximum capacity is usually updated from a voltage measurement | Li-ion | 5.2, R104 |
| Book-keeping registers | current register, SOC counter (reset at low-battery indication), charge accumulator and discharge accumulator over battery life | mobile-phone example; accumulators give end-of-life information | 5.2, R105 |
| Gauge IC self-discharge counter | one count per hour at 25 C, doubling about every 10 C up to 60 C and halving every 10 C below 25 C down to 0 C | Texas Instruments gauge ICs as described | 6, R107 |
| Cell characterization data | full, standby-empty and active-empty capacity measured per temperature (0 to 40 C) and stored in the gauge IC EEPROM; data collected on assembled packs rather than cells | Maxim-style gauge; example full capacity 554 to 588 mAh | 6, Table 6, R108 |
| EKF verdict | "EKF provides the best solution for the long-term SoC estimation" | reported from Plett (ref 51), LiPB hybrid-vehicle cells | 5.3, R105 |
| Neural network result | mean error about 3%; trained on 2,860 discharge curves (260 cycles of 11 batteries) | reported from Gerard et al. (ref 38), remaining-time prediction | 5.3, R106 |
| Fuzzy logic result | maximum error +/-5% on a limited data set | reported from Salkind et al. (ref 39), Li-SO2 and NiMH | 5.3, R106 |
| Reported Coulomb-plus-OCV accuracy | 99% accuracy (1% error) for charge detection "but at a high cost" | reported from ref 37 about Aylor's lead-acid method (ref 32) | 3, R98 |
| Loaded-voltage gauge example | discharged from 24.25 V for 3 min lowers remaining capacity from 100% to 90% | Curtis traction-battery gauge, 1963 | 3 |
| Table 4 method summary | Coulomb counting: all systems, accurate with enough recalibration points and good current measurement, sensitive to parasitic reactions. OCV: lead, lithium, zinc-bromine, needs long rest. EMF: lead, lithium, needs long rest. Impedance spectroscopy: all systems, gives health information, temperature sensitive and costly. DC internal resistance: lead, NiCd, short-interval accuracy only. Neural network: all systems, needs training data of a similar battery. Kalman filter: all systems, hard to implement for nonlinearities | read from the page image | 5.4, Table 4, R107 |
| Commercial gauges | none of the commercial gauge ICs reviewed is adaptive, so none copes with spread, wide temperature and current ranges and ageing | 2005 survey | 6, 7, R108 to R109 |

**What it says about where the software runs.** Embedded throughout: the gauge IC or processor on the battery pack runs the algorithm and the host reads the result over a serial bus (I2C or one-wire). Cell characterization data is stored in the pack. The review says nothing about a server or any off-device processing; the neural-network example trains offline and then adapts, without saying where.

**What it adds to the allocation (engineering inference, not a source claim).** The review supports a split that the vault can use as a default for any approach:

- Acquisition (voltage, current, temperature) and the fast accumulation loop are embedded.
- Per-pack constants (characterization table, capacity) are produced in a lab or factory step and loaded into the device.
- Learned parameters (neural weights, Kalman filter model parameters) are the part that could be produced elsewhere and updated.

**Gaps and cross-checks.**

- Written in 2005 about consumer Li-ion packs; none of the numeric results is for a forklift battery, and the review's lead-acid coverage is brief.
- The review's examples use LiCoO2. The da Silva paper (source 2) finds hysteresis in the OCV-SOC relation of a LiFePO4 cell, which the review does not discuss; see C147.
- The review's three ways to store the EMF curve (lookup table, piecewise linear function, fitted function) match the three ways source 2 says it tested for the OCV-SOC curve in the BMS microcontroller.
- The review's EKF and book-keeping text does not say Coulomb counting is unsuitable for variable load; see the extension to C142.
- The review is not the primary source for any figure marked "reported from"; those should be traced to the cited works before the vault relies on them.

### Source 5: Margal, El Daoudi, Khallouq, Karama (2025), "Comparative Analysis of Battery State of Charge Estimation Methods"

Source: E3S Web of Conferences 601, 00033 (2025), ICEGC'2024, EDP Sciences, open access (CC BY 4.0), doi:10.1051/e3sconf/202560100033; Cadi Ayyad University, Morocco; 11 pages. Conference paper. The PDF is `Comparative_Analysis_of_Battery_State_of_Charge_Es.pdf` in the repo `Downloads` folder. Section numbers are the paper's own.

| Quantity or statement | Value | Basis and conditions | Section |
|---|---|---|---|
| Methods compared | extended Kalman filter (EKF), adaptive Luenberger observer (ALO), NARX recurrent neural network | simulation on a Thevenin dual-polarization model; Coulomb counting used as the reference | 1, 3, 4 |
| Test cell | Turnigy Graphene 5000 mAh 3S 65C Li-polymer; Table 1: 5000 mAh, 3.7 V nominal, 4.2 V and 2.8 V cut-offs; voltage plot spans about 3.9 to 4.15 V | data from the cited work (ref 18) at a battery tester; "3S" conflicts with the single-cell voltages, see C149 | 2.2, 4 |
| Test cycle | LA92 driving schedule (light-vehicle dynamometer), 7,478 s = 2.08 h; current swings about +5 A to -15 A | passenger-vehicle cycle, not forklift duty | 4 |
| Parameter identification | hybrid pulse power characterization; fifth-order polynomial of SOC for each of R0, R1, C1, R2, C2 and open-circuit voltage | 36 coefficients (Table 2) | 2.2 |
| Coulombic efficiency | 0.9 to 1, depending on temperature and charge rate | stated range | 2.1 |
| NARX settings | learning rate 0.001, 5 hidden units, 1 hidden layer, ReLU and tanh activations, delay 2, Adam, mean squared error loss, 1,000 epochs | Table 3 | 3.3 |
| SOC error, abstract | NARX RMSE 0.33%, EKF 5.34%, ALO 5.94% | abstract | Abstract |
| SOC error, Table 5 | RMSE: KF 5.349e-1, ALO 5.948e-1, NARX 3.3288e-2; MAE: 4.4996e-1, 4.9046e-1, 2.3208e-2; MSE: 2.8612e-1, 3.5379e-1, 1.1081e-3; units not stated | Table 5; MSE and RMSE are consistent (the square root of 2.8612e-1 is 0.5349) | 4 |
| Voltage error, Table 4 | MSE: KF 1.4377e-6, ALO 2.6794e-6, NARX 6.5442e-7; MAE 7.4787e-4, 8.9792e-4, 4.8831e-4; the RMSE row repeats the Table 5 SOC RMSE values | the square root of 1.4377e-6 is 1.2e-3, not 5.349e-1; see C149 | 4 |
| Convergence | EKF and ALO converge more slowly than NARX but without oscillation; NARX oscillates at the start; no times given | Figure 8 | 4 |
| Claimed limits | direct methods: open-circuit voltage needs long rest and depends on temperature and hysteresis; Coulomb counting is inaccurate from sensor noise; EIS is precise but costly. Kalman filters need noise characterization and are sensitive to initial conditions. Data-driven methods need heavy compute and training data | introduction, no data | 1 |
| CC reference caveat | CC "is not suitable for use in real-life conditions" because it needs the exact initial SOC; it is used here as the ideal reference | the reference for all SOC errors is a Coulomb-counted trajectory | 4 |

**Approach and dependencies.** All three methods need only current and terminal voltage as measurements; temperature is not an input, and the parameter curves are for one test temperature (not stated). The model-based pair needs a stored parameter set (36 polynomial coefficients) and tuned noise or gain settings. The NARX needs only a small network and past values, but a training set that covers the operating range.

**Engineering inference (not a source claim).** The NARX at 5 hidden units and delay 2 is small enough that inference on a battery-mounted microcontroller looks plausible, but the paper gives no memory, time or fixed-point figure. Training would be offline or in the cloud. The EKF and observer run per sample and are embedded by nature; their parameter set would be loaded at commissioning.

**Gaps in the evidence.**

- Errors are measured against a Coulomb-counted SOC, not a true SOC. The NARX is also fed its own previous SOC outputs. Whether training and test data come from the same cycle is not stated. The 0.33% is therefore a measure of agreement with Coulomb counting on one cycle, not independent accuracy.
- The abstract's RMSE figures are ten times Table 5's (see C148).
- One cell, one cycle, no temperature or aging variation; a passenger-vehicle cycle, not forklift duty.
- ALO is expanded as "Adaptive Luenberger Observer" in the abstract and "Ant Lion Optimizer" in the discussion (see C149).

### Source 7: Mao and Tang, GM Global Technology Operations, US 8,922,217 B2, "Battery State-of-Charge Observer"

Source: United States patent, application 13/466,394 filed 2012-05-08, published as US 2013/0300190 A1 on 2013-11-14, granted 2014-12-30; inventors Xiaofeng Mao and Xidong Tang; assignee GM Global Technology Operations LLC; 20 claims, 2 drawing sheets; classes G01N 27/416 and G01R 31/36 (CPC G01R 31/3648). The PDF is `Battery_state-of-charge_observer.pdf` in the repo `Downloads` folder; it is an image-only scan, read by optical character recognition and checked against page 1 as an image, so some equations and symbols are not legible. Patent text states what the applicant claims and describes. It reports no test data. This note records technical content only and is not a freedom-to-operate or validity assessment.

| Quantity or statement | Value | Basis and conditions | Location |
|---|---|---|---|
| Problem addressed | open-circuit voltage normally needs a rest period; existing online estimators ignore parameter uncertainty (resistances, capacitances) that changes with age and temperature | vehicle batteries | Background |
| Rest time for an accurate open-circuit voltage | "typically about 24 hours" after charging stops | vehicle battery; surface charge on the plates gives false voltage readings until it dissipates | Detailed description |
| Measurements used | terminal voltage, terminal current, battery temperature, each at a plurality of time steps | | Claim 1 |
| Model | two-RC pair equivalent circuit with an ohmic resistance; parameters (R, double-layer and diffusion resistances and capacitances) are time-varying and "bounded in practice" | lithium-ion preferred; other batteries by changing the model | FIG. 2, claims 2 to 6 |
| Estimator | robust observer: nominal matrices plus norm-bounded uncertainty; observer gains solved online each step by minimizing an upper bound of the error covariance (first-order derivatives set to zero) | recursive, per time step | FIG. 3, claims 7 to 12 |
| Configuration inputs | initial estimate and covariance; scalar tolerance levels for uncertainty and noise that set how tight the bound is | block 30 and block 32 | FIG. 3 |
| SOC step | open-circuit voltage looked up in a Voc-to-SOC table that is a function of battery temperature | after the observer | Description, FIG. 3 block 39 |
| Outputs | SOC to a display for the vehicle user (claim 13); to an electronic control unit regulating the battery terminal voltage (claim 14); to an electronic control unit for fuel economy (claim 15) | claim 1 ends with "regulating the battery in response to the state of charge" | Claims 1, 13 to 15 |
| Stated advantages | robustness to battery age, variation, operating conditions and current sensor noise; reduced calibration time; no rest needed | stated without data | Description |
| Test results | none: no experiment, accuracy or computation figure | | |

**Where the software runs, per the document.** On the vehicle: a control module with a processing unit receives the sensor signals and executes the algorithm. No server or off-vehicle step appears.

**Approach and dependencies.** The estimator needs voltage, current and temperature at the same time steps, a stored voltage-to-SOC table by temperature, and the model bounds and tolerance settings fixed at design time. The model bounds are the part that depends on the chemistry and would have to be set for a lead-acid battery.

**Engineering inference (not a source claim).** The per-step matrix computation is heavier than a lookup or a Coulomb counter, and the patent gives no cost figure; whether it fits a battery-mounted microcontroller is unknown. The bounds and the voltage-to-SOC table are chemistry data that could be produced offline and loaded.

**Gaps in the evidence.**

- No results anywhere, so accuracy is unknown; the advantages are assertions.
- Lithium-ion vehicle (hybrid) context; the plate surface-charge explanation is the lead-acid mechanism, yet the claimed model is for Li-ion.
- OCR left some equations unreadable; the claim wording above is read from the scan.
- "About 24 hours" for equilibrium is stated for a vehicle battery with no source; compare with the unspecified "long time" in the Pop review (source 4) and with East Penn 0656 in [[Generic Reference Values]], which says to measure gel open-circuit voltage no earlier than 4 hours after charge (see C150).

### Source 8: Lakhdari (2026), "Joint Fractional-Order Modeling and Kalman Filtering for Battery State-of-Charge Estimation"

Source: Revue Roumaine des Sciences Techniques, Serie Electrotechnique et Energetique, vol. 71, no. 3, pp. 415 to 420, Bucharest, 2026, doi:10.59277/RRST-EE.2026.3.13; received 2026-03-22; single author, LEPESA laboratory, University of Science and Technology of Oran (USTO), Algeria; 6 pages. Peer-reviewed journal article. The PDF is `JOINT_FRACTIONAL-ORDER_MODELING_AND_KALMAN_FILTERI.pdf` in the repo `Downloads` folder. Section numbers are the paper's own.

| Quantity or statement | Value | Basis and conditions | Section |
|---|---|---|---|
| Method | fractional-order equivalent circuit (open-circuit voltage source, ohmic resistor, leakage resistor, one resistor and constant-phase element branch) with a joint state-and-parameter extended Kalman filter | lithium-ion | 3, 5 |
| Filter state | SOC, the fractional-branch voltage history (L past values), ohmic resistance R0 and leakage resistance; with L = 4 this is 7 states | the 7 is derived by the note author from equation 36 | 5, 6.1 |
| Why a joint filter | model parameters drift with age and temperature, so fixed offline models degrade | the paper's stated gap | 1 |
| Memory length | Akaike criterion picks 5, Bayesian criterion picks 4; going from 4 to 5 improves RMSE by only 3.2% (ratio 0.968 against a 0.95 threshold), so 4 is chosen "balancing model fidelity against computational complexity" | candidates 1 to 20 | 6.1 |
| Identification procedure | open-circuit voltage by a piecewise linear fit to low-current rest data; R0 as the median of voltage step over current step; leakage resistance by regression on self-discharge during long rests; polarization parameters by an autoregressive fit then a grid search over alpha and gradient refinement | offline, from a discharge-and-rest protocol | 4 |
| OCV curve | linear over a wide range with a slope change near 20% SOC | bench cell | 6, Fig 3 |
| Bench | commercial 18650 packs, 2.5 Ah, 14.8 V, programmable electronic load; voltage and current recorded at 1 Hz | laboratory | 6 |
| Benchmark data | CALCE 2 Ah INR18650 cells, DST and FUDS profiles; DST at 25 C, FUDS at 45 C; 1% Gaussian noise added to current and voltage | published data set | 6.3 |
| SOC accuracy | "average RMSE of 3.5% (vs. Coulomb counting)" on the bench; "about 3.5% across all test conditions" on the benchmarks; the abstract says "consistently below 3.5%" | reference is Coulomb counting on the bench; the reference for the benchmark runs is not stated | Abstract, 6.2, 6.3, 7 |
| Resistance tracking | R0 "converging rapidly to a stable low value"; leakage resistance "maintains its characteristic high value"; the paper says this "enables effective State-of-Health tracking without separate estimation routines" | no SOH reference or aging test | 6.2 |
| Embedded status | "embedded hardware implementation" and "long-term aging studies" are future work; no run time, memory or processor given | | 7 |

**Approach and dependencies.** Only current and terminal voltage are measured; temperature is neither a measured input nor an estimated state (adding it as a state is future work). The filter needs an OCV table, capacity, identified polarization parameters and a memory length, all produced offline, plus covariance tuning that the paper plans to automate later.

**Where the software runs, per the paper.** The identification (autoregressive fit, grid search, criteria for memory length) is offline. The filter is called "real-time" and "computationally efficient" but is evaluated on recorded data and no device is named.

**Engineering inference (not a source claim).** With L = 4 the filter has 7 states, so its per-step matrices are small; running it on a battery-side microcontroller looks plausible but is unproven by the paper. The offline identification fits a commissioning step or a cloud job, and the R0 and leakage-resistance states are natural outputs to log and trend in a fleet service for the [[Resistance-Trend State of Health Estimator]] role.

**Gaps in the evidence.**

- The abstract says the method adapts "to aging and temperature changes" and was "validated under ... varying temperatures". The tests are two fixed temperatures (25 C and 45 C), no cold, no aging, no temperature ramp (see C151).
- Reported accuracy is against Coulomb counting on the bench; the reference on the benchmarks is not stated.
- The SOH claim rests on two resistance traces from a short run, with no health reference.
- Small lithium-ion cells and packs (2 to 2.5 Ah); no forklift-scale data and no lead-acid.

### Source 9: Ismail, Firdaus, Rakiman, Budiman, Sardani (2024), "The Estimation of Battery State of Charge using Corny Network"

Source: International Journal of Recent Technology and Engineering (IJRTE), vol. 12, issue 6, March 2024, pp. 5 to 11, doi:10.35940/ijrte.F7999.12060324; Politeknik Negeri Padang, Indonesia; published by Blue Eyes Intelligence Engineering and Sciences Publication; open access (CC BY-NC-ND). Journal article; its indexing and peer-review standing were not checked here. The text has many terminology and consistency errors (listed below), so this source is carried at low weight. The PDF is `The_Estimation_of_Battery_State_of_Charge_using_Co.pdf` in the repo `Downloads` folder. Section numbers are the paper's own; Table 1, Figure 18 and Figure 19 were read from the page images.

| Quantity or statement | Value | Basis and conditions | Section |
|---|---|---|---|
| Method | feedforward neural network with narrow layers, called "Corny"; no convolution, pooling or batch normalization | regression of SOC | III, IV |
| Layer sizes | input of 5 channels, fully connected 55, tanh, fully connected 55, leaky ReLU (scale 0.3), fully connected 1, clipped ReLU (ceiling 1), regression output | Table 1 | III |
| Parameter count | about 3,466 weights and biases (5 x 55 + 55, 55 x 55 + 55, 55 + 1) | derived by the note author from Table 1 | III |
| Inputs | voltage, current, temperature, average voltage and average current over the last 500 s | the text also says the data set holds "voltage, current, temperature and capacity" | III, IV |
| Data | LG 18650HG2 Li-ion data set (Kollmeyer et al., Mendeley Data, 2020), cited as reference 17 with an example deep-network SOC estimator script; the paper does not say what it changed from that example | driving-cycle data at several temperatures | IV, refs |
| Training settings | 1,200 epochs, mini-batch of 1, Adam, gradient threshold 1, learning rate 0.01 dropped by 0.1 every 400 epochs, validation every 30 iterations | | III |
| Test temperatures | method text: 0, 10, 25, 20 and 40 C; Figure 18: -10, 0, 10, 25 C | see C153 | III, IV |
| RMSE by temperature | about 1.2% to 1.6% (bar heights read by eye): about 1.55% at -10 C, 1.3% at 0 C, 1.6% at 10 C, 1.2% at 25 C | Figure 19, axis labeled percent | IV |
| Maximum error by temperature | about 11% at -10 C, 7.5% at 0 C, 8% at 10 C, 6.5% at 25 C (read by eye) | Figure 19 | IV |
| Claimed accuracy | "very high", "predicted and targeted values are almost merged", RMSE and MAX "very low"; training "accuracy of 100%" with loss "very close to zero and might be zero" | abstract and results | Abstract, IV |
| Claims about the architecture | low computational cost, avoids overfitting, "easily understood by individuals with no prior experience in deep learning" | no run time, memory or overfitting test | Abstract, IV |
| Literature figures it repeats | a dual H-infinity filter about 1.5% error [3]; an extended Kalman filter "about 5% to 10%, depending on battery characteristics" [8]; a fractional Kalman filter terminal-voltage error 0.014 V [4]; a self-supervised transformer RMS of 0.9 [12] | reported from the cited works, not checked | I, II |
| BMS data path described in the introduction | cell voltage, module current and each cell's temperature sampled by the microcontroller's ADC and sent to a neural network that estimates SOC and SOH | describes cited work [2] (interleaved pulse charging with NARX), not this paper's network | I |

**Approach and dependencies.** Same data-driven class as Wang (source 1) and Margal (source 5): voltage, current and temperature, plus 500-second rolling averages of voltage and current, which are the only memory the network has. A rolling-average buffer is therefore the embedded state this approach needs. The paper says nothing about where the network runs.

**Engineering inference (not a source claim).** At about 3,500 parameters, inference is small enough for a microcontroller, and training with a pooled data set suits the cloud or a workstation. Neither is shown in the paper.

**Gaps and consistency problems.**

- The accuracy claims are not supported by the paper's own figures: RMSE of about 1.2% to 1.6% and maximum errors of about 6.5% to 11% are not "very low" for a charge gauge, and the "100% accuracy" refers to training loss (see C152).
- The text calls SOC "soil organic carbon" once and "HOC" in the results and conclusion; Table 1 is titled as a convolutional model although the text says there is no convolution; the text says "ReLU" where Table 1 shows leaky and clipped ReLU; the data set is described with different inputs in different places (see C153).
- The abstract and introduction open with lead-acid and "Li-ion" interchangeably; the data and results are lithium-ion only.
- No comparison against another estimator, no separate test of generalization, no run-time figure.

### Source 10: Anthony, Yount, Downey, Sado (2025), "Inferring Battery State of Charge using Strain Sensing and Machine Learning"

Source: IMECE 2025 (ASME), doi:10.1115/imece2025-168119; this PDF is the uncopyrighted author version dated 2026-02-28; University of South Carolina; funded by the Office of Naval Research; approved for public release (Distribution A); 7 pages. Conference paper. The PDF is `author_version.pdf` in the repo `Downloads` folder (the file name does not identify the paper). The data set is cited as a public GitHub repository of the ARTS Laboratory (cycling with strain monitoring for a Samsung 30Q cell). Section numbers are the paper's own.

| Quantity or statement | Value | Basis and conditions | Section |
|---|---|---|---|
| Cell and sensor | Samsung 30Q 18650 NMC cell; strain gauge measuring hoop (circumferential) strain at the middle of the cell, thermocouple fastened beside it | single cell | Abstract, 2.1 |
| Cycling | 1C (3 A) charge and discharge at a 20 C constant chamber temperature, 100% depth of discharge, about 650 cycles; charge to 4.2 V then constant voltage down to 0.15 A; discharge at constant 3 A to 2.5 V with no constant-voltage stage | NHR 9200 battery test system | 2.1 |
| Signals logged | voltage, current, temperature, strain | 1 Hz | 2.1 |
| Why 1C only | above 2C lithium plating causes excessive strain | reported from ref 7 | 2.1 |
| SOC label | capacity determined from the data to give "an accurate baseline estimate of SOC" for training | derived from the test, not an independent SOC | 2.1 |
| Strain mechanism | reversible expansion from graphite intercalation plus non-reversible expansion from SEI growth and other factors | | 1 |
| Model | multilayer perceptron, three hidden layers of 64, 32 and 32 nodes, ReLU, Adam with a constant learning rate of 0.001, L2 regularization 0.0001, mean squared error loss, at most 1,000 epochs with early stopping | text says "a single input as strain", windowed features are five numbers | 2.2 |
| Parameter count | about 3,300 weights and biases for one input, about 3,550 for five inputs | derived by the note author from the layer sizes | 2.2 |
| Features | window of strain data reduced to maximum, minimum, standard deviation, slope and mean; the maximum is the most important | window length not stated | 2.2, 3 |
| Split | 80% training and 20% testing, apparently by whole cycles | | 2.2, 3 |
| Result by data volume | 10 cycles (8 train, 2 test): RMSE 0.1291; 100 cycles: average 0.1008; all about 631 cycles: 0.0886 | RMSE units not stated; if SOC fraction, 0.0886 is 8.9% of full scale | 3 |
| Best cycle | cycle 578: MSE 0.002254, RMSE 0.047477, MAE 0.033308; the text also says some tests reached "as low as 0.0478" | the square root of 0.002254 is 0.04748, consistent | 3, Table 1 |
| Error pattern | error spikes for cycles 50 to 350 and is better for later cycles; cause not determined | | 3 |
| Stated benefit | adds a mechanical measurement to voltage and current; "non-invasive and simplified"; could be combined with traditional methods in a BMS | no combined test | Abstract, 4 |
| Stated limits | one cell only; more cells needed to show the method is not specific to this cell | | 4 |

**Approach and dependencies.** A new measurement quantity: casing strain. The vault has measurement functions for voltage, current, temperature, weight and specific gravity but none for strain of a cell. The estimator also needs a window buffer of strain samples and a trained network. The training label depends on measured capacity per cycle, so a capacity measurement at commissioning or from cycle data is a dependency of the training, not of the live estimate.

**Where the software runs, per the paper.** Not stated. Training time is "less than 40 iterations" on an unspecified computer.

**Engineering inference (not a source claim).** Feature extraction over a window and a 3,000-parameter network would be embedded-sized. The strain gauge and its signal conditioning would be new hardware on every instrumented cell; for a pack of many cells, the cost and wiring are a deployment question the paper does not address.

**Gaps in the evidence.**

- One cell, one temperature (20 C), one rate (1C constant-current discharge), discharge only; no dynamic load, no charge-direction result, no temperature variation. Forklift duty is dynamic and mixed.
- The error is reported against a capacity-derived SOC and the paper does not say whether the held-out cycles come from the same aging period as the training cycles; the unexplained error spike in cycles 50 to 350 is not explained.
- "Non-invasive" is claimed, but the method needs a gauge bonded to the cell casing.
- Not applicable to lead-acid as written: the mechanism is graphite intercalation in a cylindrical lithium-ion cell. No lead-acid strain result appears in the paper.
- The vault's existing strain-gauge mentions (see [[Detect Battery Weight]]) concern load measurement, not cell deformation.

### Source 11: Yunusoglu, Le, Isik, Tiwari, Dikmen, Karadag, "Battery State of Health Estimation Using LLM Framework"

Source: preprint-style conference paper, undated in the file (the PDF is `126_Paper.pdf` in the repo `Downloads` folder; the file name does not identify the paper); Purdue, Drexel, Stanford, IISc Bangalore and Temsa R&D Center (Turkey); 8 pages. Venue and review status not stated in the file. Its results contradict each other (see below), so it is carried at low weight. Section numbers are the paper's own.

| Quantity or statement | Value | Basis and conditions | Section |
|---|---|---|---|
| Test cells | eight lithium titanate (LTO) cells, various cycling conditions, 500 cycles; dataset released in the paper's ref 24 | cycle-based plus instantaneous discharge data | Abstract, IV |
| SOH definition | current charge capacity (mAh) divided by nominal capacity (mAh) x 100 | measured per cycle | III |
| End of life | SOH of 80% | | III, IV |
| RUL method | quadratic fit of SOH against cycle number, solved for the cycle where SOH = 80%; described as done by "the LLM" but is a polynomial regression | | III |
| DVA example | between 2.25 V and 2.30 V the stored charge falls from 40 mAh at cycle 50 to 28 mAh at cycle 500 | a 30% drop, derived by the note author | III |
| Model actually trained | BERT with a linear regression head on the [CLS] output; each data row turned into a text string, 128 tokens maximum; AdamW; mean squared error; 80/20 split; 5 epochs | the label is the charge or discharge capacity | IV, V |
| Model size | 109,483,009 trainable parameters, about 438 MB at 4 bytes each | the 438 MB is derived by the note author | VI |
| Evaluation result at epoch 5 | training loss (MSE) 655,290; test loss (MSE) 654,173; R2 negative; 122 batches at 13.3 batches per second | the paper says the model "unable to capture accurate relationships" and "failed to generalize" | VI |
| Table I (MAE %, time) | GPR 21.00, 34.50; RD 8.74, 27.50; SVR 4.27, 22.00; CNN 10.31, 30.00; the LLM 0.81, 61.17; units of "time" and the meaning of "RD" not stated | | VI, Table I |
| Abstract result | MAE "as low as 0.87%" | | Abstract |
| Deployment statement | "pruning, quantization, and TensorRT acceleration enable real-time inference on edge computing devices"; "hybrid deployment strategy: running estimations at edge nodes (BMS units) while fine-tuning on cloud platforms"; "offline pretraining, online inference" | proposal; no pruning, quantization or edge test is reported | V, VII |
| Conclusion on speed | best suited to applications "where precision is more critical than real-time speed" | | VII |

**Approach and dependencies.** Strip away the language model and the paper's usable content is three simple estimators: SOH as a capacity ratio, a quadratic trend to 80% for remaining life, and differential-voltage features. Their dependencies are concrete:

- the capacity ratio needs a complete-cycle Ah accumulation, a cycle boundary rule and a nominal capacity (see [[Accumulate Amp-Hours]], [[Log Battery Events and Usage]]);
- the trend needs a stored history of SOH per cycle, which suits a service such as [[Battery Replacement Forecasting Service]] or the cloud side of [[Battery State of Health Analytics Service]];
- differential voltage needs high-resolution voltage and charge during a controlled cycle.

**Where the software runs, per the paper.** The paper proposes a split: edge inference on the BMS, cloud fine-tuning and periodic analysis. It tests neither; the only model it trains runs on a GPU and is too large for a BMS (about 438 MB of weights).

**Engineering inference (not a source claim).** The capacity ratio is embedded-sized (counters and one division) but needs complete cycles, which a forklift with opportunity charging may rarely produce. The quadratic trend and replacement forecast are naturally cloud. The language-model part adds nothing the capacity ratio does not already supply, since its label is the capacity itself.

**Gaps in the evidence.**

- The reported accuracy cannot be relied on: the paper's own evaluation shows a negative R2 and a test loss of about 654,000, while the abstract and Table I claim an MAE under 1% (see C156).
- Figures 1, 2 and 3 and most of the methods text describe a state-of-charge pipeline, while the abstract and conclusion are about state of health (see C157).
- Cells are LTO, not lead-acid or the lithium chemistries in the other sources; the cycle conditions are not tabulated.
- The comparison methods (GPR, "RD", SVR, CNN) have no stated settings.

### Source 12: Sarikurt, Ceylan, Balikci (2014), "An Analytical Battery State of Health Estimation Method"

Source: IEEE ISIE 2014 conference paper (978-1-4799-2399-1/14), Gebze Institute of Technology, Turkey; 5 pages; funded by TUBITAK project 110E209. The PDF is `ISIE2014.pdf` in the repo `Downloads` folder. Section numbers are the paper's own.

| Quantity or statement | Value | Basis and conditions | Section |
|---|---|---|---|
| Test cell | Kokam SLBP55205130H lithium polymer, 11 Ah (the Fig. 1 caption prints the model as SLBP5520510H) | single cell | I, IV-B |
| SOH definition | percent of initial condition; 100% is initial; battery unusable below 80% relative capacity | manufacturer's capacity-versus-cycle curve (Fig. 1) | I |
| Test rig | Chroma 62050P programmable DC supply, Chroma 63297 electronic load, NI 9206 and NI 9213 data acquisition cards, LabVIEW; measures voltage, current, temperature | used to build the cell model, run aging and record ECE 15 responses | II |
| Cycle number method | the voltage dips ("slopes") of the cell's ECE 15 response are fitted with y = a/(x+b); a and b from two points on a dip, then polynomials map a or b to cycle number | reference curves come from an equivalent-circuit model with an analytical open-circuit voltage, from the authors' ref 33 (in Turkish); aging at other cycle numbers is simulated, not tested | III-A |
| Cycle number results, 400-cycle cell | 397.7 to 407.1 cycles across three dips and two parameters; mean error 4.60 cycles or 1.15% | Table 2 | IV-A |
| Cycle number results, dip 3 | parameter a: 104.77, 303.43, 502.47 for true 100, 300, 500 (errors 4.77%, 1.14%, 0.49%); parameter b: 113.57, 309.68, 506.95 (13.58%, 3.23%, 1.39%) | Table 1 | IV-A |
| SOH method | capacity % = A x b/a with an aging coefficient A of 23.971, 23.583, 23.821 for dips 1, 2, 3; then SoH % = (capacity % - 80) x 5 | Eq 14, 15 | III-B |
| Capacity fade curve | 8th order polynomial in cycle number, moving-average smoothed, coefficients printed | Eq 13 | III-B |
| SOH results | estimated capacity 99.194, 98.694, 67.194 % versus measured 101.58, 95.50, 96.50 % at cycles 100, 300, 500; errors 2.348, 3.344, 0.719; mean 2.137% | Table 3; measured from discharge time at 1C (11 A): 3659, 3438, 3474 s | IV-B |

**Approach and dependencies.** The method does two things. It estimates cycle number from how the voltage dips under a fixed driving-current profile, then it looks up capacity on the manufacturer's fade curve. It therefore dependsOn: voltage and time acquisition at a high enough rate to fit a dip, a load profile that repeats exactly, and a stored fade polynomial for the specific cell. A device that already counts cycles needs no estimator to get the cycle number.

**Where the software runs, per the paper.** Not stated. The arithmetic is two-point fitting and polynomial evaluation, so it would fit in firmware. Nothing in the paper needs cloud processing.

**Engineering inference (not a source claim).** The SOH result is a cycle-count lookup on a manufacturer curve, not a measurement of the cell's own capacity. It cannot see cells that age faster or slower than the datasheet curve, which the paper itself says depends on temperature and internal dynamics. For a forklift, whose load is not a repeatable profile, the cycle-number step does not apply; counting cycles directly (see [[Log Battery Events and Usage]]) and applying a fade curve gives the same SOH output with no voltage fitting.

**Checks by the note author.**

- Table 1 and Table 2 errors recompute from their own columns (for example 404.745 against 400 is 1.19%); the mean errors in the conclusion (4.1%, 6.813 cycles, 4.5955 cycles, 1.1485%, 2.137%) recompute from the tables.
- Table 3 row 3 lists estimated capacity 67.194 against measured 96.50 with error 0.719. A 67.194 estimate would be a 30% error. 97.194 gives 0.719% and keeps the 2.137% mean, so 67.194 looks like a typo (derived).
- Recomputing Eq 14 with the Table 1 parameters (a = 11832.95, b = 49284.283 at cycle 100) gives 99.21, 98.33, 97.83 for cycles 100, 300, 500, against the printed 99.194, 98.694 and 97.194 (if corrected). The differences are up to 0.65 points.
- 3659 s at 11 A is 101.64% of 11 Ah, the paper prints 101.58%.

**Gaps in the evidence.**

- One cell, three tested cycle counts for SOH and no temperature or rate variation.
- The "measured" capacities are non-monotonic (95.5% at 300, 96.5% at 500) and exceed 100% at cycle 100, so they say little about fade.
- Eq 13 coefficients cannot be evaluated as printed (0.0096 C^8 at C = 100 is about 1e14), so a scaled cycle variable is implied but not defined.
- No embedded implementation, timing, memory or noise tolerance is reported.

### Source 13: Mbagaya, Reddy, Botes (2025), "Machine Learning Techniques for Battery State of Health Prediction: A Comparative Review"

Source: peer-reviewed review, World Electric Vehicle Journal 2025, 16, 594 (MDPI, open access, doi 10.3390/wevj16110594), Nelson Mandela University, South Africa; 26 pages. The PDF is `Machine_Learning_Techniques_for_Battery_State_of_H.pdf` in the repo `Downloads` folder. This is a secondary source: its literature claims are reported from the papers it cites and are not checked here. Only its own simulation counts as a primary result. Section numbers are the paper's own.

| Quantity or statement | Value | Basis and conditions | Section |
|---|---|---|---|
| SOH definition | current discharge capacity over initial nominal capacity x 100% | Eq 17; nominal 2 Ah | 1, 4.1 |
| Dataset | NASA PCoE cells B0005, B0006, B0007, B0018; 2 Ah, 3.7 V; CC-CV charge at 1.5 A to 4.2 V, 2 A constant-current discharge, 24 C; discharge cutoff 2.7 V (B0005), 2.5 V (B0006), 2.2 V (B0007), 2.5 V (B0018); end of life at 70% of nominal | trained on B0006, B0007, B0018; tested on B0005 only | 4.1 |
| Inputs | voltage, current, temperature and their time derivatives, each resampled to 120 points over a normalised discharge; CNN and LSTM take the 6 x 120 array; SVR and RF take summary statistics (Table 3) | no feature selection | 4.2 |
| Result, LSTM (bidirectional) | RMSE 0.0146, MAE 0.0118, R2 0.980, MAPE 1.39% | test cell B0005; SOH as a fraction | 4.5.1, Table 5 |
| Result, CNN | RMSE 0.0194, MAE 0.0160, R2 0.964, MAPE 1.84% | | Table 5 |
| Result, random forest | RMSE 0.0207, MAE 0.0172, R2 0.959, MAPE 2.15% | 600 trees, minimum leaf 2 | Table 5 |
| Result, SVR | RMSE 0.0457, MAE 0.0392, R2 0.800, MAPE 4.80% | RBF kernel, C 10, epsilon 0.03 | Table 5 |
| Training time | CNN 57.95 s, SVR 5.29 s, RF 26.11 s, LSTM 201.59 s | "typical workstation"; hardware not specified | 4.5.3, Table 6 |
| Inference time, memory, parameter count | not reported | | |
| Deployment statement | LSTM's computational and memory demands "make direct deployment on embedded BMS hardware challenging"; RF and SVR "remain relevant in resource-constrained applications"; pruning, quantisation, knowledge distillation or hybrid offline-online frameworks suggested | no test | 4.5.2, 5 |
| Edge-cloud claim (reported from Chen et al., 2024, ref 64) | Transformer with VMD in an edge-cloud collaborative SOH framework, MAE < 0.6% across NASA, CALCE, MIT and EV field data | not checked here | 3 |
| Pack-level claim (reported from Lamprecht et al., 2020, ref 55) | random forest on a simulated 96S74P pack: 1.94% error for capacity SOH, 4.28% for resistance SOH | simulation | Table 2 |
| Stated limits | NASA data only, 25 C, fixed protocols; not representative of fluctuating temperature, dynamic load or irregular charging | | 5 |

**Approach and dependencies.** All four tested models rest on the same input: a full constant-current discharge of voltage, current and temperature, resampled to a fixed length. They depend on a measurement chain for voltage, current and temperature at a steady rate, a cycle segmentation that finds each full discharge, and a capacity label for training. That label comes from Ah accumulation over complete cycles (see [[Accumulate Amp-Hours]]). Cells with different discharge cutoffs sit in the same training set, so the models see normalised curves, not equal voltage windows.

**Where the software runs, per the paper.** Training is offline on a workstation. For inference the paper only says the heavier models are hard to embed and that the lighter ones are candidates. It describes a hybrid offline-online split as a possibility and cites an edge-cloud Transformer paper without detail.

**Engineering inference (not a source claim).** This fits the vault's allocation rule: acquisition, cycle segmentation and feature extraction embedded; training and fleet-wide retraining in the cloud; inference embedded for random forest or SVR and probably cloud or gateway for LSTM until a compressed version is shown. The vault has no data-driven SOH candidate, so this would be a new Object with dependsOn on voltage, current and temperature measurement, a cycle segmenter and Accumulate Amp-Hours. The full-discharge requirement is the weak point for forklifts, which use partial discharges and opportunity charging.

**Gaps in the evidence.**

- One test cell (B0005); the SOH range is about 100% to 70%, so errors in points of SOH are the figures to read: LSTM RMSE 0.0146 is about 1.5 points.
- No inference latency, memory or hardware is reported, despite the statement that all models give "sufficient real-time SOH estimation capabilities" (see C161).
- Training cells have different discharge cutoffs than the test cell, which the paper does not discuss as an effect on the result.
- Lead-acid is not covered; the work is lithium-ion only.

### Source 14: Giuliano, Wu, Yawney, Gadsden (2025), "Transformer-Based Transfer Learning for Battery State-of-Health Estimation"

Source: peer-reviewed article, Energies 2025, 18, 5439 (MDPI, open access, doi 10.3390/en18205439), McMaster University, Canada; 21 pages; NSERC funded. The PDF is `Transformer-Based_Transfer_Learning_for_Battery_St.pdf` in the repo `Downloads` folder. Section numbers are the paper's own.

| Quantity or statement | Value | Basis and conditions | Section |
|---|---|---|---|
| Source dataset | NASA PCoE, 34 18650 cells, Table 2 says LiCoO2, 2 Ah, charge 0.75 C; discharge cutoff 2 to 2.7 V; 4 to 43 C | pre-training on B0005, B0006, B0007, B0018 | 3.1, 4.2 |
| Target dataset | Oxford, 8 Kokam SLPB533459H4 pouch cells, LiNiCoMnO2, 740 mAh, 1C charge, 40 C | fine-tuning on Cell 6; testing on the others | 3.1, 4.2 |
| Inputs | battery voltage, current, temperature, relative time, cycle number, and the maximum capacity of the previous cycle "approximated using the Coulomb counting method"; window of 300 steps ("the average size of a full discharge cycle") | features scaled 0 to 1 except cycle number; points beyond two standard deviations dropped | 3.2 |
| Labels | capacity after each cycle, smoothed with a Savitzky-Golay filter (window 111, 4th order); predictions smoothed again (3rd order; windows 999, 3001, 5001; 5001 best) | smoothing "increased model performance by a factor of 10" | 3.2, 3.3, 4.2 |
| Model sizes | transformer 117,161 parameters (4 blocks, 8 heads); ANN 133,633; LSTM 138,671 | Table 3 | 3.3 |
| NASA only, test B0018 (RMSE) | LSTM 0.01161 (R2 0.978); ANN 0.01932 (0.938); transformer 0.02517 (0.895) | trained on B0005 to B0007 | Table 4 |
| Oxford only, test Cell 8 (RMSE) | ANN 0.01747 (R2 0.933); transformer 0.01918 (0.919); LSTM 0.01953 (0.916) | trained on Cells 1 to 7 | Table 5 |
| NASA to B0029 (43 C), no fine-tuning (RMSE) | transformer 0.00792 (R2 0.941), 0.00974 without smoothing; LSTM 0.01156 (0.875); ANN 0.01261 (0.851) | | Table 6 |
| NASA to Oxford, average over test cells (RMSE) | transformer 0.01461 (R2 0.932); ANN 0.01481 (0.929); LSTM 0.02931 (0.781); transformer without smoothing 0.01781 | | Table 7 |
| Abstract claim | transformer RMSE 0.01461 beats the best Oxford-only model (ANN, 0.01747) and a literature transformer "RMSE of 0.90170" | 0.01461 against 0.01747 is 16.4% lower (derived); the text says 17% | Abstract, 4.2 |
| Deployment statement | "poorly suited for direct, real-time deployment on resource-constrained hardware like an embedded BMS"; attention memory is quadratic in sequence length; LSTM or ANN "more pragmatic and power-efficient" on board; pruning and quantisation are future work | no inference test | 4.2, 6 |
| Stated limits | laboratory data only; no sensor drift, packet loss or asynchronous sampling; sensitive to pre-training length (5 epochs best); transfer between NCA-type and NMC cells only | | 6 |

**Approach and dependencies.** A data-driven SOH estimator that needs a measurement chain for voltage, current and temperature, a cycle counter, and the previous cycle's capacity from Coulomb counting. So it dependsOn the same acquisition and Ah accumulation functions as the capacity-ratio approach (see [[Accumulate Amp-Hours]]), plus a model and its weights. Transfer learning adds a training workflow: pre-train on a large source dataset, fine-tune on one target cell run to end of life, then test on others.

**Where the software runs, per the paper.** Training and fine-tuning are offline. Inference is not placed, but the paper rules out an embedded BMS for this model and suggests a lightweight variant as future work. The Savitzky-Golay smoothing windows (999 to 5001 steps, roughly 3 to 17 cycles of 300 steps, derived) are applied to the whole predicted curve, so the reported numbers are for after-the-fact smoothing, not a causal on-board estimate (derived by the note author).

**Engineering inference (not a source claim).** The split follows the vault rule: Coulomb counting, acquisition and cycle count embedded; pre-training and fine-tuning in the cloud; inference on a gateway or in the cloud. The paper's own two best-case results come from smoothed whole-life curves with a previous-cycle capacity feature. Next-cycle capacity is close to previous-cycle capacity, so a simple persistence baseline (predict the last measured capacity) is the comparison that is missing; the paper does not report one. For a fleet, fine-tuning needs a labeled full life of a cell of the same type, which exists only after a pack has aged or from a test lab.

**Checks by the note author.**

- Table 4 and Table 5 RMSE values match the square roots of their MSE values (for example 0.000633 gives 0.02516).
- 0.01461 against 0.01747 is a 16.4% reduction, not 17%. Against the transformer's own Oxford-only result (0.01918) it is 23.8%.
- Eq 1 defines SOH as Cmax over Crated, with Cmax "the nominal battery capacity" and Crated "the estimated current battery capacity"; read literally this gives values above 100% for an aged cell, so the labels are swapped.
- Table 6 lists eight models but five R2 values.

**Gaps in the evidence.**

- Table 7 averages over seven Oxford cells including Cell 6, which was also the fine-tuning cell; Cell 7 is not explained. Table 5 tests only Cell 8. The headline comparison mixes these (see C165).
- No inference time, memory use or hardware test.
- Lithium-ion laboratory cells at fixed temperatures; no lead-acid and no partial-discharge forklift duty.

### Source 15: Ahmed, Aagela, Geth, Iqbal, "A Lifecycle-Aware Evaluation Framework for Battery State-of-Health Estimation"

Source: manuscript-style paper (Springer-style layout) from the University of Huddersfield, UK; 12 pages; no venue, date or review status in the file (the PDF is `main.pdf` in the repo `Downloads` folder; the file name does not identify the paper). Treated as an unreviewed preprint. Section numbers are the paper's own.

| Quantity or statement | Value | Basis and conditions | Section |
|---|---|---|---|
| Data | NASA PCoE, 34 cells, nine protocols, 4 to 44 C, 1 to 4 A, cutoffs 2.0 to 2.7 V; 20 cells kept after quality filters (14 dropped for artefacts such as apparent SOH up to 27.5 times initial) | filters: capacity below 0.1 Ah dropped, SOH above 1.15 dropped, fewer than 20 valid cycles excluded | 3.1, 3.2, Table 2 |
| SOH definition | capacity at cycle n over the first recorded capacity of the same cell | not the nominal 2 Ah | 3.1 |
| Tier 1 test | leave one cell out over B0005, B0006, B0007, B0018; 636 test cycles | | 3.3 |
| Tier 2 test | leave one cell out over all 20 cells, so unseen protocols | | 3.3 |
| LightGBM result, Tier 1 | MAE 0.031 +/- 0.019, R2 0.862 +/- 0.102 (3.1 points of SOH) | 61 features, deepest configuration | 5.2 |
| LightGBM result, Tier 2 | MAE 0.049 +/- 0.043; R2 per cell "frequently negative" | bimodal; out-of-envelope cells fail | 5.4 |
| Feature ablation | 31 features: MAE 0.0333, R2 0.838; 61: 0.031, 0.862; 134: 0.0335, 0.838 | the full 3 x 3 grid is not tabulated in the text | 5.1 |
| Band recall, Tier 1 | Good 91.5%, Fair 81.1%, Poor 66.7%, Critical 7.1% (5 of 70); overall 72.0% | pooled predictions | 5.3, Table 3 |
| Band recall, Tier 2 | Good 83.8%, Fair 80.6%, Poor 65.1%, Critical 5.2%; overall 69.0% | n = 628, 283, 361, 174 | Table 3 |
| Worst Tier 1 cell | B0006, terminal SOH 0.57; predictions flatten near 0.74 in late life | the model never saw degradation that deep | 5.2 |
| Hardware statement | the trained LightGBM artefact is "a few kilobytes", but the inference path (hundreds of tree traversals, heap and OS assumed, 61-feature scratch memory) does not fit a Cortex-M target (256 kB SRAM or less); "structurally non-deployable" | argued, "not by an attempted port" | 5.5, 7 |
| CNN preview | 10,169 parameters; 3 x 200 input; Tier 1 MAE 0.028 +/- 0.010, R2 0.826 +/- 0.160, band accuracy 78.7%; Tier 2 MAE 0.040 +/- 0.033, R2 -2.13 +/- 5.22, band accuracy 77.0%; worst Tier 2 cell MAE 0.164, R2 -19.0 | evaluation of all folds took 314 s on a laptop CPU (training, not inference) | 6, Table 4 |
| Design premise | cloud SOH is "unattractive: connectivity is intermittent, latency unbounded, and streaming raw cycle data conflicts with the installations' own energy budgets"; target microcontrollers with hundreds of kilobytes | stated, not tested | 1 |
| Roadmap | on-target latency and energy, INT8 quantisation, protocol conditioning, severity-aware loss, thermal and RUL extension | future work | 7 |

**Approach and dependencies.** Both models work on one completed discharge cycle of voltage, current and temperature, so they depend on acquisition of those three signals, a cycle segmenter and a buffer large enough for a full discharge (the CNN needs the cycle resampled to 200 points). The label needs a first-cycle capacity reference per cell (see [[Accumulate Amp-Hours]]). The paper's key point for dependencies is protocol: a model trained without temperature, load and cutoff context fails on cells run under other protocols, so the estimator would also depend on a record of the operating conditions (the vault's [[Log Battery Events and Usage]]).

**Where the software runs, per the paper.** The paper's premise is on or near the asset. Its own measured work is offline on a laptop. The CNN is sized for a microcontroller but not put on one.

**Engineering inference (not a source claim).** This is the clearest statement in the set of an embedded-first allocation, and it comes from a design argument. The part that is certainly embedded is acquisition, cycle segmentation and feature or resample steps; the model could be embedded if the CNN claim holds. The band mapping and any replacement forecast are cheap and could run in either place. For a forklift, the full-discharge requirement again applies (see Source 13). The result that matters most for the vault is the Critical-band blind spot: an estimator with good average error can still miss the region that triggers replacement, so any Requirement for Estimate State of Health should set a threshold-crossing target, not only an average error.

**Checks by the note author.**

- Table 3 pooled Tier 1 recalls weighted by band counts give 455 of 636 correct, or 71.5%; the paper states 72.0%. Tier 2 recomputes to 69.0%.
- The inverted-U feature curve rests on a difference of 0.0002 in MAE between 31 and 134 features (0.0333 against 0.0335), against a fold standard deviation of 0.019.
- The CNN's weights are 10,169 x 4 bytes = about 40.7 kB and 10 kB at one byte each, matching the stated sizes.
- Table 4 shows CNN Tier 1 R2 of 0.826 against LightGBM 0.862 (lower), and Tier 2 R2 -2.13 against a LightGBM entry given only as "wide, often < 0".

**Gaps in the evidence.**

- No on-target timing, memory or energy for either model.
- NASA lithium-ion 18650 cells only; one manufacturer; no lead-acid.
- Early stopping is monitored on the held-out cell, disclosed by the authors as mild optimism.
- The feature matrix and notebook are available only from the authors on request.

### Source 16: Kafadarova, Sotirov, Herbst, Stoynova, Rizanov (2023), "A System for Determining the Surface Temperature of Cylindrical Lithium-Ion Batteries Using a Thermal Imaging Camera"

Source: peer-reviewed article, Batteries 2023, 9, 519 (MDPI, open access, doi 10.3390/batteries9100519), Plovdiv University, Technical University of Sofia and BioInterface GmbH; 19 pages. The PDF is `1_batteries.pdf` in the repo `Downloads` folder. This paper does not estimate SOC or SOH. It is kept because temperature is an input to the Hybrid SOC and the learned SOH approaches in the register, and because it argues about where cell temperature can be measured. Section numbers are the paper's own.

| Quantity or statement | Value | Basis and conditions | Section |
|---|---|---|---|
| Method | the cell rotates about its axis, synchronised to the camera frame rate (1 frame per second); frames are cut into segments within a chosen viewing angle; segments are combined into a 3D surface temperature map and an average surface temperature | Eq 6 to 12 | 2, 3 |
| Camera and rig | FLIR E8, 320 x 240 pixels, thermal sensitivity below 0.050 C, accuracy listed as +/-2% of reading; TENMA 72-13510 electronic load; Keithley 2010 voltmeter; 1.8 degree stepper motor; thermally insulated chamber | Table 1 | 2 |
| Surface preparation | thermographic paint HERP-LT-MWIR-BK-11, emissivity 0.94 for viewing angles 0 to 45 degrees | the emissivity at other angles is "unknown" | 2, 3 |
| View-angle error (reported from refs 26, 27, 31) | recorded temperature starts to drop between 40 and 60 degrees and drops more above 60; 60 degrees gives a 4 to 5% error | not tested here | 1.3, 3 |
| Claim for the method | pixels whose view-angle error exceeds a limit are cut; within the kept angle the angular error is below 0.25 C | error is relative to the camera's own 0-degree reading, not to a reference sensor | 3 |
| Resolution | fourfold upscaling of thermograms by the EDSR image-super-resolution method | image quality, no measurement check | 3 |
| Non-radiometric images | temperature recovered from the colour bar in a JPEG by nearest-neighbour search in a k-d tree | | 3 |
| Test cell | Samsung ICR18650-22F, 2200 mAh, pre-charged to 4.2 V, rested 4 h, discharged at constant 2200 mA to 3.5 V; ambient 22 C, 65% humidity; camera 500 mm from the cell axis | one cell, one test | 3 |
| Result | average surface temperature rises from about 24 C to 31 C over about 72 s (7 points, Fig 19) | the text calls the end of discharge "exothermic" | 3, Fig 19 |
| Contact-sensor critique | thermocouples "limited to measuring purely relative temperature changes", need a cold junction and analogue conditioning, cannot be multiplexed on a single conductor; fibre-optic (FBG) sensors are mechanically sensitive and costly; embedded thermistors have long-term stability problems | 1.1, 1.4 | |
| Scope statement | the method "is for testing batteries in laboratory conditions" and suits development, diagnostics, quality control and testing | | 1, 4 |

**Approach and dependencies.** Nothing in the paper depends on, or feeds, an SOC or SOH algorithm. It describes how to measure the surface temperature field of a cylindrical cell in a lab. The vault's [[Battery Temperature Acquisition Firmware]] and its sensor elements (see [[Thermistor Temperature Sensor]] and [[BMS Temperature Sensor Network]]) are the on-board counterpart; the paper offers no data for choosing between them.

**Where the software runs, per the paper.** Offline Python image processing on a computer. The camera, rotating fixture and paint exclude on-board use.

**Engineering inference (not a source claim).** The useful content for the vault is the finding that surface temperature varies with view angle and across the surface, so one contact sensor sees one point. It does not show how large the spread is on a cell in a pack: the paper's 3D maps cover one cell in free air, with 7 C of change but no measured spread across the surface. Not usable as a requirement for pack temperature sensing.

**Checks by the note author.**

- A discharge at 2200 mA for 72 s removes 44 mAh, about 2% of the 2200 mAh capacity (derived). The test is said to run to 3.5 V, which at about 1C takes on the order of an hour, so Fig 19 shows only the first minute or so, and the "end of discharge" rise the text describes is not in the plotted data.
- A rise from about 24 C to 31 C in the first 72 s at 1C is larger than this note can confirm from any other source in the set; no reference sensor reading is given for comparison.
- Camera accuracy of +/-2% of reading is 0.6 C at 30 C (derived), larger than the 0.25 C view-angle bound the paper reports.
- The thermocouple critique is contradicted by a manufacturer application note: a thermocouple's voltage depends on the difference between its two junctions, and with the cold junction temperature measured and compensated, it reads the actual (absolute) hot-junction temperature ([Analog Devices, Cold Junction Compensation in Thermocouple Guide](https://www.analog.com/en/resources/technical-articles/cold-junction-compensation-in-thermocouple-guide.html)). The paper's own sentence, that thermocouples "require a cold junction element", describes the same mechanism.

**Gaps in the evidence.**

- No comparison of the camera result with a contact sensor, so "high accuracy" is not shown.
- One cell, one rate (about 1C), one ambient, free air; no pack, no cooling, no ageing.
- Emissivity at view angles above 45 degrees is stated as unknown, yet the cut limits are defined by angle.

### Vault changes made from this review (2026-10-13)

Created as Draft, with no product allocation: [[Segment Discharge Cycles]] (Function), [[Model-Based State of Charge Estimator Firmware]], [[Data-Driven State of Health Estimator Firmware]], [[Learned State of Health Service]], [[Estimate State of Health - Report Configured Threshold Crossings]] and [[Estimate State of Charge and Health - Declare Accuracy Basis]] (the last two are proposed Requirements with no stakeholder source and no numeric values). Edited: dependencies added to [[Capacity-Retention State of Health Estimator]] and [[Resistance-Trend State of Health Estimator]]; candidate paths added to [[Estimate State of Charge]] and [[Estimate State of Health]]; band mapping noted in [[Battery Replacement Forecasting Service]]. Not created, by decision: a candidate for the BERT approach (results contradict themselves), the cycle-number method (needs a fixed load profile) and strain sensing (one low-confidence source). The skipped forklift design paper (file 6) is not reviewed.

Related: [[Estimate State of Charge]], [[Estimate State of Health]], [[State of Charge Estimation Firmware]], [[Coulomb Counting State of Charge Estimator Firmware]], [[Hybrid State of Charge Estimator Firmware]], [[Battery State of Health Analytics Service]], [[Cloud Battery Data Upload Service]].

## Former ids

## Aliases

- SOC and SOH literature review
