---
type: Document
subtype:
id: DOC-00411
uid: 20261017150002000skellyspencer
status: Draft
tags:
  - source-document
  - regulation
  - forklift
  - clean-fuel-program
  - first-hand-read
  - oregon
  - metering
  - estimation-method
sourceClass: other
sourceUrl: "https://www.oregon.gov/deq/ghgp/Documents/cfpAfEstMethodMemo.pdf"
accessed: 2026-10-17
describes:
  - "[[Western State Clean Fuel Programs for Forklift Electricity Register]]"
  - "[[Forklift Clean Fuel Credit Business Case]]"
---

# Document - Oregon DEQ Electric Forklift Estimation Methodology Memo (2023-06-09)

## Definition

Oregon DEQ's approved 2023 electric forklift estimation method, valid only until the Q3 2023 report, with its variables and typical charger efficiency numbers.

## Notes

**How it was read:** first-hand, from the raw file the owner added to the repo (`Downloads/ODEQ_cfpAfEstMethodMemo.pdf`), with text extracted by pdftotext. Not a summary.

Added from the owner's downloads. Signed approval memo dated 2023-06-09 from the Clean Fuels Program team lead to the Office of GHG Programs manager, with the final estimation methodology attached. The web address is inferred from the file name the owner used and has not been checked.

- **Authority and period:** OAR 340-253-1000(2) lets DEQ approve an alternative methodology. The method is for Q1, Q2 and Q3 2023 only; it cannot be used for Q4 2023 or later. From Q4 2023 all forklift reporting must reflect actual metering at the point of dispensation. A reporter with real charging data must use it.
- **Changes from the draft:** depth of discharge raised from 20 to 30 percent; method extended to Q3 2023; shifts per day capped at 2.
- **Formula:** kWh per forklift per charge cycle = depth of discharge (max 30 percent) x battery capacity (kWh) x charger efficiency x charge return factor; kWh per quarter = that x shifts per day (max 2) x work days per quarter. The sum for all forklifts at the FSE is reported.
- **Observation (analyst):** the formula as printed multiplies by charger efficiency and by a charge return factor above 100 percent. Multiplying by an efficiency below 100 percent lowers the reported figure, whereas energy drawn from the wall would be the battery energy divided by efficiency; the 115 or 118 percent charge return partly offsets it. Whether this is intended conservatism was not stated.
- **Typical charger numbers stated:** ferro-resonant efficiency 82 to 86 percent, SCR 78 to 82, high frequency 90 to 96 (older units at the low end). Charge return factor 115 percent for ferro-resonant and high-frequency chargers, 118 percent for SCR.
- **Reporting detail:** kWh are reported in OFRS segregated into forklifts made before 2016 and from 2016 on, by model year, with DEQ's spreadsheet uploaded. Battery capacity is to be found with an EnerSys tool (mptools.enersys.com/oem).
- **Use for the business case:** the cap of 30 percent depth of discharge and two shifts is a regulatory ceiling for estimation, not a measure of real consumption (real trucks commonly discharge deeper, analyst reasoning). It gives no per-truck annual kWh figure (IB-258).
- **Conflicts:** the earlier meeting deck proposed 20 percent per shift (C302). Confirms metering from Q4 2023 (C292).

## Provenance

- **Source type:** regulator memo (PDF).
- **Source identity:** Oregon Department of Environmental Quality.
- **Original web address:** <https://www.oregon.gov/deq/ghgp/Documents/cfpAfEstMethodMemo.pdf>.
- **Repo copy:** `Downloads/ODEQ_cfpAfEstMethodMemo.pdf`.
- **Access date:** 2026-10-17. **Revision:** memo dated 2023-06-09
- **Evidence tier:** not covered by T1 to T5 in [[Landscape Evidence and Modeling Conventions]] (government regulator publication: the authority for what the rule or the agency says, not evidence of product capability; read first-hand from the raw file the owner added to the repo).

## Traceability

- `describes` links the document to the registers it supports; disagreements are logged in [[Battery Product Landscape Conflicts and Open Questions]].

## Aliases

## Former ids
