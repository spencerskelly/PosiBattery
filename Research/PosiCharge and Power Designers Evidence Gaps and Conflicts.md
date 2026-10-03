---
type: conflict-and-gap-register
status: active
scope: PosiCharge-and-Power-Designers-current-public-portfolio
prepared: 2026-10-03
reviewer: Director of Engineering
rule: Preserve conflicting evidence and document resolution; do not silently overwrite or delete it.
---

# PosiCharge and Power Designers Evidence Gaps and Conflicts

## Triage model

| Priority | Meaning |
|---|---|
| P0 | Could materially affect near-term product, engineering, safety, compatibility, commercial, infrastructure, or strategic conclusions. Resolve before external assertions or decision-grade modeling. |
| P1 | Important for product definition, service/channel readiness, commercial model, or architecture; resolve during planned baseline completion. |
| P2 | Enabling metadata, maintenance, or scale detail. Track but do not block early portfolio synthesis. |

## Active public-evidence conflicts

| ID | Priority | Conflict | Evidence retained | Risk if unresolved | Resolution evidence needed | Status |
|---|---|---|---|---|---|---|
| `PC-PUB-001` | P0 | **SVS100 power rating conflict.** Official SVS100 page headline presents 10 kW; its technical-specification table presents 40 kW. A third-party distributor describes SVS100 as 10 kW. | `PUB-006`, `PUB-016` | Incorrect facility/infrastructure sizing, charging-time analysis, eGSE deployment modeling, sales claims, and competitor comparisons. | Current controlled SVS100 spec sheet; current part-number/configuration record; product-owner confirmation. Determine whether 40 kW is a template/copy error, system rating, or another variant. | Open |
| `PC-PUB-002` | P0 | **MVS800 vehicle-count/topology conflict.** Official headline claims up to 16 vehicles; body content repeats an eight-vehicle statement. | `PUB-009` | Incorrect eGSE system sizing, fleet capacity calculation, and competitive claims. | Current MVS800 topology/configuration guide showing server count, power-station count, port count, simultaneous charging rules, and derating/power-allocation logic. | Open |
| `PC-PUB-003` | P0 | **MVS400/MVS800 component-rating ambiguity.** Pages describe power servers at 40/80 kW but associated power-station content at 60 kW without defining how the component ratings combine. | `PUB-008`, `PUB-009` | Incorrect architecture, output-capacity, and infrastructure claims. | System topology drawing, BOM/configuration table, and controlled specifications explaining server/station/port relationships. | Open |

## P0 evidence gaps

| ID | Question / missing evidence | Decision consequence | Preferred evidence source | Status |
|---|---|---|---|---|
| `PC-GAP-001` | What is the authoritative current SKU/model/option list across PosiCharge and Power Designers? | Distinguishes current offerings from legacy web content and makes all subsequent matrix work reliable. | Active-item extract, product master, current catalog, price/configuration guide. | Open |
| `PC-GAP-002` | Which current Power Designers products/capabilities are standalone branded offerings, OEM/private-label offerings, PosiCharge-branded offerings, or manufacturing/technology capabilities only? | Determines correct portfolio boundaries, route to market, competitor/partner mapping, and strategic value of the acquisition. | Current Power Designers catalog/site export, product roadmap, product-owner confirmation, OEM/private-label mapping. | Open |
| `PC-GAP-003` | What is the definitive product and data-flow boundary among BMID, PosiGuard, Battery Rx, PosiLink, SkyLink, PosiConnect, and E-Meter? | Essential for roadmap, integration, sales positioning, security, support, and competitive analysis. | Current system architecture/data-flow diagrams, product one-pagers, SKU/price map, release notes, API documentation. | Open |
| `PC-GAP-004` | Which charger products support which battery chemistry, nominal voltage/capacity envelope, connectors, BMID generation, BMS/CAN protocol, vehicle conversion, and charging profile? | Needed for safety, application engineering, service, product architecture, qualification, and customer commitments. | Compatibility matrix, installation manuals, interface specifications, application engineering rules. | Open |
| `PC-GAP-005` | Which certifications, safety ratings, ingress ratings, and regional approvals apply to each exact product/configuration? | Required for compliant product statements, deployment, channel readiness, and design decisions. | Certificates, declarations, NRTL files, regional compliance matrix. | Open |

## P1 evidence gaps

| ID | Question / missing evidence | Decision consequence | Preferred evidence source | Status |
|---|---|---|---|---|
| `PC-GAP-006` | What are standard vs. optional monitoring, connectivity, cloud, fleet, and analytics features, and what are the related commercial terms? | Separates included capabilities from optional hardware, installation, subscription, gateway, and service offerings. | Price/configuration guide, service descriptions, SaaS agreement, feature matrix. | Open |
| `PC-GAP-007` | What are the supported installation, commissioning, field service, RMA, warranty, and firmware-update models? | Drives total cost, supportability, dealer/channel readiness, engineering requirements, and lifecycle risk. | Installation/service manuals, training material, warranty policy, field procedures. | Open |
| `PC-GAP-008` | Which public claims are inherited from historical product generations instead of current production configurations? | Prevents legacy-content contamination of technical/product/competitive analysis. | Revision-controlled manuals/specs, lifecycle/change-control records, product-owner review. | Open |
| `PC-GAP-009` | What are PosiLink and SkyLink integrations, API/export functions, data retention, user roles, hosting, and cyber/privacy posture? | Required for fleet-platform positioning, enterprise integration, cybersecurity review, and service model. | Architecture, security documents, API docs, customer agreement, data-processing documentation. | Open |
| `PC-GAP-010` | What are E-Meter’s hardware architecture, measurement variables, accuracy, calibration, installation method, interface, and lifecycle status? | Needed to assess fleet-assessment usefulness, technical overlap, and potential product integration. | Product specification, installation manual, test/calibration documentation, product-owner review. | Open |

## P2 evidence gaps

| ID | Question / missing evidence | Decision consequence | Preferred evidence source | Status |
|---|---|---|---|---|
| `PC-GAP-011` | What is the exact SKU, technical rating, compatibility, and service structure of each accessory/conversion product? | Enables a complete solution/BOM/service model and avoids accessory compatibility errors. | Accessory catalog, pricing/configuration guide, installation manuals. | Open |
| `PC-GAP-012` | What are current public and internal lifecycle states for every product family and variant? | Supports replacement/upgrade decisions and prevents sale/support of obsolete configurations. | Lifecycle matrix, active-item status, engineering change history. |Open |
| `PC-GAP-013` | What is the geographic availability, local certification, channel, and support footprint of each offering? | Needed for addressable-market, channel, and deployment feasibility analysis. | Regional offering matrix, distributor/OEM authorization records, compliance matrix. | Open |

## Resolution protocol

For every resolution:

1. Add the new primary or controlled source to [[Research/PosiCharge and Power Designers Public Evidence Register]].
2. Retain the original conflicting claims and cite the source IDs.
3. Record the conclusion, reviewer, date, scope of applicability, and remaining limitation.
4. Update affected baseline rows and comparison matrices.
5. If the evidence alters strategic or technical conclusions, add an entry to [[Research/Research Change and Decision Tracker]].

## Related

- [[Research/PosiCharge and Power Designers Current Portfolio Baseline]]
- [[Research/PosiCharge and Power Designers Public Evidence Register]]
- [[Research/Battery Product Landscape Conflicts and Open Questions]]
- [[Research/Research Change and Decision Tracker]]
- [[Research/Knowledge Base Next Steps]]
