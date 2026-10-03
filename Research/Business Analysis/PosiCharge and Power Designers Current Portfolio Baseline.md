---
type: Info
subtype:
id: INFO-00234
uid: 20261003143453029skellyspencer
status: Draft
tags:
  - business-analysis
  - baseline
describes:
  - "[[PosiCharge]]"
  - "[[Power Designers]]"
---

# PosiCharge and Power Designers Current Portfolio Baseline

## Definition

This is a public-evidence baseline of product families currently represented on official PosiCharge pages and resources as of 2026-10-03. It is a working internal-review artifact, not an approved product master, current price list, configuration guide, or external claim set.

## Notes

### Purpose and scope

Scope decisions:

- Include current PosiCharge and Power Designers products/capabilities where public evidence supports their current representation.
- Start broad: MHE charging, eGSE charging, battery monitoring, mobile configuration, cloud/fleet platforms, fleet optimization, and relevant accessories.
- Use public primary sources first. Record unclear claims and gaps rather than filling them with inference.
- Treat a public product-page listing as evidence of public representation, not proof that every SKU, option, geography, or configuration is currently orderable.

### Evidence terminology

| Status | Meaning |
|---|---|
| Verified public | Directly supported by an official current page, resource listing, official app listing, or official press release. |
| Publicly indicated | Supported by a public secondary source or historical/manual reference, but not yet reconciled to an official current product master. |
| Unclear / conflict | Public evidence is missing, ambiguous, or internally inconsistent. Do not use as a decision-grade claim without resolution. |
| Internal verification required | Expected to be available from controlled product, engineering, commercial, service, or compliance evidence. |

### Portfolio overview

| Domain | Current publicly represented families / products | Baseline confidence |
|---|---|---|
| Material-handling charging | ProCore Edge; DVS100; DVS150 | Mixed: strong for ProCore Edge and DVS150; DVS100 requires current official confirmation |
| Airport ground-support equipment charging | SVS100; DVS300/330/400; MVS400; MVS800; High Voltage Power Station AC; High Voltage Power Station DC | Strong family-level representation; configuration/topology details require controlled documentation |
| Battery edge monitoring | PosiGuard; BMID/BMID-related tools | Strong for PosiGuard; current BMID generations and compatibility need confirmation |
| Mobile field configuration | PosiConnect | Strong public description; enterprise control/security details need confirmation |
| Cloud fleet and charger reporting | PosiLink; SkyLink | Both publicly represented; product and architecture boundary is not yet clear |
| Fleet assessment / optimization | E-Meter | Publicly represented; hardware/data architecture is not yet clear |
| Accessories and conversion | Extended/custom modular charge cables; charger stand/handler kits; automatic battery watering; DIY Fast Charge Kit; stack light; Cooling Fan Box | Publicly listed; compatible products, ratings, SKUs, and ordering structure require confirmation |
| Power Designers | Acquisition adds industrial charging/electronics manufacturing capability, configurations, OEM relationships, predictive analytics, and energy-demand-management software | In scope, but current standalone product-family evidence is not yet enumerated |

### Product-family baseline

#### Material-handling charging

| Product family | Verified public facts | Confidence | Required internal/public gap closure |
|---|---|---|---|
| ProCore Edge | Facts and sources are on [[PosiCharge ProCore Edge]] | Verified public—family level | Current SKU/option master; certification and regional configuration matrix; chemistry/BMS/connector/BMID interoperability; active firmware and software versions; installation and service policy. |
| DVS150 | Facts and sources are on [[PosiCharge DVS150]] | Verified public—product level | Current commercial model/ordering codes; chemistry and capacity envelope; output connector options; exact certifications; BMID/communications interfaces; relationship to DVS100. |
| DVS100 | Facts and sources are on [[PosiCharge DVS100]] | Publicly indicated only | Confirm current product existence with current official page/spec sheet; establish SKU, ratings, certifications, and relationship to DVS150 before relying on these specifications. |

#### Airport ground-support equipment charging

| Product family | Verified public facts | Confidence | Required internal/public gap closure |
|---|---|---|---|
| SVS100 | Facts and sources are on [[PosiCharge SVS100]] | Verified public, with P0 rating conflict | Resolve whether rated power is 10 kW, 40 kW, or configuration-dependent; obtain current controlled spec sheet, part-number structure, approved eGSE applications, certifications, and accessory/interface list. |
| DVS300/330/400 | Facts and sources are on [[PosiCharge DVS300 Series]] | Verified public—family level | Resolve 300/330/400 configuration mapping; confirm current/output limits, power-sharing conditions, GBT board scope, eGSE/OEM compatibility, connectors, certifications, current BMID generation/protocol, and geographic availability. |
| MVS400 | Facts and sources are on [[PosiCharge MVS400 and MVS800]] | Verified public—system level | Obtain topology/configuration guide; explain power-server vs. power-station rating, valid port counts, output allocation, installation architecture, connector choices, and current commercial configuration. |
| MVS800 | Facts and sources are on [[PosiCharge MVS400 and MVS800]] | Verified public—system level, with P0 topology conflict | Resolve whether system supports 8 or 16 vehicles, why associated power-station text states 60 kW, and the valid topology/power-allocation rules. |
| High Voltage Power Station—AC | Facts and sources are on [[PosiCharge High Voltage Power Station (AC)]] | Verified public—listing level | Obtain and extract controlled/current spec sheet; define ratings, topology, interfaces, application, certification, and commercial status. |
| High Voltage Power Station—DC | Facts and sources are on [[PosiCharge High Voltage Power Station (DC)]] | Verified public—listing level | Obtain and extract controlled/current spec sheet; define ratings, AC/DC boundary, interfaces, application, certification, option structure, and commercialization status. |

#### Battery, mobile, fleet, and energy products

| Product family | Verified public facts | Confidence | Required internal/public gap closure |
|---|---|---|---|
| PosiGuard | Facts and sources are on [[PosiCharge PosiGuard]] | Verified public—product level | Current SKU/variant/sensor configurations; supported BMS/CAN protocols; LoRa band/gateway requirements; data model/API; cloud/service plan; cybersecurity; firmware/update pathway; connector/wiring diagrams. |
| BMID / related tools | Public charger pages and resource titles show BMID recognition/tooling. Public PosiGuard and PosiConnect materials show the product family is used for battery identification/monitoring and configuration. | Verified public—functional level | Current BMID generation lineup, part numbers, compatibility matrix, physical/electrical interfaces, firmware variants, distinction from PosiGuard, service/replacement status. |
| PosiConnect | Facts and sources are on [[PosiCharge PosiConnect]] | Verified public—product level | Supported OS/device versions; authentication/identity lifecycle; role permissions; update security; offline behavior; data export and synchronization; service and support ownership. |
| PosiLink | Facts and sources are on [[PosiCharge PosiLink]] | Verified public—family level | Retrieve current product/spec documentation; define product/service boundary, subscription/commercial model, hosting, retention, API/integration, user roles, alerts, cyber/privacy posture, and relation to SkyLink. |
| SkyLink | Facts and sources are on [[PosiCharge SkyLink]] | Verified public—product level | Define relationship to PosiLink; supported chargers/BMID generations; deployment/onboarding; data retention; API/export; security/cyber model; user-role and commercial model. |
| E-Meter | Facts and sources are on [[PosiCharge E-Meter]] | Verified public—product level | Hardware architecture, installation method, measurement variables/accuracy/calibration, interfaces, current generation, connectivity/data export, compatibility, and relationship to PosiGuard/PosiLink/SkyLink. |
| Battery Rx | Facts and sources are on [[PosiCharge Battery Rx]] | Verified public—listing/family level | Obtain current controlled product sheet; resolve hardware/software/service architecture, relationship to PosiGuard, supported chemistry/data acquisition, SKU/lifecycle state, and interfaces. |

#### Accessories and conversion products

| Product / family | Verified public facts | Confidence | Required internal/public gap closure |
|---|---|---|---|
| Extended/custom modular charge cables | Facts and sources are on [[PosiCharge Modular Charge Cables]] | Verified public—listing level | Connector families; cable gauge; voltage/current ratings; certification; compatible chargers; custom-order limits. |
| Charger stand kit / cable handler | Facts and sources are on [[PosiCharge Charger Stand Kit and Cable Handler]] | Verified public—listing level | Mechanical variants, mounting requirements, cable/chassis compatibility, orderable kits, safety/environmental ratings. |
| Single-point automatic battery watering | Facts and sources are on [[PosiCharge Single-Point Automatic Battery Watering]] | Verified public—listing level | Supported battery types, water source/interface, required charger option, control/sensor logic, installation/service/safety requirements. |
| DIY Fast Charge Kit | Facts and sources are on [[PosiCharge DIY Fast Charge Kit]] | Verified public—listing level | Eligible vehicle models; qualification requirement; kit contents; connector/BMID configuration; warranty and compliance responsibility; current commercial status. |
| Three-color stack light | Facts and sources are on [[PosiCharge Three-Color Stack Light]] | Verified public—listing level | Electrical interface; compatible products; mounting options; current SKU; environmental/regulatory rating. |
| Cooling Fan Box | Facts and sources are on [[PosiCharge Cooling Fan Box]] | Verified public—listing level | Thermal performance, compatible configurations, installation/control requirements, serviceability, current status; verify product-page text for potential copy inconsistency. |

### Connected-product working architecture

This is a public-evidence working model. It is not a verified internal architecture.

```text
Battery / battery sensors
  → PosiGuard or BMID-family edge device
    → local configuration: PosiConnect via Bluetooth / QR / search
    → battery/fleet platform: PosiLink

Charger / charger energy and charge-session data
  → SkyLink cloud reporting and remote-support functions

Existing-fleet energy and usage assessment
  → E-Meter reports and analysis
```

The relationship among PosiLink, SkyLink, E-Meter, Battery Rx, and current BMID/PosiGuard variants is a P0 clarification item. Public sources substantiate each element but do not fully define whether they are separate commercial products, integrated modules, customer-segment-specific tools, predecessors/successors, or interoperable layers.

### Power Designers baseline

Ampure announced acquisition of Power Designers Sibex on 2025-09-02. The announcement states that the acquisition adds industrial charging products and electronics manufacturing, additional power configurations, ISO-certified manufacturing/final assembly in Crystal River, Florida, OEM relationships, and software capabilities in predictive analytics and energy-demand management.

This establishes Power Designers as strategically relevant to the baseline. However, the public evidence collected to date does not enumerate an authoritative current Power Designers-branded product catalog or establish which acquired product/capability elements are currently commercialized under PosiCharge, Power Designers, Ampure, OEM/private-label brands, or another arrangement.

**Status:** In scope; product-family enumeration is an evidence gap, not an inferred product mapping.

### Where the facts live (round 19)

Per-product facts were moved to the product notes under [[README_Products|Products]] so each fact is stored once; this note keeps the confidence and the still-needed evidence for each family, the connected-product working architecture and the review limits.

### Review and use limits

- Do not convert this artifact directly into external collateral, product commitments, compatibility claims, or compliance assertions.
- Use it to guide evidence acquisition, internal product-master reconciliation, research prioritization, and architecture/gap analysis.
- Add resolved evidence with source, date, exact claim, and reviewer. Preserve conflicts and their disposition history.

### Related

- [[PosiCharge]]
- [[Power Designers]]
- [[PosiCharge BMID Variants]]
- [[PosiCharge Business Scope and Portfolio]]
- [[PosiCharge Product Comparison Matrix]]
- [[Document Wishlist]]
- [[Knowledge Base Next Steps]]
- [[PosiCharge and Power Designers Public Evidence Register]]
- [[PosiCharge and Power Designers Evidence Gaps and Conflicts]]

### Original document properties

Carried over unchanged from the note's earlier frontmatter (the model status is Draft until a person changes it):

  - type: research-baseline
  - status: draft-for-internal-review
  - scope: current-publicly-represented-products
  - organizations: PosiCharge, Power Designers
  - source-boundary: public evidence only
  - prepared: 2026-10-03
  - reviewer: Director of Engineering
  - confidence-policy: Preserve uncertainty and conflicts; do not infer unverified product, SKU, compatibility, certification, or availability claims.

## Aliases

## Former ids
