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
| 3 | `Battery_studypaper` | Alshaebi et al., ISERC 2017 (Raymond Corp co-author): lead-acid vs lithium reach trucks, measured data plus simulation | reviewed below |
| 4 | `State-of-the-art_of_battery_state-of-charge_determ` | Pop et al., Meas. Sci. Technol. 2005: SOC determination review | reviewed below |
| 5 | `Comparative_Analysis_of_Battery_State_of_Charge_Es` | Margal et al., E3S Web Conf. 2025: SOC methods compared | reviewed below |
| 6 | `DesignandFabricationofForklift` | Sequeira et al., JESA 2019: design and fabrication of a battery-operated forklift | deferred, likely out of scope |
| 7 | `Battery_state-of-charge_observer` | US 8,922,217 B2, GM: robust SOC observer from open-circuit voltage | reviewed below |
| 8 | `JOINT_FRACTIONAL-ORDER_MODELING_AND_KALMAN_FILTERI` | Lakhdari, Rev. Roum. Sci. Techn. 2026: fractional-order model with EKF for SOC | reviewed below |
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

Related: [[Estimate State of Charge]], [[Estimate State of Health]], [[State of Charge Estimation Firmware]], [[Coulomb Counting State of Charge Estimator Firmware]], [[Hybrid State of Charge Estimator Firmware]], [[Battery State of Health Analytics Service]], [[Cloud Battery Data Upload Service]].

## Former ids

## Aliases

- SOC and SOH literature review
