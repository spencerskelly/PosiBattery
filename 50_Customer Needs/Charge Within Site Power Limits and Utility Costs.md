---
type: Use Case
subtype: why
id: UC-00054
uid: 20261014132849707skellyspencer
status: Draft
tags:
  - customer-need
  - need-hypothesis
  - vendor-stated
  - power-management
realizedBy:
  - "[[Balance Charging Power Across Site Capacity]]"
participants:
  - "[[Fleet Operations Manager]]"
needOf:
  - "[[Fleet Operations Manager]]"
---

# Charge Within Site Power Limits and Utility Costs

## Definition

Customer need: Charge Within Site Power Limits and Utility Costs. The problem behind it: a site's electrical service and utility tariff limit how many chargers can run at once and what charging costs, so adding vehicles can force a service upgrade or a high demand charge.

## Notes

- **Evidence status: need hypothesis.** The statements below are what makers say their products do. They come from EV-fleet software pages; no source read ties the need to forklift, GSE or industrial-truck charging, and no customer-side source confirms it.
- **Customer work (analyst reasoning):** planning how many chargers run at once on the site supply and when they run. Candidate operational Use Case: Charge Within the Site Power Limit. The function removes the case where a person staggers chargers by hand or the site pays for a larger service.
- **Who has the problem:** [[Fleet Operations Manager]].
- **Realized by (specific functions; products link to these):** [[Balance Charging Power Across Site Capacity]].
- **Vendor-stated evidence (by product):**
  - [[Flip Turn Energy Management]]: Flip Turn says it redistributes power across active chargers so more chargers can run on existing electrical service, enforces site limits to avoid demand spikes and shifts charging to off-peak hours; it reports a customer cutting heavy-duty charging cost from $0.40 to about $0.18 per kWh (vendor-reported). Source: [[Document - Flip Turn Energy Management Page (retrieved 2026-10-14)]] (T1). <https://getflipturn.com/product/energy-management>
  - [[PowerFlex X]]: PowerFlex says Adaptive Load Management controls EV charging power to keep costs down and can reduce or shift consumption on utility signals. Source: [[Document - PowerFlex X Energy Management Platform Page (retrieved 2026-10-14)]] (T1). <https://powerflex.com/product/powerflex-x>
  - [[Siemens depotfinity]]: the Advanced tier offers load-managed depot operation and the Premium tier dynamic load management and day-ahead optimization to reduce costs. Source: [[Document - Siemens depotfinity Page (retrieved 2026-10-14)]] (T1). <https://www.siemens.com/en-us/products/emobility/depotfinity>
- **Industrial-truck evidence added 2026-10-14 (IB-221, vendor-stated):** [[Linde connect charger]] (Linde says peak demand is a major cost driver and that simultaneous charging after breaks or shift end raises demand; T2), [[Jungheinrich Active Load Management]] (avoid expensive load peaks, reduce energy and infrastructure cost; T1), [[Toyota Peak Load Management]] (avoid expensive power peaks; T2), [[Crown V-HFM3 Charger]] (Demand Response Management; the blog's example is a 4 to 9 p.m. peak window; T1), [[ACT ACTenergy]] (T3) and [[Fronius PV Connect]] (T2). Register: [[Forklift Charger Load Management Register]].
- **Gaps:** no customer-side source; the EV and robot evidence is from fleet software and the industrial-truck evidence is from truck and charger makers' own systems (no savings figures); the savings figure is one customer result reported by the vendor; whether industrial truck chargers can be managed by an OCPP or EV-fleet platform is not shown (IB-221 answered 2026-10-14: no source found); no Requirement is linked.

## Operational traceability

- Operational Use Cases: none yet.

## Former ids
