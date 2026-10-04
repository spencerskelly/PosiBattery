---
type: Info
subtype:
id: INFO-00236
uid: 20261003143453031skellyspencer
status: Draft
tags:
  - business-analysis
  - evidence-gaps
describes:
  - "[[PosiCharge]]"
  - "[[Power Designers]]"
---

# PosiCharge and Power Designers Evidence Gaps and Conflicts

## Definition

Research working note: PosiCharge and Power Designers Evidence Gaps and Conflicts.

## Notes

### Triage model

| Priority | Meaning |
|---|---|
| P0 | Could materially affect near-term product, engineering, safety, compatibility, commercial, infrastructure, or strategic conclusions. Resolve before external assertions or decision-grade modeling. |
| P1 | Important for product definition, service/channel readiness, commercial model, or architecture; resolve during planned baseline completion. |
| P2 | Enabling metadata, maintenance, or scale detail. Track but do not block early portfolio synthesis. |

### Active public-evidence conflicts

Conflicts now live in the single vault register, [[Battery Product Landscape Conflicts and Open Questions]], so they are not kept in two places. The owner ids are kept here for reference:

| Owner id | Register id | Priority | Short description | Status |
|---|---|---|---|---|
| `PC-PUB-001` | C77 | P0 | SVS100 power rating conflict | Resolved for the current sheet (10 kW); web page not rechecked (round 20) |
| `PC-PUB-002` | C78 | P0 | MVS800 vehicle-count/topology conflict | Resolved by the sheets: MVS800 16, MVS400 8 (round 20) |
| `PC-PUB-003` | C79 | P0 | MVS400/MVS800 component-rating ambiguity | Partly resolved: powerserver and powerstation are separate components; combination rule not stated (round 20) |
| `PC-PUB-004` | C80 | P1 | DVS400 input current equals DVS300 | Open |
| `PC-PUB-005` | C81 | P1 | High Voltage Power Station 20 kW versus 30 kW | Open |
| `PC-PUB-006` | C82 | P1 | High Voltage Power Station (AC) listing links a DC card | Open |
| `PC-PUB-007` | C83 | P1 | PosiGuard operating voltage 18-20 V versus 18-120 V | Open |

Full text, evidence retained, risk and resolution evidence needed are in the register entries. Resolution protocol below still applies.

### P0 evidence gaps

| ID | Question / missing evidence | Decision consequence | Preferred evidence source | Status |
|---|---|---|---|---|
| `PC-GAP-001` | What is the authoritative current SKU/model/option list across PosiCharge and Power Designers? | Distinguishes current offerings from legacy web content and makes all subsequent matrix work reliable. | Active-item extract, product master, current catalog, price/configuration guide. | Open |
| `PC-GAP-002` | Which current Power Designers products/capabilities are standalone branded offerings, OEM/private-label offerings, PosiCharge-branded offerings, or manufacturing/technology capabilities only? | Determines correct portfolio boundaries, route to market, competitor/partner mapping, and strategic value of the acquisition. | Current Power Designers catalog/site export, product roadmap, product-owner confirmation, OEM/private-label mapping. | Open |
| `PC-GAP-003` | What is the definitive product and data-flow boundary among BMID, PosiGuard, Battery Rx, PosiLink, SkyLink, PosiConnect, and E-Meter? | Essential for roadmap, integration, sales positioning, security, support, and competitive analysis. | Current system architecture/data-flow diagrams, product one-pagers, SKU/price map, release notes, API documentation. | Open |
| `PC-GAP-004` | Which charger products support which battery chemistry, nominal voltage/capacity envelope, connectors, BMID generation, BMS/CAN protocol, vehicle conversion, and charging profile? | Needed for safety, application engineering, service, product architecture, qualification, and customer commitments. | Compatibility matrix, installation manuals, interface specifications, application engineering rules. | Open |
| `PC-GAP-005` | Which certifications, safety ratings, ingress ratings, and regional approvals apply to each exact product/configuration? | Required for compliant product statements, deployment, channel readiness, and design decisions. | Certificates, declarations, NRTL files, regional compliance matrix. | Open |

### P1 evidence gaps

| ID | Question / missing evidence | Decision consequence | Preferred evidence source | Status |
|---|---|---|---|---|
| `PC-GAP-006` | What are standard vs. optional monitoring, connectivity, cloud, fleet, and analytics features, and what are the related commercial terms? | Separates included capabilities from optional hardware, installation, subscription, gateway, and service offerings. | Price/configuration guide, service descriptions, SaaS agreement, feature matrix. | Open |
| `PC-GAP-007` | What are the supported installation, commissioning, field service, RMA, warranty, and firmware-update models? | Drives total cost, supportability, dealer/channel readiness, engineering requirements, and lifecycle risk. | Installation/service manuals, training material, warranty policy, field procedures. | Open |
| `PC-GAP-008` | Which public claims are inherited from historical product generations instead of current production configurations? | Prevents legacy-content contamination of technical/product/competitive analysis. | Revision-controlled manuals/specs, lifecycle/change-control records, product-owner review. | Open |
| `PC-GAP-009` | What are PosiLink and SkyLink integrations, API/export functions, data retention, user roles, hosting, and cyber/privacy posture? | Required for fleet-platform positioning, enterprise integration, cybersecurity review, and service model. | Architecture, security documents, API docs, customer agreement, data-processing documentation. | Open |
| `PC-GAP-010` | What are E-Meter’s hardware architecture, measurement variables, accuracy, calibration, installation method, interface, and lifecycle status? | Needed to assess fleet-assessment usefulness, technical overlap, and potential product integration. | Product specification, installation manual, test/calibration documentation, product-owner review. | Open |

### P2 evidence gaps

| ID | Question / missing evidence | Decision consequence | Preferred evidence source | Status |
|---|---|---|---|---|
| `PC-GAP-011` | What is the exact SKU, technical rating, compatibility, and service structure of each accessory/conversion product? | Enables a complete solution/BOM/service model and avoids accessory compatibility errors. | Accessory catalog, pricing/configuration guide, installation manuals. | Open |
| `PC-GAP-012` | What are current public and internal lifecycle states for every product family and variant? | Supports replacement/upgrade decisions and prevents sale/support of obsolete configurations. | Lifecycle matrix, active-item status, engineering change history. |Open |
| `PC-GAP-013` | What is the geographic availability, local certification, channel, and support footprint of each offering? | Needed for addressable-market, channel, and deployment feasibility analysis. | Regional offering matrix, distributor/OEM authorization records, compliance matrix. | Open |

### Resolution protocol

For every resolution:

1. Add the new primary or controlled source to [[PosiCharge and Power Designers Public Evidence Register]].
2. Retain the original conflicting claims and cite the source IDs.
3. Record the conclusion, reviewer, date, scope of applicability, and remaining limitation.
4. Update affected baseline rows and comparison matrices.
5. If the evidence alters strategic or technical conclusions, add an entry to [[Research Change and Decision Tracker]].

### Related

- [[PosiCharge and Power Designers Current Portfolio Baseline]]
- [[PosiCharge and Power Designers Public Evidence Register]]
- [[Battery Product Landscape Conflicts and Open Questions]]
- [[Research Change and Decision Tracker]]
- [[Knowledge Base Next Steps]]

### Original document properties

Carried over unchanged from the note's earlier frontmatter (the model status is Draft until a person changes it):

  - type: conflict-and-gap-register
  - status: active
  - scope: PosiCharge-and-Power-Designers-current-public-portfolio
  - prepared: 2026-10-03
  - reviewer: Director of Engineering
  - rule: Preserve conflicting evidence and document resolution; do not silently overwrite or delete it.
- **Round 20 (2026-10-03):** the owner uploaded the current PosiCharge sheets; resolutions and four new conflicts (PC-PUB-004 to 007, register C80 to C83) are recorded above and in the central register. Extraction was by AI; reviewer sign-off is still needed.

## Aliases

## Former ids
