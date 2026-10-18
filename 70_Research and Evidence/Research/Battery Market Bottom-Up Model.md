---
type: Info
subtype:
id: INFO-90054
uid: 20261018161000000skellyspencer
status: Draft
tags:
  - market
  - market-model
  - bottom-up
  - register
  - forklift
  - motive-power
describes: []
describedBy:
  - "[[Document - Forklift Battery Replacement Cost 2026 Guide (Forkliftaction, sponsored by ROYPOW)]]"
  - "[[Document - Flux Power Blog Why a Forklift Battery Price Isn't Its True Cost]]"
  - "[[Document - Flux Power X-Series Battery Pack Brochure (Class 1)]]"
  - "[[Document - Flux Power C-Series Battery Pack Brochure]]"
  - "[[Document - Flux Power L-Series L48 Battery Pack Brochure]]"
  - "[[Document - EPRI Electric Forklifts Brochure (April 2015, ID 3002005805)]]"
  - "[[Document - FirstEnergy Electric Forklift Fact Sheet]]"
---

# Battery Market Bottom-Up Model

## Definition

A bottom-up estimate of the yearly value of industrial truck traction batteries: electric trucks by class, times batteries per truck, times how often batteries are replaced, times price. Built 2026-10-18 to test the vendor market sizes in [[Market Size and Volume Register]]. It is a plausibility check, not an independent estimate.

## Notes

**Result in one line.** The model gives USD 3.0bn (low), USD 12.2bn (base) and USD 34.2bn (high) a year for world traction batteries, against vendor reports of USD 5.4 to 5.9bn. The range is wide because the inputs are wide; the base case is 2.1 to 2.3 times the vendors (derived). Treat the model as showing which inputs matter, not as a market size.

### 1. Method (steady state, one year, world)

- Class 1 and 2 (riders with large batteries): yearly battery units = trucks shipped × batteries per truck × truck life ÷ battery life, split by chemistry. This treats the installed base as constant at the 2025 shipment rate and ignores growth, so it understates a growing market.
- Class 3 (pedestrian pallet and other, Class 31 and 32 combined): the same formula with its own prices and lives.
- Classes 4 and 5 (combustion) are excluded; they carry a small starter battery, not a traction battery.
- Prices are one price per battery, not per kWh. No source was found that gives price by class.

### 2. Inputs (low / base / high)

| Input | Value | Status | Source |
|---|---|---|---|
| Class 1 and 2 truck shipments, world, 2025 | 601,722 | Sourced | [[Market Size and Volume Register]] (WITS 2025 factsheet) |
| Class 3 truck shipments (31 + 32), world, 2025 | 1,290,448 | Sourced | [[Market Size and Volume Register]] (WITS 2025 factsheet) |
| Lithium share of Class 1/2 stock | 32 / 40 / 50% | Partly sourced: 32% of full-electric sales in 2024 is Interact's; 40 and 50% are assumptions | [[Market Size and Volume Register]] (Interact 2026) |
| Lead-acid battery price, Class 1/2 (USD) | 2,000 / 3,975 / 6,000 | Sourced range (sponsored); base is the midpoint of 2,950 to 5,000 | [[Document - Forklift Battery Replacement Cost 2026 Guide (Forkliftaction, sponsored by ROYPOW)|fka]] |
| Lithium battery price, Class 1/2 (USD) | 6,000 / 15,500 / 25,000 | Sourced range (sponsored, 'and up'); base is the midpoint | [[Document - Forklift Battery Replacement Cost 2026 Guide (Forkliftaction, sponsored by ROYPOW)|fka]] |
| Lead-acid life (years) | 5 / 4 / 3 | Sourced (3 to 5, heavy use) | [[Document - Forklift Battery Replacement Cost 2026 Guide (Forkliftaction, sponsored by ROYPOW)|fka]] |
| Lithium life (years) | 10 / 9 / 8 | Sourced (8 to 10+) | [[Document - Forklift Battery Replacement Cost 2026 Guide (Forkliftaction, sponsored by ROYPOW)|fka]] |
| Truck life, Class 1/2 (years) | 8 / 10 / 12 | **Assumption, no source found** | none |
| Batteries per truck | 1.0 / 1.25 / 1.5 | **Assumption**; source says 2 to 3 per forklift at multi-shift sites only | [[Document - Forklift Battery Replacement Cost 2026 Guide (Forkliftaction, sponsored by ROYPOW)|fka]] |
| Class 3 battery price (USD) | 500 / 1,000 / 1,500 | **Assumption, no source found** | none |
| Class 3 battery life (years) | 5 / 4 / 3 | **Assumption** (lead-acid life from the same source) | [[Document - Forklift Battery Replacement Cost 2026 Guide (Forkliftaction, sponsored by ROYPOW)|fka]] |
| Class 3 truck life (years) | 6 / 8 / 10 | **Assumption, no source found** | none |

### 3. Result

| Case | Lead-acid units, Class 1/2 | Lithium units, Class 1/2 | Class 3 units | Lead-acid value (USD bn) | Lithium value (USD bn) | Class 3 value (USD bn) | Total (USD bn) |
|---|---|---|---|---|---|---|---|
| Low | 654,674 | 154,041 | 1,548,538 | 1.3 | 0.9 | 0.8 | 3.0 |
| Base | 1,128,229 | 334,290 | 2,580,896 | 4.5 | 5.2 | 2.6 | 12.2 |
| High | 1,805,166 | 676,937 | 4,301,493 | 10.8 | 16.9 | 6.5 | 34.2 |

All values derived from the inputs above. First-fit batteries alone (one battery per new electric truck, no replacements) come to USD 2.6bn, 6.5bn and 11.3bn for low, base and high (derived).

### 4. Which inputs matter

Each input moved from its low to its high value with the others held at base (derived):

| Input | Total at low value (USD bn) | Total at high value (USD bn) | Swing (USD bn) |
|---|---|---|---|
| Lithium price, Class 1/2 | 9.1 | 15.4 | 6.4 |
| Lead-acid price, Class 1/2 | 10.0 | 14.5 | 4.5 |
| Truck life, Class 1/2 (years) | 10.3 | 14.2 | 3.9 |
| Batteries per truck | 10.3 | 14.2 | 3.9 |
| Class 3 battery price | 11.0 | 13.5 | 2.6 |
| Lead-acid life (years) | 11.4 | 13.7 | 2.4 |
| Class 3 battery life (years) | 11.7 | 13.1 | 1.4 |
| Class 3 truck life (years) | 11.6 | 12.9 | 1.3 |
| Lithium life (years) | 11.7 | 12.9 | 1.2 |
| Lithium share of Class 1/2 stock | 11.8 | 12.8 | 1.0 |

Truck life, lithium price and the lithium share of Class 1/2 dominate. None of the three has a clean source, and the lithium price comes from sponsored content.

### 5. Reconciliation with top-down figures

| Basis | USD bn | Source |
|---|---|---|
| Vendor reports, forklift batteries | 5.4 to 5.9 | [[Market Size and Volume Register]] section 4 |
| EnerSys Motive Power sales FY2026 divided by its stated 32% share (derived) | 4.5 | [[Market History and Outlook Register]] section 5; the 32% is the company's, for earlier years |
| Bottom-up base | 12.2 | this note |
| Bottom-up range | 3.0 to 34.2 | this note |

For the vendor figure to hold, battery revenue would average about USD 2,910 per electric truck shipped in 2025 (USD 5.5bn ÷ 1,890,339 electric truck orders, derived). Most electric trucks are Class 3 pedestrian trucks with small batteries, so this is plausible only if Class 3 batteries are cheap and replaced slowly, or if the Class 1/2 replacement rate is below the 3 to 5 year life quoted by the sponsored source.

### 6. Conflicts and checks

| # | Topic | Position A | Position B | Status |
|---|---|---|---|---|
| BU1 | Bottom-up against vendors | Base case USD 12.2bn | Vendors USD 5.4 to 5.9bn | Open. The model has no calibration to vendor data, on purpose |
| BU2 | Lithium forklift price per kWh | Flux X-Series packs of 22.7 to 33.6 kWh ([[Document - Flux Power X-Series Battery Pack Brochure (Class 1)|fxx]]) at USD 6,000 to 25,000 ([[Document - Forklift Battery Replacement Cost 2026 Guide (Forkliftaction, sponsored by ROYPOW)|fka]]) give about USD 180 to 1,100 per kWh (derived) | BloombergNEF average pack price USD 108 per kWh in 2025 ([[Market History and Outlook Register]] section 6) | Open. The BNEF figure is for automotive-scale packs; the gap is not explained here and the price range is from sponsored content, not a price list |
| BU3 | Battery life in years | Lead-acid 3 to 5 years, lithium 8 to 10+ ([[Document - Forklift Battery Replacement Cost 2026 Guide (Forkliftaction, sponsored by ROYPOW)|fka]]) | Cycle life 1,000 to 1,500 against 2,500 to 3,000 ([[Document - Flux Power Blog Why a Forklift Battery Price Isn't Its True Cost|flb]]); at one cycle a day that is about 3 to 4 years against 7 to 8, at two cycles a day about half that (derived) | Consistent in direction; the lithium years differ by usage assumption |
| BU4 | Lithium share | Interact: 32% of full-electric sales in 2024 | Model share is of Class 1/2 stock, which lags sales | Open; stock share is lower than sales share, so the base 40% is high for stock if 32% is the sales figure |
| BU5 | Energy use against battery size | EPRI: 12,960 to 25,932 kWh a year per truck ([[Document - EPRI Electric Forklifts Brochure (April 2015, ID 3002005805)|epri]]) | Flux Class 1 packs 22.7 to 33.6 kWh, so 400 to 1,100 full cycles a year (derived) | Plausible for multi-shift use |

### 7. Not done

- Charger bottom-up: no source for chargers per truck or charger price by class was found.
- Aftermarket against first-fit split: the model separates them only through replacement; no sourced split.
- US-only: the same method works on Americas shipments (Class 1 plus 2 shipments 136,911, [[Market Size and Volume Register]]) but the unit prices are not US-specific.
- A source for installed base and truck life. These are the two inputs worth finding next.

## Traceability

- Sources listed in the front matter. Related: [[Market Overview]], [[Market History and Outlook Register]], [[Market Size and Volume Register]].

## Aliases


## Former ids
