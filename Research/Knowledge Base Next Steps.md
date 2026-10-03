---
type: knowledge-base-backlog
status: active
created: 2026-10-03
last-reviewed: 2026-10-03
purpose: Persistent, prioritized next-step list for expanding the PosiBattery knowledge base. Add newly identified work here unless it belongs in a more specific existing backlog; preserve conflicts rather than silently deleting them.
---

# Knowledge Base Next Steps

## Operating rules

- This is the repository-wide working list for knowledge-base expansion actions identified during reviews and research.
- Keep each action outcome-oriented, evidence-aware, and linked to the affected notes or artifacts.
- Use `P0` for work that can materially change near-term strategic, technical, commercial, or safety conclusions; use `P1` for high-value follow-on work; use `P2` for enabling, maintenance, and scale work.
- Record conflicting evidence in a conflict register and retain both the conflict and its disposition.
- When work is completed, move it to the Completed section with a completion date and links to the resulting artifacts. Do not delete history.

## P0 — Decision-grade baseline

- [ ] **Complete the verified PosiCharge and Power Designers current-state product and variant baseline.** Public-evidence draft captured in [[Research/PosiCharge and Power Designers Current Portfolio Baseline]]. Reconcile current and relevant active offerings against the internal product/SKU master; add lifecycle state, target applications, chemistry/voltage/capacity envelope, charging/interface compatibility, monitoring functions, communications, mechanical/environmental constraints, certifications, service model, channels, and known deployments. Attach source, evidence class, confidence, reviewer, and last-verified date for every material claim.  
  **Current progress:** Public first pass complete; product-master and controlled-document reconciliation pending.  
  **Completion criteria:** A product manager or engineer can establish what PosiCharge/Power Designers currently sell, to whom, under which constraints, and with what verified evidence without reconciling multiple notes.  
  **Related:** [[Research/PosiCharge and Power Designers Current Portfolio Baseline]], [[Research/PosiCharge and Power Designers Public Evidence Register]], [[Organizations/PosiCharge]], [[Organizations/Power Designers]], [[Research/PosiCharge BMID Variants]], [[Research/PosiCharge Business Scope and Portfolio]], [[Research/PosiCharge Product Comparison Matrix]]

- [ ] **Resolve public-evidence product conflicts `PC-PUB-001` through `PC-PUB-003`.** Preserve existing source claims, then obtain controlled current specifications/configuration records to resolve: SVS100’s 10 kW versus 40 kW rating; MVS800’s eight versus 16-vehicle claim; and MVS400/MVS800 power-server versus power-station rating/topology ambiguity.  
  **Completion criteria:** Each conflict has a disposition, source basis, applicability boundary, reviewer, date, and all affected baseline/matrix records are updated without deleting historical conflict evidence.  
  **Related:** [[Research/PosiCharge and Power Designers Evidence Gaps and Conflicts]], [[Research/PosiCharge and Power Designers Public Evidence Register]]

- [ ] **Enumerate and classify the current Power Designers portfolio and its relationship to PosiCharge.** Establish whether each acquired product/capability is a Power Designers-branded, PosiCharge-branded, Ampure-branded, OEM/private-label, manufacturing-only, software-only, active, or legacy element.  
  **Completion criteria:** An authoritative current Power Designers portfolio map exists, including product families, branding/route-to-market, lifecycle, owner, and evidence source.  
  **Related:** [[Organizations/Power Designers]], [[Research/PosiCharge and Power Designers Current Portfolio Baseline]], [[Research/PosiCharge and Power Designers Evidence Gaps and Conflicts]]

- [ ] **Define and validate the connected-product architecture.** Establish the product and data-flow boundaries among BMID, PosiGuard, Battery Rx, PosiLink, SkyLink, PosiConnect, and E-Meter, including hardware, communications, configuration, cloud/fleet function, interfaces, security ownership, commercial/product boundaries, and lifecycle relationships.  
  **Completion criteria:** A reviewed system/data-flow diagram and product-boundary matrix identify confirmed interfaces, assumptions, incompatibilities, ownership, and validation needs.  
  **Related:** [[Research/PosiCharge and Power Designers Current Portfolio Baseline]], [[Research/PosiCharge and Power Designers Evidence Gaps and Conflicts]], [[Research/PosiCharge BMID Variants]]

- [ ] **Define a canonical, normalized product-attribute facts schema.** Create a controlled vocabulary and structured facts layer for products and variants; include manufacturer, family/model, asset application, chemistry, voltage/capacity, charging and connector interface, monitoring functions, communications, fleet integration, certifications, service model, lifecycle status, and source evidence.  
  **Completion criteria:** Populate PosiCharge’s offering set plus five priority competitor or partner product families; demonstrate a reproducible filtered comparison view.  
  **Related:** [[Products/BASE_all_Products.base]], [[Research/Battery Comparison Matrix]], [[Research/Charger Comparison Matrix]], [[Research/Monitor Comparison Matrix]], [[Research/Truck Device Comparison Matrix]]

- [ ] **Establish a source-evidence confidence and freshness model.** Define evidence tiers; add source type, claim confidence, verification date, and review-by date to material findings. Set review cadence for technical specifications/certifications, organization/channel relationships, availability/pricing signals, and strategic hypotheses.  
  **Current progress:** Draft evidence classes and source register created for PosiCharge/Power Designers public baseline.  
  **Completion criteria:** The standard is documented and applied to the PosiCharge baseline plus priority comparison-matrix records.  
  **Related:** [[Research/PosiCharge and Power Designers Public Evidence Register]], [[Research/Landscape Evidence and Modeling Conventions]], [[Research/Document Wishlist]], [[Research/Link Audit]], [[Source Documents]]

## P1 — Strategic synthesis and validation

- [ ] **Build a segment → job → requirement → offering → gap → response traceability matrix.** Start with the highest-priority PosiCharge target segment and map operational jobs, pain points, measurable requirements, current solutions, unmet needs, and credible PosiCharge responses. Include buyer/buying path, switching barriers, and evidence strength.  
  **Completion criteria:** At least one priority segment has a decision-ready traceability model that identifies and ranks response hypotheses.  
  **Related:** [[Research/PosiCharge Market Segments and Jobs-to-Be-Done]], [[Research/PosiCharge Business Scope and Portfolio]], [[Research/PosiCharge Capability Gap Assessment]], [[Research/Function Map]], [[Research/Design Map]]

- [ ] **Create priority organization strategic profiles and an ecosystem map.** Rank the organizations most likely to be partners, channels, suppliers, integration dependencies, competitors, or strategic threats. For each, record roles, portfolio overlap/complementarity, relationship evidence, customer/segment access, integration prerequisites, commercial risks, recommended posture, and the next intelligence action.  
  **Completion criteria:** A ranked top-ten ecosystem map exists, with an explicit partner/qualify/monitor/compete/displace/deprioritize recommendation per organization.  
  **Related:** [[Organizations/Business Relationship Ledger]], [[Organizations/Offerings by Organization]], [[Research/PosiCharge Competitive and Partner Landscape]]

- [ ] **Score opportunities as investment hypotheses and define validation plans.** Apply a weighted model covering strategic fit, validated customer pain/willingness to pay, market access/channel leverage, differentiation durability, technical feasibility, certification/service burden, and time to test/revenue. Turn the top five into bounded validation experiments.  
  **Completion criteria:** Each top-five opportunity has a score, assumptions, evidence gaps, named owner, decision gate, and a time-bounded validation plan.  
  **Related:** [[Research/PosiCharge Opportunity Backlog]], [[Research/Investigation Backlog]], [[Research/PosiCharge Capability Gap Assessment]]

- [ ] **Develop an end-to-end battery/charger/vehicle/monitor/fleet integration architecture matrix.** Capture electrical, mechanical, control, communications, safety/compliance, and service interfaces across target vehicle, battery, charger, BMID/monitor, and fleet-platform configurations. Identify ownership boundaries and hidden interoperability risks.  
  **Completion criteria:** One priority deployment architecture is mapped with verified interfaces, assumptions, incompatibilities, and required validation tests.  
  **Related:** [[Research/Function Map]], [[Research/Design Map]], [[Research/Function and Design Levels]], [[Research/ICE and Fuel Cell Feature Gap Review]]

- [ ] **Acquire the highest-value missing primary documents.** Prioritize manuals, wiring/interface documents, application guides, certification records, warranty/service documents, compatibility lists, and official product catalogs required to resolve P0 conflicts and populate the canonical facts layer.  
  **Initial acquisition order:** SVS100 spec/configuration record; MVS400/MVS800 topology and spec documentation; High Voltage Power Station AC/DC spec sheets; PosiLink and Battery Rx product sheets; ProCore Edge controlled manuals/tool documents; DVS100 current official evidence.  
  **Completion criteria:** The document wishlist is ranked by decision impact and each P0 dependency has a source-acquisition path or documented access limitation.  
  **Related:** [[Research/PosiCharge and Power Designers Public Evidence Register]], [[Research/PosiCharge and Power Designers Evidence Gaps and Conflicts]], [[Research/Document Wishlist]], [[Source Documents]], [[Downloads]]

## P2 — Commercial intelligence and operating system

- [ ] **Add commercial, lifecycle, and service intelligence for priority entities.** Capture lifecycle status, geographic availability, support footprint, channel model, warranty/service responsibility, lead-time and supply-chain signals, pricing bands with confidence, installation/service economics, installed-base indicators, and upgrade/replacement risk.  
  **Completion criteria:** Commercial/lifecycle fact sheets exist for PosiCharge and the priority competitor/partner set.  
  **Related:** [[Organizations]], [[Products]], [[Research/Battery Product Landscape]]

- [ ] **Operationalize research execution in GitHub Issues.** Create issues for P0/P1 evidence gaps and research tasks, with labels for conflict, evidence gap, source needed, product, organization, integration, market, opportunity, priority, and blocked status. Include decision consequence, evidence threshold, linked notes, expected artifact, owner, due date, and closure condition.  
  **Completion criteria:** All P0 actions and selected P1 actions are represented as auditable issues or an equivalent tracked work system, with review cadence defined.  
  **Related:** [[Research/Investigation Backlog]], [[Research/Research Change and Decision Tracker]]

- [ ] **Implement a recurring KB quality and freshness review.** Review high-impact claims, stale sources, unresolved conflicts, orphaned product records, broken links, and duplicate/inconsistent terminology on a defined cadence.  
  **Completion criteria:** A recurring review checklist and review log are in place; the first review produces a dated set of corrective actions.  
  **Related:** [[Research/Link Audit]], [[Research/Note Reuse Audit]], [[Research/Landscape Evidence and Modeling Conventions]]

## Suggested first sprint

- [x] Conduct an initial public-evidence inventory for current PosiCharge and Power Designers portfolio representation; capture source/evidence and open conflicts. Completed 2026-10-03: [[Research/PosiCharge and Power Designers Current Portfolio Baseline]], [[Research/PosiCharge and Power Designers Public Evidence Register]], and [[Research/PosiCharge and Power Designers Evidence Gaps and Conflicts]].
- [ ] Convert the top 20 unresolved conflicts into the conflict register and identify the five highest-impact items.
- [ ] Create the canonical facts schema and populate it for PosiCharge plus five priority competitor/partner product families.
- [ ] Produce one segment-to-offering traceability matrix for the highest-priority target segment.
- [ ] Create a top-ten ecosystem priority map and strategic-profile template.
- [ ] Create tracked work items for the P0 actions and selected P1 evidence gaps.

## Completed

- 2026-10-03 — Created a public-evidence baseline, evidence register, and gaps/conflicts register for current PosiCharge and Power Designers product/capability research. The work includes P0 records for SVS100 rating conflict, MVS800 vehicle-count conflict, MVS component-rating ambiguity, Power Designers portfolio enumeration, current product/SKU master reconciliation, and connected-product architecture clarification. See [[Research/PosiCharge and Power Designers Current Portfolio Baseline]], [[Research/PosiCharge and Power Designers Public Evidence Register]], and [[Research/PosiCharge and Power Designers Evidence Gaps and Conflicts]].
