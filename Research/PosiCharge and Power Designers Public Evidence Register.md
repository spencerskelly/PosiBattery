---
type: evidence-register
status: active
scope: public-primary-and-app-store-evidence
prepared: 2026-10-03
reviewer: Director of Engineering
---

# PosiCharge and Power Designers Public Evidence Register

## Use rules

- This register records the exact evidence basis for the public portfolio baseline.
- A source supports only the specific claims listed beside it. Do not generalize a family-level claim into model-, option-, certification-, region-, or SKU-level evidence.
- Public web sources are volatile. Recheck before using a claim externally or making a business/engineering decision.
- Mark contradictions in [[Research/PosiCharge and Power Designers Evidence Gaps and Conflicts]]; do not edit them out of the history.

## Evidence classes

| Class | Definition |
|---|---|
| P1 | Official current product page or official product-resource page |
| P2 | Official company press release or official app-store listing |
| P3 | Public third-party technical/distributor source or indexed manual; useful lead, requires reconciliation |

## Source register

| ID | Class | Source | Accessed | Supported claim(s) | Limits / notes |
|---|---|---|---|---|---|
| `PUB-001` | P1 | [PosiCharge Products](https://posicharge.com/products/) | 2026-10-03 | Public top-level representation of ProCore Edge, DVS300/330/400, MVS400, MVS800, PosiGuard, PosiLink, SVS100, High Voltage Power Station AC/DC, and other portfolio/navigation elements. | Product listing is not proof of exact orderability, variant, rating, or certification. |
| `PUB-002` | P1 | [PosiCharge Product Resources](https://posicharge.com/product-resources/) | 2026-10-03 | Public resource/spec-sheet/manual listing for product families including ProCore Edge, DVS300/330/400, High Voltage Power Station AC/DC, PosiLink, Battery Rx, SVS100, accessories, and installation materials. | Resource title does not substitute for extracting the controlled document revision. |
| `PUB-003` | P1 | [ProCore Edge](https://posicharge.com/products/procore-edge/) | 2026-10-03 | Product family; 24/36/48 V 6–30 kW range; 48/72/80/96 V 9–30 kW range; 96 V Li-ion-only statement; multi-chemistry claims; Bluetooth diagnostics; modularity; listed manuals/tools. | Family-level marketing/specification page; exact SKU and configuration applicability remains unverified. |
| `PUB-004` | P1 | [DVS150](https://posicharge.com/products/dvs150/) | 2026-10-03 | 24–80 V, dual-port MHE charging; 15 kW/port; 300 A/port; 480/600 VAC; NEMA 1; 0.98 PF; up to 92% efficiency; 13 ft cable; 250 event logs; listed BMID/control/protection features. | Exact model/region/certification/connector/chemistry applicability needs controlled evidence. |
| `PUB-005` | P3 | Indexed DVS100/DVS150 public installation manual search result | 2026-10-03 | Indicates DVS100 2 × 10 kW, 16–120 V DC, 200 A max, 480/600 VAC variants. | Not yet linked to a current official DVS100 product page/spec sheet; do not treat as product-master authority. |
| `PUB-006` | P1 | [SVS100](https://posicharge.com/products/svs100/) | 2026-10-03 | GSE charger, 24–80 V, BMID recognition, automatic start/stop, anti-arcing, thermal shutdown, IGBT, NEMA 3R, Euro/Burton options. | Contains a material 10 kW vs. 40 kW documentation conflict; see `PC-PUB-001`. |
| `PUB-007` | P1 | [DVS300/330/400](https://posicharge.com/products/dvs300-330-400/) | 2026-10-03 | 30/33/40 kW GSE family; 24–96 V, dual/single output claim, 480/600 VAC, PF/efficiency, NEMA 3R, BMID, RS-232, power sharing, GBT manual reference. | Need exact model-to-rating/configuration mapping. |
| `PUB-008` | P1 | [MVS400](https://posicharge.com/products/mvs400/) | 2026-10-03 | 40 kW power server, 24–96 V, 250 A dual / 500 A single, RS-232, up to eight simultaneous vehicles, listed power/server attributes. | System topology and component-rating relationship unclear; see `PC-PUB-003`. |
| `PUB-009` | P1 | [MVS800](https://posicharge.com/products/mvs800/) | 2026-10-03 | 80 kW power server, 24–96 V, 250 A dual / 500 A single, RS-232, 95% server efficiency, up to 16 vehicle claim. | Conflicting eight-vehicle and 60 kW power-station content; see `PC-PUB-002` and `PC-PUB-003`. |
| `PUB-010` | P1 | [PosiGuard](https://posicharge.com/products/posiguard/) | 2026-10-03 | Lead-acid/lithium use; current, voltage, electrolyte monitoring; serial/CAN/Bluetooth/LoRa; PosiLink connection; 24–96 V nominal/18–120 V operation; IP65; 16 MB; UL 583; EN1175; operating range and resolution data. | Need SKU, BMS/CAN, LoRa, data/API, cybersecurity, service, and firmware details. |
| `PUB-011` | P1 | [PosiConnect](https://posicharge.com/products/posiconnect/) | 2026-10-03 | Bluetooth/QR/search connection to PosiGuard; live status, faults, thresholds, time-range data extraction, firmware update, Admin/Technician/Operator roles. | Need actual permissions, identity/authentication, supported devices/OS, offline and synchronization design. |
| `PUB-012` | P2 | [Apple App Store: PosiConnect](https://apps.apple.com/us/app/posiconnect/id6748969496) | 2026-10-03 | PosiConnect is on-site PosiGuard BMID management; centralized fleet management is directed to PosiLink. | App-store summary is not an enterprise security or product-architecture specification. |
| `PUB-013` | P1 | [SkyLink](https://posicharge.com/products/skylink/) | 2026-10-03 | Cloud charger/energy reporting; charger performance, energy use, charge-session records, BMID vehicle activity, remote troubleshooting, manual billing, OTA updates. | Need relation to PosiLink, integration/API, security, retention, role, and commercial documentation. |
| `PUB-014` | P1 | [E-Meter](https://posicharge.com/products/e-meter/) | 2026-10-03 | Automatically captures existing electric-fleet energy/usage data; real-time-clock monitoring/recording; reports/analysis; freezer-capable claim. | Need device architecture, measured variables, accuracy, calibration, interface, connectivity, and lifecycle evidence. |
| `PUB-015` | P2 | [Ampure acquisition release: Power Designers Sibex](https://www.ampure.com/press-releases/transom-capital-backed-ampure-acquires-power-designers-sibex) | 2026-10-03 | 2025 acquisition; adds industrial charging products/electronics manufacturing, additional power configurations, ISO-certified Crystal River manufacturing/final assembly, OEM relationships, predictive analytics, and energy-demand-management software. | Does not enumerate an authoritative current standalone Power Designers product catalog or branding/route-to-market mapping. |
| `PUB-016` | P3 | [Alpine Power Systems: SVS100](https://alpinepowersystems.com/products/av-posicharge-svs100) | 2026-10-03 | Third-party listing describes SVS100 as a 10 kW charger. | Useful corroboration for the 10 kW claim but cannot resolve the official-page 40 kW conflict. |
| `PUB-017` | P3 | [Tech Webasto: SVS100 installation](https://www.techwebasto.com/documentation/heater/documentation-techdocs/charging-systems/installation-charg/posicharge-industrial-charging-install/gse-install/svs-100-install.html) | 2026-10-03 | Historical/public installation evidence that the GSE SVS100 operates with a battery-mounted BMID. | Historical manufacturer-hosted documentation; needs current-generation reconciliation. |

## Evidence acquisition queue

Prioritize downloading and extracting the official controlled documents named in `PUB-002` before extending technical claims:

1. SVS100 current spec sheet to resolve `PC-PUB-001`.
2. MVS400/MVS800 current spec sheets and architecture/configuration documents to resolve `PC-PUB-002` and `PC-PUB-003`.
3. High Voltage Power Station AC/DC spec sheets.
4. PosiLink and Battery Rx current spec sheets.
5. ProCore Edge installation, service, spare-parts, anti-arc, BMID, and software-tool documents.
6. DVS100 current official page/spec sheet or controlled catalog.

## Related

- [[Research/PosiCharge and Power Designers Current Portfolio Baseline]]
- [[Research/PosiCharge and Power Designers Evidence Gaps and Conflicts]]
- [[Research/Knowledge Base Next Steps]]
