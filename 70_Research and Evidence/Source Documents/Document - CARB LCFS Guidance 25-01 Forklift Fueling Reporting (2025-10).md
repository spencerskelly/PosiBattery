---
type: Document
subtype:
id: DOC-00376
uid: 20261017120008000skellyspencer
status: Draft
tags:
  - source-document
  - regulation
  - california
  - forklift
  - lcfs
  - metering
  - regulator
sourceClass: other
sourceUrl: "https://ww2.arb.ca.gov/sites/default/files/2025-10/lcfsguidance_25_01_2025.pdf"
accessed: 2026-10-17
describes:
  - "[[California Forklift Electrification Regulations Register]]"
  - "[[California Air Resources Board]]"
contradicts:
  - "[[Document - 17 CCR 95491 Cornell LII Page (retrieved 2026-10-17)]]"
referencedBy:
  - "[[California LCFS - Facility Owner Registers Charging Locations and Reports as First Reporting Entity]]"
  - "[[California LCFS - Forklift Charging Energy Shall Be Metered]]"
  - "[[California LCFS - Third-Party Verification of Forklift Electricity Data]]"
  - "[[California LCFS - Forklift Volumes Are Reported by Lift Capacity Class]]"
  - "[[California LCFS - Rental Forklift Charging Locations Are Registered and Movements Recorded]]"
---

# Document - CARB LCFS Guidance 25-01 Forklift Fueling Reporting (2025-10)

## Definition

CARB's October 2025 guidance on reporting forklift fueling electricity for LCFS credits: metered kWh from Q1 2026, charger-loss adjustment, FSE registration and the reporting entity.

## Notes

**How it was read:** through a summarizing fetch tool (second-hand), not the raw file.

Added for the regulatory-driver topic; this is the primary source for how forklift charging electricity is reported under the Low Carbon Fuel Standard (LCFS). Read twice with different prompts through the summarizing tool; the two readings agree. The guidance says it has no force of law and does not change the regulation. The shell could not reach the CARB site (403), so the raw PDF is on the Document Wishlist.

- **Scope:** how to report forklift fueling (electric, hydrogen, propane) in the LCFS reporting tool (LRT-CBTS). Participation in credit generation is a choice; the guidance sets how to report if an entity reports.
- **Metering (section C.2):** estimating kWh with CARB's earlier approved method is accepted through Q4 2025 reports. From Q1 2026 quarterly reports estimation is no longer accepted and kWh must be measured with equipment that operates within 5 percent accuracy, following the equipment maker's performance specifications and QA/QC, or, without such specifications, an entity monitoring plan with calibration and maintenance. The summary found no meter standard (such as ANSI C12.20) and no revenue-grade requirement. CARB does not approve meters for forklift compliance and says marketing that claims otherwise is false.
- **Where the meter may sit:** upstream of the charger (point A in the guidance's Figure 1; the exact location of point A is not described in the text) with an efficiency adjustment; at the charger output (point C) if it measures electricity leaving the charger for forklift fueling; on the forklift measuring electricity entering it, with no adjustment.
- **Charger efficiency adjustment:** multiply measured electricity by the charger's efficiency from the manufacturer's specifications; if none is given, use 85 percent (example: 100 kWh measured becomes 85 kWh reportable). The summary found no other accepted proof and no statement on whether data reported by the charger itself qualifies, or whether peak or full-cycle efficiency is meant.
- **Registration:** register each charging location as fueling supply equipment (FSE); this needs an Admin role with Signatory Authority, with details in CARB guidance 19-04; CARB approval creates the FSE ID used in reports.
- **Who reports:** since 2025-07-01 (Q3 2025 reporting) the owner of the facility or location is the first fuel reporting entity for electric forklifts; each rental location is registered separately; records of where forklifts charged (for example rental agreements or meter serial numbers) should be kept. Fleet-owned forklifts that charge at a customer site are not separately addressed; the guidance suggests confirming with LRTAdmin@arb.ca.gov.
- **Dates:** quarterly reports are due 30 June (Q1), 30 September (Q2), 31 December (Q3) and 31 March (Q4); verification statements for electric and hydrogen forklifts are due 31 August (or the next business day) starting in 2027 for the 2026 data year.
- **Conflict:** the Cornell copy of the regulation shows an estimation option with no cutoff and allows the fleet owner or its designee to report, which differs from this guidance (C283, [[Document - 17 CCR 95491 Cornell LII Page (retrieved 2026-10-17)]]).
- **Update 2026-10-17 (first-hand read):** the owner added the raw PDF (`Downloads/CARB_lcfsguidance_25_01_2025.pdf`) and it was read in full text, replacing the earlier second-hand reading. Confirmed: effective Q3 2025 two forklift application types (under 12,000 lb and 12,000 lb and over) and the lowest-credit rule when classes cannot be told apart; estimation stops with Q1 2026 reports; meter within 5 percent accuracy; manufacturer charger efficiency or 85 percent default (footnote 4) with a worked 100 kWh x 0.85 example; the owner of the facility or location is the first reporting entity from 2025-07-01 and rental fleets register each location separately and keep location records; verification by a verification body from 2027 for the 2026 data year, statement due 31 August, with deferral up to two years for reporters under 6,000 credits (10,000 if certain other transaction types are reported) and an option to give up the credits instead. Nothing contradicts the earlier summary; the deferral and rental-record details are new ([[Forklift Clean Fuel Credit Business Case]], REQ-00061, REQ-00062).

## Provenance

- **Source type:** regulator guidance (PDF).
- **Source identity:** California Air Resources Board, Low Carbon Fuel Standard program.
- **Original web address:** <https://ww2.arb.ca.gov/sites/default/files/2025-10/lcfsguidance_25_01_2025.pdf>.
- **Access date:** 2026-10-17. **Revision:** dated October 2025 in the file path and text
- **Evidence tier:** not covered by T1 to T5 in [[Landscape Evidence and Modeling Conventions]] (government regulator publication: the authority for what the rule or the agency says, not evidence of product capability; values second-hand through the fetch tool's summary).

## Traceability

- `describes` links the document to the register and organization it covers; disagreements are logged in the conflict register (see [[Battery Product Landscape Conflicts and Open Questions]]).
- `contradicts` points at the Cornell copy of section 95491 on estimation and on who reports; the Cornell text may predate the 2025 amendments (not checked).

## Aliases

## Former ids
