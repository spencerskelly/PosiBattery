---
type: Use Case
subtype: why
id: UC-00006
uid: 20261003215631070skellyspencer
status: Draft
tags:
  - customer-need
  - need-hypothesis
  - vendor-stated
realizedBy:
  - "[[Estimate State of Charge]]"
  - "[[Estimate Remaining Run Time]]"
  - "[[Display Battery Status to Operator]]"
  - "[[Indicate Battery Status Locally]]"
  - "[[Accumulate Amp-Hours]]"
  - "[[Measure Battery Voltage]]"
  - "[[Measure Battery Current]]"
  - "[[Measure Electrolyte Specific Gravity]]"
  - "[[Declare Estimator Accuracy Basis]]"
  - "[[Indicate Charger Status Locally]]"
  - "[[Report Fuel Cell State to Truck]]"
  - "[[Show Battery and Charger State in Fleet Software]]"
participants:
  - "[[Forklift Operator]]"
  - "[[Maintenance Technician]]"
needOf:
  - "[[Forklift Operator]]"
  - "[[Maintenance Technician]]"
arisesIn:
  - "[[Inspect Battery Condition Through a BMID]]"
  - "[[Start a Shift and Confirm Vehicle Energy Readiness]]"
---

# Know Battery State Before and During the Shift

## Definition

Customer need: Know Battery State Before and During the Shift. The problem behind it: Operators and technicians cannot plan work or avoid a mid-shift shutdown without knowing the real state of charge and remaining run time.

## Notes

- **Added 2026-10-14 (software coverage pass, analyst reasoning):** [[Show Battery and Charger State in Fleet Software]]: a person sees battery and charger state without walking to the charger (Fronius says Charge & Connect shows state of charge, energy use and charger status).
- **Added 2026-10-14 (analyst reasoning):** [[Report Fuel Cell State to Truck]]: Plug Power says GenDrive communicates with the truck to monitor stack and system performance and has a fuel level gauge (source: [[Plug Power GenDrive]]). The fuel cell takes the battery's place, so the same question (how much energy is left) applies. Customer work: starting a shift and checking energy.
- **Added 2026-10-14 (analyst reasoning):** [[Indicate Charger Status Locally]]: Analyst reasoning: the operator at the charger sees whether a battery is charging, finished or faulted without opening a portal. Customer work: [[Connect a Vehicle or Battery to a Charger]].
- **Evidence status: need hypothesis.** The statements below are what makers and dealers say their products do for customers. No customer, user or buyer source in the vault confirms that customers hold this need or rank it. Per the ruleset, source research becomes a validated need only after customer-side evidence.
- **Problem solved (analyst wording):** Operators and technicians cannot plan work or avoid a mid-shift shutdown without knowing the real state of charge and remaining run time.
- **Who has the problem:** [[Forklift Operator]], [[Maintenance Technician]].
- **Operating segments (analyst crosswalk to [[PosiCharge Market Segments and Jobs-to-Be-Done]], hypothesis):** Material-handling fleets, Airport eGSE fleets.
- **Realized by (specific functions; products link to these):** [[Estimate State of Charge]], [[Estimate Remaining Run Time]], [[Display Battery Status to Operator]], [[Indicate Battery Status Locally]].
- **Update 2026-10-14 (analyst links, hypothesis):** added realizing functions [[Accumulate Amp-Hours]], [[Measure Battery Voltage]], [[Measure Battery Current]], [[Measure Electrolyte Specific Gravity]], [[Declare Estimator Accuracy Basis]] - rationale: measurements and counts that feed the state-of-charge estimate, and the stated accuracy basis of that estimate. Product counts above predate these links and are not regenerated.
- **Products reaching this need:** 79 by function, design or option (owner decision, round 40: design and option routes count as reached); 68 of those perform a realizing function. Largest families by function: Battery Accessories/Monitoring Devices (27), Batteries/Lithium-Ion Batteries (7), Battery Accessories/Identification and Charge Interface Devices (5), Battery Accessories/Water Level Monitors (5). The metric route (hypothesis, carried over) adds 0 more. Per-product routes in [[Product to Customer Need Map]]. Recounted 2026-10-14.
- **2026-10-06 scope correction:** the counts above predate the split of [[Indicate Charger Status Locally]] from [[Indicate Battery Status Locally]]. The two charger-light accessories no longer reach this need through the battery-status Function. Regenerate the derived counts rather than manually treating 35/32 as current.
- **Vendor-stated evidence (by product):**
  - [[EnerSys Truck iQ]]: EnerSys says Truck iQ is a truck-mounted touchscreen powered through the lift truck cables that reads Wi-iQ3 data wirelessly and shows remaining work time, battery warnings, state of charge, temperatures, electrolyte level and cell imbalance, connecting without driver action. Source: EnerSys Truck iQ page (T1), retrieved 2026-10-02. <https://enersys.com/en/products/monitoring-and-fleet-management/data-logger/enersys/truck-iqsuptradesup-smart-battery-dashboard>
  - [[Linde 6-8 t Electric Counterbalance Forklifts]]: The KION North America catalog says the Linde energy management system on the Series 1279 (E60 to E80) calculates the projected remaining operating time for the operator automatically. Source: KION North America catalog 2023 (in repo) (T1), retrieved 2026-10-03. <https://expoproduction.thelogisticsworld.com/wp-content/themes/theme-summitexpo/directorio/assets/fichas/d0631ac8-a3f8-4b21-8640-bf6f41154ae8.pdf>
  - [[PosiCharge Battery Rx]]: PosiCharge's Battery Rx sheet says it monitors state of charge, water level, voltage and temperature in real time, with current measurement range of plus or minus 1000 A, an electrolyte-immersed temperature sensor rated about -20 F to 165 F, a water-level detector, 7.63 x 2.25 x 1.25 in size, and tolerance of acid immersion and pressure-wash spray. The sheet names AeroVironment, so it likely predates current ownership (dated). Source: PosiCharge Battery Rx sheet (T1), retrieved 2026-10-02. <https://www.posicharge.com/source/PDF/BatteryRx.pdf>
- **Gaps:** no customer-side source; each function in the list is realized by only the products that state it, so the product count is a lower bound; no Requirement is linked (the vault leaves requirements as an intentional gap).

## Operational traceability

- Operational Use Cases: [[Start a Shift and Confirm Vehicle Energy Readiness]].
- Operating contexts: [[Material-Handling Fleet Site]], [[Airport Ground-Support Operating Area]].

## Aliases


## Former ids
