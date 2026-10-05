---
element_type: plan
status: active
scope:
  kind: cross-product
created: 2026-10-04
---

# Knowledge Base Backlog

## Purpose

This is the canonical, repository-native backlog for work that improves the PosiBattery knowledge base. It records taxonomy, model, evidence, integrity, migration, and validation work.

The backlog does not replace source evidence or canonical model elements. Each work item should link to the relevant notes, schemas, relationships, or source records as they are created.

## Operating rules

- Keep conflicts, open questions, and unresolved classification decisions visible; do not silently resolve or delete them.
- Create a distinct note when public evidence introduces a distinct product, actor, need, function, design, organization, source, or reusable concept.
- Improve the body of an existing canonical note when new evidence concerns the same identity.
- Use explicit typed relationships to express model meaning; folder placement is only the canonical storage location.
- Record evidence, applicability, confidence, and uncertainty with claims and material relationships where practical.
- Complete work in small, reviewable commits and run applicable integrity checks after structural changes.

## Status definitions

| Status | Meaning |
| --- | --- |
| Proposed | Identified but not yet scheduled |
| Active | Currently being worked |
| Blocked | Cannot proceed until a dependency or decision is resolved |
| Complete | Definition of done is met |
| Deferred | Intentionally postponed |

## Priority definitions

| Priority | Meaning |
| --- | --- |
| P0 | Required to preserve model integrity or unblock current work |
| P1 | High-value foundational work for the next modeling stage |
| P2 | Useful improvement with no immediate dependency |
| P3 | Future enhancement or exploration |

## Active backlog

| ID | Priority | Status | Work item | Definition of done | Dependencies |
| --- | --- | --- | --- | --- | --- |
| KB-001 | P0 | Active | Establish canonical top-level folder taxonomy | Approved product-first numbered folder map, scope rules, and migration principles are documented | None |
| KB-002 | P0 | Proposed | Inventory and map current vault content | Every current content file has a proposed canonical destination; conflicts and ambiguous cases are listed | KB-001 |
| KB-003 | P0 | Proposed | Define common element metadata | A common frontmatter contract and type-specific extensions are aligned to the existing schemas and templates | KB-001 |
| KB-004 | P0 | Proposed | Review relationship vocabulary and usage | Essential relationship types, directionality, allowed source/target types, evidence rules, and ambiguous terms are documented | KB-003 |
| KB-005 | P1 | Proposed | Create top-level navigation notes and views | Each approved top-level content area has an index/readme that explains scope and links to key model elements | KB-001, KB-002 |
| KB-006 | P1 | Proposed | Migrate content in controlled batches | Content is moved according to the approved map; links, names, and dependencies are checked after each batch | KB-002, KB-005 |
| KB-007 | P1 | Proposed | Standardize external-evidence ingestion | Source records, research synthesis, canonical elements, provenance, omitted-data inventory, and temporary-download cleanup are governed by a repeatable procedure | KB-003, KB-004 |
| KB-008 | P1 | Proposed | Build traceability views | Views make stakeholder-to-need-to-use-to-requirement-to-function-to-design-to-product-to-verification relationships inspectable | KB-003, KB-004, KB-005 |
| KB-009 | P2 | Proposed | Add model integrity reporting | Name, dependency, orphan, missing-evidence, and relationship-quality checks produce a reviewable report | KB-003, KB-004, KB-006 |
| KB-010 | P2 | Proposed | Plan internal-data comparison method | A controlled approach separates external evidence from internal data while enabling later comparison and conflict analysis | KB-003, KB-004 |

## Parking lot

Record future work here before it is prioritized. Include a short reason it may add value and links to any triggering evidence or model gap.

| Candidate work | Potential value | Trigger / related notes |
| --- | --- | --- |
| Add lifecycle/status governance for claims and relationships | Makes provisional, verified, superseded, and disputed model knowledge visible | KB-003, KB-004 |
| Develop reusable model-query views by product, stakeholder, and evidence confidence | Improves review readiness and exposes gaps in traceability | KB-005, KB-008 |

### Business and roadmap-data candidates (added 2026-10-04)

Topics and data that are thin or absent in the vault and would inform two-year engineering roadmap decisions. Each item is a candidate, not a commitment. Dates and figures were taken from public sources on 2026-10-04 and should get source records under KB-007 before being used as evidence.

#### Topic gaps

| Candidate work | Potential value | Trigger / related notes |
| --- | --- | --- |
| Assess OEM-integrated battery and charger offers (OEMs moving power in-house) | Hyster now sells factory-validated integrated lithium batteries and chargers and positions them against third-party power; this tests the "powered by PosiCharge" channel | <https://www.hyster.com/en-us/north-america/why-hyster/press-releases/2026/hyster-unveils-lithium-ion-power-solutions-designed-to-provide-turnkey-seamless-experience-from-a-single-source/>; [[PosiCharge]]; open conflict C18 in [[Battery Product Landscape Conflicts and Open Questions]] |
| Model the lead-acid to lithium transition rate by segment | Lead-acid was about 70% of 2025 forklift battery share (published estimates range from about 54% to 70%); this sets how long mixed-chemistry support, monitoring, and ID products stay central | <https://www.mordorintelligence.com/industry-reports/forklift-battery-market>; [[PosiCharge Market Segments and Jobs-to-Be-Done]] |
| Track regulations that drive demand (CARB Zero-Emission Forklift rule, LCFS electricity reporting) | CARB phases out existing propane/gas forklifts from 2028 to 2038; LCFS needs metered forklift electricity data, which may be a charger or PosiLink feature | <https://ww2.arb.ca.gov/sites/default/files/2026-04/ZEF%20Brochure.pdf>; <https://ww2.arb.ca.gov/sites/default/files/2026-04/Guidance%2020-03%20-%202026%20Update.pdf> |
| Map EU Battery Regulation digital battery passport obligations | Applies from 2027-02-18 to industrial batteries over 2 kWh; affects battery-mounted ID/monitoring data and partner battery makers | <https://single-market-economy.ec.europa.eu/news/guidance-support-preparations-digital-batteries-passport-2026-08-21_en> |
| Map product cybersecurity obligations (EU Cyber Resilience Act, IEC 62443, SBOM, secure OTA) | CRA reporting applied from 2026-09-11; full rules from 2027-12-11; affects connected chargers, monitors, and PosiLink | <https://cms.law/en/int/legal-updates/ready-respond-report-the-cyber-resilience-act-s-reporting-regime-is-here> |
| Add tariff, sourcing, and component-obsolescence research | No tariff, cost-of-goods, or end-of-life coverage exists; Section 301 tariffs on Chinese non-EV lithium-ion batteries rose from 7.5% to 25% | <https://www.cambridge.org/core/journals/american-journal-of-international-law/article/president-biden-adds-increases-and-maintains-tariffs-on-chinese-goods-levied-by-president-trump/7932886F65891411ED22DFAB22136BCD> |
| Cover site energy economics (demand charges, peak shaving, utility make-ready and rebates) | Fast charging raises site peak demand; utility rebates exist for lithium forklifts | <https://afdc.energy.gov/utility-finder?button=&page=6&search_type=state&state=&zip=>; possible overlap with staging folders `_EMS Research/` and `_Cost Driver Research/Cost Driver 08 Utilities and Energy.md` (not yet migrated; reconcile, do not duplicate) |
| Add fire-code and AHJ treatment of lithium charging areas (NFPA 855 2026 edition and related codes) | Site approval can block or delay deployments; may justify charger safety features | <https://www.nfpa.org/codes-and-standards/nfpa-855-standard-development/855> |
| Define charging-interface needs for AMRs, AGVs, and autonomous trucks (auto-docking, hands-free connection, ISO 3691-4 context) | Autonomous fleets rely on automatic opportunity charging; AGVs are mentioned in the vault but have no charging requirements | <https://www.sourcebyspec.com/encyclopedia/amr-robot.html> |
| Plan cellular network-lifetime and modem migration for connected products | AT&T has committed to LTE only through the end of 2027; affects cellular-connected [[PosiCharge PosiLink]] and [[PosiCharge SkyLink]] hardware, if any | <https://lte.callmc.com/past-and-future-cellular-network-sunsets/> |
| Research WMS and fleet-software integration expectations | No WMS coverage; integration may decide platform value; ties to the PosiLink and PowerCharge.NET overlap | [[Ampure Industrial Portfolio Overlap and Synergy Map]]; [[PosiCharge Opportunity Backlog]] |

#### Internal data to collect (depends on KB-010)

| Candidate work | Potential value | Trigger / related notes |
| --- | --- | --- |
| Installed-base profile by product, firmware version, chemistry, region, and age | Prioritizes sustaining work and end-of-life decisions | KB-010 |
| PosiLink usage and field telemetry (charge sessions, fault codes, uptime, utilization, chemistry mix) | Shows real feature use, early failure signals, and chemistry-transition speed | KB-010; [[PosiCharge PosiLink]] |
| Quality and service data (RMA, warranty cost, no-fault-found rate, failure modes, time between failures) | Directs reliability work with the highest cost-of-quality return | KB-010 |
| Win/loss reasons and quotes lost by feature, certification, or price | Confirms capability gaps instead of inferring them from competitor comparison | KB-010; [[PosiCharge Capability Gap Assessment]] |
| Cost of goods by product, tariff exposure per BOM line, single-source and end-of-life parts | Sets cost-down, redesign, and supply-risk priorities | KB-010 |
| Revenue and margin by product, segment, and channel (OEM-branded vs direct) | Measures exposure to OEM in-house power offers | KB-010; [[PosiCharge Competitive and Partner Landscape]] |
| Dated compliance calendar (CRA, battery passport, UL/CSA, NFPA, cellular sunsets) | Turns fixed external deadlines into must-do roadmap items | Topic-gap items above |
| Engineering capacity split (sustaining vs new product vs customer-specific) | Shows real capacity available for roadmap bets | KB-010 |
| Customer economics baseline (TCO, energy and demand cost, labor saved) | Supports value-based pricing and energy-management features | `_Cost Driver Research/` staging folder |

## Change history

- 2026-10-04 — Added business and roadmap-data candidates (topic gaps and internal data to collect) to the parking lot. Existing items unchanged. Possible overlap with unmigrated `_EMS Research/` and `_Cost Driver Research/` staging folders noted for reconciliation.
