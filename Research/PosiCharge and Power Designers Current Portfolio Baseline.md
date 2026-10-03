---
type: research-baseline
status: draft-for-internal-review
scope: current-publicly-represented-products
organizations:
  - PosiCharge
  - Power Designers
source-boundary: public evidence only
prepared: 2026-10-03
reviewer: Director of Engineering
confidence-policy: Preserve uncertainty and conflicts; do not infer unverified product, SKU, compatibility, certification, or availability claims.
---

# PosiCharge and Power Designers Current Portfolio Baseline

## Purpose and scope

This is a public-evidence baseline of product families currently represented on official PosiCharge pages and resources as of 2026-10-03. It is a working internal-review artifact, not an approved product master, current price list, configuration guide, or external claim set.

Scope decisions:

- Include current PosiCharge and Power Designers products/capabilities where public evidence supports their current representation.
- Start broad: MHE charging, eGSE charging, battery monitoring, mobile configuration, cloud/fleet platforms, fleet optimization, and relevant accessories.
- Use public primary sources first. Record unclear claims and gaps rather than filling them with inference.
- Treat a public product-page listing as evidence of public representation, not proof that every SKU, option, geography, or configuration is currently orderable.

## Evidence terminology

| Status | Meaning |
|---|---|
| Verified public | Directly supported by an official current page, resource listing, official app listing, or official press release. |
| Publicly indicated | Supported by a public secondary source or historical/manual reference, but not yet reconciled to an official current product master. |
| Unclear / conflict | Public evidence is missing, ambiguous, or internally inconsistent. Do not use as a decision-grade claim without resolution. |
| Internal verification required | Expected to be available from controlled product, engineering, commercial, service, or compliance evidence. |

## Portfolio overview

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

## Product-family baseline

### Material-handling charging

| Product family | Verified public facts | Confidence | Required internal/public gap closure |
|---|---|---|---|
| ProCore Edge | Opportunity charger platform for forklift batteries. Public pages list 24/36/48 V variants at 6–30 kW and 48/72/80/96 V variants at 9–30 kW; 96 V is listed for lithium-ion applications only. Public capabilities include automatic multi-chemistry charging, Bluetooth diagnostics, LED status, modular/scalable power, wall/pole/free-standing installation options, and PosiLink-connected fleet tools. Resource listings reference installation, service, spare-parts, anti-arc, BMID III-B dongle, PilotTerm software-loading, and iOS updater documentation. | Verified public—family level | Current SKU/option master; certification and regional configuration matrix; chemistry/BMS/connector/BMID interoperability; active firmware and software versions; installation and service policy. |
| DVS150 | Dual-port MHE fast charger for 24–80 V batteries. Public page lists 15 kW per port, 300 A per port, 480/600 VAC input, up to 92% efficiency, 0.98 power factor, NEMA 1 enclosure, 13 ft output cable, and 250 logged charge events. Listed controls/protections include BMID, real-time clock, equalization scheduling, electrolyte-immersed thermistor, thermal foldback/shutdown, and 5 ms shutdown response. | Verified public—product level | Current commercial model/ordering codes; chemistry and capacity envelope; output connector options; exact certifications; BMID/communications interfaces; relationship to DVS100. |
| DVS100 | A public installation-manual search result describes 2 × 10 kW, 16–120 V DC output, 200 A maximum output, and 480/600 VAC variants. | Publicly indicated only | Confirm current product existence with current official page/spec sheet; establish SKU, ratings, certifications, and relationship to DVS150 before relying on these specifications. |

### Airport ground-support equipment charging

| Product family | Verified public facts | Confidence | Required internal/public gap closure |
|---|---|---|---|
| SVS100 | Single-port outdoor GSE charger. Public content lists 24–80 V batteries, BMID recognition of voltage/state of charge/temperature, automatic start/stop, anti-arcing disconnect, thermal shutdown, high-frequency IGBT conversion, NEMA 3R enclosure, and Euro/Burton connector/cable options. | Verified public, with P0 rating conflict | Resolve whether rated power is 10 kW, 40 kW, or configuration-dependent; obtain current controlled spec sheet, part-number structure, approved eGSE applications, certifications, and accessory/interface list. |
| DVS300/330/400 | Outdoor fast-charge family for airport GSE. Official page lists 30/33/40 kW variants, 24–96 V battery range, 250 A dual-vehicle output or up to 500 A single-vehicle output, 480/600 VAC three-phase input, 0.96 power factor, 90% efficiency, NEMA 3R enclosure, BMID recognition, anti-arcing disconnect, thermal protection/shutdown, jet-bridge/other-device power sharing, and RS-232. Resource content includes a China GBT interface-board manual. | Verified public—family level | Resolve 300/330/400 configuration mapping; confirm current/output limits, power-sharing conditions, GBT board scope, eGSE/OEM compatibility, connectors, certifications, current BMID generation/protocol, and geographic availability. |
| MVS400 | Multi-vehicle GSE fast-charge system. Public page lists a 40 kW power server, 24–96 V battery range, 250 A dual-mode / 500 A single-mode output, RS-232, 480/600 VAC input, 0.96 power factor, 90% efficiency, NEMA 3R, BMID recognition, power sharing, and up to eight simultaneous vehicles. | Verified public—system level | Obtain topology/configuration guide; explain power-server vs. power-station rating, valid port counts, output allocation, installation architecture, connector choices, and current commercial configuration. |
| MVS800 | Multi-vehicle GSE fast-charge system. Public page lists an 80 kW power server, 24–96 V battery range, 250 A dual-mode / 500 A single-mode output, RS-232, 0.96 power factor, 95% listed power-server efficiency, and up to 16 simultaneous vehicles. | Verified public—system level, with P0 topology conflict | Resolve whether system supports 8 or 16 vehicles, why associated power-station text states 60 kW, and the valid topology/power-allocation rules. |
| High Voltage Power Station—AC | Listed as a current eGSE product; resource library lists an AC spec sheet. | Verified public—listing level | Obtain and extract controlled/current spec sheet; define ratings, topology, interfaces, application, certification, and commercial status. |
| High Voltage Power Station—DC | Listed as a current eGSE product; resource library lists a DC spec sheet. Ampure’s 2025 announcement describes the High Voltage Power Station as part of the expanded eGSE offering. | Verified public—listing level | Obtain and extract controlled/current spec sheet; define ratings, AC/DC boundary, interfaces, application, certification, option structure, and commercialization status. |

### Battery, mobile, fleet, and energy products

| Product family | Verified public facts | Confidence | Required internal/public gap closure |
|---|---|---|---|
| PosiGuard | Battery-edge monitor for lead-acid and lithium batteries that captures battery data and sends it to PosiLink. Public specs list 24–96 V nominal battery voltage; 18–120 V operating range; 30 mV voltage resolution; 100 mA current resolution; serial, CAN, Bluetooth, and LoRa communications; electrolyte-level capability; 16 MB storage; IP65; −25 to 75 °C operating range; UL 583 and EN1175. | Verified public—product level | Current SKU/variant/sensor configurations; supported BMS/CAN protocols; LoRa band/gateway requirements; data model/API; cloud/service plan; cybersecurity; firmware/update pathway; connector/wiring diagrams. |
| BMID / related tools | Public charger pages and resource titles show BMID recognition/tooling. Public PosiGuard and PosiConnect materials show the product family is used for battery identification/monitoring and configuration. | Verified public—functional level | Current BMID generation lineup, part numbers, compatibility matrix, physical/electrical interfaces, firmware variants, distinction from PosiGuard, service/replacement status. |
| PosiConnect | Mobile companion that connects with PosiGuard via Bluetooth, QR scan, or search. Public page lists live battery status, fault alerts, configurable thresholds, time-range data extraction, firmware updates, and Admin/Technician/Operator roles. App-store content says it is for on-site PosiGuard BMID management and directs centralized fleet management to PosiLink. | Verified public—product level | Supported OS/device versions; authentication/identity lifecycle; role permissions; update security; offline behavior; data export and synchronization; service and support ownership. |
| PosiLink | Identified in PosiGuard and ProCore Edge material as the destination for battery/fleet data, charging activity, battery health, maintenance trends, fleet performance, and alerts. A PosiLink spec sheet is listed in the resource library. | Verified public—family level | Retrieve current product/spec documentation; define product/service boundary, subscription/commercial model, hosting, retention, API/integration, user roles, alerts, cyber/privacy posture, and relation to SkyLink. |
| SkyLink | Cloud-based charger and energy reporting platform. Public page describes real-time charger performance/energy visibility, charge-session records, vehicle-level activity using BMID, charger summaries, remote troubleshooting, manual billing support, and OTA firmware updates. | Verified public—product level | Define relationship to PosiLink; supported chargers/BMID generations; deployment/onboarding; data retention; API/export; security/cyber model; user-role and commercial model. |
| E-Meter | Fleet assessment/optimization tool that captures energy and usage data from an existing electric fleet automatically. Public page states it uses a real-time clock to monitor/record vehicle data and generate reports/analysis; it is described as capable of operating in environments including freezers. | Verified public—product level | Hardware architecture, installation method, measurement variables/accuracy/calibration, interfaces, current generation, connectivity/data export, compatibility, and relationship to PosiGuard/PosiLink/SkyLink. |
| Battery Rx | Public product and resource listings represent it as a current advanced battery-management tool for monitoring, recording, and reporting battery health to extend useful life and improve fleet productivity. | Verified public—listing/family level | Obtain current controlled product sheet; resolve hardware/software/service architecture, relationship to PosiGuard, supported chemistry/data acquisition, SKU/lifecycle state, and interfaces. |

### Accessories and conversion products

| Product / family | Verified public facts | Confidence | Required internal/public gap closure |
|---|---|---|---|
| Extended/custom modular charge cables | Official product pages list 20 ft, 25 ft, and 30 ft modular cable lengths. | Verified public—listing level | Connector families; cable gauge; voltage/current ratings; certification; compatible chargers; custom-order limits. |
| Charger stand kit / cable handler | Official pages list stand/handler solutions for SVS/DVS and ProCore; stated purpose is keeping cables off the floor. | Verified public—listing level | Mechanical variants, mounting requirements, cable/chassis compatibility, orderable kits, safety/environmental ratings. |
| Single-point automatic battery watering | Public accessory listing describes charger-controlled watering at the right time and level. | Verified public—listing level | Supported battery types, water source/interface, required charger option, control/sensor logic, installation/service/safety requirements. |
| DIY Fast Charge Kit | Public listing describes parts and instructions for qualified truck-repair dealers to convert a truck for fast charging. | Verified public—listing level | Eligible vehicle models; qualification requirement; kit contents; connector/BMID configuration; warranty and compliance responsibility; current commercial status. |
| Three-color stack light | Public listing describes green=charged, yellow=charging, red=not charging/fault and requires an Accessory Driver Kit. | Verified public—listing level | Electrical interface; compatible products; mounting options; current SKU; environmental/regulatory rating. |
| Cooling Fan Box | Public accessory listing identifies a thermal-management accessory for ProCore. | Verified public—listing level | Thermal performance, compatible configurations, installation/control requirements, serviceability, current status; verify product-page text for potential copy inconsistency. |

## Connected-product working architecture

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

## Power Designers baseline

Ampure announced acquisition of Power Designers Sibex on 2025-09-02. The announcement states that the acquisition adds industrial charging products and electronics manufacturing, additional power configurations, ISO-certified manufacturing/final assembly in Crystal River, Florida, OEM relationships, and software capabilities in predictive analytics and energy-demand management.

This establishes Power Designers as strategically relevant to the baseline. However, the public evidence collected to date does not enumerate an authoritative current Power Designers-branded product catalog or establish which acquired product/capability elements are currently commercialized under PosiCharge, Power Designers, Ampure, OEM/private-label brands, or another arrangement.

**Status:** In scope; product-family enumeration is an evidence gap, not an inferred product mapping.

## Review and use limits

- Do not convert this artifact directly into external collateral, product commitments, compatibility claims, or compliance assertions.
- Use it to guide evidence acquisition, internal product-master reconciliation, research prioritization, and architecture/gap analysis.
- Add resolved evidence with source, date, exact claim, and reviewer. Preserve conflicts and their disposition history.

## Related

- [[Organizations/PosiCharge]]
- [[Organizations/Power Designers]]
- [[Research/PosiCharge BMID Variants]]
- [[Research/PosiCharge Business Scope and Portfolio]]
- [[Research/PosiCharge Product Comparison Matrix]]
- [[Research/Document Wishlist]]
- [[Research/Knowledge Base Next Steps]]
- [[Research/PosiCharge and Power Designers Public Evidence Register]]
- [[Research/PosiCharge and Power Designers Evidence Gaps and Conflicts]]
