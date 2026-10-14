---
type: Info
subtype: research
id: INFO-00946
uid: 20261014144542580skellyspencer
status: Draft
tags:
  - research-note
  - fleet-software
  - power-management
describedBy:
  - "[[Document - Logistics Business Linde connect charger Article (2023-04-26)]]"
  - "[[Document - Jungheinrich Active Load Management Page (retrieved 2026-10-14)]]"
  - "[[Document - Warehouse News Fronius PV Connect Article (2023-06-13)]]"
  - "[[Document - Raymond West ACT Chargers ROI Blog (2026-01-15)]]"
  - "[[Document - INDUSTRIAL Production Toyota Peak Load Management Article (2026-02-19)]]"
  - "[[Document - Crown Take Control of Forklift Energy Costs Blog (retrieved 2026-10-14)]]"
  - "[[Document - Ampcontrol Compatible Vehicles Page (retrieved 2026-10-14)]]"
describes:
  - "[[Linde connect charger]]"
  - "[[Jungheinrich Active Load Management]]"
  - "[[Toyota Peak Load Management]]"
  - "[[Fronius PV Connect]]"
  - "[[ACT ACTenergy]]"
  - "[[Crown V-HFM3 Charger]]"
---

# Forklift Charger Load Management Register

## Definition

How forklift and industrial-truck chargers are managed as a group against a site power limit or tariff, and whether any OCPP or EV charge-management platform is shown managing them. Created 2026-10-14 to answer IB-221.

## Notes

### Answer to IB-221

- **No source shows a forklift or GSE charger managed by an OCPP charge-management or EV-fleet energy platform.** Flip Turn, PowerFlex X, depotfinity and Ampcontrol describe EV fleets; Ampcontrol's compatible vehicles page lists one road truck and no industrial truck ([[Document - Ampcontrol Compatible Vehicles Page (retrieved 2026-10-14)]]). Absence in these pages is not proof that it cannot be done; the pages invite contact about unlisted vehicles.
- **Truck and charger makers sell their own group load management.** Six systems state power sharing, peak limiting or peak-rate avoidance for forklift chargers, each through the maker's own network or portal.

### Evidence by product

| Product | Maker | What is stated | Link between chargers | Outside interface stated | Tier |
|---|---|---|---|---|---|
| [[Linde connect charger]] | Linde Material Handling | power limits, time slots, priority by charge level, readiness dashboard; up to 50 chargers | central hardware unit, wired at launch; wireless planned | energy management integration planned | T2, second-hand |
| [[Jungheinrich Active Load Management]] | Jungheinrich | group power limit (peak shaving), priority by state of charge, weekly schedules, fallback rules | radio, LAN/Wi-Fi or cable via SLC 700 control centre | optional higher-level energy management system, protocol not named | T1 |
| [[Toyota Peak Load Management]] | Toyota Material Handling | shared power budget by truck priority | industrial radio between chargers; Bluetooth app for setup | PV data by radio access point; no EMS interface stated | T2, second-hand |
| [[Crown V-HFM3 Charger]] | Crown Equipment | Demand Response Management: group chargers, program around spot pricing, target peak loads, infrastructure limits | not stated | not stated | T1 |
| [[Fronius PV Connect]] | Fronius International | plan charging around PV output with load balancing | cloud portal Charge & Connect | PV system and Fronius inverter | T2, second-hand |
| [[ACT ACTenergy]] | Advanced Charging Technologies | shift and stagger charging away from peak-rate periods | not stated | utility signal path not stated | T3 dealer blog |

### Findings

- **Same function, different networks.** All six state the same behavior (share a power budget, prioritize trucks, avoid peaks) but each runs on its own radio or portal. The vault function [[Balance Charging Power Across Site Capacity]] therefore covers both EV software and these. No common protocol is shown.
- **Interfaces to a site energy system are the open point.** Jungheinrich states optional higher-level integration and Linde plans it; neither names a protocol (OpenADR, Modbus, OCPP, MQTT). Compare [[Interface and Protocol Layer Reference]] and [[Charger-Vehicle Interface Register]].
- **No figure supports the cost claims.** No source gives a measured saving; ACT's demand-charge numbers are an illustration in a dealer blog.
- **Consistent with C210 and C211.** Those entries say industrial chargers are not evidenced on OCPP; this research found nothing that contradicts that. They stay open.
- **Dates.** The two Linde articles (2023-04-26 and 2023-09-07) both say the launch is timed for LogiMAT with no year (C266).

### Gaps

- Not read: the Jungheinrich factsheet PDF, Linde's own connect:charger page, Toyota Material Handling's own page, the SolarEdge commercial EV platform article (redirected), and Fronius PV Connect product pages. See IB-227 and IB-228.

## Aliases

## Former ids
