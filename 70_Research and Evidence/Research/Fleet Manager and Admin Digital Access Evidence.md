---
type: Info
subtype:
id: INFO-90036
uid: 20261013220000001skellyspencer
status: Draft
tags:
  - research
  - fleet-digital-access
  - customer-needs
  - evidence
describes:
  - "[[Fleet Operations Manager]]"
  - "[[Fleet Software Administrator]]"
  - "[[Monitor and Manage Chargers and Batteries Across Sites]]"
  - "[[Manage Fleet Use]]"
describedBy:
  - "[[Document - Supply Chain 24-7 Real-Time Battery Monitoring Fills in the Data Gaps (2017-09-05)]]"
  - "[[Document - AJOT Only 45% of Fleet Operators Are Satisfied with Telematics (2026-05-12)]]"
  - "[[Document - Charged EVs Flux Power SkyEMS 3.0 (2026-07-09)]]"
  - "[[Document - Toyota I_Site Fleet Management Page (retrieved 2026-10-13)]]"
  - "[[Document - MMH Crown Other Voices Five Steps to a Healthier Forklift Fleet (2020-02-27)]]"
  - "[[Document - MMH 237K in Annual Battery Savings in a Grocery DC (2026-03-06)]]"
  - "[[Document - Crown InfoLink Fleet Management Page (retrieved 2026-10-13)]]"
  - "[[Document - MMH Turning Fleet Data into Savings (Chicago Tribune and Crown InfoLink)]]"
  - "[[Document - SIERA.AI Forklift Telematics Data Blog (2023-05-25)]]"
  - "[[Document - Flux Power How Smart Battery Data Helps Manage Forklift Fleets (retrieved 2026-10-13)]]"
  - "[[Document - Raymond iWAREHOUSE Reporting and Analytics (retrieved 2026-10-13)]]"
  - "[[Document - Logistics Matters Cloud Management for Forklift Charging (Exide Motion+ Fleet, 2022-02-18)]]"
  - "[[Document - MH&L Keytroller Infomatics Forklift Fleet Management Software (2017-07-24)]]"
  - "[[Document - Flux Power SkyEMS Fleet View Page (retrieved 2026-10-13)]]"
  - "[[Document - Logistics Management Your Telematics Data To-Do List (2023-05-08)]]"
  - "[[Document - Linde connect desk Fleet Management Page (retrieved 2026-10-13)]]"
---

# Fleet Manager and Admin Digital Access Evidence

## Definition

What fleet managers and software administrators do through digital access, dashboards, alerts and reports, drawn from vendor pages, trade press and a few customer statements, and worked back to customer needs, use cases, functions and products in the vault.

## Notes

### How strong the evidence is

- **Customer-side sources found: one named, two unnamed.** The Chicago Tribune Freedom Center receiving lead is the only named fleet-side voice (F1, reported by trade press about Crown InfoLink; the 30% impact reduction is his estimate). An unnamed grocer (F9, vendor-produced) and an unnamed German dealer customer (F13, reported by the vendor's trade-press item) are the others.
- **Everything else is vendor-stated or vendor-quoted** (F2 to F8, F10 to F12, F14, F15). Article F11 quotes six truck-maker representatives and no fleet manager.
- **No G2 or Capterra review for a forklift fleet product was found.** The review search returned road-vehicle fleet software only. Reddit and LinkedIn cannot be fetched by Claude (see [[Demand Evidence Source Register]]).
- All pages were read through a summarising fetch; a statement 'not stated' means the summary found none on that page, not that the product lacks the feature.
- **Consequence:** the activities below are what vendors say customers do. They support asking customers about these tasks; they do not show how often or how well customers do them. The three new needs are tagged `need-hypothesis`, like the existing ones.

### What fleet managers and administrators do

| Id | What the fleet manager or administrator does | Sources | Customer need | Function | Use case |
|---|---|---|---|---|---|
| A1 | Find idle capacity and right-size the fleet from utilization and peak-hour reports | F1, F2, F3, F4, F12 | [[Right-Size the Fleet from Usage Data]] (new) | [[Report Truck Telemetry]] | [[Review Fleet Utilization and Idle Capacity]] (new) |
| A2 | Receive impact alerts above a set threshold and coach the operator | F1, F2, F3, F4, F5, F11 | [[Detect and Learn from Truck Impacts]] | [[Detect and Record Impacts]] | [[Review an Impact Event and Decide Whether to Return the Vehicle to Service]] |
| A3 | Review pre-shift checklist completions and failures; send service | F2, F11, F15 | [[Find and Fix Vehicle Faults Without Downtime]] | [[Enforce Pre-Shift Checklist]], [[Diagnose Vehicle Remotely]] | [[Review Checklist Failures and Dispatch Service]] (new) |
| A4 | Manage operator access, training and licence expiry | F3, F4, F5, F11 | [[Control Who Operates Each Truck]] | [[Control Operator Access]] | [[Authenticate and Complete Pre-Shift Authorization]]; [[Manage Fleet Portal Users and Alert Thresholds]] (new) |
| A5 | Review fault codes and maintenance cost trends | F2, F3, F12 | [[Find and Fix Vehicle Faults Without Downtime]] | [[Report Truck Telemetry]] | none yet |
| A6 | Check the age and health of every battery and budget replacement ahead | F6, F9, F10, F12, F13 | [[Plan Battery Replacement and Budget Ahead]] (new) | [[Predict Battery Replacement Timing]], [[Estimate State of Health]], [[Upload Battery Data to Cloud Portal]] | [[Review Fleet Battery Health and Plan Replacements]] (new) |
| A7 | Review charging routines across shifts and sites; avoid deep discharge | F3, F4, F7 | [[Prevent Battery Abuse and Premature Replacement]] | [[Protect Battery from Deep Discharge]], [[Log Battery Events and Usage]] | [[Review BMID Battery History and Exceptions]] |
| A8 | Find operators who abuse batteries (amperage spikes, improper charging) | F7, F10 | [[Prevent Battery Abuse and Premature Replacement]] | [[Calculate Battery Abuse Cycles]], [[Log Battery Events and Usage]] | [[Review BMID Battery History and Exceptions]] |
| A9 | Compare sites and use standardized reports across locations | F3, F7, F8 | [[Monitor and Manage Chargers and Batteries Across Sites]] | [[Upload Battery Data to Cloud Portal]], [[Manage Chargers Remotely]] | none yet |
| A10 | Set and change alert thresholds (impact level, licence due, battery limits) | F4, F5, F6 | [[Act on Fleet Data Without Information Overload]] (new) | [[Alert on Abnormal Condition]] | [[Manage Fleet Portal Users and Alert Thresholds]] (new) |
| A11 | Add users, assign roles, limit what each person sees | F2, F3, F6, F14 | [[Act on Fleet Data Without Information Overload]] (new) | none in the vault (candidate: Manage Portal Users and Roles) | [[Manage Fleet Portal Users and Alert Thresholds]] (new) |
| A12 | Export reports or connect through an interface for reviews and integration | F5, F6, F8 | none yet | none in the vault (candidate: Export Fleet Reports) | none yet |

Rows A1, A6, A10 and A11 produced the new notes; A5, A9 and A12 have no new use case yet. A12 and part of A11 have no function in the vault.

### Roles and administration

- Toyota I_Site: 'Colleagues can be added and assigned to roles'; the roles are not listed (F3).
- Keytroller Infomatics: 'enabling roles such as admin, local admin and supervisor' (F14, 2017).
- Flux SkyEMS 3.0: 'role-based user management feature' and an enterprise interface (F6).
- Raymond iWAREHOUSE: 'views can be customized for different personnel based on location or area of responsibility'; no explicit roles stated (F2).
- Crown InfoLink and Linde connect desk: fleet-level roles are not stated; Linde lets an operator's truck access expire on a set date (F4, F5).
- No source says who holds the administrator role. See [[Fleet Software Administrator]].

### What customers are reported to struggle with

- Too much data: 'intimidation by data'; 'they try to track and gather too much data' (F11, truck-maker voices).
- Not using it: one maker estimate puts consistent use at about 40% of companies and casual use at 30% to 40% (F11). See C197.
- Satisfaction: 45% of commercial fleet adopters strongly agree telematics meets their needs (F16); scope and sample unknown.

### Gaps in the vault

- **Functions with no home:** managing portal users and roles; exporting or scheduling reports; exception-based dashboards; API integration. Candidates are not created because no product in the vault performs them yet.
- **Products with evidence but no note:** Toyota I_Site (the vault has only Toyota MyInsights Telematics), Flux SkyEMS, Keytroller Infomatics, Exide Motion+ Fleet, Linde connect desk (the vault has Linde connect). Creating them needs the organization and design notes.
- **Not yet read:** user manuals or admin guides that list every report and role. A manual is the best next source because it shows the actual report catalogue; none was found as a public file.

### Open conflicts

See C196 to C199 in [[Battery Product Landscape Conflicts and Open Questions]].

## Sources

- **F1** [[Document - MMH Turning Fleet Data into Savings (Chicago Tribune and Crown InfoLink)]] <https://www.mmh.com/article/turning_fleet_data_into_savings> (T2)
- **F2** [[Document - Raymond iWAREHOUSE Reporting and Analytics (retrieved 2026-10-13)]] <https://prod-cms-iwarehouseknows.raymondcorp.com/data-management/reporting-and-analytics> (T1)
- **F3** [[Document - Toyota I_Site Fleet Management Page (retrieved 2026-10-13)]] <https://toyota-forklifts.eu/solutions/i_site-fleet-management/> (T1)
- **F4** [[Document - Linde connect desk Fleet Management Page (retrieved 2026-10-13)]] <https://linde-mh.co.uk/en_uk/Solutions/Fleet-management/connect-desk> (T1)
- **F5** [[Document - Crown InfoLink Fleet Management Page (retrieved 2026-10-13)]] <https://www.crown.com/en-us/fleet-management/infolink.html> (T1)
- **F6** [[Document - Charged EVs Flux Power SkyEMS 3.0 (2026-07-09)]] <https://chargedevs.com/newswire/flux-powers-skyems-3-0-adds-battery-health-analytics-and-customizable-dashboards/> (T2)
- **F7** [[Document - Flux Power How Smart Battery Data Helps Manage Forklift Fleets (retrieved 2026-10-13)]] <https://www.fluxpower.com/blog/how-smart-battery-data-helps-manage-forklift-fleets-more-efficiently> (T1)
- **F8** [[Document - Flux Power SkyEMS Fleet View Page (retrieved 2026-10-13)]] <https://www.fluxpower.com/energy-management-solution/fleets> (T1)
- **F9** [[Document - MMH 237K in Annual Battery Savings in a Grocery DC (2026-03-06)]] <https://www.mmh.com/download/237k_in_annual_battery_savings_in_grocery_dc/papers> (T2)
- **F10** [[Document - Supply Chain 24-7 Real-Time Battery Monitoring Fills in the Data Gaps (2017-09-05)]] <https://www.supplychain247.com/article/real_time_battery_monitoring_fills_in_the_data_gaps> (T2)
- **F11** [[Document - Logistics Management Your Telematics Data To-Do List (2023-05-08)]] <https://www.logisticsmgmt.com/article/your_telematics_data_to_do_list/lm_may_2023> (T2)
- **F12** [[Document - MMH Crown Other Voices Five Steps to a Healthier Forklift Fleet (2020-02-27)]] <https://www.mmh.com/article/other_voices_five_steps_to_ensure_a_healthier_forklift_fleet> (T2)
- **F13** [[Document - Logistics Matters Cloud Management for Forklift Charging (Exide Motion+ Fleet, 2022-02-18)]] <https://www.logisticsmatters.co.uk/?p=380> (T2)
- **F14** [[Document - MH&L Keytroller Infomatics Forklift Fleet Management Software (2017-07-24)]] <https://www.mhlnews.com/new-products/forklift-fleet-management-software> (T2)
- **F15** [[Document - SIERA.AI Forklift Telematics Data Blog (2023-05-25)]] <https://www.siera.ai/blog/forklift-telematics-data/> (T4)
- **F16** [[Document - AJOT Only 45% of Fleet Operators Are Satisfied with Telematics (2026-05-12)]] <https://www.ajot.com/news/only-45-off-fleet-operators-are-satisfied-with-telematics> (T2)

## Aliases

- fleet manager digital access
- fleet portal
- fleet dashboard
- fleet reports
- telematics reports
- portal administrator
- fleet admin

## Former ids
